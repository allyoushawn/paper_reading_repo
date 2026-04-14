# Paper Analysis: Causal-Driven Attribution: Channel Influence from Aggregate Data

**Source:** https://arxiv.org/pdf/2512.21211.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Causal-Driven Attribution: Channel Influence from Aggregate Data  
**Authors:** Iason Filippou, Ioannis Tsamardinos (University of Crete)  
**Abstract:** Privacy and aggregation break user-level path reconstruction. Proposes **Causal-Driven Attribution (CDA)**: (1) PCMCI+ on multivariate time series of channel-level impressions and outcomes to learn a causal graph; (2) encode the graph as a structural causal model (SCM); (3) estimate per-channel causal effects (CATE/ACE) via do-interventions and counterfactuals on the SCM. Evaluated on synthetic SCM data and a real aggregated marketing mix dataset.

**Key contributions:**
- Pipeline bridging constraint-based discovery + SCM-based effect estimation under aggregation.
- Empirical gains vs baselines (e.g., Shapley regression, Granger) on synthetic and real tasks.

**Methodology:** PCMCI+ for temporal conditional independence testing; linear/nonlinear SCM variants; interventional queries for channel uplift.

**Main results:** CDA tracks ground-truth channel influences in simulation; on real aggregated data, reported improvements over attribution baselines per paper tables.

---

## 2. Experiment Critique

**Design:** Synthetic known SCM plus one aggregated real case study.

**Statistical validity:** Depends on stationarity, sufficient history, and correctness of discovery assumptions; aggregation removes path granularity.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Methods are standard open libraries (PCMCI family); raw proprietary logs not released.

**Overall:** Strong for **macro channel incrementality** when only aggregates exist; weak for per-user touch sequences as training labels.

---

## 3. Industry Contribution

**Deployability:** Moderate for MMM-style stacks with daily/weekly channel series.

**Problems solved:** Causal channel weights without user-level joins.

**Engineering cost:** Time-series QA, lag selection, and SCM misspecification risk.

---

## 4. Novelty vs. Prior Work

Contrasts with Shapley regression on tabular mixes, Granger-only attribution, and classical MMM without explicit SCM layer.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic SCM | Generated | Partial | Specs in paper |
| Aggregated marketing mix | Proprietary / bundled | Partial | As cited |

---

## 6. Community Reaction

Not specified in source.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Iason Filippou, Ioannis Tsamardinos  
**Affiliations:** University of Crete  
**Venue:** arXiv (cs.LG / stat.ML)  
**Year:** 2025  
**PDF:** https://arxiv.org/pdf/2512.21211.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(a) Per-touchpoint fractional credit:** No—operates on **channel-level** series; no touch-level label vector for supervised path models.

**(b) Continuous outcomes:** Supported if the outcome series is continuous in the SCM.

**(c) Selection / heterogeneous paths:** User heterogeneity collapsed by aggregation; selection discussion not specified in source.

**(d) Incrementality:** Yes at channel level via do-calculus / counterfactuals on the learned SCM.
