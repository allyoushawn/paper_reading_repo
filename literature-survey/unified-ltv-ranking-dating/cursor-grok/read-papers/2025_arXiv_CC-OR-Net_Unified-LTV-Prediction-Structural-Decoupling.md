# Paper Analysis: CC-OR-Net: A Unified Framework for LTV Prediction through Structural Decoupling

**Source:** https://arxiv.org/pdf/2601.10176.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** CC-OR-Net: A Unified Framework for LTV Prediction through Structural Decoupling
- **authors or company:** Mingyu Zhao, Haoran Bai, Yu Tian, Bing Zhu, Hengliang Luo (Meituan; Renmin University of China)
- **venue:** WWW
- **year:** 2026
- **URL:** https://arxiv.org/pdf/2601.10176.pdf
- **source type:** industry paper
- **direction:** D4
- **problem setting:** Customer-level LTV prediction on large Web platforms; zero-inflated long-tail spend with rare whale users—not item-level reciprocal recommendation ranking.
- **objective and label definition:** Non-negative lifetime value \(y\in\mathbb{R}^+\) per user; \(K=4\) ordinal buckets (zero + three quantile splits on positives); trilemma: ranking (Gini, Spearman), regression (NMAE, MAPE, NRMSE), whale precision (AMBE, SVA stratified accuracy).
- **prediction or incrementality:** Supervised LTV point prediction with architecturally guaranteed ordinal ranking; not causal incrementality of exposure.
- **model architecture:** CC-OR-Net: shared encoder → cascaded ordinal decomposition (\(K-1\) conditional exceedance classifiers + distillation) → intra-bucket residual regression → attention-guided high-value augmentation for top bucket; combined losses \(L_{total}=L_{cascade}+L_{distill}+L_{residual}+L_{high\_value}\).
- **credit assignment:** User-level LTV label only; no session/impression or two-sided credit assignment.
- **training data and counterfactual handling:** Three Meituan industrial domains (248M / 41M / 33M records); chronological 40% test split; no counterfactual or treatment arms.
- **offline and online evaluation:** Offline ranking/regression/classification metrics; production deployment on Meituan platforms stated; no A/B numbers reported in source.
- **reported gains:** vs baselines on Domain 1: Gini 0.803, Spearman 0.761, SVA 67.01%, whale-bucket AMBE 4.849 (−25.0% vs w/o augmentation); Recall@5000 whales 38.1% vs ExpLTV 36.5%; inference 0.79 ms (100k batch).
- **applicability note for a two-sided dating recommender:** Structural ordinal-then-residual LTV modeling fits dating's zero-inflated payer/subscriber revenue if labels are user-level 7–30d+ monetization—not per-swipe.
  Whale-augmentation module is directly relevant when a small fraction of subscribers drives revenue and global Gini masks tail errors.
- **unverified claims:** none

## 1. Summary

CC-OR-Net structurally decouples ordinal user stratification from within-bucket regression and whale-specific augmentation for zero-inflated LTV. Cascaded binary exceedance classifiers enforce monotonic buckets; distillation aligns batch distributions; residual head refines values; high-value module cuts whale bias. Evaluated on 300M+ user industrial data with superior trilemma trade-offs; deployed at Meituan.

## 2. Experiment Critique

Strengths: massive industrial scale; principled ablations; SVA business metric; efficiency table; production deployment claim. Weaknesses: LTV horizon not stated in days; bucket thresholds are data-driven quantiles not fixed business horizons; no online experiment metrics in paper.

## 3. Industry Contribution

Production LTV stack for Meituan; modular \(O(K)\) ordinal cascade suitable for billion-user batch scoring; whale targeting for marketing ROI.

## 4. Novelty vs. Prior Work

vs ZILN/OptDist/ExpLTV: architectural (not loss-only) ordinal guarantee; vs CORAL/CORN: specialized whale augmentation and fixed pipeline vs soft routing. Related to Frank-Hall ordinal cascades and Meituan/Kuaishou industrial LTV work.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Meituan Domain 1–3 | Internal | No | 33M–248M records |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Jointly optimizes LTV ranking (Gini, Spearman) and regression; not CTR or match rate. Retention: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
User-level LTV label; no item-level assignment. Horizon: Not specified in source (chronological industrial LTV).

### (3) Label and horizon definitions; delay, sparsity, censoring
Zero-inflated long-tail LTV with whale sparsity explicitly modeled; exact day horizon: Not specified in source.

### (4) Short vs long-term head fusion
Structural decomposition of ordinal rank vs residual value vs whale head—analogous to multi-objective LTV label design, not online ranker fusion.

### (5) Prediction vs incrementality
Absolute LTV prediction/regression, not incrementality.

### (6) Offline and online evaluation
Offline metrics on three domains; production deployment claimed without reported A/B effect sizes.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
User-level LTV scorer that could feed a unified ranker value head; no feed-ranking integration described.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Mingyu Zhao, Haoran Bai, Yu Tian, Bing Zhu, Hengliang Luo
**Affiliations:** Meituan; Renmin University of China
**Venue:** WWW 2026
**Year:** 2026
**PDF:** https://arxiv.org/pdf/2601.10176.pdf
**Relevance:** Core
**Priority:** 4
