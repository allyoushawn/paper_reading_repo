# Paper Analysis: Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR Prediction

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2019 (Twitter) (RecSys) Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Title: Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR Prediction. Authors: Sofia Ira Ktena, Alykhan Tejani, Lucas Theis, Pranay Kumar Myana, Deepak Dilipkumar, Ferenc Huszár, Steven Yoo, Wenzhe Shi (all Twitter). Venue: RecSys '19 (13th ACM Conference on Recommender Systems), Copenhagen, Denmark, September 16-20, 2019.

Abstract/contribution: In continuous (online) training of CTR models, positive labels (clicks) can arrive with delay after impression. The naive strategy is to label every impression negative and later correct the label when a click arrives; this creates "fake negative" (FN) examples that bias the model toward under-estimating CTR. The paper compares five loss functions for handling this: (1) standard log loss (ignores the FN problem), (2) a delayed feedback loss (jointly models pCTR and an exponential time-to-click delay distribution, in the spirit of Chapelle 2014's DFM), (3) a positive-unlabeled (PU) loss that treats FN-labeled examples as unlabeled rather than confirmed negative, (4) a novel fake-negative-weighted (FNW) loss derived via importance sampling that asymmetrically reweights positive examples (which arrive as corrections of an earlier fake negative) and negative examples, and (5) a novel fake-negative-calibration (FNC) loss that first estimates the biased observed label distribution and then analytically inverts it to recover the true conversion probability. Three of the five loss functions (PU, FNW, FNC) are applied to this exact continuous-training CTR setting for the first time in this paper; the delayed feedback loss is adapted from prior importance-sampling-based approaches.

Methodology: Two model architectures are benchmarked — logistic regression and a wide & deep neural network (Cheng et al. 2016). Offline evaluation uses the public Criteo click-to-conversion dataset (15.5M train / 3.5M test, conversions after a click) and an in-house Twitter video-ad dataset (668M training examples). The top offline performers (FNW and FNC with the wide & deep model) are then deployed in a live continuous-training pipeline and evaluated in a 1-week online A/B experiment on 1% of Twitter's production ad traffic, where models are retrained and snapshotted every 10 minutes on a live impression/click data stream.

Main results: Offline, on the public Criteo data the delayed feedback loss gives the best relative cross-entropy (RCE 17.32) with the linear model, narrowly ahead of FN calibration (17.29). On Twitter data with the wide & deep model, FNW and FNC give the best RCE (13.54 and 13.58 respectively) and PR-AUC. Online, both FNW and FNC beat the log-loss baseline: RPMq (revenue per thousand requests) improves by +55.10% (FNW) and +54.37% (FNC), and monetized CTR improves by +23.01% (FNW) and +23.19% (FNC). The PU loss performs competitively offline but diverges after about 2 days in the online continuous-training setting and is reported only prior to divergence.

## 2. Experiment Critique

Design: The offline comparison is reasonably controlled — same architecture, same hyperparameters, five loss functions, two datasets, with a held-out Twitter evaluation set from which fake negatives were scrubbed by waiting 9 hours past the engagement window. Statistical validity is partially addressed: Tables 1/2 report an unpaired t-test (p<0.05) between the top two offline methods on Criteo/Twitter logistic-regression results, but Table 3 (wide & deep) and Table 4 (online) report no significance test, and the online RPMq/monetized-CTR gains are given as single-run relative percentages with no confidence interval or reported variance across the 1-week run. The online experiment is described by the authors as "budget-unaware" (does not account for advertiser budget pacing when deciding which ad to display), a limitation they state explicitly. Reproducibility: hyperparameters are stated (SGD, lr 0.02, batch 128, wide&deep layer sizes [400,300,200,100]), but the in-house Twitter datasets are proprietary and not released; only the public Criteo dataset supports replication, and no code is released.

## 3. Industry Contribution

This is squarely an industry-engineering paper: the loss functions studied are chosen explicitly for their compatibility with a continuous-training production pipeline (Figure 3: a streaming training service publishing model snapshots every 10 minutes to a prediction service) rather than for offline elegance alone. The paper explicitly discusses engineering-cost trade-offs — the delayed-feedback-loss approach requires maintaining and estimating a separate delay model online, adding infrastructure complexity, whereas FNW/FNC require no additional model, only a reweighting or post-hoc calibration of the existing pCTR output. This directly informs ranking-pipeline engineering: no additional serving latency is introduced (FNW/FNC change only the training loss, not the inference path), and the method integrates into an existing online-gradient-descent continuous-training loop without new feature engineering.

## 4. Novelty vs. Prior Work

The paper's own framing of its novelty: PU loss, FNW, and FN calibration are "applied to this problem for the first time," while the delayed feedback loss (importance-sampling variant) builds on prior work (Bottou et al., counterfactual reasoning and learning systems: the example of computational advertising, JMLR 2013; Chapelle, modeling delayed feedback in display advertising, KDD 2014). The paper positions itself against Chapelle 2014 (DFM, parametric exponential delay model, the dominant prior approach) and Yoshikawa & Imai 2018 (non-parametric delayed feedback model, EM-based) by noting both require maintaining and estimating an explicit delay model, which is costly in a continuous-training deep-learning setting; FNW/FNC avoid this by working directly with importance-sampling-style reweighting or calibration of the biased label distribution, without modeling delay explicitly. This is the earliest paper in this batch (2019) and the lineage root the later delayed-feedback papers in this corpus (ES-DFM, DEFER, DEFUSE) build on and benchmark FNW/FNC against.

## 5. Dataset Availability

| Dataset | Type | Size | Availability |
|---|---|---|---|
| Criteo delayed-feedback (click-to-conversion) | Public benchmark | 15.5M train / 3.5M test | Public (Criteo Labs release accompanying Chapelle 2014); exact URL not restated in this paper — Not specified in source. |
| In-house Twitter video-ad data (offline) | Proprietary | 668M training examples / 7M test | Not available — proprietary |
| Twitter production ad traffic (online A/B) | Proprietary, live | 1% of production traffic, 1 week | Not available — proprietary |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR Prediction," Ktena, Tejani, Theis, Myana, Dilipkumar, Huszár, Yoo, Shi; Twitter; RecSys '19; 2019; https://doi.org/10.1145/3298689.3347002 |
| 2 | Source type | Industry paper (Twitter), peer-reviewed at an academic venue (RecSys) |
| 3 | Direction | D7 |
| 4 | Problem setting | Continuous (online) training of a pCTR model for display/video ad ranking, where a click may arrive minutes to hours after impression; naive online labeling produces "fake negative" impressions that bias the model toward underestimating CTR. |
| 5 | Objective and label definition | Binary label: whether a user clicks (or, for video ads, achieves an MRC view) on a displayed ad. Horizon/delay handling varies by loss: log loss ignores delay entirely; the delayed feedback loss assumes an exponential distribution for time-to-click and jointly models pCTR and delay; PU loss treats currently-negative-labeled examples as unlabeled rather than confirmed negative; FNW reweights positive and negative examples via importance sampling; FNC first fits the biased observed label distribution then analytically inverts it. Delay horizon actually observed: the time-to-click distribution (Fig. 4) is shown over roughly 0-300 minutes (up to 5 hours); the online holdback evaluation set removes fake negatives by waiting up to 9 hours after the end of the engagement-label window. This is a minutes-to-hours horizon, not days or weeks. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. All five loss functions correct a label-censoring/label-bias problem (the "fake negative" problem) in a click-probability prediction; none estimate the causal effect of showing the ad. |
| 7 | Model architecture | Two architectures compared: (a) logistic regression on sparse hashed user/ad features; (b) a wide & deep network (linear component with cross-product features + 4-layer [400,300,200,100] feed-forward deep component with leaky ReLU) on the same feature set. Each of the five loss functions is combined with both architectures. |
| 8 | Credit assignment | Not applicable in the cascade sense — the paper operates at the level of a single impression-to-click label correction, not a multi-step conversion cascade or slate. Each impression gets exactly one (possibly delayed) click label; there is no aggregation across items or across a user's session. |
| 9 | Training data and counterfactual handling | Trained online via SGD on a continuous stream of impression/click data (Twitter) or offline in batch (Criteo). No counterfactual/causal adjustment; the "counterfactual handling" the paper addresses is purely the missing-label problem (the observed label distribution differs from the true label distribution because unconverted examples are provisionally labeled negative). |
| 10 | Offline and online evaluation | Offline: log loss, relative cross-entropy (RCE) vs. a naive-prediction baseline, and PR-AUC on Criteo and Twitter holdout data. Online: 1-week A/B test on 1% of Twitter production traffic using pooled RCE (control vs. treatment on pooled traffic), RPMq (revenue per thousand requests), and monetized CTR. |
| 11 | Reported gains | On the Criteo public dataset with a linear model: delayed feedback loss RCE 17.32 vs. log loss RCE 17.26. On the Twitter dataset with the wide & deep model: FNW RCE 13.54 and FNC RCE 13.58 vs. log loss RCE 7.81. Online on Twitter production traffic (wide & deep model, vs. log-loss control): RPMq +55.10% (FNW) and +54.37% (FNC); monetized CTR +23.01% (FNW) and +23.19% (FNC). |
| 12 | Applicability to a two-sided dating recommender | Not directly applicable to a two-sided/reciprocal setting — this is single-sided ad CTR prediction with no reciprocity, congestion, or slate structure. Its relevance is narrower and more foundational: the FNW/FNC correction for censored delayed binary labels is a candidate building block for how the project labels an impression whose retention/subscription outcome has not yet resolved, but the horizon here (hours) is far shorter than the project's 7-30 day retention window. |
| 13 | Unverified claims | The claim that "good performance with linear models does not necessarily translate to equivalent performance with deep models" is stated as an empirical observation from this paper's own results, not independently verified elsewhere. The online RPMq/monetized-CTR percentage gains are reported without confidence intervals or a stated significance test, so their precision should be treated cautiously. |

## Project Relevance

Speaks to **Q3** (label and horizon definitions for delayed outcomes; delay, sparsity, censoring handling) most directly — FNW/FNC are the lineage root for the censored-label correction techniques that later, more directly relevant papers in this corpus (ES-DFM, DEFER, DEFUSE) extend. Also touches **Q6** (offline/online evaluation of a delayed-label model) via its RCE/PR-AUC offline metrics and its RPMq/monetized-CTR online A/B design. **Low direct relevance to Q1, Q2, Q4, Q5, Q7, Q8** — the delay horizon here (minutes to hours) is two to three orders of magnitude shorter than the project's 7-30 day retention window and weeks-scale revenue window, the problem is single-event CTR (not a multi-step like→match→conversation→subscription cascade), there is no two-sided/reciprocal structure, and the paper does not address incrementality. The paper's core contribution — reweighting or calibrating a model trained on provisionally-negative-labeled examples — is the conceptual ancestor of any scheme the project might use to train on impressions whose 30-day retention outcome is not yet known, but the specific loss functions would need re-derivation for a delay horizon in weeks rather than hours.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `FNW-FNC`._

## Meta Information

- **Authors:** Sofia Ira Ktena, Alykhan Tejani, Lucas Theis, Pranay Kumar Myana, Deepak Dilipkumar, Ferenc Huszár, Steven Yoo, Wenzhe Shi
- **Affiliations:** Twitter (London, UK and San Francisco, USA)
- **Venue:** RecSys '19 (13th ACM Conference on Recommender Systems)
- **Year:** 2019
- **Relevance:** Core
- **Priority:** 1
- **nlm:ee57717b**
