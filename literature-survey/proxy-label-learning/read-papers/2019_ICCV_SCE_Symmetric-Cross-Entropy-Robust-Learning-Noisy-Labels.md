Date: 2026-04-11
Source: https://arxiv.org/pdf/1908.06112
NLM Source ID: 9c487e78-69e5-48ab-bfa0-f769f6582fc4
Venue: ICCV 2019
Relevance: Core
Priority: 2

# Symmetric Cross Entropy for Robust Learning with Noisy Labels

**Authors:** Yisen Wang, Xingjun Ma, Zaiyi Chen, Yuan Luo, Jinfeng Yi, James Bailey
**Affiliation:** University of Melbourne; Tencent AI Lab

## Problem

Standard Cross Entropy (CE) suffers from two failure modes under label noise: (1) overfitting on noisy labels for "easy" classes, and (2) severe **under-learning** on "hard" classes whose features are similar to other classes. CE fails to produce confident predictions for hard classes even when most of their labels are clean. This diagnosis — that *under-learning*, not just over-fitting, limits noisy-label performance — is the key novel observation.

## Method: Symmetric Cross Entropy (SCE) Loss

Inspired by symmetric KL-divergence, SCE combines CE with a novel **Reverse Cross Entropy (RCE)** term:

```
L_SL = α * L_CE + β * L_RCE
```

- **CE** = H(q, p): standard cross entropy using noisy labels q to evaluate predictions p
- **RCE** = H(p, q): reverse cross entropy — swaps prediction and label roles

The α/β hyperparameters decouple the CE overfitting mitigation from RCE's robustness benefit. RCE introduces an adaptive gradient acceleration: for hard (low-confidence) samples, it accelerates learning; for noisy high-confidence samples, it suppresses residual probability mass on wrong classes.

**Theoretical basis:** Theorem 1 proves RCE is strictly noise-tolerant under:
- Symmetric (uniform) noise: rate η < (K-1)/K
- Asymmetric (class-dependent) noise: if R(f*) = 0 and noise is diagonal-dominated in the transition matrix

Because SCE is purely a loss modification, it can be appended to any existing method (Forward, LSR, etc.) to boost performance.

## Key Experiments

| Dataset | Noise Type | Noise Rate | SCE Acc | Best Baseline | Delta |
|---------|-----------|-----------|---------|--------------|-------|
| CIFAR-100 | Sym | 80% | 15.00% | GCE: 8.43% | +6.57pp |
| CIFAR-10 | Sym | 80% | 53.81% | GCE: 40.81% | +13pp |
| Clothing1M | Real | ~38% | **71.02%** | Forward: 69.84% | +1.18pp |
| MNIST | Sym | 80% | 65.02% | D2L: 48.57% | +16.45pp |

Clothing1M uses proxy labels generated from surrounding text of online shopping images — directly analogous to systematic proxy label noise (asymmetric confusion between similar classes like Knitwear vs. Sweater).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2021_NeurIPS_GJS_Generalized-Jensen-Shannon-Divergence-Loss.md](./2021_NeurIPS_GJS_Generalized-Jensen-Shannon-Divergence-Loss.md) | Novelty vs. Prior Work | 2017 (MAE robustness theory): theoretical foundation used directly. Zhang & Sabuncu 2018 (GCE): GJS shown to outperform on most settings. Wang et al. 2019 (SCE): different interpolation mechanism, not bounded. Ma et al. 2020 (NCE+RCE): normalization vs. divergence approach. Concurrent: Wei & Liu ... |
| [2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md](./2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md) | Summary | Three applications include booster for **GCE/SCE/ELR**; reports **GCE+FINE** gains on CIFAR-100 sym-80% vs GCE alone. |
| [2022_ICML_NLS_To-Smooth-or-Not-Label-Smoothing-Noisy.md](./2022_ICML_NLS_To-Smooth-or-Not-Label-Smoothing-Noisy.md) | Experiment Critique | Extensive evaluation compares against **Bootstrap, FLC, BLC, SCE, APL, Peer Loss, ELR, AUM**, F-div baselines across synthetic, CIFAR-N, Clothing-1M, and tabular sets. |
| [2023_NeurIPS_ANL_Active-Negative-Loss-Noisy-Labels.md](./2023_NeurIPS_ANL_Active-Negative-Loss-Noisy-Labels.md) | Relevance to Proxy Label Learning | Positions ANL as a drop-in like **SCE**—pure loss, no architecture changes, no GMM or two-network training. |

---
## Relevance to Proxy Label Learning

**Rating: High.** Several dimensions of relevance:

1. **Asymmetric noise model matches proxy label structure:** The paper explicitly targets class-dependent noise (systematic confusions between semantically similar classes), which is the structure expected from attribution-derived or model-generated proxy labels.
2. **Theoretical noise tolerance under systematic bias:** RCE's tolerance proof holds for asymmetric noise if the transition matrix is diagonal-dominated — a reasonable assumption for well-calibrated proxy labelers.
3. **Clothing1M as proxy-label benchmark:** The authors use a real-world proxy-label dataset (text-derived image labels) as primary real benchmark — validating applicability to the proxy-label regime.
4. **Drop-in compatibility:** SCE can augment any existing training pipeline; useful as a practical robustness layer when training on Shapley-score proxy labels.

**Limitation for continuous labels:** SCE is formulated for discrete class labels. Continuous/soft proxy labels would require adaptation (e.g., treating proxy label as a soft distribution and applying the symmetric-KL idea directly).

## Method Tracker Update

- **SCE / SL loss**: Wang et al., ICCV 2019 | Baseline mention count: 2 (cited in NLS, LogitClip as robustness baseline) | Derived variants: 1 (SL+Forward, SL+LSR) | Component count: 2 | Simplicity: 5 | Performance consistency: 4 | Composite: ~21
