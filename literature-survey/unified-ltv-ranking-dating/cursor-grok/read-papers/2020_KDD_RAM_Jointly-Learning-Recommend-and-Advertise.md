# Paper Analysis: Jointly Learning to Recommend and Advertise

**Source:** https://arxiv.org/abs/2003.00097
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Jointly Learning to Recommend and Advertise
- **authors or company:** Xiangyu Zhao, Xudong Zheng, Xiwang Yang, Xiaobing Liu, Jiliang Tang (Michigan State University; ByteDance)
- **venue:** KDD
- **year:** 2020
- **URL:** https://arxiv.org/abs/2003.00097
- **source type:** industry paper
- **direction:** D1/D7
- **problem setting:** Mixed recommendation–advertising feeds (e-commerce, news, short video): RS and AS optimized separately by different teams/metrics, causing suboptimal trade-off between immediate ad revenue and user experience; RAM jointly optimizes rec-list generation and ad insertion in a two-level MDP.
- **objective and label definition:** RS reward: session dwell time (minutes) on recommended items — long-horizon engagement proxy with γ=0.95 discount; AS reward: 1 if user continues browsing after ad, 0 if leaves; immediate ad revenue revt(aas) from RTB/GSP bidding; horizon is session-level cumulative reward, not subscription LTV or delayed retention days.
- **long-term retention/revenue reward:** **Partial.** RS explicitly optimizes discounted cumulative session dwell time (long-run user experience); AS balances immediate advertising revenue against long-term browse continuation — not retention-day or revenue-per-user LTV labels.
- **prediction or incrementality:** RL policy optimization (two-level DQN) maximizing expected cumulative rewards; not causal incrementality of a single exposure on retention/revenue.
- **model architecture:** Level-1 cascading DQN (RS): GRU-encoded rec/ad histories + context → sequential selection of k=6 regular videos via shared-weight RNN Q-functions; Level-2 DQN (AS): value + advantage decomposition over ad-location pairs (insert or not, which ad, which slot); RAM-l linear trade-off vs RAM-n two-step selection; off-policy pre-training from logged behavior policy.
- **credit assignment:** MDP transition rewards at session timestep: dwell time attributed to rec-list, continuation binary reward to ad decision; discounted sum over session — not per-impression delayed retention attribution with counterfactual correction.
- **training data and counterfactual handling:** 1M TikTok sessions (Mar 2019), 70/30 chronological split; off-policy training from historical logs with replay buffer and behavior-policy actions; simulator for evaluation predicts dwell time, leave, and ad revenue from mixed lists.
- **offline and online evaluation:** Simulated online environment (not live A/B): session dwell time Rrs, session length Ras, session ad revenue Rrev vs W&D, DeepFM, GRU4Rec, DRQN baselines; p-values reported on simulator metrics.
- **reported gains:** RAM-l vs DRQN: Rrs 19.61±0.23 min (+3.26% improv. over DRQN baseline row), Ras 9.76±0.09 (+4.16%), Rrev 1.49±0.06 (+16.42%); RAM-n vs RAM-l: Rrev 1.56±0.07 (+4.70%, p=0.001), Rrs 19.49±0.16 (−0.61% vs RAM-l).
- **applicability note for a two-sided dating recommender:** Two-level RL framing for revenue-vs-experience trade-offs maps to mixing premium features, promoted profiles, or subscription upsells into match feeds while optimizing session-level engagement — structural analogue to D1 multi-objective fusion under D7 delayed session rewards.
- **applicability note for a two-sided dating recommender:** Evaluated on short-video rec–ads simulator only; no reciprocity, bilateral match outcomes, or dating-specific revenue labels — dwell-time reward is engagement proxy, not 7–30 day retention or subscription LTV.
- **unverified claims:** none

## 1. Summary

RAM proposes a two-level deep RL framework: a cascading DQN recommender generates a regular-content list optimizing discounted session dwell time, then a second DQN inserts at most one ad (whether, which, where) balancing immediate RTB revenue against continued browsing. Off-policy training uses TikTok session logs; evaluation uses a learned simulator. RAM-l and RAM-n outperform supervised and single-level RL baselines on simulated session engagement, length, and ad revenue.

## Project Relevance

Speaks to **Q1** (multi-objective fusion): explicit joint optimization of experience (dwell) and revenue (ads) in one MDP. Speaks to **Q7** indirectly via revenue-vs-experience tension. **Q3**: session-level rewards, not delayed retention labels. No reciprocity, match quality, or production online A/B — simulator-only evaluation limits transfer confidence for dating LTV ranking.

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Session dwell time + ad revenue + browse continuation. |
| **(2) Credit assignment** | RL discounted session rewards; no IPS/DR. |
| **(3) Label / horizon; delay / sparsity / censoring** | Session-level dwell and leave signals; not multi-day retention. |
| **(4) Short-term vs long-term head fusion** | Two-level policies fuse rec and ad objectives via RL. |
| **(5) Prediction vs incrementality** | RL policy optimization, not uplift modeling. |
| **(6) Offline / online eval** | Simulator only; no live platform A/B reported. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Revenue vs experience trade-off explicit; reciprocity not modeled. |
| **(8) CTR → unified long-term migration** | Not specified in source. |

## Meta Information

**Authors:** Xiangyu Zhao et al.  
**Affiliations:** Michigan State University; ByteDance  
**Venue:** KDD 2020  
**DOI:** https://doi.org/10.1145/3394486.3403384  
**Relevance:** Peripheral (D1 revenue–experience joint optimization)  
**Priority:** 3
