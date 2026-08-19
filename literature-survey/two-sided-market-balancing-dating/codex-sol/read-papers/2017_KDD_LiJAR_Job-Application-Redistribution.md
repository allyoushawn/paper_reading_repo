# Paper Analysis: LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace

**Source:** http://theory.stanford.edu/~kngk/papers/LiJAR-SystemForJobApplicationRedistribution-KDD2017.pdf  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace  
**Authors:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi  
**Abstract:** LinkedIn's relevance-only job recommendation concentrated applications on already oversubscribed jobs while leaving other jobs underserved. LiJAR forecasts each job's final application count, then boosts relevant under-delivered jobs and exponentially penalizes over-delivered jobs in production ranking.

**Key contributions:**

- A dynamic Gamma-Poisson click-through-rate model plus Negative-Binomial future-impression forecast.
- Confidence-bound rules for early boosting and penalization with a relevance floor.
- A deployed offline/online architecture integrated with LinkedIn's GLMix ranking stack.
- Live evidence that redistribution improves application-distribution entropy without significantly reducing total applications.

**Methodology:** Daily Hadoop jobs learn forecast parameters and publish them to Voldemort. Online, Galene retrieval and GLMix scoring are followed by a forecast lookup. Jobs projected below `minApps` are boosted only above a relevance threshold; jobs projected above `maxApps` are exponentially downweighted as applications accumulate.

**Main results:** The full system increases applications to jobs with fewer than eight applications by 6.5%, decreases applications to jobs with more than 100 by 8.7%, changes total applications by a non-significant +2.3%, and increases application-distribution entropy by 12%.

## 2. Experiment Critique

**Design:** Forecasting is trained on 2015 logs and tested on September-December 2016. Offline baselines isolate day-of-week, full impression features, and full impression-plus-CTR features. The live A/B study separates boosting-only, penalization-only, and combined treatments from an unmodified GLMix control.

**Statistical validity:** The paper identifies statistically significant bucket effects and reports forecast recall/false-positive rates, but sample sizes, confidence intervals, test statistics, traffic shares, and experiment duration per arm are not specified in the source extraction. The bucket outcomes and entropy are well aligned to redistribution, while completed hires are not observed.

**Online experiments:** Combined LiJAR produces +6.5% applications in the underserved bucket, -8.7% in the overserved bucket, +2.3% total applications (not significant), and +12% entropy. An early version with no relevance threshold caused a significant total-application loss, demonstrating the need for the floor.

**Reproducibility:** Proprietary logs and production infrastructure are not public; code, hyperparameters beyond the described thresholds, and a public dataset are not specified.

**Overall:** The live results support the claim that forecast-driven score intervention can redistribute demand without a significant engagement loss. They do not establish application quality, hiring, retention, or interference-robust causal effects.

## 3. Industry Contribution

**Deployability:** High for an existing multi-stage recommender: LiJAR is a model-agnostic score adjustment after relevance scoring and uses familiar batch forecasts plus low-latency feature lookup.

**Problems solved:** Over-subscription, underserved supply, delayed feedback about eventual demand, and marketplace concentration.

**Engineering cost:** Daily probabilistic forecasting, real-time interaction counters, feature-store integration, confidence-bound calibration, and continuous relevance-floor monitoring.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Formulates application redistribution as an explicit career-marketplace objective and couples cumulative-demand forecasting with production score interventions.

**Prior work comparison:** GLMix provides the relevance baseline; Agarwal et al. provide spatiotemporal CTR models and LinkedIn budget pacing; CaS-MoS provides candidate selection; Lee et al. provide impression discounting; Arcaute and Vassilvitskii model stable matching in job markets.

**Verification:** Title, authors, affiliation, venue, deployment context, and reported effects are stated in the primary paper. No independent reproduction is specified.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| LinkedIn job recommendation logs | Not public | No | 2015 training data; September-December 2016 test logs. |
| LinkedIn Jobs Homepage live traffic | Not public | No | Production A/B tests on Jobs You May Be Interested In. |

**Offline experiment reproducibility:** Not independently reproducible from the source because code and proprietary data are unavailable.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Forecast the final likes/applications each recipient will receive; boost relevant profiles projected below a minimum and exponentially suppress profiles whose lower confidence bound already exceeds an upper demand target.

**Metrics and reported effect:** Forecast RMSE improves 7.5% versus the weekly baseline; boosting detects underdelivery at about 90% recall and 3% false positives, penalization at about 86% recall and 0.4% false positives. Live combined treatment shifts applications +6.5% to underserved jobs and -8.7% from overserved jobs while raising distribution entropy 12%.

**Capacity/congestion relevance:** Directly operationalizes soft recipient capacity through `minApps`/`maxApps` targets and uses early throttling before the item expires. It does not model mutual interest, reply probability, hard inbox limits, or interference-aware experimentation.

**Practical mapping:** Replace job applications with expected incoming likes or conversation starts, use a recipient-specific capacity forecast rather than fixed global thresholds, and retain LiJAR's relevance floor. Reciprocal like-back scoring would be an additional layer, not part of the paper.

**Dating fit: Medium.** This is the closest production analogue for redistributing attention away from overloaded recipients, but its outcome is unilateral application rather than mutual match or conversation.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi  
**Affiliations:** LinkedIn Corporation  
**Venue:** KDD 2017 Applied Data Science  
**Year:** 2017  
**PDF:** available  
**Relevance:** Core  
**Priority:** 1

## Annotated Bibliography Fields

- **Title:** LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace
- **Authors/organization:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi; LinkedIn
- **Year:** 2017
- **Venue/type:** KDD 2017 Applied Data Science; conference paper
- **Link:** http://theory.stanford.edu/~kngk/papers/LiJAR-SystemForJobApplicationRedistribution-KDD2017.pdf
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Built and deployed a cumulative-demand forecasting and reranking system for LinkedIn Jobs. It combines dynamic CTR estimation, future-impression forecasting, confidence intervals, relevance-gated boosting, and exponential penalization to move applications from jobs projected to be oversubscribed toward relevant jobs projected to remain underserved.
- **Mechanism relevant to two-sided balancing (≤50 words):** Forecast each recipient's end-of-horizon demand and intervene early: boost under-capacity recipients above a relevance floor and exponentially throttle recipients projected beyond capacity, reallocating attention without replacing the base relevance model.
- **Metrics and reported effect:** Full LiJAR: underserved applications +6.5%, overserved applications -8.7%, total applications +2.3% (not significant), distribution entropy +12%; forecast RMSE -7.5% versus IMP-WEEKLY.
- **Dating-app fit:** Medium — production-proven capacity-aware exposure redistribution, but unilateral and not match- or conversation-aware.
- **Confidence:** High — primary KDD paper describing a deployed LinkedIn system and live A/B results.
