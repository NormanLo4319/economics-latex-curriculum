# Curriculum & Question Bank Progress Tracker (Spring 2027)

**Legend:** `[ ]` Not started / Legacy · `[~]` Draft / Partial · `[x]` Audited & Verified  
**Live Quiz Check:** `python tools/validate_qbank.py --all`  
**Single-Chapter Web Sync:** `python convert_to_quarto.py --chapter <micro|macro>/<stem>`  
**Single-Chapter QTI Export:** `python tools/build_qti.py <micro|macro>/quizzes/<stem>.json --shuffle`

---

## Microeconomics (14 Chapters — Eric Chiang)

| Sprint | Ch | Stem | Reading (`.tex`) | Web (`.qmd`) | Quiz v2 (50Q) | QTI (`.zip`) | Notes |
| :-: | :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| S1 | 01 | `ch01_principles` | `[~]` | `[x]` | `[ ]` | `[ ]` | Minor BIH/WIO polish; legacy quiz |
| S1 | 02 | `ch02_ppf` | `[~]` | `[ ]` | `[ ]` | `[ ]` | Expanded 434L; audit + web sync |
| S1 | 03 | `ch03_supply_demand` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 362L; audit + upgrade |
| S2 | 04 | `ch04_surplus` | `[x]` | `[x]` | `[ ]` | `[ ]` | Flagship reading; check GDrive v2 qbank |
| S2 | 05 | `ch05_elasticity` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 685L; audit + web sync |
| S3 | 06 | `ch06_costs_production` | `[x]` | `[ ]` | `[ ]` | `[ ]` | Audited reading restored; re-sync `.qmd`; **missing quiz** |
| S3 | 07 | `ch07_perfect_competition` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 316L; audit + upgrade |
| S3 | 08 | `ch08_monopoly` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 292L; audit + upgrade |
| S4 | 09 | `ch09_imperfect_competition_game_theory` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 302L; audit + upgrade |
| S4 | 10 | `ch10_externalities_public_goods` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 286L; **missing quiz** |
| S4 | 11 | `ch11_consumer_choice` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 298L; **missing quiz** |
| S5 | 12 | `ch12_factor_markets` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 290L; audit + upgrade |
| S5 | 13 | `ch13_asymmetric_information_risk` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 282L; **missing quiz** |
| S5 | 14 | `ch14_international_trade` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | Restored 237L; audit + upgrade |

---

## Macroeconomics (12 Chapters — Krugman & Wells)

| Sprint | Ch | Stem | Reading (`.tex`) | Web (`.qmd`) | Quiz v2 (50Q) | QTI (`.zip`) | Notes |
| :-: | :-: | :--- | :-: | :-: | :-: | :-: | :--- |
| S1 | 01 | `ch01_principles` | `[~]` | `[x]` | `[ ]` | `[ ]` | Minor BIH/WIO/Calc polish; legacy quiz |
| S1 | 02 | `ch02_macro_ppf` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 399L draft; add WIO + audit + web sync |
| S1 | 03 | `ch03_supply_demand` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 473L draft; single-market price check |
| S2 | 04 | `ch04_aggregate_output` | `[~]` | `[ ]` | `[x]` | `[x]` | Quiz 50/50 PASS + QTI built; audit reading |
| S2 | 05 | `ch05_inflation_deflation` | `[~]` | `[ ]` | `[~]` | `[ ]` | Quiz **20/50** v2 (add 30Q); audit reading |
| S2 | 06 | `ch06_unemployment` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 619L draft; rebuild quiz (remove old CPI mix) |
| S3 | 07 | `ch07_savings_investment_financial_system` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 633L draft; add Calc box + audit |
| S3 | 08 | `ch08_aggregate_expenditure_multiplier` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 485L draft; add Calc box + audit |
| S4 | 09 | `ch09_aggregate_demand_aggregate_supply` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 378L draft; full audit + web sync |
| S4 | 10 | `ch10_fiscal_policy` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 565L draft; full audit + web sync |
| S5 | 11 | `ch11_money_banking_fed` | `[~]` | `[ ]` | `[ ]` | `[ ]` | 614L draft; verify post-2020 ample reserves |
| S5 | 12 | `ch12_monetary_policy` | `[~]` | `[ ]` | `[x]` | `[x]` | Quiz 50/50 PASS + QTI built; audit reading |

---

## Session Handoff Rule (1 Fresh Chat per Chapter)

1. **At session start:** Read only this tracker + the target chapter's `.tex` + the relevant spec (`docs/CHAPTER_REVIEW_WORKFLOW.md` for readings, `docs/UNIVERSAL_QBANK_SCHEMA.md` for quizzes).
2. **At session end:** Flip the completed `[ ]` / `[~]` checkboxes on that chapter's row to `[x]`, run the validation/export commands above, and start a fresh chat for the next chapter.
