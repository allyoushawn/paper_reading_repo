Date: 2026-04-11
Source: https://proceedings.iclr.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf
NLM Source ID: 29c63b60-f564-4105-b459-7bf2d665264a
Venue: ICLR 2024
Relevance: Core
Priority: 1

# Robust Classification via Regression for Learning with Noisy Labels

**Authors:** (ICLR 2024 proceedings)

## Problem

Standard cross-entropy training for classification operates on probability simplex outputs — this creates a sharp asymmetry: the loss landscape is highly sensitive to label flips near the decision boundary. The label flipping structure of noisy labels (systematic class confusion) is not naturally represented in CE's probability space. Can we reformulate classification as regression in a geometry where noisy label transitions become simple additive Gaussian noise — enabling standard robust regression tools?

## Method: SGN (Shifted Gaussian Noise)

**Core transform — Isometric Log-Ratio (ilr):**

Map class probabilities from the probability simplex Δ^{K-1} to unconstrained Euclidean space R^{K-1} via the ilr transform:

```
t = ilr(y_onehot) ∈ R^{K-1}
```

The ilr transform is an isometry: preserves distances, makes the simplex a flat Euclidean space. In this space, label flips from asymmetric noise become approximately additive perturbations.

**Shifted Gaussian Noise model:**

In the ilr space, the observed noisy label target t̃ follows:
```
t̃ = μ + ε,    ε ~ N(Δ, Σ)
```

Where:
- **μ**: true class center (EMA of model predictions in ilr space)
- **Δ = t̃ - μ_EMA**: shift vector — empirical noise bias; used for **label correction** (subtract Δ from observed targets before computing loss)
- **Σ**: noise covariance — used for **loss reweighting** (upweight low-variance, high-confidence samples via Mahalanobis distance)

**SGN training procedure:**
1. Maintain EMA of predictions μ_EMA in ilr space
2. Compute Δ (bias correction) and Σ (variance estimate) per mini-batch
3. Corrected loss: regress model output toward t̃ - Δ with weights ∝ 1/Σ_ii
4. Convert back to probability simplex for final classification

**Why regression in ilr space is better than CE:**
- Label correction via Δ subtraction directly removes systematic noise bias (impossible in CE's probability space without knowing T)
- Mahalanobis reweighting naturally downweights uncertain/noisy samples without explicit sample selection
- No need to estimate the full transition matrix T explicitly

## Key Results

| Dataset | SGN | Best Prior | Delta |
|---------|-----|-----------|-------|
| CIFAR-100 Asym-40% | **71.01%** | NAL 58.01% | +13pp |
| CIFAR-100N Worst | **60.36%** | SOP+ ~58% | +2.36pp |
| Clothing1M | **73.9%** | ELR+ 73.8% | +0.1pp |
| WebVision top-1 | **77.2%** | ELR+ 77.78% | competitive |

The CIFAR-100 Asym-40% result (+13pp) is remarkable — asymmetric noise is exactly the structure for which ilr+Δ correction is most effective (the shift Δ encodes the class confusion pattern).

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: Very High (direct bridge to continuous proxy label regression).**

1. **ilr transform connects classification and regression:** Proxy labels from attribution models (Shapley values) are continuous — training with them is inherently regression, not classification. SGN's ilr framework provides the theoretical bridge: classification with noisy discrete labels is isomorphic to regression with additive noise in ilr space.
2. **Δ correction = attribution bias correction:** The shift vector Δ in SGN directly models systematic bias in proxy labels. For Shapley attribution, this bias corresponds to consistent under/over-estimation of specific feature importances. SGN's EMA-based Δ estimation adapts this correction automatically without domain knowledge.
3. **Mahalanobis reweighting = confidence-aware proxy training:** Σ captures which samples have high-variance proxy labels (attribution instability) and downweights them. This is exactly the right inductive bias for recommendation proxy labels where interaction-heavy users have more stable attributions.
4. **Strongest on asymmetric noise — matches proxy label structure:** Attribution-derived labels have strong class asymmetry (specific features are systematically over/undervalued). SGN's +13pp on CIFAR-100 Asym-40% demonstrates its advantage precisely in this regime.
5. **Direct adaptation to continuous case:** For continuous Shapley targets, SGN simplifies — the ilr transform is not needed (already in Euclidean space), and Δ/Σ correction applies directly to the regression MSE/MAE loss.

## Method Tracker Update

- **SGN (Shifted Gaussian Noise)**: ICLR 2024 | Baseline mentions: 0 (new) | Derived variants: 0 | Component count: 3 | Simplicity: 4 | Performance consistency: 4 | Composite: ~20
