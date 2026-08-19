# Paper Analysis: Notification Volume Control and Optimization System at Pinterest

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/notifications-kdd18.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Notification Volume Control and Optimization System at Pinterest
**Authors:** Bo Zhao, Koichiro Narita, Burkay Orten, John Egan (Pinterest, San Francisco, CA)
**Venue/Year:** KDD 2018 (24th ACM SIGKDD Conference on Knowledge Discovery & Data Mining), London, United Kingdom

**Abstract (paraphrased):** Notification volume — how frequently to send notifications to each user across email, push and other channels — is the most important and challenging lever in a production notification system. The paper proposes a machine-learning approach to set notification volume per user such that long-term user engagement is optimized. The system has been in production at Pinterest since mid-2017 and significantly reduced notification volume while improving CTR and site-engagement metrics compared with the prior ML-based system.

**Key contributions:**
- Reframes volume control as maximizing a per-user expected-activity objective p(a|u,k) subject to a global weekly volume constraint, rather than tuning per-notification-type frequency rules against CTR percentiles.
- Models the *long-term cost* of over-notifying explicitly: a three-model reward function combining an activity-prediction model, an unsubscribe-prediction model, and a model of user activity four weeks after an unsubscribe event (the paper's stand-in for the long-term negative consequence of over-notifying).
- Decouples the volume-control layer from per-notification-type content ranking, an architectural choice made explicitly to let content/ranking teams iterate independently without re-tuning global frequency caps.
- Replaces the quadratic-programming solver used in prior LinkedIn-style systems with two lightweight, Map-Reduce-parallelizable algorithms (per-user budget allocation, and threshold search across users) that scale to hundreds of millions of users.

**Methodology:** Three binary classifiers, all trained via XGBoost (GBDT) with logistic loss: (1) activity model p(a|u,k,s) conditioned on user action s (subscribe/unsubscribe); (2) unsubscribe model p(s_unsub|u,k); (3) long-term unsubscribe-effect model p(a_L|u,s_unsub), predicting activity in the 4th week after an unsubscribe. These combine into a single reward function (Eq. 4) that is maximized per user subject to a global weekly notification-volume constraint (Eq. 2), solved via a custom allocation algorithm (Algorithm 1) plus a threshold-search wrapper (Algorithm 2) instead of a QP solver.

**Main results:** Production A/B test across three user/channel segments (Table 1): Email Only volume -24%, notification CTR +31%, DAU +0%; Push Only volume -6%, CTR +11%, DAU +1%; Email & Push volume -7%(email)/-4%(push), CTR +10%(email)/+21%(push), DAU +3%. The optimizer shifts volume away from very-active and very-inactive users toward users in the middle of the activity distribution (Figure 7), consistent with a diminishing/negative marginal utility of notifications for the most engaged users.

## 2. Experiment Critique

**Design:** Training data for the three classifiers is collected via deliberate randomization of notification volume across a group of users — a genuine randomized-experiment approach to avoid confounding in the labels. The production A/B test compares the new system against the prior ML-based volume system (not against a no-notification baseline), run separately on three segments (email only / push only / email & push) because behavior differs sharply by channel availability.

**Statistical validity:** No confidence intervals, p-values, or significance tests are reported for any number in Table 1 or Figures 5/6/8. Arm sizes for the A/B test are not stated (only that the algorithm is built to handle "hundreds of millions of users" generally). All results are point estimates.

**Online experiments:** Yes — a real production A/B test with day-since-trigger dashboards (Figures 5, 6, 8) segmented into core vs. marginal users, which is a meaningful strength: it supports the mechanism claim (marginal users get more volume and more engagement; core users get less volume with no DAU loss) with finer granularity than the headline table alone.

**Reproducibility:** Proprietary Pinterest data, not released; no code released. Feature lists are given only at a category level (user profile, organic activity history, email/push activity history), and neither GBDT hyperparameters nor the threshold-search range are specified numerically. Not independently reproducible from the paper.

## 3. Industry Contribution

**Deployability:** Fully deployed in Pinterest production since mid-2017, explicitly engineered for horizontal scale (hundreds of millions of users) via Map-Reduce-parallelizable allocation and threshold-search algorithms, replacing the more expensive QP-based approach used in prior LinkedIn-style systems ([7],[8]).

**Problems solved:** Converts a set of siloed, per-notification-type frequency rules (previously tightly coupled to each type's own CTR model) into a single decoupled volume-control layer. This is as much an organizational/engineering win as a modeling one: new notification types and improved ranking models can be tested without disturbing the global volume budget, which the authors state was a major pain point of the legacy system.

**Engineering cost:** Three GBDT models trained/scored regularly on a Hadoop pipeline (Data ETL → Model Trainer/Scorer → Global Optimizer), an online key-value budget store, a daily budget pacer service, and separate models/constraints per channel-availability segment (email only / push only / both — effectively tripling the pipeline). In recommender-engineering terms this sits as a control-plane layer upstream of the per-type content-ranking models (Figure 2), computed in batch (daily/weekly), not on the real-time serving critical path, so latency is not a binding constraint.

## 4. Novelty vs. Prior Work

Positions itself directly against LinkedIn's email volume-optimization work (Gupta et al., "Optimizing Email Volume For Sitewide Engagement," CIKM 2017; Gupta et al., "Email Volume Optimization at LinkedIn," KDD 2016): (1) removes the assumption that the total effect of k notifications is simply the sum of k independent single-notification effects, modeling diminishing returns directly via a nonlinear GBDT on p(a|u,k); (2) replaces separate, globally-tunable upper/lower bounds on positive and negative actions with one unified per-user objective function; (3) replaces a quadratic-programming solver with a cheaper two-algorithm heuristic for scalability; (4) decouples volume control from the per-type CTR ranking models, which were tightly coupled in the prior LinkedIn design.

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| Pinterest internal notification logs (email/push engagement, unsubscribe events) | No — proprietary/internal | Hundreds of millions of users (production scale) | Not released; no public benchmark used |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Value |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Notification Volume Control and Optimization System at Pinterest," Bo Zhao, Koichiro Narita, Burkay Orten, John Egan (Pinterest), KDD 2018. URL: https://doi.org/10.1145/3219819.3219906 |
| 2 | Source type | Industry paper |
| 3 | Direction | D4 |
| 4 | Problem setting | Per-user notification frequency/volume control across multiple channels (email, push) at a large-scale consumer platform, balancing short-term engagement gain against long-term negative consequences of over-notifying (unsubscribe, spam flags, uninstall). |
| 5 | Objective and label definition | Maximize expected user activity probability p(a\|u,k_u) (configurable to DAU/WAU/other) subject to a global weekly volume constraint; built from 3 binary-classification heads — same-week activity given volume and action, same-week unsubscribe probability given volume, and a 4-week-later activity label for users who unsubscribe (the paper's one genuinely delayed/long-horizon label; no formal censoring treatment beyond the fixed 4-week choice). |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. All three heads are supervised classifiers of conditional probability given volume; despite collecting training data via randomized volume assignment, the models are not framed or evaluated as causal-effect estimators. |
| 7 | Model architecture | Three independent XGBoost (GBDT) binary classifiers with logistic loss, combined into one reward function (Eq. 4), optimized under a linear volume constraint via a custom two-algorithm allocation/threshold-search procedure (no QP solver). |
| 8 | Credit assignment | The delayed outcome (activity 4 weeks after an unsubscribe) is attributed to the (user, week) volume decision k_u that preceded the unsubscribe event — aggregate weekly-budget granularity, not a specific notification or notification type. |
| 9 | Training data and counterfactual handling | Production interaction logs; unbiased data collected via deliberate randomization of notification volume across users; the unsubscribe model explicitly uses allocated (not actually-sent) budget as a feature to avoid survivorship bias. No explicit counterfactual/causal-inference machinery. |
| 10 | Offline and online evaluation | Offline: qualitative claim that XGBoost outperforms logistic regression, no reported metric numbers. Online: production A/B test across three user/channel segments over multiple days (Table 1), with day-since-trigger breakdowns (Figures 5, 6, 8) and a volume-vs-activity-level curve (Figure 7). |
| 11 | Reported gains | Pinterest internal A/B test (Table 1): Email Only, Volume -24%, Notification CTR +31%, DAU +0%; Push Only, Volume -6%, CTR +11%, DAU +1%; Email & Push, Volume -7%(email)/-4%(push), CTR +10%(email)/+21%(push), DAU +3%. |
| 12 | Applicability to a two-sided dating recommender | The 3-model decomposition (short-term action, negative-action risk, delayed effect of that negative action) is directly reusable for the dating app's success paradox — e.g., modeling churn risk from over-messaging separately from a delayed post-churn retention effect. It does not transfer for the ranking-of-candidates problem itself: the decision unit is a single-sided per-user volume budget, with no reciprocity or congestion modeling. |
| 13 | Unverified claims | "Much higher" accuracy of XGBoost vs. logistic regression is asserted without a reported number. The 4-week horizon for the long-term unsubscribe-effect label is justified only as "a reasonable choice," with no ablation over other horizons. No statistical significance is reported for any A/B result. |

## Project Relevance

Speaks most directly to **Q3** (label/horizon definition for a delayed outcome — the 4-week post-unsubscribe activity label) and **Q4** (how a short-term head and a long-term head are combined into one reward function, Eq. 4), and to **Q8** (a documented decoupling pattern: separate the volume-control objective from the per-item ranking model rather than fusing them). It is also a directly quantified instance of the batch's volume/fatigue theme: cutting email volume 24% raises notification CTR 31% with DAU flat-to-positive (Table 1), and Figure 7 shows the optimizer voluntarily reduces budget for the most active users — a diminishing/negative marginal utility of more notifications for already-engaged users, the direct analogue of the project's success-paradox concern. Low relevance to **Q2** (credit assignment is at weekly-budget granularity, not item/impression level), **Q5** (no uplift/incrementality machinery), and **Q7** (no two-sided or reciprocal-market element).

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Bo Zhao, Koichiro Narita, Burkay Orten, John Egan
- **Affiliations:** Pinterest, San Francisco, CA
- **Venue:** KDD 2018
- **Year:** 2018
- **Relevance:** Core
- **Priority:** 1
- **nlm:1c974611**
