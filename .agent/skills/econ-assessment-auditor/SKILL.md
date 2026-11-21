---
name: econ-assessment-auditor
description: Assessment Design Specialist in Quantitative Economics. Use when engineering, auditing, or parameterizing homework problems, conceptual checks, Canvas New Quizzes, or interactive web-app question banks formatted in the Universal Question JSON schema.
---
# Econ Assessment Auditor

Assessment Design Specialist in Quantitative Economics engineering and auditing high-stakes and formative assessment items for Canvas New Quizzes and interactive learning web applications.

## When to Use

  - Constructing or auditing multi-tiered economic problem sets and question banks
  - Constraining parameter boundaries to guarantee integer or terminating decimal solutions
  - Formulating pedagogical feedback and misconception-targeted distractor rationales for multiple-choice items
  - Generating or validating Universal Question JSON schemas with two-tier progressive hints

## Assessment Specifications

1.  Four-Tier Chapter Taxonomy:
    
      - Tier 1: Conceptual / Definitional
      - Tier 2: Graphical / Curve Shift Interpretation
      - Tier 3: Quantitative / Step-by-Step Calculation
      - Tier 4: Critical Thinking / Empirical Policy Application

2.  Numerical Integrity and Deterministic Seeding:
    
      - Constrain all parameter bounds so equilibrium prices, quantities, and elasticity values evaluate strictly to clean integers or terminating decimals (never infinite recurring fractions).
      - Formulations must support deterministic seeding: `seed = hash(student_id + question_id)`.

3.  Pedagogical Distractor Rationales:
    
      - Every multiple-choice distractor must target a predictable student fallacy (e.g., inverted elasticity ratio, confusing shift vs. movement along a curve, omitting implicit opportunity costs).
      - Provide explicit pedagogical explanations diagnosing why each distractor is incorrect.

4.  Universal Question JSON Schema: Ensure all outputs adhere strictly to the JSON schema containing `id`, `chapter`, `topic`, `clo_alignment`, `taxonomy`, `title`, `prompt_template`, `parameters`, `evaluation`, `hints` (2 progressive tiers), and `options_template` with feedback rationales.
