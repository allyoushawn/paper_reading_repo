# Paper Analysis: Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay

**Source:** NotebookLM, `nlm:5a389db3-49b0-4a99-b6da-bfa1d0e295c5`
**Date analyzed:** 2026-08-16

## 1. Summary

Thomas M. McDonald (University of Manchester), Lucas Maystre (Spotify), Mounia Lalmas (Spotify), Daniel Russo (Columbia University & Spotify), Kamil Ciosek (Spotify), "Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay," KDD 2023. DOI: https://doi.org/10.1145/3580305.3599386

**Abstract (paraphrased):** Recommenders increasingly must optimize long-term satisfaction, formalized here as a multi-armed bandit with delayed rewards. Waiting for the full reward (weeks) hurts learning speed; using a short-term proxy reward misaligns with the true long-term goal. The paper resolves the tradeoff by exploiting the "progressive feedback" setting: intermediate outcomes are revealed progressively between action and full reward realization. A Bayesian filter combines these partial observations into a belief about the delayed reward, and a meta-learning step estimates the filter's prior/noise parameters from historical items. A Thompson-sampling bandit ("impatient bandit") built on this filter is applied to Spotify podcast recommendation, where the goal is identifying shows users engage with repeatedly over two months.

**Key contributions:** (1) A Bayesian filtering reward model that folds in progressively revealed intermediate outcomes to predict a delayed reward and quantify uncertainty. (2) A meta-learning procedure that estimates the filter's prior mean, prior covariance, and noise covariance from historical items via simple empirical averages. (3) The Impatient Bandit algorithm, combining the filter with Thompson sampling. (4) A real-world evaluation on Spotify podcast data showing the progressive approach substantially outperforms both a fully-delayed baseline and a short-term-proxy baseline.

**Methodology:** Actions (podcast shows) generate a reward r after a fixed delay Δ=60 days, decomposed as r = w⊤z where z is a K-dimensional trace of intermediate daily engagement indicators (here K=59, w=1, so r is simply the count of active days). A generative model assumes the mean trace per action is drawn from a multivariate Gaussian N(μ, Σ) and each observed trace is a noisy copy N(0, V). Given a partially-observed trace (first ℓ elements), Bayesian updating yields a closed-form Gaussian posterior on the mean trace and, by linearity, on r. Prior parameters {μ, Σ, V} are meta-learned via empirical averages over a disjoint set of established shows. The Impatient Bandit algorithm updates each candidate arm's posterior every round using all newly revealed observations, then applies Thompson sampling (sample a reward per arm, pick the arm with the highest sample) to select actions, with a batched (B actions/round) extension.

**Main results:** Evaluated on Spotify podcast consumption data (Sept 2021–May 2022; 8.77M activity traces, 26M cumulative active-days; disjoint train/validation cohorts of 200 shows each). Reward-model evaluation: stickiness predictions are reasonably accurate after only 10 days of observed data; 10 days of data explain over 50% of the noise-covariance (aleatoric) uncertainty, and prior-covariance uncertainty is 50% explained by 8 days and 95% explained within a month. Bandit evaluation (180 simulated rounds ≈ 6 months, 10 repeats): the progressive (impatient) bandit tracks close to an unrealistic Oracle baseline and substantially beats both a Delayed-feedback baseline (uninformed for the first 60 rounds) and a Day-two-proxy baseline (plateaus after ~1 month because the proxy is misaligned with true stickiness), including in a dynamic setting where the show library is continuously refreshed.

## 1b. Surrogate Construction, Validation, and Failure Mode (batch-specific extraction)

**Surrogate/proxy construction:** The long-term "stickiness" reward (days of engagement over a 60-day post-recommendation window) is estimated by Bayesian-filtering a progressively-revealed 59-dimensional binary daily-engagement trace against a meta-learned prior (mean μ, prior covariance Σ, noise covariance V) fit from historical items. This is not a separately-engineered short-term proxy metric substituted for the long-term one (as in a classical "autosurrogate" or "day-N proxy"); rather, the surrogate is the partial observation of the long-term metric itself, combined via exact Gaussian belief updating with everything the model has learned about how early days correlate with the eventual total across similar historical items. The linear reward form r=w⊤z (with w the all-ones vector here) is explicitly noted by the authors as an approximation: if the true long-term target y is not exactly a linear function of the trace z, then r is itself a surrogate index in the Athey-et-al. sense, and the authors flag that using it as such requires two testable assumptions: the surrogacy assumption (y ⊥ action | r) and the comparability assumption (the learned relationship generalizes from training to evaluation data).

**Validation procedure:** Multi-part and unusually rigorous for this batch. (1) Predictive-accuracy validation: mean absolute error of predicted vs. ground-truth (empirical) stickiness as a function of days observed and number of traces used, on a held-out validation cohort of shows disjoint from the training cohort used to fit the meta-learned prior. (2) Explained-variance decomposition: the fraction of total noise-covariance and prior-covariance variance captured as a function of days observed, directly quantifying how much of the long-term uncertainty a short observation window resolves. (3) End-to-end decision-quality validation: bandit regret and selection-entropy compared against a Delayed baseline (isolates the cost of waiting for full feedback), a Day-two-proxy baseline (isolates the cost of using a poorly-aligned short-term proxy), and an Oracle (upper bound), across three traffic scales and a dynamic (evolving item set) scenario — this directly measures whether the surrogate's uncertainty reduction translates into better sequential decisions, not just better point predictions.

**Stated failure mode:** The authors are explicit that the day-two proxy — "representative of short-term proxies widely used in recommender systems, such as the click-through-rate, the dwell time, or the conversion rate" — performs comparably to the progressive approach only for the first month, after which its regret rapidly plateaus and its action-selection entropy collapses toward zero: the bandit converges on repeatedly recommending a small, sub-optimal subset of shows because the proxy is a noisy, poorly-aligned indicator of true 60-day stickiness. Separately, the authors flag two structural failure conditions for their own method: (a) if the surrogacy or comparability assumptions above are violated, the linear reward is no longer a faithful stand-in for the true long-term target and should be tested empirically before being trusted; (b) the Gaussian trace-noise assumption is acknowledged to be "arguably a poor model" for the binary daily activity indicators actually used, justified only asymptotically via the Central Limit Theorem for large numbers of traces per item — a new or low-traffic item would not have this protection.

## 2. Experiment Critique

- **Design:** Reward-model evaluation uses a clean train/validation split across disjoint shows and time windows, avoiding information leakage. Bandit evaluation is a simulation replaying real historical Spotify traces rather than a live online experiment, so the counterfactual reward for actions not actually taken is approximated by resampling from the empirical trace pool, not a true online A/B test.
- **Statistical validity:** Bandit results are averaged over 10 repeated runs with confidence intervals reported; comparisons across three traffic-volume regimes (10/50/200 actions per day) and two library sizes (N=50, N=200) support the robustness of the qualitative ranking (Progressive > Day-two proxy > Delayed, Progressive ≈ Oracle).
- **Online experiments:** None reported — the "bandit" evaluation is an offline replay simulation on logged Spotify data, not a live production deployment.
- **Reproducibility:** Method and update equations are given in full closed form (Algorithms 1–2); the underlying Spotify dataset is proprietary and not released, so exact reproduction is not possible, though the algorithm itself is straightforward to reimplement on comparable data.
- **Overall:** Experimentally strong on the specific question it asks (does progressive Bayesian filtering beat delayed/proxy baselines in simulated sequential decision-making), but the evaluation stops short of a live online test, and the method is explicitly non-personalized, limiting direct transfer to the project's per-user ranking setting.

## 3. Industry Contribution

- **Deployability:** High for content-exploration/cold-start-style problems structurally similar to podcast-show discovery — the closed-form Bayesian updates are cheap (matrix operations on a K-dimensional trace, K=59 here) and the meta-learning step requires only empirical averages over historical items, not gradient-based training.
- **Problems solved:** Directly solves "we can't wait 60 days to know if a new item is good" by using partial observations that arrive daily, which is structurally the same shape as the project's 7–30 day retention delay.
- **Engineering cost:** Moderate — requires maintaining per-arm partial-trace state and running the iterative posterior update at each round; the contextual extension (sketched but not implemented) that would be needed for a per-user personalized version is explicitly left as future work, so bridging to the project's per-(A,B)-pair ranking setting is nontrivial. No online-serving latency concerns are discussed since the application is item-level exploration, not per-request ranking.

## 4. Novelty vs. Prior Work

**Claimed novelty:** The Bayesian filtering approach exploiting progressively (not i.i.d.) revealed intermediate outcomes, the meta-learning procedure for the filter's prior from historical items, and the resulting Impatient Bandit algorithm for this specific "progressive feedback" bandit setting.

**Prior work most heavily built on:**
- Maystre, Lalmas, et al., "Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective" — defines the exact "clickiness"/"stickiness" metrics this paper adopts for the podcast application.
- Athey et al., "The Surrogate Index" — formalizes combining short-term proxies to estimate long-term outcomes; explicitly invoked for the surrogacy/comparability caveats on the linear reward model.
- Hohnhold, O'Brien, and Tang, "Focusing on the Long-Term: It's Good for Users and Business," KDD 2015 — industry motivation for shifting from short-term clicks to long-term satisfaction.
- Li, Chu, Langford, and Schapire, "A Contextual-Bandit Approach to Personalized News Article Recommendation," WWW 2010 — basis for the paper's sketched (unimplemented) contextual extension.
- Russo, Van Roy, et al., "A Tutorial on Thompson Sampling" — the exploration-exploitation mechanism the impatient bandit builds on.
- Kandasamy et al., "Parallelised Bayesian Optimisation via Thompson Sampling" — basis for the batched/parallel-action extension.
- Zheng et al., "DRN: A Deep Reinforcement Learning Framework for News Recommendation," and Zou et al. — RL alternatives for reasoning about delayed engagement, positioned as heavier-weight alternatives to this paper's bandit approach.

## 5. Dataset Availability

| Dataset | Source | Size | Public? |
|---|---|---|---|
| Podcast consumption traces | Spotify (Sept 2021–May 2022) | 8.77M activity traces, 26M cumulative active-days, 400 shows (200 train / 200 validation) | Proprietary, not released |

No public benchmark is used; the dataset is internal to Spotify and not available for independent replication.

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay," McDonald, Maystre, Lalmas, Russo, Ciosek (Spotify/University of Manchester/Columbia), KDD 2023. URL: https://doi.org/10.1145/3580305.3599386 |
| 2 | Source type | Industry paper (Spotify-affiliated, published at an academic venue). |
| 3 | Direction | D3 |
| 4 | Problem setting | Multi-armed bandit content exploration with a fixed 60-day delayed reward, where intermediate daily engagement outcomes are progressively revealed between action and full reward realization. Applied to identifying new podcast shows worth exploring. |
| 5 | Objective and label definition | Reward r = number of days (0–59) a user engages with a show in the 59 days after a first listen ("stickiness"); observed after a fixed 60-day delay. Handled via progressive feedback: each daily binary activity indicator zₖ is observed with its own short delay (k+1 days), and a Bayesian filter forms a belief over r at every round from whatever prefix of the trace has been observed so far. No formal censoring/survival model is used; delay is handled by exact partial-trace Bayesian updating, not by discounting or imputation. |
| 6 | Prediction or incrementality | Prediction only. Paper's own wording: "we develop a predictive model of delayed rewards," and "we focus on estimating stickiness... we do not model the click-through rate." It does not estimate the causal/incremental effect of showing a given item vs. not showing it. |
| 7 | Model architecture | Bayesian linear-Gaussian filter over a K-dimensional intermediate-outcome trace (conjugate updating, closed-form posterior mean/covariance), with prior parameters meta-learned by empirical averaging over historical items; combined with Thompson sampling for action selection (Algorithm 2). No neural architecture. |
| 8 | Credit assignment | Direct, pointwise item-level: the user-level delayed engagement trace generated by a user who discovers a show is assigned entirely to that one recommended show (action). No slate-level or multi-item credit assignment; the method is explicitly non-personalized. |
| 9 | Training data and counterfactual handling | Reward-model prior/covariance parameters are estimated via simple empirical averages over historical items' consumption traces (no counterfactual/causal correction; this is observational meta-learning, not off-policy correction). The bandit itself handles the standard sequential exploration-exploitation tradeoff via Thompson sampling, not an off-policy or counterfactual estimator. |
| 10 | Offline and online evaluation | Offline only. Reward-model evaluation: MAE of stickiness prediction vs. days/traces observed, on a held-out validation cohort. Bandit evaluation: simulated regret and action-entropy over 180 rounds (~6 months) on real Spotify logs, compared to Delayed, Day-two-proxy, and Oracle baselines, across three traffic scales and a dynamic-library scenario. No live online A/B test. |
| 11 | Reported gains | On the Spotify podcast dataset: stickiness predictions are reasonably accurate after only 10 days of observation; 10 days of data explain >50% of aleatoric (noise) uncertainty in the 60-day reward, and 95% of prior-covariance variance is explained within one month. In bandit simulation, the progressive approach tracks close to the Oracle and considerably outperforms both Delayed and Day-two-proxy baselines in average per-step regret, including in the dynamic (continuously refreshed) show-library setting. |
| 12 | Applicability to a two-sided dating recommender | The progressive-feedback Bayesian-filtering mechanism is directly transferable to shortening the retention-label wait (7–30 days) in the project's setting. It is non-personalized, item-only, and has no notion of reciprocity, congestion, or a second user side, so it would need substantial extension before use. |
| 13 | Unverified claims | None flagged as unverified beyond the authors' own explicitly-stated caveats (surrogacy/comparability assumptions on the linear reward, and the Gaussian-noise approximation for binary daily indicators), which the paper itself surfaces rather than asserts without evidence. |

## Project Relevance

Directly answers **Q1** and **Q3** (acting on and defining a long-horizon retention-like objective from progressively-revealed short-term signals, with an explicit horizon of 60 days and no waiting required for the full window) and **Q6** (its core offline-evaluation methodology — predictive-accuracy and explained-variance validation, plus simulated sequential-decision evaluation against Delayed/Proxy/Oracle baselines — is a template the project could adapt). Provides a partial, single-value-head answer to **Q4** in that it replaces separate short-term/long-term heads with one Bayesian-filtered belief over the long-term target, though this is not framed by the authors as a fusion architecture question.

Does not address **Q2** (the method is pointwise/item-level by construction and explicitly non-personalized — no aggregation across a slate or across sessions), **Q5** (predicts an outcome, not the causal effect of exposure, by the authors' own words), **Q7** (no two-sided market, congestion, or fairness treatment — the setting is single-sided content exploration), or **Q8** (no discussion of migrating an existing CTR/CVR + uplift-blend system toward this approach).

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `ImpatientBandit`._

## Meta Information

- **Authors/Affiliations:** Thomas M. McDonald (University of Manchester), Lucas Maystre, Mounia Lalmas, Kamil Ciosek (Spotify), Daniel Russo (Columbia University & Spotify).
- **Venue:** KDD 2023 (29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- **Year:** 2023
- **Relevance:** Core
- **Priority:** 1
- **NotebookLM source:** `nlm:5a389db3-49b0-4a99-b6da-bfa1d0e295c5`
