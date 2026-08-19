# Paper Analysis: UnifiedRL: A Reinforcement Learning Algorithm Tailored for Multi-Task Fusion in Large-Scale Recommender Systems

**Source:** https://arxiv.org/abs/2404.17589
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** UnifiedRL: A Reinforcement Learning Algorithm Tailored for Multi-Task Fusion in Large-Scale Recommender Systems
- **authors or company:** Peng Liu, Cong Xu, Ming Zhao, Jiawei Zhu, Bin Wang, Yi Ren (Tencent)
- **venue:** CIKM 2024 (arXiv:2404.17589)
- **year:** 2024
- **URL:** https://arxiv.org/abs/2404.17589
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Industrial RS three-stage funnel (candidate generation → MTL ranking → MTF); MTF combines MTL behavior scores into final ranking via fusion formula; session defined as user access until exit with sequential recommendations influencing future steps.
- **objective and label definition:** RL maximizes discounted cumulative session reward G_t = Σ γ^i r(s_{t+i}, a_{t+i}); instant reward r(s_t, a_t) = weighted sum over list items of watch time, valid consumption (>10s), like/share/collect, etc.; action a is 10-D fusion weight vector (power/bias terms) for final_score = Π_i (pred_score_i + bias_i)^power_i; γ = 0.9.
- **prediction or incrementality:** Offline RL actor–critic learns fusion-weight policy maximizing session cumulative reward—policy optimization over logged exploration data, not pointwise outcome prediction.
- **model architecture:** UnifiedRL integrates offline actor–critic with custom bounded uniform exploration policy (baseline policy + ε ~ U(b_l, b_u), typically ±0.15); actor/critic MLPs (PLE-like actor); q=2 critic sets × m=24 critics each; penalty terms relax OOD constraints using known exploration bounds; progressive training mode with 5 exploration/training rounds.
- **credit assignment:** User-level state (profile + behavior sequence + stats); single fusion-weight action per request applied to all candidates via Eq. 1; instant reward summed over full recommendation list l items; session-level discounted cumulative reward—no per-item fusion weights.
- **training data and counterfactual handling:** Exploration data from ~2M users × 3 groups, ~6.8M sessions per dataset, 5-day collection; compared Gaussian-noise vs bounded uniform exploration; offline evaluation via NCIS cumulative reward and MTF-GAUC; deployed since June 2023.
- **offline and online evaluation:** Offline: NCIS cumulative reward (UnifiedRL 53.96 vs IQL 52.39) and MTF-GAUC (0.7953 vs ES 0.7836); online 1-week A/B vs ES: UVC +4.64%, UDT +1.74% (p < 0.05); valid consumption = videos watched >10s per user per day.
- **reported gains:** Online vs ES: +4.64% user valid consumption, +1.74% user duration time; offline MTF-GAUC 0.7953 vs ES 0.7836; deployed in multiple Tencent RSs plus search and ads.
- **applicability note for a two-sided dating recommender:** RL-MTF over existing MTL heads is a practical path to optimize session-level engagement toward retention without retraining swipe/match predictors—fusion weights adapt per user state.
- **applicability note for a two-sided dating recommender:** User-level single action for all candidates ignores item/candidate heterogeneity and bilateral match reciprocity; reward is watch/engagement weighted, not match quality or receiver-side congestion.
- **unverified claims:** none

## 1. Summary

**Title:** UnifiedRL: A Reinforcement Learning Algorithm Tailored for Multi-Task Fusion in Large-Scale Recommender Systems
**Authors:** Peng Liu, Cong Xu, Ming Zhao, Jiawei Zhu, Bin Wang, Yi Ren (Tencent)
**Abstract:** Proposes UnifiedRL, an offline RL algorithm for MTF that unifies a custom bounded exploration policy with actor–critic training, relaxing overly strict OOD constraints and enabling progressive online–offline iteration.

**Key contributions:**
- Identifies three flaws in prior RL-MTF: strict OOD constraints, exploration/training decoupling, inefficient exploration.
- Custom exploration policy ~2^10× more efficient than Gaussian noise for 10-D actions.
- Actor/critic penalties using known per-user exploration bounds instead of BCQ-style strict action matching.
- Progressive training: 5 rounds of exploration + offline training.

**Methodology:** MDP over recommendation sessions; 10-D continuous fusion-weight actions; instant reward over behavior-weighted list outcomes; MLP actor/critic with ensemble critics and soft target updates.

**Main results:** Online +4.64% UVC and +1.74% UDT vs ES; offline UnifiedRL cumulative reward 53.96 and MTF-GAUC 0.7953.

## 2. Experiment Critique

**Design:** Industrial A/B vs ES and offline RL baselines (DDPG, CQL+SAC, BatchRL-MTF, IQL); no public dataset.

**Statistical validity:** Online improvements p < 0.05; one-week A/B.

**Online experiments (if any):** One-week deployment in large-scale RS; ES production baseline.

**Reproducibility:** Proprietary Tencent traffic only; hyperparameters listed but data unavailable.

**Overall:** Strong industrial evidence for RL-MTF; user-level action limits item-specific optimization addressed by follow-on EnhancedRL.

## 3. Industry Contribution

**Deployability:** Deployed since June 2023 across multiple Tencent RSs, search, and advertising.

**Problems solved:** Long-term session reward optimization in MTF stage; efficient exploration for frequent policy iteration.

**Engineering cost:** Online exploration + offline training loops, ensemble critics (2×24), progressive multi-round data collection.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First RL algorithm tailored for MTF; unified exploration + offline RL framework; progressive training mode.

**Prior work comparison:** BatchRL-MTF (BCQ), DDPG, CQL+SAC, IQL, ES, Grid Search, Bayesian Optimization.

**Verification:** Builds directly on BatchRL-MTF (Zhang et al. KDD 2022); main advance is exploration-aware constraint relaxation and progressive training.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Tencent industrial RS exploration logs | Not public | No | ~6.8M sessions per dataset, 3 groups |

**Offline experiment reproducibility:** Not reproducible without proprietary data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Session-level cumulative reward over engagement behaviors (watch time, valid consumption, interactions)—long-term within-session optimization; not subscription retention directly.

**(2) Credit assignment:** User-level fusion weights applied to all candidates; list-level instant reward summed over l items; session MDP with discount γ=0.9—item-level credit via list reward only.

**(3) Label and horizon definitions:** Instant behaviors per recommendation step; session terminal at user exit; exploration data collected over 5 days; delayed subscription retention not used as reward.

**(4) Short-term + long-term heads:** MTL provides pred_score_i; RL learns fusion weights combining heads toward session cumulative reward—learned fusion via RL policy, not fixed utility weights.

**(5) Prediction vs incrementality:** Policy optimization (actor–critic RL) over exploration logs—not pointwise prediction of outcomes.

**(6) Offline and online evaluation:** NCIS + MTF-GAUC offline; 1-week online A/B on UVC/UDT; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Keep MTL ranker; add RL-MTF layer learning personalized fusion weights for long-term session reward—explicit production migration path described.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Peng Liu, Cong Xu, Ming Zhao, Jiawei Zhu, Bin Wang, Yi Ren
**Affiliations:** Tencent Inc., Beijing
**Venue:** CIKM 2024
**Year:** 2024
**PDF:** https://arxiv.org/pdf/2404.17589.pdf
**Relevance:** Core
**Priority:** 1
