Date: 2026-04-12  
Source: https://arxiv.org/pdf/2402.17517 (ingested; OpenReview PDF `I5JBFKNTQW` returned HTTP 403 to automated fetchers)  
NLM Source ID: 3b06d77d-7bb4-4ce7-8f7c-c1739f22ffd0  
Venue: ICLR 2024  
Relevance: Related  
Priority: 2

# Paper Analysis: Label-Noise Robust Diffusion Models (TDSM)

**Source:** https://arxiv.org/pdf/2402.17517  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Label-Noise Robust Diffusion Models

**Authors:** Byeonghu Na, Yeongmin Kim, HeeSun Bae, Jung Hyun Lee, Se Jung Kwon, Wanmo Kang, Il-Chul Moon (KAIST; NAVER Cloud; summary.ai)

**Abstract:**  
Conditional diffusion models trained with noisy labels learn a **noisy-label conditional score**, producing **class mismatch** and degraded sample quality. The paper proposes **Transition-aware weighted Denoising Score Matching (TDSM)**: under class-conditional label noise, the noisy-label score is a **convex combination** of clean-class scores with **instance- and time-dependent** weights. A **time-dependent noisy-label classifier** plus (estimated) transition structure implements the weights. Optional **affine score** inference reduces mismatched outliers.

**Key contributions:**
- Theory: **Theorem 1** linking noisy- vs clean-label conditional scores via weights \(w(x_t,\tilde y,y,t)\) interpretable as \(p_t(Y=y\mid \tilde Y=\tilde y, x_t)\).
- Training objective **TDSM**: match perturbed data score to **weighted sum** of per-class score network outputs.
- Practical speed/memory tricks: **skip threshold** \(\tau\) on tiny weights; backprop mainly through noisy-label channel; combines with **VolMinNet / DISC** correctors.

**Methodology:**  
EDM-style diffusion backbone; synthetic symmetric/asymmetric noise on MNIST/CIFAR; **Clothing-1M** real noise evaluation; compares to DSM and robust GAN baselines.

**Main results:**  
Example: CIFAR-10 40% symmetric noise: **CW-FID 30.45 → 15.92** and **CAS 47.21% → 62.28%** (DSM vs TDSM) in-source; **Clothing-1M** **FID 6.67 → 4.94**, **CAS 46.52 → 47.79**; strong gains under **80%** noise in severe-noise table excerpt.

---

## 2. Experiment Critique

**Design:**  
Uses both unconditional and **class-wise (CW-)** metrics to separate sample quality from conditional alignment; includes pipeline combining with external label correctors.

**Statistical validity:**  
Standard generative metrics (FID/IS/Density/Coverage + CW variants + CAS). Multiple tables across noise rates.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
Code link in abstract (`byeonghu-na/tdsm`); relies on EDM codebase and classifier training schedules; transition matrix estimation can use VolMinNet.

**Overall:**  
The paper is careful to show **S-weighted DSM** (instance-independent GAN-style weighting) **does not** recover clean scores (differs from GAN setting) — an important negative result for method transfer.

---

## 3. Industry Contribution

**Deployability:**  
Relevant to generative pipelines trained on **weak labels** (catalog tags, heuristic classifiers). Affine score trick targets “hard” mismatch outliers at inference.

**Problems solved:**  
Reduces **conditional mismatch** from label noise in diffusion training; orthogonal to classifier-only denoising.

**Engineering cost:**  
TDSM requires multi-class score evaluations per step (mitigated by skipping low weights); still heavier than standard DSM.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
First diffusion-focused theory + training remedy for class-conditional label noise; emphasizes **time-dependent** transition structure unlike GAN robustness tricks.

**Prior work comparison:**  
Compares to **Kaneko et al.** / **Thekumparampil et al.** robust conditional GANs; builds on **Song/Ho/Karras EDM** line.

**Verification:**  
Claims are supported by synthetic toy visualizations and benchmark tables in-source; real-world section acknowledges limitations of class-conditional assumption.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| MNIST / CIFAR-10 / CIFAR-100 | Public | Yes | Synthetic noise |
| Clothing-1M | Public benchmark | Yes | ~61.5% label accuracy noted in-source |

**Offline experiment reproducibility:**  
Standard; Clothing-1M setup follows prior noisy-label generative work (Kaneko et al. protocol excerpt).

---

## 6. Community Reaction

No significant HN/Reddit thread surfaced in the quick title-targeted search for this paper. **No significant community discussion found** in the scan performed for this batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Byeonghu Na et al.  
**Affiliations:** KAIST; NAVER Cloud; summary.ai  
**Venue:** ICLR 2024  
**Year:** 2024  
**PDF:** downloaded (arXiv; OpenReview mirror blocked with 403 in this environment)  
**Relevance:** Related  
**Priority:** 2

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
