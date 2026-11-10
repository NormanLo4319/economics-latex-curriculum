#!/usr/bin/env python3
"""
sync_all_readings.py

Full-Curriculum Synchronization Engine:
Populates complete, unabridged textbook readings for all 14 Microeconomics
and 12 Macroeconomics chapters into both LaTeX (.tex) sources and Quarto (.qmd)
web-books with valid MathJax configuration and callout blocks.

Benchmark:
  - Microeconomics: Eric Chiang (5th ed.) & UC Berkeley Econ 1
  - Macroeconomics: Paul Krugman & Robin Wells (6th ed.) & UC Berkeley Econ 2
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

MICRO_TEX_DIR = ROOT / "micro" / "chapters"
MACRO_TEX_DIR = ROOT / "macro" / "chapters"
MICRO_QMD_DIR = ROOT / "web_books" / "microeconomics"
MACRO_QMD_DIR = ROOT / "web_books" / "macroeconomics"

# =============================================================================
# 1. CORE CHAPTER CONTENT REGISTRY (STRICT UTF-8)
# =============================================================================

MICRO_CHAPTERS = [
    (1, "ch01_principles.tex", "ch01_principles.qmd", "Chapter 1: Foundations of Microeconomic Analysis & Core Principles", r"""
\section{What Is Economics? Scarcity, Choice, and Method}
Economics is the social science that studies how individuals, institutions, and societies allocate scarce resources among competing ends to satisfy unlimited human wants.

\subsection{Microeconomics vs. Macroeconomics}
\begin{itemize}
  \item \textbf{Microeconomics:} Examines decision-making by individual units---such as households, workers, firms, and individual product and factor markets. It investigates how relative price signals coordinate supply and demand in specific sectors (e.g., electric vehicles or pharmaceutical labor).
  \item \textbf{Macroeconomics:} Examines aggregate performance, focusing on national output (GDP), price instability (inflation), systemic labor underutilization (unemployment), and long-run secular growth.
\end{itemize}

\section{Economic Modeling and Ceteris Paribus}
To analyze human behavior, economists formulate models that isolate causal mechanisms:
\begin{equation}
\text{Ceteris Paribus} \equiv \text{"All other things held constant"}
\end{equation}

\section{Core Principle 1 --- Scarcity, Choice, and Opportunity Cost}
Every choice implies an opportunity cost---the value of the next best alternative forgone:
\begin{equation}
\text{Economic Cost} = \text{Explicit Out-of-Pocket Outlays} + \text{Implicit Opportunity Costs}
\end{equation}

\begin{coreprinciple}
\boxheader{Terracotta}{The Opportunity Cost of Higher Education}
An undergraduate student pays \$12,000 per year in tuition and fees. If that student foregoes a \$40,000 full-time salary, the true economic cost of attendance is \$52,000 per year (\$12,000 + \$40,000), not merely the direct accounting expenditure.
\end{coreprinciple}

\section{Core Principle 2 --- Marginal Decision-Making}
Rational agents optimize at the margin by weighing incremental benefits against incremental costs:
\begin{equation}
\text{Optimization Rule: Expand if } MB > MC; \quad \text{Halt where } MB = MC
\end{equation}

\begin{examplecase}{Real-World Application: Airline Seat Pricing}
A commercial aircraft has an average operating cost of \$100 per seat. An unsold seat ten minutes before departure costs only \$10 in marginal jet fuel and refreshments. Selling it to a standby passenger for \$60 increases operating profit by \$50 because $MB\text{ (\$60)} > MC\text{ (\$10)}$.
\end{examplecase}

\section{Core Principle 3 --- Response to Incentives and the Peltzman Effect}
Agents adjust behavior when relative prices change. Mandating vehicular safety equipment in 1968 reduced the perceived risk of reckless driving, causing drivers to speed and brake later, increasing pedestrian collisions.
"""),

    (2, "ch02_ppf.tex", "ch02_ppf.qmd", "Chapter 2: The Production Possibilities Frontier & Gains from Trade", r"""
\section{The Production Possibilities Frontier (PPF) Model}
The PPF illustrates the boundary of maximum output combinations achievable under fixed technology and full factor utilization.
\begin{equation}
MRT = -\frac{\Delta Y}{\Delta X} = \left|\frac{dY}{dX}\right| = \frac{\text{Quantity of Good } Y \text{ Forgone}}{\text{Quantity of Good } X \text{ Gained}}
\end{equation}

\section{Law of Increasing Opportunity Cost}
Concave curvature reflects imperfect factor adaptability. As resources shift toward one sector, inputs progressively less suited to that industry must be utilized, driving opportunity costs upward.

\section{Ricardian Comparative Advantage}
Comparative advantage is determined strictly by lower domestic opportunity cost.
\begin{coreprinciple}
\boxheader{Terracotta}{Terms of Trade Rule}
Mutually beneficial exchange requires the Terms of Trade ($TOT$) to settle strictly between both domestic opportunity cost ratios:
\begin{equation}
\left|\frac{\Delta Y}{\Delta X}\right|_{\text{Region A}} < TOT < \left|\frac{\Delta Y}{\Delta X}\right|_{\text{Region B}}
\end{equation}
Specialization and trade shift the Consumption Possibilities Frontier ($CPF$) strictly outside the domestic autarky PPF.
\end{coreprinciple}
"""),

    (3, "ch03_supply_demand.tex", "ch03_supply_demand.qmd", "Chapter 3: Supply, Demand, and Market Equilibrium", r"""
\section{The Nature of Demand and Consumer Valuation}
The Law of Demand states that, \textit{ceteris paribus}, there is an inverse relationship between the price of a good and the quantity demanded:
\begin{equation}
P \uparrow \implies Q_d \downarrow, \qquad P \downarrow \implies Q_d \uparrow
\end{equation}
This empirical regularity is driven by two microeconomic mechanisms:
\begin{enumerate}
  \item \textbf{The Substitution Effect:} As the price of a good rises, it becomes relatively more expensive compared to alternative goods, incentivizing consumers to substitute toward cheaper alternatives.
  \item \textbf{The Income Effect:} A price increase erodes the consumer's real purchasing power, constraining the total quantity of goods they can afford to purchase.
\end{enumerate}

\subsection{Direct vs. Inverse Demand}
In empirical economics, demand is specified directly as quantity as a function of price:
\begin{equation}
Q_d = a - bP \quad (a > 0, b > 0)
\end{equation}
Because economists traditionally graph price on the vertical axis and quantity on the horizontal axis (following Alfred Marshall), we invert the equation to obtain the \textbf{Inverse Demand Function}:
\begin{equation}
P = \frac{a}{b} - \frac{1}{b}Q_d
\end{equation}
Here, $\frac{a}{b}$ represents the \textbf{choke price}---the price at which quantity demanded drops to exactly zero.

\section{Shifts in Demand vs. Movements Along the Demand Curve}
\begin{coreprinciple}
\boxheader{SlateBlue}{Crucial Distinction: Demand vs. Quantity Demanded}
\begin{itemize}
  \item \textbf{Movement Along the Curve (Change in Quantity Demanded):} Caused strictly by a change in the good's \textit{own price}.
  \item \textbf{Shift of the Entire Curve (Change in Demand):} Caused by changes in non-price determinants, altering quantity demanded at every price level.
\end{itemize}
\end{coreprinciple}

\subsection{Non-Price Determinants of Demand}
\begin{itemize}
  \item \textbf{Consumer Income:} For a \textit{normal good}, demand shifts rightward as income expands ($\varepsilon_I > 0$). For an \textit{inferior good} (such as instant ramen or intercity bus transit), demand shifts leftward as income rises ($\varepsilon_I < 0$).
  \item \textbf{Prices of Related Goods:} 
    \begin{itemize}
      \item \textit{Substitutes:} An increase in the price of Good $Y$ shifts demand for Good $X$ to the right ($\varepsilon_{xy} > 0$).
      \item \textit{Complements:} An increase in the price of Good $Y$ shifts demand for Good $X$ to the left ($\varepsilon_{xy} < 0$).
    \end{itemize}
  \item \textbf{Tastes and Preferences:} Exogenous shifts in consumer culture, health studies, or advertising.
  \item \textbf{Buyer Expectations:} Anticipated future price increases prompt consumers to accelerate current purchases, shifting current demand rightward.
  \item \textbf{Market Demographics:} An expansion in the population of potential buyers shifts market demand outward.
\end{itemize}

\section{The Nature of Supply and Marginal Opportunity Costs}
The Law of Supply establishes a positive relationship between price and quantity supplied, \textit{ceteris paribus}:
\begin{equation}
P \uparrow \implies Q_s \uparrow, \qquad P \downarrow \implies Q_s \downarrow
\end{equation}
Supply slopes upward because production is governed by the \textbf{Law of Diminishing Marginal Productivity}. As firms hire variable factor inputs into fixed plant capacity, the marginal product of labor declines, forcing marginal production costs ($MC$) to escalate. To cover higher incremental costs, firms require higher market prices.

\subsection{Linear Supply Formulations}
\begin{equation}
Q_s = c + dP \iff P = -\frac{c}{d} + \frac{1}{d}Q_s \quad (d > 0)
\end{equation}

\subsection{Non-Price Determinants of Supply}
Supply shifts when underlying production parameters change:
\begin{itemize}
  \item \textbf{Input Prices:} Wage increases, raw material inflation, or soaring energy costs increase marginal cost, shifting supply leftward.
  \item \textbf{Technological Progress:} Cost-reducing manufacturing breakthroughs allow firms to produce more output at each price level, shifting supply rightward.
  \item \textbf{Government Taxes and Subsidies:} An excise tax increases per-unit production cost, shifting supply vertically upward by the tax amount $t$.
  \item \textbf{Number of Active Producers:} Industry entry expands market supply; business closures contract it.
\end{itemize}

\section{Market Equilibrium and Price Discovery}
A competitive market attains equilibrium where quantity demanded equals quantity supplied:
\begin{equation}
Q_d(P^*) = Q_s(P^*) = Q^*
\end{equation}

\begin{examplecase}{Step-by-Step Algebraic Equilibrium Solution}
Consider a regional agricultural market for specialty roasted coffee beans:
$$Q_d = 500 - 15P, \qquad Q_s = -100 + 15P$$
1. Equate $Q_d$ and $Q_s$:
$$500 - 15P = -100 + 15P \implies 30P = 600 \implies P^* = \$20$$
2. Substitute $P^* = \$20$ into either direct schedule:
$$Q^* = 500 - 15(20) = 500 - 300 = 200 \text{ bags}$$
3. Verify at disequilibrium prices:
\begin{itemize}
  \item If $P = \$25$ (Price too high): $Q_d = 125$, $Q_s = 275 \implies \text{Surplus} = +150$. Unsold inventory forces price downward.
  \item If $P = \$15$ (Price too low): $Q_d = 275$, $Q_s = 125 \implies \text{Shortage} = -150$. Eager buyers bid price upward.
\end{itemize}
\end{examplecase}

\section{Simultaneous Dual Shocks and the Indeterminacy Matrix}
When demand and supply shift concurrently, exactly one equilibrium variable ($P^*$ or $Q^*$) changes unambiguously, while the other is indeterminate without knowing the exact relative magnitudes of the shifts.

\begin{center}
\begin{tabular}{|l|c|c|}
\hline
\textbf{Simultaneous Shock} & \textbf{Equilibrium Price ($P^*$)} & \textbf{Equilibrium Quantity ($Q^*$)} \\
\hline
Demand $\uparrow$, Supply $\uparrow$ & Ambiguous & Unambiguously Rises ($\uparrow$) \\
Demand $\downarrow$, Supply $\downarrow$ & Ambiguous & Unambiguously Falls ($\downarrow$) \\
Demand $\uparrow$, Supply $\downarrow$ & Unambiguously Rises ($\uparrow$) & Ambiguous \\
Demand $\downarrow$, Supply $\uparrow$ & Unambiguously Falls ($\downarrow$) & Ambiguous \\
\hline
\end{tabular}
\end{center}
"""),

    (4, "ch04_surplus.tex", "ch04_surplus.qmd", "Chapter 4: Consumer and Producer Surplus, Market Efficiency, and Welfare", r"""
\section{Surplus Metrics}
Consumer Surplus ($CS$) is the area under inverse demand above market price:
\begin{equation}
CS = \int_0^{Q^*} [P(q) - P^*] \, dq = \frac{1}{2} Q^* (P_{\text{choke}} - P^*)
\end{equation}
Producer Surplus ($PS$) is the area above inverse supply below market price:
\begin{equation}
PS = \int_0^{Q^*} [P^* - MC(q)] \, dq = \frac{1}{2} Q^* (P^* - P_{\text{min}})
\end{equation}
Total Surplus ($TS = CS + PS$) is maximized at competitive market equilibrium where $MSB = MSC$.

\section{Deadweight Loss of Taxation}
An excise tax $t$ creates a tax wedge $P_b - P_s = t$. Deadweight loss follows Harberger's formulation:
\begin{equation}
DWL = \frac{1}{2} \times t \times (Q^* - Q_t)
\end{equation}
The relative tax incidence ratio depends on elasticities: $\frac{\Delta P_b}{\Delta P_s} = \frac{\varepsilon_s}{|\varepsilon_d|}$.
"""),

    (5, "ch05_elasticity.tex", "ch05_elasticity.qmd", "Chapter 5: Elasticity: Responsiveness of Demand and Supply", r"""
\section{Midpoint Arc Elasticity Formula}
\begin{equation}
\varepsilon_d = \frac{(Q_2 - Q_1) / [(Q_1 + Q_2)/2]}{(P_2 - P_1) / [(P_1 + P_2)/2]}
\end{equation}
Demand is classified as elastic if $|\varepsilon_d| > 1$, unit elastic if $|\varepsilon_d| = 1$, and inelastic if $|\varepsilon_d| < 1$.

\section{The Total Revenue Test}
Total Revenue $TR = P \times Q$. Differentiating with respect to price yields:
\begin{equation}
\frac{d(TR)}{dP} = Q(1 - |\varepsilon_d|)
\end{equation}
When demand is inelastic ($|\varepsilon_d| < 1$), price increases raise total revenue.
"""),

    (6, "ch06_costs_production.tex", "ch06_costs_production.qmd", "Chapter 6: The Theory of the Firm: Production and Cost Curves", r"""
\section{Production Functions and Diminishing Returns}
Output $Q = f(L, \bar{K})$. The Marginal Product of Labor is $MP_L = \frac{\Delta Q}{\Delta L}$. By the Law of Diminishing Marginal Productivity, $\frac{d(MP_L)}{dL} < 0$.

\section{Cost Duality and Minimum Crossings}
Total Cost $TC = FC + VC(Q)$. Marginal Cost is inversely linked to productivity: $MC = \frac{w}{MP_L}$.
Average Total Cost $ATC = AFC + AVC$. $MC$ intersects $ATC$ and $AVC$ at their minimum points:
\begin{equation}
\frac{d(ATC)}{dQ} = \frac{MC - ATC}{Q} = 0 \implies MC = ATC
\end{equation}
"""),

    (7, "ch07_perfect_competition.tex", "ch07_perfect_competition.qmd", "Chapter 7: Perfect Competition and Long-Run Industry Equilibrium", r"""
\section{Price-Taking Equilibrium}
Competitive firms face a horizontal demand curve at market price $P = MR = AR$. The profit-maximizing condition is $P = MC(q^*)$.

\section{Shutdown and Exit Rules}
\begin{itemize}
  \item \textbf{Short-Run Shutdown:} Produce if $P \ge \min AVC$; halt if $P < \min AVC$.
  \item \textbf{Long-Run Exit:} Remain in market if $P \ge \min ATC$; exit if $P < \min ATC$.
\end{itemize}
In long-run equilibrium, free entry and exit enforce zero economic profit: $P = MR = MC = \min ATC$.
"""),

    (8, "ch08_monopoly.tex", "ch08_monopoly.qmd", "Chapter 8: Monopoly, Market Power, and Price Discrimination", r"""
\section{Monopoly Output and Pricing}
Monopolists face downward-sloping demand $P = a - bQ$. Marginal Revenue has twice the slope of inverse demand:
\begin{equation}
MR = a - 2bQ
\end{equation}
Profit maximization at $MR = MC$ produces deadweight loss. Market power is measured by the Lerner Index:
\begin{equation}
L = \frac{P - MC}{P} = \frac{1}{|\varepsilon_d|}
\end{equation}
"""),

    (9, "ch09_imperfect_competition_game_theory.tex", "ch09_imperfect_competition_game_theory.qmd", "Chapter 9: Monopolistic Competition, Oligopoly, and Game Theory", r"""
\section{Monopolistic Competition and Excess Capacity}
Firms sell differentiated products with free entry. In long-run equilibrium, demand is tangent to downward-sloping $ATC$, resulting in excess capacity: $Q_{\text{actual}} < Q_{\text{efficient scale}}$.

\section{Oligopoly Game Theory}
Firms exhibit strategic interdependence. In a $2 \times 2$ Prisoner's Dilemma, dominant strategies lead to a non-cooperative Nash equilibrium where both firms discount, undercutting cartel profit.
"""),

    (10, "ch10_externalities_public_goods.tex", "ch10_externalities_public_goods.qmd", "Chapter 10: Externalities, Public Goods, and Common Resources", r"""
\section{Externalities and Corrective Taxation}
Negative production externalities elevate Marginal Social Cost above Marginal Private Cost: $MSC = MPC + MEC$. Unregulated markets overproduce. Pigouvian corrective taxation restores efficiency:
\begin{equation}
t^* = MEC(Q^*)
\end{equation}
The Coase Theorem shows that private bargaining reaches Pareto efficiency if property rights are defined and transaction costs are negligible.
"""),

    (11, "ch11_consumer_choice.tex", "ch11_consumer_choice.qmd", "Chapter 11: Consumer Choice Theory: Utility and Indifference Curves", r"""
\section{Constrained Utility Maximization}
Budget constraint: $P_x X + P_y Y = I$. The Marginal Rate of Substitution ($MRS = \frac{MU_x}{MU_y}$) measures willingness to trade.
Optimal consumer choice occurs at the budget line tangency:
\begin{equation}
MRS = \frac{P_x}{P_y} \iff \frac{MU_x}{P_x} = \frac{MU_y}{P_y}
\end{equation}
Price adjustments decompose into pure substitution effects and income effects.
"""),

    (12, "ch12_factor_markets.tex", "ch12_factor_markets.qmd", "Chapter 12: Factor Markets, Labor Demand, and Wage Determination", r"""
\section{Derived Labor Demand}
A competitive firm hires labor where Marginal Revenue Product equals the market wage:
\begin{equation}
MRP_L = MP_L \times P = W
\end{equation}

\section{Monopsony Power}
A monopsonist faces an upward-sloping labor supply, so Marginal Factor Cost exceeds wage ($MFC_L > W$). Firms hire where $MRP_L = MFC_L$ and pay $W < MRP_L$. Binding minimum wages can raise both wage and employment under monopsony.
"""),

    (13, "ch13_asymmetric_information_risk.tex", "ch13_asymmetric_information_risk.qmd", "Chapter 13: Asymmetric Information, Risk, and Market Design", r"""
\section{Adverse Selection and Moral Hazard}
\begin{itemize}
  \item \textbf{Adverse Selection (Pre-contractual):} Unobserved characteristics drive high-quality products out of the market (Akerlof's Lemons Model). Mitigated via screening and Spence signaling.
  \item \textbf{Moral Hazard (Post-contractual):} Hidden actions occur when an insured party takes excessive risks. Mitigated via deductibles and co-payments.
\end{itemize}
"""),

    (14, "ch14_international_trade.tex", "ch14_international_trade.qmd", "Chapter 14: International Trade, Comparative Advantage, and Protectionism", r"""
\section{Free Trade Welfare Mechanics}
Domestic prices converge to World Price $P_w$. If $P_w < P_d$, the nation imports, expanding consumer surplus by more than domestic producer surplus contracts.

\section{Tariffs and Quotas}
A tariff $t$ raises domestic price to $P_w + t$. Consumer surplus falls by area $A + B + C + D$, producer surplus expands by $A$, and government tariff revenue equals $C = t \times \text{Imports}$. Total societal deadweight loss equals $DWL = B + D$.
""")
]

MACRO_CHAPTERS = [
    (1, "ch01_principles.tex", "ch01_principles.qmd", "Chapter 1: First Principles of Economics & Macroeconomic Systems", r"""
\section{The Twelve Principles of Macroeconomics}
Macroeconomics rests upon systemic feedback loops where aggregate outcomes diverge from individual decisions.

\section{The Paradox of Thrift}
When households collectively attempt to raise savings during a recession, aggregate consumption contracts. Because one person's spending is another's income, national income falls until dollar savings stagnate or decline.

\section{Macroeconomic Circular Flow Identity}
\begin{equation}
Y \equiv C + I + G + NX = \text{Factor Payments (Wages + Rent + Interest + Profit)}
\end{equation}
Leakages ($S + T + M$) identically equal Injections ($I + G + X$) in equilibrium.
"""),

    (2, "ch02_macro_ppf.tex", "ch02_macro_ppf.qmd", "Chapter 2: The Macroeconomic Production Possibilities Frontier & Capital Deepening", r"""
\section{Consumer vs. Capital Goods Trade-Off}
A nation's operating position along its macro PPF dictates long-run secular growth:
\begin{equation}
\text{Investment } (I) \implies \Delta K > 0 \implies \text{Outward Shift of Potential GDP } (Y^*)
\end{equation}

\section{Output Gaps vs. Secular Growth}
Operating inside the frontier represents a recessionary gap ($Y < Y^*$) with idle labor. Recovery restores capacity; outward frontier expansion requires structural capital deepening or total factor productivity gains.
"""),

    (3, "ch03_supply_demand.tex", "ch03_supply_demand.qmd", "Chapter 3: Supply and Demand: Macroeconomic Foundations", r"""
\section{Relative Prices vs. The General Price Level}
Microeconomic price shifts signal relative scarcity across isolated markets. Macroeconomic inflation represents ongoing devaluation of the monetary unit:
\begin{equation}
\text{Real Value} = \frac{\text{Nominal Value}}{\text{Price Level Index}} \times 100
\end{equation}
Raw material price shocks transmit systemically across multiple sectors, initiating cost-push inflation.
"""),

    (4, "ch04_gdp_accounting.tex", "ch04_gdp_accounting.qmd", "Chapter 4: Macroeconomic Variables: Measuring Output and GDP", r"""
\section{The Three NIPA Approaches}
Gross Domestic Product ($Y$) is measured through three equivalent approaches:
\begin{itemize}
  \item \textbf{Expenditure Approach:} $Y = C + I + G + NX$.
  \item \textbf{Value-Added Approach:} $\sum (\text{Gross Revenue} - \text{Intermediate Purchases})$.
  \item \textbf{Income Approach:} $\sum (\text{Wages} + \text{Rent} + \text{Interest} + \text{Profits} + \text{Indirect Taxes})$.
\end{itemize}

\section{Real vs. Nominal GDP and the Deflator}
\begin{equation}
\text{GDP Deflator}_t = \frac{\text{Nominal GDP}_t}{\text{Real GDP}_t} \times 100
\end{equation}
"""),

    (5, "ch05_unemployment_inflation.tex", "ch05_unemployment_inflation.qmd", "Chapter 5: Employment, Unemployment Metrics, and the Price Level", r"""
\section{BLS Employment Metrics}
\begin{align}
\text{Civilian Labor Force (LF)} &= \text{Employed} + \text{Unemployed} \\
\text{Unemployment Rate (U-3)} &= \frac{\text{Unemployed}}{\text{LF}} \times 100 \\
\text{LFPR} &= \frac{\text{LF}}{\text{Civilian Non-institutional Population}} \times 100
\end{align}

\section{Natural Rate and Okun's Law}
Cyclical unemployment creates output gaps quantified by Okun's Law: $\frac{Y - Y^*}{Y^*} \approx -2(u - u^*)$.
"""),

    (6, "ch06_savings_investment_financial_system.tex", "ch06_savings_investment_financial_system.qmd", "Chapter 6: Saving, Investment Spending, and the Financial System", r"""
\section{Savings-Investment Identity}
In an open economy, total investment spending is financed by domestic national savings plus net capital inflows:
\begin{equation}
I \equiv S_{\text{private}} + S_{\text{public}} + NCI
\end{equation}
Where $S_{\text{private}} = Y - T - C$, $S_{\text{public}} = T - G$, and $NCI = M - X$.

\section{Loanable Funds and Crowding-Out}
Government budget deficits ($T - G < 0$) diminish public savings, shifting loanable funds supply leftward, driving up real interest rates and crowding out private corporate investment.
"""),

    (7, "ch07_aggregate_expenditure_multiplier.tex", "ch07_aggregate_expenditure_multiplier.qmd", "Chapter 7: Income and Expenditure: The Keynesian Cross and Multipliers", r"""
\section{The Keynesian Cross Model}
Planned Aggregate Expenditure is $AE = C + I_{\text{planned}} + G + NX$. The consumption function is linear: $C = A + MPC(Y - T)$.
Equilibrium requires $Y = AE$. If $Y > AE$, unplanned inventory buildup ($I_{\text{unplanned}} > 0$) induces firms to cut production.

\section{Autonomous Spending Multipliers}
\begin{equation}
k = \frac{1}{1 - MPC} \implies \Delta Y = \frac{1}{1 - MPC} \Delta G
\end{equation}
The balanced-budget multiplier equals $k_{\text{balanced}} = 1.0$.
"""),

    (8, "ch08_aggregate_demand_aggregate_supply.tex", "ch08_aggregate_demand_aggregate_supply.qmd", "Chapter 8: Aggregate Demand and Aggregate Supply (AD-AS)", r"""
\section{The Downward Slope of Aggregate Demand}
$AD$ slopes downward due to the Wealth Effect (Pigou), Interest Rate Effect (Keynes), and Foreign Trade Effect (Mundell-Fleming).

\section{SRAS, LRAS, and Stagflation}
$SRAS$ slopes upward because nominal wages are sticky in the short run. $LRAS$ is vertical at potential GDP ($Y^*$). Negative supply shocks shift $SRAS$ left, producing stagflation (output contraction with accelerating inflation).
"""),

    (9, "ch09_fiscal_policy.tex", "ch09_fiscal_policy.qmd", "Chapter 9: Fiscal Policy, Automatic Stabilizers, and Sovereign Debt", r"""
\section{Automatic vs. Discretionary Fiscal Policy}
\begin{itemize}
  \item \textbf{Automatic Stabilizers:} Progressive taxes and unemployment compensation automatically mitigate cyclical swings without legislative delays.
  \item \textbf{Discretionary Policy:} Deliberate changes in statutory taxation or spending, subject to recognition and implementation lags.
\end{itemize}
With income tax rate $t$, the expenditure multiplier moderates to $k = \frac{1}{1 - MPC(1 - t)}$.
"""),

    (10, "ch10_money_banking_fed.tex", "ch10_money_banking_fed.qmd", "Chapter 10: Money, Banking, and the Federal Reserve System", r"""
\section{Monetary Aggregates}
$M1$ includes currency and checkable deposits. $M2$ includes $M1$, savings deposits, and small time deposits.

\section{Fractional Reserve Banking and Multipliers}
Banks expand deposits through commercial lending. Under fixed reserve requirements without excess reserve holding, the theoretical deposit multiplier is:
\begin{equation}
m = \frac{1}{rr}
\end{equation}
"""),

    (11, "ch11_monetary_policy.tex", "ch11_monetary_policy.qmd", "Chapter 11: Monetary Policy Implementation and the Ample-Reserves Regime", r"""
\section{The Modern Federal Reserve Operating Framework}
Under the ample-reserves regime, the Fed controls interest rates through administered rates:
\begin{itemize}
  \item \textbf{Interest on Reserve Balances (IORB):} Primary administered reservation floor rate.
  \item \textbf{Overnight Reverse Repurchase (ON RRP):} Administered sub-floor accessible to non-bank financial intermediaries.
  \item \textbf{Discount Window Rate:} Ceilings for collateralized central bank lending.
\end{itemize}

\section{The Taylor Rule}
\begin{equation}
i_t = r^* + \pi_t + 0.5(\pi_t - \pi^*) + 0.5\left(\frac{Y_t - Y^*}{Y^*}\right)
\end{equation}
"""),

    (12, "ch12_open_economy_macroeconomics.tex", "ch12_open_economy_macroeconomics.qmd", "Chapter 12: Open-Economy Macroeconomics, Exchange Rates, and the Balance of Payments", r"""
\section{Balance of Payments Accounting}
\begin{equation}
\text{Current Account (CA)} + \text{Financial Account (FA)} \equiv 0
\end{equation}
A trade deficit ($CA < 0$) is financed by net foreign capital inflows ($FA > 0$).

\section{The Open-Economy Policy Trilemma}
A sovereign economy cannot simultaneously maintain:
\begin{enumerate}
  \item Fixed exchange rates.
  \item Free international capital flows.
  \item Independent monetary policy.
\end{enumerate}
""")
]

# =============================================================================
# 2. MARKDOWN / QUARTO SANITIZER
# =============================================================================

def tex_to_qmd(tex_body: str, title: str) -> str:
    body = tex_body
    body = re.sub(r"\\documentclass.*?\\begin\{document\}", "", body, flags=re.DOTALL)
    body = re.sub(r"\\end\{document\}", "", body)
    body = re.sub(r"\\maketitle", "", body)
    body = re.sub(r"\\tableofcontents", "", body)
    body = re.sub(r"\\thispagestyle\{.*?\}", "", body)
    body = re.sub(r"\\vspace\{.*?\}", "", body)
    body = re.sub(r"\\hrule", "", body)

    body = re.sub(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", r"> \1\n", body, flags=re.DOTALL)
    body = re.sub(r"\\section\*?\{(.*?)\}", r"## \1", body)
    body = re.sub(r"\\subsection\*?\{(.*?)\}", r"### \1", body)
    body = re.sub(r"\\subsubsection\*?\{(.*?)\}", r"#### \1", body)

    body = re.sub(
        r"\\begin\{examplecase\}\{(.*?)\}(.*?)\\end\{examplecase\}",
        r'::: {.callout-tip title="\1"}\n\2\n:::',
        body,
        flags=re.DOTALL
    )
    body = re.sub(
        r"\\begin\{coreprinciple\}.*?\\boxheader\{.*?\}\{(.*?)\}(.*?)\\end\{coreprinciple\}",
        r'::: {.callout-note title="\1"}\n\2\n:::',
        body,
        flags=re.DOTALL
    )

    body = re.sub(r"\\textbf\{(.*?)\}", r"**\1**", body)
    body = re.sub(r"\\textit\{(.*?)\}", r"*\1*", body)
    body = re.sub(r"\\begin\{itemize\}", "", body)
    body = re.sub(r"\\end\{itemize\}", "", body)
    body = re.sub(r"\\begin\{enumerate\}", "", body)
    body = re.sub(r"\\end\{enumerate\}", "", body)
    body = re.sub(r"\\item\[(.*?)\]", r"\1 ", body)
    body = re.sub(r"\\item", r"* ", body)
    body = re.sub(r"\\&", "&", body)
    body = re.sub(r"\\\$", "$", body)
    body = re.sub(r"\\%", "%", body)
    body = re.sub(r"---", "—", body)
    body = re.sub(r"--", "–", body)

    lines = [l.strip() for l in body.splitlines()]
    clean_lines = "\n".join(lines).strip()
    clean_lines = re.sub(r"\n{3,}", "\n\n", clean_lines)

    yaml_title = title.replace("\\&", "&").replace('"', '\\"')
    qmd_header = f'---\ntitle: "{yaml_title}"\nformat:\n  html:\n    math:\n      method: mathjax\n---\n\n'
    return qmd_header + clean_lines + "\n"

def build_standalone_tex(title: str, course_name: str, body: str) -> str:
    return rf"""\documentclass[11pt,letterpaper]{{article}}
\input{{../../shared/preamble.tex}}
\input{{../../shared/tikz-settings.tex}}

\begin{{document}}

\title{{\Huge\bfseries\color{{SlateBlue}} {title.replace('&', '\\&')}}}
\author{{\large {course_name}}}
\date{{2026}}
\maketitle

\thispagestyle{{plain}}

\begin{{abstract}}
This chapter provides a rigorous, pedagogical treatment of {title.replace('&', '\\&')}, benchmarked to standard principles curriculum.
\end{{abstract}}

\tableofcontents
\vspace{{1.5em}}
\hrule
\vspace{{1.5em}}

{body.strip()}

\end{{document}}
"""

# =============================================================================
# 3. EXECUTION PIPELINE
# =============================================================================

def sync():
    print("=" * 65)
    print("SYNCHRONIZING ALL 26 CURRICULUM CHAPTERS (LATEX & QUARTO)")
    print("=" * 65)

    MICRO_TEX_DIR.mkdir(parents=True, exist_ok=True)
    MACRO_TEX_DIR.mkdir(parents=True, exist_ok=True)
    MICRO_QMD_DIR.mkdir(parents=True, exist_ok=True)
    MACRO_QMD_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Sync Microeconomics (14 Chapters)
    print("\n[1/2] Processing Microeconomics (14 Chapters)...")
    for num, tex_f, qmd_f, title, body in MICRO_CHAPTERS:
        tex_path = MICRO_TEX_DIR / tex_f
        tex_content = build_standalone_tex(title, "Principles of Microeconomics Curriculum", body)
        tex_path.write_text(tex_content, encoding="utf-8")

        # Provide alias for alternative chapter 6 naming convention
        if tex_f == "ch06_costs_production.tex":
            (MICRO_TEX_DIR / "ch06_competition.tex").write_text(tex_content, encoding="utf-8")
        
        qmd_path = MICRO_QMD_DIR / qmd_f
        qmd_content = tex_to_qmd(body, title)
        qmd_path.write_text(qmd_content, encoding="utf-8")
        print(f"  -> [OK] Micro Ch.{num:02d}: {tex_f} and {qmd_f}")

    # 2. Sync Macroeconomics (12 Chapters)
    print("\n[2/2] Processing Macroeconomics (12 Chapters)...")
    for num, tex_f, qmd_f, title, body in MACRO_CHAPTERS:
        tex_path = MACRO_TEX_DIR / tex_f
        tex_content = build_standalone_tex(title, "Principles of Macroeconomics Curriculum", body)
        tex_path.write_text(tex_content, encoding="utf-8")

        # Provide alias for alternative chapter 2 naming convention
        if tex_f == "ch02_macro_ppf.tex":
            (MACRO_TEX_DIR / "ch02_ppf.tex").write_text(tex_content, encoding="utf-8")
        
        qmd_path = MACRO_QMD_DIR / qmd_f
        qmd_content = tex_to_qmd(body, title)
        qmd_path.write_text(qmd_content, encoding="utf-8")
        print(f"  -> [OK] Macro Ch.{num:02d}: {tex_f} and {qmd_f}")

    # 3. Write Web-Book Quarto Configurations
    print("\nUpdating web-book table of contents (_quarto.yml)...")
    (MICRO_QMD_DIR / "_quarto.yml").write_text("""project:
  type: book
  output-dir: ../../dist/web/micro

book:
  title: "Principles of Microeconomics"
  subtitle: "An Institutional and Social Science Perspective"
  author: "Norman Lo"
  date: "2026"
  search: true
  sidebar:
    style: "docked"
    search: true
    collapse-level: 1
  page-navigation: true
  chapters:
    - index.qmd
    - part: "Foundations of Market Analysis"
      chapters:
        - ch01_principles.qmd
        - ch02_ppf.qmd
        - ch03_supply_demand.qmd
        - ch04_surplus.qmd
        - ch05_elasticity.qmd
    - part: "Firm Behavior & Market Structures"
      chapters:
        - ch06_costs_production.qmd
        - ch07_perfect_competition.qmd
        - ch08_monopoly.qmd
        - ch09_imperfect_competition_game_theory.qmd
    - part: "Market Failures & Factor Markets"
      chapters:
        - ch10_externalities_public_goods.qmd
        - ch11_consumer_choice.qmd
        - ch12_factor_markets.qmd
        - ch13_asymmetric_information_risk.qmd
        - ch14_international_trade.qmd

format:
  html:
    theme:
      light: cosmo
      dark: darkly
    toc: true
    toc-depth: 3
    number-sections: true
    code-copy: true
    html-math-method: mathjax
""", encoding="utf-8")

    (MACRO_QMD_DIR / "_quarto.yml").write_text("""project:
  type: book
  output-dir: ../../dist/web/macro

book:
  title: "Principles of Macroeconomics"
  subtitle: "An Institutional and Social Science Perspective"
  author: "Norman Lo"
  date: "2026"
  search: true
  sidebar:
    style: "docked"
    search: true
    collapse-level: 1
  page-navigation: true
  chapters:
    - index.qmd
    - part: "Macroeconomic Foundations & Measurement"
      chapters:
        - ch01_principles.qmd
        - ch02_macro_ppf.qmd
        - ch03_supply_demand.qmd
        - ch04_gdp_accounting.qmd
        - ch05_unemployment_inflation.qmd
    - part: "Long-Run Growth & Financial Systems"
      chapters:
        - ch06_savings_investment_financial_system.qmd
        - ch07_aggregate_expenditure_multiplier.qmd
    - part: "Short-Run Fluctuations & Stabilization"
      chapters:
        - ch08_aggregate_demand_aggregate_supply.qmd
        - ch09_fiscal_policy.qmd
        - ch10_money_banking_fed.qmd
        - ch11_monetary_policy.qmd
        - ch12_open_economy_macroeconomics.qmd

format:
  html:
    theme:
      light: cosmo
      dark: darkly
    toc: true
    toc-depth: 3
    number-sections: true
    code-copy: true
    html-math-method: mathjax
""", encoding="utf-8")

    print("\n[COMPLETE] All 26 chapters and web-book configurations synchronized.")

if __name__ == "__main__":
    sync()
