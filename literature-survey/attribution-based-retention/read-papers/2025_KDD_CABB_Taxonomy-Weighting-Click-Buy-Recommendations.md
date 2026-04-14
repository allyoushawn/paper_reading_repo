# Paper Analysis: Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations

**Source:** https://arxiv.org/pdf/2507.15113.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations  
**Authors:** Xiangyu Zeng, Amit Jaspal, Bin Liu, Goutham Panneeru, Kevin Huang, Nicolas Bievre, Mohit Jaggi, Prathap Maniraju, Ankur Jain (Meta Platforms)  
**Abstract:**  
Many conversions come from sessions where users click product A but purchase a different product B (CABB). Training on naive last-click pairs over-rewards popular “click magnets” and hurts relevance/diversity. The authors use a two-head multitask model (CABA vs CABB) and scale the CABB loss by a taxonomy-grounded, category-to-category similarity score learned from co-engagement (clicks/add-to-cart/purchases), down-weighting unrelated cross-item purchases.

**Key contributions:**
- Multitask decomposition separating same-item vs cross-item purchase prediction.
- Category-level item-to-item collaborative filtering similarity in \([0,1]\) used as example weights \(\alpha\) in the CABB loss.
- Offline NE gains vs last-click and CABA-only baselines; online +0.25% primary business metric lift with higher CABA rate.

**Methodology:**  
Shared embeddings + separate heads; cosine similarity on category co-engagement vectors; total loss \(\mathcal{L}=\mathcal{L}_{\mathrm{CABA}}+\lambda \mathcal{L}_{\mathrm{CABB}}\).

**Main results:**  
Reported NE 0.495 vs 0.575 (Baseline-1 last-click) and 0.547 (Baseline-2 CABA-only); taxonomy+CF weighting improves CABA NE vs unweighted CABB inclusion.

---

## 2. Experiment Critique

**Design:**  
Clear ablations on similarity schemes (static=1 vs i2i embeddings vs taxonomy+CF) and on \(\lambda\).

**Statistical validity:**  
Uses NE as primary calibration metric; online A/B reported as statistically significant.

**Online experiments (if any):**  
Two-week live test vs production last-click model.

**Reproducibility:**  
Internal Meta e-commerce logs; method reproducible with taxonomy + co-engagement pipeline.

**Overall:**  
Practical attribution-of-credit issue in recsys, but not MTA along a multi-ad touchpath in the classical sense.

---

## 3. Industry Contribution

**Deployability:**  
Lightweight vs deep sequence MTA models; interpretable category similarity trace.

**Problems solved:**  
Cross-item purchase noise in conversion modeling for ads-driven e-commerce.

**Engineering cost:**  
Taxonomy maintenance + periodic similarity matrix refresh; \(\lambda\) tuning sensitivity noted by authors.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First end-to-end framework explicitly separating CABA/CABB with semantic/behavioral gating of cross-item supervision.

**Prior work comparison:**  
Contrasts with deep sequence MTA (RNN/Transformer credit assignment) and cites ESMM for multitask conversion modeling.

**Verification:**  
Claims are internally consistent with reported offline/online deltas.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Meta internal e-commerce sessions | N/A | No | Proprietary |

**Offline experiment reproducibility:**  
Algorithmic steps reproducible; dataset not.

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

**Authors:** Xiangyu Zeng; Amit Jaspal; Bin Liu; Goutham Panneeru; Kevin Huang; Nicolas Bievre; Mohit Jaggi; Prathap Maniraju; Ankur Jain  
**Affiliations:** Meta Platforms, Inc.  
**Venue:** KDD  
**Year:** 2025  
**PDF:** https://arxiv.org/pdf/2507.15113.pdf  
**Relevance:** Core  
**Priority:** 2

---

## Project Relevance

**Low project relevance.** The learned \(\alpha\) weights are **example-level loss scalers** for a **post-click, cross-item purchase** issue, not a general multi-touch fractional credit allocation across a sequence of heterogeneous engagement events leading to a **continuous** retention outcome. Outcomes are **binary purchase labels** per session granularity described in-source. Co-engagement features mix clicks/add-to-cart/purchases for similarity construction, but the prediction setup does not target user-days-active or dating-style selection bias beyond popularity-driven co-occurrence noise called out in limitations.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
