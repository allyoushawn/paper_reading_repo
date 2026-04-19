# Paper Analysis: Which is Better for Learning with Noisy Labels: The Semi-supervised Method or Modeling Label Noise?

**Source:** https://proceedings.mlr.press/v202/yao23a/yao23a.pdf  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Which is Better for Learning with Noisy Labels: The Semi-supervised Method or Modeling Label Noise?  
**Authors:** Yu Yao, Mingming Gong, Yuxuan Du, Jun Yu, Bo Han, Kun Zhang, Tongliang Liu  
**Abstract:** Answers the question of when to use SSL-based vs. model-based methods for noisy label learning from the perspective of causal data generative processes. If X causes Y (causal), P(X) contains no labeling information and SSL fails; if Y causes X (anticausal), SSL succeeds. Proposes CDNL, a causal structure discovery method for noisy datasets that exploits an asymmetric property of flip-rate estimation under different causal structures.

**Key contributions:**
- Causal framework: when X→Y, SSL-based methods suffer from data sacrifice and are dominated by model-based methods; when Y→X, SSL-based methods substantially outperform model-based ones
- CDNL estimator: automatically discovers causal structure by comparing P(Ỹ|Y') (from unsupervised clustering) with P(Ỹ|Y*) (from end-to-end Bayes label learning); if estimation distance ≤ 0.05, dataset is anticausal
- Superior flip-rate estimation: CDNL estimation error near 0 across noise rates vs. VolMinNet which has substantially higher error
- First causal discovery method for datasets containing noisy labels

**Methodology:**  
CDNL three-step algorithm: (1) estimate P(Ỹ|Y*) via trainable column-stochastic matrix A with Gumbel-Softmax constraint; (2) estimate P(Ỹ|Y') via unsupervised clustering (K-means or SPICE) + Hungarian assignment; (3) compare distance between two estimates to classify as causal or anticausal.

**Main results:**  
Causal (X→Y) datasets: T-Revision 79.06% vs. DivideMix 63.94% on KrKp with IDN-40%. Anticausal (Y→X) datasets: DivideMix 94.50% vs. Forward 74.72% on CIFAR-10 with IDN-40%. CDNL correctly identifies causal structure on 6/6 real datasets; PC and GIES algorithms fail on several. CDNL estimation error ≈ 0 vs. VolMinNet high error on synthetic datasets.

---

## 2. Experiment Critique

**Design:**  
Systematic evaluation across 2 synthetic datasets (XYgaussian, YXgaussian) and 6 real-world datasets (KrKp, Balancescale, Splice, Waveform, MNIST, CIFAR10). Three noise types (symmetric, pair, instance-dependent). Both model-based and SSL-based baselines evaluated. Causal discovery comparison with PC and GIES provides a strong ablation for the discovery mechanism.

**Statistical validity:**  
Mean ± std reported. Multiple seeds. The 0.05 threshold for causal/anticausal classification is empirically motivated rather than theoretically derived, which is a limitation.

**Online experiments (if any):**  
None.

**Reproducibility:**  
Code implemented in PyTorch. SPICE clustering for CIFAR10 (requires separate pre-training). Baseline MoPro required modification for non-image datasets (small Gaussian noise substituted for image augmentations), which may affect its performance. Full hyperparameter tables documented.

**Overall:**  
Strong theoretical insight that resolves a longstanding practical dilemma. The empirical demonstration is convincing for both synthetic and real-world datasets. Key limitation: the Waveform anticausal dataset is a failure case (CDNL produces large estimation error), suggesting the method's reliability depends on how much labeling information P(X) actually contains. High sample complexity of model-based methods under high-dimensional data limits their practical applicability.

---

## 3. Industry Contribution

**Deployability:**  
The CDNL estimator provides a diagnostic tool: run it before training to determine which type of method to invest in. This saves significant compute for model selection. In proxy-label learning, the attribution-label dataset almost certainly falls in the anticausal regime (Y causes X when X is user behavior features and Y is the label derived from downstream conversion), making SSL-based methods the preferred choice.

**Problems solved:**  
Resolves the "which method to use" dilemma by grounding it in causal theory. Provides theoretical justification for why DivideMix-style SSL methods dominate leaderboards on image datasets (Y causes X in image classification).

**Engineering cost:**  
Moderate. CDNL requires training a classification network (for P(Ỹ|Y*)) and running unsupervised clustering (for P(Ỹ|Y')). One-time diagnostic cost before choosing the training strategy.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First theoretical analysis of when SSL vs. model-based methods should be preferred for noisy labels, grounded in causality. First causal discovery method for noisy label datasets. No prior work differentiated between causal and anticausal regimes in the noisy labels context.

**Prior work comparison:**  
Patrini et al. 2017 (Forward): model-based baseline. Li et al. 2020 (DivideMix): SSL baseline. Schölkopf et al. 2012, Peters et al. 2017: causal modularity theory. VolMinNet (Li et al. 2021): prior SOTA for flip-rate estimation, shown to be inferior to CDNL.

**Verification:**  
UCSC + CMU + Sydney AI Centre + Hong Kong Baptist University, ICML 2023.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| XYgaussian / YXgaussian | synthetic | Yes | 2D Gaussian, code-generated |
| KrKp, Balancescale, Splice, Waveform | UCI | Yes | Tabular classification |
| MNIST | public | Yes | Anticausal |
| CIFAR-10 | public | Yes | Anticausal |

**Offline experiment reproducibility:**  
High. SPICE clustering pre-training may require additional setup for CIFAR-10 experiments.

---

## 6. Community Reaction

UCSC + CMU + Sydney AI Centre + HKBU, ICML 2023. The causal framing of the SSL vs. model-based debate is considered a foundational theoretical contribution. The practical implication (most image classification datasets are anticausal → prefer DivideMix-style methods) is widely resonant.

**Relevance to proxy-label learning:** Core. Attribution-based proxy label datasets are almost certainly anticausal (label derives from behavior features), validating SSL-based methods. The CDNL estimator can serve as a quick diagnostic on any new proxy label dataset.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Yu Yao, Mingming Gong, Yuxuan Du, Jun Yu, Bo Han, Kun Zhang, Tongliang Liu  
**Affiliations:** University of California Santa Cruz; Carnegie Mellon University; Sydney AI Centre, University of Sydney; Hong Kong Baptist University  
**Venue:** ICML 2023  
**Year:** 2023  
**PDF:** available at proceedings.mlr.press/v202/yao23a/yao23a.pdf  
**Relevance:** Core  
**Priority:** 1  
**NLM Source ID:** f155dd5a-9689-4c8c-b707-a78967c559af
