# Paper Analysis: Hierarchically Modeling Micro and Macro Behaviors via Multi-Task Learning for Conversion Rate Prediction

**Source:** https://doi.org/10.1145/3404835.3463053  
**Source ID:** ad032348-2b1f-4018-8ed5-15768681767b  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Abstract:** HM3 represents detail-page micro behaviors and broader macro post-click behaviors as one- and two-hop nodes in a sequential behavior graph. Six probability heads are composed by conditional-probability identities into four auxiliary tasks and final CVR, using all impressions to reduce sample-selection bias and data sparsity.

**Methodology:** End-to-end multi-task DNN with graph-derived probability factorization. Baselines include a single-task DNN, ESMM, ESM2, GMCM, ESM2 augmented with micro behaviors, and a reversed hierarchy ablation.

**Main results:** On the largest offline set HM3 reached CVR AUC 0.85726 and CTCVR AUC 0.86806, beating the base by 0.00794 AUC. A 2020-10-08–21 production test reported +8.27% CVR and +8.32% GMV versus base, compared with ESMM’s +2.76%/+3.02% and ESM2’s +4.84%/+5.11%.

---

## 2. Experiment Critique

**Design:** Chronological platform logs with three training-window sizes and the last day as test; multiple strong baselines plus ordering ablation; two-week production A/B test.

**Statistical validity:** AUC and relative online lift are reported, but confidence intervals, p-values, traffic allocation, random seeds, and variance are absent from extracted content.

**Online experiments:** Yes, roughly two weeks, measuring CVR and GMV. Longer-horizon retention and delayed revenue were not measured.

**Reproducibility:** Core factorization, optimizer, learning rate, and baselines are described. Proprietary micro/macro logs are unavailable; the authors state no public large-scale dataset contains both behavior types.

**Overall:** Results support hierarchical auxiliary supervision for sparse cascades, but business lift may include platform-specific merchandising effects.

---

## 3. Industry Contribution

**Deployability:** Compatible with industrial multi-head rankers and demonstrated online.

**Problems solved:** Post-click selection bias, sparse purchase labels, and use of intermediate fine-grained signals.

**Engineering cost:** Moderate-to-high label instrumentation and strict probability-graph implementation.

**Project relevance:** Core. The impression→like→match→conversation→date/subscription path can be encoded as a conditional-probability graph with auxiliary heads, exploiting abundant upstream labels while preserving a final value target.

**Most important mismatch:** HM3 predicts conversion/GMV rather than direct long-horizon incremental value and assumes a one-sided ordered behavior hierarchy; dating transitions are reciprocal, non-monotone, congested, delayed, and censored by successful exit.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Joint hierarchical modeling of micro and macro behaviors in an entire-space MTL graph.

**Prior work comparison:** Extends ESMM/ESM2 and graph-based micro-behavior models by combining both behavior levels with explicit conditional identities.

**Verification:** Source-grounded only; no independent web audit.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Shopping Recommendation logs (SR-S/M/L) | Not specified | No | 2020-09-16–30 proprietary platform logs. |
| Online A/B test | Not specified | No | 2020-10-08–21. |

**Offline experiment reproducibility:** Not possible exactly without proprietary behavior graphs; model can be tested on a substitute cascade dataset.

---

## 6. Community Reaction

No significant community discussion was assessed in this fallback batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Not specified in extracted header  
**Affiliations:** Industrial e-commerce platform  
**Venue:** SIGIR  
**Year:** 2021  
**PDF:** Indexed via DOI  
**Relevance:** Core—inferred  
**Priority:** 1  
**Direction:** D5 — multi-stage / multi-task conversion chains
