Date: 2026-04-12  
Source: `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/03_Ranking/Multi-task/2025 （Alibaba) (CIKM) [MAL] See Beyond a Single View - Multi-Attribution Learning Leads to Better Conversion Rate Prediction.pdf`  
NLM Source ID: 3b2910bf-5162-420b-b75c-c24dd51894f0  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: CIKM 2025  
Relevance: Related  
Priority: 3

# Paper Analysis: Multi-Attribution Learning for CVR (MAL)

**Source:** Local awesome-repo PDF (no public URL per queue)  
**Date analyzed:** 2026-04-12

---

## 1. Summary (one paragraph)

**MAL** trains CVR under the **system-optimized attribution** (e.g., Last-Click) while **jointly** exploiting **First-Click, Linear, and MTA** partial-credit labels from **Taobao display ads** (two-month click logs + next-day test; no public multi-attribution CVR set). **AKA** is a shared-bottom multi-tower module (DIN-style interactions) with one tower per attribution + **CAT**: Cartesian product of four binary attributions → **16-class auxiliary head** feeding a concatenated **knowledge embedding** \(\mathcal{K}\). **PTP** mirrors production CVR architecture but fuses \(\mathrm{MLP}(\mathcal{K})\) with primary features via **element-wise add** (KEEP-inspired). Offline: **+0.51% GAUC / +0.14% AUC** vs production Base with Last-Click primary; **+0.75% / +0.21%** when MTA is primary; **beats MMoE/PLE/HoME** by **~0.15–0.20% GAUC**; ablation—**multi-attribution signal** drives gains (towers all on primary → **+0.01% GAUC** only). Online (May 21–25, 2025): **+2.7% GMV, +1.2% orders, +2.6% ROI**; long-path categories (appliances **+11.6%** BuyCnt) benefit most; short-path (toys/pets) smaller lifts. Limits: purchase-only scope; future LLM/gen-rec extensions noted.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Alibaba authors (CIKM 2025); full author string not captured in NLM excerpt  
**Affiliations:** Alibaba (Taobao display advertising)  
**Venue:** CIKM 2025  
**Year:** 2025  
**PDF:** local awesome-repo only  
**Relevance:** Related  
**Priority:** 3
