# 2025 Tinder Tech Blog — Two-tower P(Match) — Elasticsearch 8 migration

**Title:** Tinder’s migration to Elasticsearch 8  
**Authors:** Igor Sokolov, Jessica Hickey, Rongxin Du  
**Year / venue:** 2025, Tinder Tech Blog (Medium)  
**Link:** https://medium.com/tinder/tinders-migration-to-elasticsearch-8-1999748ed7f4  
**Tier:** 1  
**nlm:** ef5834f7-2122-4ddd-93cb-914c2b4d5edf

## Summary
Tinder serves 90%+ of recommendations from one Elasticsearch cluster plus a custom Java scoring plugin. The ES8 migration unlocked kNN vector search. Ranking changes are treated as **sender–receiver ecosystem** risk (swiper and swipee KPIs), not single-viewer CTR. Two-tower experiments: P(Match) vs P(Like).

## Metrics
- 2T P(Match): **+6.5% match rate**, **+22% match volume**
- 2T P(Like): **+3.8% swipe-right rate**
- p99 latency −12–56%; <0.2% data discrepancy; zero outages

## Project Relevance
**High.** Direct evidence that optimizing like probability is the wrong north star on this product. Pattern: train/serve a match (reciprocal) head, not a swipe head.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| [2025_HingeBlog_NA_How-We-Connect-Daters.md](./2025_HingeBlog_NA_How-We-Connect-Daters.md) | corpus | Independent product confirmation: score mutual compatibility, not viewer-only like. Hinge has no architecture; Tinder has the A/B numbers. |
| [2021_OkCupidBlog_NA_Voter-Votee-Collaborative-Filtering-JAX.md](./2021_OkCupidBlog_NA_Voter-Votee-Collaborative-Filtering-JAX.md) | corpus | Same directed-like split (voter vs votee) without an online match-rate A/B. |
