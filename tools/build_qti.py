"""Build a Canvas-importable QTI 1.2 package from a quiz JSON bank.

Supports both:
  - Universal Question Bank JSON v2.0 (options_template, prompt_template, feedback)
  - Legacy flat quiz JSON (stem, choices[].why)

Usage: python tools/build_qti.py macro/quizzes/ch04_aggregate_output.json [--shuffle]

Output: build/qti/<course>_<stem>_qti.zip (or <name>_qti.zip)
Import in Canvas: Settings > Import Course Content > "QTI .zip file".
Each answer carries diagnostic feedback explaining why it is right or wrong.
"""
import argparse
import json
import os
import random
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def is_universal_v2(bank: dict) -> bool:
    if bank.get("schema_version") == "2.0":
        return True
    qs = bank.get("questions", [])
    return bool(qs and isinstance(qs[0], dict) and "options_template" in qs[0])


def resolve_params(text: str, params: dict) -> str:
    """Substitute {var} template placeholders using parameter defaults for static Canvas QTI."""
    if not text or not params:
        return text
    out = text
    for key, spec in params.items():
        if isinstance(spec, dict):
            if "default" in spec:
                val = spec["default"]
            elif isinstance(spec.get("values"), list) and spec["values"]:
                val = spec["values"][0]
            else:
                continue
        elif isinstance(spec, (int, float, str)):
            val = spec
        else:
            continue
        out = out.replace("{" + key + "}", str(val))
    return out


def normalize_question(q: dict, universal: bool) -> dict:
    """Normalize either schema into {id, stem, choices:[{text, correct, why}]}."""
    if not universal:
        return {
            "id": q.get("id", "?"),
            "stem": q.get("stem", ""),
            "choices": q.get("choices", []),
        }
    params = q.get("parameters") or {}
    choices = []
    for opt in q.get("options_template", []):
        fb = opt.get("feedback") or opt.get("rationale") or ""
        choices.append({
            "text": resolve_params(opt.get("text", ""), params),
            "correct": bool(opt.get("is_correct")),
            "why": resolve_params(fb, params),
        })
    return {
        "id": q.get("id", "?"),
        "stem": resolve_params(q.get("prompt_template", ""), params),
        "choices": choices,
    }


def validate(bank: dict) -> list[str]:
    errors, ids = [], set()
    universal = is_universal_v2(bank)
    for q in bank.get("questions", []):
        nq = normalize_question(q, universal)
        qid = nq["id"]
        if qid in ids:
            errors.append(f"{qid}: duplicate id")
        ids.add(qid)
        if not nq["stem"]:
            errors.append(f"{qid}: missing question stem/prompt_template")
        if not universal:
            for field in ("outcome", "bloom", "difficulty"):
                if not q.get(field):
                    errors.append(f"{qid}: missing {field}")
        else:
            if q.get("tier") not in (1, 2, 3, 4):
                errors.append(f"{qid}: missing/invalid tier (1..4)")
            if not q.get("clo_alignment"):
                errors.append(f"{qid}: missing clo_alignment")
        choices = nq["choices"]
        correct = [c for c in choices if c.get("correct")]
        if len(correct) != 1:
            errors.append(f"{qid}: needs exactly one correct choice, has {len(correct)}")
        if len(choices) < 3:
            errors.append(f"{qid}: needs at least 3 choices")
        for c in choices:
            if not str(c.get("why", "")).strip():
                errors.append(f"{qid}: choice missing feedback/why: {c.get('text', '')[:40]}")
        texts = [c.get("text") for c in choices]
        if len(set(texts)) != len(texts):
            errors.append(f"{qid}: duplicate choice text")
    return errors


def to_html(text: str) -> str:
    """Minimal markup: **bold**, $$display$$ and $inline$ -> Canvas MathJax delimiters."""
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Protect display math first, then inline math
    text = re.sub(r"\$\$(.+?)\$\$", r"\\[\1\\]", text, flags=re.DOTALL)
    text = re.sub(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$", r"\\(\1\\)", text)
    return text


def mattext(text: str) -> str:
    return f'<mattext texttype="text/html">{escape(to_html(text))}</mattext>'


def build_item(nq: dict, points: float, n: int, shuffle: bool = False) -> str:
    choices = list(nq["choices"])
    if shuffle:
        rng = random.Random(nq["id"])
        rng.shuffle(choices)
    ids = [str(1000 + n * 10 + i) for i in range(len(choices))]
    out = [f'<item ident="{escape(nq["id"])}" title="{escape(nq["id"])}">']
    out.append("<itemmetadata><qtimetadata>")
    for k, v in (
        ("question_type", "multiple_choice_question"),
        ("points_possible", f"{points:.1f}"),
        ("original_answer_ids", ",".join(ids)),
    ):
        out.append(f"<qtimetadatafield><fieldlabel>{k}</fieldlabel><fieldentry>{v}</fieldentry></qtimetadatafield>")
    out.append("</qtimetadata></itemmetadata>")
    out.append(f"<presentation><material>{mattext(nq['stem'])}</material>")
    out.append('<response_lid ident="response1" rcardinality="Single"><render_choice>')
    for cid, c in zip(ids, choices):
        out.append(f'<response_label ident="{cid}"><material>{mattext(c["text"])}</material></response_label>')
    out.append("</render_choice></response_lid></presentation>")
    out.append('<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>')
    for cid in ids:
        out.append(
            f'<respcondition continue="Yes"><conditionvar><varequal respident="response1">{cid}</varequal></conditionvar>'
            f'<displayfeedback feedbacktype="Response" linkrefid="{cid}_fb"/></respcondition>'
        )
    correct_id = next(cid for cid, c in zip(ids, choices) if c["correct"])
    out.append(
        f'<respcondition continue="No"><conditionvar><varequal respident="response1">{correct_id}</varequal></conditionvar>'
        '<setvar action="Set" varname="SCORE">100</setvar></respcondition>'
    )
    out.append("</resprocessing>")
    for cid, c in zip(ids, choices):
        why = str(c["why"]).strip()
        if c["correct"] and not why.lower().startswith("correct"):
            why = "Correct. " + why
        elif not c["correct"] and not (why.lower().startswith(("not quite", "incorrect", "diagnostic", "misconception"))):
            why = "Not quite. " + why
        out.append(
            f'<itemfeedback ident="{cid}_fb"><flow_mat><material>{mattext(why)}</material></flow_mat></itemfeedback>'
        )
    out.append("</item>")
    return "".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("bank")
    ap.add_argument("--shuffle", action="store_true", help="deterministically shuffle answer choices per question ID")
    args = ap.parse_args()

    bank_path = Path(args.bank).resolve()
    with open(bank_path, encoding="utf-8") as f:
        bank = json.load(f)
    errors = validate(bank)
    if errors:
        sys.exit("Validation failed:\n  " + "\n  ".join(errors))

    universal = is_universal_v2(bank)
    stem = bank_path.stem
    # Prefix with course folder (micro_ or macro_) when present to prevent collisions
    parent_course = bank_path.parent.parent.name
    name = f"{parent_course}_{stem}" if parent_course in ("micro", "macro") else stem
    quiz_title = bank.get("quiz_title") or bank.get("title") or name
    points = float(bank.get("points_per_question", 1))
    items = "".join(
        build_item(normalize_question(q, universal), points, i, shuffle=args.shuffle)
        for i, q in enumerate(bank["questions"], 1)
    )
    assessment = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">'
        f'<assessment ident="{escape(name)}" title="{escape(quiz_title)}">'
        '<qtimetadata><qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>1</fieldentry></qtimetadatafield></qtimetadata>'
        f'<section ident="root_section">{items}</section></assessment></questestinterop>'
    )
    manifest = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        f'<manifest identifier="{escape(name)}_manifest" xmlns="http://www.imsglobal.org/xsd/imscp_v1p1" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata>'
        '<organizations/><resources>'
        f'<resource identifier="{escape(name)}_res" type="imsqti_xmlv1p2" href="{escape(name)}.xml"><file href="{escape(name)}.xml"/></resource>'
        '</resources></manifest>'
    )
    out_dir = os.path.join(ROOT, "build", "qti")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"{name}_qti.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", manifest)
        z.writestr(f"{name}.xml", assessment)
    print(f"Wrote {out} ({len(bank['questions'])} questions)")


if __name__ == "__main__":
    main()
