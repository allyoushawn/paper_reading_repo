# Paper Analysis: A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications

**Source:** https://research.duolingo.com/papers/yancey.kdd20.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications
- **authors or company:** Kevin P. Yancey, Burr Settles (Duolingo)
- **venue:** KDD
- **year:** 2020
- **URL:** https://research.duolingo.com/papers/yancey.kdd20.pdf
- **source type:** industry paper
- **direction:** D4
- **problem setting:** Notification template selection (not feed ranking) to maximize lesson completion and retention.
- **objective and label definition:** Binary reward \(r_t=1\) if user completes a lesson within 2 hours of notification; long-term metrics include DAU, lessons completed, D1/D7 retention.
- **prediction or incrementality:** Estimates relative template lift (difference scoring) with recency penalty; deployed as bandit policy, not supervised LTV model.
- **model architecture:** Recovering Difference Softmax: weighted importance-sampled \(\hat{s}_a\), empirical Bayes shrinkage, exponential recency penalty, softmax selection over eligible arms.
- **credit assignment:** User-level binary outcome attributed to the single selected notification template within a 2-hour window; user arm history tracks recency.
- **training data and counterfactual handling:** Off-policy logs from uniform-random legacy policy; importance sampling with truncation (\(\theta=0.5\%\)); rolling history window by credible-interval width.
- **offline and online evaluation:** Offline weighted off-policy eval on 114M-row test set; online A/B vs optimized uniform-random baseline; 5% holdout after 5 months.
- **reported gains:** Offline +1.9% reward vs random; online +0.5% DAU, +0.4% lessons, +2.0–2.2% new-user D1/D7 retention; holdout +2.5% reward after 5 months.
- **applicability note for a two-sided dating recommender:** Difference scoring for sleeping arms maps to template-level push/re-engagement where eligibility (streak, match state) confounds raw CTR—relevant for retention notification optimization.
  The 2-hour attribution window and recency penalty are concrete label/loss choices for linking short-delay actions to notification decisions without claiming full LTV credit.
- **unverified claims:** none

## 1. Summary

Duolingo optimizes daily practice-reminder push notifications with the Recovering Difference Softmax bandit, addressing sleeping arms (conditional template eligibility) and recovering arms (novelty decay when templates repeat). The algorithm estimates each template’s relative lift via importance-sampled difference between used vs eligible-but-not-used rewards, regularizes with empirical Bayes, applies an exponential recency penalty, and selects via softmax. Deployed at scale, it improved DAU, lesson volume, and especially new-user retention over a strong uniform-random baseline.

## 2. Experiment Critique

Strengths: massive logs (88M train / 114M test), off-policy evaluation with exploration-cost analysis, ablations on recency and template+language arms, multi-month holdout monitoring, and honest discussion of organic-noise confounding. Weaknesses: reward is short-horizon (2h) and diluted for DAU; sleeping-arm confounding only partially addressed; daily batch scorer adds feedback delay; dependence on legacy random logging policy for unbiased training data.

## 3. Industry Contribution

Practical production architecture (decision log, user arm history KV, daily Spark scorer, online selector) for notification bandits at millions of sends/day. Cognitively motivated recency penalty prevents convergence to a single template—a common failure mode in engagement bandits.

## 4. Novelty vs. Prior Work

Combines sleeping bandits, recovering bandits, importance sampling for off-policy evaluation (Li et al.), empirical Bayes stabilization, and softmax exploration. Distinct from standard MAB by jointly handling eligibility confounding and template fatigue without encoding eligibility rules in the bandit structure.

## 5. Dataset Availability

Proprietary Duolingo notification logs; 5% uniform holdout introduced post-launch for ongoing unbiased data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Optimizes notification template selection for lesson completion (2h) and tracks DAU, lessons, D1/D7 retention. CTR not specified. LTV/revenue: not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Outcome (lesson within 2h) assigned to the selected notification template; user arm history updated for recency. Slate-level or feed-item credit: not specified in source.

### (3) Label and horizon definitions; delay, sparsity, censoring
Label: binary 2-hour post-notification lesson completion. Long-term retention tracked in A/B. Scorer runs daily (batch delay). Organic activity adds noise/sparsity to true notification effect. Censoring: not specified in source.

### (4) Short vs long-term head fusion
Recency penalty models short-term template fatigue; no multi-horizon prediction heads. Separate short (2h reward) vs long (DAU/retention) evaluation only.

### (5) Prediction vs incrementality
Estimates relative template lift via difference scoring (used vs counterfactual eligible-not-used); operational bandit policy rather than user-level outcome prediction.

### (6) Offline and online evaluation
Offline off-policy eval on historical random logs. Online A/B vs optimized uniform baseline; 5-month holdout shows +2.5% reward persistence.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Replaced legacy uniform-random selector with bandit scorer+selector pipeline. Broader CTR→LTV migration: not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Kevin P. Yancey, Burr Settles
**Affiliations:** Duolingo
**Venue:** KDD
**Year:** 2020
**PDF:** https://research.duolingo.com/papers/yancey.kdd20.pdf
**Relevance:** Core
**Priority:** 1
