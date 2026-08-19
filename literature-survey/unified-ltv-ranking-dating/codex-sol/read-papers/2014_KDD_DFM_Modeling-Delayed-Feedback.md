# Paper Analysis: Modeling Delayed Feedback in Display Advertising

**Source:** https://doi.org/10.1145/2623330.2623634  
**Source ID:** 4eb91866-7a34-46eb-98ae-42405788f46c  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Author:** Olivier Chapelle  
**Abstract:** DFM jointly fits conversion probability and a conditional exponential delay distribution using positive events and right-censored nonconversions. Recent unlabeled clicks contribute little as negatives until elapsed time exceeds their predicted delay.

**Main results:** On Criteo traffic, DFM improved NLL nearly 3% over naive training and approached an oracle; naive predictions underpredicted conversion 21%. DFM reacted to a new simulated campaign within about two days despite four-day mean delay.

---

## 2. Experiment Critique

**Design:** Toy recovery study, empirical delay fit, seven test days with rolling three-week/≈6M-example training sets, recent-campaign slice, and several heuristics.

**Statistical validity:** Calibration/NLL is appropriate for bidding; uncertainty is shown for toy simulations but not the real-data headline table.

**Online experiments:** None.

**Reproducibility:** Criteo dataset link and objective are provided; L-BFGS implementation is straightforward.

**Overall:** Foundational and interpretable, but the exponential hazard underfits short/long mixture behavior and joint objective is non-convex.

---

## 3. Industry Contribution

**Deployability:** Simple two-head generalized linear model.

**Project relevance:** Core survival-model framing for weeks-long retention/payment labels and censoring at training cutoff.

**Most important mismatch:** Assumes a conventional eventual event versus no event, not successful-exit competing risks, reciprocity, interference, causal effect, or heterogeneous revenue.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** Joint conversion and conditional delay model for positive/unlabeled ad data without a fixed matching window.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Criteo conversion logs | Yes | Public dataset cited by paper. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2018_arXiv_NoDeF_Nonparametric-Delayed-CVR.md](./2018_arXiv_NoDeF_Nonparametric-Delayed-CVR.md) | Introduction / Summary | Explicitly mentions DFM in baseline or comparison context. |
| [2020_IJCAI_TS-DL_Attention-CVR-Post-Click-Calibration.md](./2020_IJCAI_TS-DL_Attention-CVR-Post-Click-Calibration.md) | Introduction / Summary | Explicitly mentions DFM in baseline or comparison context. |
| [2021_AAAI_ESDFM_Elapsed-Time-Sampling-Delayed-Feedback.md](./2021_AAAI_ESDFM_Elapsed-Time-Sampling-Delayed-Feedback.md) | Introduction / Summary | Explicitly mentions DFM in baseline or comparison context. |
| [2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md](./2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md) | Experiments | Explicitly mentions DFM in baseline or comparison context. |
| [2021_SIGIR_CBDF_Counterfactual-Delayed-Streaming.md](./2021_SIGIR_CBDF_Counterfactual-Delayed-Streaming.md) | Introduction / Summary | Explicitly mentions DFM in baseline or comparison context. |
| [2021_arXiv_DelayBuckets_Handling-Many-Conversions-Per-Click.md](./2021_arXiv_DelayBuckets_Handling-Many-Conversions-Per-Click.md) | Related Work | Explicitly mentions DFM in baseline or comparison context. |
| [2022_WWW_DEFUSE_Delayed-Feedback-Label-Correction.md](./2022_WWW_DEFUSE_Delayed-Feedback-Label-Correction.md) | Introduction / Summary | Explicitly mentions DFM in baseline or comparison context. |
| [2026_AAAI_IF-DFM_Delayed-Feedback-Influence-Functions.md](./2026_AAAI_IF-DFM_Delayed-Feedback-Influence-Functions.md) | Introduction / Summary | Explicitly mentions DFM in baseline or comparison context. |

---

## Meta Information

**Affiliations:** Criteo  
**Venue:** KDD  
**Year:** 2014  
**Relevance:** Core foundational exception  
**Priority:** 1  
**Direction:** D7 — delayed feedback / censored labels
