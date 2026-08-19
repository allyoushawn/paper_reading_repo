# Paper Analysis: Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction

**Source:** https://ojs.aaai.org/index.php/AAAI/article/view/25583/25355
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction
- **authors or company:** Hongzu Su, Zhekai Du, Jingjing Li, Lei Zhu, Ke Lu (UESTC; Shandong Normal University; Tencent Games advertising data)
- **venue:** AAAI 2023
- **year:** 2023
- **URL:** https://ojs.aaai.org/index.php/AAAI/article/view/25583/25355
- **source type:** academic (industry data)
- **direction:** D4
- **problem setting:** Cross-domain supervised LTV prediction: transfer from a data-abundant Tencent Games advertising platform (source) to a data-scarce target platform advertising the same game.
- **objective and label definition:** LTV = total consumption over trailing 7 days linked via anonymous ad identifier (e.g., IDFA); ZILN-variant loss (payment-indicator cross-entropy + lognormal NLL on positives); no censoring/survival handling discussed.
- **prediction or incrementality:** Direct outcome prediction only; domain adaptation aligns distributions, not treatment effects.
- **model architecture:** Two-stage CDAF: source expert (CTR-style embedding + ZILN predictor) pre-trained on source; target model with shared embedding Et, dual predictors P^s_t and P^t_t; sliced Wasserstein discrepancy on representations + ℓ1 alignment of predictor outputs; inference = mean of both predictors.
- **credit assignment:** User-level 7-day consumption aggregated by ad identifier; no per-impression or per-exposure decomposition.
- **training data and counterfactual handling:** Five paired G1–G5 datasets from three months of Tencent Games advertising logs; observational supervised regression; domain adaptation (SWD + DPO), not propensity/causal correction.
- **offline and online evaluation:** Offline only on target-domain test sets: AUC (payment probability) and normalized Gini (LTV ranking); no online A/B reported.
- **reported gains:** vs single-domain target training: average AUC improvements 6.8–14.5% across eight backbones; vs fine-tuned source expert on Mixed model: +3.2–9.6% AUC and +7.4–24.7% Gini across G1–G5; example DCNv2 on G2: +13.7% AUC (abstract).
- **applicability note for a two-sided dating recommender:** Transferable idea: bootstrap LTV/retention models from a data-rich market/cohort to a sparse one via representation alignment.
- **applicability note for a two-sided dating recommender:** Not ranking, reciprocity, or exposure allocation—advertising LTV regression on 7-day spend only.
- **unverified claims:** "First attempt at domain adaptive LTV prediction" is authors' priority claim, not independently verified here.

## 1. Summary

CDAF addresses scarce consumption labels on new/low-traffic ad platforms by pre-training a ZILN LTV model on a related high-volume source platform, then adaptively fine-tuning on the target with sliced Wasserstein alignment of user representations and dual predictors with ℓ1 output alignment to preserve both domain-invariant and domain-specific signals. Evaluated on five real Tencent Games source/target pairs with ~30× sample imbalance.

## 2. Experiment Critique

Comprehensive backbone sweep (DNN, WDL, DCN, DeepFM, FiBiNet, GateNet, DCNv2, Mixed) and ablations (WD, ℓ1, per-predictor). No statistical significance tests or confidence intervals. All offline; no deployment A/B. Ablation framing that missing components "do not lead to severe degradation" is somewhat at odds with numeric drops (e.g., w/o target predictor on G1).

## 3. Industry Contribution

Motivated by >4-order-of-magnitude funnel from ad request to consumption. Backbone-agnostic plug-in atop standard CTR architectures already used in ad systems. Code: https://github.com/TL-UESTC/CDAF

## 4. Novelty vs. Prior Work

Builds on ZILN (Wang, Liu & Miao 2019), sliced Wasserstein discrepancy (Lee et al. CVPR 2019), and supervised domain adaptation. Positions against TSUR (KDD 2021) and Vanderveld et al. (KDD 2016) as requiring abundant target labels.

## 5. Dataset Availability

G1–G5 Tencent Games advertising pairs; proprietary, not public. Source train sizes 2.9M–6.7M; target train 2,530–183,413 per Table 1.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**Low project relevance.** Core content is cross-domain LTV regression (D4 label/ZILN family already covered elsewhere). Marginally useful for **Q3** (7-day consumption label, zero-inflated ZILN loss) if bootstrapping retention/revenue models across sparse dating markets. Does not address ranking objectives, item credit assignment, incrementality, or two-sided dynamics (**Q1, Q2, Q5, Q6, Q7, Q8**).

| # | Field | Answer |
|---|-------|--------|
| 1 | Ranking objective | Not specified in source—user-level LTV regression, not ranking. |
| 2 | Credit assignment | User-level 7-day consumption; no item-level mapping. |
| 3 | Labels / horizon | 7-day total consumption; ZILN loss; no delay/censoring treatment. |
| 4 | Short/long fusion | Not specified in source—single LTV head. |
| 5 | Prediction vs incrementality | Predicts consumption outcome; not effect of exposure/treatment. |
| 6 | Offline / online eval | Offline AUC and normalized Gini on G1–G5 target tests only. |
| 7 | Reciprocity / fairness | Not specified in source. |
| 8 | CTR → long-term migration | Not specified in source. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Hongzu Su, Zhekai Du, Jingjing Li, Lei Zhu, Ke Lu
**Affiliations:** UESTC; Shandong Normal University; Tencent internship
**Venue:** AAAI-23
**Year:** 2023
**PDF:** https://ojs.aaai.org/index.php/AAAI/article/view/25583/25355
**Relevance:** Peripheral
**Priority:** 4
