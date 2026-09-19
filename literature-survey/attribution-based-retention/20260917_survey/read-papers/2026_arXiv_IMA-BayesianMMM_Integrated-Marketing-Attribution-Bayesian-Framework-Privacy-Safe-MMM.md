# Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM

**Source:** https://arxiv.org/pdf/2606.16878.pdf | **NLM source id:** 5a8a299e-afe2-4909-ac42-4bfc9e71851f | **Year / venue:** 2026, arXiv:2606.16878 | **Authors / affiliation:** Meghana R. Bhat, Ankit Umare, Utsav Aggarwal, Richard Vecsler, Arunkumar Mani, Karthik Nair, Chandhu Nair — Lowe's Companies, Inc. | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Multi-Touch Attribution (MTA) gives granular, per-touchpoint credit but has become unreliable post-cookie-deprecation; Marketing Mix Modeling (MMM) is privacy-safe and robust but too coarse for campaign-level decisions (high dimensionality, campaign multicollinearity, few weekly observations); randomized incrementality experiments don't scale to thousands of campaigns. The paper proposes Integrated Marketing Attribution (IMA), a 3-stage pipeline: (1) weekly MMM estimation of channel-level incremental sales and adstock parameters; (2) temporal disaggregation of weekly channel contributions to daily resolution using daily-scaled adstock; (3) channel-specific Bayesian linear regression over daily campaign media series, where MMM-derived channel coefficients serve as informative (truncated-normal) priors that shrink/regularize campaign-level estimates. **Unit of credit:** per daily campaign media series within a channel (aggregated data, no user-level tracking). **Outcome:** daily channel-level incremental sales, disaggregated to campaign level. **Bias handling:** non-negativity constraints plus MMM-anchored priors regularize against severe campaign-level multicollinearity (overlapping flighting schedules); there is no individual-user selection bias to handle since the model never observes individual users.

## 2. Evidence
Three years of daily data across Search/Social/Display at Lowe's. Aggregated daily IMA predictions reconstruct weekly MMM totals at R²=0.98. Weekly MAPE: Search 4.1%, Social 5.97%, Display 3.25% (vs. ~2% for pure MMM, expected given the incremental-contribution target's lower signal-to-noise ratio). Posterior campaign coefficients, though anchored to a shared channel prior, disperse meaningfully to distinguish low/moderate/high-impact campaigns.

## 3. Limitations
Modestly higher error than the primary MMM benchmark. Severe campaign-level multicollinearity would break an unregularized regression (motivating the Bayesian shrinkage in the first place). No cross-channel interaction/spillover modeling — channels are fit independently. Priors are static, not dynamically/sequentially updated. No geo-level or subgroup heterogeneity modeling (named as future work).

## 4. Prior works named
- Jin et al. (2017) — Bayesian MMM with carryover/shape effects (Google)
- Chan & Perry (2017) — challenges and opportunities in MMM (Google)
- Google (2022) — Unified Marketing Measurement (blending MMM/MTA/experiments)
- Gordon et al. (2019) — comparison of ad measurement approaches, Facebook field experiments
- Salvatier et al. (2016) / Kucukelbir et al. (2017) — PyMC3 / ADVI variational inference

## 5. Project Relevance
- **Answers:** Q1
- **Attributes retention to individual interactions?** No — operates entirely on aggregate daily campaign/channel media series; there is no user-level tracking or in-app interaction data at all.
- **Transferable components:** The macro-to-micro Bayesian prior-anchoring pattern itself (use a reliable aggregate causal/experimental estimate as an informative prior to regularize a noisy, high-dimensional granular estimate) is a reusable idea for shrinking per-swipe credit estimates toward a more reliable aggregate N7 lift number. Adstock/carryover modeling is also conceptually relevant to delayed match/message effects.
- **Required changes:** Everything about the unit of analysis: aggregate daily campaign series would need to become individual user interaction sequences; the sales-revenue target would need to become a recurring daily N7 retention label; homogeneous media spend/impressions would need to become heterogeneous swipe/match/message event types.
- **On last-touch:** Does not address last-touch directly, but broadly critiques user-level MTA as increasingly unreliable and operationally fragile under privacy restrictions and incomplete customer journeys — motivating its own aggregate-data-only design.
- **Transfer rating:** background — a macro, aggregate-data attribution framework; useful only as a design pattern (prior-anchored shrinkage), not as a directly portable algorithm.
