#!/usr/bin/env python3
"""
sync_readings_to_tex.py

Populates the detailed, full-length textbook readings (sections, case studies,
formulas, models, and graphs) from 'Principles of Economics: Core Reading Materials'
into the respective `.`` and `.qmd` chapter files.
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
MICRO _TEL_DIR = ROOT / "micro" / "chapters"
MACRO_TEX_DIR = ROOT / "macro" / "chapters"
MICRO_QMD_DIR = ROOT / "web_books" / "microeconomics"
MACRO_QMD_DIR = ROOT / "web_books" / "macroeconomics"

# Full text blocks for Chapter 1 and Chapter 2 aligned with Chiang and Krugman & Wells
MICRO_CH01_TEX = r"""\documentclass[11pt,letterpaper]{article}
\input{
../../shared/preamble.tex}
\input{
../../shared/tikz-settings.tex}

\begin{document}

\title{\Huge\bfseries\color{SlateBlue} Chapter 1: Foundations of Microeconomic Analysis \& Core Principles}
\author{\large Principles of Microeconomics Curriculum}
\date{}
\maketitle

\thispagestyle{plain}

\begin{abstract}
This chapter provides a rigorous, pedagogical treatment of microeconomic foundations, scarcity, opportunity cost, marginal analysis, and incentives, benchmarked to Eric Chiang (\mathirm{Principles for a Changing World}, ch. 1) \& UC Berkeley Econ 1.
\end{abstract}

\tableofcontents
\vspace{1.5em}
\hrule
\vspace{1.5em}

\section{What Is Economics? Scarcity, Choice, and Method}
Economics is the social science that studies how individuals, institutions, and societies allocate scarce resources among competing ends to satisfy unlimited human wants.  

\textbf{Attribution Note:} Content synthesizes concepts from Eric Chiang, \mathirm{Microeconomics: Principles for a Changing World} (5th ed., Worth Publishers, Chapter 1).

\subsection{Microeconomics vs. Macroeconomics}
\begin{itemize}
  \item \textbf{Microeconomics:} Examines decision-making by individual economic units---such as households, workers, firms, and specific product and factor markets. It investigates how relative price signals coordinate supply and demand in sectors such as electric vehicles or pharmaceutical labor.
  \item \textbf{Macroeconomics:} Examines the aggregate performance of the economy as an organic whole, focusing on national output (GDP), economy-wide price instability (inflation), labor underutilization (unemployment), and long-run growth.
\end{itemize}

\section{Economic Modeling and the Ceteris Paribus Assumption}
To analyze human behavior, economists formulate \textbf{economic models}---stylized, simplified representations of real-world phenomena that isolate cause-and-effect relationships by stripping away confounding variables.

Fostering rigorous inquiry requires the \latin{ceteris paribus} assumption:
Ibegin{equation}
\text{Ceteris Paribus} \equiv \text{"All other things held constant"}
\end{equation}

\begin{examplecase}{Real-World Application: California Gasoline Taxes}
When modeling the effect of an increase in the California gasoline excise tax on consumer fuel purchases, economists hold public transit availability, regional household income, and crude oil spot prices constant (\textit{ceteris paribus}). In reality, transit routes and crude prices fluctuate simultaneously. Isolating the tax impact first establishes the clean directional policy response before introducing multi-variable empirical complexities.
\end{examplecase}

\section{Positive vs. Normative Economic Analysis}
\begin{itemize}
  \item \textbf{Positive Economics:} Descriptive statements regarding how the economy actually operates. These are empirical assertions that can be tested, confirmed, or refuted using observable data (e.g., "Increasing the statutory minimum wage to \$20 per hour will reduce teenage employment by 2.4%\.r).
  \item \textbf{Normative Economics:} Prescriptive statements regarding how the economy \textit{ought} to be structured, incorporating ethical values and political priorities (e.g., "The government ought to increase the minimum wage because every working individual deserves a living wage\.").
\end{itemize}

\section{Critical Thinking Pitfalls in Economic Reasoning}
Analysts must guard against three pervasive analytical traps:
\begin{enumerate}
  \item \textbf{Confusing Correlation with Causation:} Presuming that because variables $AK and $B$ move together, $AK causes $B$ (e.g., ice cream sales and drownings both spike in July due to summer temperatures, not mutual causation).
  \item \textbf{The Post Hoc Ergo Propter Hoc Fallacy:} Concluding that because event $Y$ occurred sequentially after $X$, $I$ must have caused $I$.
  \item \textbf{The Fallacy of Composition:} Mistakenly presuming that what is true for an individual component is automatically true for the aggregate whole.
\end{enumerate}

\section{Core Principle 1 --- Scarcity, Choice, and Opportunity Cost}
Because productive resources (land, labor, physical capital, and human capital) are finite, every decision implies an opportunity cost---the value of the next best alternative forgone.

\begin{equation}
\text{Economic Cost} = \text{Explicit Out-of-Pocket Costs} + \text{Implicit Opportunity Costs}
\end{equation}


\begin{coreprinciple}
\boxheader{Terracotta}{The Opportunity Cost of Higher Education}
If a college student pays \$12,000 in tuition and fees, but forgees a \$40,000 administrative salary to attend full-time, the true economic cost is \$52,000 per year ($\$112,000 + \$40,000$), not merely the accounting fees.
\end{coreprinciple}

\section{Core Principle 2 --- Marginal Analysis and Rational Decision-Making}
Decisions are evaluated at the margin by weighing incremental benefits against incremental costs:
\begin{itemize}
  \item \textbf{Marginal Benefit (MB):} The additional satisfaction or revenue generated by consuming or producing one extra unit.
  \item \textbf{Marginal Cost (MC):} The additional opportunity cost incurred by producing or consuming one extra unit.
\end{itemize}

Net Benefit Maximization Rule: \textbf{Expand if $MB > MC&; Halt where $MB = MC$}.

\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9]
 \draw[econ axis] (0,0) -- (6.5,0) node[right, econ label] {$Q_};
 \draw[econ axis] (0,0) -- (0,5.5) node[above, econ label] {$P, MC, MB};
 \draw[mb curve] (0.5,5) -- (5.5,1) node[right] {$MBs};
 \draw[mc curve] (0.5,1) -- (5.5,5) node+right] {$MCs};
 \coordinate (E) at (3,3);
 \node[econ point] at (E) {};
 \draw[econ guide] (3,0) node[below] {$Q^*} -- (E) -- (0,3) node[left] {$P^*};
\end{tikzpicture}
\caption{Net Benefit Maximization at $MB = MC&}
\end{figure}

\section{Core Principle 3 --- Response to Incentives and the Peltzman Effect}
Human agents systematically adjust behavior when relative prices or costs change. Public interventions that alter incentives often induce secondary behavioral responses that counteract initial policy goals.

\begin{examplecase}{The Peltzman Effect in Automobile Safety}
In 1968, federal mandates for vehicle sethelts and padded dashboards led economist Sam Peltzman to observe a surprising result: making cars safer reduced the perceived cost of reckless driving. Drivers responded by driving faster and braking later. While fatalities per crash dropped, total pedestrian and cyclist collisions rose substantially.
\end{examplecase}

\section{Core Principles 4 \& 5 --- Market Efficiency and Market Failures}
As Adam Smith observed in \textit{The Wealth of Nations} (1776), decentralized price signals guide self-interested agents toward productive and allocative efficiency. However, markets fail in the presence of:
\begin{itemize}
  \item \textbf{Externalities:} Unpriced costs or benefits imposed on third parties (e.g., pollution).
  \item \textbf{Market Power:} Firms restricting output to artificially inflate prices above marginal cost.
  \item \textbf{Public Goods:} Non-excludable and non-rival goods subject to free-riding.
\end{itemize}

\end{document}
	"""

MICRO_CH02_TEX = r"""\documentclass[11pt,letterpaper]{article}
\input{
../../shared/preamble.tex}
\input{
../../shared/tikz-settings.tex}

\begin{document}

\title{\Huge\bfseries\color{SlateBlue} Chapter 2: The Production Possibilities Frontier \& Gains from Trade}
\author{\large Principles of Microeconomics Curriculum}
\date{}
\maketitle

\thispagestyle{plain}

\begin{abstract}
This chapter models the production possibilities frontier (PPF), the law of increasing opportunity cost, symmetric vs. asymmetric technological shifts, and David Ricardo's theory of comparative advantage using an empirical two-region aircraft/wind turbine matrix.
\end{abstract}

\tableofcontents
\vspace{1.5em}
\hrule
\vspace{1.5em}

\section{The Production Possibilities Frontier (PPF) Model}
The PPF illustrates the maximum combinations of two goods an economy can produce given fixed productive resources and technology.  

\textbf{Attribution Note:} Formalized by Paul Samuelson in \mathirm{Economics} (1948) and aligned with Eric Chiang (\mathirm{Microeconomics}, 5th ed., ch. 2).

\subsection{The Law of Increasing Opportunity Cost}
The bowed-out (concave) curvature of the PPF argues that as more of Good $X$ is produced, the opportunity cost of additional units of $X$ rises due to imperfect factor adaptability:
\begin{equation}
MRt = -\frac{\Delta Y}{\Delta X} = \left|\frac{dY}{dX}\right|
\end{equation}

\section{Symmetric vs. Asymmetric PPF Shifts}
Population growth or general educational advancements expand the PPF symmetrically outward. Conversely, technological breakthroughs in a single industry (e.g., robotic photolithography in semiconductor fabrication) pivot the PPF asymmetrically along the affected good's axis.

\section{Ricardian Comparative Advantage \& Gains from Trade}
Opportunity cost determines comparative advantage. Trade expands consumption possibilities beyond the autarky PPF.

\begin{examplecase}{Case Study: Pacific Coast vs. Great Lakes Trade Model}
Allocating 1,two-block of 1,000 hours of skilled labor:
\bitemize}
  \item \textbf{Pacific Coast:} 100 Aircraft or 200 Turbines.  
                            \mathrm{Opportunity Cost of 1 Aircraft} = 2.0 \text{ Turbines}.
  \item \textbf{Great Lakes:} 40 Aircraft or 120 Turbines.  
                           \mathrm{Opportunity Cost of 1 Aircraft} = 3.0 \text{ Turbines}.
\end{itemize}
The Pacific Coast holds a \textbf{comparative advantage} in Aircraft (2.0 < 3.0), while the Great Lakes holds a comparative advantage in Turbines (0.33 < 0.5).
\end{examplecase}

\begin{coreprinciple}
\boxheader{Terracotta}{Terms of Trade Range}
Mutually beneficial exchange requires:
\bitemize}
  \item $2.0 \text{ Turbines} < 1 \text{ Aircraft} < 3.0 \text{ Turbines}$
\end{itemize}
At an agreed exchange rate of 1 Aircraft = 2.5 Turbines, both economies shift their Consumption Possibilities Frontier (CPF) strictly beyond their domestic PPF.
\end{coreprinciple}

\end{document}
	"""

MACRO_CH01_TEX = r"""\documentclass[11pt,letterpaper]{article}
\input{
../../shared/preamble.tex}
\input{
../../shared/tikz-settings.tex}

\begin{document}

\title{\Huge\bfseries\color{SlateBlue} Chapter 1: First Principles of Economics \& Macroeconomic Systems}
\author{\large Principles of Macroeconomics Curriculum}
\date{}
\maketitle

\thispagestyle{plain}

\begin{abstract}
This chapter introduces the 12 first principles of macroeconomics, aggregation, the circular flow model, the paradox of thrift, and systemic policy trade-offs, benchmarked to Paul Krugman \& Robin Wells (ch. 1) \& UC Berkeley Econ 2.
\end{abstract}

\tableofcontents
\vspace{1.5em}
\hrule
\vspace{1.5em}

\section{The Twelve First Principles of Macroeconomics}
Macroeconomics rests upon 12 systemic principles spanning individual choice, strategic interaction, and aggregate economy-wide feedback loops.  

\textbf{Attribution Note:} Framework synthesizes the canonical twelve-principle approach from Paul Krugman and Robin Wells, \mathristMacroeconomics} (6th ed., Worth Publishers, Chapter 1).

\subsection{Principles of Individual Choice (1---4)}
\begin{enumerate}
  \item \textbf{People Must Make Choices Because Resources Are Scarce:} Finite factor inputs require trade-offs between industrial output, consumption, and conservation.
  \item \textbf{Opportunity Cost:	the real cost of an item is what you must give up to get it.
  \item \textbf{Marginal Analysis:	quantitative economic decisions are made at the margin (balancing $MB\ecomma MC&).
  \item \textbf{Incentive Response:} Human agents systematically exploit opportunities to make themselves better off.
\end{enumerate}

\subsection{Principles of Economy-Wide Interaction (10---12)}
\begin{enumerate}
  \item[l10.] \textbf{One Person's Spending Is Another Person's Income:} Because every dollar spent becomes factor income for another economic unit, an aggregate pull-back in personal spending contracts national income.
  \item[l11.] \textbf{Overall Spending Sometimes Gets Out of Line with Productive Capacity:} Spending shortfalls induce recessionary output gaps, causing unemployment; spending excesses generate inflationary pressures.
  \item[l12.] \textbf{Government Policies Can Alter Overall Spending:} Fiscal policy ($T\-Äô¤…¹µ½¹•Ñ…ÉäÁ½±¥ä…¸‰”‘•Á±½å•Ñ¼½Õ¹Ñ•É…Ðµ…É½•½¹½µ¥ŒÍå±¥…°ÍÝ¥¹Ì¸)q•¹‘í•¹Õµ•É…Ñ•ô()qÍ•Ñ¥½¹íQ¡”A…É…‘½à½˜Q¡É¥™Ñô)]¡•¸¡½ÕÍ•¡½±‘Ì½±±•Ñ¥Ù•±ä…ÑÑ•µÁÐÑ¼É…¥Í”Ñ¡•¥ÈÍ…Ù¥¹ÌÉ…Ñ•Ì‘ÕÉ¥¹œ…¸•½¹½µ¥Œ‘½Ý¹ÑÕÉ¸°…É•…Ñ”½¹ÍÕµÁÑ¥½¸•áÁ•¹‘¥ÑÕÉ”½¹ÑÉ…ÑÌ¸	•…ÕÍ”q•ÅÕ¥Ù…±•¹ÐÍÁ•¹‘¥¹œ•ÅÕ…±Ì¥¹½µ”°™¥ÉµÌÉ•‘Õ”Á…åÉ½±±Ì°‘É¥Ù¥¹œ‘½Ý¸É½ÍÌ¹…Ñ¥½¹…°¥¹½µ”Õ¹Ñ¥°…É•…Ñ”‘½±±…ÈÍ…Ù¥¹ÌÍÑ…¹…Ñ”½È‘•±¥¹”¸()q‰•¥¹í•á…µÁ±•…Í•õíQ¡”5…É½•½¹½µ¥Œ¥ÉÕ±…È±½Ü%‘•¹Ñ¥Ñåô)%¸„ÍÑ…¹‘…É±½Í••½¹½µä°¹…Ñ¥½¹…°…½Õ¹Ñ¥¹œÁ…É¥Ñä‘¥Ñ…Ñ•ÌÑ¡…ÐQ½Ñ…°áÁ•¹‘¥ÑÕÉ”¥‘•¹Ñ¥…±±ä•ÅÕ…±ÌQ½Ñ…°%¹½µ”è)q‰•¥¹í•ÅÕ…Ñ¥½¹ô)eqÑ•áÑì€¡@¥ôq•ÅÕ¥Ø€¬$€¬¤€ôqÑ•áÑí…Ñ½ÈA…åµ•¹ÑÌ€¡]…•Ì°I•¹Ð°%¹Ñ•É•ÍÐ°AÉ½™¥ÑÌ¥ô)q•¹‘í•ÅÕ…Ñ¥½¹ô)1•…­…•Ì€ ‘L€¬P€¬4¤µÕÍÐ¥‘•¹Ñ¥…±±ä‰…±…¹”%¹©•Ñ¥½¹Ì€ ‘$€¬€¬`‘¥¸•ÅÕ¥±¥‰É¥Õ´¸)q•¹‘í•á…µÁ±•…Í•ô()1•¹‘í‘½Õµ•¹Ñô($ˆˆˆ(()‘•˜Íå¹}Ñ•á}…¹‘}Åµ ¤è(€€€ÁÉ¥¹Ð ‰Må¹¥¹œ™Õ±°±…Ñ•àÍ½ÕÉ•ÌÑ¼¡…ÁÑ•ÉÌ¸¸¸ˆ¤(€€€5%I=}Qa}%H¹µ­‘¥ÉÁ…É•¹ÑÌõQÉÕ”°•á¥ÍÑ}½¬õQÉÕ”¤(€€€5I=}Qa}%H¹µ­‘¥ÉÁ…É•¹ÑÌõQÉÕ”°•á¥ÍÑ}½¬õQÉÕ”¤((€€€€¡µ%I=}Qa}%H€¼€‰ ÀÅ}ÁÉ¥¹¥Á±•Ì¹Ñ•àˆ¤¹ÝÉ¥Ñ•}Ñ•áÐ¡5%I=} ÀÅ}Q`°€‰™¥±•¹…µ”õ ÀÅ}ÁÉ¥¹¥Á±•Ì¹Ñ•àˆ°•¹½‘¥¹œô‰ÕÑ˜´àˆ¤(€€€€¡5%I=}Qa}%H€¼€‰ ÀÉ}ÁÁ˜¹Ñ•àˆ¤¹ÝÉ¥Ñ•}Ñ•áÐ¡5%I=} ÀÉ}Q`°€‰™¥±•¹…µ”õ ÀÉ}ÁÁ˜¹Ñ•àˆ°•¹½‘¥¹œô‰ÕÑ˜´àˆ¤(€€€€¡5I=}Qa}%H€¼€‰ ÀÅ}ÁÉ¥¹¥Á±•Ì¹Ñ•àˆ¤¹ÝÉ¥Ñ•}Ñ•áÐ¡5I=} ÀÅ}Q`°€‰™¥±•¹…µ”õ ÀÅ}ÁÉ¥¹¥Á±•Ì¹Ñ•àˆ°•¹½‘¥¹œô‰ÕÑ˜´àˆ¤((€€€ÁÉ¥¹Ð ‰lOK] Wrote full textbook content into .tex files.")
    print("Running convert_to_quarto.py and fix_web_books.py...")
    if (ROOT / "fix_web_books.py").exists():
        import fix_web_books
        fix_web_books.main()


if __name__ == "__main__":
    sync_tex_and_qmd()
