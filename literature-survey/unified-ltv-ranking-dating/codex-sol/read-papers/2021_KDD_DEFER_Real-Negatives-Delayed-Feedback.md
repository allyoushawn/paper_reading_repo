# Paper Analysis: Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling

**Source:** https://arxiv.org/abs/2104.14121  
**Source ID:** 37991319-4bdb-4953-ac0c-c9206bc92413  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback; indexed source contained the arXiv abstract/metadata rather than full paper, so absent fields are explicit.

---

## 1. Summary

**Authors:** Siyu Gu; Ying Fan; Guorui Zhou; Xiaoqiang Zhu; one additional author not specified in indexed metadata  
**Abstract:** DEFER re-ingests matured real negatives as well as late positives. This restores the actual feature distribution distorted by duplicated positives, adds abundant certainty from negatives, and uses importance sampling to correct the resulting sampling distribution.

**Main results:** The source reports deployment in Alibaba display advertising with more than 6.0% CVR improvement across several scenarios. Detailed offline tables were not present in the indexed source.

---

## 2. Experiment Critique

**Design:** Industrial delayed-feedback experiments are stated; exact datasets, baselines, splits, and ablations are not specified in indexed content.

**Statistical validity:** Not specified in source.

**Online experiments:** Production deployment is reported, but duration, traffic, uncertainty, and randomization are not specified.

**Reproducibility:** Code/data: https://github.com/gusuperstar/defer.git. Full paper details were unavailable in this extraction.

**Overall:** The production result supports practical value, but the abstract-only evidence prevents a detailed validity audit.

---

## 3. Industry Contribution

**Deployability:** Demonstrated at Alibaba; concept fits continuous-training queues.

**Project relevance:** Core. Mature 7–30-day non-retention/non-payment examples are informative and should enter training alongside late positives; otherwise duplicated positives distort feature marginals.

**Most important mismatch:** Does not address reciprocal outcomes, interference, causal uplift, or success-paradox censoring.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** Correct delayed-feedback sampling with explicit ingestion of real negatives plus importance weighting.

**Verification:** Abstract-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Released code/data | Yes | GitHub link above; contents not independently audited. |
| Alibaba production | No | Details not in indexed abstract. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** Alibaba  
**Venue:** KDD  
**Year:** 2021  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D7 — delayed feedback / censored labels
