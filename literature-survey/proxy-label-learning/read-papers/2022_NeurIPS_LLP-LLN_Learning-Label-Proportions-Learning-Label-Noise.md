Date: 2026-04-11
Source: https://arxiv.org/pdf/2203.02496
NLM Source ID: db841313-1246-422e-8c93-225040237ec5
Venue: NeurIPS 2022
Relevance: Core
Priority: 1

# Learning from Label Proportions by Learning with Label Noise

**Authors:** Jianxin Zhang, Yutong Wang, Clayton Scott
**Affiliation:** University of Michigan (EECS)

## Problem

Learning from Label Proportions (LLP) is a weakly supervised problem where training data is grouped into "bags" and only the label proportions per bag are observed, not instance-level labels. Prior multi-class LLP work lacked theoretical grounding. This paper provides a rigorous reduction of LLP to Learning with Label Noise (LLN), enabling strong theoretical guarantees.

## Core Method: Reduction to LLN via Forward Correction

**Reduction mechanism:** Partition NC bags into N groups of C bags each. Assign a uniform "noisy label" Ỹ = i to all instances in the i-th bag of each group. This constructs an LLN problem with noise transition matrix:

```
T(i, j) = γ_i(j) * α(i) / σ(j)
```

where γ_i(j) = label proportion of class j in bag i, α(i) = noisy class prior, σ(j) = clean class prior.

**Forward Correction (FC) loss:** For a strictly proper loss ℓ and transition matrix T:
```
ℓ_T(q, c) = ℓ(T*q, c)
```
Scales the model's predicted distribution q by T before computing loss. Unlike backward correction (which scales loss coefficients — numerically unstable in deep learning), FC scales inputs and behaves better empirically.

## Key Theoretical Results

1. **Uniform calibration:** FC loss is uniformly calibrated w.r.t. the 0-1 loss (Theorem 5). There exists strictly increasing θ such that:
   ```
   excess 0-1 risk on clean P ≤ θ^{-1}(excess FC risk on noisy P_T)
   ```
   Optimizing FC on noisy data is consistent for minimizing clean classification error.

2. **Explicit bound (log loss):** For log loss:
   ```
   excess 0-1 risk ≤ sqrt(2 * ||T^{-1}||_1 * excess FC risk)
   ```
   where ||T^{-1}||_1 quantifies overall noise severity. More noise → larger constant → looser bound.

3. **Generalization bound:** Rademacher complexity bound for empirical FC risk over multiple transition matrices (Theorem 7 + Proposition 8). Enables consistency proofs for the full LLPFC algorithm.

**Assumption required:** Label proportions {γ_1, ..., γ_C} must be linearly independent and σ must lie in their convex hull. This guarantees T is column-stochastic and invertible.

## Empirical Performance

Outperforms competing LLP methods (ProPortioN, DLLP, Mixbag) by substantial margins across CIFAR-10, CIFAR-100, and STL-10 with various bag sizes.

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: High (theoretical).** This is one of the few papers providing a direct calibration-theoretic justification for why training on systematically biased labels can still learn the correct classifier. Key connections:

1. **Proxy labels as bag proportions:** In the attribution-derived proxy label setting, a Shapley score can be viewed as a "proportion" — it encodes how much credit each feature/interaction is assigned. The LLP→LLN reduction provides a principled bridge: if proxy labels are linear functions of true labels (as bag proportions are of instance labels), then the FC loss with estimated transition matrix recovers Bayes optimality.

2. **Theoretical guarantee for systematic bias:** The excess risk bound (Theorem 5) is the kind of result most needed for proxy-label practice: it quantifies the cost of training on biased labels in terms of ||T^{-1}||_1. Knowing the attribution model's bias structure allows bounding the generalization gap.

3. **Forward vs backward correction practical guidance:** The authors show forward correction empirically superior for deep learning — directly applicable advice for any proxy-label training pipeline.

**Limitation:** The reduction requires estimating T, which in the attribution-proxy setting requires knowledge of how the attribution model systematically deviates from ground-truth labels — harder to obtain than in the LLP bag-proportion case.

## Method Tracker Update

- **LLPFC (Forward Correction for LLP)**: Zhang, Wang, Scott 2022 | Key theoretical: uniform calibration + excess risk bound via ||T^{-1}||_1 | Component count: 2 | Simplicity: 4 | Primarily theoretical | Composite: ~15
