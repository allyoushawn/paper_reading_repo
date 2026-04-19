Date: 2026-04-11
Source: https://proceedings.neurips.cc/paper_files/paper/2023/file/15f4cefb0e143c7ad9d40e879b0a9d0c-Paper-Conference.pdf
NLM Source ID: 66bbda55-bb61-4f53-8120-a1574e99ee13
Venue: NeurIPS 2023
Relevance: Core
Priority: 1

# Active Negative Loss Functions for Learning with Noisy Labels

**Authors:** Xichen Ye, Xiaoqiang Li, Songmin Dai, Tong Liu, Yan Sun, Weiqin Tong
**Affiliation:** Shanghai University

## Problem

The APL (Active Passive Loss) framework uses MAE or its scaled variants (RCE, NMAE, NRCE) as its passive component. The authors prove these are ALL scaled versions of MAE: NMAE = 1/(2(K-1)) × MAE, RCE = -(A/2) × MAE, NRCE = 1/(2(K-1)) × MAE. MAE treats every sample equally — it slows convergence, causes underfitting, and makes training difficult on complex datasets.

## Method: Active Negative Loss (ANL)

**Core building block — Normalized Negative Loss Function (NNLF):**

Three-step construction from any active loss L:
1. **Complementary label focus:** Focus on all classes except the labeled class y
2. **Vertical flipping:** A - L(f(x), k) converts maximization to minimization target (A is a constant, L's maximum)
3. **Normalization:** L_nn(f(x), y) = 1 - (A - L(f(x), y)) / Σ_k (A - L(f(x), k))

**ANL framework:**
```
L_ANL = α * L_norm + β * L_nn
```
where L_norm = normalized active loss, L_nn = corresponding NNLF.

Two specific instantiations:
- **ANL-CE:** α × NCE + β × NNCE
- **ANL-FL:** α × NFL + β × NNFL (Focal Loss variant)

**Theoretical properties:**
- **Symmetry (Theorem 1):** Σ_k L_nn(f(x), k) = K-1 (constant) → NNLF is symmetric
- **Noise tolerance:** Symmetric losses are theoretically tolerant to both symmetric and asymmetric noise
- **Gradient property (Theorems 2-3):** NNLF assigns larger gradients to well-learned samples (high p(y|x)) than MAE, and focuses more on low-uncertainty classes — amplifies clean-sample learning signal while suppressing noisy-sample gradients

**Implementation note:** L2 regularization fails to prevent overfitting for NNLF at high noise rates; L1 regularization works.

## Key Results

| Dataset | Noise | ANL-CE | Best Prior (NCE+AGCE) | Delta |
|---------|-------|--------|----------------------|-------|
| CIFAR-10 | Sym-80% | **61.27%** | 55.62% | +5.65pp |
| WebVision | top-1 | **67.44%** | 65.00% (NCE+AGCE) | +2.44pp |
| Animal-10N | real | **80.72%** | 80.39% (GCE) | +0.33pp |
| Clothing-1M | real | **69.93%** | 69.07% (NCE+RCE) | +0.86pp |

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: High (practical + theoretical).**

1. **Direct theoretical guarantee for asymmetric noise:** ANL's symmetry property guarantees robustness under class-conditional noise (exactly the structure of systematic proxy bias). The proof applies without needing to know the transition matrix.
2. **Better than MAE/RCE for training:** The gradient analysis explains why NNLF outperforms MAE as a passive loss — it continues learning from memorized clean-adjacent samples. For proxy label training where "hard" attribution-ambiguous samples are mislabeled, this matters.
3. **Drop-in replacement for any training pipeline:** Like SCE, ANL is a pure loss function — no architecture changes, no GMM components, no two-network training. This is the simplest intervention for proxy-label robustness.
4. **Tested on proxy-label benchmarks (WebVision, Clothing1M):** Demonstrates generalization beyond synthetic noise to actual proxy-label settings.

**Limitation for continuous labels:** ANL is defined for discrete class labels. Applying to continuous proxy labels (Shapley scores) requires reformulation.

## Method Tracker Update

- **ANL (Active Negative Loss)**: Ye et al., NeurIPS 2023 | Baseline mentions: 0 (new paper) | Derived variants: 0 | Component count: 2 | Simplicity: 5 | Performance consistency: 4 | Composite: ~18
