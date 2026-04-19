Date: 2026-04-12  
Source: https://arxiv.org/pdf/1901.04215.pdf  
NLM Source ID: `ee595b51-c309-408d-9e74-a8ffcc4e92b8`  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: ICML 2019  
Relevance: Core  
Priority: 2

# Paper Analysis: How does Disagreement Help Generalization against Label Corruption? (Co-teaching+)

**Source:** https://arxiv.org/pdf/1901.04215.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** How does Disagreement Help Generalization against Label Corruption?

**Authors:** Xingrui Yu, Bo Han, Jiangchao Yao, Gang Niu, Ivor W. Tsang, Masashi Sugiyama

**Abstract:**  
**Co-teaching** trains two networks with the small-loss trick and cross-updates peer-selected examples, but the two networks **converge to agreement** over epochs, degenerating toward **self-training / MentorNet** behavior and accumulating errors. **Co-teaching+** keeps disagreement by (1) filtering each mini-batch to **prediction-disagreement** examples, then (2) selecting **small-loss** examples within that disagreement pool, but **backpropagating peer-selected** small-loss instances (cross-update). A schedule \(\lambda(e)\) controls how many small-loss points are kept as training progresses.

**Key contributions:**
- Introduces **Co-teaching+** bridging **Update-by-Disagreement** (Decoupling; Malach & Shalev-Shwartz) with Co-teaching’s cross-peer filtering.
- Summarizes three empirical “key factors” for robustness: **small-loss selection**, **cross-update**, **maintained divergence**.
- Evaluates on synthetic noise (symmetric + pair flipping) and **open-set** noisy CIFAR-10 replacements (Wang et al. protocol).

**Methodology:**  
Two networks; per batch disagreement mask \(\{(x_i,y_i): \hat{y}^{(1)}_i \neq \hat{y}^{(2)}_i\}\); small-loss subsets within disagreement; cross-gradient updates; \(\lambda(e)\) decay variants (fast early decay + later slow decay to cope with inaccurate noise-rate estimates).

**Main results:**  
Examples: **Tiny-ImageNet** sym **50%**: Co-teaching+ max acc **41.77%** vs Co-teaching **37.60%** vs MentorNet **35.76%** (per extracted table snippet). **Open-set** CIFAR-10+SVHN **40%** noise: Co-teaching+ max **80.95%** vs Iterative **77.73%** vs MentorNet max **79.81%**. Shows **F-correction** can fail under harder pair/sym noise and can fail across conditions on **NEWS** in their setting.

---

## 2. Experiment Critique

**Design:**  
Strong baseline coverage: Standard, MentorNet, Co-teaching, Decoupling, F-correction (Patrini et al.), plus open-set iterative baseline from Wang et al.

**Statistical validity:**  
Reports averaged/max over last 10 epochs for some settings (open-set table); synthetic experiments cover multiple noise regimes.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
PyTorch, default parameters stated; architectures vary by dataset (MLP MNIST; conv nets CIFAR; Pre-act ResNet-18 Tiny-ImageNet; GloVe+MLP NEWS).

**Overall:**  
Method depends on **warm-up** schedules for harder datasets (e.g., delay disagreement-update for T-ImageNet / Open-sets) and can fall back to disagreement-only update if insufficient small-loss points exist—authors disclose these operational details.

---

## 3. Industry Contribution

**Deployability:**  
2× training cost vs single network; useful when label corruption is pervasive and peer disagreement is a cheap signal for denoising dynamic training batches.

**Problems solved:**  
Mitigates **consensus collapse** in dual-network small-loss training under label noise.

**Engineering cost:**  
Moderate: two models + careful scheduling; needs noise-rate estimate for \(\lambda(e)\) scheduling (authors discuss inaccuracy).

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
Unifies disagreement-based divergence control with Co-teaching’s robust peer filtering.

**Prior work comparison:**  
Builds on **Han et al. Co-teaching**, **Jiang et al. MentorNet**, **Malach & Shalev-Shwartz Decoupling**, **Blum & Mitchell co-training intuition**, **Patrini et al. F-correction**, **Wang et al. open-set noise** setting.

**Verification:**  
Not independently verified beyond NotebookLM extraction.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| MNIST / CIFAR-10 / CIFAR-100 | Public | Yes | Synthetic noise |
| Tiny-ImageNet | Public | Yes | Harder vision benchmark |
| NEWS | Public | Yes | Text classification |
| Open-set CIFAR-10 | Derived | Yes | Outside images injected per Wang et al. |

**Offline experiment reproducibility:**  
Standard splits + published noise generation (symmetry + pair flipping); open-set construction described in-source.

---

## 6. Community Reaction

No dedicated X/Reddit/HN scan was run for this notebook-driven batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---

## Meta Information

**Authors:** Xingrui Yu; Bo Han; Jiangchao Yao; Gang Niu; Ivor W. Tsang; Masashi Sugiyama  
**Affiliations:** UTS / RIKEN-AIP / Alibaba Damo / UTokyo (per paper header in source)  
**Venue:** ICML 2019  
**Year:** 2019  
**PDF:** downloaded (arXiv PDF)  
**Relevance:** Core  
**Priority:** 2

---

## NotebookLM Extraction Notes (Phase 3 Batch 3)

**Q1:** Motivation (Co-teaching consensus issue) + Co-teaching+ steps + datasets/baselines.

**Q2:** Quantitative excerpts (Tiny-ImageNet 50% sym; open-set table; F-correction failure modes; NEWS behavior), limitations (Decoupling alone insufficient; warm-up required; rare lack of small-loss disagreement batches; noise-rate \(\tau\) estimation issues), and prior anchors (Han et al.; Jiang et al.; Malach & Shalev-Shwartz; Blum & Mitchell; Patrini et al.; Wang et al.; Zhang et al.; Arpit et al.).
