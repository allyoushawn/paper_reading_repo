# Paper Analysis: Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets

**Source:** https://arxiv.org/pdf/2306.09060  
**Source ID:** 5f2155d9-f8d0-4247-a21e-eef7f102c721  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Yoji Tomita; Riku Togashi; Yuriko Hashizume; Naoto Ohsaka  
**Abstract:** The method treats bilateral preference scores as transferable-utility surplus and solves a stochastic market equilibrium whose implicit transfers spread demand away from over-popular users. Efficient vector search yields rankings without specifying examination curves.

**Main results:** Across synthetic market sizes, TU beat naive/product-reciprocal methods and generally matched the social-welfare optimizer; the latter failed at n=500. On Japanese dating data, TU matched/slightly trailed the correctly specified skyline at 200×200 and clearly beat naive/reciprocal at 1,000×1,000 where the skyline was infeasible.

---

## 2. Experiment Critique

**Design:** Synthetic crowding/examination sensitivity, ten repetitions with 10K Monte Carlo simulations, real dating preferences, 200×200/1,000×1,000 cases, and scalability comparison.

**Statistical validity:** Synthetic standard errors were about 1e-1; real-data experiments are simulations on estimated ALS preferences, not live outcomes.

**Online experiments:** None; explicitly future work.

**Reproducibility:** Code: https://github.com/CyberAgentAILab/tu-matching-recommendation. Dating data are proprietary.

**Overall:** Directly addresses reciprocity and congestion, but evidence is limited to moderate offline simulations and model-based preference completion.

---

## 3. Industry Contribution

**Deployability:** More scalable and robust to examination misspecification than prior stochastic social-welfare optimization, though still O(|C||J|) per iteration.

**Project relevance:** Core. This paper directly fits viewer A→candidate B ranking, balances mutual preference, reduces popular-candidate congestion, and optimizes total matches rather than unilateral CTR.

**Most important mismatch:** The objective is expected match count, not conversation/date/retention/revenue or incremental value. Implicit transferable utility may not represent dating preferences, and success-paradox censoring is absent.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** TU-matching reciprocal ranking with examination-agnostic inference and practical vector-search implementation.

**Prior work comparison:** Improves over unilateral aggregation and an examination-dependent constrained social-welfare policy.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Synthetic generator | Yes | Included with code. |
| Japanese dating platform | No | Proprietary, millions of cumulative members; sampled subsets. |
| Code | Yes | Official GitHub. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** CyberAgent AI Lab  
**Venue:** RecSys  
**Year:** 2023  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D8 — reciprocal recommendation / matching markets
