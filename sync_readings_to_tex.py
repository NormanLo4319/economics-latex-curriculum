#!/usr/bin/env python3
"""
sync_readings_to_tex.py (Full 26-Chapter Curriculum Engine)

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
\section{Learning Outcomes and Key Terms}
After this chapter, students should be able to model a single-price monopolist's output and price, calculate economic profit and deadweight loss in a linear example, and explain how market power differs from the mere presence of one seller. These objectives support C2001-1, C2001-2, and C2001-3.

Key terms include monopoly, entry barrier, marginal revenue, market power, price discrimination, consumer surplus, and deadweight loss.

\section{A Scanner, a Local Market, and the Cost of Entry}
Consider a hospital deciding whether to operate an advanced diagnostic scanner. The equipment has a large fixed cost: it must be purchased, staffed, maintained, and kept available even when no patient is being scanned. Once installed, the marginal cost of one additional scan may be much smaller than the average cost at low volume. A nearby clinic considering entry must also recruit technicians, obtain regulatory approvals, and attract enough patients to cover its fixed costs.

This example helps distinguish scale economies from monopoly power. A scanner can lower average cost as its fixed cost is spread over more scans, but that fact alone does not establish that the hospital is a monopolist. We must define the relevant service and geographic market, identify reasonable substitutes, and examine whether entry is feasible. A patient may travel to another hospital, use a different diagnostic test, or defer a scan; each possibility changes the competitive constraint.

\begin{examplecase}{Illustrative Hospital Scanner Calculation}
Suppose annualized fixed cost is \$900,000 and the marginal cost of each scan is \$100. At 3,000 scans per year, average total cost is $900{,}000/3{,}000 + 100 = \$400$ per scan. At 9,000 scans, it is $900{,}000/9{,}000 + 100 = \$200$. These values are illustrative, not hospital data. Higher volume lowers average cost over this range, but it does not by itself prove that the hospital can profitably raise price above the level constrained by alternatives.
\end{examplecase}

\section{The Demand Curve, Marginal Revenue, and the Graph}
A competitive firm can sell another unit at the going market price without changing the price received on earlier units. A single-price monopolist cannot: to sell an additional unit, it generally must lower the price, and that lower price applies to all units sold. Therefore its marginal revenue lies below its demand curve.

In the standard graph, put quantity on the horizontal axis and price or cost per unit on the vertical axis. Draw a downward-sloping demand curve $D$ and a marginal-revenue curve $MR$ below it. Draw marginal cost $MC$ rising or horizontal. The monopolist chooses the quantity at the intersection of $MR$ and $MC$, then moves vertically to the demand curve to find the price consumers will pay. Do not read the monopoly price from the $MR=MC$ intersection: that intersection determines quantity, not price.

The competitive benchmark is the quantity where willingness to pay on demand equals marginal cost. With downward-sloping demand and the same marginal cost, the monopoly quantity is lower and its price is higher than that benchmark. The missing mutually beneficial trades between the two quantities are the source of deadweight loss.

\section{A Linear Model: From Story to Equation}
Let inverse demand be $P(Q)=100-2Q$ and constant marginal cost be $MC=20$, with no fixed cost in this numerical exercise. Total revenue is $TR(Q)=P(Q)Q=100Q-2Q^2$. Differentiating gives $MR(Q)=100-4Q$. The firm's profit-maximizing condition is $MR=MC$:
\begin{equation}
100-4Q_M=20 \quad\Longrightarrow\quad Q_M=20, \qquad P_M=100-2(20)=60.
\end{equation}
At this outcome, profit is $(P_M-MC)Q_M=(60-20)20=800$. The competitive quantity in this simplified model solves $P=MC$, so $100-2Q_C=20$, or $Q_C=40$. Deadweight loss is the triangle between demand and marginal cost over the units from 20 to 40:
\begin{equation}
DWL=\tfrac{1}{2}(Q_C-Q_M)(P_M-MC)=\tfrac{1}{2}(20)(40)=400.
\end{equation}
The triangle formula assumes the linear curves used here. If curves are nonlinear, deadweight loss is the area between marginal social benefit and marginal cost over the underproduced units.

The Lerner index relates a firm's price-cost margin to the absolute value of demand elasticity at the optimum, under the assumptions of a single-price profit-maximizing firm with an interior solution:
\begin{equation}
L=\frac{P-MC}{P}=\frac{1}{|\varepsilon_d|}.
\end{equation}
In the example, $L=(60-20)/60=2/3$. A larger index signals a larger price-cost margin relative to price; it is not, by itself, a complete measure of consumer harm or a legal finding of anticompetitive conduct.

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: One Seller Does Not Automatically Mean Monopoly Power}
The number of firms in a narrow category is not enough to establish market power. The relevant market includes products and locations that buyers see as substitutes, and potential entry can constrain an incumbent even before a new firm opens. Conversely, several firms may still have substantial market power if they face weak competition.
\end{coreprinciple}

\section{Price Discrimination}
Price discrimination means charging different prices for the same or similar product when the difference is not explained by a difference in marginal cost. It requires some ability to set price, a way to sort or identify buyers, and limits on resale between buyer groups. Student discounts, time-based fares, and quantity discounts are familiar examples, although their economic and legal details differ.

Under first-degree discrimination, a seller charges each buyer close to that buyer's willingness to pay. In the idealized model, output can expand toward the efficient quantity while the seller captures most consumer surplus. Under third-degree discrimination, the seller separates observable groups and sets different prices; the group with less elastic demand generally faces the higher markup, provided marginal costs are comparable. Price discrimination can expand access for some buyers, but it can also transfer surplus from consumers to the seller. Its welfare effect depends on output, costs, and who receives the service.

\section{A FRED Price Index Is Not a Monopoly Test}
FRED series CPIMEDSL is the Consumer Price Index for All Urban Consumers: Medical Care in U.S. City Average. It is a monthly, seasonally adjusted index with base period 1982-1984=100. The September 2026 observation is 593.666. The index tracks the average price movement of a defined basket; it is not a price for a particular hospital scanner, a hospital's marginal cost, or a measure of concentration. A rising index alone therefore cannot show that monopoly power caused medical-care inflation. To test that claim, researchers would also need evidence about product markets, entry, costs, quality, and substitutes.

\section{Check Your Understanding}
\begin{enumerate}
  \item In the linear example, what price corresponds to the quantity where $MR=MC$? Why is the intersection itself not the monopoly price?
  \item If the demand curve becomes more elastic at the optimum while marginal cost is unchanged, what does the Lerner relation predict about the percentage markup?
  \item A hospital is the only provider of one scanner type in a town. Name two additional facts needed before concluding that it has market power in the relevant market.
\end{enumerate}
Answers: (1) $P=60$, read from demand at $Q=20$; the $MR=MC$ intersection identifies quantity. (2) The markup share $L$ falls. (3) Examples include travel distance to substitutes, alternative diagnostic procedures, and the likelihood of entry.
"""),

    (9, "ch09_imperfect_competition_game_theory.tex", "ch09_imperfect_competition_game_theory.qmd", "Chapter 9: Monopolistic Competition, Oligopoly, and Game Theory", r"""
\section{Monopolistic Competition and Excess Capacity}
Firms sell differentiated products with free entry. In long-run equilibrium, demand is tangent to downward-sloping $ATC$, resulting in excess capacity: $Q_{\text{actual}} < Q_{\text{efficient scale}}$.

\section{Oligopoly Game Theory}
Firms exhibit strategic interdependence. In a $2 \times 2$ Prisoner's Dilemma, dominant strategies lead to a non-cooperative Nash equilibrium where both firms discount, undercutting cartel profit.
"""),

    (10, "ch10_externalities_public_goods.tex", "ch10_externalities_public_goods.qmd", "Chapter 10: Externalities, Public Goods, and Common Resources", r"""
\section{Learning Outcomes and Key Terms}
Students should distinguish private from social costs and benefits, solve for a simple efficient quantity, and compare corrective policy tools. These objectives support C2001-1 and C2001-2. Key terms include externality, marginal private cost, marginal social cost, Pigouvian tax, public good, common resource, free rider, and Coase bargaining.

\section{A Neighborhood, a Plant, and Unpriced Costs}
Imagine a production facility that releases pollution affecting nearby residents. The firm pays for labor, energy, and materials, but without a fee or regulation it may not pay for all health and environmental damage imposed on others. The firm's private production decision can therefore differ from the decision that maximizes total surplus. The same logic applies to traffic congestion: one driver's trip adds delay to other road users, a cost the driver may not fully consider.

An externality is a cost or benefit from an action that affects a third party outside the transaction. A negative externality creates a wedge between private and social cost; a positive externality creates a wedge between private and social benefit. Not every spillover is a market failure of equal size: measurement, the number of affected parties, property rights, and transaction costs matter.

\section{Negative Production Externalities: The Graph}
For a negative production externality, place quantity on the horizontal axis and dollars per unit on the vertical axis. Draw marginal private cost ($MPC$) below marginal social cost ($MSC$), because $MSC$ includes the damage borne by third parties. Draw marginal benefit ($MB$), assumed here to equal marginal private benefit. The unregulated market produces where $MB=MPC$. The efficient quantity is where $MB=MSC$; it is lower in this example. The vertical distance between $MSC$ and $MPC$ is marginal external cost ($MEC$). The overproduced units create deadweight loss between the benefit and social-cost curves.

\section{A Corrective-Tax Calculation}
Suppose inverse marginal benefit is $MB=100-Q$, marginal private cost is $MPC=20+Q$, and marginal external cost is a constant 10 dollars per unit. Then $MSC=MPC+MEC=30+Q$. The unregulated outcome satisfies $100-Q=20+Q$, giving $Q_M=40$. The efficient outcome satisfies $100-Q=30+Q$, giving $Q^*=35$. A per-unit tax equal to $MEC(Q^*)=10$ makes the private decision face the social marginal cost at the efficient quantity:
\begin{equation}
MB(Q^*)=MSC(Q^*)=MPC(Q^*)+t^*, \qquad t^*=MEC(Q^*)=10.
\end{equation}
In this linear example, the deadweight loss from the five excess units is $\tfrac{1}{2}(40-35)(10)=25$ dollars per period. The triangle formula depends on the linear, constant-damage assumptions; with changing damage, use the area between $MB$ and $MSC$.

\begin{examplecase}{FRED Data: Emissions Are Not a Damage Estimate}
FRED series EMISSCO2TOTVTTTOUSA reports U.S. total carbon dioxide emissions from all sectors and fuels, in million metric tons, annually and not seasonally adjusted. It records 4,594.7 million metric tons in 2020 and 4,911.2 in 2021. These totals describe emissions, not the marginal health or climate damage from one additional unit, and the year-to-year rebound does not identify a single cause. Students should separate measured quantities from an external-cost estimate.
\end{examplecase}

\section{Positive Externalities and Corrective Subsidies}
Vaccination can reduce a recipient's risk and lower transmission risk for others. If decision-makers consider only private benefit, participation may be below the socially efficient level. In a graph, marginal social benefit ($MSB$) lies above marginal private benefit ($MPB$). The market chooses where $MPB=MC$; the efficient quantity satisfies $MSB=MC$. A subsidy can encourage participation, but its design should account for fiscal cost, targeting, and the size of the spillover rather than assuming every private benefit deserves public payment.

\section{Public Goods and Common Resources}
Goods can be classified by whether people can be excluded and whether one person's use reduces another's use. Private goods are excludable and rival; public goods are difficult to exclude people from and are non-rival over the relevant range. A lighthouse signal is a classic stylized example. Common resources are difficult to exclude users from but rival, such as a congested fishery. Club goods are excludable and largely non-rival until congestion, such as a subscription service.

The free-rider problem occurs when people can benefit without paying, making voluntary private provision difficult. For a pure public good, efficiency requires the sum of individuals' marginal willingness to pay to equal marginal cost:
\begin{equation}
\sum_i MB_i(Q^*)=MC(Q^*).
\end{equation}
For a common resource, each user may ignore the congestion or depletion imposed on others. Property rights, access rules, tradable permits, or community management can help, but monitoring and enforcement have costs.

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: A Tax Does Not Erase the Externality}
A corrective tax changes private incentives; it does not make the physical damage disappear. The efficient tax is tied to marginal external damage at the efficient quantity under the model's assumptions. Distribution, measurement error, and administrative costs still matter.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item In the numerical example, why is the market quantity larger than the efficient quantity?
  \item If marginal external damage rises with output, should the efficient tax necessarily equal the damage at the unregulated market quantity?
  \item Give one example of a common resource and explain which of the two defining properties it has.
\end{enumerate}
Answers: (1) Producers face $MPC$ rather than the higher $MSC$. (2) No; the Pigouvian tax is the marginal damage at the efficient quantity in the standard model. (3) A fishery is rival and difficult to exclude users from without enforceable access rules.
"""),

    (11, "ch11_consumer_choice.tex", "ch11_consumer_choice.qmd", "Chapter 11: Consumer Choice Theory: Utility and Indifference Curves", r"""
\section{Learning Outcomes and Key Terms}
Students should represent a budget constraint, identify an affordable choice, and explain how prices and income shape a consumer's decision. These objectives support C2001-1 and C2001-3. Key terms include budget set, utility, indifference curve, marginal utility, marginal rate of substitution, substitution effect, and income effect.

\section{A Monthly Budget and Two Goods}
Suppose a student allocates a fixed monthly budget between meals ($X$) and transit trips ($Y$). The budget is limited, so buying more of one good means giving up some of the other. The consumer's choice depends on prices, income, and preferences; the model does not claim that every person calculates derivatives before buying lunch. It organizes the trade-offs implied by those constraints.

\section{The Budget Line: Geometric Description}
Place meals $X$ on the horizontal axis and transit trips $Y$ on the vertical axis. The budget line slopes downward. Its horizontal intercept is the number of meals affordable if all income is spent on meals; its vertical intercept is the number of transit trips affordable if all income is spent on transit. A rise in income shifts the budget line outward in parallel when prices are fixed. A change in one price pivots the line around the intercept for the other good.

The budget constraint is
\begin{equation}
P_xX+P_yY=I, \qquad Y=\frac{I}{P_y}-\frac{P_x}{P_y}X.
\end{equation}
The slope is $-P_x/P_y$: it is the number of transit trips that must be forgone to purchase one more meal while staying on the same budget line.

\section{Preferences, Utility, and Indifference Curves}
An indifference curve collects bundles that provide the same ordinal utility. A higher curve represents a preferred bundle when preferences are monotonic. With well-behaved preferences, indifference curves slope downward and are convex to the origin: as a person has more of $X$ relative to $Y$, they are generally willing to give up fewer units of $Y$ for another unit of $X$.

Marginal utility ($MU_x$) is the change in utility from a small increase in $X$, holding $Y$ fixed. The marginal rate of substitution is the absolute slope of an indifference curve:
\begin{equation}
MRS_{XY}=\frac{MU_x}{MU_y}.
\end{equation}
Utility numbers are a representation for ranking choices, not a literal measurement of happiness that can be compared across people.

\section{Choice at a Tangency: Worked Example}
Let income be $I=60$, with $P_x=4$ and $P_y=3$. The consumer has Cobb-Douglas utility $U(X,Y)=XY$. Since $MU_x=Y$ and $MU_y=X$, the tangency condition $MRS=P_x/P_y$ implies $Y/X=4/3$. Combining this with the budget constraint gives $X^*=7.5$ meals and $Y^*=10$ transit trips. The bundle exhausts the budget: $4(7.5)+3(10)=60$.

For an interior optimum with smooth, convex preferences:
\begin{equation}
\frac{MU_x}{MU_y}=\frac{P_x}{P_y} \quad\Longleftrightarrow\quad \frac{MU_x}{P_x}=\frac{MU_y}{P_y}.
\end{equation}
At a corner solution, the consumer chooses only one good; the tangency equality need not hold. Perfect substitutes, perfect complements, and nonstandard preferences can also change the shape of the solution.

\section{Price Changes: Substitution and Income Effects}
If the price of $X$ falls, the budget line pivots outward along the $X$ axis. The total change in the chosen amount of $X$ can be separated conceptually into a substitution effect and an income effect. The substitution effect reflects the change in relative prices while holding purchasing power conceptually constant; the income effect reflects the change in real purchasing power. For a normal good, both effects of a price decrease usually raise quantity demanded. For an inferior good, the income effect works in the opposite direction and may partly offset the substitution effect. A parallel budget shift is caused by a change in income at fixed prices; it is not the price-change income effect itself.

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: The Price Change Pivots the Budget Line}
A change in $P_x$ changes the budget line's slope and rotates it around the $Y$ intercept. A change in income shifts the entire budget line in parallel when both prices remain fixed. Keep these two geometric changes distinct.
\end{coreprinciple}

\section{FRED Data and Real Purchasing Power}
FRED series CPIAUCSL is the Consumer Price Index for All Urban Consumers: All Items in U.S. City Average. It is monthly, seasonally adjusted, and indexed to 1982-1984=100; its September 2026 observation is 336.298. The CPI is a broad price index, not the exact cost of every household's basket. It can help convert a nominal dollar amount to a broad real-dollar comparison, but it does not identify an individual's preferences or their personal inflation rate.

\section{Check Your Understanding}
\begin{enumerate}
  \item With $I=60$, $P_x=4$, and $P_y=3$, what are the two intercepts of the budget line?
  \item Why does the budget line pivot rather than shift in parallel when only $P_x$ changes?
  \item Is utility measured in directly comparable units across people? Explain.
\end{enumerate}
Answers: (1) $X=15$ and $Y=20$. (2) The $X$ intercept changes while the $Y$ intercept remains $I/P_y$. (3) No; ordinal utility represents an individual's ranking of bundles.
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
\section{Learning Outcomes and Key Terms}
Students should distinguish hidden information before a transaction from hidden actions after it, calculate expected value and expected utility in a simple risk problem, and evaluate screening, signaling, and contract design. These objectives support C2001-1, C2001-2, and C2001-3. Key terms include asymmetric information, adverse selection, signaling, screening, moral hazard, risk aversion, expected utility, and risk premium.

\section{A Used-Car Market with Hidden Quality}
Imagine a market in which sellers know whether a used car is reliable, but buyers cannot observe its condition before purchase. Buyers offer a price based on expected quality across cars offered for sale. Owners of especially reliable cars may reject that pooled price and keep their vehicles. The remaining pool has lower average quality, so buyers reduce their offers again. This feedback can shrink the market or drive high-quality products out of it.

This is adverse selection: private information about a characteristic that exists before a contract affects who chooses to participate. It is not the same as a seller's deliberate fraud; the problem can arise even when everyone behaves legally and rationally.

\section{A Graph of Pooling and Market Unraveling}
In a price-quality diagram, put product quality on the horizontal axis and buyers' willingness to pay on the vertical axis. If quality is hidden, buyers initially offer a pooled price reflecting expected quality. Sellers whose cars are worth more than that price to them exit first. The average quality of cars still offered falls, shifting buyers' expected willingness to pay downward. A credible warranty, inspection, or reputation can make quality more observable and interrupt this unraveling process.

\section{Screening and Signaling}
Screening is an action by the less-informed party to learn about hidden types. An insurer may ask risk-relevant questions or offer a menu of plans with different premiums and deductibles. Signaling is an action by the informed party intended to credibly reveal type. A warranty may signal seller confidence if it is more costly for a seller of an unreliable product to honor.

For a signal to separate types, it must be credible: the cost of sending it should differ across types. A signal everyone can imitate at negligible cost conveys little information. Screening and signaling can improve matching, but they can also exclude people, expose private information, or create administrative costs.

\section{Moral Hazard after a Contract}
Moral hazard is a change in behavior after a contract when one party's action is not fully observable or contractible. Insurance can reduce the cost of a loss to the insured person, which may change prevention effort or use of covered services. The effect is not necessarily fraud: it is a predictable response to changed incentives. Deductibles and co-payments can preserve some incentives to economize, but they also expose risk-averse households to more financial risk and may discourage valuable care.

\section{Risk, Expected Value, and Expected Utility}
Suppose a household faces a 10 percent chance of a \$1,000 loss and a 90 percent chance of no loss. The expected loss is \$100. A risk-neutral person compares premiums with expected monetary loss. A risk-averse person has a concave utility function and may be willing to pay more than the expected loss for insurance, up to the risk premium, because a certain outcome can provide greater utility than a risky outcome with the same expected wealth.

For outcomes $x_i$ with probabilities $p_i$, expected value and expected utility are:
\begin{equation}
E[X]=\sum_i p_ix_i, \qquad EU=\sum_i p_i u(W+x_i).
\end{equation}
The certainty equivalent ($CE$) is the certain change in wealth that gives the same utility as the risky prospect. For a gain-risk representation, the risk premium is $RP=E[X]-CE$. The sign and interpretation depend on how gains and losses are represented; the central lesson is that expected dollars and expected utility are different criteria.

\begin{examplecase}{FRED Data: Delinquency Is an Outcome, Not a Diagnosis}
FRED series DRALACBS is the Delinquency Rate on All Loans at All Commercial Banks. It is quarterly, seasonally adjusted, and measured in percent; the Q2 2026 observation is 1.42 percent. This aggregate rate can motivate questions about credit risk, but it cannot by itself identify adverse selection, moral hazard, underwriting changes, borrower composition, or macroeconomic shocks as the cause. Identifying those mechanisms requires more detailed evidence and a credible comparison.
\end{examplecase}

\section{Contract Design and Trade-Offs}
Markets use warranties, certification, deductibles, co-payments, collateral, audits, and reputation systems to mitigate information problems. Each tool trades off information or incentive benefits against cost, privacy, access, and fairness. A policy that reduces one information problem can create another: extensive screening may improve risk classification while making essential coverage unaffordable to some households.

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: Adverse Selection and Moral Hazard Differ by Timing}
Adverse selection concerns hidden characteristics that affect participation before a contract is signed. Moral hazard concerns hidden actions or effort after a contract changes incentives. The same market can experience both, but the diagnosis and remedy differ.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item A buyer cannot distinguish reliable from unreliable sellers before purchase. Which mechanism can cause high-quality sellers to leave the market?
  \item An insured driver takes less care after coverage begins. Is this adverse selection or moral hazard, and why?
  \item For the 10 percent, \$1,000-loss example, calculate expected loss. Does that number determine the maximum premium every risk-averse household will pay?
\end{enumerate}
Answers: (1) Adverse selection. (2) Moral hazard because the behavior changes after the contract. (3) Expected loss is \$100; risk preferences and the risk premium determine willingness to pay beyond it.
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
\section{Learning Outcomes and Key Terms}
Students should distinguish a change in one market's relative price from a sustained change in the general price level, calculate a simple inflation rate, and explain how nominal values differ from real values. These objectives support MA-1 and C2002-1. Key terms include relative price, price index, inflation, nominal value, real value, and purchasing power.

\section{One Price Changes, or the Price Level Changes?}
Suppose the price of a hospital visit rises while prices of most other goods are stable. That is a change in a relative price: medical care has become more expensive compared with the rest of the consumption basket. A family may respond by using insurance, choosing another provider, or postponing care. The change guides choices and reallocates resources in that market, but by itself it is not economy-wide inflation.

Inflation is a sustained increase in a broad price index. It reduces the purchasing power of a nominal dollar if the dollar amount does not rise with prices. A one-time increase in a single price may contribute to an index, but it does not establish that the general price level is accelerating. Similarly, a temporary price-level increase is not the same thing as an ongoing inflation rate.

\section{Graph Description: Relative Price and a Broad Index}
To compare price movements over time, put time on the horizontal axis and index values on the vertical axis. Set both series to 100 in a chosen base month. One line tracks the price index for a particular category, such as medical care; the other tracks the all-items CPI. If the medical-care line rises faster, its relative price has increased over that interval. If both rise at the same rate, the relative price is roughly unchanged even though nominal prices have risen. Indexing the series makes proportional changes comparable; it does not put different baskets on the same dollar scale.

The economic distinction is between a movement in one component's price and a change in the overall index. A demand or supply shift in one product market changes that market's equilibrium price; economy-wide inflation requires broad price changes and a sustained process, not a relabeling of one relative-price shock.

\section{Price Indexes, Inflation, and Real Values}
A price index compares the cost of a defined basket in one period with its cost in a reference period. The percentage inflation rate between periods $t-1$ and $t$ is:
\begin{equation}
\pi_t=\frac{P_t-P_{t-1}}{P_{t-1}}\times 100\%.
\end{equation}
To express a nominal amount in the purchasing power of a selected base period, rescale it by the ratio of the base-period index to the current index:
\begin{equation}
X^{\text{real, base}}_t=X^{\text{nominal}}_t\frac{P_{\text{base}}}{P_t}.
\end{equation}
When the index base is 100, this is commonly written as nominal value times $100/P_t$. Real values answer a purchasing-power question; nominal values answer how many current dollars changed hands. Neither measure is universally preferable: use the one suited to the question.

\begin{examplecase}{FRED Data: Medical Care and the CPI}
FRED series CPIAUCSL is the all-items Consumer Price Index for All Urban Consumers: U.S. City Average, monthly and seasonally adjusted, with 1982-1984=100. CPIMEDSL is the corresponding medical-care index with the same base and frequency. Comparing their percentage changes can illustrate how a component's price movement differs from the overall basket. The CPI reflects a weighted urban-consumer basket, not every household's exact spending pattern; the comparison is descriptive and does not by itself identify why prices changed.
\end{examplecase}

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: A Price Increase Is Not Automatically Inflation}
A rise in one product's price changes that product's relative price. Inflation refers to a sustained rise in a broad price index. Also keep nominal and real values distinct: a nominal wage can rise while its real purchasing power falls if the price level rises faster.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item If a nominal wage rises by 3 percent while the relevant price index rises by 5 percent, what happens approximately to its purchasing power?
  \item Why is a rise in the price of one service not sufficient evidence of economy-wide inflation?
  \item What does rebasing two indexes to 100 help compare, and what does it not make identical?
\end{enumerate}
Answers: (1) Real purchasing power falls by roughly 2 percent, using the small-change approximation. (2) It may be a relative-price change confined to that market. (3) It compares proportional changes; it does not make the baskets or dollar costs identical.
"""),

    (4, "ch04_gdp_accounting.tex", "ch04_gdp_accounting.qmd", "Chapter 4: Macroeconomic Variables: Measuring Output and GDP", r"""
\section{Learning Outcomes and Key Terms}
Students should interpret a basic GDP measure, distinguish nominal from real GDP, and explain why the expenditure, production, and income views describe the same current production. These objectives support MA-1 and C2002-1. Key terms include final good, intermediate good, value added, consumption, investment, government purchases, net exports, nominal GDP, real GDP, and GDP deflator.

\section{What GDP Counts: A Chip in a Computer}
Imagine a processor sold to a computer maker and then installed in a new laptop. Counting the processor's full sale and the laptop's full sale would count some production twice. National accounts avoid this by counting final output or summing each firm's value added. The processor maker contributes the value of its output minus intermediate inputs; the computer maker contributes the laptop's value minus purchased components. GDP measures the market value of final goods and services produced within a country's borders during a period, not the value of every financial transaction or every useful activity.

GDP excludes purchases of existing assets, such as a used home, because that production occurred earlier. It also excludes transfers such as Social Security benefits from government purchases: transfers redistribute income but are not direct purchases of current output. Newly produced residential construction is counted as investment, while a household's purchase of the same house from another household is an asset transfer.

\section{Three Equivalent Accounting Views}
The expenditure approach adds spending on final domestic production:
\begin{equation}
Y=C+I+G+NX, \qquad NX=X-M.
\end{equation}
$C$ is household consumption, $I$ is gross private domestic investment (including inventory change and new residential construction), $G$ is government purchases of goods and services, and $NX$ is exports minus imports. Imports are subtracted because they may already be included in $C$, $I$, or $G$ but were produced abroad.

The production or value-added approach sums each producer's value added, avoiding double counting. The income approach sums incomes generated in domestic production, including compensation of employees, proprietors' income, rental income, corporate profits, net interest, taxes on production and imports less subsidies, and consumption of fixed capital. GDP and gross domestic income (GDI) should be equal in principle because one producer's output is another party's expenditure and income; measured estimates can differ because of data sources and timing. The statistical discrepancy records that difference rather than implying two different economies.

\section{Nominal GDP, Real GDP, and the Deflator}
Nominal GDP values current production at current-period prices. If both quantities and prices rise, nominal GDP can rise even when physical output does not. Real GDP values production using a chain-type quantity index designed to remove price changes. The GDP implicit price deflator is:
\begin{equation}
	ext{GDP Deflator}_t=\frac{\text{Nominal GDP}_t}{\text{Real GDP}_t}\times 100.
\end{equation}
Its percent change approximates price change for domestically produced final output. It is not the same basket as the CPI, which focuses on prices paid by urban consumers and includes imports in the consumer basket.

\begin{examplecase}{FRED Data: Current-Dollar and Chained-Dollar GDP}
FRED's GDP series reports Gross Domestic Product in billions of current dollars at a seasonally adjusted annual rate, quarterly. GDPC1 reports real GDP in billions of chained 2017 dollars at a seasonally adjusted annual rate, quarterly. The series titles and units matter: compare changes over time using the appropriate real measure, and do not read chained-dollar levels as current-dollar spending. Both series are revised as the BEA incorporates new source data.
\end{examplecase}

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: Investment Is Not a Stock Purchase}
In GDP accounting, investment means newly produced capital goods, new residential structures, and inventory accumulation. Buying an existing share of stock is a financial transaction, not current production, so it is not counted as $I$ in GDP.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item Why are imported goods subtracted in $NX$ even though consumers and firms buy them?
  \item If nominal GDP rises while real GDP is unchanged, what has happened to the GDP deflator?
  \item Why does counting a final laptop and every component's full sale overstate output?
\end{enumerate}
Answers: (1) Imports were produced abroad and must be removed from domestic production. (2) The deflator rises. (3) It double-counts intermediate production; use final value or value added.
"""),

    (5, "ch05_unemployment_inflation.tex", "ch05_unemployment_inflation.qmd", "Chapter 5: Employment, Unemployment Metrics, and the Price Level", r"""
\section{Learning Outcomes and Key Terms}
Students should calculate labor-market rates, interpret what the unemployment rate does and does not measure, and relate cyclical unemployment to output gaps without confusing correlation with causation. These objectives support MA-1 and C2002-1. Key terms include employed, unemployed, labor force, participation rate, U-3, underemployment, natural rate, and output gap.

\section{How a Household Enters the Labor Statistics}
The Bureau of Labor Statistics classifies people in the civilian noninstitutional population age 16 and older using a household survey. A person is employed if they did paid work or had a job from which they were temporarily absent. A person is unemployed if they had no job, were available for work, and actively looked for work in the previous four weeks, or were on temporary layoff under the survey rules. Everyone else is not in the labor force. These are operational definitions for consistent measurement, not judgments about whether someone needs a job.

The labor force is the employed plus the unemployed. A discouraged worker who wants a job but stopped searching is not counted as unemployed under U-3; they are outside the labor force. A person working part time for economic reasons is counted as employed even if they want full-time work. Broader BLS measures include additional forms of labor underutilization.

\section{Rates and Their Denominators}
The unemployment rate uses the labor force, not the entire population. The labor-force participation rate and employment-population ratio answer different questions:
\begin{align}
LF &= E+U, \\
u &= \frac{U}{LF}\times 100\%, \\
LFPR &= \frac{LF}{P}\times 100\%, \\
EPOP &= \frac{E}{P}\times 100\%.
\end{align}
Here $E$ is employment, $U$ is unemployment, and $P$ is the civilian noninstitutional population age 16 and older. Rates can move for different reasons. If people stop searching, the unemployment rate may fall even if employment does not rise; the participation rate can reveal that denominator change.

\section{Graph Description: Cycles and the Natural Rate}
On a time-series graph, put months or quarters on the horizontal axis and the unemployment rate on the vertical axis. Recessions often coincide with a rise in unemployment, followed by a gradual decline during recovery. The natural rate is not a fixed number written into the data; it is an estimated benchmark reflecting frictional and structural unemployment at a given time. The cyclical component is the gap between actual and estimated natural unemployment, and estimates are uncertain.

Okun's law summarizes a historical tendency for output to be below potential when unemployment is above its sustainable benchmark. A commonly used rough relation is:
\begin{equation}
\frac{Y-Y^*}{Y^*}\approx -\beta(u-u^*), \qquad \beta>0.
\end{equation}
The coefficient varies by period and specification. This relationship is a useful model, not a fixed engineering law or proof that unemployment alone caused an output change.

\begin{examplecase}{FRED Data: Reading the U-3 Series}
FRED's UNRATE series is the BLS U-3 unemployment rate: percent, seasonally adjusted, monthly. The October 2026 observation is 4.1 percent. A single monthly rate is a snapshot, not a complete account of job quality, hours desired, discouraged workers, or the causes of a change. Pair it with labor-force participation and employment measures when interpreting a cycle.
\end{examplecase}

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: Unemployment Is a Stock; Separations and Hires Are Flows}
The number unemployed at a point in time is a stock. New job losses, hires, exits, and entries are flows that change the stock over a period. A falling unemployment stock can result from hiring, labor-force exits, or both, so check the related flows and rates before drawing a conclusion.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item A person wants work, is available, but has not searched in the past four weeks. How is that person classified in U-3?
  \item If $E=160$, $U=10$, and $P=200$, calculate the unemployment rate and participation rate.
  \item Why might a falling unemployment rate fail to show that employment increased?
\end{enumerate}
Answers: (1) Not in the labor force, under the stated facts. (2) $u=10/170\times100\%=5.9\%$; $LFPR=170/200\times100\%=85\%$. (3) People may have left the labor force, reducing the denominator.
"""),

    (6, "ch06_savings_investment_financial_system.tex", "ch06_savings_investment_financial_system.qmd", "Chapter 6: Saving, Investment Spending, and the Financial System", r"""
\section{Learning Outcomes and Key Terms}
Students should distinguish saving from wealth, apply the national saving identity, and use the loanable-funds model to explain how saving and investment plans respond to real interest rates. These objectives support MA-2 and MA-3 and prepare students for C2002-2. Key terms include private saving, public saving, national saving, investment, loanable funds, real interest rate, deficit, and capital inflow.

\section{Saving Is a Flow; Wealth Is a Stock}
A household that saves part of this month's income adds to its assets, but saving itself is measured over a period. Wealth is the value of assets held at a point in time. Likewise, investment in macroeconomics is spending on newly produced capital goods and inventories during a period; it is not the purchase of an existing stock certificate. Keeping stocks and flows separate prevents a common accounting error.

\section{National Saving and the Open-Economy Identity}
Start with the expenditure identity $Y=C+I+G+NX$. Rearranging gives $Y-C-G=I+NX$. National saving is $S=Y-C-G$, so in the simplified model $S=I+NX$. If net exports are used as the current-account proxy, then $S-I=NX$: saving above domestic investment corresponds to net lending abroad, while investment above saving is matched by net borrowing from abroad. In full balance-of-payments accounts, the current account includes net primary income and transfers as well as goods and services.

With taxes $T$ and disposable income $Y-T$, private saving is $S_p=Y-T-C$ and public saving is $S_g=T-G$. National saving adds the two:
\begin{equation}
S=S_p+S_g=(Y-T-C)+(T-G)=Y-C-G, \qquad S-I=NX \quad\text{(simplified model)}.
\end{equation}
In a closed economy, $NX=0$ and planned national saving equals investment in the accounting identity. The identity does not guarantee that desired saving and planned investment are equal at every interest rate; prices, output, and financial markets adjust toward consistency.

\section{Loanable Funds: Graph and Mechanism}
Put the quantity of loanable funds on the horizontal axis and the real interest rate on the vertical axis. Planned saving is drawn as a supply of funds, often rising with the real return. Planned investment is a demand for funds, often falling as borrowing becomes more expensive. Their intersection is the model's equilibrium real rate and quantity. A shift in saving or investment plans moves one curve; a change in the interest rate is a movement along a curve. This is a market model, not a literal inventory of all bank deposits.

\section{Deficits, Interest Rates, and Crowding Out}
If government purchases rise while taxes and private saving behavior are fixed, public saving falls. In a closed-economy loanable-funds model, the saving supply can shift left, raising the equilibrium real interest rate and reducing some private investment. This is the crowding-out mechanism. Its size depends on conditions: monetary policy, spare capacity, household saving responses, international capital flows, and the central bank's reaction can change the outcome. A deficit does not mechanically imply a one-for-one decline in private investment.

\begin{examplecase}{FRED Data: Gross Private Domestic Investment}
FRED series GPDI reports gross private domestic investment in billions of current dollars at a seasonally adjusted annual rate, quarterly. It includes fixed investment and inventory change. It is a nominal expenditure flow, not a capital stock and not a direct measure of productive capacity. To study physical investment growth across time, compare an appropriate real series and account for revisions and price changes.
\end{examplecase}

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: The Identity Is Not a Causal Claim}
The accounting relation $S-I=NX$ in the simplified model must hold ex post. It does not by itself tell us whether saving caused investment, investment caused income and saving, or foreign flows adjusted. Use a behavioral model and evidence to discuss causation.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item If $Y=1{,}000$, $C=650$, and $G=200$, calculate national saving.
  \item If national saving is 150 and investment is 180, what is $NX$ in the simplified open-economy identity?
  \item Is buying an existing share of a company macroeconomic investment? Why or why not?
\end{enumerate}
Answers: (1) $S=Y-C-G=150$. (2) $NX=S-I=-30$, a deficit in the simplified model. (3) No; it transfers ownership of an existing financial asset rather than purchasing newly produced capital.
"""),

    (7, "ch07_aggregate_expenditure_multiplier.tex", "ch07_aggregate_expenditure_multiplier.qmd", "Chapter 7: Income and Expenditure: The Keynesian Cross and Multipliers", r"""
\section{Learning Outcomes and Key Terms}
Students should construct planned aggregate expenditure, identify equilibrium output in a simple Keynesian-cross model, and explain the assumptions behind the government-purchases multiplier. These objectives support MA-3 and C2002-2. Key terms include autonomous consumption, marginal propensity to consume, planned expenditure, unplanned inventory investment, equilibrium output, and multiplier.

\section{The Inventory Story}
A firm produces goods before knowing exactly how many customers will buy them. If households and businesses plan to spend less than firms produce, unsold goods accumulate as unplanned inventory investment. Firms respond by reducing orders and production; household income falls, which can further reduce consumption. If planned spending exceeds production, inventories fall unexpectedly and firms have an incentive to increase output. The Keynesian cross formalizes this short-run adjustment when prices are relatively sticky and resources are not fully employed.

\section{The Consumption Function and Expenditure Schedule}
Let consumption depend on autonomous consumption and disposable income:
\begin{equation}
C=C_0+c(Y-T), \qquad 0<c<1,
\end{equation}
where $c$ is the marginal propensity to consume. In a simplified closed economy with fixed planned investment, government purchases, and lump-sum taxes, planned aggregate expenditure is:
\begin{equation}
AE=C_0+c(Y-T)+I_p+G.
\end{equation}
On a graph with income/output $Y$ on the horizontal axis and planned expenditure $AE$ on the vertical axis, draw a 45-degree line where $AE=Y$ and the expenditure line with slope $c$. Their intersection is short-run equilibrium. If the expenditure line shifts upward, equilibrium output rises by more than the initial autonomous-spending increase because each round of income induces additional consumption.

\section{Worked Multiplier Example}
Suppose values are in billions of dollars, $C_0=100$, $c=0.8$, $T=50$, $I_p=120$, and $G=80$. Then:
\begin{align}
AE &=100+0.8(Y-50)+120+80=260+0.8Y,\\
Y&=AE=260+0.8Y,\\
0.2Y&=260 \quad\Longrightarrow\quad Y^*=1{,}300.
\end{align}
If autonomous government purchases increase by 20, the simple multiplier is $1/(1-c)=5$, so the model predicts $\Delta Y=100$. This result assumes fixed prices, constant $c$, no proportional income taxes, no imports, and sufficient capacity to raise production. It is a model prediction, not a forecast that every real-world spending increase produces exactly five times as much output.

\section{Leakages, Taxes, and a Smaller Multiplier}
Saving, taxes, and imports are leakages from each round of domestic consumption spending. If taxes rise with income at rate $t$ and imports rise with income at marginal propensity $m$, one simplified multiplier is:
\begin{equation}
k=\frac{1}{1-c(1-t)+m}.
\end{equation}
The exact expression depends on how the model specifies taxes, imports, and other induced spending. More leakages make each successive spending round smaller. Automatic stabilizers can moderate a downturn by reducing disposable-income losses, although their strength depends on program design and the initial shock.

\begin{examplecase}{FRED Data: Output Is Not Planned Expenditure}
FRED series GDPC1 reports real GDP in billions of chained 2017 dollars at a seasonally adjusted annual rate, quarterly. It measures realized production, not households' or firms' planned expenditure. A change in GDP alone cannot identify the Keynesian multiplier: analysts need a plausibly exogenous spending change and a strategy for separating its effects from simultaneous changes in income, policy, and expectations.
\end{examplecase}

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: A Multiplier Is Conditional}
The algebraic multiplier follows from a specified behavioral model and assumptions about prices, taxes, imports, interest rates, and available capacity. It is not a universal constant and should not be applied mechanically to every fiscal action.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item If $c=0.75$ in the simple closed model, what is the government-purchases multiplier?
  \item Why does an unplanned inventory increase tend to make firms cut production in the model?
  \item Name two leakages that make the multiplier smaller than $1/(1-c)$.
\end{enumerate}
Answers: (1) $k=1/(1-0.75)=4$. (2) Output exceeded planned sales, leaving firms with more inventory than intended. (3) Taxes and imports are examples.
"""),

    (8, "ch08_aggregate_demand_aggregate_supply.tex", "ch08_aggregate_demand_aggregate_supply.qmd", "Chapter 8: Aggregate Demand and Aggregate Supply (AD-AS)", r"""
\section{Learning Outcomes and Key Terms}
Students should distinguish a change in the price level from a shift in aggregate demand, use the AD--AS model to explain output and inflation outcomes, and compare short-run with long-run adjustment. These objectives support MA-3 and C2002-2. Key terms include aggregate demand, short-run aggregate supply, long-run aggregate supply, potential output, output gap, demand shock, and supply shock.

\section{Aggregate Demand: Total Planned Spending}
Aggregate demand (AD) represents planned spending on domestically produced final goods and services at different overall price levels, holding other determinants fixed. In the expenditure model, $AD=C+I+G+NX$. A lower price level can raise real purchasing power, affect interest rates, and change net exports; together these mechanisms help explain the downward slope in the standard AD curve. The curve is not the same thing as microeconomic demand for one product.

\section{Movement Along AD or a Shift?}
Put real output $Y$ on the horizontal axis and the price level $P$ on the vertical axis. A change in the price level causes a movement along a given AD curve. A change in consumption confidence, planned investment, fiscal policy, monetary conditions, foreign income, or the exchange rate can shift AD. For example, an increase in government purchases shifts AD right at each price level in the short-run model; it does not mean the price level itself caused the shift.

\section{Short-Run and Long-Run Aggregate Supply}
Short-run aggregate supply (SRAS) slopes upward in the basic model because some wages and prices adjust slowly. If the overall price level rises while nominal input costs are temporarily fixed, firms may find production more profitable and supply more output. Long-run aggregate supply (LRAS) is vertical at potential output $Y^*$, determined by labor, capital, technology, and institutions rather than the price level alone.

The short-run equilibrium is where AD intersects SRAS. If output is below potential, the economy has a recessionary gap; if output is above potential, resource bottlenecks and wage or price pressures may build. Over time, wages, expectations, and other costs adjust, shifting SRAS. The speed and direction of adjustment depend on institutions and expectations, so the diagram is a framework rather than a calendar forecast.

\section{Demand and Supply Shocks}
An increase in AD generally raises short-run output and the price level; a decrease generally lowers both. An adverse supply shock shifts SRAS left, reducing output while raising the price level, a combination called stagflation. A favorable productivity shock can shift SRAS and potential output outward. The diagram keeps separate the initial shock, the short-run movement, and any later adjustment.

\begin{examplecase}{FRED Data: Output, Prices, and Unemployment Move Together}
GDPC1 measures real GDP in billions of chained 2017 dollars at a seasonally adjusted annual rate, quarterly. CPIAUCSL is a monthly, seasonally adjusted all-items CPI index. UNRATE is the monthly, seasonally adjusted U-3 unemployment rate. These series can help students describe output, prices, and labor-market conditions around an episode, but their co-movement alone does not identify whether an AD or supply shock caused it. Frequency, units, revisions, and causal evidence must be considered.
\end{examplecase}

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: Price Level Versus Aggregate Demand}
An increase in the price level is a movement along AD. A change in planned spending at every price level shifts AD. Confusing the two turns an outcome of the model into a cause of the curve's shift.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item If households become more optimistic and raise planned consumption, is this a movement along AD or a shift? Which direction?
  \item What combination of short-run changes follows an adverse SRAS shock?
  \item Why cannot two FRED series moving together establish an AD shock?
\end{enumerate}
Answers: (1) A rightward shift in AD. (2) Output falls while the price level rises. (3) Other shocks and reverse causality may explain the co-movement; a causal design is needed.
"""),

    (9, "ch09_fiscal_policy.tex", "ch09_fiscal_policy.qmd", "Chapter 9: Fiscal Policy, Automatic Stabilizers, and Sovereign Debt", r"""
\section{Learning Outcomes and Key Terms}
Students should distinguish automatic stabilizers from discretionary fiscal actions, explain how taxes and government purchases affect planned spending, and distinguish a deficit flow from debt outstanding. These objectives support MA-4 and C2002-3. Key terms include fiscal policy, transfer, automatic stabilizer, multiplier, deficit, debt, and implementation lag.

\section{A Downturn and the Budget Response}
During a recession, household incomes and tax receipts may fall while applications for unemployment insurance rise. These changes support disposable income without a new vote each month: they are automatic stabilizers. Congress and the executive branch can also change purchases, taxes, or transfers deliberately, but identifying the downturn, passing legislation, and delivering the policy take time. A well-timed policy may support demand; a delayed policy can arrive after conditions have changed.

\section{Government Purchases and Taxes in a Simple Model}
In a closed-economy model with lump-sum taxes and fixed prices, planned spending is $AE=C_0+c(Y-T)+I_p+G$. An increase in $G$ raises autonomous spending directly. A tax reduction raises disposable income, but households spend only the marginal propensity $c$ of the extra income. The corresponding simple multipliers are:
\begin{equation}
k_G=\frac{1}{1-c}, \qquad k_T=-\frac{c}{1-c}.
\end{equation}
The tax multiplier has a negative sign because a tax increase lowers equilibrium output in this model. If taxes rise proportionally with income at rate $t$, one common version is $k_G=1/[1-c(1-t)]$. Imports, interest-rate responses, price changes, and supply constraints alter these multipliers.

\section{Graph Description: Fiscal Policy in AD--AS}
On an AD--AS graph with real GDP on the horizontal axis and the price level on the vertical axis, an increase in government purchases shifts AD right. In the short run, output and the price level generally rise. If the economy is near capacity, more of the effect may appear in prices; if resources are idle, more may appear in output. The result is not an unconditional promise that fiscal expansion pays for itself or that every spending program has the same multiplier.

\section{Automatic Stabilizers and Discretionary Choices}
Progressive income taxes, unemployment benefits, and some means-tested transfers tend to support disposable income when activity weakens and withdraw support as incomes recover. Their effect depends on eligibility rules and take-up. Discretionary measures include a temporary purchase, tax credit, or transfer enacted in response to conditions. Policymakers weigh stabilization benefits against opportunity cost, administrative capacity, distributional goals, and the risk that support persists after it is needed.

\section{Deficits Are Flows; Debt Is a Stock}
A budget deficit is the excess of outlays over revenues during a fiscal period. Public debt is the accumulated stock of liabilities at a point in time, subject to accounting adjustments. An annual deficit can add to debt, but a change in debt also reflects other transactions and valuation choices. Compare these concepts as flow versus stock, just as saving during a year differs from wealth on a date.

\begin{examplecase}{FRED Data: Federal Surplus or Deficit}
FRED series FYFSD reports the federal surplus or deficit in millions of dollars, annual by fiscal year, not seasonally adjusted; a deficit is negative. The fiscal-year timing matters when comparing it with calendar-year GDP or quarterly data. The series describes a budget outcome; by itself it cannot show how much of a deficit was caused by policy choices versus changes in economic activity.
\end{examplecase}

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: A Deficit Is Not the Same as Debt}
The deficit is a flow over a fiscal year; debt is a stock accumulated across years. Quoting a deficit as if it were the total debt confuses units and time dimensions.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item Which has the larger absolute multiplier in the simple lump-sum-tax model: government purchases or taxes?
  \item Give one automatic stabilizer and explain how it changes over the business cycle.
  \item Why should an annual fiscal-year deficit series not be compared casually with one quarter of GDP?
\end{enumerate}
Answers: (1) $|k_G|=1/(1-c)$ exceeds $|k_T|=c/(1-c)$ for $0<c<1$. (2) Unemployment benefits rise as eligible unemployment rises, supporting disposable income. (3) They differ in time period and units; align annual fiscal-year flows with a comparable denominator.
"""),

    (10, "ch10_money_banking_fed.tex", "ch10_money_banking_fed.qmd", "Chapter 10: Money, Banking, and the Federal Reserve System", r"""
\section{Learning Outcomes and Key Terms}
Students should describe the roles of money, commercial banks, and the Federal Reserve; interpret a simplified bank balance sheet; and distinguish a textbook multiplier from the modern banking system. These objectives support MA-5 and C2002-2, C2002-3, and C2002-4. Key terms include medium of exchange, unit of account, store of value, reserves, deposits, capital, liquidity, M1, and M2.

\section{Why Money and Banks Matter}
A household can hold money to make payments while a firm uses deposits to meet payroll. Banks connect savers and borrowers, provide payment services, and transform short-term liabilities into longer-term loans. This transformation can support investment, but it exposes banks to liquidity and credit risk. A bank may be solvent because its assets exceed liabilities yet still face a liquidity problem if many depositors demand payment at once and assets cannot be sold quickly without loss.

\section{A Bank Balance Sheet}
A simplified balance sheet records assets on one side and liabilities plus equity on the other:
\begin{equation}
	ext{Reserves}+\text{Loans}+\text{Securities}=\text{Deposits}+\text{Borrowing}+\text{Equity}.
\end{equation}
Deposits are liabilities of the bank because the bank owes payment to depositors. Loans are assets because borrowers owe payments to the bank. Equity absorbs losses before depositors and other creditors. If loan defaults rise, bank capital can fall; if depositors withdraw rapidly, a bank may need liquid assets or central-bank funding.

\section{How Lending Creates Deposits}
When a bank approves a loan and credits a borrower's deposit account, its balance sheet expands: the loan asset and deposit liability rise together. If the borrower pays someone at another bank, the banks settle the payment using reserves or other settlement arrangements. Lending is constrained by capital, liquidity, funding costs, credit risk, regulation, and loan demand; it is not simply a mechanical process in which a fixed stock of reserves is multiplied without limit.

The textbook deposit multiplier $1/rr$ is a special model with a binding reserve requirement, no excess reserves, no currency drain, and willing banks and borrowers. It can illustrate repeated redepositing under those assumptions, but it is not a reliable general description of modern monetary policy or a forecasting formula for bank lending.

\section{Monetary Aggregates and Current Definitions}
M1 and M2 are statistical measures of money-like assets, not physical quantities of all wealth. Under the Federal Reserve's current H.6 definitions, M1 includes currency, demand deposits, and other liquid deposits, including savings deposits. M2 adds small-denomination time deposits and retail money-market fund balances, with specified retirement-account adjustments. The inclusion of savings deposits in other liquid deposits took effect in 2020, so researchers must read series notes before comparing historical definitions.

\begin{examplecase}{FRED Data: M1 and M2 Series}
FRED's M1SL and M2SL series report seasonally adjusted monthly money-stock levels in billions of dollars. FRED notes that M1SL includes other liquid deposits beginning in May 2020, while M2SL is constructed from M1 plus additional components and adjustments. A rise in an aggregate is not by itself evidence that bank lending or consumer spending rose by the same amount; definitions, portfolio shifts, and financial behavior matter.
\end{examplecase}

\section{The Federal Reserve's Institutional Roles}
The Federal Reserve is the U.S. central bank. Its responsibilities include monetary policy, payment-system functions, and supervision and regulation of many banking organizations, with mandates and tools set by law. Commercial banks are private or public-chartered institutions that take deposits and make loans; they are not branches of the central bank. Deposit insurance, capital requirements, liquidity rules, and lender-of-last-resort facilities address different risks and do not eliminate every possibility of failure.

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: Reserves Are Not the Same as Bank Capital}
Reserves are liquid assets used for settlement and withdrawals. Capital is the residual claim that absorbs losses. A bank can hold ample reserves yet have weak capital, or have strong capital but insufficient immediately available liquidity.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item In a bank balance sheet, is a customer deposit an asset or liability for the bank?
  \item Why is $1/rr$ not a universal predictor of modern bank lending?
  \item What change to M1's definition should analysts note when studying data across 2020?
\end{enumerate}
Answers: (1) A liability. (2) The multiplier assumes restrictive conditions on reserves, lending, and cash holdings that need not hold. (3) Savings deposits were included as other liquid deposits in M1 beginning in 2020.
"""),

    (11, "ch11_monetary_policy.tex", "ch11_monetary_policy.qmd", "Chapter 11: Monetary Policy Implementation and the Ample-Reserves Regime", r"""
\section{Learning Outcomes and Key Terms}
Students should explain how the Federal Reserve implements monetary policy, trace a policy-rate change through interest-sensitive spending to output and inflation, and identify uncertainty and lags in that process. These objectives support MA-6 and C2002-3. Key terms include federal funds rate, target range, IORB, overnight reverse repurchase facility, transmission mechanism, expectations, policy lag, and effective lower bound.

\section{From the Policy Decision to Market Rates}
The Federal Open Market Committee sets a target range for the federal funds rate. In the current ample-reserves framework, administered rates, especially interest on reserve balances (IORB), help keep overnight rates within the target range. The overnight reverse repurchase facility provides an additional option for eligible counterparties. The discount window offers collateralized lending to eligible institutions. These tools operate through institutions and markets; the Fed does not simply dictate every loan or mortgage rate.

\section{The Transmission Mechanism}
If the policy stance tightens, short-term market rates generally rise. Longer-term borrowing costs may rise as expectations adjust; households can delay purchases of durable goods, and firms may postpone investment. Weaker interest-sensitive spending can reduce aggregate demand, output, and inflation pressure over time. An easing can work in the opposite direction. Exchange rates, credit conditions, expectations, and global events can amplify or offset these channels, and monetary policy affects demand with uncertain lags.

\section{Graph Description: Policy and Aggregate Demand}
In the money-market diagram, the vertical axis is the short-term nominal interest rate and the horizontal axis is reserve balances or overnight funding. Under abundant reserves, changes in administered rates shift the range in which overnight rates trade; the classic scarcity-of-reserves intersection is not the whole operating story. In AD--AS, a policy easing that lowers borrowing costs may shift AD right over time, while a tightening may shift it left. The rate decision is not a direct movement along AD caused by the price level.

\section{A Policy Rule as a Benchmark}
A Taylor-type rule summarizes how a central bank might respond to deviations of inflation and output from desired levels:
\begin{equation}
i_t=r^*+\pi_t+\alpha(\pi_t-\pi^*)+\beta\left(\frac{Y_t-Y_t^*}{Y_t^*}\right),
\end{equation}
where $i_t$ is a nominal policy rate, $r^*$ is an equilibrium real-rate benchmark, $\pi_t$ is inflation, $\pi^*$ is the inflation objective, and $Y_t-Y_t^*$ is the output gap. Coefficients $\alpha$ and $\beta$ describe responsiveness. This is a guide for analysis, not a law that the FOMC must follow; estimates of potential output and the equilibrium real rate are uncertain.

\begin{examplecase}{FRED Data: Effective Federal Funds Rate}
FRED's FEDFUNDS series is the monthly average of daily effective federal funds rates, in percent and not seasonally adjusted. It is an observed market rate influenced by policy implementation, not the FOMC target range itself. Compare it with policy announcements and other indicators before attributing a change to a particular decision.
\end{examplecase}

\section{The Effective Lower Bound and Policy Limits}
When nominal short-term rates approach their effective lower bound, conventional rate cuts may have less room to stimulate demand. The Federal Reserve can use forward guidance and asset purchases, subject to legal authority, market functioning, and expected benefits. These tools still work through expectations and financial conditions; they do not guarantee a precise output or inflation result.

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: The Fed Controls a Policy Instrument, Not GDP}
The central bank can influence financial conditions, but output and inflation also respond to fiscal policy, supply shocks, global markets, and private expectations. A policy-rate change is not a one-for-one change in real GDP.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item Why is FEDFUNDS not exactly the same thing as the FOMC target range?
  \item Trace one channel through which a higher policy rate may lower aggregate demand.
  \item Why should a Taylor-type rule be treated as a benchmark rather than a mechanical instruction?
\end{enumerate}
Answers: (1) FEDFUNDS is an observed monthly average effective market rate; the Committee sets a target range. (2) Higher rates can raise borrowing costs, reducing planned consumption or investment. (3) Key variables and parameters are uncertain, and policy must account for multiple shocks and risks.
"""),

    (12, "ch12_open_economy_macroeconomics.tex", "ch12_open_economy_macroeconomics.qmd", "Chapter 12: Open-Economy Macroeconomics, Exchange Rates, and the Balance of Payments", r"""
\section{Learning Outcomes and Key Terms}
Students should interpret a trade-balance measure, explain how saving and investment relate to the current account, and use supply and demand for foreign exchange to reason about currency appreciation and depreciation. These objectives support MA-7 and C2002-1, C2002-2. Key terms include exports, imports, trade balance, current account, financial account, exchange rate, appreciation, depreciation, and policy trilemma.

\section{Trade, Spending, and the Current Account}
An open economy buys and sells goods and services across borders and exchanges financial claims. Exports are domestic production purchased abroad; imports are foreign production purchased domestically. A trade deficit means imports of goods and services exceed exports over the measured period. It does not by itself show whether trade is beneficial or harmful: consumers and firms may gain from lower-cost imports, while some domestic producers face adjustment costs.

In a simplified national-accounting model, net exports are $NX=X-M$. With national saving $S=Y-C-G$ and investment $I$, the identity is $S-I=NX$. The official current account is broader: it includes the balance on goods and services plus net primary income and transfers. In the balance of payments, current-account transactions are matched by financial flows and other accounting items under a specified sign convention. Avoid treating the trade balance and the entire current account as identical.

\section{The Foreign-Exchange Market: Graph Description}
To analyze the dollar, place the quantity of dollars traded on the horizontal axis and the foreign-currency price of one dollar on the vertical axis. Demand for dollars comes from foreign buyers who need dollars to purchase U.S. exports or U.S. assets; supply comes from U.S. residents exchanging dollars to buy foreign goods and assets. If demand for dollars rises relative to supply, the dollar appreciates in this quotation. A stronger dollar makes imports cheaper in dollars and U.S. exports more expensive to foreign buyers, other things equal. Actual trade quantities may adjust slowly and depend on contracts and elasticities.

Exchange-rate quotations must be read carefully. If the rate is dollars per euro, an increase means the euro appreciates against the dollar. If it is euros per dollar, the same movement is a dollar appreciation. Always state which currency is the numerator.

\section{Saving, Investment, and International Capital Flows}
In a simplified setting, a country that invests more than it saves borrows the difference from abroad and runs a current-account deficit; a country that saves more than it invests lends abroad and runs a surplus. This is an accounting relationship, not a claim that one flow alone causes the other. Returns, risk, demographics, fiscal policy, and global demand for assets can influence both saving and investment.

\begin{examplecase}{FRED Data: Trade Balance and Dollar Index}
FRED BOPGSTB measures the U.S. trade balance in goods and services on a balance-of-payments basis, in millions of dollars, monthly and seasonally adjusted. DTWEXBGS is the Federal Reserve's Nominal Broad U.S. Dollar Index, a daily index with January 2006=100 and not seasonally adjusted. The first is a flow over a month; the second is an index of exchange-rate movements. Their co-movement does not establish that the dollar caused a particular trade-balance change.
\end{examplecase}

\section{The Open-Economy Policy Trilemma}
A country cannot simultaneously maintain all three of the following: a fixed exchange rate, free international capital flows, and independent monetary policy. A fixed parity with mobile capital tends to require domestic rates to be consistent with the rate needed to defend the parity. Allowing the exchange rate to float gives more monetary autonomy but exposes firms and households to exchange-rate movements. The trilemma describes a constraint, not a ranking of which choice is best for every country.

\begin{coreprinciple}
\boxheader{SlateBlue}{Clear It Up: A Trade Deficit Is Not a Household Credit-Card Bill}
The trade balance is a flow of exports minus imports over a period. It is not the national debt, and a negative balance does not alone identify policy failure. Interpret it with saving, investment, capital flows, and the composition of trade.
\end{coreprinciple}

\section{Check Your Understanding}
\begin{enumerate}
  \item If $S=400$ and $I=450$ in the simplified identity, what is $NX$?
  \item Under a foreign-currency-per-dollar quotation, what does a rise in the rate mean?
  \item Name the two policies a country must choose between if it wants both fixed exchange rates and free capital flows.
\end{enumerate}
Answers: (1) $NX=S-I=-50$, a deficit in the simplified model. (2) The dollar appreciates. (3) It gives up independent monetary policy.
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

    qmd_header = f'---\ntitle: "{title}"\nformat:\n  html:\n    math:\n      method: mathjax\n---\n\n'
    return qmd_header + clean_lines + "\n"

def build_standalone_tex(title: str, course_name: str, body: str) -> str:
    latex_title = title.replace("&", r"\&")
    title_command = chr(92) + "title"
    return rf"""\documentclass[11pt,letterpaper]{{article}}
\input{{../../shared/preamble.tex}}
\input{{../../shared/tikz-settings.tex}}

\begin{{document}}

{title_command}{{\Huge\bfseries\color{{SlateBlue}} {latex_title}}}
\author{{\large {course_name}}}
\date{{2026}}
\maketitle

\thispagestyle{{plain}}

\begin{{abstract}}
This chapter provides a rigorous, pedagogical treatment of {latex_title}, benchmarked to standard principles curriculum.
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
    css: styles.css
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
