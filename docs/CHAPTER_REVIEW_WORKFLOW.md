# Principles of Economics Chapter Review Workflow

## Purpose and authority

Use this workflow for one Microeconomics or Macroeconomics chapter at a time. It records process lessons from the Chapter 1 reviews; it does not replace the course requirements in the [Core Values and Pedagogical Standards](./ssot/Core_Values_and_Pedagogical_Standards.md) or the [Academic Development Master Summary](./ssot/Academic_Development_Master_Summary.md). Consult those documents and the relevant project skills before each review.

The approved section sequence follows the Core Values SSOT:

1. Conceptual introduction and real-world hook.
2. Visual representation.
3. Mathematical foundation, algebra-first.
4. Optional advanced calculus extension.

Use real-world applications as hooks, examples, or learning checkpoints within that sequence. Keep calculus optional. The user has also selected unnumbered structural subheadings (for example, `Conceptual Introduction`) beneath numbered main sections (for example, `1.1`); do not add another numeric level unless requested.

## 1. Scope the review

- Keep the chat and file inspection limited to the requested chapter, its figures, the relevant converter/configuration, the SSOT documents, and applicable skills.
- Treat the chapter `.tex` file as the canonical content source when that is the established project workflow. Treat generated web-book `.qmd` as output; fix the source or converter rather than editing generated content by hand.
- Inspect the worktree before editing. Preserve existing user changes and avoid broad registry syncs that could overwrite hand-edited chapters.
- Audit first, then present findings and proposed patches. Edit canonical curriculum files only when the user has authorized implementation.

## 2. Audit and record findings

Use a concise ledger with the location, issue, consequence, proposed fix, and verification needed. Check:

- **Alignment and accuracy:** Micro topics against the Eric Chiang benchmark; Macro topics against Krugman and Wells. For Macro, represent the post-2020 ample-reserves regime accurately and reject obsolete scarce-reserve money-multiplier explanations.
- **Section structure and teaching:** Begin with plain-language intuition; include a readable visual, algebra-first mathematical foundation, and an optional advanced-calculus extension where relevant. Check for misconception explanations and step-by-step worked examples.
- **Mathematics:** Independently recompute every equilibrium, elasticity, welfare area, and reported metric. State assumptions and show enough arithmetic to make results auditable.
- **Evidence:** Verify empirical claims, dates, citations, and FRED series against authoritative sources. Do not invent evidence or official course-outcome IDs; flag unavailable mappings.
- **Visuals and accessibility:** Check economic geometry, axes, labels, curves, equilibrium markers, colorblind-safe colors, text collisions, captions, and non-empty image alt text.
- **Web-book presentation:** Check section hierarchy, MathJax rendering, links, stylesheet loading, and responsive layout. A technically correct TeX source can still produce malformed or unreadable HTML.

## 3. Implement at the source

- Make surgical edits to the canonical `.tex` chapter and directly related converter/configuration code only.
- Preserve numbered main sections while keeping structural subheadings descriptive and unnumbered.
- TeX comment-only lines (such as `% -----` dividers) must not leak into Markdown as visible text. If they do, fix the converter and regenerate the `.qmd`.
- Keep each Quarto book's stylesheet available within that book's generated output. A stylesheet referenced from a sibling project may not be copied by Quarto.
- Use a targeted conversion/render command. `python convert_to_quarto.py --chapter1-only` is verified for Chapter 1 only; inspect the available command or workflow before applying it to another chapter.

## 4. Validate the delivered output

1. Compile the edited TeX chapter twice into a temporary directory; confirm the PDF exists and inspect errors or unresolved references.
2. Regenerate the target `.qmd` and figures from TeX; confirm comment dividers and source-only markup are absent.
3. Render the target Quarto page and check that equations, figures, captions, links, and heading hierarchy survive conversion.
4. Preview at a narrow viewport (476 px) and a desktop width. Confirm there is no horizontal page overflow, long links wrap, display math can scroll when needed, and figures load with meaningful alt text. Inspect the diagrams themselves, not only their source code.
5. Report what changed, the exact checks run, and anything deferred. Do not claim completion while a known rendering or correctness issue remains.

## Chapter 1 lessons to carry forward

- LaTeX comment dividers appeared as literal `%` text in the web-book; the converter now removes standalone comment lines.
- Numbering both main sections and the four structural subheadings made the hierarchy confusing; retain main-section numbers and use unnumbered structural labels.
- Mobile overflow came from a combination of long math and an unbreakable URL; make display math horizontally scrollable and allow long links to wrap, then measure the rendered page.
- Macro's cross-project stylesheet reference was not present in the rendered output; use a stylesheet local to the Macro book and verify the generated page actually loads it.
- The Chapter 1 converter command is scoped to Chapter 1. Do not use a whole-book or stale-registry sync for other chapters without checking what it will overwrite.

## Relevant references

- [Core skill](../.github/skills/core-skill/SKILL.md)
- [Economics curriculum author skill](../.github/skills/econ-curriculum-author/SKILL.md)
- [Economics professor auditor skill](../.github/skills/econ-professor-auditor/SKILL.md)
- [Economics visualization reviewer skill](../.github/skills/econ-visualization-reviewer/SKILL.md)
- Chapter 1 examples: [Micro TeX](../micro/chapters/ch01_principles.tex), [Macro TeX](../macro/chapters/ch01_principles.tex)
