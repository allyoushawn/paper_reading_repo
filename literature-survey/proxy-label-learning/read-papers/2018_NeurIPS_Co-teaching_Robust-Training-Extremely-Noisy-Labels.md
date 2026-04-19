# Paper Analysis: Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels

**Source:** https://arxiv.org/pdf/1804.06872  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels  
**Authors:** Bo Han, Quanming Yao, Xingrui Yu, Gang Niu, Miao Xu, Weihua Hu, Ivor W. Tsang, Masashi Sugiyama  
**Abstract:** Proposes Co-teaching, a dual-network training paradigm where two networks simultaneously train and cross-teach each other using only small-loss instances, achieving state-of-the-art robustness under extremely noisy labels (45–50% noise rates).

**Key contributions:**
- Co-teaching paradigm: two networks with different initializations each select small-loss instances and teach them to the peer network, not to themselves
- Dynamic drop rate R(T): starts high (keep most data early when networks are noise-resistant) and decreases over time as networks begin memorizing noise
- Reduces error accumulation from self-selection bias (a core failure mode of MentorNet and single-network approaches)
- Achieves state-of-the-art on MNIST, CIFAR-10, CIFAR-100 under extreme noise (45–50%)

**Methodology:**  
Two neural networks (same architecture, different initializations) are trained simultaneously. Each network selects its small-loss instances (likely clean) and passes them to the peer for parameter update. A dynamic drop schedule reduces the fraction of kept instances over epochs.

**Main results:**  
MNIST Pair-45%: Co-teaching 87.63% vs MentorNet 80.88%. CIFAR-10 Pair-45%: Co-teaching 72.62% vs MentorNet 58.14%. CIFAR-100 Symmetry-50%: Co-teaching 41.37% vs F-correction 41.04%. Co-teaching also achieves higher label precision than baselines throughout training.

---

## 2. Experiment Critique

**Design:**  
Three datasets (MNIST, CIFAR-10, CIFAR-100) with two noise types (Pair-45% and Symmetry-50%). Compared against 6 baselines (Standard, Bootstrap, S-model, F-correction, Decoupling, MentorNet). Experiments are repeated 5 times with error bars. Both test accuracy and label precision (clean-label selection quality) are reported.

**Statistical validity:**  
Results include mean and standard deviation over 5 runs. The separation between Co-teaching and baselines is large enough (e.g., 14% gap on CIFAR-10 Pair-45%) to be clearly significant even without formal significance tests.

**Online experiments (if any):**  
None. All experiments are offline with synthetically corrupted datasets.

**Reproducibility:**  
Code available at https://github.com/bhanML/Co-teaching. Architecture and hyperparameters (Adam, lr=0.001, batch=128, 200 epochs) are specified. Relies on known noise rate for setting R(T) schedule.

**Overall:**  
Well-executed. The use of both test accuracy and label precision as metrics is informative. The main limitation is that label noise is synthetic (symmetric or pair-flip), not real-world annotation noise.

---

## 3. Industry Contribution

**Deployability:**  
Co-teaching is simple to implement: two copies of any model trained with a small-loss selection filter and cross-update. No special architecture needed. Works with any optimizer. Directly applicable to proxy-label settings where noise rate can be estimated.

**Problems solved:**  
When training labels come from a noisy proxy source (attribution model, teacher model, weak labeler), Co-teaching's small-loss trick can filter out the most aggressively mislabeled examples and reduce overfitting to proxy label errors.

**Engineering cost:**  
Moderate: requires 2x model parameters during training, which doubles memory and compute. At inference, only one network is needed.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Unlike MentorNet (single self-evolving network) and Decoupling (updates only on disagreement), Co-teaching explicitly cross-teaches: each network trains on the other's clean-instance selections. This breaks the error feedback loop that causes self-selection bias.

**Prior work comparison:**  
MentorNet requires a separate pre-trained teacher; Co-teaching is trained from scratch. Decoupling uses disagreement criterion that is not robust (noisy labels are evenly spread). Co-teaching combines the small-loss trick with the anti-confirmation-bias advantage of dual-network training.

**Verification:**  
Co-teaching is the most widely used baseline in the noisy-label learning literature (cited in nearly every subsequent paper: DivideMix, ELR, FINE, Neural Relation Graph, etc.). Its status as a canonical baseline confirms the novelty and impact of the contribution.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| MNIST | http://yann.lecun.com/exdb/mnist | Yes | Artificially corrupted |
| CIFAR-10 | https://www.cs.toronto.edu/~kriz/cifar.html | Yes | Artificially corrupted |
| CIFAR-100 | https://www.cs.toronto.edu/~kriz/cifar.html | Yes | Artificially corrupted |

**Offline experiment reproducibility:**  
High. Code is released and hyperparameters are fully specified.

---

## 6. Community Reaction

Co-teaching (NeurIPS 2018) is one of the most impactful papers in noisy label learning. It has accumulated thousands of citations and is the de facto standard baseline. The dual-network cross-teaching paradigm has directly inspired DivideMix (Li et al. ICLR 2020), ELR+ (Liu et al. NeurIPS 2020), FINE (NeurIPS 2021), and many others. It is commonly used as the primary baseline in new method evaluations.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2018_ICML_MentorNet_Data-Driven-Curriculum-Corrupted-Labels.md](./2018_ICML_MentorNet_Data-Driven-Curriculum-Corrupted-Labels.md) | Novelty vs. Prior Work | the loss level. MentorNet's dynamic, trainable weighting is more flexible. Verification: MentorNet is the standard predecessor to Co-teaching and DivideMix. It is cited in virtually every subsequent noisy-label paper as a key baseline. The Google affiliation and ICML 2018 venue confirm high quali... |
| [2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md](./2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md) | Summary | Help Generalization against Label Corruption? Authors: Xingrui Yu, Bo Han, Jiangchao Yao, Gang Niu, Ivor W. Tsang, Masashi Sugiyama Abstract: Co-teaching trains two networks with the small-loss trick and cross-updates peer-selected examples, but the two networks converge to agreement over epochs,... |
| [2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md](./2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md) | Related Work | Positions Co-teaching+ as building on **Han et al. Co-teaching** and compares against **MentorNet**, **Decoupling**, **Patrini et al. F-correction**, and open-set noise protocols. |
| [2020_ICLR_DivideMix_Learning-Noisy-Labels-Semi-supervised.md](./2020_ICLR_DivideMix_Learning-Noisy-Labels-Semi-supervised.md) | Novelty vs. Prior Work | 74.76% (vs. P-correction 73.49%). Consistently state-of-the-art across all benchmarks. --- Paper's claimed novelty: Key advance over Co-teaching: cross-epoch co-divide (GMM-based dataset partitioning) combined with SSL makes noisy samples useful (as unlabeled data), whereas Co-teaching simply dis... |
| [2020_NeurIPS_DualT_Dual-T-Reducing-Estimation-Error-Transition-Matrix.md](./2020_NeurIPS_DualT_Dual-T-Reducing-Estimation-Error-Transition-Matrix.md) | Summary | pairs (fitting labels vs. fitting posteriors) - Empirical matrix-estimation error reductions and accuracy gains when plugging dual-T into MentorNet / Co-teaching / Forward / Reweighting / Revision Methodology: Warm up a classifier; reserve a validation split to mitigate overfitting when estimatin... |
| [2020_NeurIPS_ELR_Early-Learning-Regularization-Noisy-Labels.md](./2020_NeurIPS_ELR_Early-Learning-Regularization-Noisy-Labels.md) | Summary | examples and neutralize gradients of mislabeled ones - ELR+: enhanced variant combining ELR with weight averaging, dual-network cross-target estimation (Co-teaching-inspired), and MixUp augmentation - Significantly faster than DivideMix (2.3h vs 5.4h on CIFAR-10) Methodology: For each example, ma... |
| [2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md](./2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md) | Novelty vs. Prior Work | (principal components align with randomly labeled data); FINE operationalizes this observation. Prior work comparison: Co-teaching (Han et al. 2018): small-loss selection across two networks — replaced by FINE in F-Coteaching. DivideMix (Li et al. 2020): GMM on loss distribution — FINE outperform... |
| [2021_arXiv_CausalNL_Instance-Dependent-Label-Noise-Structural-Causal-Model.md](./2021_arXiv_CausalNL_Instance-Dependent-Label-Noise-Structural-Causal-Model.md) | Summary | Y\mid Y,X)$. CausalNL instantiates this via a causal VAE with decoders for reconstruction and label corruption, ELBO training, and a two-branch co-teaching wrapper to align latent clusters with classes while reducing selection bias. Key contributions: - SCM factorization $P(X,\tilde Y,Y,Z)=P(Y)P(... |
| [2021_arXiv_NA_Instance-dependent-Label-noise-Learning-under.md](./2021_arXiv_NA_Instance-dependent-Label-noise-Learning-under.md) | Main note body | *Co-teaching: Robust training of deep neural networks with extremely noisy labels*:** Extensively referenced as a leading baseline and explicitly integrated into the CausalNL framework to dynamically select reliable training examples and reduce selection bias [14-20]. * **Pearl (2000) - *Causalit... |
| [2022_ICLR_CIFAR-N_Learning-Noisy-Labels-Revisited-Real-World-Human-Annotations.md](./2022_ICLR_CIFAR-N_Learning-Noisy-Labels-Revisited-Real-World-Human-Annotations.md) | Main note body | -10N Worst) \| Method \| CIFAR-10N Worst \| CIFAR-100N \| \|--------\|----------------\|-----------\| \| CE \| 77.69 \| 55.50 \| \| Co-Teaching+ \| 83.26 \| 57.88 \| \| ELR \| 83.58 \| 58.94 \| \| SOP+ \| 94.0 \| — \| \| RepReg (CE+Reg) \| 88.74 \| 60.81 \| |
| [2022_ICML_ICML_Estimating-Instance-dependent-Label-noise-Transition.md](./2022_ICML_ICML_Estimating-Instance-dependent-Label-noise-Transition.md) | Novelty vs. Prior Work | et al. (forward correction), Xia et al. (PTD, T-Revision), Han et al. (co-teaching family as baselines). Verification: ICML 2022 proceedings (PMLR 162); arXiv 2105.13001 aligns with camera-ready content. --- |
| [2022_ICML_BLTM_Estimating-Bayes-Label-Transition-Matrix-DNNs.md](./2022_ICML_BLTM_Estimating-Bayes-Label-Transition-Matrix-DNNs.md) | Experiment Critique | Synthetic IDN sweeps list **Co-teaching / Co-teaching+** among broad baselines (alongside MentorNet, Forward/Reweight/T-Revision, PTD, DivideMix in appendix). |
| [2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md](./2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md) | Novelty vs. Prior Work | et al. 2017) that require anchor points or clean validation data, SOP requires no such assumptions. Unlike two-network methods (DivideMix, Co-teaching) that require complex training pipelines, SOP is a single-model single-stage method. The implicit sparsity regularization via the u∘u − v∘v Hadama... |
| [2022_arXiv_NA_Tackling-Instance-Dependent-Label-Noise-with.md](./2022_arXiv_NA_Tackling-Instance-Dependent-Label-Noise-with.md) | Main note body | web) [30, 31]. * Comparison Baselines: * Standard training (SGD), Co-teaching+, GCE (Generalized Cross Entropy), SL (Symmetric Cross Entropy), and LRT [32]. * PLC (Progressive Label Correction) was used as a primary direct comparison, as the MDDC and CDDC methods gracefully degrade to PLC if the ... |
| [2023_ICML_CrossSplit_Mitigating-Label-Noise-Memorization-Data-Splitting.md](./2023_ICML_CrossSplit_Mitigating-Label-Noise-Memorization-Data-Splitting.md) | Novelty vs. Prior Work | , which reinforces memorized noise. CrossSplit's peer network cannot have seen the label it is correcting. Prior work comparison: Han et al. 2018 (Co-teaching): selects clean samples across two networks — CrossSplit uses soft correction instead of hard selection. Li et al. 2020 (DivideMix): GMM-b... |
| [2023_arXiv_NA_Combating-Label-Noise-With-A-General.md](./2023_arXiv_NA_Combating-Label-Noise-With-A-General.md) | Main note body | representing the "small-loss criterion," a learning-centric strategy that identifies clean samples by assuming networks fit simple patterns first [17, 23, 24]. 4. Arpit et al. (2017): Cited to establish the foundational theoretical premise of label noise research: the "memorization effect," which... |
| [2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md](./2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md) | Novelty vs. Prior Work | claimed novelty: First study of label noise in pre-training affecting downstream performance. Classic noisy label learning (DivideMix, ELR, Co-teaching) focuses on training from scratch. NML is a different problem — the noisy pre-trained model is the starting point, and downstream data may be cle... |
| [2024_NeurIPS_DeFT_Vision-Language-Models-Strong-Noisy-Label-Detectors.md](./2024_NeurIPS_DeFT_Vision-Language-Models-Strong-Noisy-Label-Detectors.md) | Main note body | /HotanLee/DeFT ## Problem Fine-tuning vision-language models (e.g., CLIP) on noisy downstream datasets is challenging. Standard small-loss filtering (GMM, Co-teaching) fails on instance-dependent noise and "hard" clean samples with large loss. Full fine-tuning (FFT) on noisy data distorts CLIP's ... |
| [2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md](./2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md) | Summary | . Methodology: Follows FINE’s experimental protocol backbone/hyperparameters (per paper text summarized by NLM); compares against broad baselines (Co-teaching(+), CRUST, FINE, etc.). Main results: NLM-cited examples: CIFAR-100 40% asymmetric accuracy 73.2% vs FINE 61.7% (+11.5 points absolute in ... |
| [2022_NeurIPS_NoiseShape_Robustness-Label-Noise-Shape-Distribution.md](./2022_NeurIPS_NoiseShape_Robustness-Label-Noise-Shape-Distribution.md) | Empirical validation | Evaluates mitigation methods including **CoTeaching** under feature-dependent noise; reports degradation vs. baseline at higher noise. |
| [2023_ICML_IdentifiabilityFramework_Identifiability-Label-Noise-Transition-Matrix.md](./2023_ICML_IdentifiabilityFramework_Identifiability-Label-Noise-Transition-Matrix.md) | Community Reaction | Warns that correlated artificial labels (e.g., **co-teaching style** stacked teachers) can violate conditional-independence assumptions for transition-matrix identifiability. |
| [2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md](./2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md) | Novelty vs Prior Work | Baseline zoo includes **Co-teaching / JoCoR / JoSRC** among small-loss and robust-training comparisons. |
| [2024_ICLR_SAM_Why-SAM-Robust-Label-Noise.md](./2024_ICLR_SAM_Why-SAM-Robust-Label-Noise.md) | Novelty vs. Prior Work | Relates SAM under label noise to robust learning baselines cited in the introduction (e.g., **MentorNet / Co-teaching+** family). |

---
## Meta Information

**Authors:** Bo Han, Quanming Yao, Xingrui Yu, Gang Niu, Miao Xu, Weihua Hu, Ivor W. Tsang, Masashi Sugiyama  
**Affiliations:** University of Technology Sydney; RIKEN; 4Paradigm Inc.; Stanford University; University of Tokyo  
**Venue:** NeurIPS 2018  
**Year:** 2018  
**PDF:** available at arxiv.org/pdf/1804.06872  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** b144c219-3d9c-4f2d-9eed-5f0e27a3dc3a
