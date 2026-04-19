Date: 2026-04-12

# Proxy Label Learning — Executive Summary

## Key Questions

Questions this literature survey is trying to answer (from `requirements.md`):

1. What happens when a model is trained on **proxy or surrogate labels** instead of ground truth, and does it generalize to the true task?
2. How do **instance-dependent**, feature-dependent, or **systematic** label errors affect learned behavior?
3. Which **robust training** tools (loss correction, sample selection, SSL hybrids) are most evidence-backed?
4. How does **bias from the label generator** (teacher, weak labeler, reward model, attribution model) propagate to the student?
5. When do models trained on **continuous proxy scores** (e.g., Shapley-style credits) still track the deployment objective?

## Main Findings

Based on **~86** per-paper markdown analyses in `read-papers/` plus NotebookLM cross-notebook synthesis (`literature-review.md`):

1. **Proxy supervision is not one problem.** The literature splits into noisy *class* labels, *soft* targets from teachers, **privileged features** available only at training time, and **RLHF reward scores**—but the common question is identifiability: what extra structure (clean anchor set, small-loss behavior, transition model, PI, or multi-head disagreement) prevents the student from fitting generator bias.

2. **Empirical anchors repeat:** CIFAR with synthetic noise, WebVision / Clothing1M, and (for weak supervision) **WRENCH** appear across dozens of papers, so reported gains are often **relative to shared baselines** such as `"Patrini et al., Making Deep Neural Networks Robust to Label Noise: a Loss Correction Approach, CVPR 2017"`, `"Han et al., Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels, NeurIPS 2018"`, and `"Li et al., DivideMix: Learning with Noisy Labels as Semi-supervised Learning, ICLR 2020"` (see `literature-review.md` §2).

3. **Industrial analogues are explicit.** `"Xu et al., Privileged Features Distillation at Taobao Recommendations, KDD 2020"`, `"Tang et al., Multi-objective Learning to Rank by Model Distillation, KDD 2024"`, `"Yuan et al., Hardness-aware Privileged Features Distillation with Latent Alignment for CVR Prediction, KDD 2025"` (see `read-papers/2025_KDD_HA-PFD_Hardness-aware-Privileged-Features-Distillation-CVR.md`), and RLHF reward papers (`"Kirk et al., Understanding the Effects of RLHF on LLM Generalisation and Diversity, ICLR 2024"` and companions in `read-papers/`) stress **train/serve skew**—the same skew attribution-based retention labels introduce.

4. **Open gaps** (NotebookLM Q3 synthesis, echoed in `"Liu et al., Understanding Instance-Level Label Noise: Disparate Impacts and Treatments, ICML 2021"` and causal IDN notes) include **real benchmarks with verified clean labels**, **joint noise + long-tail**, and **foundation-model pretraining noise** (`"Chen et al., Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks, ICLR 2024"`).

## Most Fundamental Methods (from `method-tracker.md`, top 5 by fundamentality composite score)

Criteria: frequent **baseline** use, **variants**, **consistent** cross-paper measurements, and **simple** mechanisms (`method-tracker.md` §“How to Compute…”).

1. **Small-loss trick / sample selection** (composite **37**): Clean examples tend to drop loss earlier; most curricula and co-training schemes exploit this. Synthesized across `"Han et al., Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels, NeurIPS 2018"`, `"Jiang et al., MentorNet: Learning Data-Driven Curriculum for Very Deep Neural Networks on Corrupted Labels, ICML 2018"`, and follow-on survey notes.

2. **LUPI (Learning Using Privileged Information)** (composite **30**): Formalizes features present only at training time—the closest classical framing to **proxy labels** that are not observable at inference. `"Vapnik & Vashist, Learning Using Privileged Information, 2009"` as cited through `"Collier et al., Transfer and Marginalize: Explaining Away Label Noise with Privileged Information, ICML 2022"` and Pi-DUAL line in `read-papers/`.

3. **Noise transition matrix (forward / backward correction)** (composite **28**): Estimating **class-flip** structure remains a standard baseline path under label noise. `"Patrini et al., Making Deep Neural Networks Robust to Label Noise: a Loss Correction Approach, CVPR 2017"` and `"Han et al., Dual T: Reducing Estimation Error for Transition Matrix in Label-noise Learning, NeurIPS 2020"` (`read-papers/2020_NeurIPS_DualT_Dual-T-Reducing-Estimation-Error-Transition-Matrix.md`).

4. **Co-teaching** (composite **28**): Two-network **disagreement / cross-teaching** is still a reference point for debiasing sample selection. `"Han et al., Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels, NeurIPS 2018"`.

5. **DivideMix** (composite **27**): Bridges **noise robustness** and **SSL** by treating low-confidence data as unlabeled. `"Li et al., DivideMix: Learning with Noisy Labels as Semi-supervised Learning, ICLR 2020"`.

## For a model trained on attribution-derived proxy labels (continuous Shapley scores), what does the literature say?

**Direct Shapley-as-label papers are sparse in this corpus**, so conclusions are **analogical**:

- **Privileged features distillation** and **listwise / multi-task distillation** (`"Xu et al., Privileged Features Distillation at Taobao Recommendations, KDD 2020"`, `"Gui et al., Calibration-compatible Listwise Distillation of Privileged Features for CTR Prediction, WSDM 2024"`, `"Tang et al., Multi-objective Learning to Rank by Model Distillation, KDD 2024"`) show students can track **deployment metrics** when the teacher uses extra features—provided distillation losses align calibration and serving constraints.

- **RLHF reward modeling** (`"Yang et al., Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs, NeurIPS 2024"`, `"Kirk et al., Understanding the Effects of RLHF on LLM Generalisation and Diversity, ICLR 2024"`) warns that **proxy scores can improve while true utility worsens** (overoptimization / diversity collapse)—the same structural risk if Shapley scores are imperfect proxies for retention.

- **Soft-label and KD bias** (`"Zhou et al., Rethinking Soft Labels for Knowledge Distillation: A Bias–Variance Tradeoff Perspective, arXiv 2021"`, `"Yuan & Xu, Learning from Biased Soft Labels, arXiv 2023"`, `"Ildiz et al., High-dimensional Analysis of Knowledge Distillation: Weak-to-Strong Generalization and Scaling Laws, arXiv 2024"`) emphasize **variance and identifiability** of the teacher signal: continuous proxies help optimization but can encode systematic teacher bias.

- **Instance-dependent noise** (`"Yao et al., Instance-dependent Label-noise Learning under a Structural Causal Model, 2021"`, `"Liu et al., Understanding Instance-Level Label Noise: Disparate Impacts and Treatments, ICML 2021"`) argues that **without modeling how errors depend on inputs**, generalization to the true task is not guaranteed—Shapley credit noise is typically **input-dependent** and **generator-structured**, so these papers are philosophically on-point even when experiments are discrete-label.

**Practical read:** treat attribution outputs like **PI / teacher logits**: monitor **calibration**, use **auxiliary clean anchors** where possible, and borrow **robust training + SSL** hybrids (`"Li et al., DivideMix: Learning with Noisy Labels as Semi-supervised Learning, ICLR 2020"`, `"Liang et al., Combating Label Noise With A General Surrogate Model For Sample Selection, arXiv 2023"` in `read-papers/2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md`) when a subset of users can be labeled with higher-fidelity outcomes.

## Approach comparison (high level)

| Approach | Pros | Cons | Related work |
|----------|------|------|--------------|
| Loss correction + **T**-matrix | Interpretable noise model; strong when noise is class-conditional | Misses instance-wise structure | `"Patrini et al., Making Deep Neural Networks Robust to Label Noise: a Loss Correction Approach, CVPR 2017"` |
| Small-loss / co-teaching | Simple to bolt on; good when memorization order is clean | Confirmation bias if single network | `"Han et al., Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels, NeurIPS 2018"` |
| DivideMix-style SSL hybrid | Uses unlabeled portion of corrupted data | Hyperparameters / mixture assumptions | `"Li et al., DivideMix: Learning with Noisy Labels as Semi-supervised Learning, ICLR 2020"` |
| PFD / KD from privileged towers | Matches production skew explicitly | Needs careful calibration / serving parity | `"Xu et al., Privileged Features Distillation at Taobao Recommendations, KDD 2020"` |
| RLHF-style reward modeling | Direct precedent for scalar proxy objectives | Overoptimization vs true human utility | `"Yang et al., Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs, NeurIPS 2024"` |

## Coverage self-check (requirements.md)

Items evaluated: **5** numbered research questions + **10** “Must include” bullets + **11** core keyword themes ≈ **26** checklist atoms. **25** are covered with at least one cited paper in `literature-review.md` or this summary (**≈96%**). The single thinnest item remains **closed-form theory specifically for continuous Shapley-labeled supervised objectives** (addressed by analogy through PFD, soft-label KD, and RLHF proxy-reward work). Optional tightening: add **1** primary-source paper on **Shapley-based supervision** for deep models and rerun Phase 3 if the product team needs citation-dense grounding beyond analogies.
