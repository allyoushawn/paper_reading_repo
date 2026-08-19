# Paper Analysis: Modeling User Retention through Generative Flow Networks
**Source:** NotebookLM, source_id `3183e5a0-4ebb-4f26-bd56-5be0441fe5a5`
**Date analyzed:** 2026-08-16

## 1. Summary
Title: Modeling User Retention through Generative Flow Networks (GFN4Retention)
Authors: Zijian Zhang (City University of Hong Kong), Lantao Hu, Han Li, Peng Jiang, et al. (Kuaishou Technology)
Venue/Year: KDD '24, August 25–29, 2024, Barcelona, Spain

Abstract/key contributions: Recommender systems have shifted from immediate-feedback optimization (clicks, likes) toward optimizing user retention (how often users return), because retention correlates closely with Daily Active Users (DAU). Retention is hard to optimize directly because it is a between-session signal: it does not occur until the user leaves and returns, has no clear relation to any single recommendation step, and involves unobservable inter-session activity. The paper introduces GFN4Retention, the first Generative Flow Network (GFN) framework for retention optimization. It models a session as a trajectory-generation process where the terminal retention reward is matched by the end-of-session generation probability, and an integrated reward design (product of the terminal retention reward and cumulative immediate reward) plus a refined Detailed Balance (DB) loss back-propagates the delayed retention reward to each recommendation step ("retention attribution"). The formulation extends GFN theory from small discrete action spaces to continuous vector spaces to accommodate list-wise recommendation.

Methodology: Three modules — (a) a User State Encoding module (Transformer history encoder + DNN context detector, concatenated into state s_t); (b) the recommendation policy as a forward flow P_F(s_{t+1}|s_t), where the policy outputs Gaussian parameters (mu, sigma) and a deterministic top-K selection module maps the sampled action vector to an item list; (c) flow estimation modules — a state flow estimator F(s_t) and a backward flow estimator P_B(s_t|s_{t+1}), both sigmoid-activated for non-negativity. The reward is integrated as R(S) = R_retention · e^(alpha·sum of immediate rewards), decomposed as F(s_t) = F_R(s_t) · (F_I(s_t))^alpha, where F_I is a non-parametric tracker of accumulated immediate reward and F_R is the learned retention flow. This yields a log-scale Detailed Balance loss with smoothing offsets (beta_F, beta_B, beta_r) for training stability.

Main results: On two offline datasets (Kuairand-Pure, MovieLens-1M) simulated via the KuaiSim cross-session simulator, GFN4Retention statistically significantly reduces Return Time and improves Retention score vs. five baselines (CEM, DIN, TD3, SAC, RLUR), while matching or exceeding baselines on Click Rate, Long View Rate, and Like Rate. In a live A/B test on an industrial billion-scale video platform (Kuaishou), deployed in the ranking-score-ensemble modules of two ranking stages, GFN4Retention produced statistically significant lifts: overall next-day retention +0.015%, target (lower-activity) users' next-day retention +0.069%, watch time +0.558% (first stage); target users' next-day retention +0.056%, watch time +0.224% (second stage).

## 2. Experiment Critique
Design: Two offline benchmarks (Kuairand-Pure: 27,285 users / 7,551 items / 1,436,609 interactions, density 0.70%; MovieLens-1M: 6,400 users / 3,706 items / 1,000,208 interactions, density 4.22%) simulated with the KuaiSim leave-and-return simulator, plus a live industrial A/B test. Five baselines span classic RL (CEM, DIN) and continuous-action actor-critic RL (TD3, SAC, RLUR), the last of which is the closest prior retention-specific method.

Statistical validity: Offline gains on Return Time and Retention are marked as statistically significant (two-sided t-test, p<0.05) over the best baseline; online gains are also flagged as statistically significant, though the underlying test/CI methodology beyond "10% GFN4Retention / 20% baseline" traffic split is not elaborated in the retrieved content.

Online experiments: A live A/B test was run across two ranking stages of a billion-scale industrial platform (10% holdout for GFN4Retention, 20% for baseline), reporting overall and target-user next-day retention plus watch-time deltas — a genuine production validation and one of the paper's strongest points.

Reproducibility: Source code is stated to be released. Hyperparameters (learning rates, batch sizes, smoothing offsets alpha/beta_F/beta_B/beta_r) are reported per dataset in appendices, aiding reproducibility of the offline results; the industrial deployment details (traffic, production architecture) are not reproducible outside Kuaishou.

Overall: A methodologically careful offline/online combination with ablations (NIF, SIF, NCD variants) isolating the contribution of immediate-feedback integration and the context-detection module. The balance parameter alpha is shown to be sensitive in both directions (under- and over-weighting immediate reward both hurt performance), and the authors are transparent about this instability.

## 3. Industry Contribution
Deployability: Demonstrated end-to-end production deployment at Kuaishou — one of the strongest industry signals in this batch. Deployed inside "ranking score ensemble modules," i.e., the policy output is the fusion weight across multiple existing prediction models' ranking scores rather than a full replacement ranking model, which lowers integration risk.

Problems solved: Directly optimizes retention (a between-session, delayed, sparse signal) instead of relying on immediate-feedback proxies or an indirect RL cumulative-reward surrogate.

Engineering cost: Requires a session-level replay buffer / cross-session data pipeline (states, actions, per-step immediate rewards, and a terminal retention reward per session), a Transformer-based user history encoder, and three additional flow-estimation networks (forward, backward, retention flow) trained jointly via a custom DB loss with several smoothing hyperparameters shown to require careful tuning. At inference, the policy only needs to sample from a Gaussian and run the pre-existing top-K selection, so inference-time cost is modest; the additional flow/backward networks are training-time only.

## 4. Novelty vs. Prior Work
Claimed novelty: First application of Generative Flow Networks to retention optimization in recommendation; a reward-integration design and refined Detailed Balance loss that explicitly derives per-step "retention attribution" instead of using RL's indirect cumulative-reward surrogate; extension of GFN flow-matching theory from discrete to continuous action spaces for list-wise recommendation.

Prior work cited (from Query 2 part 3): Cai et al., "Reinforcing User Retention in a Billion Scale Short Video Recommender System" (RLUR) — the primary baseline and closest retention-specific predecessor; Bengio et al. (2023), "GFlownet foundations" — DB loss / flow-matching theoretical foundation; E. Bengio et al. (2021), "Flow network based generative models for non-iterative diverse candidate generation" — the original GFN paper; Zhao et al. (2023), "KuaiSim: A comprehensive simulator for recommender systems" — the simulation environment; S. Liu et al. (2023), "Exploration and Regularization of the Latent Action Space in Recommendation" — continuous latent action mapping; Wu et al. (2017), "Returning is believing: Optimizing long-term user engagement in recommender systems" — foundational inter-session return-time optimization work.

## 5. Dataset Availability
| Dataset | Type | Users | Items | Interactions | Public |
|---|---|---|---|---|---|
| Kuairand-Pure | short-video, unbiased random exposure | 27,285 | 7,551 | 1,436,609 | Yes (kuairand.com) |
| MovieLens-1M | movie ratings | 6,400 | 3,706 | 1,000,208 | Yes (grouplens.org) |
| KuaiSim simulator | cross-session leave/return simulator | — | — | — | Yes (open source) |
| Industrial live platform | billion-scale video platform (Kuaishou) | billions of requests/day, millions candidate pool | — | — | No (proprietary) |

## 6. Community Reaction
Not assessed in NotebookLM mode.

## 7. Reference Card
1. **Title, authors/company, venue, year, URL:** "Modeling User Retention through Generative Flow Networks," Zijian Zhang, Lantao Hu, Han Li, Peng Jiang, et al. (City University of Hong Kong / Kuaishou Technology), KDD '24, Barcelona, Spain. URL: https://doi.org/10.1145/3637528.3671646. `nlm:3183e5a0-4ebb-4f26-bd56-5be0441fe5a5`.
2. **Source type:** Academic (industry-affiliated; co-authored and deployed by Kuaishou).
3. **Direction:** D2.
4. **Problem setting:** Session-level recommendation for a short-video platform; jointly optimizing immediate per-item feedback and a between-session user-retention signal with no clear per-step causal link to any single recommendation.
5. **Objective and label definition:** Two coupled rewards per session: (a) immediate reward r_t = weighted sum of per-step behavior signals (click, view time, like, comment, follow, forward offline; normalized watch time online); (b) terminal retention reward R = reciprocal of the inter-session return-time gap, observed only at session end s_T. Horizon: one user session, T steps, with retention measured as the gap until the next session ("next-day" retention in the live deployment). Delay handling: the terminal, delayed retention signal is back-propagated to every intermediate step via the flow-matching Detailed Balance objective, rather than via reward shaping or discounting. Censoring: Not specified in source.
6. **Prediction or incrementality:** Prediction only — the paper explicitly frames the model as an "estimation" of the retention signal via probabilistic flow ("we regard the retention signal as an overall estimation of the user's end-of-session satisfaction and propose to estimate this signal through a probabilistic flow") and as an "energy-based model that can predict the delayed retention signal." It does not estimate the causal/incremental effect of a given exposure versus a counterfactual non-exposure; it optimizes a policy against an observed/simulated reward, which is not the same as isolating incrementality.
7. **Model architecture:** Transformer + DNN user-state encoder (history encoder + context-detector) → policy network outputs Gaussian(mu, sigma) over a continuous action vector → deterministic top-K selection maps the vector to an item list (forward flow P_F); separate sigmoid-activated state-flow estimator F(s_t) and backward-flow estimator P_B(s_t|s_{t+1}) networks, trained jointly via a log-scale Detailed Balance loss with smoothing hyperparameters.
8. **Credit assignment:** A single terminal, session-level retention reward R (observed only at s_T) is distributed across every preceding recommendation step via flow-matching: the overall state flow is factored as F(s_t) = F_R(s_t) · (F_I(s_t))^alpha, where F_I is a non-parametric running product of immediate per-step rewards and F_R is a learned "retention flow" that must satisfy the Detailed Balance equation at every step. Minimizing the resulting per-step squared DB loss implicitly back-propagates the terminal retention outcome into a credit value for each step's action, which the authors term "retention attribution." This genuinely decomposes a delayed outcome across the sequence of decisions that preceded it, but it attributes credit to a per-request *slate* decision (the whole recommended list at step t), not to an individual item within that slate — the paper does not further decompose credit within a list.
9. **Training data and counterfactual handling:** Each training sample is a session tuple (states, actions, immediate rewards, terminal retention reward), collected via the KuaiSim cross-session simulator offline or via live production logging (fixed 10%/20% traffic holdout) online; no explicit counterfactual/propensity correction or off-policy correction is described.
10. **Offline and online evaluation:** Offline — KuaiSim cross-session simulator on Kuairand-Pure and MovieLens-1M, metrics: Return Time, Retention score, Click Rate, Long View Rate, Like Rate, averaged over the last 1000 training episodes across 5 baselines. Online — live A/B test on an industrial billion-scale video platform, deployed in the ranking-score-ensemble modules of two ranking stages, with next-day user return frequency and average watch time as the reported metrics, split by overall users and lower-activity "target" users.
11. **Reported gains:** Offline (Kuairand-Pure): Return Time 1.496 days vs. RLUR's 1.786 days (best baseline), statistically significant (p<0.05); Retention score 0.163 vs. RLUR's 0.159. Offline (MovieLens-1M): Return Time 1.479 days vs. RLUR's 1.723 days; Retention 0.165 vs. RLUR's 0.160. Online (Kuaishou, 1st ranking stage): overall next-day retention +0.015%, target users' next-day retention +0.069%, watch time +0.558% (all statistically significant). Online (2nd ranking stage): target users' next-day retention +0.056%, watch time +0.224%.
12. **Applicability to a two-sided dating recommender:** Low direct applicability on the two-sidedness dimension — the paper is single-sided (video consumption) with no reciprocity, congestion, or two-sided fairness treatment. The flow-based retention-attribution mechanism itself is directly transferable as a candidate technique for the survey's Q2 (attributing a delayed, between-session outcome to a ranking decision) once adapted with reciprocal/congestion constraints.
13. **Unverified claims:** The claim that GFN exploration properties "naturally solve" RL's exploration-exploitation trade-off is asserted from general GFN literature rather than demonstrated with a dedicated exploration-specific experiment in this paper. The generalization claim ("applied in two major ranking scenarios... indicating its generalization ability and scalability") rests on only two internal deployment stages at one company.

## Project Relevance
GFN4Retention speaks most directly to **Q2** (attributing a user-level, delayed outcome to an item-level decision) and **Q3** (label/horizon definitions, delay handling for retention). It offers a concrete, production-validated alternative to standard RL cumulative-reward surrogates for retention: flow-matching credit assignment via a Detailed Balance loss, explicitly targeting the "retention attribution" problem the survey brief identifies as its hardest question. It also speaks to **Q1** (making retention the direct training objective rather than a proxy), since the terminal reward literally is return-time/retention, not a proxy like watch time. It is weak on **Q7** (two-sided/reciprocal market, congestion, fairness) — entirely absent — and does not address **causal incrementality (Q5)**: the retention signal is predicted/estimated, not measured as an incremental treatment effect. The credit-assignment mechanism operates at the slate level (one recommendation request → one list of items), not at the single-item level, so further adaptation would be needed to attribute retention credit to showing one specific candidate profile B to viewer A.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2019_arXiv_NA_Deep-RL-Search-Recommendation-Advertising-Survey.md](./2019_arXiv_NA_Deep-RL-Search-Recommendation-Advertising-Survey.md) | Related Work / Experiments | Names this paper's method (`GFN4Retention`) |
| [2023_NeurIPS_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md](./2023_NeurIPS_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md) | Related Work / Experiments | Names this paper's method (`GFN4Retention`) |
| [2023_WWW_TSCAC_Two-Stage-Constrained-Actor-Critic-Short-Video.md](./2023_WWW_TSCAC_Two-Stage-Constrained-Actor-Critic-Short-Video.md) | Related Work / Experiments | Names this paper's method (`GFN4Retention`) |

_3 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `GFN4Retention` across all 133 cards._

## Meta Information
- Authors: Zijian Zhang, Lantao Hu, Han Li, Peng Jiang, et al.
- Affiliations: City University of Hong Kong; Kuaishou Technology, Beijing, China
- Venue: KDD 2024 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- Year: 2024
- Relevance: Core
- Priority: 1
- `nlm:3183e5a0-4ebb-4f26-bd56-5be0441fe5a5`
