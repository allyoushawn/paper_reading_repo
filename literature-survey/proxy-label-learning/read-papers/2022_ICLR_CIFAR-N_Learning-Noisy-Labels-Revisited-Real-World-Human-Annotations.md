Date: 2026-04-11
Source: https://arxiv.org/pdf/2110.12088
NLM Source ID: 61cfde88-ff84-495c-8e84-c3b2335411b6
Venue: ICLR 2022 (competition track / dataset paper)
Relevance: Core
Priority: 1

# Learning with Noisy Labels Revisited: A Study Using Real-World Human Annotations

**Authors:** Jiaheng Wei, Zhaowei Zhu, Hao Cheng, Tongliang Liu, Gang Niu, Yang Liu
**Affiliation:** UC Santa Cruz, University of Sydney, RIKEN
**Dataset:** http://noisylabels.com

## Contribution

This paper introduces **CIFAR-10N and CIFAR-100N** — the standard benchmark for learning with real-world noisy labels. These are CIFAR-10/100 training images re-annotated by Amazon Mechanical Turk workers, providing ground-truth clean labels alongside authentic human-generated noisy labels. This enables controlled, reproducible evaluation without the scale confounds of Clothing1M or WebVision.

## Dataset Construction

- **CIFAR-10N:** 50K training images re-annotated by 3 independent workers each → 5 noisy label sets (aggre, random1-3, worst)
- **CIFAR-100N:** 50K images, single annotation per image; workers guided by superclass hierarchy
- Collection: Amazon Mechanical Turk, paid per HIT; no ground-truth used for quality control (only pattern-detection filtering)

## Key Empirical Findings

**Finding 1: Human noise is instance-dependent (proven by hypothesis test)**
- Tested via M-NN noise clusterability: transition matrix T(x) is feature-dependent (not class-dependent)
- Hypothesis test result: p = 1.8e−36 — overwhelmingly rejects class-dependent noise hypothesis for CIFAR-10N
- Human annotators mislabel based on visual features, not just class confusion

**Finding 2: Imbalanced annotations**
- Annotators have strong class preferences: automobile mislabeled more often than truck, horse more than deer
- CIFAR-100N: 25% of noisy labels fall outside super-class, 15% inside — showing both cross-category and within-category confusion

**Finding 3: Label flips to similar features**
- ~20% of "snake" images mislabeled as "worm" and vice versa; similar for "cockroach"-"beetle", "fox"-"wolf"
- This structured class confusion is qualitatively different from random symmetric noise

**Finding 4: Multiple valid labels**
- Many CIFAR-100 "errors" are legitimate ambiguities: flatfish image with a man holding the fish → annotator selects "man"
- This implies some noisy labels are not errors but reflect genuine multi-label structure

**Finding 5: Performance gap (human vs. synthetic noise)**
- Robust methods designed for synthetic noise consistently perform worse on human noise at the same noise level
- Exception: ELR performs slightly better on real noise than synthetic — suggesting its temporal smoothing aligns with human noise patterns

**Finding 6: Aggravated memorization**
- DNNs overfit human-annotated wrong labels more easily than synthetic noise
- Human errors cluster around ambiguous/complex instances — exactly the features DNN memorizes first

## Benchmark Results (key methods on CIFAR-10N Worst)

| Method | CIFAR-10N Worst | CIFAR-100N |
|--------|----------------|-----------|
| CE | 77.69 | 55.50 |
| Co-Teaching+ | 83.26 | 57.88 |
| ELR | 83.58 | 58.94 |
| SOP+ | 94.0 | — |
| RepReg (CE+Reg) | 88.74 | 60.81 |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md](./2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md) | Summary | with std=1e-8. SOP+ adds KL consistency regularizer and class-balance regularizer. Architecture: ResNet34 for synthetic noise, PreActResNet18 for CIFAR-N. Main results: CIFAR-10 synthetic symmetric: SOP 93.18/90.09/86.76/68.32% at 20/40/60/80% noise (vs ELR 91.16/89.15/86.12/73.86%). SOP+ 94.0% a... |
| [2023_ICML_LogitClip_Mitigating-Memorization-Noisy-Labels-Clipping.md](./2023_ICML_LogitClip_Mitigating-Memorization-Noisy-Labels-Clipping.md) | Novelty vs. Prior Work | 2018 (GCE): partially robust. Menon et al. 2020 (PHuber-CE, gradient clipping): shown not sufficient for noise robustness. LogitNorm (Wei et al. 2022a): focuses on OOD detection, not noisy labels; always normalizes to unit norm (equivalent to fixed τ=1). LogitClip differs by having an adaptive th... |
| [2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md](./2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md) | Summary | per algorithm text in source; ignore garbled bracket artifacts in some summaries). - Empirical gains on symmetric/asymmetric CIFAR noise, Clothing1M, and CIFAR-N variants vs strong selection baselines; MW-Net shown to overfit badly under noise in reported tables. Methodology: Follows FINE’s exper... |

---
## Relevance to Proxy Label Learning

**Rating: Very High (provides conceptual foundation + benchmark).**

1. **CIFAR-N is THE benchmark for proxy-label methods:** Every method in this survey that reports "real-world noise" results uses CIFAR-10N or CIFAR-100N. Understanding how these benchmarks were constructed is essential for interpreting method comparisons.
2. **Instance-dependent human noise = proxy label model:** The proven IDN structure of human annotations exactly parallels attribution-derived labels — both are feature-dependent, both cluster around decision-ambiguous instances.
3. **Multiple valid labels observation maps to proxy label ambiguity:** Attribution-derived labels for instances that are genuinely hard to attribute (high feature interaction, attribution variance) are analogous to multi-label images — there is no single "correct" proxy label.
4. **Memorization of systematic errors:** The finding that DNNs memorize human annotation patterns (structured errors) applies directly to Shapley proxy labels — the model will memorize attribution artifacts associated with specific feature patterns.
5. **Performance gap insight:** Methods optimized for synthetic noise don't transfer reliably to real/structured noise — validating the need for methods specifically designed for instance-dependent proxy label regimes.

## Method Tracker Update

This is a dataset paper — no new method. No tracker row needed.
