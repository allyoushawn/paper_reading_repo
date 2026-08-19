# Rethinking Causal Ranking: A Balanced Perspective on Uplift Model Evaluation

- **Source index:** 103
- **Source ID:** `c4848299-fb1a-4ff6-a732-61282faada22`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Minqin Zhu, Zexu Sun, Ruoxuan Xiong, Anpeng Wu, Baohong Li, Caizhi Tang, Jun Zhou, Fei Wu, Kun Kuang
- **Year / venue:** 2025 / ICML
- **Direction / priority:** D6 incrementality and causal ranking / Priority 3
- **URL:** https://openreview.net/forum?id=iJdjDM6Odd

## 1. Summary

The paper argues that standard uplift and Qini curves can mis-rank causal models even on randomized data because their value functions privilege units with positive observed outcomes and underweight negative outcomes. A biased model can therefore score above a model that better orders persuadables ahead of sleeping dogs. The proposed Principled Uplift Curve (PUC) balances contributions from positive and negative outcomes. A corresponding Principled Uplift Loss is added to a three-headed, targeted-regularization network called PTONet so training is aligned with the new ranking metric.

Evidence includes constructed cases, simulations, the public Criteo uplift benchmark, and real-world Lazada data. The indexed source states that PUC yields less biased evaluation and that PTONet outperforms comparison methods; exact aggregate result values are not reliably recoverable from the indexed text rendering.

## 2. Experiment Critique

The paper attacks an important evaluation failure rather than assuming conventional AUUC/Qini is ground truth. The case analysis exposes how a metric can reward the wrong principal-strata order, and using simulated data permits comparison with known effects. Public and industrial datasets broaden the evidence.

However, true individual effects remain unavailable in real data, so the strongest validation of ranking correctness rests on assumptions and simulation. The indexed source states standard causal-identification assumptions but does not make their plausibility auditable for every real dataset. The task is binary treatment and binary outcome; multi-action ranking, delayed value, interference, and policy-induced exposure are outside scope.

## 3. Industry Contribution / Project Relevance

For a dating recommender, the central warning is directly relevant: an uplift evaluator can select a model that appears strong while over-targeting already-successful users or harming a negative-response subgroup. PUC is a candidate offline diagnostic for ranking users or candidate exposures by incremental retention or revenue, especially when the outcome is binary.

It is not a complete marketplace objective. Treatment must be defined at the exposure or policy level, and dating violates no-interference assumptions through reciprocity and congestion. The method should be paired with randomized exploration and marketplace-aware estimators; otherwise it may optimize a well-balanced individual metric for a misspecified causal unit.

## 4. Novelty

The novelty is the value-function analysis showing a structural imbalance in common uplift curves, followed by a balanced curve and a differentiable training loss derived from it. PTONet operationalizes metric–objective alignment.

## 5. Dataset Availability

Criteo uplift data are public. Lazada data availability is **Not specified in source**. Code is reported at https://github.com/euzmin/PUC.

## 6. Community Reaction

Not specified in source beyond acceptance as an ICML 2025 poster.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Outcome type:** Binary
- **Treatment type:** Binary
- **Method family:** Uplift evaluation and direct causal-ranking optimization
- **Identification:** Potential-outcomes framework with standard causal assumptions
- **Interference:** Not modeled
- **Primary project use:** Offline incrementality metric / training loss, not end-to-end marketplace policy
