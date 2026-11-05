# ==============================================================================
# Makefile: Economics Curriculum Automated PDF Compilation
# ==============================================================================

LATEXMK = latexmk
BUILD_FLAGS = -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all micro macro clean micro_ch01 micro_ch03 html_ch03 qti_ch03 check_ch03

all: micro macro

# Build Microeconomics Chapters
micro: micro_ch01 micro_ch03

micro_ch01:
	cd micro/chapters && $(LATEXMK) $(BUILD_FLAGS) ch01_principles.tex

micro_ch03:
	cd micro/chapters && $(LATEXMK) $(BUILD_FLAGS) ch03_supply_demand.tex

# Canvas outputs (need pandoc, pdflatex, pymupdf)
html_ch03:
	python tools/build_html.py micro/chapters/ch03_supply_demand.tex

qti_ch03:
	python tools/build_qti.py micro/quizzes/ch03_quiz.json

# Recompute every number used in the chapter and quiz
check_ch03:
	python tools/check_math.py

# Build Macroeconomics Chapters (placeholder targets for chapters)
macro:
	@echo "Compiling macro chapters..."
	# Add compiled chapters here once migrated

# Clean LaTeX build artifacts
clean:
	find . -type f \( \
		-name "*.aux" -o \
		-name "*.bbl" -o \
		-name "*.bcf" -o \
		-name "*.blg" -o \
		-name "*.fdb_latexmk" -o \
		-name "*.fls" -o \
		-name "*.log" -o \
		-name "*.out" -o \
		-name "*.run.xml" -o \
		-name "*.synctex.gz" -o \
		-name "*.toc" \
	\) -delete
	@echo "Cleaned all auxiliary build artifacts."

distclean: clean
	find . -type f -name "*.pdf" -delete
	@echo "Cleaned all output PDF files."
