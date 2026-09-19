# Reinforcing User Retention in a Billion Scale Short Video Recommender System

**Source:** https://arxiv.org/pdf/2302.01724 | **NLM source id:** 21bf4037-1292-40df-a0db-714075d0f41c | **Year / venue:** WWW 2023, Austin | **Affiliation:** Kuaishou Technology | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Retention is a long-term feedback signal from multiple cross-session interactions; the authors state directly that "it is hard to decompose retention reward to each item or a list of items," so point-wise/list-wise models cannot optimize it. RLUR formulates retention optimization as an infinite-horizon, request-based MDP that minimizes cumulative returning time between sessions. **Unit of credit:** per request/step — the agent outputs an 8-dimensional continuous action ensembling weights over 8 scoring models (watchtime, like, follow, etc.) to rank videos; there is no per-item or per-swipe fractional attribution. **Outcome optimized:** app-open frequency / user retention, via minimizing cumulative discounted returning time. **Bias handling:** (uncertainty) a session-level classifier predicts expected returning time and normalizes the raw reward against it to strip out external noise; (activity bias) separate policies are trained for high-activity vs. low-activity user cohorts so power users don't dominate the gradient — this is the paper's explicit selection-bias mitigation; (long delay) a soft density-ratio regularization down-weights actor-loss updates for samples with large behavior/current-policy divergence.

## 2. Evidence
Offline: KuaiRand-based simulator vs. CEM and TD3 — RLUR achieves returning time 1.892 (vs. CEM 2.036, TD3 2.009) and 1st-day retention 0.618 (vs. 0.587/0.592). Live A/B on Kuaishou (billion-scale, 150+ days, RLUR vs. production CEM): app-open frequency +0.450%, DAU +0.20%, 1st-day retention +0.053%, 7th-day retention +0.063% — the authors note +0.01% retention / +0.1% DAU are considered statistically and practically significant at this scale.

## 3. Limitations
Standard off-policy TD3 is unstable/diverges under the multi-hour return-time distribution shift and was excluded from live comparison. The discount factor must be fixed at 1 for non-terminal intra-session steps or the returning-time reward vanishes exponentially. Retention is heavily affected by exogenous factors (social events, weekday/weekend) that add irreducible noise. Balancing immediate vs. retention critics requires careful hyperparameter tuning; over-weighting immediate feedback degrades retention gains.

## 4. Prior works named
- Lillicrap et al. (2015) / Fujimoto et al. (2018) — DDPG / TD3 (RL backbone)
- Burda et al. (2018) — Random Network Distillation (exploration)
- Wu et al. (2017) — Returning is Believing: Optimizing long-term user engagement
- Gao et al. (2022) — KuaiRand: unbiased sequential recommendation dataset
- Fujimoto & Gu (2021) — TD3+BC: a minimalist approach to offline RL

## 5. Project Relevance
- **Answers:** Q2 adjacent
- **Attributes retention to individual interactions?** Partly — a Retention Critic estimates step-wise expected retention value via TD learning, so each request gets an implicit value estimate, but RLUR is an online policy-optimization framework, not an offline credit-decomposition model that produces per-swipe fractional labels.
- **Transferable components:** framing N7 as minimizing/predicting a time-to-return target; uncertainty normalization (dividing observed by predicted return time) to strip organic/exogenous noise; activity-based cohort stratification to prevent power-swiper selection bias; dual critic (long-term + immediate) architecture.
- **Required changes:** RLUR's action space is a per-request ensembling weight vector over homogeneous video-scoring models — a dating platform needs per-candidate-profile exposure evaluation across heterogeneous funnel actions (swipe/match/message) with corresponding state/event encoders, and the session-gap reward must be re-anchored to a rolling daily N7 active indicator.
- **On last-touch:** Not named explicitly, but the paper states outright that retention "is difficult to decompose... to each item," which is the core argument against assigning full credit to the most recent (last-touch) swipe.
- **Transfer rating:** adaptable — the uncertainty-normalization and cohort-stratification debiasing techniques are directly reusable for isolating incremental retention lift from organic swiping.
