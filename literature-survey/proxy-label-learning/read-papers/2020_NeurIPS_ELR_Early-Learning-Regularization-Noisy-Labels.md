# Paper Analysis: Early-Learning Regularization Prevents Memorization of Noisy Labels

**Source:** https://arxiv.org/pdf/2007.00151  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Early-Learning Regularization Prevents Memorization of Noisy Labels  
**Authors:** Sheng Liu, Jonathan Niles-Weed, Narges Razavian, Carlos Fernandez-Granda  
**Abstract:** Proposes Early-Learning Regularization (ELR), a framework that exploits the early-learning phase of deep networks to prevent memorization of noisy labels. Uses temporal ensembling to estimate target probabilities and adds a regularization term that boosts the gradient signal from clean examples and neutralizes the gradient from mislabeled ones.

**Key contributions:**
- Theoretical proof that early learning and memorization are fundamental phenomena in high-dimensional classification, occurring even in simple linear models
- ELR regularization: adds a term log(1 - <p[i], t[i]>) to cross-entropy, where t[i] is a temporal ensemble target — analytically shown to boost gradients of clean examples and neutralize gradients of mislabeled ones
- ELR+: enhanced variant combining ELR with weight averaging, dual-network cross-target estimation (Co-teaching-inspired), and MixUp augmentation
- Significantly faster than DivideMix (2.3h vs 5.4h on CIFAR-10)

**Methodology:**  
For each example, maintain a running average target t[i] (temporal ensembling with momentum β). Add regularization term λ·log(1 - <p[i], t[i]>) to cross-entropy loss. The gradient analysis shows this term boosts learning on clean examples (whose gradient magnitude falls after the early phase) and suppresses mislabeled examples (whose gradient would otherwise dominate).

**Main results:**  
Clothing1M: ELR+ 74.81% vs DivideMix 74.76% (state-of-the-art). WebVision top-1: ELR+ 77.78% vs DivideMix 77.32%. CIFAR-10 Sym-90%: ELR+ 75.2%, slightly below DivideMix 76.0%. Training time: ELR 1.1h, ELR+ 2.3h — more than 2x faster than DivideMix (5.4h).

---

## 2. Experiment Critique

**Design:**  
Four benchmarks: CIFAR-10, CIFAR-100, Clothing1M, WebVision. Both symmetric and asymmetric synthetic noise. Ablation study decomposes contributions of temporal ensembling, weight averaging, dual-network, and MixUp. Hyperparameter sensitivity analysis for β, λ, and α.

**Statistical validity:**  
CIFAR results include mean ± std over 5 noise realizations — better than most comparable papers. Real-world dataset results (Clothing1M, WebVision) are single-run.

**Online experiments (if any):**  
None.

**Reproducibility:**  
Simple implementation: only requires adding one regularization term to the training loop plus a running average of model outputs. No second model needed for base ELR (ELR+ needs two models). Code available via supplementary material.

**Overall:**  
Excellent theoretical justification (gradient analysis in Section 4.2) paired with strong empirical results. The key limitation is that ELR+ underperforms DivideMix on ILSVRC12 evaluation (70.29% vs 75.20% top-1), suggesting the approach may be less robust to cross-distribution generalization. KL-divergence alternative is carefully analyzed and shown to fail.

---

## 3. Industry Contribution

**Deployability:**  
Base ELR is extremely deployment-friendly: single network, one additional regularization term, running average of model outputs. No second model, no GMM fitting, no special sampling. Training is 5x faster than DivideMix.

**Problems solved:**  
ELR's theoretical insight — that noisy-label gradient dominates late in training — directly applies to proxy-label settings. In attribution-derived supervision, the systematic bias of the attribution model will push model parameters in wrong directions late in training; ELR's regularization prevents this. The temporal ensemble target can be seen as a "denoised" version of the attribution label signal.

**Engineering cost:**  
Low (base ELR). Moderate (ELR+ with dual networks). The simplicity of the implementation makes ELR particularly attractive for production deployment.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Unlike Co-teaching and DivideMix (which use sample selection to detect and exclude noisy examples), ELR does not throw away any samples. Instead, it implicitly suppresses the gradient of noisy examples through the regularization term. This is both simpler and theoretically grounded.

**Prior work comparison:**  
The key innovation over DivideMix is the theoretical analysis connecting early learning to gradient dynamics, and the regularization-based approach instead of sample selection. The temporal ensembling idea comes from Laine & Aila (2018) in SSL context; ELR's novelty is the specific log(1 - <p, t>) form which is analytically shown to have the desired gradient properties, unlike the simpler KL divergence approach.

**Verification:**  
ELR is the SOTA on Clothing1M and competitive with DivideMix on CIFAR benchmarks. Strong theoretical contribution. Widely cited and adopted in subsequent work.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10/100 | https://www.cs.toronto.edu/~kriz/cifar.html | Yes | Synthetic noise |
| Clothing1M | Public | Yes | Real-world noisy |
| WebVision (mini) | Public | Yes | ~66K images, 50 classes |

**Offline experiment reproducibility:**  
High. Implementation is simple and fully described.

---

## 6. Community Reaction

ELR (NeurIPS 2020, NYU) received significant positive attention for its theoretical contribution — the gradient analysis connecting early learning to label noise is elegant and widely cited. The ELR+ variant achieving near-parity with DivideMix while being 2x faster is practically impactful. It is commonly cited alongside DivideMix as the reference point for strong noisy-label learning methods.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md](./2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md) | Summary / Main results | Synthetic CIFAR-10 results report SOP vs. ELR at multiple noise rates; Clothing-1M and WebVision comparisons include ELR as a baseline. |
| [2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md](./2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md) | Summary | FINE as detector can boost robust losses including **GCE/SCE/ELR** (applications mode 3). |
| [2021_NeurIPS_GJS_Generalized-Jensen-Shannon-Divergence-Loss.md](./2021_NeurIPS_GJS_Generalized-Jensen-Shannon-Divergence-Loss.md) | Summary / results | WebVision / ILSVRC12 tables compare GJS ensemble vs **ELR+** (e.g., ILSVRC12 top-1 **GJS 74.33% vs ELR+ 70.29%** in excerpt). |
| [2022_ICLR_CIFAR-N_Learning-Noisy-Labels-Revisited-Real-World-Human-Annotations.md](./2022_ICLR_CIFAR-N_Learning-Noisy-Labels-Revisited-Real-World-Human-Annotations.md) | Findings + benchmark table | **ELR** listed among benchmark methods on CIFAR-10N / CIFAR-100N; narrative notes ELR can do slightly better on real human noise than synthetic at matched rates. |
| [2022_ICML_NLS_To-Smooth-or-Not-Label-Smoothing-Noisy.md](./2022_ICML_NLS_To-Smooth-or-Not-Label-Smoothing-Noisy.md) | Experiment Critique | Baseline zoo explicitly includes **ELR** alongside SCE, Peer Loss, AUM, etc., across CIFAR-N and synthetic noise suites. |
| [2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md](./2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md) | Novelty vs. Prior Work | Classic noisy label learning (**DivideMix**, **ELR**, **Co-teaching**) focuses on training from scratch; NML studies noisy *pre-trained* models as the starting point. |
| [2024_ICLR_LabelWave_Early-Stopping-Label-Noise-Without-Validation.md](./2024_ICLR_LabelWave_Early-Stopping-Label-Noise-Without-Validation.md) | Problem | Existing methods (**ELR**, **DivideMix**) embed noise robustness into training but do not address stopping time explicitly; oracle early stopping beats their best checkpoints. |
| [2024_ICLR_SGN_Robust-Classification-Regression-Noisy-Labels.md](./2024_ICLR_SGN_Robust-Classification-Regression-Noisy-Labels.md) | Key Results | Tables compare SGN to strong baselines including **ELR+** on Clothing1M and WebVision (e.g., competitive with ELR+ on WebVision top-1). |
| [2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md](./2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md) | Novelty vs Prior Work | Positions against small-loss / GMM selection (DivideMix lineage), **Co-teaching / JoCoR / JoSRC**, **MOIT+**, **ELR+**, **NCR**, **InstanceGM**, **LSL**, **F-correction**, etc. |
| [2023_arXiv_NA_Combating-Label-Noise-With-A-General.md](./2023_arXiv_NA_Combating-Label-Noise-With-A-General.md) | Main note body | Benchmark narrative compares against **ELR / ELR+** among broad LNL baselines alongside DivideMix, Co-teaching+, MentorNet/MentorMix, MOIT+, NCR, etc. |

---
## Meta Information

**Authors:** Sheng Liu, Jonathan Niles-Weed, Narges Razavian, Carlos Fernandez-Granda  
**Affiliations:** New York University (Center for Data Science; Courant Institute; NYU School of Medicine)  
**Venue:** NeurIPS 2020  
**Year:** 2020  
**PDF:** available at arxiv.org/pdf/2007.00151  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** 193b001d-b755-4f22-984b-9fa91bbf555f
