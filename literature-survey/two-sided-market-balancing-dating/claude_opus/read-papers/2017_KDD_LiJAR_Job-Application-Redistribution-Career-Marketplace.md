# Paper Analysis: LiJAR — A System for Job Application Redistribution towards Efficient Career Marketplace

**Source:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi (LinkedIn Corporation), KDD 2017 (Applied Data Science Track), NotebookLM source_id `11b0d239-3d33-4e8a-a366-5c87b64a3d42`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace
**Authors:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi
**Abstract:**
LinkedIn observed that its job-recommendation system, when purely optimized for user engagement (apply-probability via GLMix), causes some job postings to receive far too many applications (recruiter overload, wasted seeker effort, low per-seeker odds) while others receive too few (employer dissatisfaction, contract non-renewal). LiJAR is a production system that forecasts, for each job, the expected number of applications by expiration with a confidence interval, and then boosts under-forecast jobs / penalizes over-forecast jobs in real-time ranking to redistribute applications toward marketplace balance without hurting relevance.

**Key contributions:**
- A two-stage dynamic forecasting model: per-job CTR via a Gamma-Poisson dynamic model (exponentially discounted recency weighting) × future impression volume via a feature-based Poisson/Negative-Binomial model, combined (independence approximation) into a 95% confidence interval for total applications at expiration.
- Real-time score-adjustment rules: exponential-decay penalization (`newScore = originalScore · e^(-#applications/softness)`) for over-forecast jobs; multiplicative boosting (`newScore = min(originalScore · boostFactor, 1.0)`, gated by a relevance floor `h`) for under-forecast jobs.
- Full production architecture (offline Hadoop retraining → Voldemort parameter store → online GLMix scoring → forecasting module → boosting/penalization post-processing layer) deployed at LinkedIn scale.

**Methodology:**
Bayesian dynamic forecasting (Gamma-Poisson for CTR with a variance-discounting recency parameter δ; Negative Binomial for impression-volume forecasting via a Poisson regression with a Gamma-distributed job-specific multiplier) combined via an independence approximation to get application-count confidence intervals; intervention layer applies exponential-decay penalization or multiplicative boosting (with a relevance floor) to the baseline GLMix ranking score based on forecast vs. `[minApps, maxApps]` thresholds.

**Main results:**
Offline: IMP-CTR-FULL forecasting model reduced RMSE by 7.5% vs. IMP-WEEKLY baseline (6.3% for IMP-FULL); ~90% recall/~3% FPR for boosting classification, ~86% recall/~0.4% FPR for penalization classification. Online A/B (Sep–Dec 2016): joint boosting+penalization increased applications to underserved jobs (Bucket 1) by 6.5%, reduced over-served-job (Bucket 3) applications by 8.7%, with total applications flat/slightly positive (+2.3%, not significant). Application-distribution entropy increased 12% relative to control, indicating meaningfully more even redistribution across the marketplace.

---

## 2. Experiment Critique

**Design:** Both offline (train on 2015 data, test on Sep–Dec 2016) and online production A/B testing (control = pure-relevance GLMix, vs. boosting-only, penalization-only, and boosting+penalization arms), with buckets defined by application-count thresholds (`minApps=8`, `maxApps=100`).

**Statistical validity:** Reports p-values for some deltas (e.g., total-applications change for boosting+penalization: +2.3%, p=0.1, not significant; Bucket 2 gain +3%, p=0.05). Several headline numbers (Bucket 1, Bucket 3 changes) are reported without explicit p-values in the excerpted text but framed as the key significant effects. Reasonably rigorous for an industry systems paper — real A/B testing with named parameter settings (`boostFactor=1.05`, `h=0.8`, `softness=300`).

**Online experiments (if any):** Yes — described above; also an explicit failure case reported (see Limitations) where an initial boosting design with no relevance floor (`h=0`) caused a significant loss of total applications, which the authors diagnose and fix.

**Reproducibility:** Model equations, architecture diagram, and parameter values are given in detail; however, training data (LinkedIn's internal 2015–2016 interaction logs) is not public, so full reproduction is not possible outside LinkedIn.

**Overall:** Strong industry-methodology paper — real production deployment, both offline predictive accuracy and online causal (A/B) evidence, explicit negative result reported and diagnosed (see below). Claims are well supported by the presented evidence.

---

## 3. Industry Contribution

**Deployability:** Already deployed in production as part of LinkedIn's job recommendation engine ("Jobs You May Be Interested In").

**Problems solved:** Marketplace liquidity / two-sided satisfaction problem in a job marketplace — directly analogous in structure to the project's dating-market problem (a scarce-capacity side gets over/under-subscribed under pure relevance-only ranking).

**Engineering cost:** Moderate-to-high — requires daily offline retraining (Hadoop), a low-latency parameter store (Voldemort) for online serving, and an additional real-time forecasting + score-adjustment layer inserted into the existing ranking pipeline (GLMix). Described as incremental on top of an existing large-scale ranking system rather than a ground-up rebuild.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Framing job recommendation as requiring *marketplace-level* application redistribution rather than pure unilateral relevance/engagement optimization — explicitly distinguished from item-recommendation settings (books/movies) where one item can be shown to unlimited users, versus a job posting with effectively fixed hiring capacity.

**Prior work comparison (top cited works per source):**
1. Zhang et al. 2016, "GLMix: Generalized Linear Mixed Models For Large-Scale Response Prediction" (KDD) — the baseline ranking model LiJAR sits on top of.
2. Borisyuk et al. 2016, "CaS-MoS: A Framework for Learning Candidate Selection Models over Structured Queries and Documents" (KDD) — candidate retrieval stage.
3. Agarwal, Chen, Elango 2009, "Spatio-temporal Models for Estimating Click-through Rate" (WWW) — source of the dynamic Gamma-Poisson CTR model.
4. Sriram & Makhani 2014, "LinkedIn's Galene Search engine" — underlying search/retrieval platform.
5. Lee, Lakshmanan, Tiwari, Shah 2014, "Modeling Impression Discounting in Large-scale Recommender Systems" (KDD) — related but distinct (single-viewer over-exposure discounting vs. LiJAR's marketplace-wide redistribution).
6. Sumbaly et al. 2012, "Serving Large-scale Batch Computed Data with Project Voldemort" (FAST) — parameter-store infrastructure.
7. Agarwal, Agrawal, Khanna, Kota 2010, "Estimating rates of rare events with multiple hierarchies through scalable log-linear models" (KDD) — Negative Binomial impression-forecasting foundation.

**Verification:** Novelty claim (marketplace-aware redistribution vs. pure engagement optimization) is credible and well distinguished from the closest related idea (impression discounting), which the authors explicitly note solves a different problem (single-item over-exposure to a single user, not marketplace-wide supply/demand balancing).

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| LinkedIn "Jobs You May Be Interested In" interaction logs, 2015 (exploratory) and Sep–Dec 2016 (train/test/online) | — | Not accessible (internal/proprietary) | No public release; industry-internal telemetry only |

**Offline experiment reproducibility:** Not reproducible outside LinkedIn — proprietary data, though the model equations and architecture are fully specified.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi
**Affiliations:** LinkedIn Corporation, USA
**Venue:** KDD 2017 (Applied Data Science Track)
**Year:** 2017
**PDF:** Not fetched directly — analyzed via NotebookLM source; not accessed as local file
**Relevance:** Core — directly transferable exposure-redistribution mechanism for an adjacent capacity-limited two-sided marketplace
**Priority:** 1 (per queue tier)

---

## Bibliography Fields

- **title:** LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace
- **authors or organization:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi — LinkedIn Corporation
- **year:** 2017
- **venue or type:** KDD 2017, Applied Data Science Track
- **link:** https://doi.org/10.1145/3097983.3098131 (KDD 2017 proceedings)
- **tier tag:** Tier 1 — Adjacent marketplace (job/career), directly relevant to capacity-aware exposure allocation
- **what they did (≤80 words):** Built and deployed LiJAR at LinkedIn: a forecasting model predicts each job posting's expected total applications by expiration (with confidence interval, via a Gamma-Poisson CTR model × Negative-Binomial impression-volume model), then a real-time layer boosts (multiplicative, relevance-floor-gated) under-forecast jobs and exponentially penalizes over-forecast jobs in the ranking score, redistributing applications toward marketplace balance without materially reducing relevance or total engagement.
- **mechanism relevant to two-sided balancing (≤50 words):** Forecast-driven, capacity-aware score adjustment (boost/penalize) applied post-hoc to a relevance ranker — a direct template for redistributing exposure away from over-subscribed profiles toward under-exposed ones in a dating app, with job capacity mapping to reply capacity.
- **metrics used, and the reported effect:** Offline RMSE (7.5% reduction vs. baseline forecaster); online A/B: +6.5% applications to underserved jobs, -8.7% to over-served jobs, total applications flat (+2.3%, ns); application-distribution entropy +12% (marketplace-wide evenness).
- **fit for a dating app:** high — the core mechanism (forecast-based soft score penalization/boosting relative to a capacity band, gated by a relevance floor) maps almost directly onto reply-capacity-aware exposure allocation for over/under-subscribed dating profiles; main adaptation needed is unilateral applications → mutual/reciprocal matches.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with extensive direct quotes, equations, and citation list matching the well-known real KDD 2017 paper; source_id validated in all three queries).

---

## Project Relevance

LiJAR is the strongest direct methodological match found so far for the project's "capacity-aware exposure allocation" layer. Its core structure — forecast a user's incoming volume with a confidence interval, then apply a soft score adjustment (exponential-decay penalization above a capacity ceiling, relevance-floor-gated multiplicative boosting below a capacity floor) on top of an existing relevance ranker — maps cleanly onto the dating-market problem: job posting ↔ candidate profile, job seeker ↔ swiper, employer review capacity ↔ reply capacity, application ↔ like/swipe-right, application entropy ↔ match/like-spread metric. The paper's own limitations section explicitly flags what would need adaptation for a reciprocal (double opt-in) setting: LiJAR forecasts *unilateral* applications, not mutual outcomes, and treats jobs as having a fixed 30-day expiration window rather than an ongoing active-session state — both differences the dating-market adaptation would need to resolve (e.g., forecasting incoming likes over a rolling active-session window, and layering a match-probability model on top rather than optimizing raw like-volume). LiJAR's "soft constraint" design principle (never fully suppress an over-subscribed profile if it's the only good option for a given viewer) and its documented failure mode (boosting without a relevance floor tanked total engagement) are both directly actionable cautions for the project's own exposure-fairness re-ranking design.
