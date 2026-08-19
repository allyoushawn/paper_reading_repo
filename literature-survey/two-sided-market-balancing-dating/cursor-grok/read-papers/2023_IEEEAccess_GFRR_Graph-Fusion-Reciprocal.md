# 2023 IEEE Access — GFRR — Graph Fusion in Reciprocal Recommender Systems

**Title:** Graph Fusion in Reciprocal Recommender Systems  
**Authors:** Luwei Zhang, Xueting Wang (UTokyo / CyberAgent), Toshihiko Yamasaki (UTokyo)  
**Year / venue:** 2023, IEEE Access 11:8860–8869  
**Link:** https://doi.org/10.1109/ACCESS.2023.3239785  
**Tier:** 2  
**nlm:** 2383281d-7e6b-4cc0-9856-0c476d92e23c (text extract; IEEE DOI page ingested as empty wall `d9e1502a`)

## Summary
GFRR is a GNN on a gender-bipartite send/reply graph. Unlike reply-only RRS, it predicts **send** and **reply** separately, then fuses. Data: 2020 interactions from a collaborating online dating service (Wang at CyberAgent; Japanese, not Chinese). Mean match rate **<10%**. Offline vs feature-interaction baselines: send AUC **73.15%** (+3.20 pp) / AP 26.01% (+2.79 pp); reply AUC **68.95%** (+1.74 pp); fusion AUC **71.26%** (+4.35 pp). No online A/B. Cites RECON / Xia ASONAM 2015.

## Project Relevance
**High** as dating-log send-vs-reply scoring (same split as Tinder P(Like) vs P(Match) and Hayashi’s two-stage OPE labels). **Medium** as an allocator — no capacity or congestion term. Do not treat as a 探探/陌陌 ranking post.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| (none in this workplace’s `read-papers/`) | | Later CyberAgent RecSys TU/NSW/MODE papers do not cite GFRR in the notes we have; treat as a parallel GNN scoring line, not the matching-theory line. |
