"""Build a Canvas-ready HTML page from a LaTeX chapter.

Usage: python tools/build_html.py micro/chapters/ch03_supply_demand.tex [--math canvas|dollar]

Requires: pandoc, pdflatex (MiKTeX/TeX Live), pymupdf (pip install pymupdf).
Output:   build/html/<chapter>.html and build/html/figures/*.png
Figures must be uploaded to Canvas Files and the <img> paths updated, or the
page can be delivered inside an .imscc package (see README).
"""
import argparse
import html as htmllib
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BOX_STYLES = {
    "coreprinciple": "border:2px solid #C2410C;background:#FFF7ED;border-radius:6px;padding:12px 16px;margin:16px 0;",
    "casestudy": "border:2px solid #1E293B;background:#F8FAFC;border-radius:6px;padding:12px 16px;margin:16px 0;",
    "takeaways": "border:1px solid #CBD5E1;background:#FFFFFF;border-radius:6px;padding:12px 16px;margin:16px 0;",
}
BOX_TITLE_COLOR = {"coreprinciple": "#C2410C", "casestudy": "#1E293B", "takeaways": "#1E293B"}


def find(tool, extra=()):
    path = shutil.which(tool)
    if path:
        return path
    for p in extra:
        if os.path.exists(p):
            return p
    sys.exit(f"{tool} not found on PATH")


def render_figures(tex, out_dir, preamble_dir):
    """Compile each tikzpicture to a PNG and replace it with \\includegraphics."""
    import pymupdf

    pdflatex = find("pdflatex")
    os.makedirs(out_dir, exist_ok=True)
    count = 0

    def repl(match):
        nonlocal count
        count += 1
        name = f"fig{count}"
        standalone = (
            "\\documentclass[border=6pt]{standalone}\n"
            f"\\input{{{preamble_dir}/preamble.tex}}\n"
            f"\\input{{{preamble_dir}/tikz-settings.tex}}\n"
            "\\begin{document}\n" + match.group(0) + "\n\\end{document}\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, f"{name}.tex")
            with open(src, "w", encoding="utf-8") as f:
                f.write(standalone)
            r = subprocess.run(
                [pdflatex, "-interaction=nonstopmode", "-halt-on-error", f"{name}.tex"],
                cwd=tmp, capture_output=True, text=True,
            )
            pdf = os.path.join(tmp, f"{name}.pdf")
            if r.returncode != 0 or not os.path.exists(pdf):
                sys.exit(f"Figure {count} failed to compile:\n{r.stdout[-1500:]}")
            doc = pymupdf.open(pdf)
            doc[0].get_pixmap(dpi=150).save(os.path.join(out_dir, f"{name}.png"))
            doc.close()
        return f"\\includegraphics{{figures/{name}.png}}"

    return re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", repl, tex, flags=re.S), count


def preprocess(tex):
    tex = re.sub(r"%.*", "", tex)  # strip comments (no escaped percent signs are used)
    tex = re.sub(r"\\input\{[^}]*\}", "", tex)
    tex = re.sub(r"\\(thispagestyle|tableofcontents|vspace\*?|hrule)(\{[^}]*\})?", "", tex)
    tex = re.sub(r"\\boxheader\{[^}]*\}\{([^}]*)\}", r"\\textbf{\1}\n\n", tex)
    tex = tex.replace("\\checkmark", "✓")
    tex = re.sub(r"\\begin\{(figure)\}\[[^\]]*\]", r"\\begin{\1}", tex)
    tex = re.sub(r"\\begin\{enumerate\}\[label=\(\\alph\*\)\]", r"\\begin{enumerate}[(a)]", tex)
    tex = re.sub(r"\\begin\{enumerate\}\[label=\\textbf\{\\arabic\*\.\}\]", r"\\begin{enumerate}[1.]", tex)
    tex = re.sub(r"\\begin\{enumerate\}\[label=\\textbf\{LO\\arabic\*\.\}\]", r"\\begin{enumerate}", tex)
    tex = re.sub(r"\\vspace\{[^}]*\}", "", tex)
    return tex


def style_boxes(body):
    for env, style in BOX_STYLES.items():
        body = re.sub(
            rf'<div class="{env}">',
            f'<div class="{env}" style="{style}">',
            body,
        )
    return body


def clean_display_math(body):
    """MathJax rejects equation/align environments nested inside $$ ... $$."""
    def fix(m):
        s = m.group(1)
        s = re.sub(r"\\(begin|end)\{equation\*?\}", "", s)
        s = re.sub(r"\\(begin|end)\{align\*?\}", r"\\\1{aligned}", s)
        return f'<span class="math display">\\[{s}\\]</span>'
    return re.sub(r'<span class="math display">\\\[(.*?)\\\]</span>', fix, body, flags=re.S)


def convert_math(body, mode):
    body = clean_display_math(body)
    if mode == "dollar":
        body = re.sub(r'<span class="math inline">\\\((.*?)\\\)</span>', r"$\1$", body, flags=re.S)
        body = re.sub(r'<span class="math display">\\\[(.*?)\\\]</span>', r"$$\1$$", body, flags=re.S)
    else:  # canvas: \( \) inline and $$ $$ display
        body = re.sub(r'<span class="math inline">(\\\(.*?\\\))</span>', r"\1", body, flags=re.S)
        body = re.sub(r'<span class="math display">\\\[(.*?)\\\]</span>', r"$$\1$$", body, flags=re.S)
    return body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter")
    ap.add_argument("--math", choices=["canvas", "dollar"], default="canvas")
    args = ap.parse_args()

    pandoc = find("pandoc", [os.path.expandvars(r"%LOCALAPPDATA%\Pandoc\pandoc.exe")])
    chapter = os.path.abspath(args.chapter)
    with open(chapter, encoding="utf-8") as f:
        tex = f.read()

    out_dir = os.path.join(ROOT, "build", "html")
    fig_dir = os.path.join(out_dir, "figures")
    os.makedirs(out_dir, exist_ok=True)
    shared = os.path.join(ROOT, "shared").replace("\\", "/")

    tex, nfig = render_figures(tex, fig_dir, shared)
    tex = preprocess(tex)

    m = re.search(r"\\begin\{document\}(.*)\\end\{document\}", tex, re.S)
    if not m:
        sys.exit("No document body found")
    body_tex = m.group(1)
    title = re.search(r"\\title\{.*?\\color\{SlateBlue\}\s*(.*?)\}\s*\\author", tex, re.S)
    title = re.sub(r"\\\\|\\&", "&", title.group(1)).strip() if title else os.path.basename(chapter)
    body_tex = re.sub(r"\\title\{.*?\\maketitle", "", body_tex, flags=re.S)

    with tempfile.NamedTemporaryFile("w", suffix=".tex", delete=False, encoding="utf-8") as tmp:
        tmp.write(body_tex)
        tmp_path = tmp.name
    try:
        r = subprocess.run(
            [pandoc, "-f", "latex", "-t", "html5", "--math-method=mathjax", "--shift-heading-level-by=1", "--wrap=none", tmp_path],
            capture_output=True, text=True, encoding="utf-8",
        )
    finally:
        os.unlink(tmp_path)
    if r.returncode != 0:
        sys.exit(r.stderr)

    body = style_boxes(convert_math(r.stdout, args.math))
    page = f"<h1>{htmllib.escape(title)}</h1>\n{body}\n"

    out = os.path.join(out_dir, os.path.splitext(os.path.basename(chapter))[0] + ".html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {out} ({nfig} figures, math={args.math})")


if __name__ == "__main__":
    main()
