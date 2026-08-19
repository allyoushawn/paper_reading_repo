# Paper Analysis: Modeling Impression Discounting in Large-Scale Recommender Systems

**Source:** http://archive.gersteinlab.org/meetings/s/2014/08.28/kdd2014-i0kdd-meeting-materials/docs/p1837.pdf  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Modeling Impression Discounting in Large-Scale Recommender Systems  
**Authors:** Pei Lee, Laks V. S. Lakshmanan, Mitul Tiwari, Sam Shah  
**Abstract:** Repeatedly showing an ignored item wastes recommendation slots and crowds out fresh alternatives. The paper adds a model-agnostic post-processing plugin that discounts a base score using impression count, time since last exposure, position, and user activity, and fits decay curves with density-weighted robust regression.

**Key contributions:**

- Defines per-user/item impression sequences as implicit negative feedback.
- Learns linear, inverse, exponential, and quadratic discount functions.
- Introduces density-based noise pruning and density-weighted regression for billion-scale skewed logs.
- Validates the plugin offline and in a live LinkedIn People You May Know experiment.

**Methodology:** The plugin multiplies the original score by a normalized predicted conversion-rate decay. Linear or multiplicative aggregation combines behavior curves. Density-weighted ridge regression reduces the influence of sparse, volatile tail observations.

**Main results:** A four-behavior offline model raises PYMK Precision@10 by 31.3%. The best live two-behavior treatment raises invitation Precision@10 by 13.26% ± 0.2%. Density weighting reduces fit RMSE from 0.1121 to 0.0188.

## 2. Experiment Critique

**Design:** Three large datasets—LinkedIn PYMK, LinkedIn Skill Endorsements, and Tencent SearchAds—test different sequence lengths and user stickiness. Baselines include no discounting, ordinary least squares, and multiple decay-function combinations; the online test compares standard production scoring with a discounting treatment.

**Statistical validity:** Dataset scale is exceptional and the live lift includes ±0.2%, but the source extraction does not specify randomization details, duration, sample size by arm, guardrails, or correction for repeated model comparisons. Precision/invitation is unilateral and does not measure downstream reciprocal acceptance.

**Online experiments:** In PYMK, inverse LastSeen plus exponential ImpCount improves P@10 by 13.26% ± 0.2% over control; two other decay combinations improve it by 11.97% and 12.18%.

**Reproducibility:** Tencent SearchAds is public. LinkedIn logs and code are not specified as public; environment, seeds, and a complete hyperparameter package are not specified.

**Overall:** The evidence strongly supports discounting repeated ignored impressions for unilateral conversion. It does not support claims about recipient capacity, total matches, conversations, or retention.

## 3. Industry Contribution

**Deployability:** High as a post-ranking multiplier independent of the base model. It needs per-pair impression history and a small curve-scoring component rather than retraining the main recommender.

**Problems solved:** Feed staleness, repeat ignored candidates, crowded top slots, and noisy behavioral curve estimation.

**Engineering cost:** Impression-history storage, online counters, periodic curve refitting, and monitoring of sparse-tail behavior.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A general impression-discounting plugin and density-aware regression for repeated-exposure effects at large scale.

**Prior work comparison:** Hu, Koren, and Volinsky ground implicit feedback; Koren grounds factorization and neighborhood models; Agichtein et al. use behavior in ranking; Agarwal et al. and Richardson et al. model click-through rate; Ester et al. provide density-based noise detection.

**Verification:** The primary paper states its title, authors, affiliations, KDD venue, model design, datasets, and results. Independent implementations are not specified.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| LinkedIn People You May Know | Not public | No | 1.08 billion impressions. |
| LinkedIn Skill Endorsements | Not public | No | 0.19 billion impressions. |
| Tencent SearchAds | http://www.kddcup2012.org/c/kddcup2012-track2 | Yes | 0.15 billion impression sequences; KDD Cup 2012 Track 2. |

**Offline experiment reproducibility:** Partial only; the public SearchAds dataset is available, but code and LinkedIn datasets are not specified.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Discount a user-profile pair after repeated non-converting impressions, allowing unseen or less-exposed candidates to replace stale entries. The intervention is local to the viewer and preserves the upstream model.

**Metrics and reported effect:** PYMK offline P@10 +31.3% with four behaviors; live P@10 +13.26% ± 0.2% with inverse LastSeen and exponential ImpCount; density-weighted regression RMSE 0.1121→0.0188.

**Capacity/congestion relevance:** It protects viewer attention from repeated ignored items, but recipient reply capacity, popularity congestion, mutual liking, wasted likes, match distribution, and interference are **Not specified in source.**

**Practical mapping:** Use impression discounting as a freshness/attention feature inside a broader reciprocal and capacity-aware ranker, not as the market-balancing objective itself.

**Dating fit: Low.** The mechanism is operationally useful but unilateral and explicitly optimized around viewer conversion rather than mutual match or reply capacity.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2017_KDD_LiJAR_Job-Application-Redistribution.md](./2017_KDD_LiJAR_Job-Application-Redistribution.md) | Novelty vs. Prior Work — Background | Attributes impression discounting to Lee et al. |

## Meta Information

**Authors:** Pei Lee, Laks V. S. Lakshmanan, Mitul Tiwari, Sam Shah  
**Affiliations:** University of British Columbia; LinkedIn Corporation  
**Venue:** KDD 2014 Applied Data Science  
**Year:** 2014  
**PDF:** available  
**Relevance:** Core  
**Priority:** 1

## Annotated Bibliography Fields

- **Title:** Modeling Impression Discounting in Large-Scale Recommender Systems
- **Authors/organization:** Pei Lee, Laks V. S. Lakshmanan, Mitul Tiwari, Sam Shah; University of British Columbia and LinkedIn
- **Year:** 2014
- **Venue/type:** KDD 2014; conference paper
- **Link:** http://archive.gersteinlab.org/meetings/s/2014/08.28/kdd2014-i0kdd-meeting-materials/docs/p1837.pdf
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Analyzed repeated non-converting impressions at LinkedIn and Tencent, learned parametric decay functions from impression count, recency, position, and user frequency, and applied the result as a model-agnostic score multiplier. Density-based pruning and weighted regression stabilize curve fitting on highly skewed billion-scale logs.
- **Mechanism relevant to two-sided balancing (≤50 words):** Repeatedly ignored user-item pairs receive a smaller score, freeing scarce ranking positions for fresh or under-exposed alternatives. The mechanism budgets viewer attention but does not account for the shown user's capacity.
- **Metrics and reported effect:** PYMK offline P@10 +31.3%; live invitation P@10 +13.26% ± 0.2%; density-weighted fit RMSE 0.1121→0.0188. Match, conversation, distribution, and retention effects are not specified.
- **Dating-app fit:** Low — useful anti-staleness component, but no reciprocity or recipient-load model.
- **Confidence:** High — primary KDD industry paper with large offline datasets and a live production test.
