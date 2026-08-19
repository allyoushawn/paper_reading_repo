# 2023 RecSys — TU matching — Fast and Examination-agnostic Reciprocal Recommendation

**Title:** Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets  
**Authors:** Yoji Tomita, Riku Togashi, Yuriko Hashizume, Naoto Ohsaka (CyberAgent)  
**Year / venue:** 2023, RecSys  
**Link:** https://arxiv.org/abs/2306.09060  
**Tier:** 1  
**nlm:** 711cc5a5-fa03-4b06-b668-247bd8c34f21

## Summary
Reciprocal ranking on dating/job platforms must encode mutual preference *and* stop concentrating likes on popular users. Prior matching-market rankers depend on a position-based examination function and do not scale. This paper uses transferable-utility (Choo–Siow) matching: IPFP produces market-clearing outside-option probabilities, concatenated into a (2d+2)-dimensional feature so scores stay inner products (MIPS). Evaluated on synthetic markets and Japanese dating-platform logs. Beats Naive and Reciprocal fusion on expected matches; remains feasible where the SW baseline dies; improves Gini.

## Project Relevance
**High.** This is the production-shaped answer to “score like-back under capacity.” Shared with Survey 3 — market-layer lens only.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| [2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md](./2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md) | method | NSW ranking is the envy-aware successor to TU/IPFP lists. |
| MRet 2026 / MODE 2026 (bib cards) | lineage | Direct-effect / retention-weighted matching built on the TU stack. |
