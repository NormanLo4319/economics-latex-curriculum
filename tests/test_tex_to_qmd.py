import shutil
import tempfile
import unittest
from pathlib import Path

from sync_readings_to_tex import tex_to_qmd, tikz_to_svg


class TexToQmdTests(unittest.TestCase):
    def test_removes_document_metadata_but_keeps_reading_content(self):
        source = r"""
\documentclass{article}
\begin{document}
\title{\Huge\bfseries\color{SlateBlue} Sample Chapter}
\author{Course Author}
\date{2026}
\maketitle
\begin{abstract}
A meaningful chapter summary.
\end{abstract}
\section{GDP}
\subsection*{Conceptual Introduction}
GDP measures current production.
\end{document}
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            qmd = tex_to_qmd(source, "Sample Chapter", Path(temp_dir))

        self.assertIn('title: "Sample Chapter"', qmd)
        self.assertNotIn(r"\title", qmd)
        self.assertNotIn(r"\author", qmd)
        self.assertNotIn(r"\date", qmd)
        self.assertIn("A meaningful chapter summary.", qmd)
        self.assertIn("### Conceptual Introduction {.unnumbered}", qmd)
        self.assertIn("GDP measures current production.", qmd)


class TikzToSvgTests(unittest.TestCase):
    @unittest.skipUnless(shutil.which("latex") and shutil.which("dvisvgm"), "TeX SVG tools are unavailable")
    def test_preserves_strokes_and_converts_text_to_paths(self):
        tikz = r"""
\begin{tikzpicture}
\draw[thick] (0,0) -- (1,1);
\fill[blue, opacity=0.5] (0,0) rectangle (1,1);
\node at (0.5, 0.5) {Readable label};
\end{tikzpicture}
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            svg_path = Path(temp_dir) / "figure.svg"
            tikz_to_svg(tikz, svg_path)
            svg = svg_path.read_text(encoding="utf-8")

        self.assertIn("stroke='#000'", svg)
        self.assertIn("fill-opacity='.5'", svg)
        self.assertNotIn("<text", svg)
        self.assertNotIn("<font", svg)
        self.assertNotIn("stroke-opacity='0'", svg)
        self.assertNotIn("fill-opacity='0'", svg)


if __name__ == "__main__":
    unittest.main()
