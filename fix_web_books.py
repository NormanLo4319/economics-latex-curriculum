#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).parent
WEB_BOOKS = ROOT / "web_books"
MICRO_DIR = WEB_BOOKS / "microeconomics"
MACRO_DIR = WEB_BOOKS / "macroeconomics"

MICRO_YML = """project:
  type: book
  output-dir: ../../dist/web/micro

book:
  title: "Principles of Microeconomics"
  subtitle: "An Institutional and Social Science Perspective"
  author: "Norman Lo"
  date: "2026"
  search: true
  sidebar:
    style: "docked"
    search: true
    collapse-level: 1
  page-navigation: true
  chapters:
    - index.qmd
    - part: "Foundations of Market Analysis"
      chapters:
        - ch01_principles.qmd
        - ch02_ppf.qmd
        - ch03_supply_demand.qmd
        - ch04_surplus.qmd
        - ch05_elasticity.qmd
    - part: "Firm Behavior & Market Structures"
      chapters:
        - ch06_costs_production.qmd
        - ch07_perfect_competition.qmd
        - ch08_monopoly.qmd
        - ch09_imperfect_competition_game_theory.qmd
    - part: "Market Failures & Factor Markets"
      chapters:
        - ch10_externalities_public_goods.qmd
        - ch11_consumer_choice.qmd
        - ch12_factor_markets.qmd
        - ch13_asymmetric_information_risk.qmd
        - ch14_international_trade.qmd

format:
  html:
    theme:
      light: cosmo
      dark: darkly
    toc: true
    toc-depth: 3
    number-sections: true
    code-copy: true
    html-math-method: mathjax
"""

MICRO_INDEX = """# Preface {.unnumbered}

Welcome to **Principles of Microeconomics: An Institutional and Social Science Perspective**.

This textbook offers an analytical, empirical approach to microeconomic decision-making, price theory, market structures, and policy evaluation. It is structured around the analytical depth of Eric Chiang (*microeconomics: Principles for a Changing World*) and UC Berkeley Econ 1.

Use the left sidebar navigation to explore individual chapters or press `g` to initiate full-text keyword searches across the entire volume.
"""

MACRO_YML = """project:
  type: book
  output-dir: ../../dist/web/macro

book:
  title: "Principles of Macroeconomics"
  subtitle: "An Institutional and Social Science Perspective"
  author: "Norman Lo"
  date: "2026"
  search: true
  sidebar:
    style: "docked"
    search: true
    collapse-level: 1
  page-navigation: true
  chapters:
    - index.qmd
    - part: "Macroeconomic Foundations & Measurement"
      chapters:
        - ch01_principles.qmd
        - ch02_macro_ppf.qmd
        - ch03_supply_demand.qmd
        - ch04_gdp_accounting.qmd
        - ch05_unemployment_inflation.qmd
    - part: "Long-Run Growth & Financial Systems"
      chapters:
        - ch06_savings_investment_financial_system.qmd
    - part: "Short-Run Fluctuations & Stabilization"
      chapters:
        - ch07_aggregate_expenditure_multiplier.qmd
        - ch08_aggregate_demand_aggregate_supply.qmd
        - ch09_fiscal_policy.qmd
        - ch10_money_banking_fed.qmd
        - ch11_monetary_policy.qmd
        - ch12_open_economy_macroeconomics.qmd

format:
  html:
    theme:
      light: cosmo
      dark: darkly
    toc: true
    toc-depth: 3
    number-sections: true
    code-copy: true
    html-math-method: mathjax
"""

MACRO_INDEX = """# Preface {.unnumbered}

Welcome to **Principles of Macroeconomics: An Institutional and Social Science Perspective**.

This volume analyzes aggregate economic performance, national income determination, labor market dynamics, monetary and fiscal policy fraeworks, and international finance. It synthesizes foundational principles from Paul Krugman and Robin Wells (*macroeconomics*) and UC Berkeley Econ 2.

Use the left navigation sidebars or press `s` to search concepts, models, and equations directly.
"""

def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"[OK] Wrote file: {path.relative_to(ROOT)}")


def sanitize_chapter(qmd_path: Path):
    if not qmd_path.exists():
      return
    text = qmd_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
      closing = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
      if closing is not None:
        lines = lines[closing + 1:]
    while lines and (not lines[0].strip() or re.fullmatch(r"[-*_]{3,}", lines[0].strip())):
      lines.pop(0)

    course_dir = "micro" if qmd_path.parent == MICRO_DIR else "macro"
    source_path = ROOT / course_dir / "chapters" / f"{qmd_path.stem}.tex"
    title = qmd_path.stem.replace("_", " ").title()
    if source_path.exists():
      source = source_path.read_text(encoding="utf-8")
      match = re.search(r"\\title\{.*?\\color\{[^}]+\}\s*(.*?)\}\s*\\author", source, re.DOTALL)
      if match:
        title = match.group(1).replace(r"\&", "&").strip()

    body = "\n".join(lines)
    body = body.replace(r"\:::", ":::").replace(r'\"', '"')
    normalized_lines = []
    for line in body.splitlines():
      opening = re.search(r"\s*:::\s+(\.callout-[\w-]+)([^\n]*)$", line)
      closing = re.search(r"\s+:::\s*$", line)
      if opening:
        preceding = line[:opening.start()].rstrip()
        if preceding:
          normalized_lines.append(preceding)
        if normalized_lines and normalized_lines[-1]:
          normalized_lines.append("")
        normalized_lines.append(f"::: {{{opening.group(1)}{opening.group(2)}}}")
      elif closing:
        preceding = line[:closing.start()].rstrip()
        if preceding:
          normalized_lines.append(preceding)
        if normalized_lines and normalized_lines[-1]:
          normalized_lines.append("")
        normalized_lines.append(":::")
        normalized_lines.append("")
      else:
        normalized_lines.append(line)
    body = "\n".join(normalized_lines)
    body = re.sub(r"(?m)(?<!\x0a)\x0a(?=:::)", lambda _: chr(10) * 2, body)
    body = re.sub(r"(?m)(?<=:::)\x0a(?!\x0a)", lambda _: chr(10) * 2, body)
    body = re.sub(r"(?m)^:::\s+([A-Za-z][\w-]*)\s*$", r"::: { .\1 }", body)
    body = re.sub(r"\\begin\{equation\*?\}", "", body)
    body = re.sub(r"\\end\{equation\*?\}", "", body)
    body = re.sub(r"\\begin\{align\*?\}", lambda _: r"\begin{aligned}", body)
    body = re.sub(r"\\end\{align\*?\}", lambda _: r"\end{aligned}", body)

    safe_title = title.replace('"', r'\"')
    new_text = f"---\ntitle: \"{safe_title}\"\n---\n\n{body.strip()}\n"
    qmd_path.write_text(new_text, encoding="utf-8", newline="\n")
    print(f"[OK] Sanitized: {qmd_path.relative_to(ROOT)}")


def main():
    print("Step 1: Writing Quarto project files for Micro and Macro...")
    write_file(MICRO_DIR / "_quarto.yml", MICRO_YML)
    write_file(MICRO_DIR / "index.qmd", MICRO_INDEX)
    write_file(MACRO_DIR / "_quarto.yml", MACRO_YML)
    write_file(MACRO_DIR / "index.qmd", MACRO_INDEX)

    print("\nStep 2: Sanitizing existing .qmd chapter files...")
    for dirpath in (MICRO_DIR, MACRO_DIR):
      for qmd in sorted(dirpath.glob("ch*.qmd")):
        sanitize_chapter(qmd)

    print("\nAll files successfully created and sanitized!")


if __name__ == "__main__":
    main()
