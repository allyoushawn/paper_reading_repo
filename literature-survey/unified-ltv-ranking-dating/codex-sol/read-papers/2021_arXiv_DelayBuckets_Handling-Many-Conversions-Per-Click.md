# Paper Analysis: Handling Many Conversions per Click in Modeling Delayed Feedback

**Source:** https://arxiv.org/abs/2101.02284  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Handling Many Conversions per Click in Modeling Delayed Feedback  
**Authors:** Ashwinkumar Badanidiyuru; Andrew Evdokimov; Vinodh Krishnan; Pan Li; Wynn Vonnegut; Jayden Wang  
**Abstract:** Google predicts counts or values of multiple post-click conversions under heterogeneous, nonparametric delays up to 90 days. Mature delay-bucket labels, thermometer encoding, and auxiliary features enable near-real-time training with neutral long-term bias.  
**Methodology:** Split total conversion label across delay buckets; train each bucket only once mature; share outputs through thermometer encoding; use intermediate campaign signals for drift/new advertisers.  
**Main results:** Proposed model improves Poisson log loss 8.6% overall, 10.16% for long-delay advertisers, and 1.81% for new advertisers versus the M3 baseline, close to oracle values of 9.1%, 10.87%, and 2.0%.

## 2. Experiment Critique

**Design:** Production-ad datasets, delay/new-advertiser slices, several ablations, bias/outlier analyses.  
**Statistical validity:** Large empirical comparisons; uncertainty and online business lift Not specified.  
**Online experiments:** Not specified in source.  
**Reproducibility:** Proprietary data.  
**Overall:** Strong mature-label construction for online learning, but post-click value is not user retention or causal exposure effect.

## 3. Industry Contribution

**Deployability:** Designed for online one-pass training and arbitrary advertiser windows.  
**Problems solved:** Multiple delayed events, 2-hour–90-day windows, distribution drift, new campaigns.  
**Engineering cost:** Bucketed label pipelines, maturity gating, multiple outputs, auxiliary delay features.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Unbiased, nonparametric many-conversion delayed-feedback model for online training.  
**Prior work comparison:** Exponential DFM and negative-binomial multiple-conversion models.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Google Ads conversions | Not specified in source. | No | OPC/MPC campaigns, up to 90-day windows. |

**Offline experiment reproducibility:** Not specified.

## 6. Community Reaction

Not specified.

## Survey Card Fields

**Source type:** Industry-lab arXiv  
**Direction:** D7  
**Problem setting:** Online expected conversion-count/value prediction with repeated delayed events.  
**Objective and label definition:** Total count or value of events within advertiser-defined 2-hour–90-day post-click window; labels split by maturity bucket.  
**Prediction or incrementality:** Prediction, not uplift.  
**Model architecture:** Poisson outputs over delay buckets with thermometer encoding and auxiliary features.  
**Credit assignment:** All events in the window are attributed to one click; no cross-exposure causal attribution.  
**Training data and counterfactual handling:** Observational click/conversion logs; maturity gating removes future-label bias but not treatment confounding.  
**Offline and online evaluation:** Offline production slices; no A/B lift specified.  
**Reported gains:** 8.6% overall Poisson-log-loss improvement.  
**Unverified claims:** Retention/revenue ranker effects Not specified.

## Project Relevance

**Source-stated facts:** Handles repeated monetary events and very long, heterogeneous maturity windows in online training.

**Survey inference:** Directly useful for subscription plus a-la-carte dating revenue over weeks, including multiple purchases per exposure/user. But attributing all events to one click is too simple for repeated profile exposures and reciprocal matches; uplift, congestion, interference, and positive churn require separate treatment.

**Applicability note:** Excellent delayed multi-event revenue label design.  
Needs marketplace-aware exposure attribution before becoming a dating ranking objective.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Ashwinkumar Badanidiyuru et al.  
**Affiliations:** Google Research; Google  
**Venue:** arXiv  
**Year:** 2021  
**PDF:** Available  
**Relevance:** Related  
**Priority:** 2
