# Paper Analysis: Counterfactual Multi-task Learning for Delayed Conversion Modeling

**Source:** https://arxiv.org/html/2604.21675  
**Source ID:** 5ea68e79-8249-42ee-af99-0f0f4dd1840d  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Xin Song; Kaiyuan Li; Jinxin Hu  
**Abstract:** CM-DCM targets event-shaped delays: pre-promotion clicks convert mostly on one future sale day. It jointly predicts direct and delayed conversion, gates transfer from daily CVR/ATC models, and uses a doubly robust counterfactual regularizer for the add-to-cart effect.

**Main results:** Six-day Double 11/12 tests with 20% traffic per arm reported +7.87% ad revenue, +4.24% delayed GMV, +1.42% overall GMV, and +2 ms P99 latency.

---

## 2. Experiment Critique

**Design:** Public and industrial offline benchmarks, delayed-CVR baselines, ablations, and two major-sale production tests.

**Statistical validity:** Online traffic share and duration are specified; confidence intervals, p-values, exact sample sizes, and multiple-event heterogeneity are not in extracted content.

**Online experiments:** Yes; delayed labels are naturally concentrated on promotion day.

**Reproducibility:** arXiv HTML is detailed; industrial data and event system are proprietary. Code availability not specified.

**Overall:** Strong evidence for scheduled, distribution-shifted delay; causal ATC claims still depend on DR nuisance-model assumptions.

---

## 3. Industry Contribution

**Deployability:** Parallel predictors and small gates add only 2 ms P99.

**Project relevance:** Core. Dating retention/revenue labels also mature after weeks and may cluster around subscription renewal or re-engagement events. Separate direct/delayed tasks, personalized transfer, and DR regularization are useful.

**Most important mismatch:** Dating delays are not tied to a known sale day, and ATC is a one-sided manipulable action unlike mutual match/conversation. Reciprocity, congestion, success exit, and revenue mixture remain unmodeled.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** First delayed-conversion framework for sales pre-promotion combining MTL, personalized transfer, and counterfactual ATC regularization.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Public delayed-CVR dataset(s) | Partial | Names not present in extracted snippets. |
| Industrial promotions | No | Double 11/12 traffic. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** Alibaba; Kuaishou  
**Venue:** SIGIR  
**Year:** 2026  
**Relevance:** Core—inferred  
**Priority:** 1  
**Direction:** D7 — delayed feedback / censored labels
