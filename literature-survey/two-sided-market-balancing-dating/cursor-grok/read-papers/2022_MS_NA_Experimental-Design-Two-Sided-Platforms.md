# 2022 Management Science — Experimental Design in Two-Sided Platforms

**Title:** Experimental Design in Two-Sided Platforms: An Analysis of Bias  
**Authors:** Ramesh Johari, Hannah Li, Inessa Liskovich, Gabriel Weintraub  
**Year / venue:** 2022, Management Science  
**Link:** https://arxiv.org/abs/2002.05670  
**Tier:** 2  
**nlm:** c2aa9d85-74ed-4a98-8c41-55a7c5642d1b

## Summary
Mean-field interference on a two-sided platform: treating one side changes congestion for the other. Which side you randomize depends on which side is the scarce resource. Customer-side, listing-side, and two-sided randomization (TSR) plus a cannibalization correction. Demand-constrained simulations: listing-side randomization bias ~**1.7% of GTE**. Do not A/B a capacity-aware ranker as if it were a feed.

## Project Relevance
**High.** This is the theory card for pattern 8. Pair with Tapple location-grouped A/B (Ramanathan AAAI 2021), Lyft MMV (2025), UniCoRn (producer-side design), and Hayashi DiPS (OPE when A/B is too expensive). Dating analog: randomize the congested gender / the inbound-like side, not only viewers.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| [2025_LyftEng_MMV_Marketplace-Marginal-Values-Interference.md](./2025_LyftEng_MMV_Marketplace-Marginal-Values-Interference.md) | method | User-split ATE is biased under resource contention; MMV is a practical correction, not a replacement for choosing the congested side. |
| [2021_NeurIPS_UniCoRn_AB-Testing-Two-Sided-Marketplace.md](./2021_NeurIPS_UniCoRn_AB-Testing-Two-Sided-Marketplace.md) | related (corpus) | Complementary: Johari chooses *which side*; UniCoRn designs *producer-side* experiments when that side’s outcomes depend on consumer assignment. |
