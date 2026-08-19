# Delayed Feedback Modeling with Influence Functions

- **Source index:** 107
- **Source ID:** `bffc8cb9-d318-4273-bc5e-2e458c5cf253`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Chenlu Ding, Jiancan Wu, Yancheng Yuan, Cunchun Li, Xiang Wang, Dingxian Wang, Frank Yang, Andrew Rabinovich
- **Affiliations:** USTC, Shanghai Key Laboratory of Data Science, Hong Kong Polytechnic University, Upwork
- **Year / venue:** 2026 / AAAI
- **Direction / priority:** D7 delayed feedback / Priority 3
- **URL:** https://github.com/oceanoceanna/IF-DFM

## 1. Summary

IF-DFM updates a conversion-rate model when late conversions and new observations arrive without fully retraining or fitting a separate delay model. Influence functions approximate how corrected labels and added samples would move the optimum. The expensive inverse-Hessian–vector product is recast as stochastic optimization. Offline and online variants adjust a pretrained model using delayed conversions, with the online version also incorporating new data to track preference drift.

Tests use public Criteo and Taobao logs, temporal splits, four backbones, and 13 baselines. Criteo has 4,019,339 clicks and 22.27% CVR; Taobao has 8,544,800 interactions/click records and 1.00% CVR as reported. Across Criteo backbones, IF-DFM reports average gains over the best baseline of 0.55% AUC, 1.29% PRAUC, and 4.99% log loss, recovering roughly 82–86% of the gap from vanilla to full retraining. On Taobao it reports +0.28% AUC and +0.94% PRAUC. The parameter update adds 14.8 seconds to a 1,351.4-second vanilla training run in one timing table.

## 2. Experiment Critique

The study is strong on breadth: public datasets, temporal rather than random splits, four common backbones, many delayed-feedback baselines, drift tests, and reported significance against the best baseline. Full retraining provides a useful oracle-like reference.

Influence approximations can be fragile for non-convex deep models and large parameter moves. The method assumes gradient access and, as the authors state, access to the full training set. Offline replay does not demonstrate business lift; the paper explicitly leaves real A/B deployment to future work. Conversion labels and delays may also be policy-dependent rather than missing only because time has not elapsed.

## 3. Industry Contribution / Project Relevance

Dating retention and revenue labels mature over days or weeks, so naive recent-window training creates false negatives. IF-DFM provides a practical correction layer that can incorporate late subscriptions, renewals, or 30-day returns without waiting for every label or rebuilding the model.

It should not be mistaken for the ranking objective. It predicts observational conversion and does not address incremental effects, reciprocity, candidate congestion, or the success paradox. For the unified LTV model, influence updates are most credible as a label-maturation mechanism with bounded update norms, periodic exact retraining, and drift monitoring.

## 4. Novelty

The paper replaces explicit delay/label-correction models with an influence-function approximation to the parameter change caused by mature labels and new data, plus a scalable stochastic solver.

## 5. Dataset Availability

Criteo conversion logs and the Taobao/Tianchi interaction dataset are public. Code is available at https://github.com/oceanoceanna/IF-DFM.

## 6. Community Reaction

Not specified in source beyond AAAI 2026 publication.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Outcome:** Delayed binary conversion
- **Metrics:** AUC, PRAUC, log loss, relative improvement
- **Method:** Influence-function parameter correction
- **Online experiment:** Not reported
- **Interference / causality:** Not modeled
- **Project role:** Delayed-label correction and rapid refresh
