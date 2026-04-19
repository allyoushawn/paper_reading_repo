# Paper Analysis: FINE Samples for Learning with Noisy Labels

**Source:** https://arxiv.org/pdf/2102.11628  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** FINE Samples for Learning with Noisy Labels  
**Authors:** Taehyeon Kim, Jongwoo Ko, Sangwook Cho, Jinhwan Choi, Se-Young Yun  
**Abstract:** Proposes FINE (Filtering Noisy Instances via their Eigenvectors), a derivative-free clean/noisy sample detector based on the eigenvectors of the data gram matrix. Instead of using classifier-biased loss values, FINE measures alignment between each sample's latent representation and the first eigenvector of its class's gram matrix. This alignment score is then clustered with GMM to separate clean/noisy samples. The FINE detector improves sample selection, SSL (F-DivideMix), and noise-robust loss function approaches.

**Key contributions:**
- FINE score: fi = ⟨u_yi, zi⟩² where u_yi is the first eigenvector of the class-k gram matrix Σk = Σ zi·zi^T; clean data aligns with the principal component, noisy data does not
- GMM on alignment scores: two-component GMM separates clean (higher mean) from noisy (lower mean) — no noise rate estimate required
- Three applications: (1) standalone sample selection, (2) replacing DivideMix's GMM loss filter (F-DivideMix), (3) booster for GCE/SCE/ELR
- Scalable: eigenvector computed from 1% of data gives 0.99 cosine similarity to full-data eigenvector; 1.1s vs 20.1s runtime
- Theoretical guarantees: bounds on alignment perturbation from noisy instances

**Methodology:**  
Feature extractor (frozen after each epoch) produces zi (pre-logits). Gram matrix built per class. Eigen decomposition via standard SVD. GMM threshold ζ=0.5 (stable in [0.4, 0.6]). Architecture follows baseline (e.g., PreAct ResNet18 following DivideMix/FINE comparison).

**Main results:**  
Sample selection on CIFAR-100 Sym-80%: FINE 25.6% vs CRUST 21.7%, Co-teaching 20.5%. F-Coteaching: 31.6% (vs FINE 25.6%). F-DivideMix CIFAR-10 Sym-90%: 90.5% vs DivideMix 76.0% (critical improvement at extreme noise). F-DivideMix CIFAR-100 Sym-80%: 61.0% vs DivideMix 60.2%. Clothing1M: F-DivideMix 74.37% vs DivideMix 74.30%. mini-WebVision top-1: FINE 75.24% vs CRUST 72.40%. GCE+FINE CIFAR-100 Sym-80%: 37.0% vs GCE 29.2% (+7.8pp).

---

## 2. Experiment Critique

**Design:**  
Three distinct application modes (sample selection, SSL, loss function booster) each validated separately. F-score dynamics across training epochs confirm FINE consistently outperforms Co-teaching and TopoFilter. Comparison against MCD (Mahalanobis distance) as an alternative representation-based detector is rigorous. Filtering time analysis (Table 9) includes 1% dataset approximation.

**Statistical validity:**  
3 runs per experiment, mean ± std reported. F-score and test accuracy both reported. Feature-dependent noise experiments in appendix add coverage.

**Online experiments (if any):**  
None.

**Reproducibility:**  
Code released at github.com/Kthyeon/FINE_official. Hyperparameter ζ sensitivity documented (Table 7). Eigendecomposition algorithm fully specified in Algorithm 1.

**Overall:**  
Solid contribution. The derivative-free nature is a key advantage: classifier bias is avoided without any backward computation. Key limitations: mini-WebVision F-DivideMix improvement marginal (GPU memory constraints forced reduced batch size, not a fundamental failure); hyperparameter ζ requires mild tuning; applying to non-classification tasks not demonstrated.

---

## 3. Industry Contribution

**Deployability:**  
High. FINE is a drop-in replacement for any loss-based sample detection step (DivideMix's GMM, Co-teaching's small-loss selection). Computational overhead is small (1.1s per epoch on CIFAR-10 using 1% data). No backward pass required.

**Problems solved:**  
In proxy-label learning: FINE provides a theoretically grounded sample filter that does not depend on the classifier's confidence in noisy labels. When proxy labels are systematically biased, a loss-based filter may retain the wrong samples; FINE's geometric approach is more robust.

**Engineering cost:**  
Low. Single gram matrix + eigen decomposition per class per epoch. 1% data approximation makes it scalable. Drop-in API for DivideMix or Co-teaching.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First sample-selection method with theoretical guarantees based on representation eigenvectors rather than classifier loss. Prior work (Co-teaching, DivideMix, CRUST) all use loss values or gradient norms that are biased by corrupted classifier. Maennel et al. 2020 provided the theoretical motivation (principal components align with randomly labeled data); FINE operationalizes this observation.

**Prior work comparison:**  
Co-teaching (Han et al. 2018): small-loss selection across two networks — replaced by FINE in F-Coteaching. DivideMix (Li et al. 2020): GMM on loss distribution — FINE outperforms significantly at extreme noise. CRUST (Mirzasoleiman et al. 2020): low-rank Jacobian subset — FINE outperforms on most settings. TopoFilter (Wu et al. 2020): k-NN Euclidean distance — FINE outperforms on F-score. MCD estimator (Lee et al. 2019): Mahalanobis distance-based novelty detection — FINE outperforms in precision and recall.

**Verification:**  
KAIST AI, NeurIPS 2021. Code released.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10/100 (synthetic) | public | Yes | Sym/asym/feature-dep. noise |
| Clothing1M | public (request) | Yes | 1M images, 14 classes, ~38.5% noise |
| mini-WebVision | public | Yes | 50 classes, Google subset |

**Offline experiment reproducibility:**  
High. Code and hyperparameter tables released.

---

## 6. Community Reaction

KAIST AI, NeurIPS 2021. Well-received as a theoretically grounded alternative to loss-based noise detection. The F-DivideMix results at extreme noise (90% sym CIFAR-10: 90.5% vs DivideMix 76%) are widely cited. The societal concern about enabling training on illegally collected data was an unusual addition appreciated for transparency.

**Relevance to proxy-label learning:** Core. FINE's representation-based detection is directly applicable when proxy labels are noisy and classifier-based filtering is unreliable.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |
| [2017_CVPR_NA_Loss-Correction-Label-Noise.md](./2017_CVPR_NA_Loss-Correction-Label-Noise.md) | Summary | 17.1% vs forward 68.4% in one table column family). Clothing1M: best 80.38% top-1 with ResNet-50 fine-tuned from forward-corrected init vs prior AlexNet pipeline 78.24% without heavy 50k→500k bootstrap. Noise estimation bottleneck: median \(\sim\)10pt drop vs oracle \(T\); CIFAR-100 high-noise co... |
| [2018_NeurIPS_Co-teaching_Robust-Training-Extremely-Noisy-Labels.md](./2018_NeurIPS_Co-teaching_Robust-Training-Extremely-Noisy-Labels.md) | Novelty vs. Prior Work | is the most widely used baseline in the noisy-label learning literature (cited in nearly every subsequent paper: DivideMix, ELR, FINE, Neural Relation Graph, etc.). Its status as a canonical baseline confirms the novelty and impact of the contribution. --- |
| [2019_CVPR_PENCIL_Probabilistic-End-to-End-Noise-Correction.md](./2019_CVPR_PENCIL_Probabilistic-End-to-End-Noise-Correction.md) | Summary | , and an entropy term on predictions. Training: backbone warmup with CE → PENCIL joint updates (label dists use larger LR \(\lambda\)) → final fine-tune with frozen label dists. Key contributions: - End-to-end probabilistic label correction as distributions on the simplex. - Reversed-KL classific... |
| [2021_ICML_ALIGN_Scaling-Up-Visual-Vision-Language-Noisy-Text.md](./2021_ICML_ALIGN_Scaling-Up-Visual-Vision-Language-Noisy-Text.md) | Summary | pairs; evaluation on retrieval (Flickr30K, MSCOCO, CxC, Multi30k), zero-shot classification (ImageNet variants), fine-tuned classification (ImageNet, VTAB, fine-grained sets), and SimLex-999 word similarity. Main results: Strong retrieval vs. cross-attention VLMs; 76.4% ImageNet zero-shot (vs. CL... |
| [2021_NeurIPS_WRENCH_Comprehensive-Benchmark-Weak-Supervision.md](./2021_NeurIPS_WRENCH_Comprehensive-Benchmark-Weak-Supervision.md) | Summary | strong label-model defaults on average; COSINE + fine-tuned LM excels on text classification; CHMM wins on 7/8 tagging sets; soft labels often beat hard for deep end models; poor LF quality (e.g. Basketball, low-coverage MIT-Restaurant) leaves large gaps to supervised gold. --- Paper's claimed no... |
| [2021_arXiv_ALIGN_Scaling-Up-Visual-and-Vision-Language.md](./2021_arXiv_ALIGN_Scaling-Up-Visual-and-Vision-Language.md) | Main note body | classification loss and a text-to-image classification loss [10]. This effectively treats the noisy text as fine-grained labels, pushing the embeddings of matched image-text pairs closer together while pushing unmatched, random in-batch pairs apart [7, 10]. A learnable temperature parameter dynam... |
| [2022_ICML_NLS_To-Smooth-or-Not-Label-Smoothing-Noisy.md](./2022_ICML_NLS_To-Smooth-or-Not-Label-Smoothing-Noisy.md) | Summary | .27%. Clothing-1M: NLS 74.24% (4th among 21 methods) vs CE 68.94% vs LS 73.44%. CIFAR-10N Worst: NLS 82.99% vs CE 77.69% vs LS 82.76%. CIFAR-100N Fine: NLS 58.59% vs CE 55.50%. --- Paper's claimed novelty: First to formally define and analyze Negative Label Smoothing. Prior work (Lukasik 2020) sh... |
| [2022_NeurIPS_DST_Debiased-Self-Training.md](./2022_NeurIPS_DST_Debiased-Self-Training.md) | Summary | benchmarks from scratch; +18.9% vs FixMatch averaged over 13 fine-grained / scene / texture tasks with pre-training (supervised +19.9%, unsupervised +23.5% over FixMatch). CIFAR-100 / STL-10: +8.3% / +10.7% over FixMatch. Hardest 20 classes on CIFAR-100: mean acc 1.0% → 34.5% with DST. Training t... |
| [2023_ICML_TRAM++_When-Does-Privileged-Information-Explain-Away-Label-Noise.md](./2023_ICML_TRAM++_When-Does-Privileged-Information-Explain-Away-Label-Noise.md) | Summary | and mislabeled examples. TRAM++ appends a unique random D-dimensional vector to PI per sample. Combined methods: TRAM++ pre-training followed by SOP fine-tuning (TRAM+SOP). Main results: CIFAR-10H: TRAM++ 66.8% vs TRAM 64.9%; TRAM+SOP 70.9% vs SOP alone 59.2%. CIFAR-10N: TRAM++ 83.9% vs TRAM 80.5... |
| [2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md](./2024_ICLR_NMTune_Understanding-Mitigating-Label-Noise-Pre-training-Downstream-Tasks.md) | Summary | - NMTune: 2-layer MLP with three regularization terms (MSE consistency + covariance + dominant SVD) that reshapes the feature space without full fine-tuning Methodology: Pre-train ResNet-50 on synthetic noisy ImageNet-1K and YFCC15M at noise ratios 0-30%. Analyze feature space singular values. NM... |
| [2024_ICLR_RLHF_Understanding-Effects-RLHF-LLM-Generalisation-Diversity.md](./2024_ICLR_RLHF_Understanding-Effects-RLHF-LLM-Generalisation-Diversity.md) | Summary | Nalmpantis, Jelena Luketina, Eric Hambro, Edward Grefenstette, Roberta Raileanu Abstract: Comprehensive empirical analysis of how each stage of the RLHF fine-tuning pipeline (SFT, reward modeling, RLHF) affects out-of-distribution generalization and output diversity. Key finding: RLHF improves ge... |
| [2024_NeurIPS_DeFT_Vision-Language-Models-Strong-Noisy-Label-Detectors.md](./2024_NeurIPS_DeFT_Vision-Language-Models-Strong-Noisy-Label-Detectors.md) | Main note body | Models are Strong Noisy Label Detectors Authors: Tong Wei et al. Affiliation: (Multiple institutions) Code: https://github.com/HotanLee/DeFT ## Problem Fine-tuning vision-language models (e.g., CLIP) on noisy downstream datasets is challenging. Standard small-loss filtering (GMM, Co-teaching) fai... |
| [2024_arXiv_NA_High-Dimensional-Knowledge-Distillation-Weak-to-Strong.md](./2024_arXiv_NA_High-Dimensional-Knowledge-Distillation-Weak-to-Strong.md) | Summary | ) and \(n\) (target); synthetic experiments + CIFAR-10 fine-tune sanity check. Methodology: Gaussian covariates, diagonalizable covariances; ridgeless interpolators in overparam regime \(p>n\). Neural experiment: pretrained ResNet-50 target on CIFAR-10 vs three 3-layer CNN surrogates (big/medium/... |
| [2024_arXiv_NA_Review-Pseudo-Labeling-Computer-Vision.md](./2024_arXiv_NA_Review-Pseudo-Labeling-Computer-Vision.md) | Summary | Kage, Jay C. Rothenberger, Pavlos Andreadis, Dimitrios I. Diochnos Abstract: The paper argues “pseudo-labeling” is broader than classical semi-supervised fine-tuning: it formalizes pseudo-labels via fuzzy partitions / stochastic labels produced by neural nets, unifies SSL and parts of self-superv... |
| [2024_arXiv_RewardGeneralizationinRL_Reward-Generalization-in-RLHF-A-Topological.md](./2024_arXiv_RewardGeneralizationinRL_Reward-Generalization-in-RLHF-A-Topological.md) | Summary | , leaf-pair sampling) evaluated against chain-based RMs and DPO-style baselines. Methodology: Theoretical analysis plus empirical RLHF-style fine-tuning using tree-built preference datasets versus chain-built datasets; evaluation uses GPT-4 judging on held-out prompts across HH-RLHF, DialogSum, a... |
| [2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md](./2025_arXiv_FBR_Revisiting-Meta-Learning-Noisy-Labels-Reweighting-Dynamics.md) | Summary | Clothing1M, and CIFAR-N variants vs strong selection baselines; MW-Net shown to overfit badly under noise in reported tables. Methodology: Follows FINE’s experimental protocol backbone/hyperparameters (per paper text summarized by NLM); compares against broad baselines (Co-teaching(+), CRUST, FIN... |

---
## Meta Information

**Authors:** Taehyeon Kim, Jongwoo Ko, Sangwook Cho, Jinhwan Choi, Se-Young Yun  
**Affiliations:** KAIST AI  
**Venue:** NeurIPS 2021  
**Year:** 2021  
**PDF:** available at arxiv.org/pdf/2102.11628  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** e2306076-d5e1-4287-a0d2-417641e7f656
