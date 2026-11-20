#!/usr/bin/env python3
"""
Migrate local economics-latex-curriculum & media_production files to the
canonical 12-chapter Macroeconomics SSOT sequence (2026-11-18).

Actions:
1. Archives old Chapter 12 Open-Economy Macroeconomics assets into archive/open_economy_ch12/.
2. Shifts existing Chapters 6..11 -> Chapters 7..12 across .tex, .qmd, .json, and .pptx files.
3. Updates slide headers/footers on existing PPTX decks (Ch 6 -> Ch 7, Ch 10 -> Ch 11) if python-pptx is installed.
"""

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ARCHIVE_PATTERNS = [
    "*ch12_open_economy*",
    "*Ch12_Open_Economy*",
    "*open_economy_macroeconomics*",
]

RENAME_MAP = [
    ("ch11_monetary_policy", "ch12_monetary_policy"),
    ("ch10_money_banking_fed", "ch11_money_banking_fed"),
    ("ch10_money_banking", "ch11_money_banking_fed"),
    ("ch09_fiscal_policy", "ch10_fiscal_policy"),
    ("ch08_aggregate_demand_aggregate_supply", "ch09_aggregate_demand_aggregate_supply"),
    ("ch07_aggregate_expenditure_multiplier", "ch08_aggregate_expenditure_multiplier"),
    ("ch06_savings_investment_financial_system", "ch07_savings_investment_financial_system"),
    ("ch06_savings_investment", "ch07_savings_investment_financial_system"),
]


def archive_open_economy():
    archive_dir = ROOT / "archive" / "open_economy_ch12"
    archive_dir.mkdir(parents=True, exist_ok=True)
    for pattern in ARCHIVE_PATTERNS:
        for path in ROOT.rglob(pattern):
            if "archive" in path.parts or not path.is_file():
                continue
            dest = archive_dir / path.name
            shutil.move(str(path), str(dest))
            print(f"[ARCHIVED] {path.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")


def shift_filenames():
    for old_stem, new_stem in RENAME_MAP:
        for path in sorted(ROOT.rglob(f"*{old_stem}*")):
            if "archive" in path.parts or not path.is_file():
                continue
            new_name = path.name.replace(old_stem, new_stem)
            dest = path.with_name(new_name)
            if not dest.exists():
                path.rename(dest)
                print(f"[RENAMED] {path.name} -> {dest.name}")


def relabel_pptx_decks():
    try:
        from pptx import Presentation
    except ImportError:
        print("[SKIP] python-pptx not installed; skipping PPTX text replacement.")
        return

    replacements = [
        ("CHAPTER 6 • MODULE 6.", "CHAPTER 7 • MODULE 7."),
        ("MODULE 6.", "MODULE 7."),
        ("Module 6.", "Module 7."),
        ("CH. 6 FIGURE", "CH. 7 FIGURE"),
        ("CHAPTER 10:", "CHAPTER 11:"),
        ("MODULE 10.", "MODULE 11."),
        ("Module 10.", "Module 11."),
        ("SSOT Ch. 10.", "SSOT Ch. 11."),
    ]

    for pptx_path in ROOT.rglob("*.pptx"):
        if "archive" in pptx_path.parts:
            continue
        prs = Presentation(str(pptx_path))
        changed = False
        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        orig = run.text
                        updated = orig
                        for old, new in replacements:
                            updated = updated.replace(old, new)
                        if updated != orig:
                            run.text = updated
                            changed = True
        if changed:
            prs.save(str(pptx_path))
            print(f"[UPDATED PPTX] {pptx_path.name}")


if __name__ == "__main__":
    archive_open_economy()
    shift_filenames()
    relabel_pptx_decks()
    print("[DONE] Macroeconomics SSOT migration complete.")
