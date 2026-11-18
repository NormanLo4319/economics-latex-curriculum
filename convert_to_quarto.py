#!/usr/bin/env python3
"""Generate Quarto chapters and SVG figures from canonical LaTeX sources."""

import re
import sys
from pathlib import Path

import sync_readings_to_tex

ROOT = Path(__file__).resolve().parent
MAPPINGS = (
    (ROOT / "micro" / "chapters", ROOT / "web_books" / "microeconomics"),
    (ROOT / "macro" / "chapters", ROOT / "web_books" / "macroeconomics"),
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


def main(chapter1_only: bool = False) -> int:
    for src_dir, target_dir in MAPPINGS:
        if not src_dir.exists():
            continue
        for tex_path in sorted(src_dir.glob("*.tex")):
            if chapter1_only and tex_path.stem != "ch01_principles":
                continue
            qmd_path = target_dir / (tex_path.stem + ".qmd")
            latex_to_qmd(tex_path, qmd_path)
    return 0


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if arguments not in ([], ["--chapter1-only"]):
        raise SystemExit("Usage: python convert_to_quarto.py [--chapter1-only]")
    raise SystemExit(main(chapter1_only=arguments == ["--chapter1-only"]))
