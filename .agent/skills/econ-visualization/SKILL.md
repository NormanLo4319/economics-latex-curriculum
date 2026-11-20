---
name: econ-visualization
description: Generate publication-grade, pedagogical economic diagrams, coordinate graphs, and econometric visualizations across Python (Matplotlib), LaTeX (TikZ/PGFPlots), and SVG. Use when plotting microeconomic or macroeconomic models (supply and demand, PPF, cost curves, monopoly deadweight loss, game theory, AD-AS, Keynesian cross, loanable funds, or Ample Reserves).
---
# Economics Visualization (Econ-Visualization)

Expert assistant for generating publication-grade, pedagogically rigorous economic diagrams, market models, and empirical charts across Python (matplotlib), LaTeX (tikz and pgfplots), and inline HTML5 SVG.

## When to Use

  - Generating coordinate graphs for microeconomic or macroeconomic theory.
  - Creating clean vector diagrams for lecture slides, problem sets, and web-books.
  - Visualizing welfare economics, consumer and producer surplus, and deadweight loss.
  - Plotting empirical time series or econometric regressions with standard economic styling.

## Core Graphic Conventions for Economic Diagrams

### 1. Coordinate Planes and Axis Conventions

  - Vertical (Y) Axis: Always used for Price ($P$), Marginal Benefit ($MB$), Marginal Cost ($MC$), Interest Rate ($r$), or Wage ($W$).
  - Horizontal (X) Axis: Always used for Quantity ($Q$), Real Output / GDP ($Y$), or Labor ($L$).
  - Clean Origin: Explicitly anchor coordinate axes at $(0, 0)$ unless representing negative values.
  - Terminal Arrows: Terminate axes with directional arrows and explicit variable labels.
  - Equilibrium Drop-lines: Use dashed guide lines from equilibrium intersection points ($E^*$) down to the respective axes with clean label tags ($P^*$, $Q^*$).

### 2. Colorblind-Safe Palette & Line Styling Rules (Mandatory)

  - **Zero Red-Green Reliance & No Solid Red Lines:** Never use crimson red (`#DC2626`) for plotted curves, bars, or callout arrows. Standard red-green pairings are inaccessible to colorblind viewers and visually harsh on slides.
  - **Okabe-Ito Colorblind-Safe Palette:**
      - **Primary Curve 1 (Demand / MB / Baseline):** Deep Blue (`#0072B2`)
      - **Primary Curve 2 (Supply / MC / Comparison):** Vermilion-Orange (`#D55E00`)
      - **Secondary / Shifted Curve or Accent:** Bluish-Green / Teal (`#009E73`) or Reddish-Purple (`#CC79A7`)
      - **Fiscal Revenue / Neutral Highlight:** Warm Amber (`#E69F00`)
      - **Axes, Grids, Labels & Reference Lines:** Dark Slate (`#1E293B`)
  - **Pointer & Callout Lines:** Never use solid red arrows to point at regions or features on a graph. Use **dashed (`--`) or dotted (`:`) Dark Slate (`#1E293B`) pointer lines** (with subtle arrowheads or clean leader ticks) so callout pointers never compete with plotted economic curves.

### 3. Typography, Text-Collision Avoidance & Legibility Rules (Mandatory)

  - **Zero Text-on-Line Overlaps:** Never place text labels, equations, or region callouts directly over plotted curves, axis lines, dashed drop-lines, or directional arrows. Text intersecting a stroke is an immediate visual defect.
  - **Whitespace Offsets & Background Halos:** Position curve labels in open whitespace beyond curve endpoints or offset cleanly perpendicular to the line. When placing annotations near shaded regions or tight intersections, either use a dashed/dotted slate leader line from open whitespace or apply an opaque white text bounding box (`bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.92)` in Matplotlib; `fill=white, inner sep=2pt` in TikZ).
  - **Tick & Origin Separation:** Ensure tick labels on the vertical and horizontal axes do not collide near $(0, 0)$ or when two price/quantity levels sit close together; use leader callouts or distinct tick spacing so every number is crisp.
  - **Font Compatibility:** Use standard ASCII/LaTeX math formatting (`$BC_0$`, `$t = \$12 \rightarrow DWL = \$18$`) rather than Unicode subscripts that may render as missing glyph boxes.

### 4. Standard Model Specifications

#### Microeconomics

  - Supply and Demand: Downward-sloping Demand ($MB$), upward-sloping Supply ($MC$). Visual distinction between movements along curves (price change) and curve shifts (exogenous parameters).
  - Welfare Analysis: Shaded polygons for Consumer Surplus ($CS$), Producer Surplus ($PS$), Deadweight Loss ($DWL$), and Tax Wedges ($t = P_b - P_s$).
  - Production Possibilities Frontier (PPF): Concave frontier reflecting increasing opportunity cost ($MRT = MC_x / MC_y$). Unattainable points outside, inefficient points inside.
  - Theory of the Firm and Cost Curves: U-shaped $MC$, $ATC$, and $AVC$ curves. $MC$ must cut the minimum points of both $AVC$ (shutdown point) and $ATC$ (breakeven point).
  - Monopoly: Downward-sloping Demand with Marginal Revenue ($MR$) plotted at twice the slope ($MR = a - 2bQ$). Profit-maximizing output at $MR = MC$, price markup on Demand ($P_m$), deadweight loss triangle, and economic profit rectangle.
  - Factor Markets: Derived labor demand ($MRP_L = MP_L \times MR$), upward-sloping labor supply, and Marginal Factor Cost ($MFC_L > W$).
  - Externalities: Divergence between Marginal Social Cost ($MSC = MPC + MEC$) and private cost. Pigouvian corrective tax ($t^* = MEC$).
  - Consumer Choice: Linear budget constraint tangent to convex indifference curves ($MRS_{xy} = P_x / P_y$).

#### Macroeconomics

  - Circular Flow Model: Closed-loop real and financial flows between households, firms, factor markets, and product markets, balancing leakages ($S + T + M$) and injections ($I + G + X$).
  - Loanable Funds: Real interest rate ($r$) vs. Quantity of loanable funds. Budget deficits shifting supply leftward and crowding out private investment ($I$).
  - Keynesian Cross: $45^\circ$ reference line ($Y = AE$) intersecting planned expenditure ($AE = C + I + G + NX$).
  - AD-AS Equilibrium: Downward-sloping Aggregate Demand ($AD$), upward-sloping Short-Run Aggregate Supply ($SRAS$), and vertical Long-Run Aggregate Supply ($LRAS$ at potential output $Y^*$).
  - Federal Reserve Ample-Reserves Framework: Administered rate corridor showing the Discount Rate ceiling, Interest on Reserve Balances ($IORB$) anchor, and Overnight Reverse Repo ($ON\ RRP$) sub-floor intersecting vertical supply of reserves.
  - Open Economy: The Mundell-Fleming policy trilemma (Impossible Trinity).

## Implementation Rules by Format

### A. Python (Matplotlib)

  - Hide top and right spines using `ax.spines[['top', 'right']].set_visible(False)`.
  - Use the Okabe-Ito colorblind-safe palette: Dark Slate (`#1E293B`) for axes and dashed/dotted callout pointers, Deep Blue (`#0072B2`) for Demand/MB, Vermilion-Orange (`#D55E00`) for Supply/MC, and Bluish-Green/Teal (`#009E73`) or Purple (`#CC79A7`) for secondary curves/regions.
  - Shade welfare areas using `ax.fill_between()` with `alpha=0.16` to `0.26`.
  - Set explicit axis limits starting at 0 with modest padding.
  - Always verify visually that zero labels touch curves, dashed lines, or tick marks.

### B. LaTeX (TikZ and PGFPlots)

  - Output self-contained or embeddable `tikzpicture` environments.
  - Define reusable styles for axes, curves, dashed projection drop-lines, and dashed/dotted slate callout pointers.
  - Use `fill[color=...]` with low opacity for surplus areas.

### C. HTML5 Responsive SVG

  - Use semantic `<svg>` containers with `viewBox="0 0 650 400"`.
  - Implement clean inline CSS styling with high-contrast text labels.
