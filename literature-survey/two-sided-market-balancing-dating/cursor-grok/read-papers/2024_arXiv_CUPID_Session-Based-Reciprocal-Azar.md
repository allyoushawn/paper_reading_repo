# 2024 arXiv — CUPID — session-based reciprocal matching at Azar

**Title:** CUPID: A Real-Time Session-Based Reciprocal Recommendation System for a One-on-One Social Discovery Platform  
**Authors:** Beomsu Kim, Sangbum Kim, Minchan Kim, Joonyoung Yi, Sungjoo Ha, Suhyun Lee, Youngsoo Lee, Gihoon Yeom, Buru Chang, Gihun Lee (Hyperconnect)  
**Year / venue:** 2024, arXiv:2410.18087  
**Link:** https://arxiv.org/abs/2410.18087  
**Tier:** 1  
**nlm:** fa442dc5-e8d7-43ec-b21c-b4f62618f3cd

## Summary
Azar video-chat matching: both users must be satisfied; preferences shift after every chat; latency budget is tens of milliseconds. CUPID caches session embeddings asynchronously, scores predicted chat duration with projected dual embeddings (plain dot product over-scores similar users). Two-phase training (embed then freeze, train predictor) to make reciprocal training tractable.

## Metrics
- Online: chat duration **+6.8%**, long-match ratio **+12.6%**, short-match **−2.4%** (all users)
- p90 latency 236→48 ms (**−79.7%**)

## Project Relevance
**Medium-high.** Not dating, but the same two-sided latency + mutual-satisfaction problem. Use chat-duration (or conversation length) as the reciprocal label if like-back is too sparse.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| (none in corpus) | | Social-discovery duration ranker; not cited by the dating TU line. |
