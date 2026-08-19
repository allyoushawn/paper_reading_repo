# 2025 Lyft Eng — MMV — Marketplace Marginal Values vs Interference

**Title:** Using Marketplace Marginal Values to Address Interference Bias  
**Authors:** Shima Nassiri, Ido Bright (Lyft Engineering)  
**Year / venue:** 2025, engineering blog  
**Link:** https://eng.lyft.com/using-marketplace-marginal-values-to-address-interference-bias-a11aff6e670f  
**Tier:** 1  
**nlm:** 9fe83587-cd97-4016-9ada-368a68677ee9 (NLM returned no body; this note is from the live page)

## Summary
90% of Lyft tests are user-split and biased when one side is congested. Switchbacks/geos lack power or wreck UX. MMV: hourly dispatch LP duals (shadow prices) as the marginal value of a rider/driver; subtract contention from the ATE. CUPED on MMV metrics. Backtests: 10% of launch decisions would flip vs naive user-split; congested cases ~45% smaller magnitude; MMV user-split closer to historical time-splits. Theory: Bright et al. 2024. Johari et al. (MS 2022) is the design counterpart.

## Project Relevance
**High for evaluation, medium for ranking.** Dating is choice-based (Johari) not match-based (Lyft), so copy the *diagnosis* (congested reply capacity leaks across arms), not the dispatch duals literally. Combine with Hayashi RecSys 2025 OPE.

## Reverse Citation Map

| Mentioning Paper | Section | Summary of Mention |
|------------|------|--------------|
| [2022_MS_NA_Experimental-Design-Two-Sided-Platforms.md](./2022_MS_NA_Experimental-Design-Two-Sided-Platforms.md) | method | Johari is the design counterpart (which side to randomize); MMV corrects a user-split after the fact. |
