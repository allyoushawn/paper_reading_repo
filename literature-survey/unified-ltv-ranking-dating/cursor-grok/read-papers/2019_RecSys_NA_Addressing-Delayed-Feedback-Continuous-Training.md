# Paper Analysis: Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction

**Source:** https://arxiv.org/pdf/1907.06558.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction
- **authors or company:** Sofia Ira Ktena, Alykhan Tejani, Lucas Theis, Pranay Kumar Myana, Deepak Dilipkumar, Ferenc Huszár, Steven Yoo, Wenzhe Shi (Twitter)
- **venue:** RecSys
- **year:** 2019
- **URL:** https://arxiv.org/pdf/1907.06558.pdf
- **source type:** industry paper
- **direction:** D7
- **problem setting:** Continuous online training of Twitter display-ad CTR models where positive engagements (clicks, MRC views) arrive after random delays; fresh impressions ingested before labels resolve create fake negatives.
- **objective and label definition:** Binary click/conversion labels with incomplete observation at ingestion time. Compares five loss functions: log loss, delayed feedback loss (exponential delay model), positive-unlabeled (PU) loss, fake-negative (FN) weighted loss, FN calibration. Labels in offline eval assigned after 9-hour window; online uses real-time click callbacks with FN entering training stream.
- **prediction or incrementality:** Predicts P(click|impression) under delayed label correction—standard predictive CTR, not causal incrementality of ad exposure on advertiser revenue or user retention.
- **model architecture:** Logistic regression and Wide & Deep (4-layer MLP [400,300,200,100] + wide crosses) on thousands of sparse/categorical ad features; continuous training service publishes models every 10 minutes.
- **credit assignment:** Per-impression click label with loss corrections for unobserved positives; time-elapsed and time-to-click features for delay model in delayed-feedback loss. No user-level delayed outcome (retention/revenue) attribution.
- **training data and counterfactual handling:** Offline: 668M video-ad training examples (4 days), 7M test; Criteo public set (15.5M train). FN losses down-weight or calibrate presumed negatives using elapsed time since impression. Online: continuous stream from impression callbacks; pooled RCE eval waits 9h to remove FNs.
- **offline and online evaluation:** Offline: loss, relative cross-entropy (RCE), PR-AUC. Twitter offline: FN calibration best for logistic (RCE 12.41); Wide & Deep: PU/FN calibration/FN weighted ~RCE 13.5–13.6 vs log loss 7.81. Online (1% traffic, Wide & Deep): FN weighted RCE 13.39, RPMq +55.10% relative, monetized CTR +23.01% vs log loss.
- **reported gains:** +3% RCE offline vs prior SOTA on 668M examples; online +55% RPMq and +23% monetized CTR (FN weighted vs log loss).
- **applicability note for a two-sided dating recommender:** Directly relevant infrastructure pattern for continuous retraining when match/conversation labels arrive days later—FN-weighted and calibration losses applicable to swipe logs with delayed reciprocity outcomes.
- **applicability note for a two-sided dating recommender:** Addresses click-delay bias only, not retention/revenue objectives, bilateral congestion, or uplift of exposure; revenue metric is ad RPMq, not member LTV.
- **unverified claims:** none

## 1. Summary

**Title:** Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction
**Authors:** Sofia Ira Ktena et al. (Twitter)
**Abstract:** Studies loss functions for continuous CTR training when positive labels are delayed. Proposes FN weighted and FN calibration losses that outperform delayed-feedback and PU alternatives offline and online on Twitter ad data.

**Key contributions:**
- Systematic comparison of five delayed-feedback losses with shallow and deep models.
- FN weighted/calibration losses using importance-style correction for fake negatives.
- Production-oriented discussion of engineering cost per loss type.

**Methodology:** Continuous training on streaming impressions; exponential delay model for delayed-feedback loss; FN methods use elapsed time since impression.

**Main results:** Best offline RCE with FN calibration/weighted; large online RPMq gain with FN weighted loss.

## 2. Experiment Critique

**Design:** Public Criteo + large Twitter offline sets; three top losses taken online.

**Statistical validity:** Offline significance via unpaired t-test for top logistic result; online differences between FN methods small.

**Online experiments (if any):** 1% traffic; models retrained every 10 minutes; pooled RCE with 9h label wait.

**Reproducibility:** Criteo public; Twitter data proprietary.

**Overall:** Solid industrial delayed-feedback study focused on CTR freshness; monetization online metric is ad revenue, not user retention.

## 3. Industry Contribution

**Deployability:** Implemented in Twitter continuous training pipeline with documented serving cadence.

**Problems solved:** Fake negatives in fresh continuous-training data depressing CTR estimates.

**Engineering cost:** FN weighted/calibration moderate vs delay-model infrastructure; PU loss unstable.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First application of PU, FN weighted, and FN calibration to continuous CTR with neural models.

**Prior work comparison:** Chapelle delayed-feedback model, NoDeF, delayed bandits, standard log loss.

**Verification:** Large-scale offline and online results support FN approach over naive log loss.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Criteo display ads | Public | Yes | Conversion-delay variant constructed |
| Twitter video ads | Not public | No | 668M training examples |

**Offline experiment reproducibility:** Criteo portion reproducible; Twitter results not.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** CTR / monetized CTR—short-horizon ad engagement, not retention/revenue ranking.

**(2) Credit assignment:** Per-impression click with FN correction; no multi-day retention mapping.

**(3) Label and horizon definitions:** 9-hour label window offline; random delay distribution for clicks (minutes to hours).

**(4) Short-term + long-term heads:** Single click head only.

**(5) Prediction vs incrementality:** Predictive CTR under delayed labels.

**(6) Offline and online evaluation:** RCE, PR-AUC, RPMq; no retention or two-sided interference metrics.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not applicable (display ads).

**(8) Migration path from CTR-like model:** Loss-function upgrade within existing CTR continuous-training stack—relevant as supporting infrastructure for delayed match/conversation labels, not unified LTV objective.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Sofia Ira Ktena, Alykhan Tejani, Lucas Theis, Pranay Kumar Myana, Deepak Dilipkumar, Ferenc Huszár, Steven Yoo, Wenzhe Shi
**Affiliations:** Twitter
**Venue:** RecSys 2019
**Year:** 2019
**PDF:** https://arxiv.org/pdf/1907.06558.pdf
**Relevance:** Core
**Priority:** 1
