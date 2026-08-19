# Tackling Interference Induced by Data Training Loops in A/B Tests: A Weighted Training Approach

- **Source index:** 105
- **Source ID:** `8a6bd8c7-0b70-4613-90a8-dab7168c19f1`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Author:** Nian Si
- **Affiliation:** University of Chicago Booth School of Business
- **Year / venue:** 2024 / arXiv preprint
- **Direction / priority:** D6 experimentation under interference / Priority 3
- **URL:** https://arxiv.org/abs/2310.17496

## 1. Summary

The paper identifies interference caused by the recommender data-training loop. During an A/B test, control and treatment algorithms generate different data distributions; pooling those observations to retrain shared behavior models changes both arms’ future predictions and outcomes. Weighted training estimates how likely each observation is under the treatment versus control data-generating process, then reweights training losses so arm-specific target distributions do not shift. The paper proves an efficiency property: among estimators that avoid training-distribution shifts, the proposed weighting has the least variance under its conditions.

Simulation experiments model short- versus long-video recommendations ranked by finishing-rate and stay-duration predictions. Across 100 replications, weighting generally has lower bias than pooling, snapshot, or arm-wise data splitting, while splitting has much larger variance. In one reported setting (treatment probability 0.2), weighted bias is 0.002 for short-video proportion, −0.008 for stay duration, and 0.000 for finishing rate. An appendix A/A test also shows a concerning 0.47 type-I error for the weighted estimator on one proportion metric, although its other two reported type-I errors are 0.07 and 0.08.

## 2. Experiment Critique

The paper cleanly separates an often-ignored interference channel from ordinary user or item spillovers. Comparisons cover pooling, data splitting, and frozen snapshots, and multiple allocation probabilities expose the bias–variance tradeoff.

Evidence is entirely simulated, and correct weights require an accurate model of cross-arm appearance probabilities. Positivity problems or policy drift can produce unstable weights. The reported A/A anomaly deserves investigation before deployment because it suggests ordinary standard errors may not capture adaptive-loop dependence. The setup also assumes a stylized retraining cycle and does not evaluate delayed outcomes, two-sided capacity, or a live system.

## 3. Industry Contribution / Project Relevance

This is a direct warning for dating experiments: if match, reply, retention, or revenue models are retrained on traffic from both experiment arms, the arms cease to represent isolated policies. A treatment that changes exposure and behavior also changes future labels and shared embeddings.

Weighted training could preserve arm-specific counterfactual training regimes while using more data than strict splits. For the unified LTV ranker, experiment design should log policy/arm propensities, version all upstream models, and report results with a frozen-model or data-diverted sensitivity arm. This method addresses evaluation contamination, not reciprocity or the unified objective itself.

## 4. Novelty

The novelty is treating the training distribution as the interference pathway and deriving a distribution-preserving, variance-efficient weighting scheme for adaptive recommender experiments.

## 5. Dataset Availability

The experiments are simulated. A public dataset or implementation is **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2026_arXiv_NA_Long-Term-Evaluation-Industry-Learnings.md](./2026_arXiv_NA_Long-Term-Evaluation-Industry-Learnings.md) | Introduction / Summary | Explicitly mentions full title in baseline or comparison context. |

## 8. Meta Information

- **Data domain:** Simulated video recommendation
- **Outcomes:** Short-video share, stay duration, finishing rate
- **Interference channel:** Pooled observations alter subsequent shared model training
- **Estimator:** Propensity-style weighted training loss
- **Main risk:** Weight misspecification and adaptive dependence
- **Project role:** Experiment validity safeguard
