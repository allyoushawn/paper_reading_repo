# Paper Analysis: Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction

**Source:** https://ojs.aaai.org/index.php/AAAI/article/view/16495
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction
- **authors or company:** Yanshi Wang, Jie Zhang, Qing Da, Anxiang Zeng (Alibaba Group)
- **venue:** AAAI
- **year:** 2021
- **URL:** https://ojs.aaai.org/index.php/AAAI/article/view/16495
- **source type:** industry paper
- **direction:** D7
- **problem setting:** E-commerce CVR faces simultaneous data sparsity, sample selection bias (train on clicks, infer on all impressions), and delayed conversion feedback creating false negatives.
- **objective and label definition:** Post-click CVR over entire impression space; 7-day attribution window (\(T=7\)); labels \(Y\)=click, \(Z\)=observed conversion, \(C\)=latent eventual conversion, \(D\)=delay, \(E\)=elapsed time since click.
- **prediction or incrementality:** Predicts absolute CTR, CTCVR, CVR, and day-slot delay probabilities; not incrementality.
- **model architecture:** Multi-task ESMM-style: shared embeddings, CTR head \(p_i\), CTCVR head \(q_i\), CVR=\(q_i/p_i\); separate delay model with \(T+2\) day-slot softmax survival outputs; EM optimization for censored conversions.
- **credit assignment:** Delayed conversion mapped to original clicked user-item interaction feature vector \(X\) captured at click time.
- **training data and counterfactual handling:** Entire-space training on all impressions (ESMM chain rule) relieves selection bias; shared CTR/CVR embeddings relieve sparsity; EM E-step assigns posterior conversion weight \(w_i\) to censored clicks using survival probabilities over remaining day slots.
- **offline and online evaluation:** Alibaba e-commerce search logs (public sample: 30.6M impressions, 0.74M clicks, 14.7K conversions; product: 11.1B impressions); ROC AUC (public), GAUC (product), log loss by delay day. No online A/B reported.
- **reported gains:** Public AUC 0.7811 (+4.93% RelaImpr vs ESMM 0.7679); product GAUC 0.6181 (+6.68% RelaImpr vs ESMM 0.6107); +0.82% and +3.16% RelaImpr over DFM on public/product datasets respectively.
- **applicability note for a two-sided dating recommender:** Unifies entire-space training (all impressions/candidates, not just clicks) with delayed-label survival modeling—direct pattern for ranking all profiles while censoring not-yet-observed matches/replies/subscriptions.
  One-sided e-commerce; no reciprocity, two-stage match funnel, or retention/LTV objective—pair with DiPS/OPE or CFRR for two-sided evaluation.
- **unverified claims:** none

## 1. Summary

ESDF jointly addresses CVR data sparsity (shared CTR/CVR embeddings), sample selection bias (entire-space ESMM multi-task formulation), and delayed feedback (discretized day-slot survival model without parametric delay assumption). EM algorithm handles censored unconverted clicks by estimating posterior conversion probability from elapsed time and learned delay distribution. First public dataset with impression, click, and delayed conversion labels for entire-space CVR.

## 2. Experiment Critique

Strengths: tackles three known CVR pain points simultaneously; large-scale industrial data plus public sample release; non-parametric day-slot delay more flexible than exponential DFM. Weaknesses: no online validation; 7-day horizon may be short for dating retention; feedback delay makes absolute predictions imprecise (authors acknowledge); DFM unstable on public data due to exponential mismatch.

## 3. Industry Contribution

End-to-end Alibaba search CVR stack pattern: ESMM entire-space multi-task + survival-based delay without distribution assumptions. Released first public entire-space delayed-feedback dataset. Practical alternative to parametric DFM when delay curves are non-exponential.

## 4. Novelty vs. Prior Work

First unified solution for sparsity + SSB + delay in CVR. Builds on ESMM (Ma et al. 2018), ESM2 (Wen et al. 2020), DFM (Chapelle 2014), Yoshikawa & Imai (2018) non-parametric delay, SHIFT/NAIVE baselines.

## 5. Dataset Availability

- **Public sample dataset:** Released by authors (URL referenced in paper as URL1).
- **Product dataset:** Alibaba internal (11.1B impressions).

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
CVR prediction with CTR/CTCVR auxiliary tasks over entire impression space. Retention/LTV: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Delayed conversion mapped to original clicked user-item sample features \(X\). Slate-level: Not specified in source.

### (3) Label and horizon definitions; delay, sparsity, censoring
7-day attribution window; day-slot discretization (\(T+2\) bins). EM handles censored unconverted clicks. Sparsity: shared CTR/CVR embeddings.

### (4) Short vs long-term head fusion
Fixed chain-rule fusion: CVR = CTCVR/CTR. Delay model combined in EM log-likelihood, not learned neural fusion.

### (5) Prediction vs incrementality
Absolute probability prediction; not incrementality.

### (6) Offline and online evaluation
Offline ROC AUC/GAUC and log loss on Alibaba logs. Online: Not specified in source.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
ESMM (1-day negatives) → NAIVE (drop delayed) → SHIFT (extend window daily) → DFM (exponential delay) → ESDF (entire-space + discretized survival delay via EM).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yanshi Wang, Jie Zhang, Qing Da, Anxiang Zeng
**Affiliations:** Alibaba Group
**Venue:** AAAI 2021
**Year:** 2021
**PDF:** https://ojs.aaai.org/index.php/AAAI/article/view/16495
**Relevance:** Core
**Priority:** 2
