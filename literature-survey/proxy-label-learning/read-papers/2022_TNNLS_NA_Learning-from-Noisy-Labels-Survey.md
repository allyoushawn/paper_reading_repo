# Paper Analysis: Learning from Noisy Labels with Deep Neural Networks: A Survey

**Source:** https://arxiv.org/pdf/2007.08199  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Learning from Noisy Labels with Deep Neural Networks: A Survey  
**Authors:** Hwanjun Song, Minseok Kim, Dongmin Park, Yooju Shin, Jae-Gil Lee  
**Abstract:** A comprehensive survey reviewing 62 state-of-the-art robust deep learning methods for training under noisy labels. The methods are categorized into five groups by methodological difference, with systematic comparison across six properties.

**Key contributions:**
- Taxonomy of 62 methods into five categories: Robust Architecture, Robust Regularization, Robust Loss Function, Loss Adjustment, and Sample Selection
- Systematic comparison across six properties: Flexibility, No Pre-training, Full Exploration, No Supervision, Heavy Noise, Complex Noise
- Summary of benchmark datasets and evaluation protocols used in the field
- Identification of open research directions including instance-dependent noise, multi-label data, and class imbalance settings

**Methodology:**  
Survey paper. Conducts a taxonomy-based systematic literature review of deep learning methods designed to handle noisy (corrupted) labels in classification. Does not propose a new method.

**Main results:**  
Real-world label noise rates range from 8.0% to 38.5% in practice. Hybrid approaches combining sample selection with semi-supervised learning achieve strongest performance at high noise rates. Instance-dependent noise, multi-label settings, and class imbalance remain underexplored.

---

## 2. Experiment Critique

**Design:**  
As a survey paper, this does not run new experiments. The comparison across 62 methods is property-based (binary/partial flags) rather than empirical accuracy-based head-to-head comparison. The six-property checklist captures structural properties (flexibility, pre-training requirement, noise tolerance type) but not performance under identical conditions.

**Statistical validity:**  
No new statistical claims. The survey summarizes results from original papers without re-running experiments; this limits comparability across methods since they use different architectures, datasets, and noise settings.

**Online experiments (if any):**  
Not applicable.

**Reproducibility:**  
The survey includes open-source implementation availability for each of the 62 methods, which is a useful reproducibility index. GitHub repo maintained at https://github.com/songhwanjun/Awesome-Noisy-Labels.

**Overall:**  
As a survey, this is a well-organized reference. The taxonomy is useful for navigation. Main limitation is the absence of unified re-evaluation experiments, making direct performance comparison across methods difficult.

---

## 3. Industry Contribution

**Deployability:**  
Survey papers inform practitioners about the solution landscape. The property-based comparison (especially "No Pre-training," "No Supervision," "Heavy Noise") is directly useful for deployment decisions.

**Problems solved:**  
Gives a structured view of which methods are applicable when ground-truth annotations are unavailable or expensive — directly relevant to proxy-label learning settings where labels come from imperfect signals (attribution models, weak labelers, teacher models).

**Engineering cost:**  
Survey format makes this a zero-cost entry point for any engineering team starting work in noisy-label robustness.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First systematic methodological comparison of robust training approaches across six unified properties. Prior surveys (Frénay & Verleysen 2013, Han et al. 2020) used different or narrower categorizations.

**Prior work comparison:**  
Frénay & Verleysen (2013) covered non-deep methods; Han et al. (2020) focused on general input/objective/optimization decomposition rather than methodological family.

**Verification:**  
The categorization (five groups) is the de facto taxonomy adopted by subsequent papers. The survey is well-cited (>2000 citations) and widely used as the reference taxonomy.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10/100 | https://www.cs.toronto.edu/~kriz/cifar.html | Yes | Clean data with synthetic noise |
| MNIST | http://yann.lecun.com/exdb/mnist | Yes | Clean benchmark |
| ANIMAL-10N | Public | Yes | Real-world noisy |
| CIFAR-10N/100N | Public | Yes | Human-annotated noise from MTurk |
| Clothing1M | Public | Yes | Web-crawled clothing images |
| WebVision | Public | Yes | 2.4M web images, real noise |

**Offline experiment reproducibility:**  
Not directly applicable — survey paper. Referenced methods each have their own reproducibility.

---

## 6. Community Reaction

The Song et al. 2022 survey is the standard reference for the noisy label learning taxonomy. It is widely cited and the associated Awesome-Noisy-Labels GitHub repo is frequently referenced by new papers. The five-category taxonomy (Robust Architecture / Regularization / Loss Function / Loss Adjustment / Sample Selection) has become the canonical framing.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Hwanjun Song, Minseok Kim, Dongmin Park, Yooju Shin, Jae-Gil Lee  
**Affiliations:** NAVER AI Lab; KAIST  
**Venue:** IEEE Transactions on Neural Networks and Learning Systems (TNNLS)  
**Year:** 2022  
**PDF:** available at arxiv.org/pdf/2007.08199  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** 4f7a865b-cf5c-44de-b002-df5d893e6236
