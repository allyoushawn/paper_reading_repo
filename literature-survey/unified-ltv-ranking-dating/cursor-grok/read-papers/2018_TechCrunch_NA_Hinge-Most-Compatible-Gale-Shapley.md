# Paper Analysis: Hinge Employs New Algorithm to Find Your "Most Compatible" Match

**Source:** https://techcrunch.com/2018/07/11/hinge-employs-new-algorithm-to-find-your-most-compatible-match-for-you/  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** Hinge Employs New Algorithm to Find Your "Most Compatible" Match
- **authors or company:** Sarah Wells (TechCrunch); Hinge CEO Justin McLeod quoted
- **venue:** TechCrunch
- **year:** 2018
- **URL:** https://techcrunch.com/2018/07/11/hinge-employs-new-algorithm-to-find-your-most-compatible-match-for-you/
- **source type:** blog
- **direction:** D8
- **problem setting:** Journalistic report on Hinge's "Most Compatible" daily feature that surfaces one mutually highlighted pairing at the top of Discover.
- **objective and label definition:** Identify pairs most likely to "hit it off"; preferences learned from historical liking and passing activity; success proxy in market tests = exchange of personal phone numbers; horizon, delay, sparsity, censoring not specified in source.
- **prediction or incrementality:** Not specified in source.
- **model architecture:** Gale-Shapley stable-marriage algorithm on learned preference rankings; stable roommate problem variant for non-heterosexual pairings without rigid gender partitions.
- **credit assignment:** Not specified in source.
- **training data and counterfactual handling:** Early market trials on live Hinge user base; compared against other Hinge recommendation algorithms; no dataset details disclosed.
- **offline and online evaluation:** Early market tests only; 8× higher date likelihood (phone-number exchange) vs other Hinge recommendations; platform ~400% user growth after 2016 redesign noted as contextual background.
- **reported gains:** Users 8× more likely to go on dates (phone-number exchange proxy) with Most Compatible vs other Hinge recommendations.
- **applicability note for a two-sided dating recommender:** Illustrates explicit reciprocal mutual surfacing—both users see each other as the day's top pick—grounded in stable matching theory rather than one-sided score ranking.
- **applicability note for a two-sided dating recommender:** Journalistic source with no loss functions, serving architecture, congestion control, retention/LTV objectives, or rigorous evaluation protocol; 8× claim is Hinge-reported from early trials without disclosed methodology.
- **unverified claims:** 8× date-likelihood lift and causal link to Gale-Shapley implementation are Hinge-reported via journalist, not peer-reviewed; stable roommate adaptation details not independently verified.

## 1. Summary

TechCrunch article (July 2018) describing Hinge's "Most Compatible" feature: one daily pairing placed at the top of Discover where both users are shown each other simultaneously. Hinge learns preferences from liking/passing history and applies the Gale-Shapley algorithm (1962 stable marriage) with a stable roommate problem variant for LGBTQ+ users. Early market tests reportedly found users 8× more likely to exchange phone numbers (date proxy) vs other Hinge recommendations. Notes original Gale-Shapley limitations for non-binary/heterosexual-only formulations and Hinge's engineering workaround.

## Project Relevance

**Low project relevance for retention/LTV ranking, credit assignment, and delayed-label modeling; moderate for reciprocal two-sided matching product design.**

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Maximize likelihood users "hit it off" and reach lasting relationships; retention/LTV/revenue/CTR not specified in source. |
| **(2) Credit assignment** | Not specified in source. |
| **(3) Label / horizon; delay / sparsity / censoring** | Liking/passing history; phone-number exchange as success proxy; horizon, delay, sparsity, censoring not specified in source. |
| **(4) Short-term vs long-term head fusion** | Not specified in source. |
| **(5) Prediction vs incrementality** | Not specified in source. |
| **(6) Offline / online eval** | Early market tests; 8× phone-number exchange rate vs other Hinge recommendations; delayed retention and two-sided interference not specified in source. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Explicit mutual pairing (both users see each other); stable roommate variant for gender-inclusive matching; congestion and revenue vs match trade-off not specified in source. |
| **(8) CTR → unified long-term migration** | Not specified in source. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Sarah Wells (TechCrunch); Justin McLeod (Hinge CEO, quoted)  
**Affiliations:** TechCrunch; Hinge  
**Venue:** TechCrunch  
**Year:** 2018  
**Relevance:** Peripheral  
**Priority:** 4
