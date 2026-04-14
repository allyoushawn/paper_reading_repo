# Paper Analysis: MAC: Conversion Prediction Benchmark Under Multiple Attribution Mechanisms

**Source:** https://arxiv.org/pdf/2603.02184.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** MAC: Conversion Prediction Benchmark Under Multiple Attribution Mechanisms  
**Authors:** Jinqi Wu, Sishuo Chen, Zhangming Chan, Yong Bai, Lei Zhang, Sheng Chen, Chenghuan Hou, Xiang-Rong Sheng, Han Zhu, Jian Xu, Bo Zheng, Chaoyou Fu (Alibaba / Alimama)  
**Abstract:**  
Introduces MAC, a public CVR dataset where each ad-click example carries labels under four mechanisms (last-click, first-click, linear, and data-driven attribution / DDA), enabling systematic study of multi-attribution learning (MAL). Releases PyMAL with baselines (Shared-Bottom, MMoE, PLE, HoME, NATAL) and proposes MoAE: mixture-of-experts backbone plus asymmetric transfer to prioritize the primary attribution target while still fitting auxiliary attribution views.

**Key contributions:**
- MAC benchmark from Taobao advertising logs (21 days; stratified sampling emphasizing highly active users).
- PyMAL open-source library for reproducible MAL experiments.
- MoAE architecture outperforming NATAL across multiple primary-target settings (reported GAUC gains).

**Methodology:**  
Defines MAL as predicting a designated primary mechanism while jointly training on auxiliary mechanism labels; MoAE combines shared + private experts and main-task-centric knowledge transfer; evaluation via AUC/GAUC with weighted binary classification framing (nonzero attribution weights as positives with importance weights).

**Main results:**  
Reported large GAUC lifts vs single-attribution BASE (e.g., up to ~+2.12pt GAUC in some last-click-primary settings per paper tables) and consistent gains vs NATAL; auxiliary-task gradient tricks (GCS/PCGrad) hurt strong MAL models.

---

## 2. Experiment Critique

**Design:**  
Strong public-benchmark contribution; careful ablations separating parameter scaling vs multi-label information gain.

**Statistical validity:**  
Industrial-scale ranking metrics; significance framed in industry “0.1pt GAUC” terms.

**Online experiments (if any):**  
Offline benchmark focus.

**Reproducibility:**  
Dataset released (HuggingFace path referenced in source); code via PyMAL.

---

## 3. Industry Contribution

**Deployability:**  
Benchmark + library intended to standardize MAL research and mirror industrial multi-label training setups.

**Problems solved:**  
Removes single-label public dataset bottleneck for MAL.

**Engineering cost:**  
Training MoE-style models at MAC scale is non-trivial but aligned with standard deep recsys practice.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First public multi-attribution CVR labels; MoAE as principled combination of “learn all views” + “prioritize main view.”

**Prior work comparison:**  
Extends Chen et al. NATAL/MAL line; compares to canonical MTL architectures.

**Verification:**  
Benchmark artifact is the primary durable contribution beyond incremental architecture gains.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| MAC (Taobao-derived, anonymized) | https://huggingface.co/datasets/alimamaTech/MAC | Yes (per paper) | Multi-attribution labels per click |

**Offline experiment reproducibility:**  
Feasible with released dataset + PyMAL; DDA labels depend on internal CausalMTA-style model details at label-generation time.

---

## 6. Community Reaction

No significant community discussion found.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Jinqi Wu et al.  
**Affiliations:** Alibaba / Alimama (Taobao advertising)  
**Venue:** arXiv  
**Year:** 2026  
**PDF:** https://arxiv.org/pdf/2603.02184.pdf  
**Relevance:** Core  
**Priority:** 2

---

## Project Relevance

The MAC dataset explicitly provides **continuous nonnegative attribution weights** per click under multiple mechanisms (including DDA from a causal MTA-style generator), which matches the “attribution-derived continuous supervision” ingredient for Phase 1/2 pipelines. However, **MoAE itself is a CVR ranker** that predicts probabilities aligned with existing labels rather than inventing new causal credit for a novel continuous outcome like user-days-active; touchpoints are **ad clicks**, not a heterogeneous {likes/messages/matches} event space. The paper notes stratified oversampling of highly active users and discusses confounding/noise mainly for **first-click** labels (time gap / promotions), not a full endogeneity treatment for “more touches because more active” beyond sampling design.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
