# Paper Analysis: Design and Analysis of Switchback Experiments

**Source:** https://arxiv.org/pdf/2009.00148.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Design and Analysis of Switchback Experiments  
**Authors:** Iavor Bojinov, David Simchi-Levi, Jinglong Zhao  
**Abstract:**  
Switchback experiments alternate a binary treatment over time on one or a few aggregated units (common in ride-hailing and marketplaces). The paper casts design under unknown carryover length as a minimax discrete optimization problem, derives optimal randomization timing and fair-coin assignment probabilities, and gives exact randomization-based tests plus a conservative finite-population CLT for inference. A data-driven procedure is proposed to identify carryover order.

**Key contributions:**
- Optimal switchback designs minimizing worst-case risk (variance) over bounded potential outcomes, jointly in randomization points and assignment probabilities.
- Estimation via Horvitz–Thompson for lag-$p$ causal effects; inference under correct or misspecified carryover length.
- Simulations showing lower worst-case and predictive risk and competitive Type I/II behavior versus naive dense randomization and an epoch-based heuristic.

**Methodology:**  
Potential-outcomes framework with $m$-carryover; minimax objective over adversarial outcomes; structural results (fair coin $q_k=1/2$; randomize every $m$ periods when $T$ aligns); Section 6 practical guidance on period length, horizon, and carryover detection.

**Main results:**  
Theoretical optimality of $p=1/2$ assignment (Theorem 1) and randomization every $m$ periods under divisibility (Theorem 2). Simulations at $T=120$, $m=2$: optimal worst-case risk $26.78$ vs naive $33.67$ and intuitive heuristic $27.85$; predictive risk table entries such as $7.96$ vs $10.22$ vs $8.11$ for one $(\delta^{(1)},\delta^{(2)},\delta^{(3)})$ row.

---

## 2. Experiment Critique

**Design:**  
Extensive simulations under linear additive carryover (Eq. 13) and heavy-tailed Student’s $t$ noise; comparison to two heuristic designs (dense randomization H1; epoch length $m{+}1$ as H2). Strengths: design-based, nonparametric robustness. Limitations: large variance when $m$ is comparable to $T$; no adaptive assignment probabilities; estimand fixed to average lag-$p$ “persistent policy” effect.

**Statistical validity:**  
Exact tests for sharp nulls; asymptotic tests using finite-population CLT; CIs via test inversion (noted as computationally intensive for exact path). Type I rates near nominal $0.05$; optimal design lowest Type II in reported figures.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
Not specified in source.

**Overall:**  
Theory and simulations support claims about risk and inference under stated assumptions; limitations are explicitly listed in the paper.

---

## 3. Industry Contribution

**Deployability:**  
Section 6 operational guidance (granularity vs carryover, horizon choice via rejection-rate curves, multi-unit replication) supports adoption where switchbacks are already used (network interference or few units).

**Problems solved:**  
Reduces variance and clarifies inference for switchbacks under carryover—relevant to marketplace/geo and time-aggregated experimentation—not to user-level multi-touch credit assignment.

**Engineering cost:**  
Not specified in source.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
First systematic optimal-design treatment for switchbacks under carryover with finite-sample and asymptotic inference and carryover-order identification.

**Prior work comparison:**  
Not specified in source (NotebookLM batch; no independent novelty web search).

**Verification:**  
Not specified in source.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| — | — | — | Simulation-based; no empirical dataset release described in reviewed excerpts |

**Offline experiment reproducibility:**  
Not specified in source.

---

## 6. Community Reaction

Not searched in this batch (NotebookLM-only ingestion).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Iavor Bojinov; David Simchi-Levi; Jinglong Zhao  
**Affiliations:** Harvard Business School; MIT IDSS / CEE / ORC; Boston University Questrom  
**Venue:** arXiv  
**Year:** 2020  
**PDF:** downloaded (arXiv)  
**Relevance:** Related  
**Priority:** 3

---

## NotebookLM — Project alignment (requirements.md §Project Context)

1. **Per-interaction fractional credit on multi-touch paths:** No — paper targets time-series average/total causal effects of a single binary treatment, not credit across heterogeneous user interactions.  
2. **Continuous outcomes as supervised training labels:** Not specified in source.  
3. **Heterogeneous touch types / selection:** No — binary treatment path; non-anticipating outcomes under experimenter-controlled assignment (not user self-selection into interaction types).
