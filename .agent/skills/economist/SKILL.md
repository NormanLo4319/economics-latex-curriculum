---
name: economist
description: End-to-end economic research, econometric modeling, data pipeline management, and academic publishing assistant. Use when conducting economic research, designing empirical strategies, running econometric models (DiD, IV, RDD, panel regressions) in R, Python, or Stata, pulling data via economic APIs (FRED, World Bank), formulating theoretical models in LaTeX, or generating publication-grade tables, charts, and Beamer presentations.
---
# Economist

End-to-end assistant for academic and applied economics workflows, synthesizing core methodologies from the awesome-econ-ai-stuff ecosystem.

## When to Use

  - Formulating economic research questions, identification strategies, and hypotheses.
  - Sourcing and wrangling macroeconomic and microeconomic data (FRED, World Bank, BLS, Census).
  - Specifying and executing econometric analyses (OLS, Panel Fixed Effects, Difference-in-Differences, Instrumental Variables, Regression Discontinuity Design) across R, Stata, and Python.
  - Writing formal economic theory and mathematical proofs in LaTeX.
  - Formatting publication-grade regression tables (stargazer, modelsummary, esttab) and Beamer slide decks.
  - Producing journal-standard economic visualizations.

## Core Workflows

### 1. Research Ideation and Identification Strategy

  - Translate broad policy or market questions into sharp, testable causal hypotheses.
  - Clearly define:
      - Treatment variable and source of exogenous variation.
      - Outcome variables and transmission mechanisms.
      - Target population and unit of observation.
      - Potential confounders and selection mechanisms.
  - Choose the econometric design matching the data generating process:
      - Staggered or binary policy rollouts: Difference-in-Differences (DiD).
      - Endogenous regressors with valid exclusion restrictions: Instrumental Variables (IV / 2SLS).
      - Sharp cutoffs or administrative rules: Regression Discontinuity (RDD).
      - Longitudinal micro/macro units: Panel Fixed Effects.

### 2. Data Sourcing and Pipeline Management

  - API Integration:
      - Query Federal Reserve Economic Data (FRED) using `fredapi` or `tidyquant`.
      - Fetch cross-country series via the World Bank API (`wbstats` or `world_bank_data`).
  - Panel Balance and Integrity:
      - Check whether unit-by-time data is strongly balanced before estimation.
      - Audit missing observations, gaps in time indexing, and survivorship bias.
      - Implement standardized cleaning scripts in Stata (`.do`), R (`.R`), or Python (`.py`).

### 3. Econometric Estimation and Diagnostics

  - Difference-in-Differences (DiD):
      - Assess parallel trends using event study specifications with leads and lags.
      - For staggered rollouts with heterogeneous treatment effects, apply modern estimators (Callaway and Sant'Anna, Sun and Abraham, or de Chaisemartin and D'Haultfoeuille) rather than naive two-way fixed effects (TWFE).
  - Instrumental Variables (IV / 2SLS):
      - Check first-stage instrument relevance: report first-stage F-statistics (Montiel Olea and Pflueger effective F-statistic or rule-of-thumb F > 10 / F > 104).
      - Defend exclusion restrictions theoretically and run overidentification tests (Sargan-Hansen) when overidentified.
  - Regression Discontinuity Design (RDD):
      - Verify continuity of running variable density via McCrary sorting tests.
      - Balance test baseline covariates across the cutoff threshold.
      - Estimate local polynomial regressions with optimal data-driven bandwidths (Calonico, Cattaneo, and Titiunik - `rdrobust`).
  - Standard Errors and Clustering:
      - Always cluster standard errors at the level of treatment assignment or policy variation.
      - For small clusters (G < 30), apply wild cluster bootstrap (`boottest` or `fwildclusterboot`).

### 4. Theoretical Modeling in LaTeX

  - Formalize optimization problems (consumer utility, firm profit, social planner).
  - State Lagrangian functions, first-order conditions (FOCs), and second-order conditions (SOCs).
  - Derive comparative statics using the Implicit Function Theorem and Cramer's Rule.
  - Maintain consistent mathematical notation throughout all derivations.

### 5. Publication-Ready Output Generation

  - Regression Tables:
      - Output clean LaTeX tables formatted to American Economic Association (AEA) or typical journal standards.
      - Include coefficient estimates, standard errors in parentheses, number of observations, fixed effects indicators, and diagnostic statistics (R-squared, Kleibergen-Paap F, p-values).
  - Visualizations:
      - Generate clean, minimalist charts: event-study coefficient plots with 95% confidence intervals, RDD bin scatters, and macroeconomic time series.
      - Maintain legible font sizing, explicit unit labels, and clear legends.
  - Beamer Presentations:
      - Structure presentations using the 3-part academic structure: Motivation and Research Question, Empirical Strategy and Identification, Results and Mechanism.

## Methodological Gotchas

  - Two-Way Fixed Effects Under Staggered Timing: Naive OLS regressions with unit and time fixed effects yield negative weights on early-treated units; use robust modern estimators.
  - Bad Controls: Never control for post-treatment variables that are themselves affected by the treatment, as this introduces collider or selection bias.
  - Cluster Count: Clustering at a level with very few groups can severely downward-bias standard errors; verify cluster counts before proceeding.
  - p-Hacking and Multiple Testing: When evaluating multiple outcomes, report False Discovery Rate (FDR) adjusted q-values or Bonferroni adjustments.
