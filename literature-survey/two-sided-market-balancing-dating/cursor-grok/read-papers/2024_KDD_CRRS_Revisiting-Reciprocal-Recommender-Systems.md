# 2024 KDD — CRRS — Revisiting Reciprocal Recommender Systems

**Title:** Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method  
**Authors:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu  
**Year / venue:** 2024, KDD  
**Link:** https://arxiv.org/abs/2408.09748  
**Tier:** 1  
**nlm:** c48aa0c3-be96-4d7e-9d69-f80a146256cc

## Summary
One-sided Recall/NDCG double-counts redundant mutual exposures. New metrics: coverage-adjusted recall/precision, bilateral stability, RNDCG. Causal RRS + vacant-slot rerank. Dating CRecall@50 0.339 vs 0.301 DPGNN. Closest thing to a post-2021 “survey,” but it is a methods paper.

## Project Relevance
**High.** Stop scoring the ranker with swipe-CTR or one-sided Recall. Coverage of unique matches is the right offline proxy for ecosystem health.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| (none later in this `read-papers/` set) | | Bilateral metrics (CRecall / RNDCG) sit next to Palomares 2021 as an evaluation map, not a parent of TU. |
