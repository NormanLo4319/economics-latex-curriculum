# CHAPTER 6: TikZ Visualization Specification
## Macroeconomics: Saving, Investment Spending, and the Financial System

**Date:** November 17, 2026  
**Status:** Ready for TikZ Rendering  
**Priority:** CRITICAL (5–6 figures required for publication)  
**Deadline:** December 15, 2026  

---

## OVERVIEW

Chapter 6 (Macroeconomics) requires 5–6 coordinate graphs to support the loanable funds model, fiscal crowding out, and open-economy dynamics. All specifications use:

- **Coordinate System:** Clean $(0, 0)$ origin with labeled axes
- **Color Palette:** Okabe-Ito colorblind-safe (defined below)
- **Line Styles:** Solid for primary curves; dashed/dotted for guides and shifts
- **Fonts:** Standard LaTeX math mode; no unicode subscripts
- **Format:** TikZ/pgfplots code (embeddable in .tex) or exportable to .svg/.png

---

## OKABE-ITO COLORBLIND-SAFE PALETTE (REQUIRED)

```
% LaTeX color definitions (already in preamble)
\definecolor{CourseBlue}{HTML}{0072B2}        % Demand, MB, Baseline (Deep Blue)
\definecolor{CourseOrange}{HTML}{D55E00}      % Supply, MC, Comparison (Vermilion-Orange)
\definecolor{CourseTeal}{HTML}{009E73}        % Secondary curve, shifted condition (Bluish-Green)
\definecolor{CoursePurple}{HTML}{CC79A7}      % Accent, alternative shift (Reddish-Purple)
\definecolor{CourseAmber}{HTML}{E69F00}       % Fiscal revenue, neutral highlight (Warm Amber)
\definecolor{CourseSlate}{HTML}{1E293B}       % Axes, grids, labels, dashed guides (Dark Slate)
```

**RULE:** No red-green pairs. All curves must use one color from the palette above. Dashed/dotted guide lines and axis labels must use CourseSlate.

---

## FIGURE 1: Saving Flow → Wealth Stock Timeline

**Location:** Section 2 (Saving vs Wealth)  
**Purpose:** Conceptual distinction between annual saving (flow) and accumulated wealth (stock)  
**Type:** Timeline diagram (not a coordinate graph)

### Specification

```
Frame width: 12 cm
Timeline: horizontal, 5 time periods (Year 0–4)
Saving bars: Annual increments (+$5k, +$10k, +$8k, +$7k, +$9k)
Wealth line: Cumulative stack showing $5k → $15k → $23k → $30k → $39k
Color: CourseBlue for saving bars, CourseTeal for cumulative wealth line
Labels: 
  - Y-axis: "Annual Saving (in thousands, $)"
  - X-axis: "Year"
  - Each bar: "$5k", "$10k", etc.
  - Wealth line annotations: "$5k", "$15k", "$23k", "$30k", "$39k"
Caption: "Annual saving represents flows each year. Accumulated wealth represents the stock of assets. 
Starting with $0 in wealth and $5k annual saving, we build to $39k wealth by Year 4."
```

### Notes
- Use side-by-side bars (grouped by year) with line overlay for cumulative wealth
- Ensure no text overlaps bars or line
- Include y-axis grid lines at $5k, $10k, $15k, etc.

---

## FIGURE 2: GDP Identity Decomposition (Y = C + I + G + NX)

**Location:** Section 3 (National Saving)  
**Purpose:** Visualize the accounting identity and show savings channel  
**Type:** Stacked bar chart or waterfall diagram

### Specification

```
Single period (Year 2024)
GDP: $27,000 billion (US, BEA, quarterly × 4 annualized)
Components (stacked horizontally):
  - C = $19,350B (71.7%) — CourseBlue
  - I = $4,320B (16.0%) — CourseOrange
  - G = $5,000B (18.5%) — CourseTeal
  - NX = -$1,670B (-6.2%) — CoursePurple

Accounting check: Y = C + I + G + NX
$27,000 = $19,350 + $4,320 + $5,000 - $1,670 ✓

Y-axis: "GDP Components (billions USD)"
X-axis: "2024 (Annualized Quarterly Data, BEA)"
Stacked bar: Left-to-right order: C, I, G (then NX offset below if negative)
Color gradient: Use palette colors to distinguish components
Callout annotation: "National Saving S = Y - C - G = $2,350B"
```

### Notes
- Use stacked bar (horizontal) for clarity
- Negative NX (import surplus) can be shown as offset or inverted segment
- Include reference callout showing S = Y - C - G = $2,350B
- Source line: "(Source: U.S. Bureau of Economic Analysis, 2024)"

---

## FIGURE 3: Closed vs. Open Economy Comparison

**Location:** Section 3 (National Saving)  
**Purpose:** Show how trade deficits affect national saving and capital flows  
**Type:** Side-by-side accounting identity bars

### Specification

```
Two scenarios: Closed Economy vs. Open Economy

CLOSED ECONOMY:
  Y = C + I + G (always balanced)
  S = I (saving must equal investment)
  Example: Y=$1000, C=$650, G=$200, I=S=$150

OPEN ECONOMY:
  Y = C + I + G + NX
  S = I + NX (saving funds investment + net exports)
  Example: Y=$1000, C=$650, G=$200, I=$180, NX=-$30, S=$150

Layout: Two columns, stacked bar or identity breakdown
Colors:
  - Saving (S): CourseBlue
  - Investment (I): CourseOrange
  - Trade deficit (−NX): CoursePurple
  - Closed loop closure: CourseTeal accent

Y-axis: "$ Billions (Hypothetical)"
Closed panel: S=$150 → I=$150
Open panel: S=$150 → I=$180 (private investment) − NX=$30 (net capital inflow)

Callout equations:
  Closed: S = I
  Open: S = I + NX (trade deficit means capital inflow)

Caption: "In closed economy, all saving funds domestic investment. In open economy, 
trade deficits (negative NX) attract foreign capital, allowing I > S."
```

### Notes
- Ensure equation annotations do not overlap bars
- Use dashed slate guide lines from bars to equations
- Include footnote on hypothetical numbers vs. 2024 actual data

---

## FIGURE 4: LOANABLE FUNDS EQUILIBRIUM (CRITICAL)

**Location:** Section 4 (Loanable Funds Market)  
**Purpose:** Show supply and demand for loanable funds; identify equilibrium interest rate and quantity  
**Type:** Coordinate graph (downward Demand, upward Supply)

### Specification — CRITICAL CORRECTNESS

```
Coordinate Plane:
  X-axis (Horizontal): "Quantity of Loanable Funds ($ billions)"
  Y-axis (Vertical): "Real Interest Rate, r (%)"
  
  X-range: 0–300 (billions)
  Y-range: 0–8 (percent)
  
  Origin: (0, 0) explicitly marked
  
  Axes labeled: "Q" (horizontal, right end)
               "r (%)" (vertical, top end)

SUPPLY CURVE (Loanable Funds Supplied by Savers):
  Equation: r = 0.5 + 0.025Q
  Points:
    Q=100 → r=3.0%
    Q=140 → r=4.0%
    Q=200 → r=5.5%
    Q=300 → r=8.0%
  Slope: +0.025 (upward, positive)
  Style: Solid CourseOrange line, width=2pt
  Label: "Supply of Loanable Funds (S)" at right endpoint, offset above line, 
         color CourseOrange, font size small
  
DEMAND CURVE (Loanable Funds Demanded by Borrowers):
  Equation: r = 6.8 − 0.02Q
  Points:
    Q=0 → r=6.8%
    Q=100 → r=4.8%
    Q=140 → r=4.0%
    Q=200 → r=2.8%
    Q=300 → r=0.8%
  Slope: −0.02 (downward, negative)
  Style: Solid CourseBlue line, width=2pt
  Label: "Demand for Loanable Funds (D)" at right endpoint, offset below line,
         color CourseBlue, font size small

EQUILIBRIUM POINT:
  Intersection: Q* = 140 (billions), r* = 4.0%
  Visual marker: Solid black dot or small circle at (140, 4)
  Dashed guide lines: 
    - Vertical dashed slate line from (140, 4) to x-axis, label "Q*=140B"
    - Horizontal dashed slate line from (140, 4) to y-axis, label "r*=4%"
  Label at intersection: "E* (Equilibrium)" with optional arrow, font bold small

GRID:
  Major grid lines: Every 50 on x-axis, every 1% on y-axis
  Grid style: Light gray dashed, 0.5pt, opacity 0.4
  No grid labels inside plot area

ANNOTATIONS:
  Title (above plot): "Loanable Funds Market Equilibrium"
  Caption (below plot): "The supply of loanable funds (upward curve) intersects 
                        demand (downward curve) at Q*=140B and r*=4%. At this 
                        equilibrium, quantity supplied = quantity demanded, 
                        and there is no tendency for the interest rate to change."

SOURCE LINE: (optional, below caption)
  "Source: Hypothetical data for pedagogical illustration."

SIZE: 10 cm (width) × 7 cm (height)
```

### Visual Standards (MUST VERIFY)
- ✅ No text overlaps curves or grid lines
- ✅ Axis labels use CourseSlate (#1E293B) in standard LaTeX font
- ✅ Curves use only CourseBlue (Demand) and CourseOrange (Supply)
- ✅ Equilibrium marker is distinct and clearly labeled
- ✅ Dashed guide lines use CourseSlate and do not interfere with curves
- ✅ All numbers on axes are legible (font size ≥ 9pt)

### Verification Checklist
- [ ] Curves computed correctly (double-check arithmetic)
- [ ] Intersection at (140, 4) verified: 0.5 + 0.025(140) = 4.0 ✓; 6.8 − 0.02(140) = 4.0 ✓
- [ ] Axes scaled appropriately (not cramped, not wasted space)
- [ ] Colors render correctly on screen and print
- [ ] All labels visible and unambiguous
- [ ] MathJax/LaTeX math mode used for $r$, $Q$, $Q^*$, $r^*$

---

## FIGURE 5: CROWDING OUT—FISCAL DEFICIT SHIFTS SUPPLY (CRITICAL)

**Location:** Section 5 (Deficits and Crowding Out)  
**Purpose:** Show how government deficit reduces private saving (shifts supply left), 
           raises interest rate, and crowds out investment  
**Type:** Two-panel coordinate graph (Before/After) or single graph with shift annotation

### Specification — CRITICAL CORRECTNESS

```
OPTION A (RECOMMENDED): Single Graph with Shift Annotation

Coordinate Plane:
  X-axis: "Quantity of Loanable Funds ($ billions)"
  Y-axis: "Real Interest Rate, r (%)"
  X-range: 0–300, Y-range: 0–8
  Origin: (0, 0) explicitly marked

INITIAL EQUILIBRIUM (No Deficit):
  Supply 1: r = 0.5 + 0.025Q  [Same as Figure 4]
  Demand 1: r = 6.8 − 0.02Q  [Same as Figure 4]
  E₁: (Q₁* = 140, r₁* = 4%)
  
  Supply curve style: Solid CourseOrange, width=2pt
  Demand curve style: Solid CourseBlue, width=2pt
  Equilibrium 1 marker: Solid dot at (140, 4), label "E₁" in CourseSlate
  Dashed guides: Vertical and horizontal, labeled Q₁*, r₁*

NEW EQUILIBRIUM (With Deficit):
  Supply 2: r = 0.9 + 0.025Q  [Supply shifted LEFT due to deficit]
           (Intercept increased from 0.5 to 0.9; slope unchanged)
           Pedagogical reason: Government deficit reduces net private saving
  Demand 2: r = 6.8 − 0.02Q  [Unchanged—government borrowing demand NOT added here]
           (Alternative: Demand could shift RIGHT if modeling govt bond demand explicitly)
           
  E₂: Solve 0.9 + 0.025Q = 6.8 − 0.02Q
      0.045Q = 5.9
      Q₂* = 131.1 ≈ 130B
      r₂* = 0.9 + 0.025(130) = 4.15% ≈ 4.25%
  
  Supply 2 curve style: Dashed CourseTeal, width=2pt
  Demand 2 (if unchanged): Solid CourseBlue, width=2pt
  Equilibrium 2 marker: Solid dot at (130, 4.25), label "E₂" in CourseSlate
  Dashed guides: Vertical and horizontal, labeled Q₂*, r₂*
  Shift arrow: Curved arrow from "E₁" to "E₂" in CoursePurple, labeled "Deficit increases r, reduces Q"

ANNOTATIONS:
  Arrow or bracket showing:
    ΔQ = 140 − 130 = 10B (crowding out of investment)
    Δr = 4.25% − 4% = 0.25% (rise in interest rate)
  
  Callout box (white background, slight transparency):
    "Government Budget Deficit:
     ↓ National Saving (net private saving − deficit)
     ⟹ Supply curve shifts left
     ⟹ r ↑ (interest rate rises)
     ⟹ I ↓ (private investment crowded out)
     Crowding-out effect: ΔI ≈ 10B"
  
  Title: "Fiscal Deficit and Crowding Out in Loanable Funds Market"
  Caption: "When government runs a deficit, it absorbs private saving, reducing 
            net supply of loanable funds. The supply curve shifts left from S₁ to S₂. 
            Equilibrium moves from E₁ to E₂: interest rate rises, and private investment 
            is crowded out by approximately $10B."

SIZE: 10 cm (width) × 7 cm (height)
```

### OPTION B (ALTERNATIVE): Two-Panel Side-by-Side

```
LEFT PANEL: "Equilibrium Without Deficit"
  Supply: r = 0.5 + 0.025Q (CourseOrange)
  Demand: r = 6.8 − 0.02Q (CourseBlue)
  E₁: (140, 4%)
  Smaller size: 8 cm × 6 cm

RIGHT PANEL: "Equilibrium With Deficit"
  Supply: r = 0.9 + 0.025Q (CourseTeal, dashed or lighter)
  Demand: r = 6.8 − 0.02Q (CourseBlue)
  E₂: (130, 4.25%)
  Smaller size: 8 cm × 6 cm

BOTH PANELS share same axis ranges for easy visual comparison
Central annotation between panels: Arrow labeled "Deficit" pointing right

CAPTION (below both panels): [Same as Option A]
```

### Visual Standards (MUST VERIFY)
- ✅ Shift from E₁ to E₂ is visually clear (do not use same line style)
- ✅ Crowding-out magnitude (ΔI ≈ 10B) is prominently labeled
- ✅ All curves use correct palette colors
- ✅ Callout box background is opaque enough for text readability
- ✅ No overlapping text or arrows

### Verification Checklist
- [ ] Supply shift computation correct: 0.9 + 0.025(130) = 4.15% ✓
- [ ] Demand unchanged (or explicitly noted if added)
- [ ] Crowding-out calculation: ΔI = ΔQ = 10B ✓
- [ ] Interest rate rise: Δr ≈ 0.25% = 25 basis points ✓
- [ ] Visual clearly shows shift direction (leftward for supply reduction)

---

## FIGURE 6 (OPTIONAL): Partial Crowding Out — Bar Chart

**Location:** Section 5 (Advanced Optional Callout on Partial Crowding Out)  
**Purpose:** Illustrate empirical reality that crowding out is typically partial, 
           not 1:1 (monetary policy, spare capacity, international flows matter)  
**Type:** Grouped bar chart (3 scenarios)

### Specification

```
Three scenarios (hypothetical, illustrative):

Scenario A: "Complete Crowding Out (1:1)"
  Deficit: −$100B → I falls by $100B
  Bars: Before I=$200B (orange), After I=$100B (orange with hatch)
  Reduction: −$100B
  Label: "ΔI/ΔG = 1.0 (1:1 crowding out)"
  Color: CourseOrange

Scenario B: "Partial Crowding Out (0.6:1)"
  Deficit: −$100B → I falls by $60B
  Bars: Before I=$200B (teal), After I=$140B (teal with hatch)
  Reduction: −$60B
  Label: "ΔI/ΔG = 0.6 (partial; monetary + spare capacity)"
  Color: CourseTeal

Scenario C: "Open Economy (0.3:1)"
  Deficit: −$100B → I falls by $30B (rest funded by capital inflow)
  Bars: Before I=$200B (purple), After I=$170B (purple with hatch)
  Reduction: −$30B
  Label: "ΔI/ΔG = 0.3 (open economy; foreign capital)"
  Color: CoursePurple

X-axis: "Scenario"
Y-axis: "Private Investment ($ billions)"

Annotations:
  Above each bar pair: Magnitude of reduction (−$100B, −$60B, −$30B)
  
Caption: "Real-world crowding out is typically partial because: 
(1) Monetary policy may lower interest rates to offset deficit, 
(2) Spare production capacity allows interest-insensitive investment, 
(3) International capital flows finance deficits without crowding out domestic I. 
Here, 1:1 crowding out is an upper bound; empirical estimates often show 0.3–0.6."

NOTES: Mark this figure as OPTIONAL. It is contextual to the advanced callout 
       in Section 5 on partial crowding-out mechanism. Prioritize FIGURES 4 and 5 
       (critical equilibrium and shift diagrams) first; add Figure 6 if time permits.
```

---

## EXPORT & INTEGRATION INSTRUCTIONS

### For TikZ Source Output (.tex)

```latex
% Save each figure as standalone .tikz file, e.g.:
% assets/tikz_specifications/fig4_loanable_funds_eq.tikz
% assets/tikz_specifications/fig5_crowding_out.tikz

% In main chapter LaTeX, embed as:
\input{assets/tikz_specifications/fig4_loanable_funds_eq.tikz}
% or
\includegraphics{assets/tikz/fig4_loanable_funds_eq.pdf}
```

### For SVG/PNG Export

1. Render TikZ to PDF using `pdflatex` or `xelatex`
2. Convert PDF → SVG using `pdf2svg` or Inkscape
3. Store SVG in `assets/figures/ch06_*.svg`
4. Embed in Quarto .qmd as:
   ```markdown
   ![Figure 4: Loanable Funds Equilibrium](assets/figures/ch06_fig4_equilibrium.svg){width="80%"}
   ```

### For Web-Book (HTML/Quarto)

- MathJax will render all $r$, $Q$, $E^*$ notation
- SVG embeds natively in HTML
- PNG works via `img` tags with alt-text

---

## TESTING & VERIFICATION

### Rendering Checklist

- [ ] **Figure 1 (Timeline):** Bars + line render correctly; no text overlap
- [ ] **Figure 2 (GDP):** Stacked bar proportions correct; callout visible
- [ ] **Figure 3 (Closed vs. Open):** Two scenarios clearly distinguished
- [ ] **Figure 4 (Equilibrium - CRITICAL):** 
  - Supply curve passes through (100, 3%), (140, 4%), (200, 5.5%)
  - Demand curve passes through (100, 4.8%), (140, 4%), (200, 2.8%)
  - Curves intersect cleanly at (140, 4%)
  - Labels unambiguous; no text-on-line overlaps
- [ ] **Figure 5 (Shift - CRITICAL):** 
  - Initial equilibrium at E₁(140, 4%)
  - New equilibrium at E₂(130, 4.25%)
  - Shift direction clear (supply left); crowding out visually evident
  - Callout box readable
- [ ] **Figure 6 (Partial Crowding - OPTIONAL):** 
  - Three bars + reductions labeled
  - Color distinctions clear

### Accessibility Audit

- [ ] **Colorblind Test:** All colors validated with Okabe-Ito palette tool
- [ ] **Contrast:** Text ≥ 4.5:1 ratio against background
- [ ] **Alt-Text:** Every figure has 1–2 sentence alt-text describing:
  - Axes and their ranges
  - Curve positions and intersections
  - Key takeaway message
- [ ] **Fonts:** Standard LaTeX math; no missing glyph boxes

### Accuracy Verification

- [ ] **Arithmetic:** All equilibrium calculations double-checked
- [ ] **Equation Coherence:** Text and graph describe same model
- [ ] **Source Attribution:** FRED series or hypothetical label clear
- [ ] **Pedagogical Alignment:** Figures support 4-part blueprint narrative

---

## PRIORITY & SCHEDULING

**CRITICAL (must complete):**
1. Figure 4 — Loanable Funds Equilibrium
2. Figure 5 — Crowding Out Supply Shift

**HIGH (strongly recommended):**
3. Figure 2 — GDP Identity Decomposition
4. Figure 3 — Closed vs. Open Economy

**STANDARD:**
5. Figure 1 — Saving vs. Wealth Timeline

**OPTIONAL (if time/bandwidth):**
6. Figure 6 — Partial Crowding-Out Comparison

---

## DELIVERABLES & HANDOFF

**Output files:**
- `assets/tikz/fig1_saving_wealth_timeline.tikz` (or .pdf)
- `assets/tikz/fig2_gdp_identity.tikz` (or .pdf)
- `assets/tikz/fig3_closed_vs_open.tikz` (or .pdf)
- `assets/tikz/fig4_loanable_funds_equilibrium.tikz` (or .pdf) ← CRITICAL
- `assets/tikz/fig5_crowding_out_shift.tikz` (or .pdf) ← CRITICAL
- `assets/tikz/fig6_partial_crowding_out.tikz` (or .pdf) [OPTIONAL]

**Integration steps (after rendering):**
1. Rename files to match chapter LaTeX references
2. Update LaTeX `\input{}` or `\includegraphics{}` commands
3. Recompile Chapter 6 PDF
4. Regenerate Quarto .qmd via `convert_to_quarto.py`
5. Run `quarto render` to update web-book
6. Verify HTML rendering in browser

**QA sign-off:**
- Economics faculty peer review (accuracy)
- Accessibility team review (colorblind, contrast, alt-text)
- Final PDF/web-book sign-off before publication

---

## CONTACT & QUESTIONS

**Curriculum owner:** Norman Lo (@NormanLo4319)  
**Repository:** NormanLo4319/economics-latex-curriculum  
**Branch:** main  
**Chapter:** macro/chapters/ch06_savings_investment_financial_system.tex  

**Key constraints:**
- Use ONLY Okabe-Ito palette colors (no exceptions for red-green pairs)
- TikZ code must be self-contained and embeddable in LaTeX
- All figures must render at 600 DPI for print quality
- Deadline: December 15, 2026

---

**Version:** 1.0  
**Last Updated:** November 17, 2026  
**Status:** Ready for TikZ Rendering
