# Paper Analysis: Entire Space Multi-Task Model (ESMM)

**Source:** `03_Ranking/Multi-task/2018 (Alibaba) (SIGIR) [ESMM] Entire Space Multi-Task Model - An Effective Approach for Estimating Post-Click Conversion Rate.pdf`  
**Date analyzed:** 2026-02-22

---

## 1. Summary

**Title:** Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate  
**Authors:** Xiao Ma, Liqin Zhao, Guan Huang, Zhi Wang, Zelin Hu, Xiaoqiang Zhu, Kun Gai (Alibaba Inc.)  
**Venue:** SIGIR 2018 (Short Research Paper, 4 pages)

**Abstract (what it solves):**
- Targets **post-click conversion rate (CVR)** prediction.
- Addresses two core issues:
  1. **Sample selection bias**: CVR models are trained on **clicked** impressions but used over **all** impressions.
  2. **Data sparsity**: conversions are rare → CVR data is **1–3 orders of magnitude** smaller than CTR data.
- Exploits sequential user actions: **impression → click → conversion**.
- Uses decomposition: **CTCVR = CTR × CVR**, allowing training over the **entire impression space**.

**Key contributions:**
- Formalizes **sample selection bias** and **data sparsity** for CVR through the sequential action lens.
- Proposes **ESMM** using:  
  \( p(CTCVR) = p(CTR) \times p(CVR) \)  
  enabling **entire-space training** without numerical instability.
- **Shares embeddings** between CTR and CVR networks (transfer from data-rich CTR to sparse CVR).
- Releases the first public dataset for this setup: **Ali-CCP** (sequential click+conversion labels).

**Methodology (how it works):**
- Two sub-networks:
  - **CTR network**
  - **CVR network**
- Both share the same **Embedding + MLP** architecture.
- Both trained on **all impressions**.
- **CVR is not directly supervised.** Instead:
  - Constrain \( pCTCVR = pCTR \times pCVR \)
  - Optimize a loss that includes **CTR** and **CTCVR** cross-entropy only (no direct CVR loss).
- Shared **embedding layers** act as transfer learning from CTR → CVR.

**Main results:**
- **Public dataset:**
  - CVR AUC: **68.56%** (**+2.56% abs** over BASE)
  - CTCVR AUC: **65.32%** (**+3.25%** over BASE)
- **Product dataset (8.9B samples):**
  - CVR: **+2.18% AUC** over BASE
  - CTCVR: **+2.32% AUC** over BASE
- ESMM consistently beats **BASE, AMAN, OVERSAMPLING, UNBIAS, DIVISION, ESMM-NS** across datasets and sampling rates.

---

## 2. Experiment Critique

### Design

| Criterion | Assessment |
|---|---|
| Controls | **Strong.** BASE is a clear baseline; competitors use the same network structure and hyperparameters. |
| Baselines | **Adequate.** Six competitors cover data manipulation (AMAN, OVERSAMPLING), debiasing (UNBIAS), decomposition (DIVISION), and ablation (ESMM-NS). Missing comparisons to richer MTL baselines (shared-bottom, cross-stitch, etc.). |
| Ablations | **Partial.** ESMM-NS (no sharing) isolates embedding sharing vs. full ESMM, but no ablation isolates the *multiplication constraint* alone vs. joint-training variants. |
| Confounds | Temporal split (first half train / second half test) is appropriate and reduces leakage risk. |

### Statistical validity

| Criterion | Assessment |
|---|---|
| Repetitions | **Good.** 10 runs; mean ± std reported. |
| Significance | **Weak.** No formal tests (p-values/CIs). Some std overlap (e.g., ESMM vs. ESMM-NS on CVR). |
| Effect sizes | **Clear.** Absolute AUC gains reported; notes that ~0.1% AUC can matter at scale. |
| Sample size | **Very large.** 84M impressions (Public) and 8.9B (Product). |

**Online experiments:**
- **None reported.** BASE is deployed in production, but no A/B for ESMM → major gap for an industrial paper.

### Reproducibility

| Criterion | Assessment |
|---|---|
| Code | **Weak.** No official repo; third-party implementations exist (PaddleRec, GitHub). |
| Hyperparameters | **Strong.** ReLU, embedding dim=18, MLP: 360×200×80×2, Adam (β1=0.9, β2=0.999, ε=1e-8). |
| Random seeds | Not reported. |
| Data splits | Described (temporal 50/50). |
| Environment | Not specified (framework/hardware). |

**Overall:** Strong structure for a 4-page short paper; consistent wins across baselines/datasets are convincing. Biggest gaps: no online A/B, weak significance analysis, and missing ablation for multiplication constraint vs. other joint-training strategies.

---

## 3. Industry Contribution

**Deployability:** High.
- Uses standard **Embedding+MLP** already common in CTR systems.
- CTR net can double as embedding provider for CVR.
- Multiplication constraint is computationally trivial.
- No extra features/external data/complex serving needed.
- If CTR is already predicted elsewhere, serving may only require CVR sub-network.

**Problems solved:**
- **Sample selection bias:** practical and pervasive; ESMM gives a principled fix.
- **Data sparsity:** embedding sharing leverages CTR volume.
- **Numerical stability:** avoids division-by-small-number issues in DIVISION.

**Engineering cost:** Low.
- Training cost moderately higher (two networks, shared embeddings).
- No new data collection required.
- Modular design: sub-networks can evolve independently.

**Adoption signal:** The approach became a de facto industry standard for CVR modeling, suggesting strong practical value.

---

## 4. Novelty vs. Prior Work

**Paper’s claimed novelty:**
- First to exploit the sequential pattern (impression → click → conversion) via \( pCTCVR = pCTR \times pCVR \).
- First to address **bias + sparsity** together through entire-space multi-task learning.
- First public sequential click+conversion dataset.

**Prior work comparison:**
- MTL itself wasn’t new (e.g., Ruder 2017), but applying it to CVR through probability decomposition was novel in this context.
- Existing methods (AMAN, OVERSAMPLING, UNBIAS) address only one issue or introduce drawbacks.
- DIVISION is a naive decomposition implementation but is numerically unstable.

**Verification:**
- ESMM is highly influential and triggered follow-ups (e.g., ESCM2 SIGIR 2022; extensions for additional action chains and better bias handling).
- No clear earlier work with the same CVR-focused formulation was identified.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Ali-CCP (Public Dataset) | tianchi.aliyun.com/dataset/408 | Yes | 1% sample; 84M impressions, 3.4M clicks, 18K conversions; ~38GB uncompressed. First public sequential click+conversion dataset. |
| Product Dataset | N/A (proprietary) | No | 8.9B impressions, 324M clicks, 1.77M conversions (Taobao logs). |

**Offline reproducibility:** Partially reproducible.
- Public dataset available and large enough to validate core claims.
- Hyperparameters provided.
- Missing: official code, random seeds, framework/hardware.
- Third-party implementations (PaddleRec / GitHub) can help.

**Run tip:** To run experiments on Ali-CCP, use the experiment-runner skill with the dataset URL: `https://tianchi.aliyun.com/dataset/408`.

