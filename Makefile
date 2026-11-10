PDFLATEX = pdflatex -interaction=nonstopmode

.PHONY: all micro macro clean

all: micro macro

micro:
	@echo "Compiling all micro chapters via pdflatex..."
	cd micro/chapters && for f in *.tex; do $(PDFLATEX) $$f && $(PDFLATEX) $$f; done

macro:
	@echo "Compiling all macro chapters via pdflatex..."
	cd macro/chapters && for f in *.tex; do $(PDFLATEX) $$f && $(PDFLATEX) $$f; done

clean:
	find . -type f \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.synctex.gz" -o -name "*.fls" -o -name "*.fdb_latexmk" \) -delete
	@echo "Cleaned auxiliary LaTeX artifacts."
