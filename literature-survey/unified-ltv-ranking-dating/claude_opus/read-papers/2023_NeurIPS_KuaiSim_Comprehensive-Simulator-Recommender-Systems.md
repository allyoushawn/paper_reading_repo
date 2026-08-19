# Paper Analysis: KuaiSim: A Comprehensive Simulator for Recommender Systems

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2309.12645.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

KuaiSim (Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai; City University of Hong Kong / Kuaishou Technology; NeurIPS 2023) is a comprehensive RL simulator for recommender systems, not a ranking model. It chains three sequential modules — a User Immediate Response Module (Transformer over user profile + history, producing per-behavior-type click/like/comment/follow/forward/hate feedback), a User Leave Module (a depleting "temper" scalar that ends a session), and a User Retention Module (a next-day return probability composed from a personal bias, a response bias proportional to the session's total immediate reward, and a global bias tuned to fit the real data's geometric-shaped return-time distribution; return day is sampled from Geometric(p_ret), capped at 10 days). All three modules are pretrained by supervised binary cross-entropy on real logged data — primarily KuaiRand-Pure (27,077 users, 7,551 items, 1.44M interactions, 246,738 sessions), with a second demonstration on MovieLens-1M to show portability. The paper benchmarks baseline algorithms at three task levels (request-level list-wise ranking, whole-session sequential RL, cross-session retention optimization) purely inside the simulator, and separately validates KuaiSim's own click-response fidelity against four prior simulators (RecoGym, RecSim, RL4RS, VirtualTaobao) via AUC on the same log, reporting a statistically significant improvement (p<0.05). The authors' own stated limitations (Section "Limitations and potential direction for solutions") are that the simulator does not model explainability, diversity, or fairness, and that both underlying datasets are video-recommendation domains — extension to music, news, or e-commerce is left as future work.

## 2. Experiment Critique

All reported results are evaluations of RL/search baselines running *inside* KuaiSim itself (Tables 3–7), averaged over five runs with standard deviations reported; there is no live online experiment anywhere in the paper. Simulator-fidelity validation (Table 6) is limited to aggregate click-response AUC against four other simulators — the retention module's individual-level predictive accuracy (e.g., predicted vs. actual return day for a held-out real user) is never separately reported; only that its bias terms are tuned so the *aggregate* return-time distribution matches an assumed geometric shape (Figure 2d). Code and both datasets (KuaiRand is public; ML-1m is the standard public benchmark) are released, supporting reproducibility.

## 3. Industry Contribution

Co-authored with Kuaishou Technology and built on a real short-video platform log; the simulator itself is not a deployable ranking component but a pre-deployment offline evaluation/training environment intended to reduce the cost of live A/B testing for RL-based recommenders. No latency, serving, or production-integration details are given, since nothing here is claimed to be in production.

## 4. Novelty vs. Prior Work

Positioned against four prior recommender simulators — RecoGym, RecSim (Ie et al. 2019), RL4RS, and Virtual-Taobao — none of which the authors say jointly support real-dataset grounding across all three of request-level, whole-session, and cross-session (retention) tasks (Table 1). Also cites and reuses RLUR (Cai et al., "Reinforcing User Retention in a Billion Scale Short Video Recommender System," 2023) as the cross-session state-of-the-art baseline, ListCVAE (Jiang et al. 2018) for request-level generative list-wise recommendation, and HAC (Liu et al. 2023) for whole-session hyper-action decomposition.

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| KuaiRand-Pure | Yes (Gao et al., KuaiRand, CIKM 2022) | 27,077 users, 7,551 items, 1,436,609 interactions, 246,738 sessions | Real Kuaishou short-video logs with randomly-exposed items, described as "unbiased" |
| MovieLens-1M | Yes (public benchmark) | 6,400 users, 3,706 items, 1,000,208 interactions, 16,629 sessions | Used to demonstrate KuaiSim's portability to a different domain/dataset |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "KuaiSim: A Comprehensive Simulator for Recommender Systems," Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai (City University of Hong Kong / Kuaishou Technology), NeurIPS 2023, https://arxiv.org/abs/2309.12645 |
| 2 | Source type | Academic (co-authored with industry, Kuaishou Technology; code and datasets released) |
| 3 | Direction | D2 |
| 4 | Problem setting | A simulator for RL-based recommender systems, addressing three nested decision levels — single-request list-wise ranking, whole-session sequential recommendation, and cross-session user-retention optimization — built from a real short-video platform log (KuaiRand) plus a portability demo on MovieLens-1M. It is an environment, not a trained production ranker. |
| 5 | Objective and label definition | Not a single training objective — the simulator supplies labels to RL agents at three levels. At the cross-session (retention) level, the learning signal is "return day" (time gap between the last request of one session and the first request of the next) and a derived binary "user retention" indicator. Horizon is hard-capped at D=10 days ("the percentage of return day greater than 10 in negligible"). No censoring mechanism beyond that fixed cutoff is described. |
| 6 | **Prediction or incrementality** | Prediction only — the paper does not address incrementality. The User Retention Module predicts/simulates a next-day return probability from personal, response, and global bias terms; it does not estimate or evaluate the causal effect of an exposure or policy against a counterfactual baseline. |
| 7 | Model architecture | Three chained modules (Algorithm 1): (a) User Immediate Response Module — Transformer over profile + history produces a ground-truth state; a DNN gives per-behavior-type attention weights; immediate feedback (click/like/comment/follow/forward/hate) is sampled, penalized by an item-correlation term that suppresses positive responses for redundant items; (b) User Leave Module — a "temper" scalar depletes by the immediate reward each step, session ends when temper crosses a threshold; (c) User Retention Module — next-day return probability p_ret = personal bias (DNN on state) + response bias (proportional to the session's total immediate reward) + a global bias fit to the data's return-time distribution shape; return day ~ Geometric(p_ret). |
| 8 | **Credit assignment** | Not the usual sense used elsewhere in this survey — KuaiSim is a synthetic response generator, not a model trained on real user-level outcomes. Internally, the retention signal it emits is attributed to a whole session's aggregate immediate reward (the "response retention bias" term), not to any single impression or item; the simulator performs no item-level credit assignment for the retention event it generates. |
| 9 | Training data and counterfactual handling | All three response modules are pretrained by supervised binary cross-entropy on real logged data (KuaiRand-Pure, described by its own paper as "unbiased" due to randomly-exposed items; also demonstrated on ML-1m). RL agents are then trained via online interaction with the fitted simulator, not directly on the log. No further counterfactual or off-policy correction is described for downstream RL training. |
| 10 | Offline and online evaluation | All evaluation is against the simulator itself — there is no online A/B test anywhere in the paper. Cross-session task: three methods (CEM, TD3, RLUR) are compared inside KuaiSim on "return day" (lower better) and "user retention" (higher better) (Table 5). Separately, KuaiSim's own fidelity is checked only via aggregate click-response AUC against four other simulators trained on the same log (Table 6) — this validates the immediate-feedback module, not the retention module. |
| 11 | Reported gains | Cross-session task inside KuaiSim (Table 5): RLUR — return day 3.481 ± 0.010, user retention 0.607 ± 0.002; TD3 — 3.556 ± 0.010 / 0.581 ± 0.001; CEM — 3.573 ± 0.012 / 0.572 ± 0.002. Simulator fidelity (Table 6, KuaiRand-Pure, whole-session task): KuaiSim's click-response AUC 0.7234 ± 0.0021 (statistically significant, p<0.05) vs. next-best baseline simulator VirtualTaobao at 0.6866 ± 0.0014. |
| 12 | Applicability to a two-sided dating recommender | The request/session/cross-session task hierarchy and explicit retention module are a structurally useful template for modeling delayed engagement, but KuaiSim is single-sided (one viewer against a passive item catalog): it has no reciprocity, congestion, or shared-attention constraint, and would need substantial extension to represent a mutual-like, congestion-bound dating market. |
| 13 | Unverified claims | The claim that KuaiSim "excels in its ability to approximate real-world environments" rests only on aggregate click-response AUC and in-simulator RL reward metrics (Table 6), not on any comparison to real online behavior at the individual level. The retention module's own predictive accuracy against a held-out user's actual return day is never separately reported — only that its bias terms are tuned so the aggregate return-time distribution matches an assumed geometric shape. |

## Project Relevance

Speaks to **Q3** (label/horizon definition and delay handling for retention — KuaiSim's geometric return-day formulation with a 10-day cap is one concrete industry precedent for horizon choice) and, indirectly, **Q6** (offline evaluation under noisy, slow retention effects — KuaiSim exists specifically because such evaluation is hard).

**On the batch note's central question — is a KuaiSim-validated retention gain comparable evidence to an online A/B result: no, and this matters directly for reading RLUR, GFN4Retention, AURO, and Stratified Expert Cloning as carded elsewhere in this survey.** KuaiSim's retention signal is not observed user behavior; it is a synthetic draw from Geometric(p_ret), where p_ret is itself a learned function whose "response retention bias" term is proportional to the very immediate-reward signal an RL policy is optimizing. A policy that increases session-level immediate reward therefore mechanically increases its own simulated retention probability by construction of the simulator, independent of whether that relationship holds in real users. Table 5's RLUR-vs-TD3-vs-CEM comparison is real evidence about relative policy behavior *inside this specific simulated MDP*, not evidence that any of the three would move real DAU. Consequently: (a) if two of the survey's retention-RL papers both report gains "on KuaiSim," those gains are comparable to each other only insofar as they used the same simulator configuration and baselines — they are not each independently validated against ground truth; (b) a KuaiSim result should be read as an ablation over policy architectures under one fixed, admittedly-untested behavioral model of retention, not as an estimate of real-world retention lift; (c) RLUR itself — cited inside KuaiSim as the cross-session state-of-the-art baseline and authored by overlapping Kuaishou personnel — is the same method KuaiSim's retention module was partly designed around, which is a further reason to discount within-simulator RLUR superiority as independent confirmation. Any executive-summary comparison table in this survey should flag every KuaiSim-only result as simulator-internal, not online-validated.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md](./2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md) | Related Work / Experiments | Names this paper's method (`KuaiSim`) |
| [2024_KDD_ItemA2C_Future-Impact-Decomposition-Request-level-Recommendations.md](./2024_KDD_ItemA2C_Future-Impact-Decomposition-Request-level-Recommendations.md) | Related Work / Experiments | Names this paper's method (`KuaiSim`) |
| [2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md](./2025_CIKM_SEC_Stratified-Expert-Cloning-Retention-Aware-Recommendation.md) | Related Work / Experiments | Names this paper's method (`KuaiSim`) |
| [2025_WWW_AURO_Reinforcement-Learning-Adaptive-User-Retention.md](./2025_WWW_AURO_Reinforcement-Learning-Adaptive-User-Retention.md) | Related Work / Experiments | Names this paper's method (`KuaiSim`) |

_4 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `KuaiSim` across all 133 cards._

## Meta Information

- **Authors:** Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai
- **Affiliations:** City University of Hong Kong; Kuaishou Technology; Unaffiliated (Kun Gai)
- **Venue:** NeurIPS 2023 (37th Conference on Neural Information Processing Systems)
- **Year:** 2023
- **Relevance:** Related
- **Priority:** 4
- **nlm:143f8c4b**
