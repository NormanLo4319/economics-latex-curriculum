"""Automated Curriculum & Question Bank Sprint Workflow for Antigravity `run_workflow`.

Runs isolated, zero-history-bloat agents per chapter:
  Stage 1: Reading Audit & Finalize (.tex) + targeted Quarto conversion attempt
  Stage 2: 50-Question Universal v2.0 Bank (.json) + strict validation + auto-repair + QTI 1.2 export
  Stage 3: Deterministic CURRICULUM_TRACKER.md update + full curriculum dashboard

Args (JSON dict passed via run_workflow Args):
  chapters: list[str]      Explicit slugs like ["micro/ch01_principles", "micro/ch02_ppf"]
  sprint: str              Optional sprint code from CURRICULUM_TRACKER.md ("S1".."S5") if chapters omitted
  force_reading: bool      Re-audit reading even if marked [x] in tracker (default: False)
  force_quiz: bool         Rebuild quiz even if validate_qbank.py --strict passes (default: False)
  skip_reading: bool       Skip Stage 1 reading audit (default: False)
  skip_quiz: bool          Skip Stage 2 quiz build (default: False)
  reading_model: str       "inherit" | "pro" | "flash" (default: "inherit")
  quiz_model: str          "inherit" | "pro" | "flash" (default: "inherit")
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(WORKSPACES[0]) if WORKSPACES else Path.cwd()
TRACKER_PATH = ROOT / "CURRICULUM_TRACKER.md"
PYTHON = sys.executable

READING_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["ok", "skipped", "error"]},
        "edits_summary": {"type": "string"},
        "math_verified": {"type": "boolean"},
        "has_bih_ciu_wio": {"type": "boolean"},
        "notes": {"type": "string"},
    },
    "required": ["status", "edits_summary", "math_verified", "has_bih_ciu_wio", "notes"],
}

QUIZ_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["ok", "error"]},
        "questions_written": {"type": "integer"},
        "tier3_math_verified": {"type": "boolean"},
        "notes": {"type": "string"},
    },
    "required": ["status", "questions_written", "tier3_math_verified", "notes"],
}


def run_cmd(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
    return proc.returncode, output.strip()


def parse_tracker() -> dict[str, dict]:
    """Parse CURRICULUM_TRACKER.md into { 'micro/stem': row_info }."""
    rows: dict[str, dict] = {}
    if not TRACKER_PATH.exists():
        return rows
    course = None
    for line in TRACKER_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Microeconomics"):
            course = "micro"
        elif line.startswith("## Macroeconomics"):
            course = "macro"
        elif course and re.match(r"^\|\s*S\d+\s*\|", line):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 8:
                sprint, ch_num, stem_raw, r_st, w_st, q_st, qti_st, notes = parts[:8]
                stem = stem_raw.strip("`")
                rows[f"{course}/{stem}"] = {
                    "sprint": sprint,
                    "chapter_num": int(ch_num),
                    "course": course,
                    "stem": stem,
                    "reading": r_st.strip("`"),
                    "web": w_st.strip("`"),
                    "quiz": q_st.strip("`"),
                    "qti": qti_st.strip("`"),
                    "notes": notes,
                }
    return rows


def update_tracker(results: list[dict]) -> None:
    """Update CURRICULUM_TRACKER.md rows cleanly in one single-threaded pass."""
    if not TRACKER_PATH.exists():
        return
    by_slug = {r["slug"]: r for r in results}
    lines = TRACKER_PATH.read_text(encoding="utf-8").splitlines()
    new_lines = []
    course = None
    for line in lines:
        if line.startswith("## Microeconomics"):
            course = "micro"
        elif line.startswith("## Macroeconomics"):
            course = "macro"
        elif course and re.match(r"^\|\s*S\d+\s*\|", line):
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) >= 8:
                stem = parts[2].strip("`")
                slug = f"{course}/{stem}"
                if slug in by_slug:
                    res = by_slug[slug]
                    if res["reading_done"]:
                        parts[3] = "`[x]`"
                    if res["web_done"]:
                        parts[4] = "`[x]`"
                    elif res["reading_done"] and parts[4].strip("`") == "[ ]":
                        parts[4] = "`[~]`"
                    if res["quiz_done"]:
                        parts[5] = "`[x]`"
                    if res["qti_done"]:
                        parts[6] = "`[x]`"
                    if res["tracker_note"]:
                        parts[7] = res["tracker_note"]
                    line = "| " + " | ".join(parts[:8]) + " |"
        new_lines.append(line)
    TRACKER_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def benchmark_for(course: str) -> str:
    if course == "micro":
        return "Eric Chiang, Microeconomics (Principles SSOT, Spring 2027)"
    return "Paul Krugman & Robin Wells, Macroeconomics (Principles SSOT, Spring 2027)"


def clo_prefix_for(course: str) -> str:
    return "MI" if course == "micro" else "MA"


async def process_chapter(slug: str, meta: dict, cfg: dict) -> dict:
    course, stem = slug.split("/", 1)
    ch_num = meta.get("chapter_num") or int(re.search(r"ch(\d+)", stem).group(1))
    tex_rel = f"{course}/chapters/{stem}.tex"
    quiz_rel = f"{course}/quizzes/{stem}.json"
    qti_rel = f"build/qti/{course}_{stem}_qti.zip"
    course_title = "Principles of Microeconomics" if course == "micro" else "Principles of Macroeconomics"

    result = {
        "slug": slug,
        "reading_done": meta.get("reading") == "[x]",
        "web_done": meta.get("web") == "[x]",
        "quiz_done": False,
        "qti_done": False,
        "web_note": "",
        "tracker_note": "",
        "errors": [],
    }

    try:
        # ------------------------------------------------------------------
        # STAGE 1: Reading Audit & Finalize (.tex)
        # ------------------------------------------------------------------
        need_reading = (not cfg["skip_reading"]) and (cfg["force_reading"] or not result["reading_done"])
        if need_reading:
            log(f"[{slug}] Stage 1: Auditing and finalizing {tex_rel}")
            reading_prompt = f"""Audit and finalize the canonical chapter `{tex_rel}` ({course_title}, Chapter {ch_num}).

Read ONLY these 3 files first (do NOT scan the rest of the repo):
1. `Core_Values_and_Pedagogical_Standards.md`
2. `docs/CHAPTER_REVIEW_WORKFLOW.md`
3. `{tex_rel}`

Requirements:
- Benchmark alignment: {benchmark_for(course)}.
- Verify every main section follows the 4-part blueprint (Conceptual Intro/Hook -> Visual -> Algebra-First Math -> Optional Advanced Calculus Box where appropriate) with unnumbered structural subheadings (`\\subsection*{{...}}`).
- Ensure active-learning checkpoints exist and are high quality: `Bring It Home` (`examplecase`), `Clear It Up` misconception box, and `Work It Out` guided problem(s). If any are missing or weak, add/strengthen them directly in `{tex_rel}`.
- Verify all economic geometry and TikZ figures use the colorblind-safe Okabe-Ito palette (`SlateBlue`, `CourseBlue`, `CourseOrange`, `CourseTeal`, `CoursePurple`, `CourseAmber`, `ForestGreen`, `Terracotta`), orthogonal equilibrium drop-lines, and clear labels/captions.
- Independently verify EVERY numerical calculation, equilibrium, table entry, and worked problem in `{tex_rel}` using a quick Python check via `run_command`. Fix any arithmetic or notation discrepancies.
- For Macroeconomics Ch. 11-12, enforce the post-2020 Federal Reserve Ample-Reserves regime (IORB, ON RRP, Discount Window). For Ch. 3, keep single-market price P strictly separate from economy-wide aggregate price indexes.
- Make clean, surgical edits directly to `{tex_rel}` (if it already meets 100% of standards and passes Python math checks, return `status: "ok"` with no unnecessary churn).
- Do NOT run `convert_to_quarto.py` (the workflow runner handles Quarto conversion next).
- Call `finish` with the required JSON schema.
"""
            r_out = await agent(
                prompt=reading_prompt,
                schema=READING_SCHEMA,
                role=f"Reading: {slug}",
                model=cfg["reading_model"],
            )
            log(f"[{slug}] Stage 1 result: status={r_out['status']} math={r_out['math_verified']} checkpoints={r_out['has_bih_ciu_wio']} | {r_out['edits_summary'][:140]}")
            if r_out["status"] in ("ok", "skipped") and r_out["math_verified"]:
                result["reading_done"] = True
            else:
                result["errors"].append(f"Reading stage issue: {r_out['notes']}")

        # Attempt targeted Quarto conversion (graceful fallback if MiKTeX is blocked by sandbox)
        if not cfg["skip_reading"]:
            rc_q, out_q = run_cmd([PYTHON, "convert_to_quarto.py", "--chapter", slug])
            if rc_q == 0:
                result["web_done"] = True
                log(f"[{slug}] Quarto sync OK")
            else:
                if "MiKTeX" in out_q or "Access is denied" in out_q or "TikZ figure failed" in out_q:
                    result["web_note"] = "Run convert_to_quarto.py outside sandbox for TikZ SVG"
                    log(f"[{slug}] Quarto sync deferred (MiKTeX sandbox restriction)")
                else:
                    result["web_note"] = f"Quarto sync error: {out_q[-200:]}"
                    log(f"[{slug}] Quarto sync warning: {out_q[-200:]}")

        # ------------------------------------------------------------------
        # STAGE 2: 50-Question Universal v2.0 Bank + Auto-Repair + QTI Export
        # ------------------------------------------------------------------
        quiz_path = ROOT / quiz_rel
        rc_pre, out_pre = (1, "missing") if not quiz_path.exists() else run_cmd(
            [PYTHON, "tools/validate_qbank.py", quiz_rel, "--strict"]
        )

        if not cfg["skip_quiz"]:
            if rc_pre == 0 and not cfg["force_quiz"]:
                log(f"[{slug}] Stage 2: {quiz_rel} already passes strict v2.0 validation (skipping re-author)")
                result["quiz_done"] = True
            else:
                log(f"[{slug}] Stage 2: Authoring/upgrading 50-question v2.0 bank -> {quiz_rel}")
                existing_note = (
                    f"An existing partial/legacy file exists at `{quiz_rel}`. If it already contains valid v2.0 items, you may keep and complete them to 50; if it is legacy `(Variant N)` templates, replace it completely with 50 fresh, unique v2.0 items."
                    if quiz_path.exists()
                    else f"No quiz file exists yet; create `{quiz_rel}` from scratch."
                )
                quiz_prompt = f"""Build the production 50-question Universal Question Bank v2.0 file `{quiz_rel}` for {course_title}, Chapter {ch_num}.

Read ONLY these files first (do NOT scan the rest of the repo):
1. `docs/UNIVERSAL_QBANK_SCHEMA.md`
2. `{tex_rel}`
{f'3. `{quiz_rel}` (first 60 lines only to check if partial v2 or legacy)' if quiz_path.exists() else ''}

Context:
- {existing_note}
- Course: `{course_title}`
- `chapter_id`: `"{course}_ch{ch_num:02d}"`
- `file_stem`: `"{stem}"`
- `benchmark`: `"{benchmark_for(course)}"`
- Question ID prefix: `"{course.upper()}_CH{ch_num:02d}_T<tier>_<01..13>"` (unique across all 50 items)
- `clo_alignment`: use chapter learning outcomes from `{tex_rel}` (or `["{clo_prefix_for(course)}-1"]`..`["{clo_prefix_for(course)}-4"]` if none numbered).

Hard Quality & Schema Requirements:
1. Exactly **50 unique multiple-choice questions**:
   - Tier 1 (`Tier 1: Conceptual / Definitional`): 13 questions
   - Tier 2 (`Tier 2: Graphical / Curve Shift Interpretation`): 13 questions
   - Tier 3 (`Tier 3: Quantitative / Step-by-Step Calculation`): 12 questions
   - Tier 4 (`Tier 4: Critical Thinking / Empirical Policy Application`): 12 questions
2. Align directly to the canonical models, terminology, equations, figures, and worked examples in `{tex_rel}`. Zero fabricated empirical statistics or FRED codes.
3. Every Tier 3 calculation MUST evaluate to clean integers or terminating decimals; write and execute a short Python verification script to independently verify ALL 12 Tier 3 correct answers AND confirm every distractor is mathematically distinct and reflects a genuine student calculation fallacy.
4. Every question must have:
   - Exactly 4 distinct options (`opt_a`, `opt_b`, `opt_c`, `opt_d`), exactly 1 `is_correct: true` matching `evaluation.correct_option_id`.
   - Specific diagnostic `feedback` on ALL 4 options (correct option reinforces reasoning; each wrong option names the exact misconception/fallacy and explains why it is wrong).
   - Exactly 2 progressive `hints`: `[{{"tier": 1, "text": "..."}}, {{"tier": 2, "text": "..."}}]`.
   - Zero `(Variant N)` boilerplate and zero duplicate `prompt_template` strings.
   - If any item uses parameterized `{{var}}` placeholders, ensure `parameters` includes concrete `default` values AND `options_template[].text` contains concrete evaluated text so Canvas QTI renders cleanly.
5. Write the full JSON directly to `{quiz_rel}` (e.g., via a Python generator script in a temp/scratch file or `write_file`—NEVER dump the 50 questions into chat).
6. Run BOTH validation commands via `run_command` before finishing:
   - `python tools/validate_qbank.py {quiz_rel} --strict`
   - `python tools/build_qti.py {quiz_rel} --shuffle`
   Fix any reported errors before calling `finish`.
"""
                quiz_agent = agent(
                    role=f"Quiz 50Q: {slug}",
                    model=cfg["quiz_model"],
                )
                try:
                    q_out = await quiz_agent(quiz_prompt, QUIZ_SCHEMA)
                    log(f"[{slug}] Stage 2 agent finished: status={q_out['status']} n={q_out['questions_written']} math={q_out['tier3_math_verified']}")

                    # Independent workflow verification gate + 1 automatic repair pass if needed
                    rc_v, out_v = run_cmd([PYTHON, "tools/validate_qbank.py", quiz_rel, "--strict"])
                    if rc_v != 0:
                        log(f"[{slug}] Strict validation failed; running auto-repair pass...")
                        repair_prompt = f"""`python tools/validate_qbank.py {quiz_rel} --strict` failed with:

{out_v}

Fix every reported error in `{quiz_rel}`, re-run `python tools/validate_qbank.py {quiz_rel} --strict` and `python tools/build_qti.py {quiz_rel} --shuffle` until both exit 0, then call `finish`."""
                        q_out = await quiz_agent(repair_prompt, QUIZ_SCHEMA)
                        rc_v, out_v = run_cmd([PYTHON, "tools/validate_qbank.py", quiz_rel, "--strict"])

                    if rc_v == 0:
                        result["quiz_done"] = True
                        log(f"[{slug}] Strict validation PASS: {out_v}")
                    else:
                        result["errors"].append(f"validate_qbank failed: {out_v[:300]}")
                finally:
                    del quiz_agent

            # Build QTI 1.2 package if quiz passed strict validation
            if result["quiz_done"]:
                rc_qti, out_qti = run_cmd([PYTHON, "tools/build_qti.py", quiz_rel, "--shuffle"])
                if rc_qti == 0 and (ROOT / qti_rel).exists():
                    result["qti_done"] = True
                    log(f"[{slug}] QTI export OK: {out_qti}")
                else:
                    result["errors"].append(f"build_qti failed: {out_qti[:250]}")

        # Compose concise tracker note
        if not result["errors"]:
            if result["reading_done"] and result["quiz_done"] and result["qti_done"]:
                result["tracker_note"] = (
                    "Audited + 50Q v2 + QTI ready"
                    if result["web_done"]
                    else "Audited + 50Q v2 + QTI ready (sync .qmd outside sandbox)"
                )
        else:
            result["tracker_note"] = "Needs attention: " + "; ".join(result["errors"])[:90]

    except Exception as exc:
        result["errors"].append(f"Unhandled error: {exc}")
        log(f"[{slug}] ERROR: {exc}")

    return result


# ==============================================================================
# MAIN WORKFLOW ENTRYPOINT
# ==============================================================================
phase("Preflight & Target Selection")
tracker = parse_tracker()
cfg = {
    "force_reading": bool(args.get("force_reading", False)),
    "force_quiz": bool(args.get("force_quiz", False)),
    "skip_reading": bool(args.get("skip_reading", False)),
    "skip_quiz": bool(args.get("skip_quiz", False)),
    "reading_model": args.get("reading_model", "inherit"),
    "quiz_model": args.get("quiz_model", "inherit"),
}

target_chapters = args.get("chapters")
if not target_chapters:
    sprint = args.get("sprint", "S1")
    target_chapters = [slug for slug, info in tracker.items() if info["sprint"] == sprint]

if not target_chapters:
    raise ValueError("No target chapters resolved from Args (`chapters` or `sprint`).")

log(f"Running curriculum workflow for {len(target_chapters)} chapter(s): {', '.join(target_chapters)}")

phase("Run Per-Chapter Isolated Pipelines")
results = await parallel(
    target_chapters,
    lambda slug: process_chapter(slug, tracker.get(slug, {}), cfg),
)

phase("Update Tracker & Final Verification")
update_tracker(results)
rc_all, dash = run_cmd([PYTHON, "tools/validate_qbank.py", "--all"])

summary_lines = ["\n=== SPRINT WORKFLOW SUMMARY ==="]
deferred_web = []
for r in results:
    status = "PASS" if not r["errors"] else f"ISSUES ({len(r['errors'])})"
    summary_lines.append(
        f"- {r['slug']:42s} | Reading:{'OK' if r['reading_done'] else 'NO'} | Web:{'OK' if r['web_done'] else 'DEFER'} | Quiz50:{'OK' if r['quiz_done'] else 'NO'} | QTI:{'OK' if r['qti_done'] else 'NO'} | {status}"
    )
    if r["errors"]:
        for e in r["errors"]:
            summary_lines.append(f"    ! {e}")
    if r["reading_done"] and not r["web_done"]:
        deferred_web.append(r["slug"])

if deferred_web:
    flags = " ".join(f"--chapter {s}" for s in deferred_web)
    summary_lines.append(f"\nDeferred Quarto TikZ sync command (run outside sandbox):\n  python convert_to_quarto.py {flags}")

summary_lines.append("\n" + dash)
report = "\n".join(summary_lines)
print(report)
log("Workflow complete.")
