# Paper Analysis: Pareto Optimal Proxy Metrics

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2307.01000.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Pareto Optimal Proxy Metrics
**Authors:** Alessandro Zito (Harvard T.H. Chan School of Public Health), Dylan Greaves, Jacopo Soriano, Lee Richardson (Google Inc.)
**Venue:** arXiv (stat.ME), 2023 (v2 Feb 2025)

**Abstract (from source):** North star metrics and online experimentation play a central role in how technology companies improve their products, but evaluating experiments on the north star directly is often difficult because of 1) low sensitivity and 2) short/long-term divergence. A common solution is to rely on proxy metrics instead. Existing literature on proxy metrics concentrates on estimating long-term impact from short-term data; this paper instead focuses on the trade-off between long-term prediction accuracy and short-term sensitivity, proposing the "Pareto optimal proxy metrics" method, which simultaneously optimizes prediction accuracy and sensitivity via a multi-objective optimization algorithm. Applied to experiments from a large industrial recommendation system, the authors find proxy metrics up to eight times more sensitive than the north star that consistently moved in the same direction, increasing decision velocity and quality.

**Key contributions:**
1. First method (per the authors) that explicitly optimizes metric *sensitivity* as a first-class objective, jointly with directional alignment ("directionality") to the long-term north star, rather than optimizing correlation with the north star alone.
2. Formal definitions of metric sensitivity (binary sensitivity — proportion of historical experiments where a metric is statistically significant; average sensitivity — mean |t-statistic|) and directionality (MSE or correlation between a metric's treatment effect and the north star's treatment effect across historical experiments).
3. Casts proxy-metric construction as multi-objective (Pareto) optimization over a linear combination of "auxiliary" short-term metrics, with three algorithms to extract the Pareto front (randomized search; constrained optimization via binning with `nlopt` DIRECT-L; Kriging/Gaussian-process via the `GPareto` R package), compared via a hypervolume-based "Area Under the Pareto Front" (AUPF) metric.
4. A scalar "proxy score" (Detections − Mistakes, normalized) for selecting one proxy off the Pareto front for production use.

**Methodology.** Applied to over 300 experiments from a large industrial recommendation system where daily active users (DAU) is the north star. Each experiment ran T=30 days; the long-term north star value was the average DAU over the last 7 days. Auxiliary metrics are short-term user-behavior signals (e.g., whether a user had a "satisfactory watch" from the homepage). Binary sensitivity and correlation are computed per metric across the 300-experiment corpus; a proxy Z = Σ ω_m·X_m is a normalized, non-negative-weighted linear combination of auxiliary metrics, and ω is chosen to jointly maximize binary sensitivity and correlation via Pareto optimization, extracted by the three candidate algorithms.

**Main results.** Constrained optimization gave the best accuracy/speed trade-off, especially as the number of auxiliary metrics grew. On a held-out set of over 500 subsequent production experiments (six months later), the selected Pareto-optimal proxy was 8.5 times more sensitive than the short-term north star itself (Table 1; the abstract rounds this to "eight times"), was statistically significant 72% of the time when the long-term north star was significant (vs. 40% for the short-term north star alone; recall 0.72 vs. 0.41), at precision 1.0 for both in this dataset, and had a 50% higher proxy score than the short-term north star.

## 2. Experiment Critique

**Design.** Pareto-front extraction and algorithm comparison on a 300-experiment training corpus (varying the number of auxiliary metrics M ∈ {5, 10, 15}); separately, forward validation of the selected proxy on a disjoint set of over 500 experiments run over the following six months.

**Statistical validity.** Sensitivity and directionality are both computed via t-statistics over ~100 independent "cookie bucket" splits per experiment (jackknife standard errors, per Chamandy et al., 2012), a standard industry variance-reduction approach. The framework explicitly assumes treatment effects across the corpus of experiments are i.i.d. draws from a common distribution — asserted as "reasonably met in practice" for minor algorithm tweaks tested over comparable population sizes, but not formally tested for the specific 300/500-experiment corpora used.

**Online experiments.** Yes — the selected proxy was validated against 500 real, subsequently run production experiments over six months, a genuine forward (though non-randomized) holdout comparison.

**Reproducibility.** Both algorithms (Algorithm 1: randomized search; Algorithm 2: constrained optimization via binning) and all objective-function equations are given explicitly, with named software (`nlopt` DIRECT-L, `GPareto`). The underlying 300+500 industrial recommendation-system experiments, the recommendation product itself, and the specific auxiliary metrics used are proprietary and not released.

**Overall.** Methodologically clear and the trade-off framing (Figure 2's empirical demonstration that sensitivity and directionality are inversely related across 70 real auxiliary metrics) is a genuinely useful empirical finding independent of the optimization method itself. The paper explicitly disclaims causal rigor (see Reference Card field 6) and the authors flag several unresolved areas themselves (see field 13).

## 3. Industry Contribution

**Deployability.** High — the resulting proxy is a fixed linear combination of already-logged auxiliary metrics, computed the same way any other metric would be; weights are refit periodically (the authors report every 5-6 months in their company) as an offline batch job, with no new online serving infrastructure required.

**Problems solved.** Directly attacks north-star insensitivity and short/long-term divergence — the two production issues motivating this whole survey direction — letting teams make faster, statistically confident launch decisions without waiting for a slow, noisy north star to reach significance.

**Engineering cost.** An experimentation-platform cost (periodic offline Pareto-front refit plus holdback validation), not a ranking-model or serving-latency cost; this method operates entirely upstream of any ranking model, at the launch-decision layer.

## 4. Novelty vs. Prior Work

**Claimed novelty.** First method that explicitly optimizes sensitivity (not just north-star correlation) when constructing a proxy metric, cast as multi-objective/Pareto optimization; explicitly agnostic to the underlying sensitivity/directionality measures chosen, so the framework generalizes across applications and metric types.

**Prior work named in the source (5-7 most relevant):**
- Athey, Chetty, Imbens, Kang, "The surrogate index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely," NBER 2019 — cited as the contrasting causal-estimation framework this paper deliberately does not adopt (see field 6).
- Deng and Shi, "Data-driven metric development for online controlled experiments: Seven lessons learned," KDD 2016 — source of the metric-sensitivity framing.
- Duan, Ba, Zhang, "Online experimentation with surrogate metrics: Guidelines and a case study," WSDM 2021.
- Drutsa, Gusev, Serdyukov, "Using the delay in a treatment effect to improve sensitivity and preserve directionality of engagement metrics in A/B experiments," WWW 2017.
- Dmitriev and Wu, "Measuring metrics," CIKM 2016 — independently developed a similar score ("Label Agreement") to this paper's proxy score.
- Hohnhold, O'Brien, Tang, "Focusing on the long-term: It's good for users and business," KDD 2015.
- Chamandy, Muralidharan, Najmi, Naidu, "Estimating uncertainty for massive data streams," Google technical report 2012 — source of the jackknife variance estimator underlying binary sensitivity.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| >300 experiments (Pareto-front construction) + >500 held-out experiments (six-month forward validation) | Industrial, large recommendation system (Google) | No | North star = daily active users (DAU); auxiliary metrics and the specific recommendation product are not named |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Pareto Optimal Proxy Metrics; Alessandro Zito (Harvard Biostatistics), Dylan Greaves, Jacopo Soriano, Lee Richardson (Google Inc.); arXiv (stat.ME), 2023 (v2 Feb 2025); https://arxiv.org/abs/2307.01000 |
| 2 | Source type | Industry paper (Google, with a Harvard Biostatistics co-author) |
| 3 | Direction | D3 |
| 4 | Problem setting | Constructing a single proxy metric — as a linear combination of existing short-term "auxiliary" metrics — for online-experiment launch decisions, when the true north-star metric is either statistically insensitive or diverges from its own long-term value, while explicitly managing the trade-off between the proxy's short-term sensitivity and its correlation ("directionality") with the long-term north star. |
| 5 | Objective and label definition | Two experiment-level treatment-effect labels per historical A/B test: the short-term "auxiliary metric" treatment effect (percentage difference, treatment vs. control, per cookie-bucket) and the long-term north-star treatment effect, defined as the average north-star value over the last T=7 days of a T=30-day experiment. No individual-level delayed-label or censoring model — the "long-term" value is a later, still fully observed, still-short (30-day) average within the same completed experiment; delay is handled only by choosing when in the experiment window to measure, not by any missing-data correction. |
| 6 | Prediction or incrementality | **Deliberately neither, by the authors' own statement.** The paper explicitly disclaims causal effect estimation: "we are not designing the proxy to estimate the long-term treatment effect, but rather to anticipate whether such effect exists and how to adapt as a consequence. While we do not claim explicit causality, nor causality is the main focus of our paper." The proxy is a decision signal for statistical significance and direction, not a point estimate of the causal effect's magnitude — contrast with Paper 1 (Netflix, this batch) and Paper 3 (Proximal Surrogate Index, this batch), which both estimate the effect itself. |
| 7 | Model architecture | Not a neural network. A proxy metric Z = Σ ω_m·X_m, a linear combination of M auxiliary short-term metrics; weights ω are found by multi-objective (Pareto) optimization jointly maximizing binary sensitivity and correlation with the long-term north star, solved via one of three algorithms (randomized search; constrained optimization via binning + `nlopt` DIRECT-L; Kriging/Gaussian-process via `GPareto`). A scalar "proxy score" (Appendix A) selects one weight vector off the resulting Pareto front for production use. |
| 8 | Credit assignment | **Not applicable at the item level — this paper operates entirely at the experiment level**, exactly like Paper 1 in this batch. Both the auxiliary metrics and the north star are experiment-arm-level treatment effects (cookie-bucket averages), never traced to an individual impression, item, or user-level decision. |
| 9 | Training data and counterfactual handling | Randomized A/B tests provide the counterfactual directly for both the auxiliary metrics and the north star; no observational counterfactual correction is used. Historical experiments are assumed i.i.d. draws from a common treatment-effect distribution, which is what lets a proxy fit on one corpus (300 experiments) be evaluated on a disjoint, later corpus (500 experiments). |
| 10 | Offline and online evaluation | Offline: Pareto-front extraction and algorithm comparison (AUPF/hypervolume, runtime) on the 300-experiment training corpus. Online/forward: the selected proxy was applied to 500 real, subsequently run production experiments over the following six months and compared against the short-term north star's own sensitivity and proxy score — a genuine forward holdout, though not a randomized comparison of the proxy method against an alternative method. |
| 11 | Reported gains | On the 500-experiment held-out set (Table 1), the Pareto-optimal proxy was 8.5 times more sensitive than the short-term north star itself (abstract rounds to "eight times"); when the long-term north star was statistically significant, the proxy was also significant 72% of the time vs. 40% for the short-term north star (recall 0.72 vs. 0.41, both at precision 1.0 in this dataset); the proxy's overall proxy score was 50% higher than the short-term north star's. The Discussion section separately states proxies were "6-10 times more sensitive" across the authors' broader multi-year experience deploying the method with multiple teams (not itself a quantified experiment in this paper). |
| 12 | Applicability to a two-sided dating recommender | Directly transferable as an evaluation-layer tool: given a corpus of past dating-app experiments, this Pareto method could combine early like/match/conversation signals into a single, highly sensitive short-term proxy for retention/revenue launch decisions without first building a full causal surrogate-index model. Says nothing about reciprocity, congestion, or fairness across the two sides of the market. |
| 13 | Unverified claims | The company-wide "6-10 times more sensitive" and "several launches that directly improved long-term user experience" claims (Section 5.2) are stated as qualitative multi-team, multi-year experience, not backed by this paper's own quantified experiments. The i.i.d.-treatment-effects-across-experiments assumption underlying the entire framework is asserted as "reasonably met in practice" without a formal test on the specific 300/500-experiment corpora used. |

## Project Relevance

Speaks directly to **Q3** (label/horizon: a concrete, production-tested method for building a highly sensitive short-term composite label to substitute for a slow retention/revenue north star) and **Q6** (offline/online evaluation methodology under noisy, low-base-rate outcomes — the sensitivity/directionality/Pareto-front machinery is a ready-made template for the survey's "surrogate validation" evaluation-plan deliverable). Also relevant to **Q1**, in the negative: the paper's stated purpose is to make a short-term proxy trustworthy enough that teams *don't* have to wait for the long-term objective — the opposite of this project's target design of training directly on the long-term objective — useful as a documented industry fallback path if the unified long-term model proves too slow to iterate against. **Not relevant to Q2, Q4, Q5, or Q7** — like Paper 1 in this batch, this is purely an experiment-level metric-selection tool, not a ranking model, and has nothing to say about item-level credit assignment, fusing short/long-term model heads, uplift placement inside a ranker, or two-sided-market mechanics. Important caveat for the survey: this method explicitly optimizes for detecting a significant, correctly signed *direction*, not for accurately estimating the *magnitude* of the long-term causal effect — a materially weaker guarantee than Paper 1 and Paper 3 in this batch provide.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `ParetoProxy`._

## Meta Information

- **Authors:** Alessandro Zito, Dylan Greaves, Jacopo Soriano, Lee Richardson
- **Affiliations:** Harvard T.H. Chan School of Public Health (Zito); Google Inc. (Greaves, Soriano, Richardson)
- **Venue:** arXiv (stat.ME)
- **Year:** 2023 (v2 Feb 2025)
- **Relevance:** Core
- **Priority:** 1
- **nlm:0c4393ea**
