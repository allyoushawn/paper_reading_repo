Date: 2026-04-11
Source: https://arxiv.org/pdf/2312.06221
NLM Source ID: 29515897-086c-45f7-af18-5618a5c2e763
Venue: NeurIPS 2023
Relevance: Core
Priority: 1

# CSOT: Curriculum and Structure-Aware Optimal Transport for Learning with Noisy Labels

**Authors:** Wanxing Chang, Ye Shi, Jingya Wang
**Affiliation:** ShanghaiTech University

## Problem

Existing noisy-label methods evaluate each sample independently when doing sample selection or pseudo-labeling, ignoring the global and local structure of the feature distribution. Standard OT-based pseudo-labeling handles global (inter-distribution) matching but ignores intra-distribution coherence — leading to mismatching nearby samples to far-away class centroids when the decision boundary is vague.

## Method: Curriculum and Structure-Aware Optimal Transport (CSOT)

**Two innovations stacked:**

### 1. Structure-Aware OT (SOT)
Adds two local coherence regularization terms to the standard OT objective:

```
min_Q ⟨−log P, Q⟩ + κ(Ω_P(Q) + Ω_L(Q))
  s.t. Q ∈ Π(1/B * 1_B, 1/C * 1_C)
```

- **Ω_P (prediction-level consistency):** Encourages samples with high cosine similarity in feature space (high S_ij) to receive the same prediction weights Q_ik, Q_jk
- **Ω_L (label-level consistency):** Same but uses original noisy label matrix L — enforces neighborhood majority consistency

Result: Samples near the decision boundary get their assignments rectified by neighborhood voting instead of local model uncertainty.

### 2. Curriculum component (CSOT)
Relaxes the sample-side marginal constraint from equality to inequality:

```
s.t. Q ≥ 0, Q * 1_C ≤ 1/B * 1_B, Q^T * 1_B = m/C * 1_C
```

Budget factor m ∈ [0,1] controls the fraction of samples that get pseudo-labels:
- m = 0.3 at start (top 30% confident samples labeled)
- Linearly increases to m = 1.0 as training progresses
- Unselected samples (low confidence) are used via self-supervised learning in Stage 1

**Solver:** Generalized conditional gradient framework with scaling iteration (non-convex objective — classical OT solvers don't apply).

**Training:** Two-stage:
1. Stage 1: Progressively select confident samples → label them; self-supervise the rest
2. Stage 2: Semi-supervised training on all denoised labels

## Key Results

| Dataset | Noise | CSOT | Best Baseline | Delta |
|---------|-------|------|--------------|-------|
| CIFAR-100 | Sym-90% | **50.5%** | UNICON 44.8% | +5.7pp |
| CIFAR-100 | Sym-80% | **67.8%** | UNICON 63.9% | +3.9pp |
| CIFAR-10 | Sym-80% | **94.4%** | NCE 93.9% | +0.5pp |
| WebVision | top-1 | **79.67%** | NCE 79.50% | +0.17pp |
| Clothing1M | — | **75.16%** | RRL 74.84% | +0.32pp |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2020_ICLR_DivideMix_Learning-Noisy-Labels-Semi-supervised.md](./2020_ICLR_DivideMix_Learning-Noisy-Labels-Semi-supervised.md) | Novelty vs. Prior Work | . Verification: DivideMix is the dominant SOTA on CIFAR and WebVision benchmarks as of 2020–2022. Many subsequent papers (ELR, CSOT, Active Negative Loss) use it as the primary baseline. Confirmed novel contribution. --- |

---
## Relevance to Proxy Label Learning

**Rating: Moderate-High.**

1. **WebVision and Clothing1M are proxy-label benchmarks** — web-crawled tags and shopping text labels. CSOT's SOTA on these validates it for proxy-label regimes.
2. **Structure-aware selection is directly applicable to systematic noise:** Proxy labels may be systematically wrong for boundary-region samples (same problem that motivated structure-awareness). Local coherence regularization could detect when attribution-derived labels violate natural feature clustering.
3. **Curriculum pacing prevents early memorization of systematic errors** — relevant for cases where proxy noise is concentrated in high-difficulty samples.

**Limitation:** CSOT is complex (3 main components + custom solver). The OT framework assumes class-balanced data; real recommendation-system proxy labels may be highly imbalanced.

## Method Tracker Update

- **CSOT**: Chang, Shi, Wang NeurIPS 2023 | Baseline mentions: 0 | Derived variants: 0 | Component count: 4 | Simplicity: 2 | Performance consistency: 4 | Composite: ~14
