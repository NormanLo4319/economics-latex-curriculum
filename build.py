#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
OUTPUT_DIR = ROOT / "dist"

COURSES = {
    "micro": ROOT / "micro" / "chapters",
    "macro": ROOT / "macro" / "chapters",
}


def compile_file(tex_path: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pdflatex",
        "-halt-on-error",
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        tex_path.name,
    ]

    print(f"--> Compiling {tex_path.name}...")
    # Run two passes to resolve labels, citations, and TOC entries
    for pass_num in (1, 2):
        result = subprocess.run(
            cmd, cwd=tex_path.parent, capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"[ERROR] Failed pass {pass_num} on {tex_path.name}")
            print(result.stdout[-1500:])
            return False
    print(f"[OK] {tex_path.stem}.pdf generated in {output_dir.relative_to(ROOT)}")
    return True


def clean():
    extensions = {
        "*.aux",
        "*.log",
        "*.out",
        "*.toc",
        "*.synctex.gz",
        "*.fls",
        "*.fdb_latexmk",
    }
    for ext in extensions:
        for f in ROOT.rglob(ext):
            f.unlink()
    print("[OK] Auxiliary files removed.")


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "all"

    if target == "clean":
        clean()
        return

    targets = ["micro", "macro"] if target == "all" else [target]

    for t in targets:
        if t not in COURSES:
            print(f"Unknown target: {t}. Use 'all', 'micro', 'macro', or 'clean'.")
            sys.exit(1)

        ch_dir = COURSES[t]
        out_dir = OUTPUT_DIR / t
        for tex_file in sorted(ch_dir.glob("*.tex")):
            if not compile_file(tex_file, out_dir):
                sys.exit(1)


if __name__ == "__main__":
    main()