Date: 2026-04-12  
Source: https://arxiv.org/pdf/2405.03676 (ingested; OpenReview PDF `ygCCLhGNNL` returned HTTP 403 to automated fetchers)  
NLM Source ID: c049f22c-24eb-4e25-be3e-78022e67be0f  
Venue: ICLR 2024  
Relevance: Related  
Priority: 2

# Paper Analysis: Why is SAM Robust to Label Noise?

**Source:** https://arxiv.org/pdf/2405.03676  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Why is SAM Robust to Label Noise?

**Authors:** Christina Baek, Zico Kolter, Aditi Raghunathan (Carnegie Mellon University)

**Abstract:**  
Sharpness-Aware Minimization (SAM) is widely known for modest clean-task gains, but its largest improvements appear under **random label noise**, often rivaling specialized robust-training methods. The paper argues that explaining this requires analyzing **early-stopping behavior**, not flatness at convergence. It decomposes SAM’s sample-wise update into **logit-scale** vs **Jacobian** components, shows linear-model robustness is driven by logit reweighting, and argues deep networks are driven primarily by the **Jacobian** mechanism.

**Key contributions:**
- Empirical demonstration that **1-SAM** (per-sample perturbation) yields large robustness gains vs SGD under noise (e.g., CIFAR-10 with 30% noise).
- Mechanistic decomposition into **L-SAM** (logit-only perturbation) vs **J-SAM** (Jacobian-only perturbation): **J-SAM** nearly matches SAM; **L-SAM** barely helps in deep nets.
- Theory for **two-layer deep linear networks** showing J-SAM relates to **activation + last-layer weight norm regularization**, motivating a cheaper explicit regularizer.

**Methodology:**  
Synthetic Gaussian toy data; CIFAR-10 / Tiny-ImageNet / Flowers102 with injected noise; architectures include linear models, 2-layer DLN/MLP, and **ResNet-18 with BatchNorm replaced by LayerNorm** (required for stable per-sample SAM).

**Main results:**  
Example table in-source: **1-SAM 69.47%** vs **SGD 52.48%** vs **J-SAM 69.17%** vs **L-SAM 54.13%** on CIFAR-10 noisy setting; proposed explicit last-layer activation/weight regularization closes part of the gap (**60.8%**).

---

## 2. Experiment Critique

**Design:**  
Clear controlled ablations isolating optimizer components; multiple datasets and noise settings. Important architecture caveat: **BN incompatible** with 1-SAM’s per-sample passes → LayerNorm swap changes baseline behavior.

**Statistical validity:**  
Standard classification accuracy with early stopping; noise injection is synthetic (except some additional dataset commentary in-source).

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
Methodological setup is reproducible in principle, but 1-SAM increases compute vs SGD; hyperparameters include SAM radius \(\rho\).

**Overall:**  
The negative result on **L-SAM** in deep nets is a strong piece of evidence against “logit reweighting alone explains SAM under noise” in nonlinear regimes.

---

## 3. Industry Contribution

**Deployability:**  
SAM-family optimizers are already used in training stacks; the paper’s cheaper regularizer is “illustrative” (authors caution it is not a full replacement for SAM’s clean-task gains).

**Problems solved:**  
Improves understanding (and partial emulation) of robustness to **noisy supervision** in vision training pipelines.

**Engineering cost:**  
1-SAM is expensive; practical systems more often use approximations or alternatives.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
Mechanistic account of SAM under label noise emphasizing Jacobian effects and early learning dynamics, contrasting with prior sharpness-centric narratives.

**Prior work comparison:**  
Engages extensively with **Foret et al. (SAM)** and contrasts with **Andriushchenko & Flammarion** analyses; relates to robust learning baselines cited in introduction (e.g., MentorNet / Co-teaching+ family).

**Verification:**  
Positioning is coherent with the empirical L-SAM vs J-SAM separation; claims are localized to studied architectures/settings.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10 | Public benchmark | Yes | Synthetic label noise |
| Tiny-ImageNet / Flowers102 | Public benchmark | Yes | Noisy-label experiments in-source |
| Toy Gaussian synthetic | Not a standard public dataset | Partial | Defined in paper |

**Offline experiment reproducibility:**  
CIFAR-10/Tiny-ImageNet pipelines are standard; toy setup is specified in appendices referenced by the source.

---

## 6. Community Reaction

Quick searches did not locate HN/Reddit threads specifically discussing this ICLR title versus unrelated “SAM” segmentation threads. **No significant community discussion found** in the scan performed for this batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Christina Baek, Zico Kolter, Aditi Raghunathan  
**Affiliations:** Carnegie Mellon University  
**Venue:** ICLR 2024  
**Year:** 2024  
**PDF:** downloaded (arXiv; OpenReview mirror blocked with 403 in this environment)  
**Relevance:** Related  
**Priority:** 2

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
