# Paper Analysis: EnhancedRL: An Enhanced-State Reinforcement Learning Algorithm for Multi-Task Fusion in Recommender Systems

**Source:** https://arxiv.org/abs/2409.11678
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** EnhancedRL: An Enhanced-State Reinforcement Learning Algorithm for Multi-Task Fusion in Recommender Systems
- **authors or company:** Peng Liu, Cong Xu, Jiawei Zhu, Ming Zhao, Bin Wang (Tencent)
- **venue:** CIKM 2024 (arXiv:2409.11678)
- **year:** 2024
- **URL:** https://arxiv.org/abs/2409.11678
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Same industrial RS MTF stage as UnifiedRL; prior RL-MTF methods use only user-level features as state and output one fusion-weight action for all candidates—cannot leverage item features or MTL predictions per candidate.
- **objective and label definition:** Maximize session cumulative reward G_t with discount γ; per user–item pair instant reward r(s_{tj}, a_{tj}) = Σ w_i · v_i (watch time, valid consumption >10s, like/share/collect); list reward r(s_t, a_t) = Σ_j r(s_{tj}, a_{tj}); fusion via final_score = Π_i (pred_score_i + bias_i)^power_i with per-pair 10-D action vector.
- **prediction or incrementality:** Offline RL actor–critic with enhanced state (user + item + MTL predictions + context) outputs per user–item fusion weights—policy optimization, not pointwise outcome prediction.
- **model architecture:** EnhancedRL actor (PLE-like MLP) and q=2 critic sets × m=10 critics; hierarchical state = user features + item features + MTL outputs per candidate; TD loss aggregates Q over l=5 items in list; adopts UnifiedRL bounded uniform exploration (±0.15) and progressive training; deployed since September 14, 2023.
- **credit assignment:** Per user–item pair state and action; critics aggregate list-item Q-values and rewards for TD update; session-level cumulative reward—item-granular fusion weights vs UnifiedRL’s single user-level action.
- **training data and counterfactual handling:** ~2M users per exploration group from industrial RS; references UnifiedRL comparison results for prior methods; offline NCIS + MTF-GAUC; online A/B vs UnifiedRL baseline.
- **offline and online evaluation:** Offline vs UnifiedRL: cumulative reward 56.13 vs 53.98, MTF-GAUC 0.8037 vs 0.7954; online 1-week A/B vs UnifiedRL: UVC +3.84%, UDT +0.58% (p < 0.05); higher compute than UnifiedRL but acceptable for deployment.
- **reported gains:** Online vs UnifiedRL: +3.84% user valid consumption, +0.58% user duration time; offline MTF-GAUC 0.8037 vs UnifiedRL 0.7954; fully deployed in large-scale RS.
- **applicability note for a two-sided dating recommender:** Per-candidate fusion weights using profile + candidate features enable different utility tradeoffs for high- vs low-competition profiles—closer to item-level ranking needed when candidate pools are heterogeneous.
- **applicability note for a two-sided dating recommender:** Still optimizes one-sided engagement rewards within a session; no reciprocal match probability, receiver capacity constraints, or bilateral fairness in state/reward design.
- **unverified claims:** none

## 1. Summary

**Title:** EnhancedRL: An Enhanced-State Reinforcement Learning Algorithm for Multi-Task Fusion in Recommender Systems
**Authors:** Peng Liu, Cong Xu, Jiawei Zhu, Ming Zhao, Bin Wang (Tencent)
**Abstract:** Extends RL-MTF from user-level to user–item-pair granularity by introducing enhanced states (user + item + MTL predictions) and redesigned actor–critic with list-aggregated TD learning.

**Key contributions:**
- Identifies limitation of user-level-only RL-MTF state/action paradigm.
- Hierarchical enhanced state per candidate; separate 10-D fusion action per user–item pair.
- Novel critic TD update summing Q and rewards across list items.
- Builds on UnifiedRL exploration and progressive training.

**Methodology:** Same fusion formula and session MDP as UnifiedRL; actor/critic penalties using exploration bounds; MLP networks with Adam, batch 256, 300k epochs.

**Main results:** Online +3.84% UVC and +0.58% UDT over UnifiedRL; offline MTF-GAUC 0.8037 vs 0.7954.

## 2. Experiment Critique

**Design:** Experiment one reuses UnifiedRL comparisons (ES, DDPG, CQL+SAC, BatchRL-MTF, IQL); experiment two head-to-head vs UnifiedRL on same test set.

**Statistical validity:** Online p < 0.05; one-week A/B.

**Online experiments (if any):** UnifiedRL as production baseline; EnhancedRL requires more online resources but deemed acceptable.

**Reproducibility:** Proprietary Tencent data; stream-clustering augmentation extension tested but excluded from reported comparison.

**Overall:** Demonstrates value of item-level state in MTF; engagement rewards still short of retention/LTV.

## 3. Industry Contribution

**Deployability:** Fully deployed since September 14, 2023 in large-scale RS.

**Problems solved:** Suboptimal user-level-only fusion weights when candidates differ in MTL predictions and item features.

**Engineering cost:** Higher serving compute than UnifiedRL (per-pair actions); q=2, m=10 critic ensembles.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First RL-MTF with user–item-pair enhanced state and per-candidate actions; hierarchical state concept.

**Prior work comparison:** UnifiedRL, BatchRL-MTF, DDPG, CQL+SAC, IQL, ES.

**Verification:** Direct successor to UnifiedRL (same team, same fusion formula); incremental but meaningful online lift over strong baseline.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Tencent industrial RS exploration logs | Not public | No | ~2M users per group |

**Offline experiment reproducibility:** Not reproducible without proprietary data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Session-level cumulative reward over engagement behaviors (watch time, valid consumption, interactions)—within-session long-term optimization, not subscription retention.

**(2) Credit assignment:** Per user–item pair state, action, and instant reward; list reward sums pairs; critic TD aggregates across l=5 videos—finer credit than user-level single action.

**(3) Label and horizon definitions:** Immediate per-item behaviors; session discount; valid consumption >10s; subscription-level delay not in reward.

**(4) Short-term + long-term heads:** MTL pred_score_i inputs to enhanced state; RL learns per-pair fusion weights toward session reward—learned item-conditional fusion.

**(5) Prediction vs incrementality:** Policy optimization via actor–critic RL.

**(6) Offline and online evaluation:** NCIS + MTF-GAUC offline; 1-week online A/B vs UnifiedRL; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Extends UnifiedRL RL-MTF with item-aware states/actions—migration from user-level to pair-level fusion without replacing MTL ranker.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Peng Liu, Cong Xu, Jiawei Zhu, Ming Zhao, Bin Wang
**Affiliations:** Tencent Inc., Beijing
**Venue:** CIKM 2024
**Year:** 2024
**PDF:** https://arxiv.org/pdf/2409.11678.pdf
**Relevance:** Core
**Priority:** 1
