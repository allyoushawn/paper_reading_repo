# Paper Analysis: Generalized Jensen-Shannon Divergence Loss for Learning with Noisy Labels

**Source:** https://arxiv.org/pdf/2105.04522  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Generalized Jensen-Shannon Divergence Loss for Learning with Noisy Labels  
**Authors:** Erik Englesson, Hossein Azizpour  
**Abstract:** Proposes using Jensen-Shannon divergence as a noise-robust loss function, proving it interpolates between CE and MAE via a controllable mixing parameter π₁. Introduces GJS, a multi-distribution generalization that incorporates built-in consistency regularization by applying GJS across M augmented views of each input. Achieves SOTA on both synthetic and real-world noise benchmarks with a single simple loss function, outperforming complex multi-network pipelines like DivideMix on WebVision top-1.

**Key contributions:**
- JS loss: theoretically shown to interpolate between CE (π₁→0) and MAE (π₁→1); symmetric and bounded unlike GCE/SCE
- GJS loss: extends JS to M distributions; decomposes into (a) JS term between label and mean prediction, (b) consistency term encouraging all perturbed predictions to agree
- M=3 recommendation: 2 augmented predictions + label; M>3 degrades at high noise rates
- Ensemble of 2 GJS networks sets SOTA on WebVision/ILSVRC12 without pretraining (79.28% / 75.50% top-1)
- Theoretical robustness proof: GJS is noise-robust at limit π₁→1; practical robustness attributed to consistency term (not yet formally proven)

**Methodology:**  
Loss: L_GJS(e(y), p^(2), ..., p^(M)) decomposes into L_JS between label and mean prediction plus (1-π₁)·L_GJS(p^(2),...,p^(M)). π₁ and M are tuned per dataset. ResNet-34 for CIFAR, ResNet-50 for WebVision. 5 runs per experiment. Hyperparameter grid search documented.

**Main results:**  
CIFAR-10 Sym-60%: GJS 91.64% vs CE 81.99%, GCE 89.37%. CIFAR-100 Sym-60%: GJS 70.15% vs GCE 65.21% (+4.94pp). CIFAR-100 Sym-80%: GJS 44.49% vs GCE 49.68% (worse — known failure at extreme noise). WebVision top-1: GJS (single) 77.99% vs DivideMix 77.32%; GJS (2-net ensemble) 79.28%. ILSVRC12 top-1: GJS 74.33% vs ELR+ 70.29%. ANIMAL-10N: GJS 84.2% vs PLC 83.4%. Food-101N: GJS 86.56% vs PLC 85.28%.

---

## 2. Experiment Critique

**Design:**  
Systematic and thorough. Reimplements all baselines (LS, BS, SCE, GCE, NCE+RCE) in the same setup for fair comparison. Ablation studies cover π₁ variation, M variation, epoch count, and dataset difficulty. The WebVision comparison with multi-network pipelines is clearly contextualized (different architecture, augmentation, network count). Instance-dependent noise experiments in appendix extend the synthetic noise coverage.

**Statistical validity:**  
5 runs per experiment, mean ± std reported. Statistically significant top performers boldfaced. The comparison against DivideMix on WebVision acknowledges setup differences (Inception-ResNet-V2 vs ResNet-50, Mixup vs color jitter).

**Online experiments (if any):**  
None.

**Reproducibility:**  
Code publicly available. Hyperparameter tables (π₁, LR, weight decay) fully documented per dataset and noise type. M=3 used consistently; only π₁ needs tuning.

**Overall:**  
Strong contribution. Results clearly support the "bounded loss + consistency regularization" claim. Key limitation: no theoretical proof of the consistency term's robustness; GJS underperforms GCE at extreme (80%) CIFAR-100 noise; computational overhead from M forward passes.

---

## 3. Industry Contribution

**Deployability:**  
Highly deployable. GJS is a drop-in loss function replacement — no architectural changes, no multi-network complexity. M=3 adds one extra forward pass per training step. Minimal hyperparameter burden (π₁ and M).

**Problems solved:**  
In proxy-label learning: GJS provides a theoretically motivated alternative to CE for noisy proxy labels without requiring pipeline changes. The consistency regularization is particularly relevant when proxy labels are noisy — it encourages stable predictions across augmented inputs, reducing reliance on specific noisy label assignments.

**Engineering cost:**  
Low. One extra forward pass for M=3. π₁ requires tuning (grid over ~10 values). No new infrastructure needed.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First to use JS divergence as a noise-robust loss function with theoretical interpolation proof between CE and MAE. GJS uniquely generalizes to M>2 distributions with varying π₁, unlike concurrent Wei & Liu 2021 work (f-divergences, fixed π₁=0.5, M=2 only). Built-in consistency regularization as a principled derivation from the GJS decomposition is novel.

**Prior work comparison:**  
Ghosh et al. 2017 (MAE robustness theory): theoretical foundation used directly. Zhang & Sabuncu 2018 (GCE): GJS shown to outperform on most settings. Wang et al. 2019 (SCE): different interpolation mechanism, not bounded. Ma et al. 2020 (NCE+RCE): normalization vs. divergence approach. Concurrent: Wei & Liu 2021 (f-divergences for noisy labels) — GJS explored M>2 and variable π₁ which their work did not.

**Verification:**  
KTH Stockholm, NeurIPS 2021. Well-cited. The WebVision SOTA claim (no pretraining) is verifiable from the paper's tables.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10/100 (synthetic) | public | Yes | Sym/asym/instance-dep. noise |
| mini WebVision | public | Yes | First 50 classes, Google subset |
| ANIMAL-10N | public | Yes | Real-world noise, human labeling |
| Food-101N | public | Yes | Real-world noise, ~20% estimate |

**Offline experiment reproducibility:**  
High. Code and hyperparameter tables released.

---

## 6. Community Reaction

KTH Stockholm, NeurIPS 2021. Well-received as a principled and elegant contribution to the robust loss function literature. The WebVision SOTA claim with a single-network approach attracted significant attention. The JS-CE-MAE interpolation analysis is widely cited in subsequent noisy label papers.

**Relevance to proxy-label learning:** Core. GJS is a practical, zero-cost improvement for any noisy proxy label training pipeline.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Erik Englesson, Hossein Azizpour  
**Affiliations:** KTH Royal Institute of Technology, Stockholm  
**Venue:** NeurIPS 2021  
**Year:** 2021  
**PDF:** available at arxiv.org/pdf/2105.04522  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** 3d7a576f-9bdb-4509-bfb6-8d04f96b7b09
