# Paper Analysis: Neural Relation Graph: A Unified Framework for Identifying Label Noise and Outlier Data

**Source:** https://arxiv.org/pdf/2301.12321  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Neural Relation Graph: A Unified Framework for Identifying Label Noise and Outlier Data  
**Authors:** Jang-Hyun Kim, Sangdoo Yun, Hyun Oh Song  
**Abstract:** Proposes the Neural Relation Graph, a unified post-hoc framework for identifying label errors and outlier data in large-scale datasets. Instead of relying on unary scores (loss, margin, TracIn), the method measures relational structure by comparing feature embeddings and assigned labels separately. A max-cut algorithm identifies noisy subsets globally; an aggregated similarity score identifies outliers. Achieves SOTA on ImageNet (8% noise), ESC-50, and SST2 across image, speech, and language domains.

**Key contributions:**
- Relation function r((xi,yi),(xj,yj)) = 1(yi=yj) · |s(fi,fj) · c(pi,pj)|^t — separates feature similarity from label consistency; values >0 mean "consistent", <0 mean "conflicting"
- Max-cut formulation for label noise detection: partitions training set into noisy subset N and clean subset T\N by maximizing conflicting edges minus λ|N| regularization; solved via efficient set-level Kernighan-Lin algorithm
- Outlier detection: aggregated inverse similarity score outlier(x) = 1/Σ_S k(x,xi); works with 1% random sample (0.4% of ImageNet)
- Data relation map visualization: scatter plot of (mean relation, variance of relation) across checkpoints — clean/error/outlier show distinct signatures
- Domain-agnostic: same framework applied to images, speech (ESC-50), and text (SST2/MNLI) without modification

**Methodology:**  
Feature extractor: MAE-Large/Base, BEIT, ConvNeXt, AST (audio), RoBERTa (text). Algorithm 1 runs in 420s on full ImageNet 1.2M. Temperature t controls kernel sharpness. λ controls noisy subset size. Code released on GitHub.

**Main results:**  
ImageNet 8% noise: Relation AP 0.526, TNR95 0.695 vs Margin (best baseline) AP 0.484, TNR95 0.521. ESC-50 (10% noise): AP 0.779 vs baseline 0.739. SST2 (10% noise): AP 0.881 vs baseline 0.861. OOD on ImageNet-100 (iNaturalist): AUROC 0.995, AP 0.940 vs KNN AUROC 0.993, AP 0.923. Robust to 1% data subsample.

---

## 2. Experiment Critique

**Design:**  
Multi-domain evaluation (images, speech, language) is a strong contribution. Multiple architectures tested (MAE-Base/Large, BEIT, ConvNeXt, AST, RoBERTa). Computation time comparison vs TracIn is rigorous and practically important. Ablation on λ, temperature t, kernel design (cosine vs RBF), and data subset size. Both AP and TNR95 metrics used for label noise; AUROC, AP, TNR95 for OOD.

**Statistical validity:**  
Results reported across multiple checkpoints (convergence tracking). Performance reported at 5k, 24k, 120k, 1.2M data points for scalability validation. Statistical dispersion not prominently reported (near-deterministic post-hoc method).

**Online experiments (if any):**  
None.

**Reproducibility:**  
Code publicly available at github.com/snu-mllab/Neural-Relation-Graph. Algorithm 1 fully specified. Hyperparameter tables (t, λ) documented.

**Overall:**  
Strong paper with practical applicability. Key limitation: performance drops after 30 epochs due to memorization — must apply at the right training stage. Detection limited to classification tasks. Simple edge aggregation fails; global max-cut required.

---

## 3. Industry Contribution

**Deployability:**  
High. Post-hoc analysis tool requiring only one trained model's features and predictions. No retraining. Can run on any classification model at any point in training. Particularly useful as a dataset auditing tool before deployment.

**Problems solved:**  
In proxy-label learning: enables auditing of proxy label datasets for systematic errors (label noise vs. outliers) using a trained model's relational structure. The separation of feature similarity from label comparison is directly applicable to identifying annotation errors in attribution-based labels.

**Engineering cost:**  
Low. Requires feature extraction (reuses existing model), then ~420s for Algorithm 1 on ImageNet 1.2M. Memory scales with graph size but 1% sampling maintains performance.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First unified framework handling both label noise and outlier detection with a single relational structure. Prior methods (TracIn, margin, loss) are unary and cannot distinguish label error from outlier. The max-cut formulation for noisy subset extraction is novel in the noisy label context.

**Prior work comparison:**  
Northcutt et al. 2021 (Confident Learning): confident learning uses class probability estimates for label noise — unary, no OOD. Pruthi et al. 2020 (TracIn): influence-based, computationally expensive (21,000s vs 420s), sensitive to outliers. Pleiss et al. 2020 (AUM): tracks margins over training, not relational. Sun et al. 2022 (KNN OOD): local k-nearest distance only — NRG uses global graph.

**Verification:**  
Seoul National University + NAVER AI Lab, NeurIPS 2023. Affiliation with NAVER (major Korean tech company) satisfies big-tech criteria. Code released.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| ImageNet | public | Yes | 1.2M images, 1000 classes, artificially noised |
| ESC-50 | public | Yes | Environmental audio, 50 classes, AST model |
| SST2 / MNLI | public | Yes | Text classification, RoBERTa |
| Places, SUN, iNaturalist, Textures | public | Yes | OOD benchmark datasets |

**Offline experiment reproducibility:**  
High. Code and hyperparameter tables released. Algorithm 1 runs in minutes.

---

## 6. Community Reaction

Seoul National University + NAVER AI Lab, NeurIPS 2023. Well-received for its practical utility and multi-domain generalizability. The data relation map visualization tool attracted interest as a dataset diagnostic. The 50x speedup over TracIn for large-scale label cleaning is widely noted.

**Relevance to proxy-label learning:** Related. The relational graph approach is applicable to any label-noise dataset. Particularly useful for diagnosing proxy label quality at scale.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Jang-Hyun Kim, Sangdoo Yun, Hyun Oh Song  
**Affiliations:** Seoul National University; NAVER AI Lab  
**Venue:** NeurIPS 2023  
**Year:** 2023  
**PDF:** available at arxiv.org/pdf/2301.12321  
**Relevance:** Related  
**Priority:** 1  
**NLM Source ID:** 20ee0a6b-c77d-4971-9924-677a404fbb0f
