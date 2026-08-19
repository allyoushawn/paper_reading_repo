# Paper Analysis: Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform

**Source:** https://arxiv.org/abs/2606.17397  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform  
**Authors:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Yuki Fujii, Shunsuke Ozeki, Shunya Noda  
**Abstract:** Myopically maximizing favorite probability on a spot-work platform concentrates exposure on popular job templates with little current capacity, while underexposing templates with unfilled jobs. The paper proposes Thresholded Eligibility Control (TEC), a parallelizable, capacity-responsive exposure controller, and evaluates it in calibrated simulations and a one-month prefecture-level production rollout on Timee.

**Key contributions:**

- Models favorite lists as stocks of latent worker demand for future short-lived job supply.
- Introduces capacity- and vacancy-responsive exposure scores, score capping, and parallel eligibility thresholds.
- Provides production field evidence that redistributing exposure increases realized matches and reduces the low-exposure tail.

**Methodology:** TEC carries a template score across rounds, adds score based on posted and unfilled capacity, subtracts score based on realized recommendations, caps any template's score at `P/c`, maps scores into eligibility thresholds, and admits a template when its threshold exceeds a worker-slot timing. A greedy fallback fills empty choice sets. The mechanism approximates adaptive quota allocation without sequential execution.

**Main results:** Calibrated simulations raise worker job-finding from 57.61% under Greedy to 70.03% and fill rate from 67.42% to 82.17%. In the field rollout, TEC adds 9.045 matches per prefecture-day (SE 4.374, `p<0.05`) and reduces the share of active template-days with at most three recommendations by 6.1 percentage points (95% CI `[-0.089,-0.030]`).

## 2. Experiment Critique

**Design:** Offline simulation compares Greedy, Static Quota, Adaptive Quota, and TEC using 838 Hokkaido templates and 1,000 workers. The production study assigns Aomori to TEC and Iwate to Greedy, with a January 2–11, 2026 pre-period and January 12–February 11 intervention.

**Statistical validity:** The prefecture-day difference-in-differences analysis uses date and prefecture fixed effects and HAC-adjusted standard errors. Distributional effects use saturated logit models and 500-replication weighted bootstrap confidence intervals. Only one treated and one control prefecture prevents reliance on large-cluster asymptotics.

**Online experiments:** The prefecture-level rollout deliberately avoids user-level randomization because workers compete for shared listings. The pool contains a few thousand users and just under ten thousand offerings in each prefecture; exact counts are confidential.

**Reproducibility:** Algorithm pseudocode and deployed parameters (`q-bar=40`, `w0=50`, `w1=125`) are provided. Public code, raw platform data, and a replication package are not specified in source.

**Overall:** The match and exposure-distribution effects support the central mechanism, but several stock outcomes are null during the 30-day window and the two-prefecture design limits uncertainty estimation and external validity.

## 3. Industry Contribution

**Deployability:** TEC was deployed on Timee and is explicitly parallelizable, avoiding the sequential bottleneck of random serial dictatorship quota allocation.

**Problems solved:** Misdirected exposure concentration, underfilled capacity, popular-but-scarce recommendations, and mismatch between intermediate favorites and downstream matches.

**Engineering cost:** Requires template-level state, frequent capacity/vacancy updates, score capping, threshold computation, exposure accounting, and a fallback path in an existing ranking stack.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A state-dependent, parallelizable exposure-control algorithm tied to changing capacity and accumulated favorite stocks, validated in a production matching market.

**Prior work comparison:** Manshadi et al. (2025) study equitable volunteer exposure; Crépon et al. (2013) establish displacement effects in labor-market experiments; Horton (2017) tests labor recommendations; Fernández-Val et al. (2024) provide distribution-regression DID; Rios et al. (2023) optimize assortments in dating. TEC targets high-frequency perishable jobs and updates exposure from current capacity and vacancy state.

**Verification:** The queried preprint supports the method, experiment, and comparisons. Independent web novelty verification was not part of this source-scoped batch.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Timee Hokkaido templates | Not specified | No | 838 active templates used for calibration. |
| Timee Aomori/Iwate rollout | Not specified | No | Proprietary field data; exact samples confidential. |

**Offline experiment reproducibility:** The simulation framework and parameters are described, but proprietary inputs and code are unavailable.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Replace an engagement-only ranker with a stateful exposure controller. Increase a profile's allocation when it has usable capacity, decrease it when it has already received recommendations, cap dominance, and enforce exposure through per-slot eligibility thresholds.

**Metrics and reported effect:** Simulation job-finding rises 57.61%→70.03% and fill rate 67.42%→82.17%. The field rollout adds 9.045 matches per prefecture-day and reduces the mass of template-days with at most three recommendations by 6.1 points. Aggregate favorites, subscriber stock, and active-offering fill rate are statistically unchanged; conversations and retention are not specified.

**Capacity/congestion relevance:** Jobs are scarce, short-lived, and capacity-constrained. Favorite lists are latent-demand stocks, while additional subscribers have diminishing value once openings fill. TEC uses posted and unfilled capacity directly in its score updates.

**Practical mapping:** A profile's recent reply/conversation capacity can replace job vacancies; impressions consume the score; likes become a demand stock. Dating requires replacing unilateral first-come-first-served hiring with reciprocal choice and measuring mutual matches, conversations, and two-sided retention.

**Dating fit: Medium.** Capacity-responsive exposure and interference-aware field design transfer directly, but Timee matching is unilateral and first-come-first-served rather than double opt-in.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Yuki Fujii, Shunsuke Ozeki, Shunya Noda  
**Affiliations:** The University of Tokyo; Timee, Inc.  
**Venue:** arXiv  
**Year:** 2026  
**PDF:** available via arXiv  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform
- **Authors/organization:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Yuki Fujii, Shunsuke Ozeki, Shunya Noda; The University of Tokyo and Timee
- **Year:** 2026
- **Venue/type:** arXiv; preprint and production field experiment
- **Link:** https://arxiv.org/abs/2606.17397
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Designed Thresholded Eligibility Control, a parallel exposure controller that updates job-template allocation from posted and unfilled capacity and past recommendations. Calibrated simulations compare Greedy and quota policies; a one-month prefecture-level production rollout on Timee measures matches, favorite stocks, fill rates, and exposure distribution.
- **Mechanism relevant to two-sided balancing (≤50 words):** Convert capacity and vacancy into stateful exposure scores, cap any one recipient's dominance, and expose a recipient only when its eligibility threshold exceeds a randomized slot timing. This redirects impressions from popular but capacity-poor options toward underserved options with usable capacity.
- **Metrics and reported effect:** Simulation job-finding 57.61%→70.03% and fill rate 67.42%→82.17%. Field effect: +9.045 matches per prefecture-day and -6.1 points in the low-exposure tail; several favorite/subscriber/fill outcomes are null.
- **Dating-app fit:** Medium — direct capacity-aware exposure and interference-aware evidence, but FCFS one-sided hiring must become reciprocal matching.
- **Confidence:** High — exact source-scoped preprint and production-study evidence, with design limitations disclosed.
