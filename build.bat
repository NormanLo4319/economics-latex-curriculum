@echo off
setlocal enabledelayedexpansion
echo ===================================================
echo Compiling Economics LaTeX Curriculum via pdflatex
echo ===================================================

echo.
echo [1/2] Compiling Principles of Microeconomics (14 Chapters)...
cd micro\chapters
for %%f in (*.tex) do (
    echo   Compiling %%f...
    pdflatex -interaction=nonstopmode "%%f" >nul 2>&1
    pdflatex -interaction=nonstopmode "%%f" >nul 2>&1
    if exist "%%~nf.pdf" (
        echo     [OK] %%~nf.pdf
    ) else (
        echo     [FAIL] %%~nf
    )
)
cd ..\..

echo.
echo [2/2] Compiling Principles of Macroeconomics (12 Chapters)...
cd macro\chapters
for %%f in (*.tex) do (
    echo   Compiling %%f...
    pdflatex -interaction=nonstopmode "%%f" >nul 2>&1
    pdflatex -interaction=nonstopmode "%%f" >nul 2>&1
    if exist "%%~nf.pdf" (
        echo     [OK] %%~nf.pdf
    ) else (
        echo     [FAIL] %%~nf
    )
)
cd ..\..

echo.
echo ===================================================
echo Compilation complete! All PDFs generated.
echo ===================================================
pause
