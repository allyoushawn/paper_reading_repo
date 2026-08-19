# Paper Analysis: AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems

**Source:** https://arxiv.org/abs/2310.03984
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems
- **authors or company:** Zhenghai Xue, Qingpeng Cai, Bin Yang, Lantao Hu, Peng Jiang, Kun Gai (Nanyang Technological University / Kuaishou)
- **venue:** WWW
- **year:** 2025
- **URL:** https://doi.org/10.1145/3696410.3714956
- **source type:** industry paper
- **direction:** D2
- **problem setting:** Short-video recommendation under non-stationary user behavior where interaction rates and retention propensities drift, causing RL policy and reward distribution shift.
- **objective and label definition:** Retention reward at episode end: r = λ × user return time (zero at other steps); return time is the gap until the user returns to the platform; optimizes long-horizon accumulated return in MDP sessions—not immediate CTR alone.
- **prediction or incrementality:** Actor-critic RL policy selects top-k items from candidate pool; state-abstraction module signals environment drift to adapt policy; guarded exploration via performance-based rejection sampling—not explicit uplift estimation.
- **model architecture:** Policy network with state-abstraction submodule trained by value-based contrastive loss aligned to estimated policy performance; guarded online exploration module with rejection sampling; compared against DDPG, TD3, SAC, RLUR, ESCP, etc.
- **credit assignment:** Session-level retention reward assigned to last step of episode; immediate click/like/comment rewards at intermediate steps in live evaluation; sparse delayed return-time signal drives long-horizon credit.
- **training data and counterfactual handling:** KuaiSim retention simulator (50K training steps, 5 seeds); modified MovieLens-1M with synthetic retention rewards from ratings; live short-video platform A/B for two weeks vs RLUR baseline—no IPS/off-policy correction described for live data.
- **offline and online evaluation:** Simulator: average return days (↓), return rate at Day 1 (↑), retention reward (↑). MovieLens offline ranking metrics. Live A/B: 7d retention rate, dwell time, CTR, like/comment/unlike rates vs RLUR/TD3/ESCP.
- **reported gains:** KuaiSim: AURO 1.531±0.058 average return days vs RLUR 1.794±0.070; Day-1 return rate 0.824±0.018 vs RLUR 0.731±0.026; retention reward −0.015±0.000 vs RLUR −0.018±0.000. Live vs RLUR: 7d retention +0.138‰, dwell time +0.263‰, CTR +3.260‰, comment rate +8.392‰ (all permillage/percent improvements as reported).
- **applicability note for a two-sided dating recommender:** AURO's state-abstraction plus guarded exploration pattern is directly relevant when retention propensities drift and naive RL exploration would destabilize match-quality recommendations in a cost-sensitive live market.
- **applicability note for a two-sided dating recommender:** Single-sided consumer feed ranking with return-time reward only—no reciprocal match acceptance, counterparty congestion, or bilateral credit for delayed retention after a mutual match.
- **unverified claims:** none

## 1. Summary

**Title:** AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems
**Authors:** Zhenghai Xue, Qingpeng Cai et al. (NTU / Kuaishou)
**Abstract:** Introduces Adaptive User Retention Optimization with a policy-network state-abstraction module trained by value-based contrastive loss to detect environment drift, plus performance-guarded exploration for stable online adaptation under non-stationary retention dynamics.

**Key contributions:**
- State abstraction reflecting environment shifts via policy-performance-aligned loss.
- Guarded exploration with rejection sampling for implicit cold-start under drift.
- Evaluation on KuaiSim simulator, MovieLens, and live short-video A/B.

**Methodology:** RL session MDP with return-time terminal reward; actor-critic training; ablations on abstraction and exploration modules.

**Main results:** Best simulator retention metrics among baselines; live A/B improves all reported metrics vs RLUR including dwell time (only method to do so).

## 2. Experiment Critique

**Design:** Simulator, offline MovieLens, and two-week live A/B cover offline-to-online spectrum; ablations on exploration and state abstraction.

**Statistical validity:** Five random seeds in simulator; live metrics reported as permillage/percent lifts with standard errors in Table 4.

**Online experiments (if any):** Two-week continuous live experiment vs RLUR, TD3, ESCP on short-video platform.

**Reproducibility:** KuaiSim and MovieLens settings described; live data proprietary.

**Overall:** Strong industry RL-for-retention story with rare live validation; MovieLens retention reward is synthetic.

## 3. Industry Contribution

**Deployability:** Deployed in live short-video recommendation; state abstraction adds module to policy network without full re-architecture.

**Problems solved:** RL policy degradation under environment non-stationarity; unsafe exploration hurting comment/dwell metrics in live systems.

**Engineering cost:** Extra abstraction training and guarded exploration logic atop existing RLUR-style retention RL stack.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Value-based state abstraction for drift detection plus guarded exploration for retention RL under non-stationarity.

**Prior work comparison:** Contrasts with RLUR, TD3/SAC, ESCP context encoders, and standard exploration methods (OAC, RND).

**Verification:** Simulator and live tables support superiority claims; abstraction ablation shows largest drop when removed.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| KuaiSim retention simulator | NeurIPS 2023 | Partial | Simulator code/settings |
| MovieLens-1M (modified) | GroupLens | Yes | Synthetic retention rewards |
| Kuaishou live traffic | Proprietary | No | Two-week A/B |

**Offline experiment reproducibility:** Partial on public simulator/MovieLens; live not reproducible.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Primary retention objective via return-time terminal reward; immediate engagement metrics monitored in live eval.

**(2) Credit assignment:** Terminal session return-time reward to last action; intermediate engagement in live metrics—not item-level delayed match outcome.

**(3) Label and horizon definitions:** Return time until next session (hours–days); Day-1 return rate; 7d retention in live A/B; sparse terminal reward.

**(4) Short-term + long-term heads:** Single RL policy optimizing delayed retention reward with immediate feedback as auxiliary live metrics—not separate supervised LTV head.

**(5) Prediction vs incrementality:** Learns policy maximizing expected return under drift; not causal effect of showing a specific candidate on mutual match retention.

**(6) Offline and online evaluation:** KuaiSim + MovieLens offline; two-week live A/B with retention/dwell/CTR/comment metrics; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source (single-sided feed).

**(8) Migration path from CTR-like model:** RLUR-style retention RL augmented with drift-aware abstraction and safe exploration—migration from myopic engagement RL toward adaptive retention optimization.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Zhenghai Xue, Qingpeng Cai, Bin Yang, Lantao Hu, Peng Jiang, Kun Gai
**Affiliations:** Nanyang Technological University; Kuaishou Technology
**Venue:** WWW 2025
**Year:** 2025
**PDF:** https://arxiv.org/pdf/2310.03984.pdf
**Relevance:** Core
**Priority:** 1
