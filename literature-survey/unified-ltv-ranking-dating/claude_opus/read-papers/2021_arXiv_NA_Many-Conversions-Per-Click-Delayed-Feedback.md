# Paper Analysis: Handling Many Conversions per Click in Modeling Delayed Feedback

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2021 (Google) (Arxiv) Handling many conversions per click in modeling delayed feedback.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Title/authors/venue: "Handling many conversions per click in modeling delayed feedback," Ashwinkumar Badanidiyuru, Andrew Evdokimov, Vinodh Krishnan, Pan Li, Wynn Vonnegut, Jayden Wang (Google Research / Google), arXiv, January 2021.

Key contribution: The first work in this line to move beyond "at most one conversion per click" (OPC) — the restriction shared by essentially all prior delayed-feedback papers, including Chapelle 2014, Yoshikawa & Imai 2018, and Ktena et al. 2019 (paper #1 in this batch) — to handle "many per click" (MPC) campaigns, where a single click can generate an arbitrary number of valued post-click events within an advertiser-defined attribution window (as short as 2 hours or as long as 90 days). The model predicts the expected number (or value) of post-click conversions, trained close to real time (online training) while remaining unbiased despite training on incomplete/immature labels.

Methodology (three core ideas): (1) Split the overall label into a sum of sub-labels over different, **overlapping** delay buckets [t_p, t_p+d_1], [t_p, t_p+d_2], ..., [t_p, t_p+M] (M = the attribution window), and train a separate sub-model f_i on each bucket, using only examples whose bucket-label is already mature (age ≥ t_p + d_{i+1}). (2) "Thermometer encoding" of the label — buckets are nested/overlapping rather than disjoint, so each sub-model's target is "total conversions from time 0 to the end of its own window"; this avoids the label sparsity that comes from over-partitioning, and means only one sub-model needs to be evaluated at inference (the latest one whose prediction interval has already elapsed), reducing serving cost. (3) "Auxiliary information" — feed each sub-model the partial/observed label-so-far (events observed up to that sub-model's bucket start) as an input feature; this is shown (via a mutual-information argument and an empirical Pearson-correlation heatmap across delay buckets) to reduce prediction variance and correct for temporal drift in the underlying delay distribution.

Datasets and baselines: A single proprietary dataset — app-install ads from a commercial mobile app store, using post-click in-app events as conversions, evaluated in an online-training regime. Ablations serve as the "baselines": M1 (neglect delay, label with <1-day-old events), M2 (fixed training delays, 7d/15d), M3 (train only on fully mature data), M4 (remove thermometer encoding), M5 (remove auxiliary information), and an "Oracle" (trained on complete, non-delayed labels — an unattainable upper bound).

Main results: The proposed model achieves near-zero mean prediction bias (≤1%, described qualitatively due to proprietary-data restrictions) versus large positive bias in M4/M5 and large negative bias in M1/M2. It achieves the largest Poisson log-loss improvement over the M3 (mature-data-only) baseline across all data (-8.6%), long-delay advertisers (-10.16%), and new advertisers (-1.81%), approaching the Oracle's improvements (-9.1%/-10.87%/-2.0% respectively) while training close to real time.

## 2. Experiment Critique

The evaluation uses a single proprietary Google Ads dataset (app-install ads), with no public benchmark and no code release, limiting external reproducibility. Accuracy results (Poisson log loss) are given as relative percentage improvements without confidence intervals, and bias results are given only qualitatively ("≤1%", plotted curves without numeric axis values) — the paper states explicitly that exact bias numbers are withheld "due to proprietary nature of the dataset," which weakens independent verification of the calibration claim. The ablation design (M1-M5, Oracle) is well-constructed and isolates each of the three core design choices (delay-bucket splitting, thermometer encoding, auxiliary information) individually, which is a methodological strength. No online A/B test against production traffic is reported — the evaluation is an offline-style backtest run "as if" in an online-training regime (train once, visit each example once in time order), not a live experiment.

## 3. Industry Contribution

This is an explicitly production-motivated paper from Google Ads: the entire framing is about training a conversion-value model close to real time in an online-training pipeline (citing McMahan et al. 2013's "Ad click prediction: a view from the trenches" for precedent) rather than offline in batch, and the design goal is to minimize the trade-off between training on fresh (but immature/incomplete) data and training on old (but complete) data. The thermometer-encoding design choice is explicitly justified by inference cost: only one sub-model needs to be evaluated at serving time instead of summing multiple bucket sub-models. The paper also discusses handling conversion retractions/restatements (a real operational concern for ad platforms) as a straightforward extension via signed labels, showing awareness of production edge cases beyond the core algorithm.

## 4. Novelty vs. Prior Work

The paper explicitly surveys the delayed-feedback literature (Chapelle 2014's exponential DFM; Ktena et al. 2019's importance-sampling/PU losses; Yoshikawa & Imai 2018's non-parametric model; Ji et al. 2017's Weibull model; Safari et al. 2017; Vernade et al. 2017's bandit formulation; Saito, Morishita & Yasui 2020's dual learning algorithm — the same DLA-DF paper as #4 in this batch; Su et al. 2020 — the TS-DL paper, #2 in this batch; Kato & Yasui 2020) and states that "all following papers on this problem have been restricted to the special case of at most one conversion per click." It identifies Choi et al. 2020 (AdKDD) as the first paper to attempt multiple conversions per click, via a negative binomial distribution extension of Chapelle 2014, but critiques that approach on two grounds: it only handles integer conversion counts (not float/value targets), and its loss function is non-convex, causing instability when trained on incomplete/immature online data (the model can degenerately predict either high-rate/long-delay or low-rate/short-delay). This paper's own approach avoids any parametric delay-distribution assumption entirely, addressing both weaknesses.

## 5. Dataset Availability

| Dataset | Type | Size | Availability |
|---|---|---|---|
| App-install ads, commercial mobile app store (Google Ads) | Proprietary, online training stream | Not specified in source (no example counts given) | Not available — proprietary |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Handling many conversions per click in modeling delayed feedback," Badanidiyuru, Evdokimov, Krishnan, Li, Vonnegut, Wang; Google; arXiv; 2021; https://arxiv.org/abs/2101.02284 |
| 2 | Source type | Industry paper (Google), arXiv preprint |
| 3 | Direction | D7 |
| 4 | Problem setting | Predicting the expected number or total value of post-click conversions in "many-per-click" (MPC) ad campaigns, where a click can generate any number of valued events (e.g., in-app purchases) within an advertiser-defined attribution window of 2 hours to 90 days, trained close to real time under online training. |
| 5 | Objective and label definition | Objective: expected count (Poisson regression) or expected value of post-click conversion events within window [t_p, t_p+M]. Label defined as a sum of sub-labels over overlapping delay buckets via "thermometer encoding" — each sub-model f_i predicts the total number/value of events from time 0 up to its own bucket boundary d_i, trained only on examples whose bucket is mature; at prediction time, the observed (mature) partial label is added to the latest applicable sub-model's prediction of the remaining, immature portion. Horizon: MPC attribution windows M range from 2 hours to 90 days in the advertiser-facing product, though the specific evaluation dataset's window is not stated numerically; the ablations use fixed training delays of 7 and 15 days (M2) as points of comparison. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. It estimates the expected number/value of conversions attributable (by last-click convention) to a click, under an unbiasedness requirement with respect to the eventual mature label, not the causal effect of the ad exposure. |
| 7 | Model architecture | Categorical features embedded into a dense vector space and passed through a fully connected deep neural network (layer sizes not specified in source). The core architectural innovation is not the network itself but the training/label-construction scheme: multiple "student" sub-models, each responsible for a different, overlapping training-delay bucket [t_p, t_p+d_i], each taking as auxiliary input the partial "label so far" observed up to its own bucket start (in addition to standard pre-click features X_p). Loss: Poisson regression (negative Poisson log-likelihood), stated to generalize to other count/value regression losses. Optimizer: AdaGrad, trained online in one sequential pass over time-ordered data (continuing to train as new data arrives), using an ensemble of models per variant for result stability. |
| 8 | Credit assignment | Single click → aggregated sum of all its post-click conversion events within the attribution window (last-click attribution convention, per Chapelle 2014). This is exactly the multi-valued-event aggregation the project needs: multiple conversions are **summed** into a single trainable target (not discounted or capped) — each thermometer-encoded sub-model's target is "total number/value of events observed from time 0 to time d_i," a running sum, with no explicit recency discounting and no cap on the number of events counted within the attribution window. |
| 9 | Training data and counterfactual handling | Trained online, visiting each example once in time order, on labels that may be incomplete (immature) at training time. No causal/counterfactual adjustment is used; "unbiasedness" here refers to statistical unbiasedness of the label-completion estimator with respect to the eventual true (mature) count/value, not counterfactual/causal unbiasedness. Handles distributional drift by conditioning sub-models on auxiliary "label so far" information rather than assuming a fixed, stationary delay distribution. |
| 10 | Offline and online evaluation | Evaluated via an online-training-style backtest (each example trained once, in time order, evaluated as it would have performed at each point in time) rather than a live A/B test. Metrics: negative Poisson log-likelihood (accuracy) and mean prediction bias (ratio of predicted to eventual mature label) over time, on the full dataset, on long-delay-advertiser slices, and on new-advertiser (<10-day-old campaign) slices. No online production experiment reported. |
| 11 | Reported gains | Poisson log-loss improvement vs. the M3 (mature-data-only) baseline on the app-install-ads dataset (Table 2): -8.6% on all data, -10.16% on long-delay advertisers, -1.81% on new advertisers — approaching the Oracle upper bound of -9.1%/-10.87%/-2.0% respectively. Bias is reported only qualitatively as "≤1%" due to proprietary-data restrictions on exact figures. |
| 12 | Applicability to a two-sided dating recommender | Directly structurally relevant: the project's cascade (impression → like → match → conversation → subscription) is exactly a "many conversions per click" (many valued events per exposure) structure, and this paper's overlapping-delay-bucket + thermometer-encoding + auxiliary-partial-label design is a candidate template for summing multiple valued post-impression events into one trainable target without a parametric delay assumption. The auxiliary "label so far" mechanism is also a plausible way to recalibrate a retention/revenue estimate as more of the 7-30 day window elapses. |
| 13 | Unverified claims | The bias improvement claim ("bias of the new model is ≤1%, showing that it is completely calibrated") is asserted without releasing the underlying numeric bias values, "due to proprietary nature of the dataset" — this is explicitly acknowledged by the authors as an evidentiary gap, not an independently verifiable number. The claim that "our results trivially generalize to batch training" is stated but not empirically tested in this paper (only online training is evaluated). |

## Project Relevance

Speaks most directly to **Q2** (attributing a user-level, delayed, multi-event outcome to an item-level decision) — this is the batch's most structurally relevant paper: the project's impression-to-{like, match, conversation, subscription} cascade is precisely the "many conversions per click" problem this paper solves, and its delay-bucket-sum + thermometer-encoding + auxiliary-partial-label design directly answers "how do you aggregate multiple valued events from one exposure into one trainable target" (summed, not discounted or capped, within a bounded attribution window). Also speaks to **Q3** (delay/censoring handling, via the mature-vs-immature label-completion mechanism) and **Q6** (bias/calibration as an offline evaluation criterion for delayed labels). **Does not address Q1** (the objective is still conversion count/value, not retention framed as an LTV objective), **Q4, Q5** (no fusion of short/long-term heads, no incrementality), **Q7** (no two-sided/reciprocal/congestion treatment), or **Q8** (no migration-path discussion). The paper's own attribution windows (2 hours to 90 days) do overlap the top end of the project's 30-day retention horizon, making it one of the closer horizon matches in this batch, though the specific evaluated dataset itself does not report its window length.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Ashwinkumar Badanidiyuru, Andrew Evdokimov, Vinodh Krishnan, Pan Li, Wynn Vonnegut, Jayden Wang
- **Affiliations:** Google Research; Google
- **Venue:** arXiv preprint (arXiv:2101.02284)
- **Year:** 2021
- **Relevance:** Related (structurally Core to Q2 — the multi-conversion aggregation mechanism is directly applicable)
- **Priority:** 2
- **nlm:4ef16774**
