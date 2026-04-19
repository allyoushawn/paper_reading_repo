Date: 2026-04-11
Source: https://arxiv.org/pdf/2206.01106
NLM Source ID: ca707631-ba84-4eac-bc84-e474d341045b
Venue: NeurIPS 2022
Relevance: Core
Priority: 1

# Robustness to Label Noise Depends on the Shape of the Noise Distribution in Feature Space

**Authors:** Diane Oyen, Michal Kucer, Nick Hengartner, Har Simrat Singh
**Affiliation:** Los Alamos National Laboratory

## Problem

Standard analysis of label noise robustness assumes noise is either uniform (class-independent) or class-dependent (independent of features given class). Both are analytically tractable but optimistic. Real-world proxy/surrogate labels are **feature-dependent**: errors occur precisely where features are ambiguous. This paper provides the first theoretical framework for feature-dependent label noise.

## Core Theoretical Contribution

**Taxonomy of noise types:**
| Type | Definition | Tipping Point |
|------|-----------|---------------|
| Uniform | P(Y|X, Y*) = P(Y) | (c-1)/c, e.g. 90% for c=10 |
| Class-dependent | P(Y|X, Y*) = P(Y|Y*) | Can be as low as 50% (depends on spread) |
| Feature-dependent | P(Y|X, Y*) ≠ P(Y|Y*) | Can fail at 10-20% noise |

**Tipping point** = noise level beyond which true labels are no longer recoverable by any classifier.

**Worst-case feature-dependent noise (GapMax, Claim 3.7):** The samples most vulnerable to label flips are those maximizing ratio P(Y*=k|x) / max_{j≠k} P(Y*=j|x). Targeting these samples rapidly relocates decision boundaries to wrong positions. Even 10-20% noise in these regions causes catastrophic accuracy degradation.

**Key lemma:** Under feature-dependent noise at point x:
- P_k(x) decreases to (1-p(x)) * P*_k(x)
- P_j(x) increases to P*_j(x) + p(x) * P*_k(x) for the most-likely wrong class j

When p(x) is sufficiently high for boundary-straddling samples, the classifier decision flips irreversibly.

## Empirical Validation

- Gaussian 10-class synthetic data: GapMax noise at 20% causes near-chance accuracy; uniform noise at 80% causes minimal degradation
- CIFAR-10, CIFAR-100 image benchmarks with controlled feature-dependent noise injection
- Mitigation methods evaluated: CleanLab, CoTeaching, MixUp, SCE — **none reliably recovers accuracy under feature-dependent noise**; CleanLab and CoTeaching both degrade vs. baseline at higher noise levels

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

**Rating: Very High (conceptual framing).** This paper provides the most direct theoretical grounding for why proxy-label training is hard:

1. **Attribution-derived noise is inherently feature-dependent.** Shapley scores conflate attribution uncertainty with label noise in exactly the boundary-region samples where the attribution model is least confident. This paper proves that such feature-dependent noise (targeting ambiguous samples) breaks robustness guarantees that hold for class-dependent or uniform noise.

2. **The tipping point concept reframes expectations:** Practitioners who rely on "DNNs are robust to label noise" intuitions derived from uniform-noise experiments will be misled. For feature-concentrated proxy noise, robustness can fail at 10-20% noise rates — well within typical proxy label error levels.

3. **Mitigation strategy failure:** Standard noise-robust methods (Co-teaching, CleanLab) are evaluated and found to fail under feature-dependent noise. This directly motivates specialized approaches for proxy-label training rather than drop-in noise-robustness methods.

4. **Systematic attribution noise hits decision boundaries:** Attribution models assign credit precisely to features near the decision boundary (high-gradient regions). These are exactly the "high ratio" samples of Claim 3.7 — worst-case feature-dependent noise targets. This is not coincidental but structural.

**Key takeaway for the project:** Shapley-derived proxy labels will systematically corrupt decision boundaries more than transition-matrix theory predicts. Any practical approach must either (a) characterize feature-dependent noise structure, or (b) use methods robust to boundary-targeted noise.

## Method Tracker Update

This paper is theoretical/analytical (no new training method). Key result: feature-dependent noise shape matters more than scale; tipping-point analysis for 3 noise types.
