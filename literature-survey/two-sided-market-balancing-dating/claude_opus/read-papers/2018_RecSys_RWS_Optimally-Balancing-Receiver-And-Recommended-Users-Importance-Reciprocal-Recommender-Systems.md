# Optimally Balancing Receiver and Recommended Users' Importance in Reciprocal Recommender Systems

- **notebook source_id:** `d9bb1a53`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Reciprocal recommender systems (RRSs) for people-to-people matching (online dating, job recruiting) must account for both the service user's interest in a candidate and the candidate's likelihood of responding positively. The paper introduces Reciprocal Weighted Score (RWS): a per-user-optimized weighted blend of a collaborative-filtering interest score and an AdaBoost-predicted reply-probability score. RWS was deployed live on an operational Israeli dating app (Doovdevan) against the prior state-of-the-art reciprocal collaborative filtering (RCF) baseline, in a 398-user randomized online experiment. RWS produced 8x more successful (mutually-replied) interactions than RCF and significantly higher reply-precision, at the cost of somewhat lower click-through on the recommendations themselves and roughly 5x more compute per recommendation.

## Method
RWS scores a candidate `y` for service user `x` as:

`RWS(x,y) = alpha_x * CF(x,y) + (1 - alpha_x) * PR(y,x)`

- **CF(x,y)**: a Jaccard-style reciprocal collaborative-filtering score using user-to-user similarity, `Similarity_{x,n} = |ReFrom_x ∩ ReFrom_n| / |ReFrom_x ∪ ReFrom_n|`, aggregated over users `x` sent messages to and users `y` received messages from, then normalized. This is the same computation used by the RCF baseline.
- **PR(y,x)**: predicted probability that `y` replies positively to an initial message from `x`, from an AdaBoost classifier trained on 35,000 labeled messages (positive/negative reply), with class-imbalance corrected via random oversampling (only ~7% of messages were positively replied). Top features by information gain (Table 1): recipient's percent of positively-replied messages before the current one, recipient's recent log-ins, recipient's profile views; sender's number of profile views received, sender's number of messages received. AdaBoost AUC = 0.833, beating random forest (0.798), logistic regression (0.795), MLP (0.791), and naive Bayes (0.672).
- **alpha_x**: a per-service-user weight, not global. `IndividualOptimization` finds `alpha_x` by minimizing the rank (in the RWS-sorted list of previously-viewed users) of users `x` actually had a successful interaction with, solved via Brent's method (numerical root-finding for a local minimum on an interval). Users with zero prior successful interactions instead get a `GlobalOptimization` weight fit across all users (computed value: alpha = 0.3978, meaning PR is on average a stronger predictor of success than CF).

Candidate generation is restricted to users where CF is nonzero (i.e., some historical interaction chain exists), which keeps the PR-model call count tractable.

## Datasets and Baselines
- **Reply-prediction training data:** 35,000 message samples from Doovdevan (~32,000-user Israeli dating app), manually labeled positive/negative reply.
- **Live online evaluation:** 398 randomly selected active Doovdevan users (24%, n=97, female; ages 18–70, mean 34.9, sd 12.9), randomly split into two conditions. Both received the top-3 recommendations once per day for three days.
- **Baseline:** RCF (Reciprocal Collaborative Filtering), from Xia et al. (2015) — harmonic mean of two-directional CF interest scores, previously shown to outperform the content-based RECON algorithm (Pizzato et al. 2010). The authors note their original plan was to compare against multiple prior methods but were constrained by the platform collaborator to a single baseline (RCF).

## Results
Table 2 (summed across all 398 users, evaluated one week after the recommendation period):

| Measure | RCF | RWS |
|---|---|---|
| RO (recommended & viewed in inbox) | 320 | 356 |
| RV (clicked for detail) | 174 | 147 |
| RM (user sent a message) | 171 | 138 |
| M (total messages sent) | 889 | 1945 |
| RI (successful/reciprocal interactions) | 1 | 8 |
| I (total positively-replied messages) | 99 | 322 |

Per-metric significance (t-test, means/sd across users):
- **VPrecision** (`|RV|/|RO|`): RCF significantly higher (mean 0.57, sd 0.43 vs RWS mean 0.43, sd 0.42) — RCF recommendations look more appealing at first glance.
- **MPrecision** (`|RM|/|RV|`): no significant difference (RCF mean 0.96, sd 0.28 vs RWS mean 0.92, sd 0.23).
- **MRecall** (`|RM|/|M|`): RCF significantly higher (mean 0.42, sd 0.38 vs RWS mean 0.29, sd 0.35).
- **RPrecision** (`|RI|/|RM|`): RWS significantly higher (RCF mean 0.01, sd 0.05 vs RWS mean 0.06, sd 0.21) — the paper's primary claimed result.
- **RRecall** (`|RI|/|I|`): RWS higher but not significant (RCF mean 0.02, sd 0.14 vs RWS mean 0.06, sd 0.21).
- **Popularity of recommended users** (messages received in the 30 days before recommendation): RCF recommended significantly more popular users (mean 59.49, sd 45.14) than RWS (mean 32.72, sd 35.06), p < 0.01 — RWS steers recommendations away from over-saturated high-demand users.
- **Runtime:** RCF averaged 1.47s per user vs RWS 6.97s (including 2.61s for the weight-optimization step); authors state this had no user-facing latency impact since recommendations are pushed, not pulled.

## Limitations
- Constrained by the platform partner to a two-condition comparison (RWS vs. RCF only), not the originally intended multi-method comparison.
- Individual-user alpha optimization only works for users with ≥1 prior successful interaction (89% of subjects in this study); others fall back to a single global alpha.
- Doovdevan does not charge users to send messages; the authors explicitly flag that results may not generalize to pay-per-message platforms, where cost could change sending behavior.
- RWS reduces VPrecision and MRecall relative to RCF — it trades some of the service user's own interest-satisfaction for reply-likelihood.
- No offline/historical-data evaluation was used to screen candidate methods before the online test (deliberately, to avoid distribution-shift bias from a prior recommender); authors state offline evaluation work was in progress as future work.

## Heavily Cited Prior Works
- Xia, Liu, Sun, Chen (2015) — "Reciprocal recommendation system for online dating," IEEE/ACM ASONAM. Source of the RCF baseline method used in this paper.
- Pizzato, Rej, Chung, Koprinska, Kay (2010) — "RECON: a reciprocal recommender for online dating," RecSys. Content-based predecessor RCF was shown to beat.
- Pizzato, Rej, Akehurst, Koprinska, Kay (2013) — "Recommending people to people: the nature of reciprocal recommender systems with a case study in online dating," User Modeling and User-Adapted Interaction.
- Krzywicki, Wobcke, Cai, Mahidadia, Compton, Kim (2010) — "Interaction-based collaborative filtering methods for recommendation in online dating."
- Krzywicki, Wobcke, Cai, Bain, Compton (2015) — "Collaborative Filtering for people-to-people recommendation in online dating: Data analysis and user trial."
- Hong, Zheng, Wang, Shi (2013) — "A Job Recommender System Based on User Clustering" (job-domain RRS analogue).
- Kleinerman, Rosenfeld, Kraus (2018) — "Providing Explanations for Recommendations in Reciprocal Environments," RecSys (same authors' companion paper).

## Bibliography Fields
- **title:** Optimally Balancing Receiver and Recommended Users' Importance in Reciprocal Recommender Systems
- **authors or organization:** Akiva Kleinerman (Bar-Ilan University), Ariel Rosenfeld (Weizmann Institute of Science), Francesco Ricci (Free University of Bozen-Bolzano), Sarit Kraus (Bar-Ilan University)
- **year:** 2018
- **venue or type:** RecSys '18 (12th ACM Conference on Recommender Systems), Vancouver, BC, Canada
- **link:** https://u.cs.biu.ac.il/~sarit/data/articles/recsys18a-sub1173.pdf
- **tier tag:** Tier 2 applied-on-real-platform-data
- **what they did (≤80 words):** Built RWS, a reciprocal recommender that blends a collaborative-filtering interest score with an AdaBoost-predicted reply-probability score, weighted per-user via an optimization that fits historical successful interactions. Deployed live on the Doovdevan dating app against the prior state-of-the-art RCF baseline in a 398-user randomized online experiment, measuring recommendation clicks, messages sent, and successful (mutually-replied) interactions.
- **mechanism relevant to two-sided balancing (≤50 words):** The PR(y,x) reply-probability predictor is a direct like-back-probability model (Layer 1: reciprocal scoring). The finding that RWS recommends significantly less-popular users than a pure-interest baseline is empirical evidence that reply-aware scoring naturally redistributes exposure away from over-saturated high-desirability users (Layer 2 adjacent).
- **metrics used, and the reported effect:** Successful interactions (RI): RCF=1 vs RWS=8. RPrecision (|RI|/|RM|): RCF mean=0.01 (sd 0.05) vs RWS mean=0.06 (sd 0.21), significant. Recommended-user popularity (messages received/30 days): RCF mean=59.49 vs RWS mean=32.72, p<0.01.
- **fit for a dating app:** high — built and evaluated live on an operational dating app; the reply-probability model is precisely the like-back-probability signal the project's Layer 1 needs.
- **confidence that the item is real and described correctly:** high — extracted directly from the full PDF (all 9 pages, including tables, figures, and references); all numbers quoted are as printed in the paper.

## Project Relevance
Directly addresses **Layer 1 (reciprocal scoring)**: PR(y,x) is exactly a like-back probability model, trained on real message-reply data with concrete, transferable features (recipient's recent reply rate, recent activity, popularity; sender's own popularity/activity). The RWS blending formula (`alpha_x * interest + (1-alpha_x) * reply-probability`) is a directly reusable pattern for combining a viewer's own interest signal with the target's predicted willingness/capacity to reciprocate, including the idea of learning the blend weight **per user** rather than globally.

The popularity finding — RWS recommends candidates receiving on average 45% fewer messages than the pure-CF baseline — is suggestive evidence for **Layer 2 (capacity-aware exposure allocation)**: conditioning on reply-likelihood alone, without any explicit capacity constraint or fairness objective, already shifts exposure away from oversaturated high-desirability users, because those users' reply probability to any given individual sender is diluted by their message volume. However, this is a side effect, not a designed mechanism — the paper does not model receiver capacity explicitly, does not optimize for spread of matches, and does not measure match Gini, wasted likes, or two-sided retention. It does not address **Layer 3 (market-design levers)** or **Layer 4 (ecosystem metrics/interference-aware experimentation)** at all — evaluation is per-user ranking quality via a single-arm live comparison, not a marketplace-wide allocation or interference-aware A/B test.

## Reverse Citation Map
