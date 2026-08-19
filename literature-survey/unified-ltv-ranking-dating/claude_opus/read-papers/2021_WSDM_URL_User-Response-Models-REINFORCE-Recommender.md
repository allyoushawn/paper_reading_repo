# Paper Analysis: User Response Models to Improve a REINFORCE Recommender System

**Source:** https://dl.acm.org/doi/10.1145/3437963.3441764 (Chen et al., WSDM 2021)
**Date analyzed:** 2026-08-16

## 1. Summary

**Title:** User Response Models to Improve a REINFORCE Recommender System
**Authors:** Minmin Chen, Bo Chang, Can Xu, Ed H. Chi (Google, Inc.)
**Venue:** WSDM 2021 (Virtual Event, Israel)

**Abstract (paraphrased from source):** Model-free reinforcement learning agents for commercial recommenders must operate over billions of users and millions-to-billions of long-tail items, with (positive) feedback that is extremely scarce relative to that space. This paper presents a general framework for augmenting model-free RL training with auxiliary tasks that predict users' immediate responses (positive or negative) to recommendations — user response modeling (URL) — to improve the learned state and action representations, plus a gradient-correlation analysis tool to guide architecture choices.

**Key contributions:**
1. A general framework for improving RL sample efficiency in recommenders via auxiliary tasks.
2. User Response Modeling (URL): supervised auxiliary tasks predicting immediate feedback (click, dwell time) to enrich state and action representations.
3. A gradient-correlation (cosine-similarity) analysis tool to guide auxiliary-task architecture design.
4. Practical deployment lessons, including activating the auxiliary loss only for low-activity users, validated via both large-scale offline and live industrial experiments.

**Methodology:** The paper builds directly on the REINFORCE recommender of Chen et al. (Top-K Off-Policy Correction for a REINFORCE Recommender System, WSDM 2019): an RNN encodes user state, a softmax policy π_θ(a|s) is trained with off-policy-corrected REINFORCE. URL adds an auxiliary head that shares the RNN, item embeddings, and historical-event embeddings with the main policy, but uses its own single linear projection (deliberately kept shallow, unlike the main head's multiple ReLU layers) to predict the immediate user response r̄(s,a) via an inner product with the item embedding, using binary cross-entropy for click or Huber loss for dwell time. The joint objective is min_θ ℓ_RL(θ) + λ·ℓ_AUX(θ). The main REINFORCE head trains only on a trailing 6-hour window (with a 4-hour buffer for computing the discounted reward), while the auxiliary head trains on the user's full historical trajectory (up to 500 pages). To prevent highly active users from dominating representation learning, the auxiliary objective is activated only for users who have not visited the platform every day over the past two weeks. A gradient cosine-similarity diagnostic (between ℓ_RL and ℓ_AUX with respect to shared item-embedding parameters) is used to compare candidate auxiliary-head architectures before committing to live experiments.

**Main results:** Offline, on a weighted MAP@1 metric computed under a supervised-learning proxy setup (predicting the next interacted item, off-policy correction turned off to control variance), all URL variants (click, dwell time, combined) improved over the base REINFORCE agent, with the combined auxiliary loss performing best and the simple linear-projection head (MAP@1 = 0.061) outperforming a separate-ReLU head (0.059) and a concatenation head (0.057). Online, a month-long live A/B test on a commercial recommendation platform serving billions of users showed a +0.12% improvement (95% CI [+0.07%, +0.18%]) in a user-enjoyment metric for URL (dwell time) vs. base REINFORCE, with a larger +0.26% gain on the low-activity user slice vs. +0.09% on the high-activity slice — consistent with the paper's low-activity targeting design.

## 2. Experiment Critique

**Design.** The paper runs a systematic offline ablation (three auxiliary-task variants: click, dwell time, combined; three head architectures: linear, separate ReLU, concatenation; auxiliary-loss weight λ swept from 0.1 to 10; auxiliary training-window length swept from 6 hours to 7 days) before committing to a single live A/B test on the best offline configuration (URL, dwell time).

**Statistical validity.** Unlike the paper's own predecessor (Chen et al., Top-K Off-Policy Correction for a REINFORCE Recommender System, WSDM 2019), this paper reports explicit 95% confidence intervals for its two headline live results: +0.12% [+0.07%, +0.18%] for URL vs. base REINFORCE, and −0.12% [−0.15%, −0.09%] for the naive 7-day-window baseline vs. the 6-hour-window control. The offline MAP@1 comparisons in Table 1 (0.061 vs. 0.059 vs. 0.057) are reported as point estimates without variance or significance testing.

**Online experiments.** A month-long live A/B test on a commercial platform (unnamed in the extracted text, but consistent with a Google property) serving billions of users, with results segmented by user activity level — directly testing the paper's own hypothesis that low-activity users benefit disproportionately.

**Reproducibility.** The auxiliary-loss formulation, architecture, training-window split, and low-activity gating rule (two-week lookback, deactivate if the user visited daily) are fully specified. The number of sampled-softmax negatives (20,000) is disclosed. The underlying commercial platform, dataset, and exact λ used in the live deployment are not released.

**Overall.** The paper explicitly acknowledges a methodological limitation in its own offline evaluation: because off-policy evaluation is highly variant, the authors deliberately evaluate offline under a simplified "supervised learning" proxy (ignoring partial feedback and off-policy correction) and state this makes the offline numbers "less accurate in predicting live experiment results," relying on the live A/B test for the paper's real validation. This is a transparent and reasonable trade-off, but it does mean the offline ablations (architecture choice, λ sweep, window-length sweep) are validated on a metric the authors themselves flag as an imperfect proxy for the live outcome that matters.

## 3. Industry Contribution

**Deployability.** The auxiliary URL head is a single linear projection added only at training time; it does not change the serving-time policy architecture or add inference latency, since the item-serving path still uses only the main REINFORCE policy head. This makes URL a low-risk way to inject additional supervision into an existing production ranking pipeline.

**Problems solved.** Directly addresses feedback sparsity in off-policy RL recommenders: more than 50% of users contribute fewer than five positive-reward tuples to the main REINFORCE loss within its 6-hour training window, biasing representation learning toward highly active users. URL's low-activity gating specifically compensates for this imbalance.

**Engineering cost.** The engineering overhead is training-time and tuning-time rather than serving-time: a second loss head, a λ hyperparameter requiring a sweep (values 0.1–10 tested, with degradation at high λ), a training-window-length choice for the auxiliary task (found to help further at 2–7 days despite the main head being capped at 6 hours), and a gradient-similarity diagnostic pipeline used to validate architecture choices before a live launch. The user-activity segmentation (two-week lookback per user) adds an additional real-time feature-computation requirement to the training pipeline.

## 4. Novelty vs. Prior Work

**Claimed novelty.** A general framework for adding immediate-response auxiliary tasks to a production RL recommender; a gradient-correlation-based diagnostic tool for choosing among candidate auxiliary architectures before running a live experiment; and the specific design choice of activating the auxiliary loss only for low-activity users to counteract representation bias toward active users.

**Prior work named in the source (Query 2, part 3):**
- Chen et al., "Top-K Off-Policy Correction for a REINFORCE Recommender System," WSDM 2019 — the base production REINFORCE system this paper extends.
- Du et al., "Adapting auxiliary losses using gradient similarity," 2018 — the source of the gradient cosine-similarity technique adopted here.
- Covington et al., "Deep neural networks for YouTube recommendations," 2016 — cited as the baseline deep recommendation architecture.
- Williams, "Simple statistical gradient-following algorithms for connectionist reinforcement learning," 1992 — the foundational REINFORCE algorithm.
- Sutton and Barto, "Reinforcement Learning: An Introduction," 1998 — general RL framing.
- Ie et al., "SlateQ: A tractable decomposition for reinforcement learning with recommendation sets," 2019 — cited among prior deep-RL extensions to slate recommendation.
- Swaminathan and Joachims, "Batch learning from logged bandit feedback through counterfactual risk minimization," 2015 — cited for off-policy evaluation and propensity-weight variance control.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Offline trajectory corpus | Hundreds of millions of user trajectories from a commercial recommendation platform; action space restricted to the top 10 million items | Not public | 1% held out for offline evaluation; trajectories capped at 500 historical pages with at least one positive interaction. |
| Live production traffic | Commercial recommendation platform serving billions of users and tens of millions of items | Not public | Source of the month-long live A/B test results. |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | User Response Models to Improve a REINFORCE Recommender System; Minmin Chen, Bo Chang, Can Xu, Ed H. Chi (Google, Inc.); WSDM 2021; https://dl.acm.org/doi/10.1145/3437963.3441764 |
| 2 | Source type | Industry paper |
| 3 | Direction | D2 |
| 4 | Problem setting | Sample-inefficient off-policy RL recommender training under extremely sparse positive feedback, across billions of users and a millions-to-billions-item long-tail corpus. |
| 5 | Objective and label definition | Joint minimization of the REINFORCE loss (label = discounted cumulative reward R_t built from immediate response r(s,a); zero for non-interacted items) and an auxiliary loss (label = the immediate user response itself — click, binary cross-entropy; or dwell time, Huber loss). Horizon: main RL head trains on a trailing 6-hour window with a 4-hour reward-computation buffer; the auxiliary head trains on the full historical trajectory (up to ~500 pages, potentially spanning months). No explicit delay or censoring model — handled via fixed sliding windows and continuous retraining. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. Paper's own wording: "we opt to add additional tasks that predict users' immediate responses (positive or negative) toward recommendations, i.e., user response modeling, to enhance the learning of the state and action representations." |
| 7 | Model architecture | Shared RNN user-state encoder and item embeddings (inherited from the base REINFORCE system); main policy head (multiple ReLU layers plus linear projection); auxiliary URL head (single linear projection, deliberately shallow) predicting immediate response via inner product with the item embedding; joint loss with scalar weight λ. |
| 8 | Credit assignment | Item-level, identical in mechanism to the base REINFORCE paper: reward/response is logged per recommended item; non-interacted items are zeroed out of the main RL loss but retained as negatives for the click auxiliary loss (all recommended items, clicked or not, contribute to that loss). |
| 9 | Training data and counterfactual handling | Logged trajectories from the deployed behavior policy. The main RL loss inherits the off-policy correction from the base REINFORCE system (Chen et al., 2019). The auxiliary loss is deliberately not off-policy corrected — it is a plain supervised loss on logged (s,a,r) triples, justified by the authors' argument that the immediate response is independent of which policy was deployed. |
| 10 | Offline and online evaluation | Offline: a "supervised learning" proxy setup (predict the next item the user interacted with, weighted by R_t, with off-policy correction turned off to reduce variance), scored by weighted MAP@1; the authors explicitly flag this as a lower-fidelity proxy for live performance. Online: month-long live A/B test on a commercial platform, with results reported for the global user base and separately for low-activity and high-activity slices. |
| 11 | Reported gains | Live A/B on the commercial platform's user-enjoyment metric: +0.12% (95% CI [+0.07%, +0.18%]) globally for URL (dwell time) vs. base REINFORCE; +0.26% on the low-activity slice vs. +0.09% on the high-activity slice. Offline weighted MAP@1 on the held-out trajectory corpus: URL (linear head) 0.061 vs. URL with separate ReLU layers 0.059 vs. URL with concatenation 0.057, with the combined click+dwell-time auxiliary loss the best-performing variant. A naive 7-day training-window-extension baseline regressed the live enjoyment metric by −0.12% (95% CI [−0.15%, −0.09%]). |
| 12 | Applicability to a two-sided dating recommender | The low-activity-user targeting mechanism maps directly onto a dating app's engagement long tail, and the auxiliary-task pattern is a low-cost way to inject additional short-horizon signal (e.g., a match or conversation auxiliary head) without altering the serving-time ranking path. Like its parent paper, however, it is entirely one-sided, with no reciprocity, congestion, or match-quality treatment. |
| 13 | Unverified claims | The claim that "focusing too much on the myopic objective... does interfere with the learning of the agent's policy" is drawn from a single λ sweep on the dwell-time auxiliary task and not shown to replicate across the click or combined variants. The offline Table 1 architecture comparison (0.061 vs. 0.059 vs. 0.057) is not accompanied by a significance test. |

## Project Relevance

This is a named seed reference. It speaks directly to **Q8** (migration paths): the "auxiliary heads first" pattern named in the survey brief's own list of documented migration paths is exactly what this paper implements — a low-term auxiliary prediction task bolted onto an existing RL policy without changing the serving architecture — making it a primary source for that specific migration stage. It also speaks to **Q1** (using RL with a reward built from engagement signals as the training objective, rather than a separate CTR/CVR proxy model) and reinforces **Q2**: the credit-assignment mechanism is identical, item-level pointwise attribution inherited from its parent paper, which is the same limitation a dating-app slate would need to resolve. It does **not** address **Q5** (prediction vs. incrementality — this paper predicts responses, not effects), **Q6** (no discussion of surrogate/offline-online evaluation gap beyond the paper's own acknowledged offline-proxy limitation), or **Q7** (two-sided markets, congestion, reciprocity — entirely absent).

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Minmin Chen, Bo Chang, Can Xu, Ed H. Chi
- **Affiliations:** Google, Inc.
- **Venue:** WSDM 2021
- **Year:** 2021
- **Relevance:** Core
- **Priority:** 1
- **nlm:2d129fa5-3f44-4781-ad86-aafac5b1edde**
