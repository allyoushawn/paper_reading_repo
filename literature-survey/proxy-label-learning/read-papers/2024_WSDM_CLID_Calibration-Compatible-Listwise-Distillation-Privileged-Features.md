Date: 2026-04-12  
Source: https://arxiv.org/pdf/2312.08727 (published WSDM 2024 per PDF)  
NLM Source ID: 30206787-3644-4a0c-94c0-000e1d2fe9f9  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: WSDM 2024  
Relevance: Core  
Priority: 3 (queue); full report per Phase 3 Batch 4 spec

# Paper Analysis: Calibration-compatible Listwise Distillation of Privileged Features (CLID)

**Source:** https://arxiv.org/pdf/2312.08727  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Calibration-compatible Listwise Distillation of Privileged Features for CTR Prediction  

**Authors:** Xiaoqiang Gui (Shandong University); Yueyao Cheng, Xiang-Rong Sheng, Shuguang Han, Yuning Jiang, Jian Xu, Bo Zheng, Yunfeng Zhao, Guoxian Yu (Alibaba / SDU collaborators per PDF header)

**Abstract:**  
**Privileged features** (e.g., **contextual items** on the same page visible only at re-ranking, not at coarse ranking) improve CTR if used offline. **PFD** distills a teacher (privileged + regular) into a student (regular only). **Pointwise** KD ignores list context; **ListNet/ListMLE** distillation **breaks pCTR calibration** (bad for CPC/eCPM billing). **CLID** defines **calibration-compatible** distillation loss (global minima align with pointwise CE optima of student and teacher) and uses **normalized pCTR** across each list as a probability simplex, then **cross-entropy** between teacher and student list distributions—**theoretically** calibration-compatible per paper.

**Key contributions:**
- Formalizes calibration-compatible distillation in PFD context (inspired by **RCR**).
- Proves common listwise losses **fail** compatibility when used as distillation losses.
- **CLID** loss Eq. (15) + DIN-style base module; public + production eval.

**Methodology:**  
Embeddings + **DIN** pooling → \(V_r\) (student), concat \(V_p\) → \(V_t\) (teacher). Student loss \(L_s = \alpha L_{CE}(y, p_s) + (1-\alpha) L^{CLID}_d\); \(P_t(x_i)=p_{t,i}/\sum_j p_{t,j}\), same for \(P_s\); \(L^{CLID}_d = -\sum_i P_t(x_i)\log P_s(x_i)\).

**Main results:**  
**Web30K:** NDCG@10 **0.4495** vs Base **0.4478**, LogLoss **0.6090** vs **0.6101**, ECE **0.1626** vs **0.1629**. **Istella-S:** NDCG@10 **0.7084** vs **0.6862**. **Production (Alibaba display ads):** **+0.38% GAUC** vs Base with **+0.02% LogLoss** (vs **+0.78%** LogLoss for Base+ListMLE). PriDropOut/PAL show calibration degradation.

---

## 2. Experiment Critique

**Design:**  
Six baselines (Base, PriDropOut, PAL, Base+Pointwise, Base+ListMLE, Base+ListNet); public LTR→CTR binarization; production relative metrics.

**Statistical validity:**  
Public sets: 5 trials, 95% CI in tables; production only **relative** improvements.

**Online experiments (if any):**  
Production table is offline relative to deployed Base; no separate long-form online A/B excerpt in NLM summary.

**Reproducibility:**  
Public **Web30K** / **Istella-S** links in paper; production data proprietary.

**Overall:**  
Theory + public benchmarks support ranking+calibration story; **α / (1−α) ratio** ablation: extreme ratios (>100) hurt both metrics.

---

## 3. Industry Contribution

**Deployability:**  
Drop-in distillation loss swap for existing two-tower PFD trainers serving **pCTR-calibrated** auctions.

**Problems solved:**  
Preserves **eCPM = 1000 · pCTR · bid** semantics while gaining **listwise** teacher ranking signal.

**Engineering cost:**  
List-normalization needs per-request lists; same infra as other listwise losses.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
First **calibration-compatible listwise** PFD loss; bridges **RCR** (LTR calibration) to distillation.

**Prior work comparison:**  
Builds on **Xu et al. Taobao PFD**, **ListNet/ListMLE**, **Bai et al. RCR**, **Liu/Yang PFD** analyses.

**Verification:**  
WSDM 2024 publication; arXiv 2312.08727 preprint—**venue year is 2024**, not “2023” in queue title.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Web30K | https://www.microsoft.com/en-us/research/project/mslr/ | Yes | LTR → binarized CTR |
| Istella-S | http://quickrank.isti.cnr.it/istella-dataset/ | Yes | Same |
| Alibaba display logs | Proprietary | No | Billions of impressions Nov 2022 excerpt |

**Offline experiment reproducibility:**  
Public portion reproducible; privileged contextual features simulated from co-listed docs.

---

## 6. Community Reaction

Not specified in source.

---

## NotebookLM handoff (Phase 3)

**Q1:** CTR PFD; contextual privileged features; CLID = normalized pCTR list-CE; DIN base; Web30K, Istella-S, Alibaba production.

**Q2:** Table metrics as above; ListMLE/ListNet destroy calibration; PriDropOut ranking can drop; **weight ratio** ablation; priors: **Xu PFD**, **Bai RCR**, **Cao ListNet**, **Xia ListMLE**, **PAL/PriDropOut**, **Liu/Yang pointwise PFD**.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Xiaoqiang Gui et al.  
**Affiliations:** Shandong University; Alibaba Group  
**Venue:** WSDM 2024 (arXiv:2312.08727)  
**Year:** 2024  
**PDF:** arXiv + NotebookLM  
**Relevance:** Core  
**Priority:** 3 (queue label); expanded per batch instructions

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
