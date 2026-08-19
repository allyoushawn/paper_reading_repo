# Paper Analysis: Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems

**Source:** https://arxiv.org/pdf/2208.06942
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems
- **authors or company:** Qihua Zhang, Junning Liu, Yuzhuo Dai, Yiyan Qi, Yifan Yuan, Kunlun Zheng, Fan Huang, Xianfeng Tan (Tencent)
- **venue:** KDD (industry track; arXiv 2208.06942)
- **year:** 2022
- **URL:** https://arxiv.org/pdf/2208.06942
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Session-based short-video ranking on Tencent production traffic; MTL predicts multiple engagement scores and an MTF module fuses them into a final ranking score per recommendation step within a session.
- **objective and label definition:** Optimizes long-term user satisfaction within a recommendation session (MDP with discount γ=0.95). Instant reward r(s,a) = weighted sum of immediate feedback metrics (video play time, play integrity, likes, shares, comments, skips); weights w_i set offline via regression relating those metrics to future app dwell time. Action is a 12-dimensional personalized fusion weight vector α for logarithmic combination of PLE MTL task outputs.
- **prediction or incrementality:** Learns a fusion policy (continuous action α) that maximizes cumulative discounted session reward; not a direct LTV predictor—optimizes fusion weights trading instant vs. delayed satisfaction.
- **model architecture:** BatchRL-MTF: session MDP + Batch-Constrained deep Q-learning (BCQ) actor-critic with VAE action generator, bounded action perturbation (ρ=0.15), clipped double Q critics; upstream PLE MTL for task scores; online mixed multi-exploration (random + action-noise) for data collection; Conservative-OPEstimator (CQL + FQE) for offline policy evaluation.
- **credit assignment:** Per recommendation timestep within a session: state = user profile + interaction history (last 500 watched videos); action = fusion weights applied to current candidate ranking; transition and reward follow user feedback on the recommended item(s) at that step; long-term value bootstrapped with γ=0.95 across the session trajectory.
- **training data and counterfactual handling:** Offline on 3.142M sessions / 11.155M user-agent interactions from Tencent short-video logs (90% chronological train, 10% test); BCQ restricts actions to in-distribution regions via VAE cloning of batch actions to mitigate extrapolation error; online exploration collects supplementary trajectories; daily retrain on past three days of trajectories.
- **offline and online evaluation:** Offline Conservative-OPEstimator on held-out 10% sessions; compares BO, ES, TD3, UWAC+TD3, CQL+SAC and ablations; one-month online A/B on production short-video platform serving hundreds of millions of users; metrics include app dwell time (ADTime) and user positive-interaction rate (UPIRate).
- **reported gains:** Production deployment: +2.550% app dwell time and +9.651% user positive-interaction rate vs. baselines; offline OPE ranks BatchRL-MTF best on stability and returns among RL variants; ablation BatchRL-MTF-Rinteraction matches top online interaction gains (+2.550% ADTime, +9.651% UPIRate in table variant).
- **applicability note for a two-sided dating recommender:** Direct template for replacing static MTF weight tuning with session-level RL over MTL heads when delayed retention/dwell proxies exist and logged fusion-weight trajectories can be collected safely.
- **applicability note for a two-sided dating recommender:** Two-sided reciprocity, match congestion, and counterparty credit assignment are not addressed; reward is single-user stickiness/activeness on consumed content, not bilateral match outcomes.
- **unverified claims:** none

## 1. Summary

**Title:** Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems
**Authors:** Qihua Zhang, Junning Liu, Yuzhuo Dai, Yiyan Qi, Yifan Yuan, Kunlun Zheng, Fan Huang, Xianfeng Tan (Tencent)
**Abstract:** Formulates multi-task fusion (MTF) as a session MDP and trains BatchRL-MTF offline from logged trajectories with BCQ and online mixed exploration, using a dwell-time-correlated reward over multiple engagement signals.

**Key contributions:**
- Session-based MDP formulation for personalized MTF weight optimization toward long-term satisfaction rather than greedy instant metrics.
- BatchRL-MTF with BCQ actor-critic, mixed online exploration, and Conservative-OPEstimator for safe offline policy evaluation.
- Heuristic reward engineering linking immediate engagement to future app dwell time; production deployment on Tencent short video.

**Methodology:** PLE MTL produces task scores; Batch RL policy outputs fusion weights α for f(o|α) = Σ α_i log(o_i + β_i); trained on historical session trajectories with daily refresh.

**Main results:** +2.550% app dwell time and +9.651% positive-interaction rate in production; offline OPE shows superiority over TD3/UWAC+TD3 and competitive stability vs. CQL+SAC.

## 2. Experiment Critique

**Design:** Strong industrial scale (millions of sessions) with chronological split, multiple RL and non-RL baselines, reward ablations, and dedicated offline OPE; fusion layer is the intervention point while MTL is fixed PLE.

**Statistical validity:** Online A/B over one month at massive scale; specific p-values not stated in extracted material for dwell-time lifts; offline OPE provides ranking of policies but is itself a modeled estimator.

**Online experiments (if any):** One-month A/B on live short-video traffic; exploration policies deliberately inject random and noise perturbations on subsets of users for data collection.

**Reproducibility:** Tencent proprietary logs; hyperparameters reported (γ=0.95, ρ=0.15, replay buffer 100k, etc.); no public dataset.

**Overall:** Claims are well aligned with a fusion-layer RL deployment story; long-term reward is proxy-based (dwell-correlated instant metrics) rather than direct retention labels; two-sided effects absent.

## 3. Industry Contribution

**Deployability:** Demonstrated at Tencent short-video scale with offline training + online serving loop and daily retraining.

**Problems solved:** Replaces inefficient grid search / BO for MTF weights; adds personalization and long-horizon optimization while limiting OOD extrapolation via BCQ.

**Engineering cost:** Requires trajectory logging of fusion weights, exploration traffic, BCQ + VAE stack, and Conservative-OPEstimator maintenance; simpler than full ranking RL but still nontrivial ops.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First successful industrial Batch RL application to MTF for long-term satisfaction; Conservative-OPEstimator; mixed multi-exploration for batch data enrichment.

**Prior work comparison:** Contrasts with BO/ES MTF tuning, online RL harm to UX, standard off-policy deadly triad; builds on BCQ, CQL, TD3, PLE MTL.

**Verification:** MTF-as-RL is a clear framing; BCQ for continuous fusion weights is a natural fit; novelty is primarily industrial integration and OPE protocol.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Tencent short-video recommendation logs | Not public | No | 3.142M sessions, 11.155M interactions |

**Offline experiment reproducibility:** Not reproducible without Tencent data; methodology and hyperparameters are documented.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Optimizes long-term user satisfaction via session cumulative reward; instant metrics (play time, integrity, interactions) weighted to correlate with future app dwell time—not single CTR optimization.

**(2) Credit assignment:** Session MDP: each timestep recommends item(s) using fusion weights; instant reward from user feedback on that exposure; state updates from profile + last 500 watched videos; discounted sum over session.

**(3) Label and horizon definitions:** Per-step instant feedback vector; reward weights from offline regression vs. future dwell time; discount γ=0.95 for long-term returns; training on logged sessions with 90/10 chronological split; no explicit retention horizon label stated beyond dwell-time correlation.

**(4) Short-term + long-term heads:** Fixed PLE MTL heads produce task scores; learned personalized fusion weights α via Batch RL (logarithmic combination)—learned fusion layer on top of short-horizon task predictions.

**(5) Prediction vs incrementality:** Policy learning for fusion weights maximizing long-term return; predicts Q-values for state-action pairs under fusion policy rather than direct outcome regression.

**(6) Offline and online evaluation:** Conservative-OPEstimator on 10% holdout sessions; one-month online A/B with ADTime and UPIRate; delayed retention via dwell proxies; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Retains existing MTL (PLE) and replaces static/greedy MTF (grid search, BO) with BatchRL-MTF optimizing long-horizon fusion weights from logs plus controlled online exploration.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Qihua Zhang, Junning Liu, Yuzhuo Dai, Yiyan Qi, Yifan Yuan, Kunlun Zheng, Fan Huang, Xianfeng Tan
**Affiliations:** Tencent Inc.
**Venue:** KDD (arXiv:2208.06942)
**Year:** 2022
**PDF:** available at arXiv link above
**Relevance:** Core
**Priority:** 1
