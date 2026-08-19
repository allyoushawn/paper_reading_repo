# 2025 RecSys — DiPS — OPE for Matching Markets

**Title:** Off-Policy Evaluation and Learning for Matching Markets  
**Authors:** Yudai Hayashi (Wantedly), Shuhei Goda, Yuta Saito (Cornell)  
**Year / venue:** 2025, RecSys  
**Link:** https://arxiv.org/abs/2507.13608  
**Tier:** 1  
**nlm:** 7e39447e-3e79-44be-a507-70275b62a7c0

## Summary
Matches are sparse two-stage rewards (scout/like then reply). Standard IPS/DR collapse. DiPS/DPR: importance-weight the first stage, impute the second. Wantedly Visit A/B logs: 21.7k companies, 17.5k seekers, 1.2% match sparsity; lower MSE than IPS/DR and tracks online A/B. Extends to offline policy learning.

## Project Relevance
**High.** Dating has the same two-stage label (like → match/reply). Use this before running expensive two-sided A/Bs on a capacity-aware ranker.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| RecSys 2025 accepted list (this workplace mine) | program | Only matching-market paper on the 2025 accepted list. LCM4Rec / Amazon two-stage OPE are adjacent, not substitutes. |
| [2021_AAAI_RRS_Reciprocal-Embedding-Framework-Tapple.md](./2021_AAAI_RRS_Reciprocal-Embedding-Framework-Tapple.md) | eval contrast | Tapple used location-grouped A/B, not OPE; DiPS is the offline path we still lack on dating logs. |
