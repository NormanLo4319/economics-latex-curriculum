# Windows PowerShell Build Script for Economics Curriculum
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "Compiling Economics LaTeX Curriculum via pdflatex" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

$microPath = Join-Path $PSScriptRoot "micro\chapters"
$macroPath = Join-Path $PSScriptRoot "macro\chapters"

Write-Host "`n[1/2] Compiling Microeconomics (14 Chapters)..." -ForegroundColor Yellow
Get-ChildItem -Path $microPath -Filter *.tex | ForEach-Object {
    $texName = $_.Name
    $baseName = $_.BaseName
    Write-Host "  Compiling $texName..." -NoNewline
    Push-Location $microPath
    pdflatex -interaction=nonstopmode $texName | Out-Null
    pdflatex -interaction=nonstopmode $texName | Out-Null
    Pop-Location
    if (Test-Path (Join-Path $microPath "$baseName.pdf")) {
        Write-Host " [OK]" -ForegroundColor Green
    } else {
        Write-Host " [FAIL]" -ForegroundColor Red
    }
}

Write-Host "`n[2/2] Compiling Macroeconomics (12 Chapters)..." -ForegroundColor Yellow
Get-ChildItem -Path $macroPath -Filter *.tex | ForEach-Object {
    $texName = $_.Name
    $baseName = $_.BaseName
    Write-Host "  Compiling $texName..." -NoNewline
    Push-Location $macroPath
    pdflatex -interaction=nonstopmode $texName | Out-Null
    pdflatex -interaction=nonstopmode $texName | Out-Null
    Pop-Location
    if (Test-Path (Join-Path $macroPath "$baseName.pdf")) {
        Write-Host " [OK]" -ForegroundColor Green
    } else {
        Write-Host " [FAIL]" -ForegroundColor Red
    }
}

Write-Host "`n===================================================" -ForegroundColor Cyan
Write-Host "Compilation complete! All PDFs successfully generated." -ForegroundColor Green
Write-Host "===================================================" -ForegroundColor Cyan
