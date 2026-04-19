Date: 2026-04-11
Source: https://proceedings.neurips.cc/paper_files/paper/2024/file/b05e6a11df6eacb600074a42bb28ae52-Paper-Conference.pdf
NLM Source ID: b7197331-bfbc-4d2d-bfbc-6ad11556c49f
Venue: NeurIPS 2024 Spotlight
Relevance: Core
Priority: 1

# Noisy Label Learning with Instance-Dependent Outliers: Identifiability via Crowd Wisdom

**Authors:** Kaining Ying, Yibing Zhan, Lichuan Gu, Dapeng Oliver Wu
**Affiliation:** Multiple institutions

## Problem

Existing instance-dependent noise (IDN) methods assume all annotators exhibit correlated noise patterns (each annotator's noise transition T(x) is smooth and feature-dependent). However, real crowdsourced labels often include **outlier annotators** — individuals whose labeling behavior is idiosyncratic or adversarial, producing transitions that are neither correlated with instance features nor with other annotators. These outliers degrade IDN estimators that rely on consistency across annotators.

## Method: COINNet (Crowd Outlier Instance-dependent Noise Network)

**Key decomposition (Theorem 1 — Identifiability):**

```
T(xn) = A + E(xn)
```

Where:
- **A**: shared noise transition matrix (common crowd behavior) — dense, full-rank
- **E(xn)**: instance-dependent outlier deviation — sparse, structured

**Crowd wisdom enables identifiability:** With R annotators, outlier deviations E(xn) become geometrically separable from consensus noise A because outlier columns in the aggregate transition matrix are column-sparse (few annotators deviate for any given instance). This gives an identifiability guarantee absent from single-annotator IDN settings.

**One-stage optimization (joint loss):**

```
L = L_CCE(ψ; A, E) + λ_1 · ||E||_{2,p} + λ_2 · log det(A)
```

- **L_CCE**: Corrected cross-entropy using decomposed T = A + E
- **||E||_{2,p}** (ℓ_{2,p} column-sparsity regularizer, p < 1): enforces that outlier deviations are sparse across annotators — only a few columns of E are non-zero
- **log det(A)** (min-volume regularizer): prevents A from collapsing to identity (degenerate solution); ensures A captures meaningful shared noise structure

**Differentiable end-to-end training:** Both A and E(xn) are learned jointly with the classifier ψ, no alternating optimization required.

## Key Theoretical Guarantees

1. **Identifiability (Theorem 1):** Under column-sparsity of E and full-rank A, the decomposition T(xn) = A + E(xn) is identifiable from crowdsourced data without requiring instance-level independence assumptions.
2. **Convergence:** The ℓ_{2,p} regularizer (p < 1) induces sparsity more aggressively than ℓ_1, enabling recovery of outlier annotators even when their proportion is non-negligible.

## Key Results

| Dataset | COINNet | Best Baseline (Max-MIG) | Delta |
|---------|---------|------------------------|-------|
| CIFAR-10N (real) | **92.09%** | Max-MIG 90.11% | +1.98pp |
| ImageNet-15N | **93.71%** | Max-MIG 81.13% | +12.58pp |
| CIFAR-100N (real) | **65.22%** | CoDis 64.77% | +0.45pp |

The ImageNet-15N result (+12.58pp) is especially striking — suggests outlier annotators are prevalent in real large-scale crowdsourcing and existing methods fail to model them.

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: High (crowdsourced proxy label analogy).**

1. **Multiple attribution runs as multiple annotators:** Running Shapley attribution with different random seeds, subsets, or model checkpoints produces multiple "annotator" views. Some runs may be outlier-like (high variance, seed-dependent instability). COINNet's framework directly applies — model the consistent component A and the run-specific outlier component E(x).
2. **Sparse outlier model matches attribution instability:** Shapley attribution instability is known to be concentrated on specific instances (near decision boundaries, high-variance feature interactions) — exactly the column-sparsity structure COINNet exploits.
3. **Identifiability is the hard problem for proxy labels:** The question "when can we recover true feature importance from noisy attributions?" is precisely the identifiability question COINNet answers for the crowdsourced case. The Theorem 1 conditions (column-sparse deviations + full-rank consensus) suggest practical conditions under which proxy label training converges.
4. **Limitation:** Requires multiple annotators/runs per instance (R ≥ 3 for the geometric separability argument). Single-run Shapley attribution doesn't directly fit — would need ensemble attribution or multiple model checkpoints.

## Method Tracker Update

- **COINNet**: Ying et al., NeurIPS 2024 Spotlight | Baseline mentions: 0 (new) | Derived variants: 0 | Component count: 3 | Simplicity: 3 | Performance consistency: 4 | Composite: ~15
