# Pseudo-Incrementality Testing: Measuring Advertising Lift from Naturally Occurring Interventions

**Source:** https://arxiv.org/pdf/2609.18257.pdf | **NLM source id:** c6d16a82-6dff-4801-aedc-e93009b24441 | **Year / venue:** 2026, arXiv 2609.18257 | **Authors / affiliation:** Georgios Filippou, Boi Mai Quach (Trinity College Dublin, School of Computer Science and Statistics), Ashish Kumar Jha (Trinity College Dublin, Trinity Business School), Dublin, Ireland | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Randomized experiments are the gold standard for measuring advertising lift but are frequently unavailable or underpowered. The paper proposes "pseudo-incrementality testing": treating naturally occurring operational budget shifts (channel launches, cuts, pauses, restarts) as quasi-experiments. Stage 1 applies exact Bayesian online change-point (run-length) detection to marketing activity series to discover and date undocumented structural breaks. Stage 2 estimates a counterfactual via a variance-constrained Unobserved Components structural time-series model, where level/slope disturbance variances are pinned to tiny fractions of pre-window variance so identification runs through co-observed demand regressors rather than a drifting random-walk intercept.
**Unit of credit:** per marketing channel / naturally-occurring intervention event (macro, not per-user or per-touch). **Outcome:** cumulative incremental lift (τ) and return-per-spend (ρ) on an aggregate business outcome series (e.g., total sales revenue). **Bias handling:** a conditional-exogeneity assumption (intervention timing carries no unobserved information about potential outcomes given co-observed covariates); requires at least one demand covariate untouched by the intervention; five qualification screens (C1 adequacy, C2 materiality, C3 isolation, C4 directional significance, C5 economic plausibility) filter out spurious/endogenous/demand-following candidates; a design rule prefers launches/restarts over pauses to avoid "donor contamination" bias from active pre-window periods.

## 2. Evidence
- Validated on Meta's public GeoLift benchmark (two 40-city US daily sales panels, 105 days, 15-day test window): dated the intervention to the exact correct day on both. Inverse (ad-removal) experiment: proposed Constrained UCM lift = -3,159,030 vs. published -3,366,433 (+6.2% error), 90% interval covers benchmark; implied return 1.50 vs. true 1.60. Positive (ad-addition) experiment: Constrained UCM = +5,737,904 vs. published +7,159,530 (-19.9% error, conservative), 90% interval [2.76M, 8.47M] covers benchmark and is 2.2x narrower than free-level BSTS's uninformative interval [66K, 12.9M].
- Baselines compared: pre-post, static OLS, free-level BSTS (CausalImpact), difference-in-differences, synthetic control — proposed method is the only one requiring no geographic control panel while still covering the true benchmark with a narrow interval.
- Simulated markets (5 three-year weekly series): correctly detected 3/5 designed interventions and rejected uninformative ones; pre-post baseline missed true effects by 231-355% and got the sign wrong on a cut.

## 3. Limitations
- If co-observed control channels/demand covariates carry weak information, all regression-based estimators (including this one) are biased; qualification screens can refuse a test but cannot manufacture signal that doesn't exist.
- Underestimated lift by 19.9% on the positive experiment — the price of the tight variance constraint when untreated markets only partially captured the demand dynamics.
- Pause-type interventions with active pre-windows suffer "donor contamination" bias (overshoot true effect by ~2x); launch/restart designs (zero pre-activity) err by only ~11%.
- Relies on the strong conditional-exogeneity assumption; vulnerable to unobserved demand-anticipating endogeneity.
- External validation relies on Meta's simulated public benchmark due to lack of a public corpus pairing real advertiser series with true randomized lift studies.

## 4. Prior works named
- Adams & MacKay (2007) — Bayesian Online Changepoint Detection (exact run-length filtering recursion)
- Harvey & Todd (1983) — Structural time series / Unobserved Components Models
- Brodersen et al. (2015) — CausalImpact / Bayesian Structural Time Series
- Vaver & Koehler (2011); Meta Marketing Science (2022) — Geo-experiments / GeoLift framework (benchmark source)
- Lewis & Rao (2015) — "The Unfavorable Economics of Measuring the Returns to Advertising" (statistical power bounds for ad experiments)

## 5. Project Relevance
- **Answers:** Q1 (2026 industry-adjacent quasi-experimental lift-measurement method), though it targets advertising spend, not in-app interaction attribution.
- **Attributes retention to individual interactions?** No — operates entirely on aggregate macro time-series (channel-level spend/outcome), not individual user interactions.
- **Transferable components:** Bayesian online change-point detection could date undocumented feature rollouts/algorithm changes in platform logs; the variance-constrained counterfactual identification principle (forcing structural-break effect estimation through co-observed regressors, not a free-floating trend) is a useful de-biasing pattern; the five-screen qualification framework (adequacy, materiality, isolation, directional significance, economic plausibility) is a reusable checklist for validating any observational incrementality estimate.
- **Required changes:** Would need a complete redesign from macro channel-level time series to individual user-level, per-swipe interaction sequences; requires a micro-level multi-touch attribution or counterfactual-path model instead of aggregate time-series forecasting; outcome must shift from cumulative revenue lift to a recurring daily N7-active binary per user.
- **On last-touch:** Not discussed — the paper does not analyze last-touch/last-click attribution; it instead critiques observational/unconstrained time-series methods generally for selection and endogeneity bias.
- **Transfer rating:** background — sound quasi-experimental identification machinery for aggregate campaign-level lift, but not designed for individual-level multi-touch attribution and requires substantial adaptation to be relevant.
