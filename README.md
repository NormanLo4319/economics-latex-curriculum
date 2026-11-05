# economics-latex-curriculum

Reusable Principles of Economics course content, written once in LaTeX and built into a PDF, a Canvas page, and a Canvas quiz.

- **Micro** follows the topic order of Chiang, *Microeconomics*.
- **Macro** follows the topic order of Krugman and Wells, *Macroeconomics*.
- All text is original. It aligns with the books by topic and chapter number and does not copy their text, figures, examples or problems.

## Layout

```
shared/            preamble, TikZ styles, boxes (edit once, applies to every chapter)
micro/chapters/    one .tex file per chapter
micro/quizzes/     one question bank (JSON) per chapter
macro/chapters/    (not started)
tools/             build_html.py, build_qti.py, check_math.py
build/             generated output (not committed)
```

## Build

Requires `pdflatex` (MiKTeX or TeX Live), `pandoc`, and `pip install pymupdf`.

```
pdflatex micro/chapters/ch03_supply_demand.tex   # run twice for the table of contents
python tools/check_math.py                       # recompute every number in the chapter and quiz
python tools/build_html.py micro/chapters/ch03_supply_demand.tex
python tools/build_qti.py micro/quizzes/ch03_quiz.json
```

`make micro_ch03`, `make html_ch03`, `make qti_ch03`, `make check_ch03` do the same when `make` and `latexmk` (needs Perl) are installed.

## Getting content into Canvas (no API token needed)

- **Page:** open `build/html/<chapter>.html`, copy the content, and paste it into the Canvas page HTML editor. Upload `build/html/figures/*.png` to Canvas Files and update the image links.
- **Quiz:** Settings > Import Course Content > "QTI .zip file" > choose `build/qti/<name>_qti.zip`.
- **Math:** by default the HTML uses `\( ... \)` inline and `$$ ... $$` display, which Canvas MathJax renders. Use `--math dollar` to get `$ ... $` instead. Test one page in a sandbox course before bulk use.

## Quality rules

- Every chapter and quiz item names its outcome ID (see the project foundation documents).
- Every numeric answer is recomputed in `tools/check_math.py`.
- Every wrong answer choice states why it is wrong.
- FRED series codes are verified on FRED before use.
- Each chapter header carries a review status. Do not publish a chapter marked DRAFT.
- No student names, IDs or grade records in this repository.
