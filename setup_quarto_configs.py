#!/usr/bin/env python3
"""
setup_quarto_configs.py

Ensures all Quarto book configurations and index files are created and
properly written as raw text files on disk, avoiding Google Drive shortcut issues.
"""
from pathlib import Path

ROOT = Path(__file__).parent
WEB_BOOKS = ROOT / "web_books"
MICRO_DIR = WEB_BOOKS / "microeconomics"
MACRO_DIR = WEB_BOOKS / "macroeconomics"

MICRO_QUARTO_YML = """project:
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
        - ch06_competition.qmd
        - ch07_monopoly.qmd
        - ch08_oligopoly.qmd
        - ch09_game_theory.qmd
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

MICRO_INDEX_QMD = """# Preface {.unnumbered}

Welcome to **Principles of Microeconomics: An Institutional and Social Science Perspective**.

This textbook offers an analytical, empirical approach to microeconomic decision-making, price theory, market structures, and policy evaluation. It is structured around the analytical depth of Eric Chiang (*Microeconomics: Principles for a Changing World*) and UC Berkeley Econ 1.

Use the left sidebar navigation to explore individual chapters or press `s` to initiate full-text keyword searches across the entire volume.
"""

MACRO_QUARTO_YML = """project:
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
        - ch04_gdp_measurement.qmd
        - ch05_unemployment_inflation.qmd
    - part: "Long-Run Growth & Financial Systems"
      chapters:
        - ch06_growth_productivity.qmd
        - ch07_savings_investment.qmd
    - part: "Short-Run Fluctuations & Stabilization"
      chapters:
        - ch08_aggregate_demand_aggregate_supply.qmd
        - ch09_fiscal_policy.qmd
        - ch10_money_banking.qmd
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

MACRO_INDEX_QMD = """# Preface {.unnumbered}

Welcome to **Principles of Macroeconomics: An Institutional and Social Science Perspective**.

This volume analyzes aggregate economic performance, national income determination, labor market dynamics, monetary and fiscal policy frameworks, and international finance. It synthesizes foundational principles from Paul Krugman and Robin Wells (*Macroeconomics*) and UC Berkeley Econ 2.

Use the left navigation sidebar or press `s` to search concepts, models, and equations directly.
"""


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"[OK] Wrote raw file: {path.relative_to(ROOT)}")


def main():
    print("Writing native Quarto configuration and index files...")
    write_file(MICRO_DIR / "_quarto.yml", MICRO_QUARTO_YML)
    write_file(MICRO_DIR / "index.qmd", MICRO_INDEX_QMD)
    write_file(MACRO_DIR / "_quarto.yml", MACRO_QUARTO_YML)
    write_file(MACRO_DIR / "index.qmd", MACRO_INDEX_QMD)
    print("Done! Native Quarto files ready.")


if __name__ == "__main__":
    main()
