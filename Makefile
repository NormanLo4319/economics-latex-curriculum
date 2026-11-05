# ==============================================================================
# Makefile: Economics Curriculum Automated PDF Compilation
# ==============================================================================

LATEXMK = latexmk
BUILD_FLAGS = -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all micro macro clean micro_ch01

all: micro macro

# Build Microeconomics Chapters
micro: micro_ch01

micro_ch01:
	cd micro/chapters && $(LATEXMK) $(BUILD_FLAGS) ch01_principles.tex

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
