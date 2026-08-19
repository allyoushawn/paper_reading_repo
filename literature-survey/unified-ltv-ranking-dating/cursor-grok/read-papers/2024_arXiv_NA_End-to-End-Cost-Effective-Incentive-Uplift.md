# Paper Analysis: End-to-End Cost-Effective Incentive Recommendation under Budget Constraint with Uplift Modeling

**Source:** https://arxiv.org/pdf/2408.11623.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** End-to-End Cost-Effective Incentive Recommendation under Budget Constraint with Uplift Modeling
- **authors or company:** Zexu Sun, Hao Yang (Renmin University of China); Dugang Liu; Yunpeng Weng, Xing Tang, Xiuqiang He (FiT, Tencent)
- **venue:** RecSys 2024
- **year:** 2024
- **URL:** https://arxiv.org/pdf/2408.11623.pdf
- **source type:** academic / industry
- **direction:** D6
- **problem setting:** Personalized incentive (coupon/discount level) assignment per user under global budget constraint, formulated as multi-choice knapsack (MCKP) maximizing ROI.
- **objective and label definition:** CATE-style uplifts τ^c_{i,k} (conversion) and τ^r_{i,k} (revenue/cost) vs control k=0; treatments k∈{0,…,K}; budget constraint on sum of cost uplifts; monotonic smooth response curves enforced structurally.
- **prediction or incrementality:** Incrementality (uplift/CATE) for allocation; end-to-end joint training of uplift heads and differentiable ILP allocation layer.
- **model architecture:** E3IR: (1) uplift module—shared bottom, adjacent-treatment incremental heads with non-negative increments (monotonicity), shared weights + Lipschitz regularization (smoothness); (2) differentiable allocation module—ILP backward pass with descent-direction gradients for τ^c and τ^r; joint loss L_E3IR = L_predict + β L_allocation.
- **credit assignment:** User-level treatment assignment (which incentive level per customer); not item-level ranking in a feed.
- **training data and counterfactual handling:** RCT-style logged data (x, t, y^c, y^r); Hillstrom email campaign (public) and Tencent short-video production dataset (8M+ users, 108 features, 3 sharpening levels + control); potential-outcome framework assumptions for CATE.
- **offline and online evaluation:** Offline: AUUC, QINI, KENDALL, AUCC (binary); MT-AUCC, EOM (multi-treatment); ablations; budget sensitivity curves. No online A/B in paper.
- **reported gains:** Binary Hillstrom-Men/Women: E3IR best on AUUC/QINI/KENDALL/AUCC vs meta-learners, DragonNet, TPM-SL, Direct Rank, DRP (Table 1, e.g., Men KENDALL 0.7033 vs DRP 0.6811). Multi-treatment: Hillstrom MT-AUCC 0.0803 vs DRM 0.0726; Production MT-AUCC 0.4639 vs DRM 0.3601; EOM 44.51 vs DRM 36.65 (scaled).
- **applicability note for a two-sided dating recommender:** Template for budgeted promotional allocation (boosts, super-likes, discounts) using uplift + constrained optimization rather than propensity-only ranking.
- **applicability note for a two-sided dating recommender:** Not reciprocal profile ranking or match-quality objectives; user-level incentive pick, not slate LTV ranking.
- **unverified claims:** none

## 1. Summary

E3IR unifies uplift estimation and budgeted incentive assignment for online marketing. It enforces marketing domain structure (monotonic, smooth dose–response curves) in the uplift network and backpropagates through a differentiable ILP layer solving the MCKP, closing the optimality gap of two-stage predict-then-optimize pipelines. Evaluated on Hillstrom and a large Tencent video-quality experiment.

## 2. Experiment Critique

Thorough baseline grid (S/X-Learner, Causal Forest, CFRNet, DragonNet, EUEN, TPM-SL, Direct Rank, DRP, Multi-TPM-SL, DRM). Five random seeds on public data. Production dataset is proprietary with no online validation. Hyperparameters tuned via Optuna on QINI—may favor E3IR objective alignment.

## 3. Industry Contribution

Tencent FiT co-authorship; production-scale dataset (8M users). Addresses real marketing constraint: finite budget over discrete incentive levels with cost-aware uplifts (not fixed coupon face value as sole cost).

## 4. Novelty vs. Prior Work

Extends two-stage MCKP+uplift (Albert & Goldenberg CIKM 2022; Zhou et al. AAAI 2023 DRP) with monotonic multi-head uplift and CombOptNet-style differentiable ILP (Paulus et al. 2021). Differentiable allocation gradient derivation is a technical contribution.

## 5. Dataset Availability

Hillstrom email merchandising campaign (public benchmark); Tencent production dataset proprietary.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**Low project relevance** for core feed ranking, but directly relevant to **D6 / Q5**: user-level incrementality under budget—not outcome-only LTV regression. Useful if the dating product allocates paid boosts or discounts with a global budget. Does not model reciprocity, congestion, or item-level delayed retention credit (**Q2, Q7**). End-to-end predict+optimize pattern parallels decision-focused ranking under constraints.

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Not specified in source—maximize incremental conversion/revenue under budget, not organic feed ranking. |
| 2 | Credit assignment | User-level incentive choice; no item/slate attribution. |
| 3 | Labels / horizon | Conversion and revenue/cost responses per treatment level from campaign logs; not long-horizon retention. |
| 4 | Short/long fusion | Not specified in source. |
| 5 | Prediction vs incrementality | CATE/uplift for treatment levels; allocation optimizes incremental ROI. |
| 6 | Offline / online eval | Offline uplift and allocation metrics only; no online test reported. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Not specified in source. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Zexu Sun, Hao Yang, Dugang Liu, Yunpeng Weng, Xing Tang, Xiuqiang He
**Affiliations:** Renmin University of China; Guangdong Lab of AI and Digital Economy (SZ); Tencent FiT
**Venue:** RecSys 2024
**Year:** 2024
**PDF:** https://arxiv.org/pdf/2408.11623.pdf
**Relevance:** Related
**Priority:** 3
