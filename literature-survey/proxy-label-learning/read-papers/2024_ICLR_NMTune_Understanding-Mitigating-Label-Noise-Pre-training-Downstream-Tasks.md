# Paper Analysis: Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks

**Source:** https://arxiv.org/pdf/2309.17336  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Understanding and Mitigating the Label Noise in Pre-training on Downstream Tasks  
**Authors:** Hao Chen, Jindong Wang, Ankit Shah, Ran Tao, Hongxin Wei, Xing Xie, Masashi Sugiyama, Bhiksha Raj  
**Abstract:** Proposes Noisy Model Learning (NML), a new research direction studying how label noise in pre-training datasets affects downstream task performance. Discovers that slight noise (5-10%) can benefit in-domain performance while consistently hurting out-of-domain robustness. Proposes NMTune, a lightweight black-box feature space tuning method using singular value regularization.

**Key contributions:**
- Introduces Noisy Model Learning (NML) — distinct from classic noisy label learning (which targets training from scratch)
- Finding: 5-10% pre-training noise benefits in-domain downstream accuracy but always hurts OOD robustness
- Analysis: noise flattens the singular value spectrum of the feature space, reducing the dominant singular value and degrading OOD transferability
- NMTune: 2-layer MLP with three regularization terms (MSE consistency + covariance + dominant SVD) that reshapes the feature space without full fine-tuning

**Methodology:**  
Pre-train ResNet-50 on synthetic noisy ImageNet-1K and YFCC15M at noise ratios 0-30%. Analyze feature space singular values. NMTune adds a 2-layer MLP transformation with regularization: L = L_CE + λ(L_MSE + L_COV + L_SVD). λ=0.01 throughout.

**Main results:**  
Swin-L (ImageNet-21K): NMTune achieves 84.16% ID / 52.35% OOD vs LP's 81.91% / 50.88%. ConvNext-L (LAION-2B): OOD 70.30% vs LP's 66.86%. BERT-L OOD on GLUE-X: 51.63% vs LP's 50.65%. OpenAI text-ada-002 API OOD: 53.48% vs LP's 44.06% (notable gain on a black-box API).

---

## 2. Experiment Critique

**Design:**  
Both controlled synthetic noise experiments (ResNet-50, 5 noise levels) and validation on practical large-scale noisy pre-trained models (JFT-300M, ImageNet-21K, LAION-2B, BERT/GPT-2). 14 ID + 4 OOD vision benchmarks; GLUE + GLUE-X for language.

**Statistical validity:**  
Results for vision reported without standard deviations in main tables. The black-box API experiment (text-ada-002) has limited reproducibility but demonstrates the most practical value.

**Online experiments (if any):**  
None. All offline.

**Reproducibility:**  
Code available. ResNet-50 experiments are reproducible. Experiments on larger backbones require significant compute. Failure on Caltech101 documented.

**Overall:**  
Novel framing and solid empirical validation. Key limitation is that analytical experiments are restricted to ResNet-50 due to compute constraints. Failure on Caltech101 (SVD regularization needs per-dataset K tuning) is acknowledged. Doesn't outperform white-box fine-tuning.

---

## 3. Industry Contribution

**Deployability:**  
High relevance for production ML: when using pre-trained models from large noisy datasets (common in industry), NMTune offers a cheap black-box fix. The approach of treating model noise as a feature space distortion is novel and practically actionable. Can be applied even to API-only models.

**Problems solved:**  
In proxy-label settings, models pre-trained on implicit behavioral signals (clicks, attributions) experience exactly this noise pattern — slight noise may benefit in-distribution but hurt OOD. NMTune's singular value regularization could correct this without requiring access to pre-training data.

**Engineering cost:**  
Very low. A 2-layer MLP adapter with three regularization terms adds negligible compute overhead. Works as a drop-in for any frozen feature extractor.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First study of label noise in pre-training affecting downstream performance. Classic noisy label learning (DivideMix, ELR, Co-teaching) focuses on training from scratch. NML is a different problem — the noisy pre-trained model is the starting point, and downstream data may be clean.

**Prior work comparison:**  
The feature space analysis draws on Chen et al. 2019 (singular value transferability) and Zbontar et al. (covariance regularization). NMTune is analogous to adapter-style fine-tuning but motivated by noise analysis rather than domain adaptation.

**Verification:**  
CMU + Microsoft Research Asia affiliation, ICLR 2024.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| ImageNet-1K | standard | Yes | Controlled noise injection |
| YFCC15M | public | Yes | CLIP pre-training |
| DomainNet (4 splits) | public | Yes | OOD vision |
| GLUE / GLUE-X | public | Yes | Language ID/OOD |

**Offline experiment reproducibility:**  
High for standard benchmarks. Large backbone experiments require significant compute.

---

## 6. Community Reaction

ICLR 2024 paper from CMU + MSR Asia. Introduces a novel framing that connects pre-training data quality to downstream OOD robustness. The black-box API result (text-ada-002) makes it practically compelling. The singular value analysis provides an interpretable diagnostic tool.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Hao Chen, Jindong Wang, Ankit Shah, Ran Tao, Hongxin Wei, Xing Xie, Masashi Sugiyama, Bhiksha Raj  
**Affiliations:** Carnegie Mellon University; Microsoft Research Asia; SusTech; RIKEN AIP; University of Tokyo  
**Venue:** ICLR 2024  
**Year:** 2024  
**PDF:** available at arxiv.org/pdf/2309.17336  
**Relevance:** Related  
**Priority:** 2  
**NLM Source ID:** ad483e56-72bc-4349-a91c-3600a0b014b9
