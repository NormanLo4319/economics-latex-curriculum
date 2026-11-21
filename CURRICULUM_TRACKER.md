# Curriculum & Question Bank Progress Tracker (Spring 2027)

**Legend:** `[ ]` Not started / Legacy · `[~]` Draft / Partial · `[x]` Audited & Verified  
**Live Quiz Check:** `python tools/validate_qbank.py --all`  
**Single-Chapter Web Sync:** `python convert_to_quarto.py --chapter <micro|macro>/<stem>`  
**Single-Chapter QTI Export:** `python tools/build_qti.py <micro|macro>/quizzes/<stem>.json --shuffle`

---

## Microeconomics (14 Chapters — Eric Chiang)

| Sprint | Ch | Stem | Reading (`.tex`) | Web (`.qmd`) | Quiz v2 (50Q) | QTI (`.zip`) | Notes |
| :-: | :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| S1 | 01 | `ch01_principles` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S1 | 02 | `ch02_ppf` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S1 | 03 | `ch03_supply_demand` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S2 | 04 | `ch04_surplus` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S2 | 05 | `ch05_elasticity` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S3 | 06 | `ch06_costs_production` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S3 | 07 | `ch07_perfect_competition` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S3 | 08 | `ch08_monopoly` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S4 | 09 | `ch09_imperfect_competition_game_theory` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S4 | 10 | `ch10_externalities_public_goods` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S4 | 11 | `ch11_consumer_choice` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S5 | 12 | `ch12_factor_markets` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S5 | 13 | `ch13_asymmetric_information_risk` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S5 | 14 | `ch14_international_trade` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |

---

## Macroeconomics (12 Chapters — Krugman & Wells)

| Sprint | Ch | Stem | Reading (`.tex`) | Web (`.qmd`) | Quiz v2 (50Q) | QTI (`.zip`) | Notes |
| :-: | :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| S1 | 01 | `ch01_principles` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S1 | 02 | `ch02_macro_ppf` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S1 | 03 | `ch03_supply_demand` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S2 | 04 | `ch04_aggregate_output` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S2 | 05 | `ch05_inflation_deflation` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S2 | 06 | `ch06_unemployment` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S3 | 07 | `ch07_savings_investment_financial_system` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S3 | 08 | `ch08_aggregate_expenditure_multiplier` | `[x]` | `[~]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready (sync .qmd outside sandbox) |
| S4 | 09 | `ch09_aggregate_demand_aggregate_supply` | `[x]` | `[~]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready (sync .qmd outside sandbox) |
| S4 | 10 | `ch10_fiscal_policy` | `[x]` | `[x]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready |
| S5 | 11 | `ch11_money_banking_fed` | `[x]` | `[~]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready (sync .qmd outside sandbox) |
| S5 | 12 | `ch12_monetary_policy` | `[x]` | `[~]` | `[x]` | `[x]` | Audited + 50Q v2 + QTI ready (sync .qmd outside sandbox) |

---

## Session Handoff Rule (1 Fresh Chat per Chapter)

1. **At session start:** Read only this tracker + the target chapter's `.tex` + the relevant spec (`docs/CHAPTER_REVIEW_WORKFLOW.md` for readings, `docs/UNIVERSAL_QBANK_SCHEMA.md` for quizzes).
2. **At session end:** Flip the completed `[ ]` / `[~]` checkboxes on that chapter's row to `[x]`, run the validation/export commands above, and start a fresh chat for the next chapter.
