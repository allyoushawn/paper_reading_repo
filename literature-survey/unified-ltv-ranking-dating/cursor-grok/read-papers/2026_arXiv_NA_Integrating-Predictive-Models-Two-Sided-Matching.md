# Paper Analysis: Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach

**Source:** https://arxiv.org/pdf/2602.19689.pdf
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach
- **authors or company:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa (MiDATA/CoupLink), Shunya Noda (University of Tokyo)
- **venue:** arXiv
- **year:** 2026
- **URL:** https://arxiv.org/pdf/2602.19689.pdf
- **source type:** industry-academic partnership (CoupLink dating platform)
- **direction:** D8
- **problem setting:** Japanese dating platform CoupLink (>1.5M cumulative users): proposers (primarily men) receive daily AI-recommended receiver lists; naive ranking by predicted dating rates concentrates exposure on highly responsive receivers, causing congestion and overstated match efficiency.
- **objective and label definition:** Integrator maps ML predictions (proposer login, proposer like, receiver login, receiver relike) into many-to-many recommendations; primary evaluation metrics are average dates, **effective dates** (congestion-discounted matches), and dating probability per proposer/receiver; dating rate δ_{ij} = product of four predicted probabilities.
- **prediction or incrementality:** Uses production gradient-boosted tree classifiers (AUC 0.80–0.92) to predict behavioral probabilities; integrators combine predictions into matchings — not causal incrementality of a recommendation on retention.
- **model architecture:** Compares One-sided (top-k by dating or like rates), deferred acceptance (DA), and **exposure-constrained deferred acceptance (ECDA)** where receiver capacity is defined on expected likes or dates (not headcount); greedy implementation when ROLs sorted by dating rates.
- **credit assignment:** Recommendation-level matching under capacity constraints; no delayed retention or revenue attribution to individual impressions.
- **training data and counterfactual handling:** Calibrated simulations on CoupLink production predictions; regional field experiment (Kanto treatment vs. Kansai/Tokai controls) with difference-in-differences; IRB-approved, AEA RCT pre-registered (AEARCTR-0015446).
- **offline and online evaluation:** Offline simulation on CoupLink data: ECDA (date-exposure, cap=1.5) achieves highest average effective dates (0.0623) vs. current recommender (0.0584) while reducing average dates; field experiment Jan 2026 deployment of ECDA with date exposure.
- **reported gains:** Simulation: ECDA improves effective dates and receiver-side dating probability despite fewer total dates. Field DID (excluding top 0.1% receiver-days): statistically significant positive effects on average effective dates, dating probabilities, and receiver likes; full-sample messaging effects ambiguous due to extreme-tail congestion.
- **applicability note for a two-sided dating recommender:** **Direct precedent** — same proposer/receiver like→match funnel; ECDA is a concrete integrator pattern for combining CTR/CVR-like predictions under receiver congestion caps instead of naive top-k by match probability.
- **applicability note for a two-sided dating recommender:** Optimizes early-stage matching efficiency and equity, not 7–30 day retention or subscription revenue; downstream messaging effects mixed when extreme popular receivers included.
- **unverified claims:** none

## 1. Summary

**Title:** Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach
**Authors:** Sekiya et al. (University of Tokyo + CoupLink/MiDATA)
**Abstract:** Models two-sided dating recommendation as many-to-many matching; introduces effective dates and ECDA integrator; validates via CoupLink simulations and a large regional field experiment.

**Key contributions:**
- Effective dates: congestion-adjusted outcome discounting matches involving overloaded receivers.
- ECDA: capacity limits on expected likes/dates rather than headcount in deferred acceptance.
- Production deployment and DID field experiment on CoupLink (Kanto vs. control regions).

**Methodology:** Four production GBDT predictors → dating rates → integrators (One-sided, DA, ECDA); simulation calibration; regional A/B with event-study and DID.

**Main results:** ECDA increases effective dates and receiver dating probability in simulation and field (after trimming top 0.1% receiver-days); total dates may decline while equity improves.

## 2. Experiment Critique

**Design:** Strong pairing of calibrated simulation and pre-registered regional field experiment; transparent discussion of tail-receiver distortion on aggregate messaging metrics.

**Statistical validity:** DID with area and day fixed effects; significance stars on predicted and realized outcomes; 0.1% receiver-day trim as mechanism check.

**Online experiments (if any):** Regional deployment in Kanto (treatment) vs. Kansai and Tokai (control), Jan 13 2026 onset; user cross-area mobility negligible (0.003%).

**Reproducibility:** CoupLink data proprietary; predictive model features proprietary; IRB and RCT registry documented.

**Overall:** Rare live dating-platform evidence for congestion-aware integrator design; retention/LTV not measured.

## 3. Industry Contribution

**Deployability:** ECDA with dating-rate sorting reduces to greedy sort + linear scan — feasible at CoupLink scale; production ML models unchanged, only integrator swapped.

**Problems solved:** Receiver-side congestion from naive top-k dating-rate ranking; misleading total-dates metric that ignores overload costs.

**Engineering cost:** Moderate — replaces One-sided integrator with capacity-constrained matching; capacity tuning required (simulation: optimal date-exposure cap ≈1.5).

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Effective dates metric; ECDA with exposure-weighted capacities; field validation on real dating platform.

**Prior work comparison:** Hitsch et al. (online dating), Horton (job platforms), deferred acceptance literature, reciprocal recommender systems, congestion in matching markets.

**Verification:** Simulation and field DID align on effective-dates direction; messaging ambiguity resolved by tail trimming analysis.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CoupLink production logs | Proprietary | No | >1.5M cumulative users; simulation + field experiment |

**Offline experiment reproducibility:** Not reproducible without CoupLink data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**High relevance for D8 and dating reciprocity/congestion; moderate for unified LTV ranking.**

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Predicted dating probability integrated under capacity constraints; effective dates as congestion-aware welfare metric — not retention/revenue. |
| **(2) Credit assignment** | Matching-level allocation; no per-exposure delayed outcome attribution. |
| **(3) Label / horizon; delay / sparsity / censoring** | Login (1-day proposer / 7-day receiver), like, relike predictions; post-match messaging tracked but not long-horizon retention. |
| **(4) Short-term vs long-term head fusion** | Single integrator over four prediction heads (login × like × relike chain). |
| **(5) Prediction vs incrementality** | Predictive probabilities fed to matching mechanism; not uplift of exposure on retention. |
| **(6) Offline / online eval** | Calibrated simulation + regional DID field experiment. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Core focus: bilateral likes → dates, receiver congestion, exposure equity; revenue not stated. |
| **(8) CTR → unified long-term migration** | Template for replacing post-hoc score blend with principled integrator over existing predictors — but objective remains match efficiency, not LTV. |

Closest D8 dating reference for how to integrate like/match predictors under receiver capacity limits.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda
**Affiliations:** University of Tokyo; MiDATA Co., Ltd. / CoupLink
**Venue:** arXiv (econ.GN)
**Year:** 2026
**PDF:** https://arxiv.org/pdf/2602.19689.pdf
**Relevance:** Core
**Priority:** 1
**Card date:** 2026-08-17
**Workplace:** cursor-grok
**Reader:** PDF only
