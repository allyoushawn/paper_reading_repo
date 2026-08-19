# 2021 AAAI — Reciprocal embedding framework — Tapple production RRS

**Title:** A Reciprocal Embedding Framework For Modelling Mutual Preferences  
**Authors:** R. Ramanathan, Nicolas K. Shinada, Michinobu Shimatani, Yuhei Yamaguchi, Junichi Tanaka, Yuta Iizuka, Sucheendra K. Palaniappan (SBX + Tapple)  
**Year / venue:** 2021, AAAI / IAAI  
**Link:** https://cdn.aaai.org/ojs/17807/17807-13-21301-1-2-20210518.pdf  
**Tier:** 1  
**nlm:** 3da6ec16-bd07-4d28-b23f-e2ccd529327f / 85130fe7-5179-4373-b25d-f52dfa40d256

## Summary
Production reciprocal recommender on Tapple (~5M users, 200M matches at writing). Likes are power-law. Men send more likes than women. Learns unidirectional embeddings (men→women and women→men) then fuses for mutual like. Two-stage: CF candidate gen, then online rerank for recency/diversity so likes hit people who can reply. Region-specific models; precomputed KV serve <100 ms. Location-grouped A/B to limit interference.

## Metrics
- Offline vs match-only RS: recall **+16.9% matches**, **+26.74% likes**
- Candidate-gen raised engagement, conversion flat; after online rerank, conversion **up to +60%**

## Project Relevance
**High.** Precursor to CyberAgent TU papers. Shows fusion of two directed prefs is not enough — you still need a serve-time capacity/recency layer or likes do not become conversations.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| [2023_RecSys_TU-matching_Fast-Examination-agnostic-Reciprocal.md](./2023_RecSys_TU-matching_Fast-Examination-agnostic-Reciprocal.md) | lineage | TU/IPFP is the matching-theory successor to this production dual-embedding + recency rerank. |
| [2022_RecSys_MTRS_Matching-Theory-Online-Dating.md](./2022_RecSys_MTRS_Matching-Theory-Online-Dating.md) | industry talk | Same Tapple stack, later framed as Choo–Siow. |
