# Paper Analysis: A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao

**Source:** https://arxiv.org/abs/2505.07197
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao
- **authors or company:** Yue Meng, Cheng Guo, Yi Cao, Tong Liu, Bo Zheng (Taobao & Tmall Group of Alibaba)
- **venue:** SIGIR
- **year:** 2025
- **URL:** https://doi.org/10.1145/3726302.3731935
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Taobao feed re-ranking after matching/ranking: reorder a candidate list of length \(l_s\) into output length \(l_o\) to optimize multiple session-level business objectives (click, conversion/order, GMV) under latency and diversity constraints — not a unified long-horizon retention objective.
- **objective and label definition:** List-level value maximization \(\alpha V_{click} + \beta V_{conversion} + \gamma V_{GMV}\) with sequential incremental accumulation over positions; training uses ordered regression on real exposed lists — cumulative click/pay counts per sub-list length (immediate session labels from logs, no delayed retention horizon).
- **prediction or incrementality:** Predicts list-level cumulative click/conversion/GMV values for sub-lists and selects items to maximize weighted multi-objective value — supervised prediction of short-horizon engagement outcomes, not causal incrementality on long-term retention.
- **model architecture:** SORT-Gen: (1) Sequential Ordered Regression Transformer — causal Transformer on item/position/user/prior-score (upstream CTR/CVR) features with ordered-regression loss over \(l_o\) threshold tasks per click and pay heads; (2) Mask-Driven Fast Generation — multi-objective candidate queues, single-forward-pass mask-driven selection maximizing list value (or MMR-adjusted value for diversity).
- **credit assignment:** List-level credit — clicks/conversions anywhere in the exposed list contribute to cumulative list-value labels; position-aware ordered regression attributes incremental value across list positions within one request slate.
- **training data and counterfactual handling:** Real exposure item lists from Taobao production (Baiyibutie mini-app for online eval); consumes upstream ranking CTR/CVR scores as features; no offline AUC/NDCG reported — paper states list-level MOO is unattainable via standard offline metrics; inference weights \(\alpha,\beta,\gamma\) set manually (5,1,1 in experiment).
- **offline and online evaluation:** Online A/B only on Baiyibutie over two weeks vs greedy-formula baseline and re-ranking baselines (LTR, Pareto formulas, fastDPP, PRM, FFT context-aware CTR, FFT+fastDPP); end-to-end latency ~19ms; ablations on multi-objective queues, ordered regression, ESMM-like loss, integrated MMR.
- **reported gains:** vs greedy formula baseline: +9.61% CLICK, +8.35% ORDER, +13.67% GMV (Table 1, asterisked); vs FFT Context-aware + fastDPP: +4.13% CLICK, +8.10% GMV; deployed across multiple Taobao App scenarios.
- **applicability note for a two-sided dating recommender:** List-level generative re-ranking with explicit multi-objective fusion (match rate, conversation, revenue) is relevant if dating stacks keep separate CTR/CVR rankers and need a final slate optimizer that models position context and diversity — analogous to optimizing a profile list shown to one viewer.
- **applicability note for a two-sided dating recommender:** Objectives are immediate click/conversion/GMV within a session, not D7/D30 retention or bilateral congestion; manual \(\alpha,\beta,\gamma\) tuning and no reciprocal or incrementality framing limit direct transfer to unified LTV ranking.
- **unverified claims:** none

## 1. Summary

SORT-Gen addresses list-level multi-objective optimization in the re-ranking stage of Taobao's cascade. A Transformer with ordered regression estimates click and conversion list values for variable-length sub-lists; mask-driven fast generation selects items from multi-objective queues in one forward pass with integrated MMR diversity. Online A/B on Baiyibutie shows large gains over item-level and context-only re-ranking baselines at ~19ms latency; deployed in multiple Taobao scenarios.
