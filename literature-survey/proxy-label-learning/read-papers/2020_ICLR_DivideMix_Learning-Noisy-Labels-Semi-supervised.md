# Paper Analysis: DivideMix: Learning with Noisy Labels as Semi-supervised Learning

**Source:** https://arxiv.org/pdf/2002.07394  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** DivideMix: Learning with Noisy Labels as Semi-supervised Learning  
**Authors:** Junnan Li, Richard Socher, Steven C.H. Hoi  
**Abstract:** Proposes DivideMix, a framework that bridges learning with noisy labels (LNL) and semi-supervised learning (SSL). Uses per-sample Gaussian Mixture Model to dynamically split training data into labeled (clean) and unlabeled (noisy) sets, then applies improved MixMatch with co-divide to train robustly.

**Key contributions:**
- Co-divide: two networks each fit a GMM to per-sample losses to partition training data, and the partition is used to train the other network (avoids confirmation bias)
- Label co-refinement: for labeled samples, blends ground-truth label with model prediction weighted by GMM-derived clean probability from the other network
- Label co-guessing: for unlabeled samples, uses ensemble prediction from both networks across multiple augmentations to generate reliable pseudo-labels
- Confidence penalty during warm-up: adds negative entropy to prevent over-confident predictions on asymmetric noise, enabling GMM to separate clean/noisy samples

**Methodology:**  
Two-network training. Each epoch: (1) fit 2-component GMM to per-sample cross-entropy loss, (2) use the other network's GMM to partition data into labeled/unlabeled, (3) apply modified MixMatch (co-refinement + co-guessing) for SSL training on both sets.

**Main results:**  
CIFAR-10 Sym-90%: 76.0% (vs. M-correction 69.1%). CIFAR-100 Sym-90%: 31.5% (vs. M-correction 24.3%, ~10% improvement). WebVision top-1: 77.32% (vs. Iterative-CV 65.24%, >12% improvement). Clothing1M: 74.76% (vs. P-correction 73.49%). Consistently state-of-the-art across all benchmarks.

---

## 2. Experiment Critique

**Design:**  
Four datasets (CIFAR-10, CIFAR-100, Clothing1M, WebVision) with both synthetic and real-world noise. Symmetric and asymmetric noise types at multiple levels (20%–90% on CIFAR). Ablation study in Table 5 decomposes contributions of each component. Training time analysis included.

**Statistical validity:**  
Accuracy is reported as both "best" and "last epoch average," which is more honest than reporting only the best. Ablation study confirms the individual importance of co-divide, label refinement, augmentation, and ensemble. However, standard deviations are not reported.

**Online experiments (if any):**  
None. All offline image classification benchmarks.

**Reproducibility:**  
Code available at https://github.com/LiJunnan1992/DivideMix. All hyperparameters reported. One sensitive hyperparameter: λ_u (unsupervised loss weight) must be tuned per-experiment (higher values needed for higher noise or more classes).

**Overall:**  
Strong experimental validation. The ablation study is particularly valuable. Limitation: no theoretical analysis of why GMM works better than BMM; the approach is empirically motivated. Also, requires 5.2h training on CIFAR-10 (2x DivideMix vs Co-teaching time).

---

## 3. Industry Contribution

**Deployability:**  
More complex than Co-teaching but highly effective. Requires two networks and a GMM fitting step per epoch. The SSL approach (treating noisy samples as unlabeled) is a principled design that extracts signal from all available data — a significant advantage in proxy-label settings where many labels may be systematically biased.

**Problems solved:**  
When training on attribution-derived proxy labels, some labels will be systematically wrong. DivideMix's GMM-based soft partitioning and SSL treatment of noisy samples directly addresses this: instead of discarding potentially useful noisy-label examples, it extracts information via consistency regularization.

**Engineering cost:**  
High: 2x parameters, GMM fitting overhead, multiple augmentations per sample. Training is ~2x slower than Co-teaching+. Not suitable for very fast iteration cycles.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
Key advance over Co-teaching: cross-epoch co-divide (GMM-based dataset partitioning) combined with SSL makes noisy samples useful (as unlabeled data), whereas Co-teaching simply discards them. The co-guessing and co-refinement mechanisms enable explicit cross-network teaching at the mini-batch level.

**Prior work comparison:**  
M-correction (Arazo et al. 2019) also uses mixture model loss fitting but with Beta Mixture Model (BMM), which fails under asymmetric noise. DivideMix replaces BMM with GMM and adds the co-divide anti-confirmation-bias structure. MixMatch (Berthelot et al. 2019) provides the SSL backbone.

**Verification:**  
DivideMix is the dominant SOTA on CIFAR and WebVision benchmarks as of 2020–2022. Many subsequent papers (ELR, CSOT, Active Negative Loss) use it as the primary baseline. Confirmed novel contribution.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10/100 | https://www.cs.toronto.edu/~kriz/cifar.html | Yes | Synthetic noise injected |
| Clothing1M | Public | Yes | Real-world noisy labels |
| WebVision | Public | Yes | 2.4M web-crawled images |

**Offline experiment reproducibility:**  
High. All code and hyperparameters provided.

---

## 6. Community Reaction

DivideMix (ICLR 2020) is the canonical strong baseline in noisy label learning after Co-teaching. It has thousands of citations. Subsequent papers consistently compare against DivideMix and most report improvements only under specific settings (e.g., ELR+ on Clothing1M; CSOT in structure-aware settings). The MixMatch + GMM combo set the standard for the 2020–2022 period.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2018_ICML_MentorNet_Data-Driven-Curriculum-Corrupted-Labels.md](./2018_ICML_MentorNet_Data-Driven-Curriculum-Corrupted-Labels.md) | Novelty vs. Prior Work | MentorNet's dynamic, trainable weighting is more flexible. Verification: MentorNet is the standard predecessor to Co-teaching and DivideMix. It is cited in virtually every subsequent noisy-label paper as a key baseline. The Google affiliation and ICML 2018 venue confirm high quality. --- |
| [2018_NeurIPS_Co-teaching_Robust-Training-Extremely-Noisy-Labels.md](./2018_NeurIPS_Co-teaching_Robust-Training-Extremely-Noisy-Labels.md) | Novelty vs. Prior Work | : Co-teaching is the most widely used baseline in the noisy-label learning literature (cited in nearly every subsequent paper: DivideMix, ELR, FINE, Neural Relation Graph, etc.). Its status as a canonical baseline confirms the novelty and impact of the contribution. --- |
| [2020_NeurIPS_ELR_Early-Learning-Regularization-Noisy-Labels.md](./2020_NeurIPS_ELR_Early-Learning-Regularization-Noisy-Labels.md) | Summary | combining ELR with weight averaging, dual-network cross-target estimation (Co-teaching-inspired), and MixUp augmentation - Significantly faster than DivideMix (2.3h vs 5.4h on CIFAR-10) Methodology: For each example, maintain a running average target t[i] (temporal ensembling with momentum β). Ad... |
| [2021_Blog_NA_Semi-Supervised-Learning-Not-Enough-Data.md](./2021_Blog_NA_Semi-Supervised-Learning-Not-Enough-Data.md) | Summary | ensembling, Mean Teacher, VAT, UDA), pseudo-labeling / self-training (Noisy Student, Meta Pseudo Labels), and hybrids (MixMatch family, FixMatch, DivideMix sketch). It also connects SSL to pre-training + self-training tradeoffs. Key contributions: - Unified loss framing and intuitive diagrams/not... |
| [2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md](./2021_NeurIPS_FINE_Filtering-Noisy-Instances-via-Eigenvectors.md) | Novelty vs. Prior Work | work comparison: Co-teaching (Han et al. 2018): small-loss selection across two networks — replaced by FINE in F-Coteaching. DivideMix (Li et al. 2020): GMM on loss distribution — FINE outperforms significantly at extreme noise. CRUST (Mirzasoleiman et al. 2020): low-rank Jacobian subset — FINE o... |
| [2021_NeurIPS_GJS_Generalized-Jensen-Shannon-Divergence-Loss.md](./2021_NeurIPS_GJS_Generalized-Jensen-Shannon-Divergence-Loss.md) | Summary | input. Achieves SOTA on both synthetic and real-world noise benchmarks with a single simple loss function, outperforming complex multi-network pipelines like DivideMix on WebVision top-1. Key contributions: - JS loss: theoretically shown to interpolate between CE (π₁→0) and MAE (π₁→1); symmetric ... |
| [2022_ICML_ICML_Estimating-Instance-dependent-Label-noise-Transition.md](./2022_ICML_ICML_Estimating-Instance-dependent-Label-noise-Transition.md) | Summary | “-V” variant - Empirical gains vs PTD / matrix baselines and competitive or better behavior vs complex pipelines (e.g., DivideMix) on hard IDN regimes Methodology: (1) Estimate noisy posteriors $\tilde\eta$; distill high-confidence examples. (2) Train transition network on distilled set minimizin... |
| [2022_ICML_BLTM_Estimating-Bayes-Label-Transition-Matrix-DNNs.md](./2022_ICML_BLTM_Estimating-Bayes-Label-Transition-Matrix-DNNs.md) | Experiment Critique | Appendix claims **+3.22% / +4.38%** over DivideMix on worst-case CIFAR-10 / SVHN at IDN-50% with a simpler two-stage matrix + forward-correction pipeline vs DivideMix’s GMM/SSL hybrid. |
| [2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md](./2022_ICML_SOP_Robust-Training-Label-Noise-Over-parameterization.md) | Summary | regularization (UDA) and class-balance regularization for SOTA results - Training efficiency: SOP takes 1.0h, SOP+ 2.1h on CIFAR-10/50% noise vs. DivideMix 5.4h Methodology: Loss: min_{θ,{ui,vi}} (1/N) Σ ℓ(f(xi;θ) + ui∘ui − vi∘vi, yi). CE is used for θ and ui; MSE for vi. Initialization of {ui,vi... |
| [2022_MM_MDDC_Tackling-Instance-Dependent-Label-Noise-Dynamic-Distribution-Calibration.md](./2022_MM_MDDC_Tackling-Instance-Dependent-Label-Noise-Dynamic-Distribution-Calibration.md) | Summary | gains on PMD + symmetric/asymmetric hybrids on CIFAR-10/100; real-world WebVision mini + Clothing1M; optional DivideMix boosting (DivideMix-M / DivideMix-C) Methodology: Warm-up $\to$ iterative confidence thresholding PLC $\to$ extract features $\to$ per-class AgnosticMean or disturbed covariance... |
| [2022_NeurIPS_DST_Debiased-Self-Training.md](./2022_NeurIPS_DST_Debiased-Self-Training.md) | Summary | by class). - DST as plug-in stabilizer for FixMatch, FlexMatch, Mean Teacher, Noisy Student, DivideMix, etc. - Large empirical gains from scratch and from supervised / unsupervised ImageNet-pretrained ResNet-50 on many transfer tasks. Methodology: WRN-28-2 (CIFAR-10/SVHN), WRN-28-8 (CIFAR-100), W... |
| [2022_arXiv_NA_Tackling-Instance-Dependent-Label-Noise-with.md](./2022_arXiv_NA_Tackling-Instance-Dependent-Label-Noise-with.md) | Main note body | ]: Cited as a leading state-of-the-art hybrid framework for learning with noisy labels, which the authors specifically use as a high-performing baseline to boost with their own methods [6, 19, 29]. 4. Huber, 1992 / 2004 [30, 31]: Cited as the foundational statistical works that define robust stat... |
| [2023_ICML_CDNL_Which-is-Better-SSL-vs-Model-Noisy-Labels.md](./2023_ICML_CDNL_Which-is-Better-SSL-vs-Model-Noisy-Labels.md) | Novelty vs. Prior Work | causal and anticausal regimes in the noisy labels context. Prior work comparison: Patrini et al. 2017 (Forward): model-based baseline. Li et al. 2020 (DivideMix): SSL baseline. Schölkopf et al. 2012, Peters et al. 2017: causal modularity theory. VolMinNet (Li et al. 2021): prior SOTA for flip-rat... |
| [2023_ICML_CrossSplit_Mitigating-Label-Noise-Memorization-Data-Splitting.md](./2023_ICML_CrossSplit_Mitigating-Label-Noise-Memorization-Data-Splitting.md) | Novelty vs. Prior Work | : Han et al. 2018 (Co-teaching): selects clean samples across two networks — CrossSplit uses soft correction instead of hard selection. Li et al. 2020 (DivideMix): GMM-based clean/noisy split + SSL — CrossSplit bypasses the selection. Karim et al. 2022 (UNICON): contrastive + FixMatch + selection... |
| [2023_ICML_LogitClip_Mitigating-Memorization-Noisy-Labels-Clipping.md](./2023_ICML_LogitClip_Mitigating-Memorization-Noisy-Labels-Clipping.md) | Summary | vs. clean labels is bounded by a function of τ and K - Universal enhancement: boosts CE, MAE, PHuber-CE, SCE, GCE, Taylor-CE, NCE, AEL, AUL, AGCE, Cores, DivideMix, SOP, SAM - Model-agnostic: consistent gains on ResNet, DenseNet, SqueezeNet architectures - Key design advantage over clipping-by-va... |
| [2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md](./2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md) | Summary | . Methodology: Pipeline: (1) pretrain representation with noisy labels (protocol aligned with DivideMix / Sel-CL prior work); (2) reinitialize classifier; (3) use frozen CLIP to score each example—prediction confidence (keep if CLIP probability for noisy label \(y_i\) exceeds \(\rho\)) and option... |
| [2023_arXiv_NA_Combating-Label-Noise-With-A-General.md](./2023_arXiv_NA_Combating-Label-Noise-With-A-General.md) | Main note body | -of-the-art semi-supervised learning baseline, which the authors use both as a comparative benchmark and as the initialization backbone for their own architecture [5, 6, 17-19]. 2. Radford et al. (2021) [CLIP]: Cited extensively as the foundational open-vocabulary vision-language surrogate model ... |
| [2024_ICLR_LabelWave_Early-Stopping-Label-Noise-Without-Validation.md](./2024_ICLR_LabelWave_Early-Stopping-Label-Noise-Without-Validation.md) | Main note body | samples. The obstacle: selecting the stopping epoch typically requires a clean validation set, which is unavailable in noisy label settings. Existing methods (ELR, DivideMix) embed noise robustness into training but don't address stopping time explicitly. Oracle early stopping (using clean test a... |
| [2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md](./2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md) | Novelty vs. Prior Work | -- Paper's claimed novelty: First study of label noise in pre-training affecting downstream performance. Classic noisy label learning (DivideMix, ELR, Co-teaching) focuses on training from scratch. NML is a different problem — the noisy pre-trained model is the starting point, and downstream data... |
| [2024_ICML_Pi-DUAL_Privileged-Information-Distinguish-Clean-Noisy-Labels.md](./2024_ICML_Pi-DUAL_Privileged-Information-Distinguish-Clean-Noisy-Labels.md) | Summary | (AUC 0.986 on ImageNet-PI high-noise) - Pi-DUAL+ enhanced variant with semi-supervised regularization achieves 83.23% on CIFAR-10H, outperforming DivideMix by 11+ points Methodology: During training: all parameters updated jointly via cross-entropy on the combined logit h(x,a). At test time: only... |
| [2024_NeurIPS_CSGN_Latent-Causal-Structure-Label-Noise.md](./2024_NeurIPS_CSGN_Latent-Causal-Structure-Label-Noise.md) | Main note body | Key Results \| Dataset \| CSGN \| Best Baseline \| Delta \| \|---------\|------\|--------------\|-------\| \| CIFAR-10 IDN-50% \| 95.88% \| DivideMix 86.30% \| +9.58pp \| \| CIFAR-100N (real) \| 71.99% \| CoDis ~70% \| +~2pp \| \| WebVision top-1 \| 79.84% \| CrossSplit 79.19% \| +0.65pp \| \| CIFAR-10N Worst \| ~91% \| SOP... |
| [2023_NeurIPS_LRA-Diffusion_Label-Retrieval-Augmented-Noisy-Labels.md](./2023_NeurIPS_LRA-Diffusion_Label-Retrieval-Augmented-Noisy-Labels.md) | Novelty vs Prior Work | Prior work comparison: builds on CARD-style classification diffusion; compares to **DivideMix**, **UNICON**, **PLC**, **C2D**, **EPL**, etc. |

---
## Meta Information

**Authors:** Junnan Li, Richard Socher, Steven C.H. Hoi  
**Affiliations:** Salesforce Research  
**Venue:** ICLR 2020  
**Year:** 2020  
**PDF:** available at arxiv.org/pdf/2002.07394  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** f32dc10c-0ec5-404c-bfb1-de98bc319e1d
