Date: 2026-04-12  
Source: `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/03_Ranking/Distill/2025 (Bytedance) (KDD) [HA-PFD] Hardness-aware Privileged Features Distillation with Latent Alignment for CVR Prediction.pdf` (arXiv fallback https://arxiv.org/pdf/2501.07509)  
NLM Source ID: e2ed9c54-5630-4a41-bf4c-5139aabf9ac6  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: KDD 2025  
Relevance: Core  
Priority: 3

# Paper Analysis: Hardness-aware Privileged Features Distillation (HA-PFD)

**Source:** Local awesome-repo PDF (ByteDance KDD 2025); arXiv `2501.07509` per queue  
**Date analyzed:** 2026-04-12

---

## 1. Summary (one paragraph)

**HA-PFD** (Huining Yuan, Wenpeng Zhang, Zijie Hao, Zengde Deng, ByteDance / Douyin ads) addresses **privileged features** in **CVR** (post-click signals only offline) by combining **focal-style logit distillation** (V1: student hardness weights; V2: teacher as attention) with **first-time latent-level PFD** via **layer-wise L2 alignment** with learnable maps between 3-layer DNN student/teacher towers, plus **MI-based selection** of ten privileged features (drop top-2 “too predictive” to avoid teacher cheating). Offline: **1.68B** Douyin 2024 logs (train Jan–Oct **1.39B**, test Nov–Dec **0.29B**). **HA-PFD V2** reaches training AUC **0.93022** / test **0.88772**, beats KD/ReviewKD/Similarity/Adversarial KD and improves **MCE** vs no-modeling/MTL; **online A/B** reports **+1.426% conversions**, **+3.739% advertiser value**, predicted CVR error **−8.634% → −0.983%** vs MTL. Limits: **γ** needs manual tuning in dynamic ads; vanilla **KD worsens calibration**; **MTL** test AUC can drop; **Platt** barely fixes MCE on imbalanced negatives.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Huining Yuan, Wenpeng Zhang, Zijie Hao, Zengde Deng  
**Affiliations:** ByteDance  
**Venue:** KDD 2025  
**Year:** 2025  
**PDF:** local awesome-repo + NotebookLM  
**Relevance:** Core  
**Priority:** 3
