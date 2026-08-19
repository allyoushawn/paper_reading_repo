# 2021 NeurIPS — UniCoRn — A/B Testing for Recommender Systems in a Two-sided Marketplace

**Title:** A/B Testing for Recommender Systems in a Two-sided Marketplace  
**Authors:** Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee (LinkedIn)  
**Year / venue:** 2021, NeurIPS  
**Link:** https://arxiv.org/abs/2106.00762  
**Tier:** 1  
**nlm:** 93144d1a-4049-4be7-a854-3e5e7ff5b79d (arXiv PDF; NLM extract 2026-08-17)

## Summary
Consumer-side ATE is a standard user-split. **Producer-side** ATE is not: a producer’s outcome depends on which consumers were treated. Cluster randomization loses power as the bipartite graph densifies; treatment-propagation estimators lack error control. UniCoRn (Unifying Counterfactual Rankings) mixes treatment/control producer lists inside each viewer session; α trades accuracy vs scoring cost. Deployed at LinkedIn on edge recs (PYMK/follow) with **α=0** (no extra online scoring). Scale: **750M+ members**, tens of millions served, **billions of edges/day**, **40%** of viewer traffic. Candidate-gen test (normalize shared-edges so stars lose exposure advantage): **+0.51% WAU**, **+0.57% sessions**. Ranking test (boost candidates predicted to visit if they get a request — viewee retention): **+0.13% WAU**, **+0.11% sessions**. All p<0.001. Not dating OPE.

## Project Relevance
**High analog** for inbound-like (producer) measurement when we change ranking. Complements Johari et al. MS 2022 (which side to randomize) and Lyft MMV (shadow-price correction of user-splits). Still **not** dating-log OPE — Hayashi RecSys 2025 remains the matching-market OPE paper, and it uses Wantedly jobs.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| (none in this workplace’s `read-papers/`) | | Same LinkedIn experiment stack as LiJAR/LinkSAGE/Geyik; not cited by the dating matching-theory line. |
