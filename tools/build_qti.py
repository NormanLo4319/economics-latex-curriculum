"""Build a Canvas-importable QTI 1.2 package from a quiz JSON bank.

Usage: python tools/build_qti.py micro/quizzes/ch03_quiz.json [--shuffle]

Output: build/qti/<name>_qti.zip
Import in Canvas: Settings > Import Course Content > "QTI .zip file".
Each answer carries feedback explaining why it is right or wrong.
"""
import argparse
import json
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def validate(bank):
    errors, ids = [], set()
    for q in bank["questions"]:
        qid = q.get("id", "?")
        if qid in ids:
            errors.append(f"{qid}: duplicate id")
        ids.add(qid)
        for field in ("outcome", "bloom", "difficulty", "stem", "choices"):
            if not q.get(field):
                errors.append(f"{qid}: missing {field}")
        correct = [c for c in q.get("choices", []) if c.get("correct")]
        if len(correct) != 1:
            errors.append(f"{qid}: needs exactly one correct choice, has {len(correct)}")
        if len(q.get("choices", [])) < 3:
            errors.append(f"{qid}: needs at least 3 choices")
        for c in q.get("choices", []):
            if not c.get("why"):
                errors.append(f"{qid}: choice missing 'why': {c.get('text', '')[:40]}")
        texts = [c.get("text") for c in q.get("choices", [])]
        if len(set(texts)) != len(texts):
            errors.append(f"{qid}: duplicate choice text")
    return errors


def to_html(text):
    """Minimal markup: **bold** and $math$ -> \\(math\\) (Canvas MathJax)."""
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\$(.+?)\$", r"\\(\1\\)", text)
    return text


def mattext(text):
    return f'<mattext texttype="text/html">{escape(to_html(text))}</mattext>'


def build_item(q, points, n):
    choices = q["choices"]
    ids = [str(1000 + n * 10 + i) for i in range(len(choices))]
    out = [f'<item ident="{q["id"]}" title="{escape(q["id"])}">']
    out.append("<itemmetadata><qtimetadata>")
    for k, v in (
        ("question_type", "multiple_choice_question"),
        ("points_possible", f"{points:.1f}"),
        ("original_answer_ids", ",".join(ids)),
    ):
        out.append(f"<qtimetadatafield><fieldlabel>{k}</fieldlabel><fieldentry>{v}</fieldentry></qtimetadatafield>")
    out.append("</qtimetadata></itemmetadata>")
    out.append(f"<presentation><material>{mattext(q['stem'])}</material>")
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
        prefix = "Correct. " if c["correct"] else "Not quite. "
        out.append(
            f'<itemfeedback ident="{cid}_fb"><flow_mat><material>{mattext(prefix + c["why"])}</material></flow_mat></itemfeedback>'
        )
    out.append("</item>")
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bank")
    ap.add_argument("--shuffle", action="store_true", help="shuffle answers in Canvas (default off)")
    args = ap.parse_args()

    with open(args.bank, encoding="utf-8") as f:
        bank = json.load(f)
    errors = validate(bank)
    if errors:
        sys.exit("Validation failed:\n  " + "\n  ".join(errors))

    name = os.path.splitext(os.path.basename(args.bank))[0]
    points = float(bank.get("points_per_question", 1))
    items = "".join(build_item(q, points, i) for i, q in enumerate(bank["questions"], 1))
    assessment = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">'
        f'<assessment ident="{name}" title="{escape(bank["quiz_title"])}">'
        '<qtimetadata><qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>1</fieldentry></qtimetadatafield></qtimetadata>'
        f'<section ident="root_section">{items}</section></assessment></questestinterop>'
    )
    manifest = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        f'<manifest identifier="{name}_manifest" xmlns="http://www.imsglobal.org/xsd/imscp_v1p1" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata>'
        '<organizations/><resources>'
        f'<resource identifier="{name}_res" type="imsqti_xmlv1p2" href="{name}.xml"><file href="{name}.xml"/></resource>'
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
