# Paper Analysis: Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing

**Source:** https://arxiv.org/pdf/2405.15301.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing (RERUM)
- **authors or company:** Bowei He, Yunpeng Weng, Xing Tang, Ziqiang Cui, Zexu Sun, Liang Chen, Xiuqiang He, Chen Ma (Tencent FiT; City University of Hong Kong)
- **venue:** KDD
- **year:** 2024
- **URL:** https://arxiv.org/pdf/2405.15301.pdf
- **source type:** industry paper
- **direction:** D6
- **problem setting:** Revenue uplift modeling for online fintech marketing—rank users by incremental revenue lift from interventions (coupons, notifications), not item-level feed ranking.
- **objective and label definition:** CATE \(\tau(x)=E[Y|X=x,T=1]-E[Y|X=x,T=0]\) with continuous revenue response \(Y\); ranking metrics AUUC, AUQC, KRCC, LIFT@30; online LIFT@2 on top-2% ranked users over 1-month sales window.
- **prediction or incrementality:** Estimates heterogeneous treatment effect on continuous revenue; optimizes uplift ranking via ZILN response heads plus listwise uplift ranking loss—incrementality for campaign targeting, not exposure effect in a swipe ranker.
- **model architecture:** Pluggable deep uplift backbone (TAR, CFR, DragonNet, etc.) with ZILN treatment/control response modules, within/cross-group response ranking losses, and ListNet-style listwise uplift ranking loss \(L_{lu-rank}\); overall \(L_{overall}=L_{ZILN}+L_{r-rank}+L_{lu-rank}+\lambda\|\theta\|^2\).
- **credit assignment:** User-level RCT samples \((x,t,y)\); pairwise/listwise losses align predicted uplift order across treatment and control arms—no per-impression delayed credit.
- **training data and counterfactual handling:** RCT-style treatment/control logs; Hillstrom 2-week spend, Tencent Product dataset (>5M users, fund purchase revenue), FiT online campaigns.
- **offline and online evaluation:** Offline AUUC/AUQC/KRCC/LIFT@30 on Hillstrom-Men/Women and Product; online three mutual-fund notification campaigns on Tencent FiT (~400M-user platform), measuring sales revenue LIFT@2 on top-2% ranked users.
- **reported gains:** Offline: RERUM(DragonNet) improves LIFT@30 by 21.98% on average vs best baseline across three datasets; online LIFT@2 +9.20%, +37.24%, +15.43% across three campaigns (20.61% average), authors report 430M USD AUM gain per month.
- **applicability note for a two-sided dating recommender:** Revenue uplift + ZILN + listwise rankability directly mirrors dating's zero-inflated subscription/LTV tails when ranking users for boosts, discounts, or CRM—not for ranking candidate profiles.
  Listwise uplift loss and response-ranking bounds are reusable if the product runs RCTs on monetization interventions and needs to prioritize high-incremental-revenue users under budget.
- **unverified claims:** none

## 1. Summary

RERUM addresses revenue (continuous) uplift where MSE fails on zero-inflated long tails. Replaces response regression with ZILN, adds theoretically motivated within/cross-group response ranking losses, and a listwise uplift ranking loss. Stacks on deep uplift backbones; strong offline uplift-ranking metrics and large-scale Tencent FiT online campaigns on mutual-fund sales.

## 2. Experiment Critique

Strengths: real 400M-user fintech deployment; ablations on ZILN, UR, RR modules; multiple backbones; code released. Weaknesses: online eval on top-2% only; campaign-level not full-ranker integration; UR/RR slightly hurt MAPE while helping ranking; RCT assumption required.

## 3. Industry Contribution

Production-grade revenue uplift ranker for Tencent FiT wealth management; demonstrates ZILN inside uplift models and listwise ranking for causal targeting at scale.

## 4. Novelty vs. Prior Work

Extends conversion uplift (CFR, DragonNet) to continuous revenue with explicit rankability losses; cites Devriendt et al. LTR-for-uplift and Google ZILN. Novel combination of ZILN + tighter uplift distance bounds + listwise uplift loss.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Hillstrom | Public | Yes | 2-week spend label |
| Tencent Product | Industrial | No | >5M users |
| FiT online campaigns | Internal | No | 400M-user platform |

**Code:** https://github.com/BokwaiHo/revenue_uplift

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Primary: rank users by incremental revenue uplift (LIFT@30, LIFT@2). CTR/match ranking: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
User-level RCT revenue labels; 1-month online horizon for LIFT@2. Item-level/impression credit: Not specified in source.

### (3) Label and horizon definitions; delay, sparsity, censoring
Continuous revenue with extreme zero inflation and whale tail; Hillstrom 2-week spend; online 1-month sales window. Sparsity explicitly addressed via ZILN.

### (4) Short vs long-term head fusion
Not specified in source (single uplift ranker, not multi-head feed model).

### (5) Prediction vs incrementality
Incrementality (CATE on revenue) with ranking-optimized training.

### (6) Offline and online evaluation
Offline uplift curves + three online marketing campaigns on FiT.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
User-level intervention ranker parallel to feed ranker; ZILN revenue head transferable to subscriber LTV scoring.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Bowei He, Yunpeng Weng, Xing Tang, Ziqiang Cui, Zexu Sun, Liang Chen, Xiuqiang He, Chen Ma
**Affiliations:** Tencent FiT; City University of Hong Kong; Renmin University of China
**Venue:** KDD 2024
**Year:** 2024
**PDF:** https://arxiv.org/pdf/2405.15301.pdf
**Relevance:** Core
**Priority:** 4
