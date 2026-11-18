# Academic Development Master Summary (SSOT Reference)

**Owner:** Norman Lo, M.A. (Adjunct Faculty, SFSU; Senior Data Scientist, CoStar Group)  
**Last Updated:** 2026-11-15  
**Purpose:** Condensed single-reference context for all future academic tasks (curriculum authoring, media production, workshop demo prep, Canvas integration, and course grading) so new tasks do not need to read prior chat history. Pair with `Core_Values_and_Pedagogical_Standards.md`.

---

## 1. Workspace & Single Source of Truth (SSOT) Architecture

- **Cloud Root (`01_ACADEMIC & TEACHING`):** `https://drive.google.com/drive/folders/1a9iDlQ7QeK-Z4n20cSGVljhfOltwIwNn` (mirrored with local Git repositories).
- **Key Subfolders:**
  - `ECON_Principles_Course_Development` (`https://drive.google.com/drive/folders/1-EN3SYQMngIDhvk6FiH3A-ngXbidaTIK`) — houses `economics-latex-curriculum/` (`micro/chapters/*.tex`, `macro/chapters/*.tex`, `sync_all_readings.py`, `sync_readings_to_tex.py`).
  - `media_production` (`https://drive.google.com/drive/folders/1XrvRIsWn3py6W57toslUi4JS0Z-zjV4C`) — houses 16:9 PPTX decks, video scripts, and workshop slides.
  - `ai_curriculum_engine` (`https://drive.google.com/drive/folders/1AwkEhQFQsjPbwP52LJVslI15Z1Reibga`) — houses modular agent skill specs (`ai_agent_skill_library.md`) and demo verification docs.
  - `canvas_master_course_shells` (`https://drive.google.com/drive/folders/1lYuR3eHK91D50hL4sWDdWzLEXbjHBqCu`) — houses `.imscc` course exports (e.g., `sfsu_econ102_macroeconomic_master_shell.imscc`), `audit_course.py`, `update_course.py`, `replacements.json`.
  - `2026_Fall` (`https://drive.google.com/drive/folders/13cDV_bCJ9Utvwyf0y2RHn08uegbHb8_T`) — houses ECON 783 MBA course grading, rubrics, and submissions.
- **Tooling & Cost Control:** VS Code + GitHub Copilot Chat (GitHub Educator Pro, $0 API cost); Quarto web-books (GitHub Pages); Python `canvasapi` / QTI 1.2 `.zip` exports; custom AI skills (`economist`, `superpower`, `econ-visualization`, `econ-curriculum-author`, `econ-presentation`, `econ-professor-auditor`, `econ-visualization-reviewer`, `econ-assessment-auditor`).

---

## 2. Active Project 1 — Principles of Economics OER Curriculum (Spring 2027 Launch)

- **Scope:** 26 chapters total (14 Microeconomics aligned with Eric Chiang; 12 Macroeconomics aligned with Krugman & Wells) for 1st/2nd-year GE students at SFSU (ECON 101/102) and CCSF.
- **4 Active Production Tracks:**
  1. Master LaTeX & Quarto Web-Books (`economics-latex-curriculum/`, MathJax + inline SVGs).
  2. Interactive Learning Web App (`economics-learning-web-app` repo).
  3. Canvas Native Assessments (4-tier Universal Question JSON -> QTI 1.2 `.zip` imports, 50-question banks per chapter with diagnostic distractors).
  4. Media Production (16:9 visual-first PPTX decks split into 8–14 min modular YouTube video segments, >= 6–8 slides per deck).
- **Completed Flagship Demo Chapters (Micro Ch. 4 & Macro Ch. 5):**
  - **Micro Ch. 4 (Surplus & Welfare):** `P = 100 - 2Q`, `P = 20 + 2Q`, `P* = $60`, `Q* = 20`, `CS = $400`, `PS = $400`, `TS = $800`; `$12` excise tax wedge (`Qt = 17`, `Pb = $66`, `Ps = $54`, `Trev = $204`, `DWL = $18`); rent ceiling (`$40` -> 20-unit shortage, `DWL = $200`). Assets: `ch04_surplus.tex`, `Micro_Ch04_Surplus_and_Welfare.html`, `Micro_Chapter_4_True_Visuals_16x9.pptx`, `micro_ch04_qbank_v2.json`.
  - **Macro Ch. 5 (Unemployment & Inflation):** `CNIP = 200M`, `LF = 120M`, `E = 114M`, `U = 6M` (`U-3 = 5.0%`, `LFPR = 60.0%`, `U-6 = 11.38%`), Okun's Law (`-$1.0T` gap), CPI & Fisher Equation (`r = i - pi`). Verified FRED series: `UNRATE`, `U6RATE`, `CIVPART`, `EMRATIO`, `CPIAUCSL`. Assets: `ch05_unemployment_inflation.tex`, `ch05_unemployment_inflation.html`, `Macro_Chapter_5_True_Visuals_16x9.pptx`.
- **Other Completed V2 Decks in `media_production`:** `Micro_Chapter_8_True_Visuals_16x9_V2.pptx`, plus Macro Sprints 3 and 4.
- **Known Technical Note:** `sync_readings_to_tex.py` previously hit non-UTF-8 encoding issues around line 240; ensure UTF-8 encoding when running cloud-to-local sync.

---

## 3. Active Project 2 — SFSU Economics Department Faculty Workshop (Dec 1, 2026)

- **Format:** 60-minute faculty development workshop (*"Teaching Economics with AI Tools"*: 25-min slide walkthrough, 20-min live demo on Micro Ch. 4 & Macro Ch. 5, 15-min Q&A).
- **Core Narrative:** Overcoming Hartmut Rosa's "Alienation & Acceleration" while eliminating $80–$120/semester commercial publisher costs via faculty-owned OER, GitHub Education Copilot Pro, VS Code, and Canvas automation.
- **Completed Workshop Assets (in `media_production` and `ai_curriculum_engine`):**
  - `Economics_Department_Workshop_10Slides.pptx`
  - `Workshop_Presentation_Narrative_Script.md`
  - `workshop_demo_runbook.md`
  - `SFSU_Economics_Department_AI_Workshop_Flyer`
  - `05_honest_skill.md`, `06_graphical_skill.md`, `07_project_management_skill.md`, `ai_agent_skill_library.md`

---

## 4. Active Project 3 — SFSU ECON 783 (Economics for Managers, Fall 2026 MBA)

- **Completed Milestone:** First Draft group project grading across 4 teams (Commercial Banking: 97/A, Group Alpha Healthcare: 94/A, Higher Education & AI: 85/B, Team Beta Restaurants: 83/B; 83-point minimum floor enforced; native Adobe Acrobat annotated PDFs + scorecards posted on Canvas).
- **Master Records:** Master Gradebook Sheet and `ECON 783 Presentation & Final Draft Guidelines & Rubrics` in `2026_Fall/`.
- **Upcoming Milestones (Mid-Dec 2026):** First Draft Anonymous Peer Evaluations (25% of project grade), In-Person Team Presentations (10–15 min, visual-first slides, Q&A), and Final Draft Written Reports (10–15 pages, APA preferred, labeled exhibits, solution weaknesses section).

---

## 5. Token-Saving Protocol for New Tasks

- Start a dedicated new chat/task per specific feature (e.g., *"Author Micro Ch. 6"*, *"Build Macro Ch. 6 PPTX"*, *"Create ECON 783 Peer Eval Form"*).
- Reference this file (`Academic_Development_Master_Summary.md`) and `Core_Values_and_Pedagogical_Standards.md` at the start of the prompt—no prior chat history loading required.
- Save all new outputs directly into the appropriate `01_ACADEMIC & TEACHING` subfolder and append 1–2 line status updates here only when a major milestone closes.
