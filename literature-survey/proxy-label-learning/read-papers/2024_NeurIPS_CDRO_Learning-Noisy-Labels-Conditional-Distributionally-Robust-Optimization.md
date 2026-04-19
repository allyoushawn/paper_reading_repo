Date: 2026-04-11
Source: https://arxiv.org/pdf/2411.17113
NLM Source ID: f6948d59-7d77-443d-9324-238bf6b1222f
Venue: NeurIPS 2024
Relevance: Core
Priority: 1

# Learning from Noisy Labels via Conditional Distributionally Robust Optimization

**Authors:** Hui Guo, Grace Y. Yi, Boyu Wang
**Affiliation:** University of Western Ontario

## Problem

Standard approaches to noisy crowdsourced labels estimate the true label posterior P(y|x, ỹ) via Bayes' theorem (using estimated noise transition probabilities), then use this as a weight or as a pseudo-label. The problem: potential misspecifications in the estimated posterior propagate uncorrected, especially in high-noise scenarios. Existing DRO requires clean true labels to construct the reference distribution — unavailable here.

## Method: Conditional Distributionally Robust Optimization (CDRO) — AdaptCDRP

**Core formulation:** Minimize the worst-case risk over a Wasserstein ambiguity ball around the reference posterior:

```
min_{ψ} E_{x,ỹ} [ sup_{Q_{y|x,ỹ} ∈ Γ_ε(P_{y|x,ỹ})} E_{Q_{y|x,ỹ}} {ℓ(ψ(X), Y)} ]
```

Where Γ_ε is the Wasserstein ball of radius ε around the estimated posterior P_{y|x,ỹ}.

**Strong duality → dual form:** Transforms nested min-max to a relaxed dual problem. Enables closed-form solutions:

- **Binary case (Theorem 3.1):** Optimal action is a likelihood ratio test — assign label j if P_j(x,ỹ) exceeds threshold ϱ(ε) + ϖ; assign 1/2 (no label) otherwise.
- **Multi-class case (Theorem 3.2):** Extends via pairwise comparisons — pseudo-label y* = k* only if P_{k*}/max_{j≠k*} P_j ≥ C_1 (confidence threshold derived from ε).

This likelihood ratio test naturally constructs a **pseudo-empirical distribution** (only high-confidence pseudo-labels included) which then serves as the robust reference in CDRO.

**Closed-form robust risk (Theorem 3.3):**
```
R̂_ε = R̂ + (1/n) Σ_{t=1}^{s*-1} P(t) * α(t) * 1(s* > 1)
```
The robust risk = nominal risk + penalty term that **prevents classifier from becoming overconfident** on uncertain data points. The penalty is adaptive via optimal Lagrange multiplier γ* = α(s*)/κ^p.

**Algorithm (AdaptCDRP):** Two parallel classifiers (co-training style); each uses the other as prior for posterior estimation. Adaptive γ updated each epoch.

## Key Theoretical Guarantees

1. **Generalization bound (Theorem 2.2):** |R_ε(ψ; P) - R̂_ε(ψ; P)| ≤ O(n^{-1/2}) — empirical robust risk converges to population robust risk
2. **Excess risk bound (Corollary 2.3):** Empirical robust minimizer ψ̂ satisfies excess risk bound proportional to O(n^{-1/2})
3. **Penalty term interpretation:** Wasserstein robust loss = nominal loss + confidence penalty. Principled way to regularize against systematic over-confidence on proxy-labeled samples.

## Key Results

| Dataset | AdaptCDRP | Best Baseline (CoDis) | Delta |
|---------|-----------|----------------------|-------|
| CIFAR-10N (real) | **88.25%** | CoDis 87.23% | +1.02pp |
| CIFAR-100N (real) | **53.42%** | CoDis 52.66% | +0.76pp |
| Animal-10N (real) | **83.08%** | TraceReg 80.34% | +2.74pp |
| CIFAR-100 IDN-High | **54.24%** | CoDis 46.12% | +8.12pp |

Especially strong on **instance-dependent noise (IDN)** — exactly the structured proxy noise regime.

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: Very High (theoretical foundation for proxy-label training).**

1. **Direct model for proxy label uncertainty:** The CDRO framework treats estimated noise transition probabilities (P(ỹ|y,x)) as potentially misspecified — exactly the assumption one should make about attribution-derived proxy labels (Shapley model makes assumptions; errors are not random).
2. **IDN focus:** Proxy labels from attribution models are instance-dependent by design. AdaptCDRP's strongest results are on IDN datasets — directly applicable.
3. **Confidence penalty = anti-hallucination for proxy labels:** The Wasserstein penalty (Theorem 3.3) prevents the model from memorizing highly confident but systematically wrong proxy assignments. This is the operationalization of "don't blindly trust the proxy" at the optimization level.
4. **Theoretical excess risk bound for noisy posterior:** Provides the kind of guarantee needed in practice — if the transition probability estimate is off by δ, the resulting classifier's excess risk is bounded.
5. **Crowdsourced label framing applies to proxy labels:** Multiple attribution model runs with different seeds = multiple noisy annotators. The CDRO framework handles sparse annotations (1 annotation per instance from R annotators) — matches single-run Shapley attribution scenario.

**Limitation:** The framework assumes the noise transition probabilities can be estimated (via e.g. Dawid-Skene or similar). For Shapley-derived labels, estimating the transition structure requires domain knowledge about the attribution model's systematic biases.

## Method Tracker Update

- **AdaptCDRP (Conditional DRO)**: Guo, Yi, Wang NeurIPS 2024 | Baseline mentions: 0 (new) | Derived variants: 0 | Component count: 3 | Simplicity: 3 | Performance consistency: 4 | Composite: ~15
