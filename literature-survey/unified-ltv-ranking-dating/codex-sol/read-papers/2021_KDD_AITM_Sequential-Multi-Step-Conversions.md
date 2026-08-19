# Paper Analysis: Modeling Sequential Dependence among Audience Multi-step Conversions with Multi-task Learning

**Source:** https://doi.org/10.1145/3447548.3467071  
**Source ID:** 876bc6f2-0112-448e-8fac-ae78057dc1f0  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Dongbo Xi; Zhen Chen; Peng Yan; Yinger Zhang; Yongchun Zhu; Fuzhen Zhuang; Yu Chen  
**Abstract:** AITM explicitly models a monotone impression→click→application→approval→activation chain. An attention-like module transfers high-level representations from each earlier task to the next, while a Behavioral Expectation Calibrator penalizes violations of decreasing end-to-end probabilities.

**Methodology:** Shared embeddings, task towers, adaptive information transfer near output layers, and an ordinal consistency loss. Earlier dense tasks supervise later sparse tasks; the final activation label is observed at T+14.

**Main results:** In two-week production comparisons on tens of millions of daily impressions, an MLP improved approval/activation 16.95%/17.55% over LightGBM; AITM then improved them 25.00%/42.11% over MLP. Serving TP999/TP9999 latency was below 20/30 ms.

---

## 2. Experiment Critique

**Design:** Industrial and public datasets, strong MTL baselines (ESMM, OMoE, MMoE, PLE), hyperparameter studies, task-count ablations, and production tests. Activation cohorts wait 14 days for mature labels.

**Statistical validity:** Means and standard-deviation shading appear for sensitivity plots, but online confidence intervals, p-values, traffic allocations, and multiple-test controls are not specified in extracted content.

**Online experiments:** Each comparison ran two weeks with four weeks allowed for complete delayed feedback. Sequential launches rather than a single simultaneous multi-arm test may leave time confounding.

**Reproducibility:** Source code is released at https://github.com/xidongbo/AITM; architecture and hyperparameters are detailed. The proprietary Meituan dataset is unavailable.

**Overall:** Strong evidence that explicit stage dependence helps a delayed sparse funnel; causal interpretation across sequential launch periods remains limited.

---

## 3. Industry Contribution

**Deployability:** Fully deployed with low tail latency.

**Problems solved:** Long conversion paths, delayed T+14 feedback, severe later-stage sparsity, and consistency of stage probabilities.

**Engineering cost:** Moderate; requires mature labels for every stage and careful monitoring of transfer/calibration terms.

**Project relevance:** Core. The dating impression→like→match→conversation→date/subscription cascade is almost isomorphic, and AITM provides a practical backbone for adaptive information flow and monotonic end-to-end probability heads.

**Most important mismatch:** Dating stages are not strictly one-user monotone events: match requires the other member, conversations can occur without dates or payments, and successful matching can end platform use. AITM also predicts response, not incremental retention/revenue, and ignores congestion.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Adaptive high-level representation transfer between sequential conversion tasks plus behavioral expectation calibration.

**Prior work comparison:** Contrasts expert-bottom sharing and scalar probability-transfer models; it transfers richer vectors near output layers.

**Verification:** Source-grounded only; no independent web audit.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Meituan credit-card advertising | Not specified | No | Tens of millions daily; T+14 activation. |
| Public benchmark | Described in paper/code | Partial | Exact name not present in extracted snippets. |
| AITM code | https://github.com/xidongbo/AITM | Yes | Official implementation stated in source. |

**Offline experiment reproducibility:** Model-level reproduction is feasible with the code; exact industrial reproduction is not.

---

## 6. Community Reaction

No significant community discussion was assessed in this fallback batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** Meituan and academic collaborators  
**Venue:** KDD  
**Year:** 2021  
**PDF:** Indexed via DOI  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D5 — multi-stage / multi-task conversion chains
