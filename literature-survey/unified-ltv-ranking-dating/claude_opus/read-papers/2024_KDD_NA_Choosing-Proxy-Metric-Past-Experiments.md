# Paper Analysis: Choosing a Proxy Metric from Past Experiments

**Source:** https://arxiv.org/abs/2309.07893 (Tripuraneni et al., KDD 2024)
**Date analyzed:** 2026-08-16

## 1. Summary

**Title:** Choosing a Proxy Metric from Past Experiments
**Authors:** Nilesh Tripuraneni, Lee Richardson, Alexander D'Amour, Jacopo Soriano, Steve Yadlowsky (Google DeepMind / Google)
**Venue:** KDD 2024 (30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining)

**Abstract (paraphrased from source):** In many randomized experiments, the treatment effect on the true long-term "north star" metric is difficult or infeasible to measure directly because it is slow to react and noisy. Experimenters commonly substitute short-term proxy metrics, but existing methods for choosing or combining them rely on strong, largely untestable causal assumptions and do not formally balance a proxy's sensitivity against its directional alignment with the long-term outcome. The paper introduces a statistical framework that defines "proxy quality," reduces the construction of an optimal composite proxy to a portfolio-optimization problem, and denoises historical experiment data via a hierarchical model to estimate the latent parameters that problem requires.

**Key contributions:**
1. A new notion of proxy quality — the correlation between an observed short-term composite proxy's treatment effect and the true, latent population treatment effect on the long-term outcome — that packages sensitivity and directional alignment into one objective.
2. A proof that optimizing this objective over a weighted combination of base proxies is equivalent to Sharpe-ratio maximization, a classic portfolio-optimization problem solvable as a convex quadratic program.
3. A hierarchical (Bayesian linear mixed) model that denoises historical, correlated within-experiment noise to recover the latent treatment-effect covariances the optimization needs.
4. A demonstration that the optimal proxy is not fixed in advance — it adapts to the sample size (noise level) of the specific new experiment it will be used for.

**Methodology.** The framework assumes a corpus of K historical randomized experiments, each with an estimated treatment effect on the long-term north-star metric (Δ̂^N) and on a vector of d base proxy metrics (Δ̂^P), plus an estimated within-experiment noise covariance Ξ̂. The true population treatment effects (Δ^N, Δ^P) for each experiment are assumed drawn i.i.d. from a common distribution D. The composite-proxy quality objective — maximize corr(Δ^N, w^⊤Δ̂^P) over a normalized weight vector w — is shown to reduce to the Sharpe-ratio-maximization form and is then re-cast as an equivalent convex quadratic program (solvable via CVXPY). To obtain the unobservable latent covariances Cov(Δ^N, Δ^P) and Cov(Δ^P, Δ^P) the objective needs, the paper fits a hierarchical Bayesian model — (Δ^N_i, Δ^P_i) ~ MVN(μ, Λ), with the observed noisy estimates (Δ̂^N_i, Δ̂^P_i) drawn around them with covariance Ξ_i — via NumPyro's No-U-Turn Sampler, using weakly informative priors (Normal on the means, Half-Cauchy on scales, LKJ on the correlation matrix). Because within-experiment noise Ξ_i scales as Ξ_ref/n_i, the paper estimates a single reference covariance Ξ_ref from the historical corpus via a precision-weighted average, which lets the optimal proxy weights for a brand-new experiment be computed a priori from only its planned sample size, before the experiment is run.

**Main results.** On a historical corpus of 307 real A/B tests from an industrial recommendation engine (sample sizes ranging from roughly 10⁶ to 10⁸ users), using stratified 4-fold cross-validation, the new composite proxy achieved the highest proxy score (0.666) and proxy quality (0.302) among all compared methods, outperforming a prior baseline composite-proxy method (Richardson et al., "Pareto optimal proxy metrics," 2023) and three individually hand-selected auxiliary metrics, while not sacrificing sensitivity unduly relative to the most sensitive raw metric.

## 2. Experiment Critique

**Design.** Stratified 4-fold cross-validation over the 307-test historical corpus, with the hierarchical model and optimal weights refit on each training fold and evaluated on the corresponding held-out fold, using three criteria: metric sensitivity, proxy score (directional-alignment detections minus mistakes against the long-term metric), and the paper's own proxy-quality correlation objective.

**Statistical validity.** Because the true population long-term treatment effect is never directly observable (there is no ground truth for Δ^N), all evaluation is necessarily against a noisy estimate of the long-term outcome rather than its latent value — a limitation the authors state explicitly. Posterior inference for the hierarchical model is diagnosed via the r-hat statistic, reported as a perfect 1.0 across all parameters and chains (10,000 burn-in plus 50,000 samples across 4 chains), which is a genuine strength for a Bayesian pipeline meant to run repeatedly in production.

**Online experiments.** The paper does not perform a new live online evaluation. All evaluation is retrospective, over historical A/B test logs that had already completed; the method is a post-hoc, offline analysis of past experiments used to inform which metric to trust on a new experiment before that experiment runs, not something validated by running a fresh live experiment of its own.

**Reproducibility.** The full statistical model, priors, and the convex reformulation of the optimization are given as explicit equations, and the inference implementation (NumPyro/NUTS, CVXPY) is named. The 307-test historical corpus, its three "Auxiliary Metric" proxies, and the underlying industrial recommendation engine are not named or released, so the specific empirical results cannot be reproduced outside that company.

**Overall.** The methodology is statistically rigorous and its central assumption — that population treatment effects across a corpus of experiments are i.i.d. draws from a common distribution — is explicitly named and defended (rather than left implicit), which is a strong practice. The corpus itself and its outcome variables remain a black box to an outside reader, so the reported proxy-score and proxy-quality numbers must be taken on the authors' word rather than independently checked.

## 3. Industry Contribution

**Deployability.** Because the reference noise covariance Ξ_ref is estimated once from the historical corpus, the optimal proxy weights for a brand-new experiment can be computed before that experiment is even run, using only its planned sample size — this makes the method operationally cheap to deploy as a metric-recommendation service inside an experimentation platform, not a model that needs retraining per launch.

**Problems solved.** Replaces ad hoc, hand-selected short-term guardrail metrics with a principled, statistically justified combination rule for deciding which metric (or weighted blend of metrics) to trust as the primary decision signal for a new experiment when the true long-term outcome cannot be measured in time.

**Engineering cost.** This is an experimentation-infrastructure cost, not a ranking-latency cost: it requires maintaining a historical corpus of paired (proxy, north-star) treatment-effect estimates across past experiments, a periodic Bayesian re-fit of the hierarchical model (MCMC with tens of thousands of samples per refit), and integration into the experiment-analysis and launch-decision pipeline rather than the online serving/ranking pipeline.

## 4. Novelty vs. Prior Work

**Claimed novelty.** A new proxy-quality definition that unifies sensitivity and directional alignment into a single correlation-based objective; a reduction of composite-proxy construction to a Sharpe-ratio/portfolio-optimization problem; a hierarchical model that denoises correlated within-experiment noise between the proxy and the long-term metric; and the finding that the optimal proxy weighting should depend on the new experiment's sample size rather than being fixed in advance.

**Prior work named in the source (Query 2, part 3):**
- Richardson et al., "Pareto optimal proxy metrics," 2023 — the paper's direct comparison baseline, and the source of the proxy-score and sensitivity evaluation criteria this paper reuses.
- Athey et al., "The surrogate index: Combining short-term proxies to estimate long-term treatment effects more rapidly and precisely," 2019 — cited as a key prior approach to combining short-term markers for long-term effect estimation.
- Elliott et al., "Surrogacy marker paradox measures in meta-analytic settings," 2015 — cited for the surrogate-paradox framing and the meta-analytic random-effects approach this paper's i.i.d.-population assumption follows.
- Wang et al., "Surrogate for long-term user experience in recommender systems," 2022 — cited for evaluating content-consumption diversity as a surrogate for long-term platform visitation, in a recommender-systems setting close to this survey's domain.
- Deng and Shi, "Data-driven metric development for online controlled experiments: Seven lessons learned," 2016, and related work on metric sensitivity decomposition — cited for distributional priors on treatment effects and metric-sensitivity framing.
- Prentice, "Surrogate endpoints in clinical trials: definition and operational criteria," 1989 — the landmark clinical-trial definition of a valid surrogate endpoint.
- Hohnhold, O'Brien, and Tang, "Focus on the long-term: It's better for users and business," 2015 — cited for establishing the industry importance of optimizing for long-term outcomes over short-term metrics.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Historical A/B test corpus (307 tests) | Industrial recommendation-engine experiment logs; sample sizes ~10⁶–10⁸ users | Not public | Source of all reported results; the recommendation engine and the 3 "Auxiliary Metric" proxies are not named. |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Choosing a Proxy Metric from Past Experiments; Nilesh Tripuraneni, Lee Richardson, Alexander D'Amour, Jacopo Soriano, Steve Yadlowsky (Google DeepMind / Google); KDD 2024; https://arxiv.org/abs/2309.07893 |
| 2 | Source type | Industry paper |
| 3 | Direction | D3 |
| 4 | Problem setting | Choosing or combining short-term proxy metrics to serve as the primary outcome of a future A/B test, when the true long-term north-star metric is too slow, noisy, or costly to measure directly within the experiment's window. |
| 5 | Objective and label definition | Maximize "proxy quality" = corr(Δ^N, w^⊤Δ^P), the correlation between a composite short-term proxy's treatment effect and the latent population long-term treatment effect. Labels are experiment-level relative average treatment effects (one Δ^N and one Δ^P vector per historical A/B test), not user- or item-level labels. There is no sequential time horizon in the RL sense; "short-term" versus "long-term" refers to how quickly each metric reacts within an already-completed experiment window. Delay itself is not modeled — the long-term metric's value is taken as already computed in the historical logs; measurement *noise* (not delay) is handled via a hierarchical Bayesian model with within-experiment covariance Ξ_i ≈ Ξ_ref/n_i. |
| 6 | Prediction or incrementality | Incrementality. The paper explicitly frames its labels as causal treatment effects from randomized controlled trials. Paper's own wording: "Randomized controlled trials (RCTs) are the gold standard approach for measuring the causal effect of an intervention... we seek to find noisy proxy metrics whose TEs closely track the population TEs on the long-term outcome." |
| 7 | Model architecture | Not a ranking or scoring network. A two-stage statistical procedure: (a) a hierarchical/linear-mixed Bayesian model (fit via NumPyro's NUTS sampler) that denoises historical treatment-effect estimates into latent covariance matrices Λ^NP and Λ^PP; (b) a convex quadratic program, equivalent to Sharpe-ratio maximization and solved via CVXPY, that outputs the optimal composite-proxy weight vector w for a new experiment given its planned sample size. |
| 8 | Credit assignment | **Does not apply in the item-level ranking sense the survey otherwise tracks. This paper operates entirely at the experiment level, not the item level:** it maps one A/B test's short-term proxy treatment effect to that same test's long-term treatment effect. There is no user-level or item-level decision being attributed at all — the mismatch with the survey's item-level credit-assignment question is itself the relevant finding for this reference. It answers "which short-term signal should we trust as a stand-in for the long-term one," not "which decision caused the outcome." |
| 9 | Training data and counterfactual handling | Historical corpus of 307 real A/B tests, each already a randomized experiment, so treatment effects are causally identified by design (no additional counterfactual correction is needed the way logged, observationally biased data would require). Within-experiment covariance Ξ_i is estimated from each test's own sample covariance and modeled as scaling with Ξ_ref/n_i across the corpus, letting a precision-weighted historical average stand in for a new test's noise level before it runs. |
| 10 | Offline and online evaluation | Offline only: stratified 4-fold cross-validation over the 307-test historical corpus, scored on held-out metric sensitivity (\|t-stat\| > 2 detection rate), proxy score (directional-alignment detections minus mistakes against the long-term metric), and proxy quality (the correlation objective itself). No new live/online evaluation is performed. |
| 11 | Reported gains | Held-out cross-validated evaluation on the 307-test industrial-recommender A/B corpus (Table 1): New Composite Proxy — sensitivity 0.181, proxy score 0.666, proxy quality 0.302; Baseline Composite Proxy (Richardson et al., 2023) — sensitivity 0.182, proxy score 0.611, proxy quality 0.279; raw Auxiliary Metric 1 — proxy score 0.611, proxy quality 0.174; raw Auxiliary Metric 2 — sensitivity 0.368, proxy score 0.222; raw Auxiliary Metric 3 — proxy score 0.104, proxy quality 0.030. The new composite proxy achieves the highest proxy score and proxy quality of all methods compared, at a sensitivity essentially tied with the prior baseline. |
| 12 | Applicability to a two-sided dating recommender | Not a ranking method and cannot itself become part of the ranking model, but directly reusable at the experimentation layer: given a corpus of past dating-app A/B tests, this framework could select the best short-term guardrail metric (e.g., day-1 conversation rate) to trust for early launch decisions on retention/revenue experiments. It says nothing about reciprocity, congestion, or item-level ranking. |
| 13 | Unverified claims | The i.i.d.-population-of-experiments assumption is explicitly flagged by the authors as "strong and not suitable for all applications," and is defended only by appeal to "historical intuition and various tests" on the authors' own corpus rather than a described, reproducible formal test. The claim that "highly non-stationary settings... may not be well addressed by our second-stage denoising procedure" is stated as a limitation but not empirically demonstrated with a non-stationary counter-experiment in the paper. |

## Project Relevance

Named Core/Priority 1, but a structurally different contribution from the other three papers in this batch: it is about **choosing a short-term metric that predicts a long-term one, not about ranking**, and Reference Card field 8 states that mismatch plainly rather than forcing an item-level framing. It is **not** relevant to **Q2** (item-level credit assignment), **Q4** (fusing short-term and long-term heads inside a model), **Q5** (where uplift lives inside a ranker — this paper's "incrementality" is at the whole-experiment level, not the exposure-to-item level the survey tracks), or **Q7** (two-sided markets). It is, however, substantively relevant to two questions: **Q3** (label and horizon choice) — this is a rigorous, general-purpose statistical method for choosing which short-horizon label best predicts the dating app's 7–30-day retention and multi-week revenue outcome, directly usable to validate candidate short-term labels before committing to them as training targets; and **Q6** (evaluation plan) — it is a ready-made offline surrogate-validation methodology, precisely the kind of "surrogate validation" component the executive summary's evaluation-plan deliverable must produce. Because it meaningfully addresses two of the eight research questions, this section is not prefixed as low relevance, but its relevance is narrow and specific to the metric-choice and evaluation-design questions rather than to ranking-model architecture.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Nilesh Tripuraneni, Lee Richardson, Alexander D'Amour, Jacopo Soriano, Steve Yadlowsky
- **Affiliations:** Google DeepMind / Google
- **Venue:** KDD 2024
- **Year:** 2024
- **Relevance:** Core
- **Priority:** 1
- **nlm:e33e4636-ba5b-4b65-a4b4-abeb9df03476**
