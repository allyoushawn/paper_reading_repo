# Paper Analysis: Learning to Rank for Uplift Modeling

**Source:** https://arxiv.org/pdf/2002.05897.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Learning to Rank for Uplift Modeling
- **authors or company:** Floris Devriendt, Tias Guns, Wouter Verbeke (Vrije Universiteit Brussel)
- **venue:** arXiv (later IEEE TKDE)
- **year:** 2020
- **URL:** https://arxiv.org/pdf/2002.05897.pdf
- **source type:** academic
- **direction:** D6
- **problem setting:** Binary conversion uplift from RCT logs; uplift scores rank users for treatment targeting (marketing/churn), not feed item ranking.
- **objective and label definition:** Individual treatment effect \(U(X)=P(y=1|X,t=1)-P(y=1|X,t=0)\); binary response \(y\) from A/B treatment \(t\in\{0,1\}\); ranking quality measured via uplift/Qini curves and AUUC.
- **prediction or incrementality:** Estimates CATE-style uplift and optimizes ranking directly via listwise LTR; not observational incrementality of exposure in a recommender.
- **model architecture:** LambdaMART gradient-boosted trees optimizing promoted cumulative gain (PCG)—an AUUC-aligned listwise metric—vs pointwise flipped-label XGBoost and two-model/uplift-RF baselines.
- **credit assignment:** User-level RCT tuples \((X,y,t)\); no item-level or delayed outcome credit assignment.
- **training data and counterfactual handling:** Assumes randomized treatment independent of \(X\); trained on historical A/B data (Information, Hillstrom, Criteo uplift benchmarks).
- **offline and online evaluation:** Offline AUUC and uplift curves only; LambdaMART+PCG matches or beats uplift RF/two-model on Hillstrom and Criteo; two-model wins on Information; top-\(k\) cutoff training does not generalize on test.
- **reported gains:** On Hillstrom, LambdaMART PCG reaches ~4% incremental gains at 50% targeted population where other methods need ~100%; significantly higher AUUC than two-model and uplift RF on Hillstrom and Criteo (student \(t\)-test, \(p=0.05\)).
- **applicability note for a two-sided dating recommender:** Treats uplift as a user-level ranking problem—useful if dating interventions (boosts, promos, push) need persuadability scores rather than profile ranking.
  PCG/AUUC optimization is a template for ranking users by incremental subscription/retention lift from RCT logs, but it does not address reciprocal match ranking or delayed LTV labels.
- **unverified claims:** none

## 1. Summary

Links uplift modeling to learning-to-rank: unifies uplift/Qini curve definitions, introduces PCG as a listwise metric aligned with AUUC, and trains LambdaMART to optimize PCG directly. Compares pointwise (flipped-label) vs listwise formulations on three public uplift datasets against standard uplift baselines. Shows LTR can match or beat tree/meta-learner uplift models on some datasets; top-\(k\)-specific training shows limited test-set benefit.

## 2. Experiment Critique

Strengths: careful formalization of conflicting uplift curve variants; direct optimization of ranking metric; comparison against multiple uplift baselines. Weaknesses: binary conversion only; small public datasets; no online deployment; top-\(k\) cutoff results largely insignificant; Information dataset favors classical two-model approach over LTR.

## 3. Industry Contribution

Conceptual bridge from causal targeting to LTR infrastructure (LambdaMART). Deployability limited: requires RCT-labeled user populations and binary outcomes; no production case study.

## 4. Novelty vs. Prior Work

Novel PCG metric and LTR formulation of AUUC; differs from SVM-struct uplift curve work (Lai et al.) by using LambdaMART and unified curve taxonomy. Builds on Devriendt et al. uplift evaluation literature and standard LTR (LambdaMART, DCG/NDCG).

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Information | Public uplift benchmark | Yes | Used in paper |
| Hillstrom | MineThatData challenge | Yes | Email campaign |
| Criteo Uplift | Public | Yes | Advertising |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Optimizes treatment targeting by uplift rank (conversion), not feed CTR, retention, or LTV. Retention/LTV/revenue: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
User-level RCT labels only; no mapping to per-profile or per-impression decisions. Item-level credit assignment: Not specified in source.

### (3) Label and horizon definitions; delay, sparsity, censoring
Binary immediate conversion from RCT; horizon defined per benchmark dataset. Delay, sparsity, censoring: Not specified in source.

### (4) Short vs long-term head fusion
Not specified in source (single uplift ranking objective).

### (5) Prediction vs incrementality
Incrementality (CATE) estimation for ranking persuadable users; not absolute outcome prediction.

### (6) Offline and online evaluation
Offline AUUC/uplift curves on three datasets. No online evaluation.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Not specified in source; orthogonal user-level uplift targeting vs feed ranker.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Floris Devriendt, Tias Guns, Wouter Verbeke
**Affiliations:** Vrije Universiteit Brussel
**Venue:** arXiv 2020; IEEE TKDE 2022
**Year:** 2020
**PDF:** https://arxiv.org/pdf/2002.05897.pdf
**Relevance:** Core
**Priority:** 4
