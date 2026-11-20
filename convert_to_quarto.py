#!/usr/bin/env python3
"""Generate Quarto chapters and SVG figures from canonical LaTeX sources."""

import argparse
import re
import sys
from pathlib import Path

import sync_readings_to_tex

ROOT = Path(__file__).resolve().parent
MAPPINGS = (
    ("micro", ROOT / "micro" / "chapters", ROOT / "web_books" / "microeconomics"),
    ("macro", ROOT / "macro" / "chapters", ROOT / "web_books" / "macroeconomics"),
)


def title_from_tex(content: str, fallback: str) -> str:
    match = re.search(
        r"\\title\{.*?\\color\{[^}]+\}\s*(.*?)\}\s*\\author",
        content,
        flags=re.DOTALL,
    )
    if match:
        return match.group(1).replace(r"\&", "&").strip()
    return fallback.replace("_", " ").title()


def latex_to_qmd(src_file: Path, dest_file: Path) -> None:
    content = src_file.read_text(encoding="utf-8")
    title = title_from_tex(content, src_file.stem)
    qmd = sync_readings_to_tex.tex_to_qmd(content, title, dest_file.parent)

    dest_file.parent.mkdir(parents=True, exist_ok=True)
    dest_file.write_text(qmd, encoding="utf-8")
    print(f"[OK] Converted {src_file.name} -> {dest_file.name}")


def main(chapter1_only: bool = False, chapters: list[str] | None = None) -> int:
    targets = set(chapters or [])
    matched = set()
    for course, src_dir, target_dir in MAPPINGS:
        if not src_dir.exists():
            continue
        for tex_path in sorted(src_dir.glob("*.tex")):
            slug = f"{course}/{tex_path.stem}"
            if chapter1_only and tex_path.stem != "ch01_principles":
                continue
            if targets and slug not in targets and tex_path.stem not in targets:
                continue
            matched.add(slug)
            matched.add(tex_path.stem)
            qmd_path = target_dir / (tex_path.stem + ".qmd")
            latex_to_qmd(tex_path, qmd_path)
    missing = [t for t in targets if t not in matched]
    if missing:
        raise SystemExit(f"Chapter(s) not found: {', '.join(missing)}")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert canonical LaTeX chapters to Quarto .qmd files.")
    parser.add_argument("--chapter1-only", action="store_true", help="Convert only Micro and Macro Chapter 1.")
    parser.add_argument(
        "--chapter",
        action="append",
        dest="chapters",
        help="Target specific chapter(s), e.g. --chapter micro/ch06_costs_production",
    )
    args = parser.parse_args()
    raise SystemExit(main(chapter1_only=args.chapter1_only, chapters=args.chapters))
