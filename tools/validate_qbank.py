#!/usr/bin/env python3
"""Validate Universal Question Bank JSON (v2.0) files and report curriculum progress.

Usage:
  python tools/validate_qbank.py macro/quizzes/ch04_aggregate_output.json [--strict]
  python tools/validate_qbank.py --all
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CANONICAL_TAXONOMY = {
    1: "Tier 1: Conceptual / Definitional",
    2: "Tier 2: Graphical / Curve Shift Interpretation",
    3: "Tier 3: Quantitative / Step-by-Step Calculation",
    4: "Tier 4: Critical Thinking / Empirical Policy Application",
}

REQUIRED_TOP_LEVEL = (
    "schema_version",
    "course",
    "chapter_id",
    "file_stem",
    "title",
    "benchmark",
    "seeding_formula",
    "questions_count",
    "tier_distribution",
    "questions",
)

VARIANT_RE = re.compile(r"\(Variant\s+\d+\)", re.IGNORECASE)


def validate_bank(path: Path, strict: bool = False) -> tuple[list[str], dict]:
    """Return (errors, stats) for a question bank JSON file."""
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"JSON parse error: {exc}"], {"count": 0, "tiers": {}, "is_v2": False}

    if not isinstance(data, dict):
        return ["Top-level JSON must be an object."], {"count": 0, "tiers": {}, "is_v2": False}

    for field in REQUIRED_TOP_LEVEL:
        if field not in data:
            errors.append(f"Missing top-level field '{field}'")

    if data.get("schema_version") != "2.0":
        errors.append(f"Expected schema_version '2.0', got {data.get('schema_version')!r}")

    if data.get("file_stem") and data.get("file_stem") != path.stem:
        errors.append(f"file_stem '{data.get('file_stem')}' does not match filename '{path.stem}'")

    questions = data.get("questions", [])
    if not isinstance(questions, list):
        errors.append("'questions' must be a list")
        return errors, {"count": 0, "tiers": {}, "is_v2": False}

    if data.get("questions_count") != len(questions):
        errors.append(
            f"questions_count ({data.get('questions_count')}) != len(questions) ({len(questions)})"
        )

    seen_ids: set[str] = set()
    seen_prompts: set[str] = set()
    tier_counts: Counter[int] = Counter()

    for idx, q in enumerate(questions, 1):
        qid = q.get("id") or f"index_{idx}"
        if qid in seen_ids:
            errors.append(f"{qid}: duplicate question id")
        seen_ids.add(qid)

        tier = q.get("tier")
        if tier not in CANONICAL_TAXONOMY:
            errors.append(f"{qid}: invalid or missing integer 'tier' (expected 1..4, got {tier!r})")
        else:
            tier_counts[tier] += 1
            if q.get("taxonomy") != CANONICAL_TAXONOMY[tier]:
                errors.append(
                    f"{qid}: taxonomy {q.get('taxonomy')!r} != canonical {CANONICAL_TAXONOMY[tier]!r}"
                )

        for req in ("chapter", "topic", "title", "prompt_template", "evaluation", "hints", "options_template"):
            if req not in q or q[req] in (None, "", []):
                errors.append(f"{qid}: missing or empty '{req}'")

        clos = q.get("clo_alignment")
        if not isinstance(clos, list) or not clos:
            errors.append(f"{qid}: clo_alignment must be a non-empty list")

        prompt = str(q.get("prompt_template", "")).strip()
        if prompt:
            if VARIANT_RE.search(prompt):
                errors.append(f"{qid}: contains legacy '(Variant N)' placeholder")
            if prompt in seen_prompts:
                errors.append(f"{qid}: duplicate prompt_template text")
            seen_prompts.add(prompt)

        hints = q.get("hints", [])
        if not isinstance(hints, list) or len(hints) != 2:
            errors.append(f"{qid}: expected exactly 2 progressive hints, got {len(hints) if isinstance(hints, list) else type(hints).__name__}")
        else:
            for h_idx, h in enumerate(hints, 1):
                if not isinstance(h, dict) or h.get("tier") != h_idx or not str(h.get("text", "")).strip():
                    errors.append(f"{qid}: hint {h_idx} must be {{'tier': {h_idx}, 'text': '...'}}")

        opts = q.get("options_template", [])
        if not isinstance(opts, list) or len(opts) != 4:
            errors.append(f"{qid}: expected exactly 4 options in options_template, got {len(opts) if isinstance(opts, list) else 0}")
        else:
            correct_opts = [o for o in opts if o.get("is_correct") is True]
            if len(correct_opts) != 1:
                errors.append(f"{qid}: expected exactly 1 correct option, got {len(correct_opts)}")
            opt_ids = [o.get("id") for o in opts]
            if len(set(opt_ids)) != len(opt_ids) or any(not oid for oid in opt_ids):
                errors.append(f"{qid}: option ids must be unique and non-empty")
            opt_texts = [str(o.get("text", "")).strip() for o in opts]
            if len(set(opt_texts)) != len(opt_texts) or any(not t for t in opt_texts):
                errors.append(f"{qid}: option texts must be unique and non-empty")
            for o in opts:
                if VARIANT_RE.search(str(o.get("text", ""))):
                    errors.append(f"{qid}: option contains legacy '(Variant N)' placeholder")
                if not str(o.get("feedback", "")).strip():
                    errors.append(f"{qid}: option {o.get('id')!r} missing diagnostic 'feedback'")

            ev = q.get("evaluation", {})
            if isinstance(ev, dict):
                if ev.get("mode") != "multiple_choice":
                    errors.append(f"{qid}: evaluation.mode must be 'multiple_choice', got {ev.get('mode')!r}")
                corr_id = ev.get("correct_option_id")
                if len(correct_opts) == 1 and corr_id != correct_opts[0].get("id"):
                    errors.append(
                        f"{qid}: evaluation.correct_option_id ({corr_id!r}) != correct option id ({correct_opts[0].get('id')!r})"
                    )

    td = data.get("tier_distribution", {})
    expected_td = {f"tier_{t}": tier_counts.get(t, 0) for t in (1, 2, 3, 4)}
    if td != expected_td:
        errors.append(f"tier_distribution {td} != computed {expected_td}")

    if strict:
        if len(questions) != 50:
            errors.append(f"strict: expected 50 questions, got {len(questions)}")
        for t in (1, 2, 3, 4):
            c = tier_counts.get(t, 0)
            if not (10 <= c <= 15):
                errors.append(f"strict: tier_{t} count ({c}) outside balanced range [10, 15]")

    stats = {
        "count": len(questions),
        "tiers": {t: tier_counts.get(t, 0) for t in (1, 2, 3, 4)},
        "is_v2": data.get("schema_version") == "2.0",
    }
    return errors, stats


def print_dashboard() -> int:
    """Print complete 26-chapter reading + quiz status dashboard."""
    total_ready = 0
    total_chapters = 0
    for course in ("micro", "macro"):
        print(f"\n=== {course.upper()} CURRICULUM STATUS ===")
        print(f"{'Chapter Stem':45s} | {'TeX Lines':>9s} | {'Quiz Status':28s} | {'Tiers (1/2/3/4)'}")
        print("-" * 108)
        chapters = sorted((ROOT / course / "chapters").glob("*.tex"))
        for ch in chapters:
            total_chapters += 1
            tex_lines = len(ch.read_text(encoding="utf-8", errors="ignore").splitlines())
            qpath = ROOT / course / "quizzes" / f"{ch.stem}.json"
            if not qpath.exists():
                status = "MISSING (0/50)"
                tstr = "-"
            else:
                errs_strict, stats = validate_bank(qpath, strict=True)
                errs_schema, _ = validate_bank(qpath, strict=False)
                t = stats["tiers"]
                tstr = f"{t.get(1,0)}/{t.get(2,0)}/{t.get(3,0)}/{t.get(4,0)}"
                if not errs_strict:
                    status = f"READY v2 ({stats['count']}/50)"
                    total_ready += 1
                elif not errs_schema:
                    status = f"PARTIAL v2 ({stats['count']}/50)"
                elif stats["is_v2"]:
                    status = f"V2 ERRORS ({len(errs_schema)} errs)"
                else:
                    status = f"LEGACY ({stats['count']}Q, needs v2)"
            print(f"{ch.stem:45s} | {tex_lines:9d} | {status:28s} | {tstr}")
    print(f"\nProduction-ready v2.0 50-question banks: {total_ready}/{total_chapters}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate Universal Question Bank JSON (v2.0) files.")
    ap.add_argument("bank", nargs="?", help="Path to a single quiz JSON file.")
    ap.add_argument("--strict", action="store_true", help="Require 50 questions and balanced 4-tier distribution.")
    ap.add_argument("--all", action="store_true", help="Print status dashboard across all 26 chapters.")
    args = ap.parse_args()

    if args.all:
        return print_dashboard()
    if not args.bank:
        ap.error("Provide a quiz JSON path or --all.")

    path = Path(args.bank)
    errors, stats = validate_bank(path, strict=args.strict)
    if errors:
        print(f"FAIL {path} ({len(errors)} error(s)):")
        for e in errors[:40]:
            print(f"  - {e}")
        if len(errors) > 40:
            print(f"  ... and {len(errors) - 40} more")
        return 1
    t = stats["tiers"]
    print(f"OK   {path} ({stats['count']} questions | T1={t[1]} T2={t[2]} T3={t[3]} T4={t[4]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
