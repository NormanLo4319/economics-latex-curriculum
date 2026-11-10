#!/usr/bin/env python3
"""
Convert LaTeX textbook chapters to Quarto (.qmd) format.
Handles callout transformation, math formatting, and file mapping.
"""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent


def latex_to_qmd(src_file: Path, dest_file: Path):
    with open(src_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Map custom environments to Quarto callouts
    content = re.sub(
        r"\\begin\{coreprinciple\}(.*?)\\boxheader\{.*?\}\{(.*?)\}",
        r'::: {.callout-note appearance="simple" title="\2"}\n',
        content,
        flags=re.DOTALL,
    )
    content = re.sub(r"\\end\{coreprinciple\}", r":::\n", content)

    content = re.sub(
        r"\\begin\{examplecase\}\{(.*?)\}",
        r'::: {.callout-tip appearance="simple" title="\1"}\n',
        content,
    )
    content = re.sub(r"\\end\{examplecase\}", r":::\n", content)

    content = re.sub(
        r"\\begin\{takeaways\}",
        r'::: {.callout-important appearance="simple" title="Key Takeaways"}\n',
        content,
    )
    content = re.sub(r"\\end\{takeaways\}", r":::\n", content)

    # 2. Convert standard LaTeX constructs to Markdown via Pandoc if available,
    # or fallback to regex extraction
    try:
        process = subprocess.Popen(
            ["pandoc", "-f", "latex", "-t", "markdown+raw_tex", "--wrap=none"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        markdown_out, _ = process.communicate(input=content)
    except FileNotFoundError:
        # Fallback if pandoc is not locally in PATH
        # Strip document wrapper, preamble, and title blocks
        body = re.search(r"\\begin\{document\}(.*?)\\end\{document\}", content, re.DOTALL)
        body_text = body.group(1) if body else content
        body_text = re.sub(r"\\maketitle", "", body_text)
        body_text = re.sub(r"\\tableofcontents", "", body_text)
        body_text = re.sub(r"\\thispagestyle\{.*?\}", "", body_text)
        body_text = re.sub(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", r"> \1\n", body_text, flags=re.DOTALL)
        body_text = re.sub(r"\\section\{(.*?)\}", r"## \1", body_text)
        body_text = re.sub(r"\\subsection\{(.*?)\}", r"### \1", body_text)
        body_text = re.sub(r"\\subsubsection\{(.*?)\}", r"#### \1", body_text)
        markdown_out = body_text

    dest_file.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(markdown_out.strip() + "\n")

    print(f"[OK] Converted {src_file.name} -> {dest_file.name}")


def main():
    mappings = [
        (ROOT / "micro" / "chapters", ROOT / "web_books" / "microeconomics"),
        (ROOT / "macro" / "chapters", ROOT / "web_books" / "macroeconomics"),
    ]

    for src_dir, target_dir in mappings:
        if not src_dir.exists():
            continue
        for tex_path in sorted(src_dir.glob("*.tex")):
            qmd_path = target_dir / (tex_path.stem + ".qmd")
            latex_to_qmd(tex_path, qmd_path)


if __name__ == "__main__":
    main()
