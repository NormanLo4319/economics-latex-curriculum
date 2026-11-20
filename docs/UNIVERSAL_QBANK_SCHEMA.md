# Universal Question Bank JSON Schema (v2.0)

Canonical specification for all 26 Principles of Economics question banks (`micro/quizzes/*.json` and `macro/quizzes/*.json`). Every bank maps 1-to-1 by file stem to its canonical chapter in `micro/chapters/*.tex` or `macro/chapters/*.tex`.

## Top-Level Object

```json
{
  "schema_version": "2.0",
  "course": "Principles of Macroeconomics",
  "chapter_id": "macro_ch04",
  "file_stem": "ch04_aggregate_output",
  "title": "Chapter 4: Aggregate Output",
  "benchmark": "Krugman & Wells (Macroeconomics) & SFSU/CCSF Principles SSOT (Spring 2027)",
  "seeding_formula": "seed = hash(student_id + question_id)",
  "points_per_question": 1,
  "questions_count": 50,
  "tier_distribution": {
    "tier_1": 13,
    "tier_2": 13,
    "tier_3": 12,
    "tier_4": 12
  },
  "questions": [ ... ]
}
```

## Canonical 4-Tier Taxonomy

| `tier` | Canonical `taxonomy` Value | Target Count (of 50) | Focus |
| :-: | :--- | :-: | :--- |
| `1` | `Tier 1: Conceptual / Definitional` | 12–13 | Core concepts, definitions, boundaries, institutional facts |
| `2` | `Tier 2: Graphical / Curve Shift Interpretation` | 12–13 | Shifts vs. movements, slopes, equilibria, comparative statics |
| `3` | `Tier 3: Quantitative / Step-by-Step Calculation` | 12–13 | Algebra-first math; clean integers or terminating decimals; Python-verified |
| `4` | `Tier 4: Critical Thinking / Empirical Policy Application` | 12–13 | Policy trade-offs, FRED empirical interpretation, synthesis |

## Per-Question Object

```json
{
  "id": "MACRO_CH04_T1_01",
  "chapter": 4,
  "tier": 1,
  "taxonomy": "Tier 1: Conceptual / Definitional",
  "topic": "GDP Boundaries & Value Added",
  "clo_alignment": ["MA-1", "C2002-1"],
  "title": "Avoiding Double Counting via Value Added",
  "prompt_template": "Why does summing each firm's value added across a production chain equal the market value of the final good without double counting?",
  "parameters": {},
  "evaluation": {
    "mode": "multiple_choice",
    "correct_option_id": "opt_a",
    "numeric_tolerance": 0
  },
  "hints": [
    { "tier": 1, "text": "Conceptual nudge pointing toward the core principle." },
    { "tier": 2, "text": "More specific structural or algebraic hint without giving away the answer." }
  ],
  "options_template": [
    {
      "id": "opt_a",
      "text": "Correct answer text.",
      "is_correct": true,
      "feedback": "Correct. Brief explanation reinforcing the economic reasoning."
    },
    {
      "id": "opt_b",
      "text": "Plausible distractor tied to a specific student misconception.",
      "is_correct": false,
      "feedback": "Diagnostic fallacy (Name of Fallacy): Why this choice is wrong."
    },
    {
      "id": "opt_c",
      "text": "Second plausible distractor.",
      "is_correct": false,
      "feedback": "Diagnostic fallacy (Name of Fallacy): Why this choice is wrong."
    },
    {
      "id": "opt_d",
      "text": "Third plausible distractor.",
      "is_correct": false,
      "feedback": "Diagnostic fallacy (Name of Fallacy): Why this choice is wrong."
    }
  ]
}
```

## Validation & Canvas Export Commands

```bash
# Validate a single bank (use --strict to require full 50 questions & balanced tiers)
python tools/validate_qbank.py macro/quizzes/ch04_aggregate_output.json --strict

# Audit status across all 26 banks
python tools/validate_qbank.py --all

# Build Canvas QTI 1.2 .zip package
python tools/build_qti.py macro/quizzes/ch04_aggregate_output.json
```
