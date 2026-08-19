# Paper Analysis: Handling many conversions per click in modeling delayed feedback

**Source:** https://arxiv.org/pdf/2101.02284.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Handling many conversions per click in modeling delayed feedback
- **authors or company:** Ashwinkumar Badanidiyuru, Andrew Evdokimov, Vinodh Krishnan, Pan Li, Wynn Vonnegut, Jayden Wang (Google Research / Google)
- **venue:** arXiv (ADKDD 2021 presentation)
- **year:** 2021
- **URL:** https://arxiv.org/abs/2101.02284
- **source type:** industry paper
- **direction:** D7
- **problem setting:** Performance display advertising must predict expected post-click conversion count or value when multiple conversions per click (MPC) occur with advertiser-specific, long-tailed, non-parametric, time-varying delay (attribution window 2 hours–90 days); online training on immature labels systematically under-predicts.
- **objective and label definition:** Label \(y_p \in [0,\infty)\) = total count or value of post-click events attributed to last click within window \(M\); delayed features \(L_p\) include partial labels in \([t_p, t_p+d_i)\); sub-models \(f_i\) predict thermometer-encoded cumulative label from delay bucket start to \(M\).
- **prediction or incrementality:** Poisson regression predicting expected conversion count per click—absolute expectation, not incrementality.
- **model architecture:** Stack of \(n\) sub-models \(f_0 \ldots f_n\) on shared DNN embeddings; delay buckets \([t_p, t_p+d_1), \ldots, [t_p+d_n, t_p+M)\); thermometer encoding (overlapping cumulative buckets); auxiliary input = label-so-far in \([t_p, t_p+d_i)\); separate sub-models per bucket to avoid catastrophic forgetting in sequential online training; 3–10 buckets typical.
- **credit assignment:** Last-click attribution; partial labels and "label so far" feature map immature observations to unbiased completed-label estimate \(y'_{p,t_k}\).
- **training data and counterfactual handling:** Each \(f_i\) trains only on examples with age \(\geq t_p + d_{i+1}\) (mature bucket label); incomplete tail replaced by sub-model predictions for unbiased label completion; auxiliary \(L_p([t_p, t_p+d_i))\) conditions delay distribution for drift.
- **offline and online evaluation:** App-install ad logs (commercial mobile app store); online sequential training (train-then-evaluate per example); metrics Poisson log loss and bias (prediction / mature label). Slices: all data, 90th-percentile delay campaigns, campaigns <10 days old. No exact bias numbers reported (proprietary); bias stated \(\leq 1\%\).
- **reported gains:** Poisson log loss improvement vs M3 (mature-only baseline): all data −8.6%; long-delay advertisers −10.16%; new advertisers (<10 days) −1.81%; Oracle upper bound −9.1% / −10.87% / −2.0%. Proposed model closest to neutral bias among online-training variants; beats M4 (no thermometer) and M5 (no auxiliary) on accuracy and calibration.
- **applicability note for a two-sided dating recommender:** Extends delayed-feedback correction to multi-event outcomes (multiple messages, dates, or revenue events per match funnel click) via bucketed mature-label training and partial-label completion.
  Single-sided ad conversion optimizer; no reciprocity, match-market balance, or subscription LTV fusion.
- **unverified claims:** none

## 1. Summary

Google proposes an unbiased online-training estimator for many-conversions-per-click when delay distributions are heterogeneous, long-tailed, and non-parametric. Three ideas: (1) split total label into delay buckets with sub-models trained only on mature bucket labels; (2) thermometer encoding (cumulative overlapping buckets) to combat sparsity and reduce inference cost; (3) auxiliary "label so far" features for stable label completion under distribution drift. Poisson DNN regression on app-install post-click events; ablations vs naive delay neglect, multi-delay training, mature-only, and oracle complete labels.

## 2. Experiment Critique

Strengths: addresses MPC gap left by DFM/FSIW/TS-DL; handles float-valued labels and retractions (extension described); strong gains on new and long-delay campaign slices. Weaknesses: proprietary dataset—no public numbers for bias or absolute log loss; qualitative bias plots only; Poisson assumption breaks if negative bucket labels from retractions (workaround described but not fully evaluated).

## 3. Industry Contribution

Production-oriented online training at Google scale; 3–10 bucket practical guidance; thermometer encoding cuts serving cost vs disjoint buckets. Extends to conversion value prediction with minimal changes.

## 4. Novelty vs. Prior Work

Beyond single-conversion DFM (Chapelle 2014), FSIW (Yasui 2020), TS-DL (Su 2020). Contrasts with Choi et al. 2020 negative-binomial survival MPC approach (integer-only, non-convex, poor for online). Complements Defer continuous-training pipeline for count-valued outcomes.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| App install ad logs | Google internal | No | Last-click attribution |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Expected post-click event count/value—closer to LTV than binary CVR but still single-sided.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Last-click attribution with partial-label completion across delay buckets.

### (3) Label and horizon definitions; delay, sparsity, censoring
Attribution window up to 90 days; immature-label bias corrected via mature-bucket sub-models and auxiliary partial labels.

### (4) Short vs long-term head fusion
Sum of bucket sub-model predictions; no neural multi-horizon fusion.

### (5) Prediction vs incrementality
Expected conversion count (Poisson mean).

### (6) Offline and online evaluation
Sequential online-training evaluation protocol; slice analysis for new/long-delay campaigns.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
When dating outcomes are repeat events (messages, dates) per impression, bucketed delay completion generalizes binary delayed-feedback rankers.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Ashwinkumar Badanidiyuru, Andrew Evdokimov, Vinodh Krishnan, Pan Li, Wynn Vonnegut, Jayden Wang
**Affiliations:** Google Research; Google
**Venue:** arXiv 2021 / ADKDD 2021
**Year:** 2021
**PDF:** https://arxiv.org/pdf/2101.02284.pdf
**Relevance:** Core
**Priority:** 2
