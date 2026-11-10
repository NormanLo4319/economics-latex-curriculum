#!/usr/bin/env python3
"""Synchronize canonical LaTeX chapters and Quarto books using strict UTF-8."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent
COURSES = {
    "micro": {
        "tex_dir": ROOT / "micro" / "chapters",
        "qmd_dir": ROOT / "web_books" / "microeconomics",
        "book_title": "Principles of Microeconomics",
        "output_dir": "../../dist/web/micro",
        "groups": (
            ("Foundations of Market Analysis", 1, 5),
            ("Firm Behavior & Market Structures", 6, 9),
            ("Market Failures & Factor Markets", 10, 14),
        ),
    },
    "macro": {
        "tex_dir": ROOT / "macro" / "chapters",
        "qmd_dir": ROOT / "web_books" / "macroeconomics",
        "book_title": "Principles of Macroeconomics",
        "output_dir": "../../dist/web/macro",
        "groups": (
            ("Macroeconomic Foundations & Measurement", 1, 5),
            ("Savings, Investment & Financial Systems", 6, 6),
            ("Short-Run Fluctuations & Stabilization", 7, 12),
        ),
    },
}

MACRO_ALIAS = Path("macro") / "chapters" / "ch02_ppf.tex"


def read_utf8(path: Path) -> str:
    with path.open("r", encoding="utf-8", errors="strict") as source:
        return source.read()


def validate_utf8(text: str, description: str) -> None:
    try:
        text.encode("utf-8", errors="strict")
    except UnicodeEncodeError as error:
        raise ValueError(f"{description} is not valid UTF-8 text: {error}") from error


def write_utf8(path: Path, text: str) -> None:
    validate_utf8(text, str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", errors="strict", newline="\n") as output:
        output.write(text)


def load_seed_module():
    try:
        import sync_readings_to_tex
    except ImportError as error:
        raise RuntimeError("Required source file sync_readings_to_tex.py is unavailable") from error

    return sync_readings_to_tex


def title_from_tex(tex: str, fallback: str) -> str:
    match = re.search(
        r"\\title\{.*?\\color\{[^}]+\}\s*(.*?)\}\s*\\author",
        tex,
        flags=re.DOTALL,
    )
    if match:
        return match.group(1).replace(r"\&", "&").strip()
    return fallback.replace("_", " ").title()


def strip_title_block(tex: str) -> str:
    return re.sub(
        r"\\title\{.*?\\author\{.*?\\date\{.*?\\maketitle",
        "",
        tex,
        count=1,
        flags=re.DOTALL,
    )


def chapter_number(stem: str) -> int:
    match = re.match(r"ch(\d+)_", stem)
    if not match:
        raise ValueError(f"Chapter filename must begin with chNN_: {stem}")
    return int(match.group(1))


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_quarto_config(course: str, chapter_stems: List[str]) -> str:
    settings = COURSES[course]
    lines = [
        "project:",
        "  type: book",
        f"  output-dir: {settings['output_dir']}",
        "",
        "book:",
        f"  title: {yaml_quote(settings['book_title'])}",
        '  subtitle: "An Institutional and Social Science Perspective"',
        '  author: "Norman Lo"',
        '  date: "2026"',
        "  search: true",
        "  sidebar:",
        '    style: "docked"',
        "    search: true",
        "    collapse-level: 1",
        "  page-navigation: true",
        "  chapters:",
        "    - index.qmd",
    ]

    grouped = set()
    for group_title, first, last in settings["groups"]:
        members = [stem for stem in chapter_stems if first <= chapter_number(stem) <= last]
        if not members:
            continue
        grouped.update(members)
        lines.extend((f"    - part: {yaml_quote(group_title)}", "      chapters:"))
        lines.extend(f"        - {stem}.qmd" for stem in members)

    remaining = [stem for stem in chapter_stems if stem not in grouped]
    if remaining:
        lines.extend(("    - part: \"Additional Chapters\"", "      chapters:"))
        lines.extend(f"        - {stem}.qmd" for stem in remaining)

    lines.extend(
        (
            "",
            "format:",
            "  html:",
            "    theme:",
            "      light: cosmo",
            "      dark: darkly",
            "    toc: true",
            "    toc-depth: 3",
            "    number-sections: true",
            "    code-copy: true",
            "    html-math-method: mathjax",
            "",
        )
    )
    return "\n".join(lines)


def qmd_index(course: str) -> str:
    settings = COURSES[course]
    if course == "micro":
        description = (
            "This textbook covers scarcity, consumer choice, firm behavior, market structures, "
            "market failures, and public policy."
        )
        reference = "Eric Chiang, *Microeconomics: Principles for a Changing World*, and UC Berkeley Econ 1."
    else:
        description = (
            "This textbook covers macroeconomic measurement, growth, financial systems, "
            "business cycles, stabilization policy, and international linkages."
        )
        reference = "Paul Krugman and Robin Wells, *Macroeconomics*, and UC Berkeley Econ 2."
    return (
        "# Preface {.unnumbered}\n\n"
        f"Welcome to **{settings['book_title']}: An Institutional and Social Science Perspective**.\n\n"
        f"{description} The readings are original course materials aligned by topic with {reference}\n"
    )


def normalize_callout_fences(qmd: str) -> str:
    frontmatter = re.match(r"\A---\n.*?\n---\n", qmd, flags=re.DOTALL)
    if not frontmatter:
        raise ValueError("Generated QMD is missing YAML front matter")

    lines = qmd[frontmatter.end():].splitlines()
    normalized: List[str] = []
    open_callouts = 0
    for line in lines:
        line = line.replace(r"\:::", ":::")
        opening = re.search(r":::\s*(\{[^}]*\})", line)
        if opening:
            preceding = line[:opening.start()].rstrip()
            if preceding:
                normalized.append(preceding)
            if normalized and normalized[-1].strip():
                normalized.append("")
            normalized.append(f"::: {opening.group(1)}")
            open_callouts += 1
            continue

        closing = re.search(r":::", line)
        if closing:
            preceding = line[:closing.start()].rstrip()
            trailing = line[closing.end():].strip()
            if preceding:
                normalized.append(preceding)
            if open_callouts == 0:
                raise ValueError("Generated QMD contains an unmatched callout close")
            normalized.append(":::")
            open_callouts -= 1
            if trailing:
                normalized.extend(("", trailing))
            normalized.append("")
            continue

        normalized.append(line)

    if open_callouts:
        raise ValueError(f"Generated QMD has {open_callouts} unclosed callout(s)")
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(normalized)).strip()
    return frontmatter.group(0) + "\n" + body + "\n"


def tex_to_qmd(tex: str, title: str, seed_module) -> str:
    converted = seed_module.tex_to_sanitized_qmd(strip_title_block(tex), title)
    frontmatter = re.match(
        r"\A---\r?\n(?P<yaml>.*?)\r?\n---[ \t]*(?:\r?\n|$)",
        converted,
        flags=re.DOTALL,
    )
    if not frontmatter:
        raise ValueError(f"Generated QMD for {title!r} has invalid YAML delimiters")

    yaml = frontmatter.group("yaml").strip()
    if not re.search(r"(?m)^title\s*:", yaml):
        raise ValueError(f"Generated QMD for {title!r} is missing a YAML title")

    body_lines = converted[frontmatter.end():].splitlines()
    while body_lines and (
        not body_lines[0].strip()
        or re.fullmatch(r"(?:-{3,}|_{3,}|\*{3,})", body_lines[0].strip())
    ):
        body_lines.pop(0)
    normalized = f"---\n{yaml}\n---\n\n{'\n'.join(body_lines).strip()}\n"
    return normalize_callout_fences(normalized)


def restore_seed_chapters(seed_module) -> Dict[Path, str]:
    restored: Dict[Path, str] = {}
    for spec in seed_module.CHAPTER_SPECS:
        content = spec["tex_content"]
        validate_utf8(content, spec["tex_filename"])
        restored[spec["tex_dir"] / spec["tex_filename"]] = content
        if "alias_tex" in spec:
            restored[spec["tex_dir"] / spec["alias_tex"]] = content
    return restored


def main() -> int:
    seed_module = load_seed_module()
    seed_module.sync()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        raise SystemExit(f"Synchronization failed: {error}") from error