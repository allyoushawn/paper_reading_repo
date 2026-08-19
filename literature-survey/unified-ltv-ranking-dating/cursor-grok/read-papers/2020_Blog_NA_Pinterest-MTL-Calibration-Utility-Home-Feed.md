# Paper Analysis: Multi-task Learning and Calibration for Utility-based Home Feed Ranking

**Source:** https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Multi-task Learning and Calibration for Utility-based Home Feed Ranking
- **authors or company:** Ekrem Kocaguneli, Dhruvil Deven Badani, Sangmin Shin (Pinterest Homefeed Ranking)
- **venue:** Pinterest Engineering Blog (Medium)
- **year:** 2020
- **URL:** https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad
- **source type:** blog
- **direction:** D1
- **problem setting:** Pinterest home feed ranks user–Pin pairs for 400M+ monthly visitors; prior single-output logistic DNN produced a non-probabilistic “pinnability” score fusing click, long-click, close-up, and repin via weighted loss, making cross-model comparison and business tuning difficult.
- **objective and label definition:** Per-action binary labels (click, long-click, close-up, repin; later video >10s view, hide); each MTL head predicts calibrated action probability; utility combines calibrated P(action) with tunable weights W(action); no explicit retention/LTV horizon—session-level engagement optimization.
- **prediction or incrementality:** Predicts per-action probabilities fused into utility score; predictive engagement modeling, not incremental effect of an exposure on long-term retention.
- **model architecture:** MTL DNN with shared representation and per-action output heads; separate logistic-regression calibration model per head (80+ features, Platt-scaling-like); utility = weighted sum of calibrated probabilities; AutoML feature pipeline beneath fully connected layer.
- **credit assignment:** Per user–Pin impression; multi-head predictions combined via fixed/tunable utility weights at ranking time; no user-level delayed outcome mapped to individual Pin exposures described.
- **training data and counterfactual handling:** Ranking DNN trained on stratified-sampled logs; calibration models trained on uniform 10% sample without stratification over 7 days (next day test); DNN replay on common logs to calibrate new models before serving; no counterfactual/off-policy training stated.
- **offline and online evaluation:** Calibration monitored via total calibration error, reliability diagrams, log loss, expected calibration error; realtime production alerting; qualitative online wins (relevance, velocity, business flexibility); video distribution +40% with engagement rate increase; no numeric home-feed lift percentages stated.
- **reported gains:** Video distribution increased by 40% with increased engagement rates after adding calibrated >10s video-view head; qualitative improvements in prediction accuracy, engineering velocity, and business tuning speed; no topline engagement lift percentages stated.
- **applicability note for a two-sided dating recommender:** MTL + per-head calibration + tunable utility fusion is a direct template for combining swipe, match, message, and hide probabilities into a business-adjustable ranking score without retraining the base model.
- **applicability note for a two-sided dating recommender:** Utility weights tune short-horizon engagement only; no bilateral match credit, congestion on popular profiles, or delayed retention labels—still a CTR-like proxy stack unless a long-term head is added.
- **unverified claims:** none

## 1. Summary

**Title:** Multi-task Learning and Calibration for Utility-based Home Feed Ranking
**Authors:** Ekrem Kocaguneli, Dhruvil Deven Badani, Sangmin Shin (Pinterest)
**Abstract:** Engineering blog describing Pinterest’s migration from single-output pinnability scoring to MTL with per-action calibrated probabilities fused via a tunable utility function, enabling faster business iteration and better interpretability.

**Key contributions:**
- MTL DNN with separate binary heads for click, long-click, close-up, repin (n=4 initially).
- Per-head calibration via feature-rich logistic regression mapping ranking-optimized scores to empirical rates.
- Utility-based ranking decoupling model training from business weight tuning.
- Extensions for video (>10s view) and negative engagement (hide with negative utility weight).

**Methodology:** Shared-parameter MTL with summed logistic losses; calibration pipeline from raw + feedview logs; three-step DNN replay for new model calibration; realtime and daily calibration monitoring.

**Main results:** MTL alone improved engagement before utility fusion; video head + utility increased video distribution 40%; hide head reduced hides via negative utility weight.

## 2. Experiment Critique

**Design:** Production engineering narrative; iterative A/B implied but no controlled experiment tables with numeric lifts for core feed metrics.

**Statistical validity:** Calibration evaluated on held-out day; online A/B details not specified in source.

**Online experiments (if any):** Business stakeholders adjust utility weights in treatment groups and observe effects within hours; prior multi-week retrain cycles avoided.

**Reproducibility:** No datasets, feature schemas, or model weights disclosed.

**Overall:** Strong systems pattern for calibrated multi-objective fusion; insufficient for quantitative benchmarking of long-term objectives.

## 3. Industry Contribution

**Deployability:** Production home feed at Pinterest scale with realtime calibration monitoring catching incidents before topline impact.

**Problems solved:** Non-comparable pinnability scores; slow business iteration; poor cross-Pin-type comparability (organic vs video).

**Engineering cost:** Separate calibration pipeline, replay infrastructure, and per-action monitoring; MTL task interference requires complementary objectives.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Utility decoupling from MTL predictions; calibration as transfer layer from stratified training to empirical rates; hide/video as plug-in MTL heads.

**Prior work comparison:** Standard weighted-loss single-head ranking; Platt scaling, isotonic regression, Facebook downsampling correction cited.

**Verification:** MTL and calibration are established; contribution is industrial integration and operational tooling at Pinterest home feed.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Pinterest production feed logs | Not public | No | 7-day calibration windows described |

**Offline experiment reproducibility:** Not specified in source.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** CTR-like engagement proxies (click, long-click, close-up, repin, video view, hide) fused via fixed/tunable utility weights—not retention, LTV, or revenue labels.

**(2) Credit assignment:** Per user–Pin impression; utility combines multi-head probabilities at ranking time; user-level delayed outcomes not specified in source.

**(3) Label and horizon definitions:** Immediate binary action labels per head; calibration uses 7-day training window; delay, sparsity, censoring for long-term outcomes not specified in source.

**(4) Short-term + long-term heads:** MTL multi-event heads with fixed/tunable linear utility fusion—no learned long-term head or session-level RL.

**(5) Prediction vs incrementality:** Predicts action probabilities; not effect of exposure on long-term outcome.

**(6) Offline and online evaluation:** Calibration offline metrics + production monitoring; qualitative online wins; no numeric retention A/B; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Evolves single weighted-loss ranker to MTL + calibration + separable utility layer—stays within engagement-proxy fusion, but decouples model iteration from business objective tuning.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Ekrem Kocaguneli, Dhruvil Deven Badani, Sangmin Shin
**Affiliations:** Pinterest (Homefeed Ranking)
**Venue:** Pinterest Engineering Blog
**Year:** 2020
**PDF:** unavailable (blog post)
**Relevance:** Core
**Priority:** 1
