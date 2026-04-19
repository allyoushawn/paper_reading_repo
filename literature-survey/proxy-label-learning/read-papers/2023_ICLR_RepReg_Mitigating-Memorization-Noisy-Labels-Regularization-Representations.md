Date: 2026-04-11
Source: https://arxiv.org/pdf/2110.09022
NLM Source ID: 9e113b4a-64be-482b-a69c-18bdc0823ede
Venue: ICLR 2023
Relevance: Core
Priority: 1

# Mitigating Memorization of Noisy Labels via Regularization between Representations

**Authors:** Hao Cheng, Zhaowei Zhu, Xing Sun, Yang Liu
**Affiliation:** UC Santa Cruz, Tencent YouTu Lab
**Code:** https://github.com/UCSC-REAL/SelfSup_NoisyLabel

## Problem

Robust loss functions (GCE, peer loss, MAE) are theoretically noise-tolerant but in practice still suffer from memorization: test accuracy peaks then drops as training continues because DNNs eventually fit noisy labels despite a robust training objective. Existing analysis of this problem treats architecture capacity as fixed. The key insight: **lower-capacity models generalize better on noisy datasets** — but designing the optimal capacity for an arbitrary task is intractable.

## Method: Representation Regularization (SSL-Guided)

**Core idea:** Instead of redesigning architecture, restrict the function space of a fixed DNN via a self-supervised regularizer that constrains the supervised output space using SSL-derived structure.

**Decoupled architecture:**
```
DNN = encoder f (shared) → linear classifier g (supervised path)
                         → projection head h (SSL path, InfoNCE)
```

**Training loss:**
```
L = ℓ(g(f(x)), ỹ)         # SL: supervised path (CE, GCE, Peer Loss, etc.)
  + ℓ_Info(h(f(x)), B)     # SSL: InfoNCE contrastive objective on batch B
  + λ · ℓ_Reg(h(f(x)), g(f(x)), B)  # Regularizer: distance constraint
```

**Distance constraint (ℓ_Reg):**
```
ℓ_Reg = (1/|B|(|B|-1)) Σ_{n≠n'} ||h(f(xn)) - h(f(xn'))|| · ||g(f(xn)) - g(f(xn'))||_w
```

The regularizer enforces: *instances with similar SSL features (raw-input structure) should have similar supervised outputs, and vice versa.*

**Why this works:** SSL features h(f(x)) are learned from raw inputs independent of noisy labels ỹ. They encode genuine semantic structure. Constraining the supervised outputs to preserve this structure prevents the classifier from memorizing idiosyncratic noisy label patterns — the function space is effectively reduced to label-invariant subspaces.

**Plug-and-play:** ℓ_Reg attaches to any supervised loss. L2 → L1 regularization switch needed at high noise rates.

## Key Results

| Dataset | Method | Best | Last |
|---------|--------|------|------|
| CIFAR-10 Sym-80% | CE | 38.46 | 15.05 |
| CIFAR-10 Sym-80% | CE + Reg | **61.94** | **56.78** |
| CIFAR-10 Sym-80% | Peer Loss | 15.60 | 10.00 |
| CIFAR-10 Sym-80% | Peer Loss + Reg | **61.64** | **53.52** |
| CIFAR-10N Worst | CE + Reg | **88.74** | — |
| CIFAR-100N | CE + Reg | **60.81** | — |
| Clothing1M | CE + DS + Reg | **73.48** | — |

The key metric: **last-epoch accuracy** improves dramatically (from 15% to 57% at Sym-80%) — demonstrating that the regularizer prevents late-stage memorization, not just early-phase accuracy.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2022_ICLR_CIFAR-N_Learning-Noisy-Labels-Revisited-Real-World-Human-Annotations.md](./2022_ICLR_CIFAR-N_Learning-Noisy-Labels-Revisited-Real-World-Human-Annotations.md) | Main note body | ------\|-----------\| \| CE \| 77.69 \| 55.50 \| \| Co-Teaching+ \| 83.26 \| 57.88 \| \| ELR \| 83.58 \| 58.94 \| \| SOP+ \| 94.0 \| — \| \| RepReg (CE+Reg) \| 88.74 \| 60.81 \| |

---
## Relevance to Proxy Label Learning

**Rating: Very High (both practical and theoretically grounded).**

1. **Memorization is the central proxy label problem:** Attribution-derived labels are systematically biased for specific instances. Without regularization, a model trained on proxy labels memorizes these biases late in training. RepReg directly addresses this late-stage memorization mechanism.
2. **SSL structure is attribution-independent:** For recommendation systems, the SSL path can be trained on user interaction sequences (behavioral structure) independently of Shapley-derived labels. The regularizer then prevents the model from memorizing Shapley artifacts that don't correspond to behavioral similarity.
3. **Last-epoch stability:** In production, models are deployed at a specific checkpoint. RepReg's key contribution — maintaining accuracy at the final epoch rather than just at the best epoch — is operationally critical (no need for checkpoint selection).
4. **Theoretical grounding:** The generalization error decomposition (estimation vs. approximation error) provides a principled bound showing why lower-capacity constraint helps. Applicable to proxy label regimes.
5. **Limitation:** The SSL path adds ~30% computational overhead per batch (InfoNCE on full batch B). For large-scale recommendation training, this may require careful batch construction.

## Method Tracker Update

- **RepReg (Representation Regularization)**: Cheng et al., ICLR 2023 | Baseline mentions: 0 (new) | Derived variants: 0 | Component count: 3 | Simplicity: 3 | Performance consistency: 4 | Composite: ~17
