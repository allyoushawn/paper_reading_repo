# Paper Analysis: Mini-Game Lifetime Value Prediction in WeChat

**Source:** https://arxiv.org/abs/2506.11037
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Mini-Game Lifetime Value Prediction in WeChat
- **authors or company:** Aochuan Chen, Yifan Niu, Gong Chen, et al. (HKUST Guangzhou / WeChat)
- **venue:** KDD
- **year:** 2025
- **URL:** https://arxiv.org/abs/2506.11037
- **source type:** industry paper
- **direction:** D4
- **problem setting:** User–item (user–game) LTV prediction for mini-game ad bidding/recommendation; extremely sparse purchases (~0.1% register→purchase).
- **objective and label definition:** Cumulative payment a user contributes to a specific game over 3-, 7-, or 30-day horizons after registration.
- **prediction or incrementality:** Predicts absolute multi-horizon payment value per user–game pair; not causal incrementality.
- **model architecture:** GRePO-LTV: graph representation learning (user/game meta-path graphs) + shared backbone with horizon-specific towers, Temporal Interaction Network, Pareto multi-objective optimization across horizons.
- **credit assignment:** Delayed payment label assigned to user–game pair \((u_p, i_q)\); not slate/impression-level attribution.
- **training data and counterfactual handling:** 3.73M LTV samples (6-month WeChat mini-game data, 7:2:1 split); GRL augments sparse purchase signal via collaborative graph embeddings.
- **offline and online evaluation:** Offline NMAE, AUC, N-GINI across 3/7/30-day tasks; online A/B (5% traffic per arm) on LTV and GMV vs production baseline and ablations.
- **reported gains:** Avg offline NMAE 0.188 vs best baselines (+14.0% NMAE, +3.6% AUC, +1.6% N-GINI); online avg LTV/GMV +8.4% (3d +9.9%/+9.83%, 7d +7.8%/+7.93%, 30d +7.73%/+7.60%).
- **applicability note for a two-sided dating recommender:** User–item LTV with graph-augmented embeddings fits dating payer-value per match/campaign when purchase events are ultra-sparse at item level.
  Pareto optimization across D3/D7/D30 payment heads directly addresses gradient conflict when fusing short- and long-term revenue labels in a shared ranker backbone.
- **unverified claims:** none

## 1. Summary

GRePO-LTV predicts cumulative user payment to a specific WeChat mini-game over 3-, 7-, and 30-day horizons. Sparse purchase data (~0.1% rate) is enriched via graph representation learning on user–game interaction graphs; co-trained horizons suffer gradient conflicts, addressed with Pareto optimization. The model beats ARIMA, ZILN, and Kuaishou ODMN offline on 3.73M samples and delivers +8.4% average LTV/GMV in online A/B on mini-game recommendation traffic.

## 2. Experiment Critique

Strengths: realistic extreme sparsity setting, strong baselines (ZILN, ODMN/Kuaishou), ablations removing GRL and Pareto, multi-horizon offline and online metrics. Weaknesses: proprietary dataset; user–game LTV may not transfer to reciprocal matching markets; Pareto adds training complexity; delay/censoring for incomplete payment windows not discussed.

## 3. Industry Contribution

Shows graph collaborative signals materially help LTV under 0.1% purchase rates, and that Pareto MOO is necessary when multi-horizon LTV tasks conflict—relevant pattern for any multi-head revenue/retention model sharing a backbone.

## 4. Novelty vs. Prior Work

Builds on ZILN (Wang et al. 2019), Kuaishou ODMN (Li et al. CIKM 2022), graph CF for sparse prediction (He et al.; Liu et al. TKDE 2020), Pareto-efficient recsys (Lin et al. RecSys 2019; Xie et al. WWW 2021), and sequence LTV (Xing et al. KDD 2021). Novel combination: GRL + TIN + Pareto for multi-horizon user–item LTV at industrial scale.

## 5. Dataset Availability

Proprietary WeChat mini-game recommendation dataset (3,730,392 LTV samples); not publicly released.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Primary objective is user–game LTV (cumulative payment) for ad bidding and recommendation. CTR not used in GRePO-LTV objective (mentioned only in unrelated prior work).

### (2) Credit assignment: user-level delayed outcome → item-level decision
Payment label assigned to user–game pair. Attribution from user-level retention or multi-item slate to single exposure: not specified in source.

### (3) Label and horizon definitions; delay, sparsity, censoring
Label: cumulative payment to a game. Horizons: 3-, 7-, 30-day. Purchase rate ~0.1% among registered users (severe sparsity). Delay and censoring: not specified in source.

### (4) Short vs long-term head fusion
Shared backbone with horizon-specific tower layers; Pareto optimization balances conflicting gradients across 3/7/30-day heads (not fixed fusion weights). Ablations: w/o Pareto drops online LTV gain to +0.28%.

### (5) Prediction vs incrementality
Absolute payment-value prediction per user–game pair.

### (6) Offline and online evaluation
Offline: 3.73M samples, NMAE/AUC/N-GINI. Online A/B: 5% traffic per group (baseline, w/o GRL, w/o Pareto, full model); LTV and GMV lifts reported by horizon.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Deployed in WeChat mini-game recommendation with online A/B validation. Explicit CTR→LTV migration steps: not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Aochuan Chen, Yifan Niu, Gong Chen, et al.
**Affiliations:** The Hong Kong University of Science and Technology (Guangzhou); WeChat (industrial deployment)
**Venue:** KDD
**Year:** 2025
**PDF:** https://arxiv.org/abs/2506.11037
**Relevance:** Core
**Priority:** 1
