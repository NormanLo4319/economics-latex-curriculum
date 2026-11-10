#!/usr/bin/env python3
"""
sync_readings_to_tex.py

Populates complete, unabridged textbook chapters into:
  - micro/chapters/*.tex
  - macro/chapters/*.tex
  - web_books/microeconomics/*.qmd
  - web_books/macroeconomics/*.qmd

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
# 1. LATEX CHAPTER SOURCES (STRICT UTF-8)
# =============================================================================

MICRO_CH01_TEX = r"""\documentclass[11pt,letterpaper]{article}
\input{../../shared/preamble.tex}
\input{../../shared/tikz-settings.tex}

\begin{document}

\title{\Huge\bfseries\color{SlateBlue} Chapter 1: Foundations of Microeconomic Analysis \& Core Principles}
\author{\large Principles of Microeconomics Curriculum}
\date{2026}
\maketitle

\thispagestyle{plain}

\begin{abstract}
This chapter provides a rigorous, pedagogical treatment of microeconomic foundations, scarcity, opportunity cost, marginal analysis, and incentives, benchmarked to Eric Chiang (\textit{Microeconomics: Principles for a Changing World}, 5th ed.) \& UC Berkeley Econ 1.
\end{abstract}

\tableofcontents
\vspace{1.5em}
\hrule
\vspace{1.5em}

\section{What Is Economics? Scarcity, Choice, and Method}
Economics is the social science that studies how individuals, institutions, and societies allocate scarce resources among competing ends to satisfy unlimited human wants.

\textbf{Attribution Note:} Content synthesizes concepts from Eric Chiang, \textit{Microeconomics: Principles for a Changing World} (5th ed., Worth Publishers, Chapter 1: ``Exploring Economics'').

\subsection{Microeconomics vs. Macroeconomics}
\begin{itemize}
  \item \textbf{Microeconomics:} Examines decision-making by individual economic units---such as households, workers, firms, and individual product and factor markets. It investigates how relative price signals coordinate supply and demand in specific sectors (e.g., the market for electric vehicles or pharmaceutical labor).
  \item \textbf{Macroeconomics:} Examines the aggregate performance of the economy as an organic whole, focusing on national output (GDP), economy-wide price instability (inflation), systemic labor underutilization (unemployment), and long-run economic growth.
\end{itemize}

\section{Economic Modeling and the Ceteris Paribus Assumption}
To analyze human behavior, economists formulate \textbf{economic models}---stylized, simplified representations of real-world phenomena that isolate cause-and-effect relationships by stripping away confounding variables.

\begin{equation}
\text{Ceteris Paribus} \equiv \text{``All other things held constant''}
\end{equation}

Economic models rely on assumptions (such as rational self-interest and net benefit optimization) not because humans are purely calculating machines, but because these abstractions yield predictable baseline tendencies across large populations.

\begin{examplecase}{Real-World Application: California Gasoline Taxes}
When modeling the effect of an increase in the California gasoline excise tax on consumer fuel purchases, economists hold public transit availability, regional household income, and crude oil spot prices constant (\textit{ceteris paribus}). In reality, transit routes and crude prices fluctuate simultaneously. Isolating the tax impact first establishes the clean directional policy response before introducing multi-variable empirical complexities.
\end{examplecase}

\section{Positive vs. Normative Economic Analysis}
Clear economic discourse separates factual mechanics from ethical prescriptions:
\begin{itemize}
  \item \textbf{Positive Economics:} Descriptive statements regarding how the economy actually operates. Positive claims are empirical assertions that can be tested, confirmed, or refuted using observable data (e.g., ``Increasing the statutory minimum wage to \$20 per hour will reduce teenage employment by 2.4\%'').
  \item \textbf{Normative Economics:} Prescriptive statements regarding how the economy \textit{ought} to be structured, incorporating ethical values and political priorities (e.g., ``The government ought to increase the statutory minimum wage to \$20 because every working individual deserves a living wage'').
\end{itemize}

\section{Critical Thinking Pitfalls in Economic Reasoning}
When evaluating economic arguments, analysts must guard against three pervasive analytical traps:
\begin{enumerate}
  \item \textbf{Confusing Correlation with Causation:} Presuming that because variables $A$ and $B$ move together, $A$ causes $B$ (e.g., ice cream sales and drownings both spike in July due to summer temperatures, not mutual causation).
  \item \textbf{The Post Hoc Ergo Propter Hoc Fallacy:} Concluding that because event $Y$ occurred sequentially after $X$, $X$ must have caused $Y$.
  \item \textbf{The Fallacy of Composition:} Mistakenly presuming that what is true for an individual component is automatically true for the aggregate whole.
\end{enumerate}

\section{Core Principle 1 --- Scarcity, Choice, and Opportunity Cost}
Because productive resources (land, labor, physical capital, and human capital) are finite, every decision implies an opportunity cost---the value of the next best alternative forgone.

\begin{equation}
\text{Economic Cost} = \text{Explicit Out-of-Pocket Costs} + \text{Implicit Opportunity Costs}
\end{equation}

\begin{coreprinciple}
\boxheader{Terracotta}{The Opportunity Cost of Higher Education}
An undergraduate student pays \$12,000 per year in college tuition, fees, and textbooks (explicit accounting cost). However, if the student could have earned \$40,000 working full-time as an administrative manager, the true economic cost of attending college is \$52,000 per year (\$12,000 + \$40,000). Room and board expenditures are only included to the extent they exceed baseline living expenses incurred regardless of enrollment.
\end{coreprinciple}

\section{Core Principle 2 --- Marginal Analysis and Rational Decision-Making}
Decisions are evaluated at the margin by weighing incremental benefits against incremental costs:
\begin{itemize}
  \item \textbf{Marginal Benefit (MB):} The additional satisfaction or revenue generated by consuming or producing one extra unit.
  \item \textbf{Marginal Cost (MC):} The additional opportunity cost incurred by producing or consuming one extra unit.
\end{itemize}

Net Benefit Maximization Rule: \textbf{Expand if $MB > MC$; Halt where $MB = MC$}.

\begin{examplecase}{Real-World Example: Airline Seat Pricing}
A commercial airliner with 180 seats has a total operating flight cost of \$18,000 (average cost = \$100 per seat). Ten minutes before departure, an unreserved seat remains empty, and a standby passenger offers \$60. A manager fixated on average cost would reject the offer because \$60 < \$100. A rational marginal manager accepts the \$60, recognizing that the marginal cost of carrying one extra passenger (a small snack and minor incremental jet fuel) is roughly \$10. Because $MB\text{ (\$60)} > MC\text{ (\$10)}$, selling the seat increases operating profits by \$50.
\end{examplecase}

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9]
 \draw[econ axis] (0,0) -- (6.5,0) node[right, econ label] {$Q$};
 \draw[econ axis] (0,0) -- (0,5.5) node[above, econ label] {$P, MC, MB$};
 \draw[mb curve] (0.5,5) -- (5.5,1) node[right] {$MB$};
 \draw[mc curve] (0.5,1) -- (5.5,5) node[right] {$MC$};
 \coordinate (E) at (3,3);
 \node[econ point] at (E) {};
 \draw[econ guide] (3,0) node[below] {$Q^*$} -- (E) -- (0,3) node[left] {$P^*$};
\end{tikzpicture}
\caption{Net Benefit Maximization at $MB = MC$}
\end{figure}

\section{Core Principle 3 --- Response to Incentives and the Peltzman Effect}
Human agents systematically adjust behavior when relative prices or costs change. Public interventions that alter incentives often induce secondary behavioral responses that counteract initial policy goals.

\begin{examplecase}{The Peltzman Effect in Automobile Safety}
In 1968, federal mandates for vehicle seatbelts and padded dashboards led economist Sam Peltzman to observe a surprising result: making cars safer reduced the perceived cost of reckless driving. Drivers responded by driving faster and braking later. While fatalities per crash dropped, total pedestrian and cyclist collisions rose substantially.
\end{examplecase}

\section{Core Principle 4 --- Markets, Efficiency, and the Invisible Hand}
As Adam Smith observed in \textit{The Wealth of Nations} (1776), decentralized price signals guide self-interested agents toward productive and allocative efficiency:
\begin{itemize}
  \item \textbf{Allocative Efficiency:} Resources are distributed to produce the specific bundle of goods and services most highly valued by society ($MB = MC$).
  \item \textbf{Productive Efficiency:} Goods are produced at the lowest possible per-unit cost using the most effective combinations of factor inputs.
\end{itemize}

\section{Core Principle 5 --- Market Failures and the Economic Role of Government}
When decentralized private transactions fail to allocate resources efficiently, a market failure occurs, establishing an economic rationale for public intervention:
\begin{itemize}
  \item \textbf{Externalities:} Unpriced costs or benefits imposed on third parties (e.g., pollution or basic research).
  \item \textbf{Market Power:} Firms restricting output to artificially inflate prices above marginal cost.
  \item \textbf{Public Goods:} Non-excludable and non-rival goods subject to free-riding (e.g., national defense).
  \item \textbf{Efficiency vs. Equity Trade-off:} Even perfectly efficient competitive markets can yield extreme inequality, requiring societies to balance allocative efficiency against distributive justice.
\end{itemize}

\end{document}
"""

MICRO_CH02_TEX = r"""\documentclass[11pt,letterpaper]{article}
\input{../../shared/preamble.tex}
\input{../../shared/tikz-settings.tex}

\begin{document}

\title{\Huge\bfseries\color{SlateBlue} Chapter 2: The Production Possibilities Frontier \& Gains from Trade}
\author{\large Principles of Microeconomics Curriculum}
\date{2026}
\maketitle

\thispagestyle{plain}

\begin{abstract}
This chapter models the production possibilities frontier (PPF), the law of increasing opportunity cost, symmetric vs. asymmetric technological shifts, and David Ricardo's theory of comparative advantage using an empirical two-region aircraft and wind turbine matrix.
\end{abstract}

\tableofcontents
\vspace{1.5em}
\hrule
\vspace{1.5em}

\section{The Production Possibilities Frontier (PPF) Model \& Core Assumptions}
The Production Possibilities Frontier (PPF) is an analytical economic model illustrating the maximum combinations of two goods or services an economy can produce when all available productive resources (land, labor, physical capital, and human capital) are fully and efficiently utilized under a fixed state of technology.

\textbf{Attribution Note:} Formalized by Paul Samuelson in \textit{Economics} (1948) and synthesized in Eric Chiang, \textit{Microeconomics: Principles for a Changing World} (5th ed., Worth Publishers, Chapter 2).

\subsection{Core Assumptions of the PPF Framework}
\begin{enumerate}
  \item \textbf{Resource Scarcity:} Productive factors are strictly bounded during the period under examination.
  \item \textbf{Full and Efficient Employment:} All factor inputs are actively engaged without operational waste or structural idling.
  \item \textbf{Fixed Technology:} Engineering processes and organizational practices remain constant.
  \item \textbf{Two-Good Economy:} Output is simplified to two alternative goods (or composite categories).
\end{enumerate}

\section{Opportunity Cost and the Law of Increasing Opportunity Cost}
Because resources are scarce, expanding the production of Good $X$ requires diverting inputs away from Good $Y$. The slope of the PPF measures the Marginal Rate of Transformation (MRT):
\begin{equation}
MRT = -\frac{\Delta Y}{\Delta X} = \left| \frac{dY}{dX} \right| = \frac{\text{Quantity of Good } Y \text{ Forgone}}{\text{Quantity of Good } X \text{ Gained}}
\end{equation}

\subsection{Constant vs. Increasing Opportunity Cost}
\begin{itemize}
  \item \textbf{Constant Opportunity Cost (Linear PPF):} Productive factors are perfectly interchangeable between both production processes. The slope remains constant along the frontier ($MRT = k$).
  \item \textbf{Increasing Opportunity Cost (Bowed-Out / Concave PPF):} Productive resources are specialized. Shifting factors into Good $X$ pulls inputs that are progressively less adapted to its production, causing opportunity costs to escalate.
\end{itemize}

\begin{examplecase}{Empirical Case: Healthcare Facilities vs. Clean Energy Infrastructure}
A regional economy allocates bonding capacity and engineering labor between Diagnostic Healthcare Facilities and Solar Energy Arrays. Initially, reallocating general electrical contractors efficiently constructs solar arrays. However, pushing exclusively toward solar requires reassigning specialized biomedical researchers and surgical nursing teams. Because these professionals possess a comparative disadvantage in manufacturing solar cells, the forgone healthcare services per megawatt rise exponentially, generating a bowed-out PPF.
\end{examplecase}

\section{Productive vs. Allocative Efficiency \& Outward Shifts}
\begin{itemize}
  \item \textbf{Productive Efficiency:} Producing directly along the PPF curve at minimum opportunity cost.
  \item \textbf{Allocative Efficiency:} The specific bundle on the PPF boundary where societal net marginal value is maximized ($MB = MC$).
\end{itemize}

\subsection{Symmetric vs. Asymmetric Technological Shifts}
General demographic growth or educational attainment expands the PPF symmetrically outward. In contrast, sector-specific innovation (e.g., robotic photolithography in semiconductor manufacturing) pivots the PPF outward along the affected axis while leaving the alternative intercept fixed.

\section{Ricardian Comparative Advantage \& Gains from Trade}
Opportunity cost determines comparative advantage. Voluntary exchange expands societal consumption possibilities beyond domestic production boundaries.

\begin{examplecase}{Numerical Case: Pacific Coast vs. Great Lakes Trade Matrix}
Allocating a standardized 1,000-hour block of skilled labor yields the following outputs:
\begin{itemize}
  \item \textbf{Pacific Coast:} 100 Aircraft or 200 Turbines.
  $$\text{Opportunity Cost of 1 Aircraft} = 2.0\text{ Turbines} \quad (\text{1 Turbine} = 0.5\text{ Aircraft})$$
  \item \textbf{Great Lakes:} 40 Aircraft or 120 Turbines.
  $$\text{Opportunity Cost of 1 Aircraft} = 3.0\text{ Turbines} \quad (\text{1 Turbine} = 0.33\text{ Aircraft})$$
\end{itemize}
Because $2.0 < 3.0$, the Pacific Coast possesses a \textbf{comparative advantage in Aircraft}. Because $0.33 < 0.5$, the Great Lakes holds a \textbf{comparative advantage in Turbines}.
\end{examplecase}

\section{The Terms of Trade and the Consumption Possibility Frontier (CPF)}
Mutually advantageous trade requires that the terms of trade (TOT) settle strictly between both domestic opportunity costs:
\begin{equation}
2.0\text{ Turbines} < 1\text{ Aircraft} < 3.0\text{ Turbines}
\end{equation}

At an agreed exchange rate of $1\text{ Aircraft} = 2.5\text{ Turbines}$:
\begin{itemize}
  \item The Pacific Coast exports 1 Aircraft (costing 2.0 turbines domestically) and receives 2.5 turbines, capturing a gain of $+0.5$ turbines per transaction.
  \item The Great Lakes imports 1 Aircraft for 2.5 turbines (saving 0.5 turbines compared to domestic production).
\end{itemize}
Both economies rotate their Consumption Possibilities Frontier (CPF) strictly beyond their domestic production possibilities.

\end{document}
"""

MACRO_CH01_TEX = r"""\documentclass[11pt,letterpaper]{article}
\input{../../shared/preamble.tex}
\input{../../shared/tikz-settings.tex}

\begin{document}

\title{\Huge\bfseries\color{SlateBlue} Chapter 1: First Principles of Economics \& Macroeconomic Systems}
\author{\large Principles of Macroeconomics Curriculum}
\date{2026}
\maketitle

\thispagestyle{plain}

\begin{abstract}
This chapter introduces the twelve systemic principles of macroeconomics, aggregate circular flows, the paradox of thrift, and policy trade-offs between allocative efficiency and distributional equity, benchmarked to Paul Krugman \& Robin Wells (\textit{Macroeconomics}, 6th ed.) \& UC Berkeley Econ 2.
\end{abstract}

\tableofcontents
\vspace{1.5em}
\hrule
\vspace{1.5em}

\section{The Twelve First Principles of Macroeconomics}
Macroeconomics investigates aggregate economic performance through twelve core principles spanning individual choice, strategic interaction, and economy-wide feedback loops.

\textbf{Attribution Note:} Framework synthesizes the canonical twelve-principle approach from Paul Krugman and Robin Wells, \textit{Macroeconomics} (6th ed., Worth Publishers, Chapter 1: ``First Principles'').

\subsection{Principles of Individual Choice (1--4)}
\begin{enumerate}
  \item \textbf{People Must Make Choices Because Resources Are Scarce:} Bounded aggregate labor, capital stocks, and natural resources require societal trade-offs between investment, private consumption, and environmental preservation.
  \item \textbf{Opportunity Cost:} The economic cost of any national outlay (such as high-speed rail) is measured by the alternative public infrastructure forgone.
  \item \textbf{Marginal Analysis:} Macroeconomic adjustments (e.g., quarterly capital equipment budgets) are decided at the margin by balancing marginal revenue against borrowing rates.
  \item \textbf{Incentive Response:} Human agents systematically exploit opportunities to make themselves better off when tax structures, subsidies, or interest rates adjust.
\end{enumerate}

\subsection{Principles of Choice Interaction (5--9)}
\begin{enumerate}
  \item[5.] \textbf{There Are Gains from Trade:} Specialization across national borders allows economies to consume beyond their domestic production boundaries.
  \item[6.] \textbf{Markets Move Toward Equilibrium:} Flexible price mechanisms adjust until shortages and surpluses clear ($Q_d = Q_s$).
  \item[7.] \textbf{Resources Should Be Used Efficiently:} An economy is Pareto efficient when it exhausts all opportunities to make some individuals better off without harming others.
  \item[8.] \textbf{Markets Usually Lead to Efficiency:} Decentralized market signals allocate productive factors to their highest-valued uses without centralized command.
  \item[9.] \textbf{When Markets Fail, Government Intervention Can Help:} Systemic breakdowns (e.g., bank runs, environmental degradation, severe monopoly power) require collective institutional stabilization.
\end{enumerate}

\subsection{Principles of Economy-Wide Interaction (10--12)}
\begin{enumerate}
  \item[10.] \textbf{One Person's Spending Is Another Person's Income:} Because every dollar spent becomes income for another entity, an aggregate pull-back in consumer spending contracts national income.
  \item[11.] \textbf{Overall Spending Sometimes Gets Out of Line with Productive Capacity:} Spending shortfalls induce recessionary output gaps and cyclical unemployment; spending excesses generate demand-pull inflation.
  \item[12.] \textbf{Government Policies Can Alter Overall Spending:} Fiscal policy (taxation $T$ and government outlays $G$) and monetary policy can stabilize cyclical downturns and prevent macroeconomic overheating.
\end{enumerate}

\section{The Macroeconomic Circular Flow Model}
The circular flow tracks real factor services and finished commodities circulating in parallel with counterbalancing monetary payments between households and business enterprises.

\subsection{Factor Markets vs. Product Markets}
\begin{itemize}
  \item \textbf{Factor Markets:} Households supply productive inputs (labor, land, capital, enterprise) to firms in exchange for factor compensation (wages, rent, interest, profit).
  \item \textbf{Product Markets:} Firms deliver finished goods and services to households in return for consumption expenditures.
\end{itemize}

\section{The Paradox of Thrift}
When households collectively attempt to raise their savings rates during an economic downturn, aggregate consumption expenditure contracts. Because spending equals income, firms cut payrolls and downsize employment. Aggregate national income falls so severely that total dollar savings across the entire economy paradoxically stagnate or decline.

\begin{examplecase}{The Macroeconomic Accounting Identity}
In a closed national economy, national accounting parity dictates that Gross Domestic Product identically equals gross factor income:
\begin{equation}
Y \equiv C + I + G = \text{Factor Payments (Wages} + \text{Rent} + \text{Interest} + \text{Profits)}
\end{equation}
In financial equilibrium, total economic Leakages ($S + T + M$) must balance total Injections ($I + G + X$).
\end{examplecase}

\section{Macroeconomic Policy Trade-Offs: Efficiency vs. Equity}
Policymakers continuously calibrate policies along the frontier connecting productive efficiency and distributional fairness. While progressive income taxes and targeted transfers reduce child poverty and enhance social cohesion, excessive marginal rates may distort labor supply and capital formation incentives.

\end{document}
"""

MACRO_CH02_TEX = r"""\documentclass[11pt,letterpaper]{article}
\input{../../shared/preamble.tex}
\input{../../shared/tikz-settings.tex}

\begin{document}

\title{\Huge\bfseries\color{SlateBlue} Chapter 2: The Macroeconomic Production Possibilities Frontier \& National Capacity}
\author{\large Principles of Macroeconomics Curriculum}
\date{2026}
\maketitle

\thispagestyle{plain}

\begin{abstract}
This chapter models the aggregate production possibilities frontier, the structural trade-off between consumer goods and capital accumulation, cyclical output gaps vs. secular economic growth, and national specialization in global trade networks, benchmarked to Paul Krugman \& Robin Wells (\textit{Macroeconomics}, ch. 2).
\end{abstract}

\tableofcontents
\vspace{1.5em}
\hrule
\vspace{1.5em}

\section{The Macroeconomic PPF and National Productive Capacity}
At the aggregate macroeconomic level, the Production Possibilities Frontier represents an entire nation's potential output capacity. Rather than comparing individual commodities, the macro PPF illustrates trade-offs between broad macroeconomic categories: Consumer Goods ($C$) versus Capital Goods ($I$), or Private Consumption versus Public Infrastructure ($G$).

\textbf{Attribution Note:} Adapts aggregate capital accumulation theory from Paul Krugman and Robin Wells, \textit{Macroeconomics} (6th ed., Worth Publishers, Chapter 2: ``Economic Models: Trade-offs and Trade'').

\section{Consumer Goods vs. Capital Goods: Current Living Standards vs. Future Growth}
A nation's operating position along its macro PPF dictates its intertemporal growth rate:
\begin{itemize}
  \item \textbf{Consumer Goods ($C$):} Manufactured for immediate utility satisfaction (e.g., retail food, residential entertainment). They do not enhance future productive capacity.
  \item \textbf{Capital Goods ($I$):} Durable physical equipment designed to manufacture other goods over extended horizons (e.g., semiconductor fabrication lines, electrical grids, transport logistics).
\end{itemize}

\begin{equation}
\text{Current Investment } (I) \implies \Delta K > 0 \implies \text{Outward Shift of Potential GDP } (Y^*)
\end{equation}

\begin{examplecase}{Empirical Case: East Asian Capital Deepening}
In the post-WWII era, emerging East Asian economies (such as South Korea and Japan) directed private and public savings into heavy industrial capital formation. By maintaining national investment shares above 30\% to 35\% of GDP, their macro PPFs expanded outward by 7\% to 9\% annually, driving multi-decade increases in real per-capita living standards.
\end{examplecase}

\section{Efficiency, Unemployment, and the Output Gap}
The macro PPF directly represents business cycle volatility:
\begin{itemize}
  \item \textbf{On the Frontier:} Full employment of national labor and physical capital ($Y = Y^*$).
  \item \textbf{Inside the Frontier:} Recessionary gap with idle machinery and cyclical unemployment ($Y < Y^*$).
  \item \textbf{Outward Shift:} Long-run economic growth resulting from capital deepening, labor force expansion, or total factor productivity (TFP) growth.
\end{itemize}

\begin{examplecase}{Recessionary Gap vs. Frontier Expansion Post-2020}
During the contractions of 2020, public health shutdowns idled factories and grounded logistics networks, dropping the economy deep inside its macro PPF (unemployment reached 14.7\%). The subsequent recovery re-employed idle resources, moving output from inside the frontier back toward the boundary. This cyclical re-utilization differed fundamentally from true outward expansions of the frontier, which were subsequently dictated by technological progress and capital deepening.
\end{examplecase}

\section{National Specialization and Global Macroeconomic Linkages}
Nations integrate into global commerce based on relative factor endowments. Economies with abundant capital equipment and research hubs develop comparative advantages in advanced technology and aerospace, whereas economies with vast labor endowments specialize in assembly or agricultural commodities. While international trade expands aggregate national consumption possibilities beyond the domestic PPF, structural shifts can create concentrated transitional dislocations for import-competing sectors.

\end{document}
"""

# =============================================================================
# 2. MARKDOWN / QUARTO SANITIZER
# =============================================================================

def tex_to_sanitized_qmd(tex_content: str, chapter_title: str) -> str:
    body = tex_content

    # Strip document wrappers
    body = re.sub(r"\\documentclass.*?\\begin\{document\}", "", body, flags=re.DOTALL)
    body = re.sub(r"\\end\{document\}", "", body)
    body = re.sub(r"\\maketitle", "", body)
    body = re.sub(r"\\tableofcontents", "", body)
    body = re.sub(r"\\thispagestyle\{.*?\}", "", body)
    body = re.sub(r"\\vspace\{.*?\}", "", body)
    body = re.sub(r"\\hrule", "", body)

    # Convert abstract to blockquote
    body = re.sub(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", r"> \1\n", body, flags=re.DOTALL)

    # Convert section headings
    body = re.sub(r"\\section\*?\{(.*?)\}", r"## \1", body)
    body = re.sub(r"\\subsection\*?\{(.*?)\}", r"### \1", body)
    body = re.sub(r"\\subsubsection\*?\{(.*?)\}", r"#### \1", body)

    # Convert custom environments to Quarto callout blocks
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

    # Clean LaTeX font and formatting macros
    body = re.sub(r"\\textbf\{(.*?)\}", r"**\1**", body)
    body = re.sub(r"\\textit\{(.*?)\}", r"*\1*", body)
    body = re.sub(r"\\text\{(.*?)\}", r"\1", body)
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
    body = re.sub(r"``(.*?)''", r'"\1"', body)

    # Remove raw tikzpicture blocks from markdown
    body = re.sub(
        r"\\begin\{figure\}.*?\\end\{figure\}",
        r"> **[Graphical Model: Marginal Benefit intersects Marginal Cost at equilibrium $(Q^*, P^*)$]**\n",
        body,
        flags=re.DOTALL
    )

    # Strip leading whitespace or unclosed dashes
    lines = [line.strip() for line in body.splitlines()]
    while lines and lines[0] in ("", "—", "-", "---", "***"):
        lines.pop(0)

    clean_body = "\n".join(lines)
    clean_body = re.sub(r"\n{3,}", "\n\n", clean_body).strip()

    # Create proper YAML front matter
    qmd_header = f'---\ntitle: "{chapter_title}"\nformat:\n  html:\n    math:\n      method: mathjax\n---\n\n'
    return qmd_header + clean_body + "\n"

# =============================================================================
# 3. SYNCHRONIZATION PIPELINE
# =============================================================================

CHAPTER_SPECS = [
    {
        "course": "micro",
        "tex_filename": "ch01_principles.tex",
        "qmd_filename": "ch01_principles.qmd",
        "title": "Chapter 1: Foundations of Microeconomic Analysis & Core Principles",
        "tex_content": MICRO_CH01_TEX,
        "tex_dir": MICRO_TEX_DIR,
        "qmd_dir": MICRO_QMD_DIR,
    },
    {
        "course": "micro",
        "tex_filename": "ch02_ppf.tex",
        "qmd_filename": "ch02_ppf.qmd",
        "title": "Chapter 2: The Production Possibilities Frontier & Gains from Trade",
        "tex_content": MICRO_CH02_TEX,
        "tex_dir": MICRO_TEX_DIR,
        "qmd_dir": MICRO_QMD_DIR,
    },
    {
        "course": "macro",
        "tex_filename": "ch01_principles.tex",
        "qmd_filename": "ch01_principles.qmd",
        "title": "Chapter 1: First Principles of Economics & Macroeconomic Systems",
        "tex_content": MACRO_CH01_TEX,
        "tex_dir": MACRO_TEX_DIR,
        "qmd_dir": MACRO_QMD_DIR,
    },
    {
        "course": "macro",
        "tex_filename": "ch02_macro_ppf.tex",
        "alias_tex": "ch02_ppf.tex",
        "qmd_filename": "ch02_macro_ppf.qmd",
        "title": "Chapter 2: The Macroeconomic Production Possibilities Frontier",
        "tex_content": MACRO_CH02_TEX,
        "tex_dir": MACRO_TEX_DIR,
        "qmd_dir": MACRO_QMD_DIR,
    },
]

MICRO_QUARTO_YML = """project:
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
"""

MACRO_QUARTO_YML = """project:
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
    - part: "Macroeconomic Foundations"
      chapters:
        - ch01_principles.qmd
        - ch02_macro_ppf.qmd

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
"""

MICRO_INDEX_QMD = """# Preface {.unnumbered}

Welcome to **Principles of Microeconomics: An Institutional and Social Science Perspective**.

This textbook offers an analytical, empirical approach to microeconomic decision-making, price theory, market structures, and policy evaluation. It is structured around the analytical depth of Eric Chiang (*Microeconomics: Principles for a Changing World*, 5th ed.) and UC Berkeley Econ 1.

Use the left sidebar navigation to explore individual chapters or press `s` to initiate full-text keyword searches across the entire volume.
"""

MACRO_INDEX_QMD = """# Preface {.unnumbered}

Welcome to **Principles of Macroeconomics: An Institutional and Social Science Perspective**.

This textbook offers an analytical, empirical approach to macroeconomic systems, national accounting, business cycles, monetary mechanisms, and fiscal policy. It is structured around the analytical depth of Paul Krugman and Robin Wells (*Macroeconomics*, 6th ed.) and UC Berkeley Econ 2.

Use the left sidebar navigation to explore individual chapters or press `s` to initiate full-text keyword searches across the entire volume.
"""

def run_sync():
    print("=" * 65)
    print("Principles of Economics: Restoring Core Readings & Web Books")
    print("=" * 65)

    MICRO_TEX_DIR.mkdir(parents=True, exist_ok=True)
    MACRO_TEX_DIR.mkdir(parents=True, exist_ok=True)
    MICRO_QMD_DIR.mkdir(parents=True, exist_ok=True)
    MACRO_QMD_DIR.mkdir(parents=True, exist_ok=True)

    # Write configs
    (MICRO_QMD_DIR / "_quarto.yml").write_text(MICRO_QUARTO_YML, encoding="utf-8")
    (MICRO_QMD_DIR / "index.qmd").write_text(MICRO_INDEX_QMD, encoding="utf-8")
    (MACRO_QMD_DIR / "_quarto.yml").write_text(MACRO_QUARTO_YML, encoding="utf-8")
    (MACRO_QMD_DIR / "index.qmd").write_text(MACRO_INDEX_QMD, encoding="utf-8")

    for spec in CHAPTER_SPECS:
        # Write .tex chapter
        tex_path = spec["tex_dir"] / spec["tex_filename"]
        tex_path.write_text(spec["tex_content"], encoding="utf-8")
        print(f"[OK] Restored LaTeX Source: {tex_path.relative_to(ROOT)}")

        if "alias_tex" in spec:
            alias_path = spec["tex_dir"] / spec["alias_tex"]
            alias_path.write_text(spec["tex_content"], encoding="utf-8")
            print(f"[OK] Restored LaTeX Alias:  {alias_path.relative_to(ROOT)}")

        # Write sanitized Quarto .qmd chapter
        qmd_content = tex_to_sanitized_qmd(spec["tex_content"], spec["title"])
        qmd_path = spec["qmd_dir"] / spec["qmd_filename"]
        qmd_path.write_text(qmd_content, encoding="utf-8")
        print(f"[OK] Generated Quarto Web:  {qmd_path.relative_to(ROOT)}")

    print("\n" + "=" * 65)
    print("All chapters synchronized cleanly with 100% valid UTF-8 encoding.")
    print("=" * 65)

if __name__ == "__main__":
    run_sync()
