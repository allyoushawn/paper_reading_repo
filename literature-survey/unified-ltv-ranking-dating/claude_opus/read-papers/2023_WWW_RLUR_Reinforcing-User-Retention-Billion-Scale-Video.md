# Paper Analysis: Reinforcing User Retention in a Billion Scale Short Video Recommender System

**Source:** https://arxiv.org/abs/2302.01724 (Cai et al., WWW 2023 Companion Proceedings / RLUR)
**Date analyzed:** 2026-08-16

## 1. Summary

**Title:** Reinforcing User Retention in a Billion Scale Short Video Recommender System
**Authors:** Qingpeng Cai, Zhenghai Xue, Chi Zhang, Wanqi Xue, Shuchang Liu, Ruohan Zhan, Xueliang Wang, Tianyou Zuo, Wentao Xie, Dong Zheng, Peng Jiang, Kun Gai (Kuaishou Technology; Kun Gai listed as unaffiliated)
**Venue:** Companion Proceedings of the ACM Web Conference 2023 (WWW '23), Austin, Texas, USA

**Abstract (paraphrased from source):** Short-video platforms optimize recommendations to drive user retention and DAU growth, but retention is a long-term feedback signal that follows multiple user–system interactions and is hard to decompose down to a single item or list of items — traditional pointwise and listwise models cannot optimize it directly. The paper formulates user retention as an infinite-horizon, request-based Markov Decision Process whose objective is to minimize the accumulated time interval between sessions (equivalent to maximizing app-open frequency and retention), and proposes RLUR to address the uncertainty, bias, and long delay that make naive RL unstable in this setting. RLUR was fully launched in the Kuaishou app and produced consistent retention and DAU gains.

**Key contributions:**
1. An infinite-horizon, request-based MDP formulation whose objective is directly the accumulated inter-session return time, rather than a proxy engagement signal.
2. RLUR, a system combining a retention critic, an immediate-response critic, uncertainty normalization, activity-based bias mitigation, and a soft behavior-regularization method for the long-delay off-policy instability problem.
3. A long-term, large-scale live production deployment on Kuaishou with reported consistent retention and DAU gains.

**Methodology.** The MDP models the recommender as the agent and users as the environment. A session begins when a user opens the app; at each request (step) i_t within session i, the agent outputs a continuous 8-dimensional action a_it — ranking weights that linearly ensemble the outputs of 8 existing deep models predicting individual feedback signals (watch time, short/long view, like, follow, forward, comment, personal-page entry). The system recommends the top 6 videos by the resulting ensembled score. The immediate reward I(s_it, a_it) is the sum of watch time and interaction counts on those 6 videos. The returning time T(s_i) is the gap between the last request of session i and the first request of session i+1; the returning-time reward is T(s_i) at the last request of a session and 0 elsewhere, and the objective is to minimize Σ γ^(i−1) T(s_i). Two DDPG-style critics are learned: a retention critic Q_T, whose Bellman target uses a discount factor of exactly 1 for non-terminal within-session steps and γ=0.95 only at a session's terminal step (preventing the returning-time signal from being exponentially decayed away before it reaches the request that actually caused the session's end); and an immediate-response critic Q_I, estimating the sum of immediate rewards plus a Random Network Distillation (RND) intrinsic-novelty bonus that encourages exploration of understudied states, kept in a separate critic specifically so it does not pollute the retention signal. Because returning time is highly uncertain (affected by factors outside the recommender, e.g., social events), the paper normalizes the raw returning-time reward using a session-level classifier T′ that predicts whether the returning time will fall below the β-th percentile threshold T_β of the empirical distribution, then applies a Markov-inequality lower bound to produce r(s_it, a_it) = clip{0, T(s_i) / ((1 − T′(x))·T_β), α}. Because high- and low-activity users have structurally different return habits, RLUR trains two separate actor policies, one per activity group, each minimizing a weighted combination of −Q_T and −Q_I. Because the multi-hour-to-multi-day delay between an action and its returning-time reward causes a much larger policy/behavior-policy distribution shift than instantaneous-reward RL settings — and the authors found that standard behavior-cloning regularization either failed to stabilize training or hurt sample efficiency — RLUR instead applies a soft regularization multiplier to the actor loss, exp(max{λ·(log p(a_it|s_it) − log p_b(a_it|s_it)), 0})·L(θ), which down-weights (rather than hard-constrains) gradient updates on samples with large distribution shift from the logged behavior policy.

**Main results.** Offline, on a simulator built from the public KuaiRand dataset, RLUR outperformed CEM, TD3, and two RLUR ablations on both returning time and 1st-day user retention (Table 1: RLUR 1.892 days / 0.618 retention, vs. CEM 2.036/0.587). Online, after full deployment on the Kuaishou app, RLUR converged (~Day 100) to a stable app-open-frequency gain of +0.450% over the CEM production baseline, with DAU +0.2%, 1st-day retention +0.053%, and 7th-day retention +0.063% — described by the authors as statistically significant at Kuaishou's scale.

## 2. Experiment Critique

**Design.** Offline evaluation uses a three-module simulator (immediate-feedback prediction, session-leave prediction, and a return-probability module spanning up to K=10 days) built on the public KuaiRand dataset, compared against CEM (the existing production baseline algorithm class), TD3 (a state-of-the-art continuous-control RL baseline), and two ablated RLUR variants (naive, γ=0 and naive, γ=0.9) that omit the paper's uncertainty-normalization, RND-exploration, and soft-regularization components. Online evaluation is a long-duration, randomized live split against the CEM production baseline; TD3 was excluded from the live test because the authors found its training too unstable to deploy.

**Statistical validity.** The offline Table 1 numbers are reported as the "averaged performance of the last 50 episodes" at convergence, without variance or a significance test. The online results are reported as converged percentage gaps over the CEM baseline (app open frequency +0.450%, DAU +0.2%, 1st-day retention +0.053%, 7th-day retention +0.063%) with the paper asserting, based on the platform's own internal convention, that "0.01% improvement of user retention and 0.1% improvement of DAU are statistically significant in short video platforms" — this is a stated significance threshold specific to Kuaishou's traffic volume, not a reported p-value or confidence interval for each individual metric.

**Online experiments.** This is the paper's central piece of evidence and its strongest claim to industrial relevance: a full, sustained production launch on a billion-scale app, tracked day-by-day from Day 0 to beyond Day 100, with a visible convergence curve rather than a single before/after snapshot.

**Reproducibility.** The MDP formulation, both critic losses, the uncertainty-normalization formula, the bias-mitigation split, and the soft-regularization actor loss are all given as explicit equations, and key hyperparameters are disclosed (γ=0.95, percentile threshold β=60%, upper bound α=3, regularization coefficient λ=1.5). However, the 8 underlying deep scoring models that produce the ensembled ranking inputs are not themselves specified, and the Kuaishou production traffic is proprietary — so exact replication is not possible outside Kuaishou, though the offline KuaiRand-based simulator provides a public partial substitute.

**Overall.** The paper's ablation design (RLUR vs. two "naive" RLUR variants that strip out individual components) is a genuine strength — it isolates the contribution of the multi-session discounting choice from the contribution of the uncertainty/exploration/regularization machinery. The main weakness, shared with much of this literature, is the absence of formal significance testing for the headline online percentages, which are instead judged against an internally stated significance convention for the platform.

## 3. Industry Contribution

**Deployability.** RLUR is engineered to slot into an existing multi-model ranking pipeline rather than replace it: the RL policy only learns an 8-dimensional continuous ensembling-weight vector over outputs from 8 pre-existing pointwise scoring models, so the action space stays small and continuous regardless of the catalog size, and the existing scoring models do not need to be retrained or replaced.

**Problems solved.** Converts an otherwise intractable "decompose a multi-session retention signal down to a single item" problem into a tractable request-level continuous-control problem, by having the agent only re-weight already-computed per-item scores rather than learning item selection directly.

**Engineering cost.** The production system now must serve and maintain two additional critics (Q_T, Q_I), a session-level returning-time classifier T′ for uncertainty normalization, an RND novelty network, and two parallel actor policies (one per user-activity segment) — roughly doubling the actor-serving surface relative to a single-policy design. The soft behavior-regularization term requires the logged behavior-policy's action density p_b(a|s) to be available at training time, which means the serving pipeline must log action propensities, an additional logging requirement beyond what a standard pointwise ranker needs.

## 4. Novelty vs. Prior Work

**Claimed novelty.** The paper states it is "one of the first works to directly optimize user retention in short video recommender systems to the best of [the authors'] knowledge," as opposed to prior RL-for-recommendation work that maximizes cumulative immediate feedback. Its specific technical novelty is the combination of session-terminal-only discounting, returning-time uncertainty normalization via a Markov-inequality bound, activity-based policy splitting, and soft (rather than hard) behavior regularization for the long-delay distribution-shift problem.

**Prior work named in the source (Query 2, part 3):**
- Lillicrap et al., "Continuous control with deep reinforcement learning," 2015 — the DDPG algorithm RLUR's critics are built on.
- Burda et al., "Exploration by random network distillation," 2018 — the RND intrinsic-reward method used in the immediate-response critic.
- Wu et al., "Returning is believing: Optimizing long-term user engagement in recommender systems," 2017 — cited for framing user return frequency as the ultimate satisfaction/retention metric.
- Covington et al., "Deep neural networks for YouTube recommendations," 2016 — cited as the representative pointwise deep-recommendation baseline paradigm.
- Silver et al., "Mastering the game of Go with deep neural networks and tree search," 2016 — cited by analogy to illustrate why a macroscopic, long-horizon reward (like Go's win/loss or retention) is hard to decompose to individual moves or items.
- Levine et al., "Offline reinforcement learning: Tutorial, review, and perspectives on open problems," 2020 — cited for the distribution-shift and delayed-reward instability this paper's soft regularization addresses.
- Fujimoto and Gu, "A minimalist approach to offline reinforcement learning," 2021 — cited regarding behavior-cloning-style regularization, which RLUR's soft regularization is positioned against.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| KuaiRand | Public, unbiased (random-exposure) short-video interaction log dataset | Public | Used to build a 3-module offline simulator (immediate feedback, session-leave, return-probability up to K=10 days) for the offline comparison in Table 1. |
| Kuaishou production traffic | Proprietary industrial live traffic | Not public | Source of the 100+ day live A/B deployment results (app open frequency, DAU, 1st/7th-day retention). |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Reinforcing User Retention in a Billion Scale Short Video Recommender System; Qingpeng Cai, Zhenghai Xue, Chi Zhang, Wanqi Xue, Shuchang Liu, Ruohan Zhan, Xueliang Wang, Tianyou Zuo, Wentao Xie, Dong Zheng, Peng Jiang, Kun Gai (Kuaishou Technology); WWW 2023 (Companion Proceedings); https://arxiv.org/abs/2302.01724 |
| 2 | Source type | Industry paper |
| 3 | Direction | D2 |
| 4 | Problem setting | Optimizing user retention — not just engagement — in a billion-scale short-video recommender, where retention is a multi-session, long-delay outcome that resists decomposition to a single item or list. |
| 5 | Objective and label definition | Minimize the cumulative discounted returning time Σ γ^(i−1) T(s_i) over an infinite-horizon, request-based MDP. T(s_i) = time gap between session i's last request and session i+1's first request; raw reward = T(s_i) at the session's terminal request only, 0 otherwise; normalized reward = clip{0, T(s_i)/((1−T′(x))·T_β), α}, where T′ is a session-level classifier predicting whether returning time falls under the β-percentile threshold T_β. Horizon: infinite, multi-session; discount γ=0.95 applied only at session-terminal steps (γ=1 within a session, to prevent the returning-time signal decaying to near-zero before reaching the causal request). Delay is handled via heuristic reward shaping (the immediate-response critic Q_I as a dense proxy signal) and soft behavior regularization; censoring (a user who never returns) is not mathematically modeled — the offline simulator simply caps its observation window at K=10 days. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. It learns two critics that predict expected cumulative returning time and expected immediate response; it does not estimate the causal effect of showing an item versus not showing it. Paper's own wording: "the ranking function f inputs the action a_it and the prediction scores x_j... outputs the ranking score f(a_it, x_j) for each video j." |
| 7 | Model architecture | Actor-critic (DDPG-style). State = user profile + 3-request behavior history + request context + candidate features. Action = continuous 8-dim ensembling-weight vector over 8 existing pointwise scoring models. Retention critic Q_T (session-terminal-discounted DDPG loss) and immediate-response critic Q_I (immediate reward + RND intrinsic bonus). Two separate actor policies for high- vs. low-activity user segments, each trained with a soft behavior-regularization multiplier on the actor loss. |
| 8 | Credit assignment | Session/request-level, not item-level. The returning-time reward attaches to the ensembling decision made at a session's last request, not to any individual video within the 6-video slate; the paper explicitly states retention "is hard to decompose... to each item or a list of items," and does not attempt that decomposition — it works around it by ensembling existing item-level scores rather than assigning credit to items directly. |
| 9 | Training data and counterfactual handling | Off-policy training on logged production trajectories generated under a prior behavior policy p_b(a\|s). The long retention delay worsens the resulting train/behavior distribution shift; RLUR addresses this with a soft, exponential actor-loss regularization penalty (rather than hard behavior cloning, which the authors found either destabilized training or hurt sample efficiency) rather than an explicit off-policy-evaluation estimator such as importance sampling. |
| 10 | Offline and online evaluation | Offline: a 3-module simulator (immediate feedback, session-leave, K=10-day return probability) built on the public KuaiRand dataset, compared against CEM, TD3, and two RLUR ablations. Online: 100+ day live A/B test on the Kuaishou app against the CEM production baseline (TD3 excluded as too unstable for live deployment), tracking app open frequency, DAU, 1st-day retention, and 7th-day retention. |
| 11 | Reported gains | Offline (KuaiRand simulator, Table 1): RLUR — returning time 1.892 days, user retention 0.618 — vs. CEM 2.036 days/0.587, TD3 2.009 days/0.592, RLUR-naive(γ=0) 2.001 days/0.596, RLUR-naive(γ=0.9) 1.961 days/0.601. Online (Kuaishou live A/B vs. CEM, converged ~Day 100): app open frequency +0.450%, DAU +0.2%, 1st-day retention +0.053%, 7th-day retention +0.063%. |
| 12 | Applicability to a two-sided dating recommender | The session-terminal discounting trick and the soft behavior-regularization for delay-induced distribution shift are directly reusable for a 7–30 day dating-retention horizon. The paper is entirely one-sided — a single consumer's own return behavior — with no treatment of reciprocity, match congestion, or a counterparty B whose exposure is itself a scarce, contested resource. |
| 13 | Unverified claims | The claim of being "one of the first works to directly optimize user retention... to the best of our knowledge" is a self-reported novelty claim, not independently verified here. The live-experiment percentage gains are judged against an internally stated significance convention ("0.01% retention... statistically significant in short video platforms") rather than reported p-values or confidence intervals. The offline Table 1 figures are averaged over "the last 50 episodes" with no reported variance. |

## Project Relevance

Named seed reference and the survey's flagship industrial example of optimizing retention directly as an RL reward. It is the primary source for **Q1** (retention as the direct RL training objective, replacing pointwise/listwise proxies) and **Q3** (label = normalized multi-session returning time; horizon = infinite with session-terminal-only discounting as the specific delay-handling mechanism — directly comparable to the dating app's 7–30 day retention horizon). It is directly relevant, but as a cautionary contrast, to **Q2**: RLUR assigns its delayed reward to a request-level ensembling decision, not to an individual item — a coarser grain than the per-candidate-profile decision the dating app's unified model needs to make, so this paper demonstrates a workaround (re-weighting existing item scores) rather than a solution to item-level credit assignment. It is also directly relevant to the survey's central caution about **Q5**: RLUR optimizes retention *conditional on* the recommendations shown, using purely predictive critics — it does **not** estimate the causal effect of exposure, which is exactly the prediction-vs-incrementality distinction the survey's Project Context calls out, and is worth flagging explicitly since RLUR is likely to be treated elsewhere in this survey as "the" retention-RL exemplar. **Q7** (two-sided market, congestion, fairness) is not addressed at all — a genuine gap for direct transfer to a reciprocal dating marketplace.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2019_arXiv_NA_Deep-RL-Search-Recommendation-Advertising-Survey.md](./2019_arXiv_NA_Deep-RL-Search-Recommendation-Advertising-Survey.md) | Related Work / Experiments | Names this paper's method (`RLUR`) |
| [2023_NeurIPS_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md](./2023_NeurIPS_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md) | Related Work / Experiments | Names this paper's method (`RLUR`) |
| [2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md](./2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md) | Related Work / Experiments | Names this paper's method (`RLUR`) |
| [2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md](./2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md) | Related Work / Experiments | Names this paper's method (`RLUR`) |
| [2025_WWW_AURO_Reinforcement-Learning-Adaptive-User-Retention.md](./2025_WWW_AURO_Reinforcement-Learning-Adaptive-User-Retention.md) | Related Work / Experiments | Names this paper's method (`RLUR`) |

_5 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `RLUR` across all 133 cards._

## Meta Information

- **Authors:** Qingpeng Cai, Zhenghai Xue, Chi Zhang, Wanqi Xue, Shuchang Liu, Ruohan Zhan, Xueliang Wang, Tianyou Zuo, Wentao Xie, Dong Zheng, Peng Jiang, Kun Gai
- **Affiliations:** Kuaishou Technology (Kun Gai: unaffiliated)
- **Venue:** WWW 2023 (Companion Proceedings of the ACM Web Conference 2023)
- **Year:** 2023
- **Relevance:** Core
- **Priority:** 1
- **nlm:192447f1-df6d-4e75-a91b-b1e550047316**
