# Paper Analysis: Understanding Guest Preferences and Optimizing Two-sided Marketplaces

**Source:** https://arxiv.org/abs/2607.00280  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example  
**Authors:** Yufei Wu; Daniel Schmierer  
**Abstract:** Airbnb combines economic demand modeling, instrumental variables, and experiments to estimate guest price sensitivity and heterogeneous preferences when hosts set prices and randomized pricing tests are difficult.  
**Methodology:** A product-level logit choice model is estimated with the Berry-Levinsohn-Pakes transformation. Supply growth conditional on realized demand instruments for endogenous price; historical experiments validate and calibrate the observational estimates. A panel-IV model recovers segment heterogeneity.  
**Main results:** Observational elasticities were slightly larger in magnitude than experimental estimates, so Airbnb applies an experiment-derived haircut. A later experiment reportedly closely matched the updated estimates; exact numerical effects are not specified.

## 2. Experiment Critique

**Design:** Marketplace panel data provide price and supply variation; carefully designed pricing experiments serve as ground truth for qualitative validation and bias calibration.  
**Statistical validity:** The paper explicitly discusses interference and low power. Identification depends on an unprovable exclusion restriction: supply-growth instruments must affect booking choice only through price.  
**Online experiments:** Historical and subsequent pricing experiments are described, but assignment details, sample sizes, and effect estimates are not specified.  
**Reproducibility:** Equations and identification logic are provided; proprietary data and experimental implementation are unavailable.  
**Overall:** A candid and practically useful causal-measurement case study, with residual IV validity risk and sparse quantitative reporting.

## 3. Industry Contribution

**Deployability:** Supports continuously refreshed price-elasticity and segment-preference estimates when recurring experiments are impractical.  
**Problems solved:** Endogenous prices, marketplace interference, infrequent bookings, heterogeneous products, and zero-share segments.  
**Engineering cost:** Requires geography-time panels, defensible supply instruments, experiment calibration, and ongoing monitoring.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Bridges experimental calibration and observational IV demand estimation for ongoing marketplace optimization, including a simple route to segment-level elasticity.  
**Prior work comparison:** Builds on BLP choice estimation, marketplace interference experiments, and demand models with zero shares.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Airbnb marketplace panel | Not specified in source. | No | Proprietary listings, prices, supply, views, and bookings. |
| Airbnb pricing experiments | Not specified in source. | No | Used for validation and calibration. |

**Offline experiment reproducibility:** Low without proprietary marketplace data and instrument construction.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D8  
**Problem setting:** Host-priced two-sided lodging marketplace with endogenous price, marketplace interference, and heterogeneous guest preferences.  
**Objective and label definition:** Estimate causal price elasticity of booking demand and segment-specific affordability preferences; outcome is product share/bookings.  
**Prediction or incrementality:** Causal elasticity estimation, calibrated against randomized experiments; not per-item ranking uplift.  
**Model architecture:** Aggregate logit demand model, BLP linearization, supply-based instrumental variables, and segment panel regression.  
**Credit assignment:** Booking response is attributed to supply-induced price variation under the IV exclusion restriction.  
**Training data and counterfactual handling:** Observational geography-time panels plus experimental calibration; IVs address price endogeneity, while interference is acknowledged in experiments.  
**Offline and online evaluation:** Observational estimates compared with historical and later experiments; no ranking A/B metrics reported.  
**Reported gains:** Qualitative agreement and close matching with a subsequent experiment; exact gains not specified in source.  
**Unverified claims:** Instrument validity, calibration stability, and downstream marketplace/product impact lack complete quantitative evidence.

## Project Relevance

**Source-stated facts:** Airbnb uses experiment-calibrated causal demand estimates to personalize guest experience and optimize host tools in a two-sided marketplace.

**Survey inference:** Dating can similarly use randomized tests to calibrate observational estimates of heterogeneous response when direct experimentation is weak or interfered with. Supply-side instruments are domain-specific, and bookings do not capture reciprocal match quality, long-run retention, or successful-match churn.

**Applicability note:** Strong template for calibrating observational marketplace preference models with experiments.  
Requires dating-specific instruments, bilateral outcomes, and LTV labels.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Yufei Wu; Daniel Schmierer  
**Affiliations:** Airbnb  
**Venue:** arXiv  
**Year:** 2026  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 2
