import unittest

from sync_readings_to_tex import tex_caption_to_alt


class TexCaptionAltTests(unittest.TestCase):
    def test_preserves_currency_symbols_inside_inline_math(self):
        caption = r"At $\$80$, demand is $Q_d=10$."

        self.assertEqual(tex_caption_to_alt(caption), "At $80, demand is Q_d=10.")

    def test_removes_tex_markup_and_unescapes_currency_outside_math(self):
        caption = r"\textbf{Real values} use \$5 \& more."

        self.assertEqual(tex_caption_to_alt(caption), "Real values use $5 & more.")


if __name__ == "__main__":
    unittest.main()
