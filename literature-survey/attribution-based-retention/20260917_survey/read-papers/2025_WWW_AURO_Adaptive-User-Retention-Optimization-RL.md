# AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems

**Source:** https://arxiv.org/pdf/2310.03984.pdf | **NLM source id:** ad961918-6d05-4369-a28d-7180ccf96629 | **Year / venue:** WWW 2025 (ACM Web Conference 2025) | **Authors / affiliation:** Zhenghai Xue (NTU Singapore), Qingpeng Cai* (Kuaishou Technology, corresponding), Bin Yang, Lantao Hu, Peng Jiang (Kuaishou Technology), Kun Gai (Unaffiliated), Bo An (NTU Singapore & Skywork AI) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Standard RL struggles to optimize user retention in production recommenders because of environment non-stationarity: user behavior (immediate feedback rates, return-time distributions) drifts daily/hourly, causing dynamics and reward shift, plus an implicit cold-start problem where the policy keeps meeting novel behavior patterns and must explore safely. AURO addresses this with (1) a value-based state abstraction module φ(s), trained via a contrastive loss that aligns abstraction distances with state-value V(s) differences so the network detects non-stationarity without hand-crafted rules, and (2) rejection-sampled guarded exploration, combining optimism under uncertainty (Q_UB = μ_Q + βσ_Q) with rejection sampling over candidate actions to filter out low-value exploratory actions that could trigger churn.

Unit of credit: per recommendation step/action a_t (a continuous scoring vector over candidate items) within a Hidden Parameter MDP (HiP-MDP) where latent parameters θ govern transition/reward dynamics T_θ, r_θ. Outcome optimized: a retention reward r_ret = λ × user return time, assigned at the terminal step of an episode, alongside 1-day/7-day retention, dwell time, and immediate feedback (CTR, like, comment, hate). Selection/confounding bias is not addressed via causal correction — it is handled implicitly through the HiP-MDP formulation (modeling non-stationary user state) and guarded exploration (avoiding actions likely taken only by already-engaged users' idiosyncratic tastes), not through explicit debiasing.

## 2. Evidence
- **KuaiSim retention simulator:** cross-session simulator of leave/return-time distributions. AURO: Average Return Days = 1.531±0.058 (vs. RLUR 1.706, ESCP 1.705, TD3 1.772, SAC 1.810); Return Rate Day 1 = 0.824±0.018 (vs. RLUR 0.765); Retention Reward = -0.015±0.000 (vs. RLUR -0.017).
- **MovieLens-1M** (5,000 train / 1,040 test users, ratings mapped to retention rewards): AURO+BC Retention Reward = 1.798±0.032 (vs. RLUR+BC 1.784, ESCP+BC 1.755, TD3+BC 1.714, BC 1.702).
- **Live A/B test on Kuaishou** (2 weeks, ~25M DAU): 7-day retention +0.138‰±0.089 (vs. ESCP +0.123‰, TD3 +0.041‰); dwell time +0.263‰±0.181 (only algorithm with positive dwell lift); CTR +3.260‰±0.332; like rate +2.821‰±0.925; comment rate +8.392‰±1.881; hate/unlike rate -1.874%±0.781 (significant drop).
- Baselines: CEM, DIN, DDPG, TD3, SAC, OAC, RND, ESCP, OSPIA, RL-LTV, RLUR.

## 3. Limitations
- No explicit joint multi-objective formulation trading off delayed retention against immediate feedback (clicks/likes).
- State abstraction can fail to adapt under extreme/unprecedented user behavior (e.g., sudden blanket disliking).
- For "stubborn" users who refuse novel content, optimistic exploration can underperform a purely greedy strategy.
- Action-selection computation overhead: +129% action-selection time (still <10% of total training step time; zero added cost at serving).

## 4. Prior works named
- Cai et al. 2023, RLUR — *Reinforcing User Retention in a Billion Scale Short Video Recommender System* (foundational MDP formulation for retention optimization)
- Doshi-Velez & Konidaris 2016 — *Hidden Parameter Markov Decision Processes* (HiP-MDP formalism)
- Luo et al. 2022, ESCP — *Adapt to Environment Sudden Changes by Learning a Context Sensitive Policy* (context-encoder Meta-RL baseline)
- Ciosek et al. 2019, OAC — *Better Exploration with Optimistic Actor Critic* (optimism-under-uncertainty exploration)
- Fujimoto et al. 2018, TD3 — *Addressing Function Approximation Error in Actor-Critic Methods* (actor-critic backbone)

## 5. Project Relevance
- **Answers:** Q2
- **Attributes retention to individual interactions?** partly — AURO learns Q(s,a)/V(s) to value recommendation actions toward retention, but does not compute explicit fractional multi-touch attribution credit across historical swipe/like/match events; it's a policy-optimization framework, not an attribution model.
- **Transferable components:** value-based state abstraction φ(s) for detecting engagement-state shifts (e.g., highly-active vs. churn-risk users) that could gate candidate-profile scoring; guarded/rejection-sampled exploration to avoid surfacing low-value candidates that risk churn.
- **Required changes:** convert from online RL policy control to offline supervised sequence attribution — Q-values/state abstractions would need to become counterfactual credit differentials per swipe; action space must move from continuous scoring vectors to heterogeneous discrete touch types (swipe, like, match, message).
- **On last-touch:** does not explicitly critique last-touch/last-click attribution, but shows myopic optimization of immediate feedback (clicks/likes) fails to maximize long-term retention and can increase churn — supporting the case against last-touch-only credit.
- **Transfer rating:** adaptable — an RL policy-optimization algorithm rather than a multi-touch attribution model, but its value-based state abstraction and guarded Q-estimation are adaptable building blocks for valuing candidate-profile impact on retention.
