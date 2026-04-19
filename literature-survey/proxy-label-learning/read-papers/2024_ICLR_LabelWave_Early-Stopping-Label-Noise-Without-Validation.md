Date: 2026-04-11
Source: https://arxiv.org/pdf/2502.07551
NLM Source ID: 9d82b9ec-b110-427d-9f86-1aa8ddbe8591
Venue: ICLR 2024
Relevance: High
Priority: 1

# Early Stopping Against Label Noise Without Validation Data

**Authors:** (ICLR 2024 proceedings)

## Problem

Early stopping is the simplest intervention against memorization of noisy labels: stop training before the network begins fitting the noisy samples. The obstacle: selecting the stopping epoch typically requires a clean validation set, which is unavailable in noisy label settings. Existing methods (ELR, DivideMix) embed noise robustness into training but don't address stopping time explicitly. Oracle early stopping (using clean test accuracy) is consistently better than these methods' best checkpoints — suggesting stopping time is more important than loss design.

## Method: Label Wave — Prediction Change (PC) Metric

**Core observable — Prediction Changes (PC):**

```
PC(t) = (1/n) Σ_{i=1}^{n} 1[ŷ_i^t ≠ ŷ_i^{t-1}]
```

The fraction of training samples whose predicted class changes between consecutive epochs t-1 and t.

**Empirical finding:** PC follows a characteristic "wave" pattern during noisy label training:
1. **Early phase (clean learning):** PC rises then falls as network stabilizes on clean patterns
2. **Transition phase:** PC has a local minimum — the model has memorized clean samples but hasn't yet started memorizing noisy ones
3. **Memorization phase:** PC rises again as the network begins fitting noisy labels (predictions become unstable)

**Stopping rule:**
```
Stop at t* = argmin_{t in window} MA_k(PC(t))
```
Where MA_k is a k-epoch moving average (smoothing over training noise). The first local minimum of the smoothed PC curve is the stopping time.

**No validation data required:** PC is computed entirely on training data predictions (only requires forward passes, no labels beyond what's already in training).

**Compatibility:** Label Wave is a wrapper — applies on top of any base training method (CE, ELR, DivideMix, etc.).

## Key Results

| Dataset / Method | Label Wave | Without Label Wave | Oracle ES |
|-----------------|------------|-------------------|-----------|
| CIFAR-10 Sym-40% (CE) | **80.15%** | 73.0% | 80.45% |
| CIFAR-10 Sym-40% (ELR) | **90.45%** | 87.2% | 90.6% |
| CIFAR-100 Sym-40% (CE) | **52.3%** | 44.1% | 52.7% |
| CIFAR-100 Sym-80% (CE) | **35.2%** | 21.8% | 35.8% |

Label Wave closes ~95%+ of the gap between no-stopping and oracle early stopping across all tested settings.

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: High (practical + orthogonal to other methods).**

1. **Proxy labels create predictable memorization waves:** Attribution-derived labels have systematic bias (not random). The network first learns the genuine correlation between features and proxy labels, then begins memorizing idiosyncratic attribution artifacts. Label Wave's PC metric detects this transition without requiring knowledge of the noise structure.
2. **No validation set requirement is critical for proxy settings:** In production recommendation, held-out ground truth (actual user retention) is expensive and delayed. Label Wave enables principled early stopping using only the attribution-labeled training data.
3. **Orthogonal combination:** Label Wave improves ELR by +3.25pp in the CIFAR-10 experiment — demonstrating that it provides signal beyond what ELR's temporal ensembling already captures. Can be combined with any method.
4. **Moving average window k as sole hyperparameter:** Minimal configuration; k ≈ 5–10 works across settings according to ablation.
5. **Limitation for proxy labels:** The PC metric assumes discrete class predictions. For continuous proxy label regression (Shapley scores as real values), the analog would be tracking prediction variance or prediction distance between epochs — not directly PC. Requires adaptation.

## Method Tracker Update

- **Label Wave (Early Stopping)**: ICLR 2024 | Baseline mentions: 0 (new technique) | Derived variants: 0 | Component count: 1 | Simplicity: 5 | Performance consistency: 4 | Composite: ~17
