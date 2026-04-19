Date: 2026-04-11
Source: https://arxiv.org/pdf/1605.07723
NLM Source ID: bd371e3f-9aa5-4605-b574-127660fef25f
Venue: NeurIPS 2016
Relevance: Core
Priority: 1

# Data Programming: Creating Large Training Sets, Quickly

**Authors:** Alexander Ratner, Christopher De Sa, Sen Wu, Daniel Selsam, Christopher Ré
**Affiliation:** Stanford University

## Problem

Hand-labeling large training sets is the primary bottleneck in deploying ML systems. For domain-specific tasks (NLP, genomics, pharmacogenomics), labeled data is expensive, requires expert annotators, and must be re-created when task requirements change. The goal: enable domain experts to supervise ML models via programmatic heuristics ("labeling functions") rather than individual labels — and recover the quality of supervised learning without requiring ground-truth labels.

## Method: Data Programming

**Core abstraction — Labeling Functions (LFs):**
```python
def LF_causes(x):
    if "causes" in x.text: return POSITIVE
    return ABSTAIN  # can abstain (output ∅)
```

LFs are user-written programs that: (1) label a subset of data points, (2) may conflict with each other, (3) have unknown accuracy and correlation structure.

**Generative model over LFs:**

The system models the joint distribution P(Λ, Y) where Λ is the m×n matrix of LF outputs (m data points, n LFs) and Y is the latent true label:

```
P(Λ, Y; α) = (1/Z) exp(Σ_k α_k · φ_k(Λ, Y))
```

Where φ_k are factor functions encoding:
- LF accuracy: P(λ_i = Y)
- LF correlations: P(λ_i = λ_j)
- LF fixing/reinforcing dependencies (user-specified DAG)

**Parameter recovery (key theorem):** With |S| ≥ O(ε^{-2}) unlabeled examples and m = O(1) LFs, the generative model recovers parameters with expected error bounded by ε — achieving the **same asymptotic scaling as supervised learning** without any ground-truth labels.

**Noise-aware discriminative training:**
```
min_w (1/|S|) Σ_x E_{(Λ,Y)~μ_{α̂,β̂}} [ℓ(w·f(x), Y)]
```
Replace hard label y_i with probabilistic soft label from the generative model — denoises training set for downstream discriminative model.

**Dependency types (user-specifiable):**
- Similar: two LFs label the same instances in the same direction
- Fixing: LF_2 corrects errors of LF_1 when they conflict
- Reinforcing: LF_2 agrees with LF_1 on a subset
- Exclusive: LF_1 and LF_2 never label the same instance the same way

## Key Results

| Task | Improvement over ITR (if-then-return) baseline |
|------|------------------------------------------------|
| TAC-KBP (News) | +competition-winning F1 |
| TAC-KBP LSTM | +5.98 F1 over LSTM baseline |
| Average (3 tasks) | +2.34 F1 over distant supervision |

User study: non-ML bioinformatics experts built a disease-tagging system within 8 hours that scored within 10 F1 of a supervised baseline.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2017_ICML_MarginalPseudolikelihood_Structure-Generative-Models-Without-Labeled-Data.md](./2017_ICML_MarginalPseudolikelihood_Structure-Generative-Models-Without-Labeled-Data.md) | Related Work | Prior work contrasts supervised graphical-model selection and hand-specified LF dependencies with Ratner et al. **data programming** as the established generative weak-supervision framework. |
| [2017_VLDB_Snorkel_Rapid-Training-Data-Creation-Weak-Supervision.md](./2017_VLDB_Snorkel_Rapid-Training-Data-Creation-Weak-Supervision.md) | Introduction | Snorkel is described as the first end-to-end system implementing the **data programming** paradigm (Ratner et al., NeurIPS 2016). |
| [2021_NeurIPS_WRENCH_Comprehensive-Benchmark-Weak-Supervision.md](./2021_NeurIPS_WRENCH_Comprehensive-Benchmark-Weak-Supervision.md) | Section 4 / prior work | Positions WRENCH against the **data programming / Snorkel** line (Ratner et al.; Fu FlyingSquid; Yu COSINE; HMM-CHMM lineage) as the standard weak-supervision stack. |

---
## Relevance to Proxy Label Learning

**Rating: Very High (foundational framework for proxy label generation).**

1. **LFs = attribution models as supervisors:** Each attribution model (SHAP, LIME, Integrated Gradients) can be treated as a labeling function — a noisy, potentially conflicting source that assigns importance scores to training instances. Data programming's framework directly applies: learn the accuracy and correlation structure of multiple attribution models without ground-truth feature importance.
2. **Multiple attribution runs = multiple LFs:** Running SHAP with different background distributions or seeds produces multiple LFs over the same dataset. The generative model learns which runs are more reliable and combines them into a denoised probabilistic label.
3. **Dependency modeling:** If two attribution methods disagree on a specific feature interaction (e.g., SHAP vs. LIME for multiplicative features), this can be encoded as an "exclusive" dependency — preventing the generative model from treating their disagreement as additional noise.
4. **Asymptotic scaling guarantee:** The theorem that O(1) LFs + O(ε^{-2}) unlabeled points achieves ε-accurate labels directly answers the question of whether a small number of attribution models can produce high-quality proxy labels for large-scale datasets.
5. **Limitation:** Data programming was designed for discrete classification labels. Direct application to continuous Shapley scores requires extension to the regression case (continuous label programming) — addressed partially by MeTaL / Snorkel 2.0 variants.

## Method Tracker Update

- **Data Programming**: Ratner et al., NeurIPS 2016 | Baseline mentions: 0 | Derived variants: 3 (Snorkel, MeTaL, WRENCH) | Component count: 3 | Simplicity: 3 | Performance consistency: 3 | Composite: ~15
