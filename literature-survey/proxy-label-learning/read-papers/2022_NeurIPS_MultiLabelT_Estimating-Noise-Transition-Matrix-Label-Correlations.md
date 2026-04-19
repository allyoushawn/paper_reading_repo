Date: 2026-04-11
Source: https://papers.neurips.cc/paper_files/paper/2022/file/98f8c89ae042c512e6c87e0e0c2a0f98-Paper-Conference.pdf
NLM Source ID: ff498f95-5695-42c6-a8ac-2f682024367d
Venue: NeurIPS 2022
Relevance: Core
Priority: 1

# Estimating Noise Transition Matrix with Label Correlations for Noisy Multi-Label Learning

**Authors:** Shikun Li, Xiaobo Xia, Hansong Zhang, Yibing Zhan, Shiming Ge, Tongliang Liu
**Affiliation:** Chinese Academy of Sciences; University of Sydney; JD Explore Academy

## Problem

Transition matrix estimation for multi-label noise is unsolved. Existing multi-class estimators rely on (1) anchor points (training examples definitively belonging to one class) and (2) accurate posterior fitting — both are impossible in multi-label settings due to severe positive-negative class imbalance and the difficulty of verifying anchor point membership.

## Method

The key insight is to exploit **mismatch of label correlations** as a signal to identify the transition matrix without anchor points or accurate posterior fitting.

**Algorithm:**
1. **Sample selection** (Stage 1): Train classifier for a few epochs; use GMM on per-sample losses to select a "likely clean" subset D_s for each class. (Leverages the memorization effect — DNN learns clean samples first.)
2. **Co-occurrence estimation** (Stage 2): Estimate two frequencies:
   - P(Ȳ_i, Ȳ_j) = co-occurrence of two *noisy* labels in full noisy dataset D
   - P(Ȳ_i | Y_j) = occurrence of noisy label given a *clean* label in selected subset D_s
3. **Bilinear decomposition**: The mismatch between these probabilities yields 4 equations in the transition matrix T_j; solved as Ê(M̂)^{-1} = (T̂_j)^T P̂ — a simple closed-form bilinear decomposition.

**Identifiability theorem:** Two noisy labels alone cannot identify T_j (Theorem 1); but adding the clean-subset estimate makes it identifiable (Theorem 4).

## Key Results

| Dataset | Noise Rate | Metric | Reweight-Ours | Reweight-DualT | Reweight-T | Standard |
|---------|-----------|--------|--------------|----------------|------------|---------|
| MS-COCO | (0.6, 0) | CF1 | **58.63** | 54.62 | 56.68 | 7.07 |
| MS-COCO | (0.0, 0.6) | CF1 | **57.46** | 52.16 | 32.78 | 22.73 |
| Pascal-VOC2007 | (0.6, 0) | est err | **1.34** | 2.68 | 2.13 | — |

Estimator error consistently lowest or second-lowest across all noise rates; robust without hyperparameter tuning per noise rate (unlike T-estimator and Dual T-estimator).

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: Moderate-High.** 

The core relevance is methodological: attribution-derived proxy labels (Shapley scores per interaction) in a multi-interaction recommendation context are structurally analogous to multi-label problems where each "label" corresponds to a feature or interaction type. The approach of exploiting label correlations to identify systematic noise transitions is applicable when:
- The proxy labeling process introduces systematic confusions between feature categories
- Multiple proxy labels per instance are available and their natural co-occurrence structure is known

The "mismatch of label correlations" framing directly translates to systematic bias detection: if proxy labels systematically over-weight one feature type at the expense of a correlated one (as Shapley values do when features are correlated), the correlation mismatch reveals the noise structure.

**Limitation:** Method assumes binary per-class labels (0/1 noise transitions). Continuous-valued Shapley proxy labels require extension to real-valued transition models.

## Method Tracker Update

- **Multi-Label Transition Matrix Estimator**: Li et al., NeurIPS 2022 | Baseline mentions: 0 | Derived variants: 0 | Component count: 3 | Simplicity: 3 | Performance consistency: 3 | Composite: ~12
