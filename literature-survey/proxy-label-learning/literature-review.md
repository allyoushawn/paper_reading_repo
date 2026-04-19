Date: 2026-04-12  
Topic: Proxy label learning / learning with noisy and surrogate supervision  
Paper count: ~86 analyzed markdown notes in `read-papers/` (plus supporting blog and industry PDFs ingested in NotebookLM)

# Proxy Label Learning — Literature Review

This document synthesizes **five full-notebook NotebookLM queries** against the main corpus notebook `6fbcf9e6-3833-4660-8b56-67b0b98bf394` (no per-source filter). Per-paper detail lives in [`read-papers/`](./read-papers/); claims below should be cross-checked against those notes when precision matters.

## Executive Summary

Across the notebook, work clusters into **(1)** sample selection and small-loss curricula under label noise, **(2)** semi-supervised and pseudo-label pipelines (including debiasing and confirmation-bias analyses), **(3)** **privileged features distillation** and related **knowledge distillation** where a teacher/proxy produces training-time targets, **(4)** transition-matrix and robust-loss corrections, and **(5)** consistency-regularized SSL. Industry-style **proxy labels** (ranking, conversion, RLHF reward models) appear as concrete instantiations of the same question this survey cares about: when the training target is not the deployment objective, what inductive biases and losses keep the student aligned with the true task?

### Most Promising Approaches

1. **Joint denoising + SSL (DivideMix-style):** treat suspected-noisy points as unlabeled and apply modern SSL rather than only discarding them — see [DivideMix note](./read-papers/2020_ICLR_DivideMix_Learning-Noisy-Labels-Semi-supervised.md) (if present) or survey entries citing DivideMix in `read-papers/`.
2. **Privileged information and distillation:** explicit mechanisms for train-only features that proxy the label — [Taobao PFD](./read-papers/2020_KDD_NA_Privileged-Features-Distillation-Taobao.md), [CLID](./read-papers/2024_WSDM_CLID_Calibration-Compatible-Listwise-Distillation-Privileged-Features.md), [HA-PFD](./read-papers/2025_KDD_HA-PFD_Hardness-aware-Privileged-Features-Distillation-CVR.md), [MO-LTR-MD](./read-papers/2024_KDD_MO-LTR-MD_Multi-objective-Learning-Rank-Model-Distillation.md).
3. **Transition-matrix and instance-dependent noise modeling:** forward/backward correction and IDN estimators — [Patrini et al. CVPR 2017](./read-papers/2017_CVPR_NA_Loss-Correction-Label-Noise.md), [Dual T / transition matrix line](./read-papers/2020_NeurIPS_DualT_Dual-T-Reducing-Estimation-Error-Transition-Matrix.md), [MDDC](./read-papers/2022_MM_MDDC_Tackling-Instance-Dependent-Label-Noise-Dynamic-Distribution-Calibration.md).
4. **Reward-model / RLHF generalization as proxy-label learning:** [Topological RLHF reward analysis](./read-papers/2024_arXiv_RewardGeneralizationinRL_Reward-Generalization-in-RLHF-A-Topological.md), [on-policy + active proxy RM](./read-papers/2024_arXiv_OnPolicyActive_Cost-Effective-Proxy-Reward-Model-Construction.md), [hidden-state regularized RM](./read-papers/2024_NeurIPS_GRM_Regularizing-Hidden-States-Generalizable-Reward-Model.md).
5. **Programmatic weak supervision:** Snorkel / WRENCH / label models — [Snorkel](./read-papers/2017_VLDB_Snorkel_Rapid-Training-Data-Creation-Weak-Supervision.md), [WRENCH](./read-papers/2021_NeurIPS_WRENCH_Comprehensive-Benchmark-Weak-Supervision.md), [HLM](./read-papers/2023_ICLR_HyperLabelModel_Learning-Hyper-Label-Weak-Supervision.md).

### Practical Recommendations

**Short term (1–3 months):** adopt **small-loss / curriculum** diagnostics on your proxy-labeled retention dataset; benchmark **PFD-style** students when any high-signal features exist only at training time; read [Combating label noise with surrogate selection](./read-papers/2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md) for CLIP-assisted cleaning patterns.

**Mid term (3–6 months):** prototype **DivideMix-like** pipelines if continuous proxy scores can be thresholded into clean vs uncertain regimes; invest in **transition-matrix or IDN** tooling if noise is structured by user segment or channel; for attribution-derived scores, mirror **RLHF reward literature** on overoptimization and proxy–true mismatch.

---

## 1. Dominant methodological approaches (from NLM Q1)

NotebookLM’s cross-paper synthesis highlights five pillars (lightly edited for readability):

### 1.1 Sample selection and noise cleansing

Methods exploit the **early-learning / small-loss** phenomenon and cross-network disagreement to avoid confirmation bias. Representative notes in this folder include [MentorNet](./read-papers/2018_ICML_MentorNet_Data-Driven-Curriculum-Corrupted-Labels.md), [Co-teaching](./read-papers/2018_NeurIPS_Co-teaching_Robust-Training-Extremely-Noisy-Labels.md), [Co-teaching+](./read-papers/2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md), [DivideMix](./read-papers/2020_ICLR_DivideMix_Learning-Noisy-Labels-Semi-supervised.md), and [LNABM / surrogate selection](./read-papers/2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md).

### 1.2 Pseudo-labeling, self-training, and SSL

Modern SSL (FixMatch-style) and debiased self-training appear throughout; see [pseudo-label confirmation bias](./read-papers/2019_arXiv_MixupPseudoLabeling_Pseudo-Labeling-Confirmation-Bias-Deep-SSL.md), [UPS](./read-papers/2021_ICLR_UPS_In-Defense-Pseudo-Labeling.md), [DST](./read-papers/2022_NeurIPS_DST_Debiased-Self-Training.md), [SoftMatch](./read-papers/2023_ICLR_SoftMatch_Quantity-Quality-Tradeoff-Semi-Supervised.md), and blog syntheses [Ruder overview](./read-papers/2018_Blog_NA_Overview-Proxy-Label-Approaches-SSL.md), [Lilian Weng SSL](./read-papers/2021_Blog_NA_Semi-Supervised-Learning-Not-Enough-Data.md).

### 1.3 Privileged features distillation and knowledge distillation

Teacher–student and **PFD** are the closest industrial analogues to attribution-derived proxy labels. See [Hinton KD](./read-papers/2014_NIPS_NA_Distilling-the-Knowledge-in-a-Neural-Network.md), [Taobao PFD](./read-papers/2020_KDD_NA_Privileged-Features-Distillation-Taobao.md), [SEAD / self-auxiliary distillation](./read-papers/2024_RecSys_NA_Self-Auxiliary-Distillation-Sample-Efficient-Google-Recommenders.md), [soft-label bias](./read-papers/2021_arXiv_WSL_Rethinking-Soft-Labels-Knowledge-Distillation.md), [biased soft labels](./read-papers/2023_arXiv_NA_Learning-Biased-Soft-Labels.md), [weak-to-strong KD theory](./read-papers/2024_arXiv_NA_High-Dimensional-Knowledge-Distillation-Weak-to-Strong.md), plus ranking/industry notes cited in the executive summary bullets.

### 1.4 Loss correction, robust losses, and transition matrices

Foundational and modern robust objectives: [Natarajan et al. 2013](./read-papers/2013_NeurIPS_NA_Learning-with-Noisy-Labels.md), [Patrini loss correction](./read-papers/2017_CVPR_NA_Loss-Correction-Label-Noise.md), [SCE](./read-papers/2019_ICCV_SCE_Symmetric-Cross-Entropy-Robust-Learning-Noisy-Labels.md), [PENCIL](./read-papers/2019_CVPR_PENCIL_Probabilistic-End-to-End-Noise-Correction.md), [ELR](./read-papers/2020_NeurIPS_ELR_Early-Learning-Regularization-Noisy-Labels.md), [Dual T](./read-papers/2020_NeurIPS_DualT_Dual-T-Reducing-Estimation-Error-Transition-Matrix.md), [GJS](./read-papers/2021_NeurIPS_GJS_Generalized-Jensen-Shannon-Divergence-Loss.md), [instance-level noise theory](./read-papers/2021_arXiv_UnderstandingInstanceLev_Understanding-Instance-Level-Label-Noise-Disparate.md), [MDDC](./read-papers/2022_MM_MDDC_Tackling-Instance-Dependent-Label-Noise-Dynamic-Distribution-Calibration.md).

### 1.5 Weak supervision and label models

[Data programming](./read-papers/2016_NeurIPS_DataProgramming_Creating-Large-Training-Sets-Quickly.md), [Snorkel](./read-papers/2017_VLDB_Snorkel_Rapid-Training-Data-Creation-Weak-Supervision.md), [generative structure without labels](./read-papers/2017_ICML_MarginalPseudolikelihood_Structure-Generative-Models-Without-Labeled-Data.md), [WRENCH](./read-papers/2021_NeurIPS_WRENCH_Comprehensive-Benchmark-Weak-Supervision.md), [source-aware influence](./read-papers/2022_NeurIPS_SourceAwareIF_Understanding-Programmatic-Weak-Supervision-Influence.md), [HLM](./read-papers/2023_ICLR_HyperLabelModel_Learning-Hyper-Label-Weak-Supervision.md).

---

## 2. Datasets and benchmarks (from NLM Q2)

**Vision / synthetic noise:** CIFAR-10/100 (symmetric, asymmetric, instance-dependent corruptions) dominate; large-scale **WebVision** and **Clothing1M** appear repeatedly for real web noise; **CIFAR-10N/100N** and related human-annotation noise sets show up in robust-training notes.

**Weak supervision:** **WRENCH** suite is the standard harness for label-model papers in this corpus.

**Ranking / ads:** **Web30K**, Istella-style LTR sets, and proprietary-style simulations appear in PFD / listwise distillation notes.

**LLM / RLHF:** TL;DR, CNN/DailyMail, AlpacaEval/MT-Bench-style references show up in reward-model generalization notes.

See individual `read-papers/*.md` files for dataset-level tables per paper.

---

## 3. Recurring open problems (from NLM Q3)

- **Instance-dependent noise** is harder than class-conditional models; many algorithms still assume overly simple noise ([structural causal view](./read-papers/2021_arXiv_CausalNL_Instance-Dependent-Label-Noise-Structural-Causal-Model.md), disparate impacts [theory note](./read-papers/2021_arXiv_UnderstandingInstanceLev_Understanding-Instance-Level-Label-Noise-Disparate.md)).
- **Benchmark realism:** synthetic CIFAR noise is convenient but weakly predictive of industrial proxy noise.
- **Coupled long-tail / multi-label / noise** regimes remain under-explored relative to single-label balanced assumptions.
- **Pre-training noise → downstream** effects are increasingly flagged as gaps ([NMTune](./read-papers/2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md)).
- **RLHF:** proxy reward overoptimization / reward hacking is an explicit open risk ([RLHF topological](./read-papers/2024_arXiv_RewardGeneralizationinRL_Reward-Generalization-in-RLHF-A-Topological.md), [hidden-state RM](./read-papers/2024_NeurIPS_GRM_Regularizing-Hidden-States-Generalizable-Reward-Model.md)).

---

## 4. Foundational papers (from NLM Q4)

NotebookLM highlights memorization analyses (Arpit et al.; Zhang et al.), **knowledge distillation** (Hinton et al.), **Co-teaching**, **DivideMix**, **loss correction** (Patrini et al.), **MentorNet**, and **FixMatch** as papers that many others conceptually build on. In *this* repository’s `read-papers/` set, the corresponding anchors are the markdown files named above for Hinton, Patrini, Co-teaching, DivideMix, MentorNet, FixMatch (where present), plus classic noisy-label [Natarajan et al.](./read-papers/2013_NeurIPS_NA_Learning-with-Noisy-Labels.md).

---

## 5. Baseline dependency map (from NLM Q5)

NotebookLM produced a **method → papers that benchmark against it** map (e.g., forward/backward correction used in PENCIL, DivideMix, Dual T, CausalNL, CIFAR-N revisited, surrogate selection; MentorNet and Co-teaching/+ appearing across transition-matrix and robust-training papers; DivideMix as a recurring SSL–noise hybrid baseline). Use NLM answer #5 in `_nlm_phase4_queries.jsonl` alongside per-paper “Related Work” sections for authoritative citation chains.

---

## References (low relevance / peripheral in repo)

Some diffusion-, SAM-, or ALIGN-focused notes are included mainly as **peripheral** robustness or representation-learning context; see their `Relevance` headers inside `read-papers/` before relying on them for proxy-label product decisions.

---

## Artifact

- Raw NotebookLM answers: [`_nlm_phase4_queries.jsonl`](./_nlm_phase4_queries.jsonl)
