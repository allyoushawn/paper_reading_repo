# Paper Analysis: Automated Decision Making at Grindr

**Source:** https://www.grindr.com/blog/automated-decision-making-and-grindr
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Automated Decision Making at Grindr
- **authors or company:** Shane Wiley (Chief Privacy Officer), with quoted input from Tom Quisel (Chief Technology Officer)
- **venue:** Grindr Company Blog
- **year:** 2023
- **URL:** https://www.grindr.com/blog/automated-decision-making-and-grindr
- **source type:** blog
- **direction:** D8
- **problem setting:** Corporate transparency statement on Automated Decision Making and AI use, responding to regulatory scrutiny (US state privacy proposals, EU AI Act, GDPR Article 22).
- **objective and label definition:** Not applicable — source states no ranking model is used for user discovery.
- **prediction or incrementality:** Not applicable for ranking; only binary security/moderation classifiers (spam accounts, non-compliant images) with human-in-the-loop override for false positives.
- **model architecture:** None for ranking/recommendation. Discovery shows recently online users matching manual filters (age, tribe, relationship status, etc.), sorted by distance with light randomization; security classifiers unspecified.
- **credit assignment:** Not applicable — no ranking or recommendation model to assign outcomes to impressions.
- **training data and counterfactual handling:** Not specified in source for security classifiers; no training data, labels, or counterfactual handling described.
- **offline and online evaluation:** Not specified in source; qualitative description of balancing false positives and false negatives in security pipeline only.
- **reported gains:** Not specified in source — no quantitative results reported.
- **applicability note for a two-sided dating recommender:** Industry baseline showing a major dating platform's production discovery can be a non-learned distance sort with user filters rather than a learned ranker — bounds how uniformly sophisticated dating-app ranking is in practice.
- **applicability note for a two-sided dating recommender:** No training objective, reciprocity modeling, congestion control, retention/LTV objective, or evaluation methodology — useful contrast case only, not a method for unified ranking design.
- **unverified claims:** Legal/policy self-assessment that ADM does not produce a "legal effect" under GDPR Article 22; no false-positive/false-negative rates disclosed for security classifiers.

## 1. Summary

Grindr's Chief Privacy Officer addresses regulatory confusion about Automated Decision Making and AI. Central claim: Grindr does not use any recommendation or matchmaking algorithm. Nearby search displays recently online users matching the searcher's filters, sorted by distance with occasional randomness. The only acknowledged automated systems are security/trust-and-safety classifiers (spam detection, non-compliant image flagging) with human review for false positives. Post frames future "smarter" features as aspirational with a transparency commitment.

## Project Relevance

**Low project relevance.** No ranking model, training objective, label, credit assignment, or evaluation methodology maps to Q1–Q6 or Q8. Narrow value as an industry data point for Q7: at least one large dating platform deployed no learned ranking as of publication, so migration from CTR/CVR-plus-uplift blend does not apply universally.

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Not applicable — no ranking model. |
| **(2) Credit assignment** | Not applicable. |
| **(3) Label / horizon; delay / sparsity / censoring** | Not applicable for ranking. |
| **(4) Short-term vs long-term head fusion** | Not applicable. |
| **(5) Prediction vs incrementality** | Not applicable for ranking. |
| **(6) Offline / online eval** | Not specified in source. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Non-learned distance sort; no reciprocity or congestion modeling. |
| **(8) CTR → unified long-term migration** | No learned ranker to migrate from. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Shane Wiley, Tom Quisel (quoted)  
**Affiliations:** Grindr  
**Venue:** Grindr Company Blog  
**Year:** 2023  
**Relevance:** Related  
**Priority:** 1
