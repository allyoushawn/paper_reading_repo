# Paper Analysis: A Graphical Point Process Framework for Understanding Removal Effects in Multi-Touch Attribution

**Source:** https://arxiv.org/pdf/2302.06075.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** A Graphical Point Process Framework for Understanding Removal Effects in Multi-Touch Attribution  
**Authors:** Tao, Wang et al.  
**Abstract:**
This paper proposes a graphical point process model for multi-touch attribution that simultaneously captures both direct conversion effects and dynamic Granger causality relations (exciting effects) between touchpoint types. The key insight is that existing models aggregate touchpoints at the channel level and ignore inter-channel spillover/carryover effects (e.g., a display impression causing a subsequent search click). The paper introduces two path-level attribution methods — Direct Removal Effect (DRE) and Total Removal Effect (TRE) — and an ADMM-based estimation algorithm.

**Key contributions:**
- Graphical point process model: multivariate temporal point process with Granger causality graph representing exciting effects between touchpoint types
- Direct Removal Effect (DRE): relative change in conversion intensity when only the event of interest is removed, assuming other touchpoints are unaffected (focuses on direct parent nodes of conversion)
- Total Removal Effect (TRE): full removal effect accounting for downstream touchpoints that would have been prevented by removing an early touchpoint (backpropagation through reverse Granger graph)
- ADMM estimation algorithm with L1 sparsity for simultaneous edge selection and parameter estimation
- Asymptotic theory for parameter estimates (theoretical guarantee)
- Real-world application: 2.8M paths, 74k conversions, Fortune 500 company

**Methodology:**
Conditional intensity: λe(t|Ht) = μe + Σe' αe'e ∫ψe'e(t−u) dNe'(u). Customer-initiated events (clicks, conversions) modeled with full intensity; firm-initiated events (impressions) treated as observed inputs. Attribution = removal effect: DRE computes direct parent contribution; TRE flows attribution scores backward through Granger causality graph via backpropagation algorithm. ADMM solves regularized least-squares with L1 penalty for sparse edge selection.

**Main results:**
Hawkes simulation (10k paths, 2 channels): TRE KL divergence 0.0002, Hellinger 0.0064 (vs DRE KL 0.0023). DASS+ simulation (98k paths, 4 channels, 9 touchpoint types): TRE KL 0.008 vs DRE 0.011 vs DNAMTA 0.012 vs Logistic 0.024 vs Markov 0.093. Rule-based methods severely underestimate search channel. Real Fortune 500 data: TRE gives display 14.2% vs DRE 10.7% (captures display→search exciting effect).

---

## 2. Experiment Critique

**Design:**
Three datasets: Hawkes simulation (ground truth known), DASS+ simulation (Google's advertising simulator), and real Fortune 500 data. 8 comparison methods including DNAMTA, Logistic, Markov, and 5 rule-based heuristics. The DASS+ simulation from Google is a well-accepted industry benchmark.

**Statistical validity:**
Strong on simulations — theoretical guarantees plus empirical validation with 100 independent runs (Hawkes) and 10 runs (DASS+). The identified limitation (TRE subadditivity) is honestly presented and mathematically justified. DRE systematically underestimates early-stage channels — honest negative result.

**Online experiments (if any):**
N/A — offline evaluation.

**Reproducibility:**
Code and data not stated as available. Fortune 500 dataset proprietary. DASS+ simulation can be reproduced independently. Hawkes simulation fully described.

**Overall:**
Strong methodological paper with theoretical guarantees. The graphical approach captures inter-channel dynamics that all prior MTA methods miss. The TRE subadditivity limitation is a genuine constraint for interpretation. This is the most sophisticated treatment of touchpoint interaction effects in the survey.

---

## 3. Industry Contribution

**Deployability:**
Moderate. The ADMM estimation and TRE backpropagation are more complex than LSTM-based models. The Fortune 500 real-world application validates deployability. The ability to learn a sparse Granger causality graph is directly useful for understanding interaction networks.

**Problems solved:**
For dating platform attribution: the Granger causality graph captures the most important dynamic in dating platform interaction sequences — early touchpoints (profile views, likes) cause later touchpoints (messages, matches). TRE correctly attributes credit to early interactions that trigger the downstream engagement chain leading to retention, which DRE and all LSTM-based methods miss.

**Engineering cost:**
High. Multivariate point process estimation with ADMM is more complex than LSTM-based methods. The backpropagation algorithm for TRE requires careful implementation. Computational cost scales with number of touchpoint types and path length.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
First MTA framework to model full Granger causality structure among multiple touchpoint types; first to distinguish DRE (direct effects only) from TRE (full causal chain effects); first to provide a backpropagation algorithm for path-level TRE computation.

**Prior work comparison:**
DNAMTA (2018): channel-level only, ignores inter-channel exciting effects; Xu et al. (2014): Bayesian Poisson process but no Granger causality graph or path-level attribution; Markov model (Anderl 2016): discrete states, ignores timestamps. Graphical MTA is the most general model for touchpoint interaction effects in the survey.

**Verification:**
Claims verified on simulations with known ground truth. The TRE outperformance over DNAMTA (KL 0.008 vs 0.012) on DASS+ is meaningful. Real data results are directionally plausible.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Hawkes Simulation | Fully described | Yes | 10k paths, 2 channels, 4 touchpoint types |
| DASS+ Simulation | Modified version of Google DASS | Partially (DASS base available) | 98,986 paths, 4 channels, 9 touchpoint types |
| Fortune 500 Real Data | Not public | No | 2.8M paths, 74k conversions |

**Offline experiment reproducibility:**
Partially reproducible — simulations reproducible; real data not available.

---

## 6. Community Reaction

arXiv 2023. ~30 citations. Novel approach — the first graphical point process MTA paper in the survey. Limited by complexity barrier for industry adoption. The Granger causality insight (display impressions cause search clicks) is a valuable contribution to the MTA literature.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Tao, Wang et al.  
**Affiliations:** Not specified in source  
**Venue:** arXiv 2023  
**Year:** 2023  
**PDF:** https://arxiv.org/pdf/2302.06075.pdf  
**Relevance:** Core  
**Priority:** 3
