# Paper Analysis: A Nonparametric Delayed Feedback Model for Conversion Rate Prediction

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2018 (Arxiv) [NoDeF] A Nonparametric Delayed Feedback Model for Conversion Rate Prediction.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** A Nonparametric Delayed Feedback Model for Conversion Rate Prediction
**Authors:** Yuya Yoshikawa (STAIR Lab, Chiba Institute of Technology), Yusaku Imai (CyberAgent, Inc.)
**Venue/Year:** arXiv:1802.00255, 2018

NoDeF extends Chapelle's Delayed Feedback Model (DFM, KDD 2014) by replacing DFM's assumed exponential (or, in later work, Weibull) time-delay distribution with a nonparametric hazard function h(d;x,V) = Σ_l α_l(x;V)·k(t_l,d), a feature-conditioned weighted sum over L fixed "pseudo-points" on the time axis combined through a kernel (a Gaussian kernel is used in experiments), borrowing the spirit of kernel density estimation. NoDeF is a joint model of two probabilistic pieces: a **conversion model** — logistic regression predicting a hidden binary variable c (whether the sample will eventually convert at all) — and a **time delay model** — the nonparametric hazard/survival function above. Parameters (a weight vector w for the conversion classifier, a weight matrix V for the hazard's pseudo-point intensities) are estimated jointly via an EM algorithm: the E-step computes the posterior of the hidden variable c for every currently-negative (not-yet-converted) sample using the survival function; the M-step updates w and V by L-BFGS gradient ascent on the resulting expected complete-data log-likelihood. On a synthetic dataset built from a 3-component mixture of truncated-normal delay distributions, NoDeF recovers the true multi-modal delay density, while an exponential MLE fit (as used by DFM) cannot. On the Criteo conversion-log dataset (the same benchmark used by Chapelle 2014), NoDeF beats both DFM and a naive always-negative-until-converted logistic-regression baseline (NAIVE) on log loss and accuracy across two campaign splits ("all campaigns" and "recent campaigns"), with a slightly lower AUC than DFM on the "all campaigns" split but a higher AUC on the "recent campaigns" split.

## 2. Experiment Critique / 3. Industry Contribution / 4. Novelty vs. Prior Work / 5. Dataset Availability

Condensed per the priority-3 depth rule — see the Reference Card (Section 7) and Project Relevance below for the substantive extraction. Datasets used: a synthetic 3-pattern mixture dataset (for delay-shape recovery only, not publicly distributed as a standalone artifact) and the public Criteo conversion-log dataset (https://labs.criteo.com/2013/12/conversion-logs-dataset/, the same dataset used in Chapelle 2014). Novelty is entirely about the delay-distribution modeling choice: NoDeF is presented as "the first study to represent the distribution of delayed feedback nonparametrically in the CVR prediction model," versus DFM's exponential assumption and a cited but unread mixture-of-Weibull variant (Ji et al. 2017).

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "A Nonparametric Delayed Feedback Model for Conversion Rate Prediction," Yuya Yoshikawa, Yusaku Imai; STAIR Lab, Chiba Institute of Technology / CyberAgent, Inc.; arXiv:1802.00255, 2018; https://arxiv.org/abs/1802.00255 |
| 2 | Source type | Academic (industry co-authored: CyberAgent) |
| 3 | Direction | D7 |
| 4 | Problem setting | CVR prediction under delayed feedback, specifically targeting the assumption-fragility of prior parametric (exponential/Weibull) delay models when the true delay-time distribution has an arbitrary, possibly multi-modal, shape. |
| 5 | Objective and label definition | Binary CVR prediction, with a hidden variable c indicating whether the sample will ever convert, and elapsed time e as the time since click at observation. Delay/censoring is handled via standard survival-analysis machinery: for a not-yet-converted sample, the probability that conversion has not yet happened by elapsed time e is given by the model's survival function s(e;x,V), and the E-step of EM computes the posterior over the hidden "will-convert" variable c using this survival function rather than treating the sample as a definite negative. Horizon: **not specified in source** as an absolute wall-clock window — experiments use normalized log time-delay values (log-transformed and min/max-normalized), and the paper only qualitatively characterizes delayed feedback generally as ranging "from hours to days" (citing Chapelle 2014); no explicit attribution or observation-window length in days is given for the paper's own Criteo experiments. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Joint two-part probabilistic model: (a) a logistic-regression "conversion" classifier p(c=1\|x;w); (b) a nonparametric "time delay" hazard model h(d;x,V) = Σ_l α_l(x;V)·k(t_l,d) built from L Gaussian-kernel pseudo-points on the time axis, with feature-dependent intensity weights α_l(x;V) = (1+exp(−V_l^T x))^−1. Learned jointly by an EM algorithm (E-step: posterior of hidden conversion indicator c for negative samples; M-step: L-BFGS updates of w and V with L2 regularization λ_w, λ_V). |
| 8 | Credit assignment | Not specified in source. The model operates at single click → single conversion-label granularity; no multi-item slate or ranked-list credit assignment is addressed. |
| 9 | Training data and counterfactual handling | A synthetic 3-pattern mixture dataset (for delay-shape recovery) and the public Criteo conversion-log dataset (six periods, each split into train/validation/test by click date, feature dimensionality reduced via PCA to 100). No counterfactual or causal handling — this is a censored-label correction via survival analysis, not treatment-effect estimation. |
| 10 | Offline and online evaluation | Offline only: on synthetic data, visual comparison of the estimated delay density against the known ground-truth mixture density; on Criteo, log loss, accuracy, and AUC across two dataset splits ("all campaigns" and "recent campaigns"), each averaged over six periods with reported standard deviations. No online evaluation is reported. |
| 11 | Reported gains | On the Criteo "all campaigns" split: log loss 0.3438 (NoDeF) vs. 0.3450 (DFM) vs. 0.3571 (NAIVE); accuracy 0.8725 (NoDeF) vs. 0.8702 (DFM) vs. 0.8714 (NAIVE); AUC 0.7387 (NoDeF) vs. 0.7423 (DFM, higher) vs. 0.7349 (NAIVE). On the "recent campaigns" split: log loss 0.2575 (NoDeF) vs. 0.3689 (DFM) vs. 0.2818 (NAIVE); accuracy 0.9157 (NoDeF) vs. 0.9151 (DFM) vs. 0.9124 (NAIVE); AUC 0.7242 (NoDeF) vs. 0.7213 (DFM) vs. 0.7187 (NAIVE). |
| 12 | Applicability to a two-sided dating recommender | The nonparametric hazard idea is attractive in principle if the project's 7–30 day retention delay turns out to be multi-modal rather than exponential, since it avoids committing to a parametric delay shape. But the paper only demonstrates this at an unstated (implicitly hours-to-days, ad-click-scale) horizon on single-event ad conversion logs, with no test of the pseudo-point/kernel machinery scaling to week-long horizons, high-cardinality features beyond PCA-reduced 100 dimensions, or any two-sided/reciprocal setting. |
| 13 | Unverified claims | The paper states NoDeF "can be used for not only CVR prediction in display advertisement but also various circumstances in which delayed feedback occurs" (e.g., citing multi-touch attribution as a possible future extension) without running any experiment in such a setting — flagged as an unverified generalization claim, offered only as future work. |

## Project Relevance

Speaks to **Q3** (delay/censoring handling) as an alternative to the exponential-delay assumption used elsewhere in this lineage, via genuine survival-analysis machinery (hazard/survival function with an EM-estimated hidden "will-convert" indicator) rather than importance-sampling label correction. Does not meaningfully address Q1, Q2, Q4, Q5, Q7, or Q8.

**Low project relevance regarding horizon.** The paper never states its own delay window in wall-clock terms, working only in normalized log-delay space, and its qualitative framing of delayed feedback ("hours to days," per the ad-tech literature it cites) is consistent with the same short-horizon regime as the rest of this lineage — one to three orders of magnitude shorter than the project's 7–30 day retention window. Its principal transferable idea is methodological (nonparametric hazard modeling as a censoring-robust alternative to exponential-delay assumptions), not its specific horizon or its dataset.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `NoDeF`._

## Meta Information

- **Authors:** Yuya Yoshikawa, Yusaku Imai
- **Affiliations:** STAIR Lab, Chiba Institute of Technology; CyberAgent, Inc.
- **Venue:** arXiv preprint
- **Year:** 2018
- **Relevance:** Related
- **Priority:** 3
- nlm:3509eb18
