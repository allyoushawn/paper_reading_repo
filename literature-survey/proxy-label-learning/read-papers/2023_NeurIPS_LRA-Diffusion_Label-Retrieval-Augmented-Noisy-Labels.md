Date: 2026-04-12  
Source: https://arxiv.org/pdf/2305.19518 (canonical NeurIPS PDF; queue previously listed `2305.03483`, which resolves to an unrelated math.AC preprint)  
NLM Source ID: 6cc17df9-9885-4d27-a16e-c1d61152bb09  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: NeurIPS 2023  
Relevance: Related  
Priority: 2

# Paper Analysis: Label-Retrieval-Augmented Diffusion Models for Learning from Noisy Labels

**Source:** https://arxiv.org/pdf/2305.19518  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Label-Retrieval-Augmented Diffusion Models for Learning from Noisy Labels

**Authors:** Jian Chen, Ruiyi Zhang, Tong Yu, Rohan Sharma, Zhiqiang Xu, Tong Sun, Changyou Chen (Buffalo / Adobe / MBZUAI)

**Abstract:**  
Reframes learning with noisy labels as **conditional label generation**: start from a noisy label guess and denoise toward the clean label using a diffusion model. Because training cannot trust per-example labels, the method retrieves **neighbor labels** in a frozen representation space to build **pseudo-clean targets** (**Label-Retrieval-Augmented**, LRA). Supports strong pretrained encoders (SimCLR, CLIP) and accelerated sampling via a **generalized DDIM** in a non-zero-mean latent.

**Key contributions:**
- **LRA-diffusion**: train label diffusion on retrieved neighbor labels (neighbor consistency) rather than only the corrupted label.
- **Efficient inference**: generalized **DDIM** with few steps (e.g., **S=10, T=1000** in-source) + a deterministic mean-start trick for approximate MLE.
- **Strong empirical results** on synthetic PMD/hybrid noise and real-world noisy benchmarks; large gains when conditioning on **CLIP** features.

**Methodology:**  
Two encoders: \(f_q\) (mean estimator / initial label guess; sometimes set to 0) and \(f_p\) (feature extractor for retrieval + conditioning). Network: frozen \(f_p\), trainable ResNet encoder (34/50) + MLP heads predicting noise \(\epsilon_\theta\). Training samples retrieved neighbor labels and mixes targets; compares against many noisy-label baselines.

**Main results:**  
Examples in-source: **LRA-diffusion (CLIP)** reaches **96.54%** on CIFAR-10 under 35% PMD vs **C2D+SimCLR 85.61%**; **84.16%** WebVision and **82.56%** ILSVRC12 vs strong EPL pipeline; **93.42%** on Food-101N.

---

## 2. Experiment Critique

**Design:**  
Broad benchmark coverage (synthetic PMD + hybrid i.i.d noise; real web noise datasets). Many SOTA baselines listed in-source tables.

**Statistical validity:**  
Multiple seeds reported for key tables (means ± std shown in-source excerpts).

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
GitHub referenced in abstract (`puar-playground/LRA-diffusion`); relies on pretrained CLIP/SimCLR weights and kNN retrieval hyperparameters.

**Overall:**  
Claims of “SOTA everywhere” are supported within the paper’s experimental matrix, but authors also document regimes where assumptions break (very high noise; weak features).

---

## 3. Industry Contribution

**Deployability:**  
Conceptually relevant when labels are cheap but wrong (web tags, weak supervision) and a strong pretrained encoder exists (CLIP-like).

**Problems solved:**  
Improves **proxy label / noisy label** classification by combining retrieval pseudo-targets with generative uncertainty modeling.

**Engineering cost:**  
Diffusion training/inference is heavier than thresholded pseudo-labeling, though DDIM reduces steps; retrieval adds index/neighbor search overhead each step.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
Generative (diffusion) framing + retrieval augmentation for noisy labels; integration with large pretrained vision encoders.

**Prior work comparison:**  
Builds on **CARD**-style classification diffusion; compares to **DivideMix**, **UNICON**, **PLC**, **C2D**, **EPL**, etc.

**Verification:**  
NeurIPS publication and public code listing improve confidence in reproducibility of headline numbers, but full replication remains effortful.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CIFAR-10/100 | Public | Yes | Synthetic noise protocols |
| WebVision / ILSVRC12 / Food-101N / Clothing1M | Public / standard noisy-label benchmarks | Mostly yes | Clothing1M domain issues noted in-source |

**Offline experiment reproducibility:**  
Standard datasets; noise generation details reference prior work (PLC PMD protocol).

---

## 6. Community Reaction

The paper has a **PapersWithCode** page and a public GitHub implementation (seen via web index during batch). No focused viral HN/Reddit thread was found in the quick search. **No significant community discussion found** beyond standard indexing/repo presence.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Jian Chen et al.  
**Affiliations:** University at Buffalo; Adobe Research; MBZUAI  
**Venue:** NeurIPS 2023  
**Year:** 2023  
**PDF:** downloaded (arXiv `2305.19518`)  
**Relevance:** Related  
**Priority:** 2

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
