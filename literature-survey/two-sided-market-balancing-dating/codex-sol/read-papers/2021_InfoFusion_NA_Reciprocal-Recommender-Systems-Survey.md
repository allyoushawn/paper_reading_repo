# Paper Analysis: Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation

**Source:** https://www.ujaen.es/grupos-de-investigacion/asia/sites/investigacion_asia/files/uploads/node_evento/revistas_indexadas/1-s2.0-S1566253520304267-mainext.pdf  
**Date analyzed:** 2026-08-18

---

## 1. Summary

Palomares et al. survey reciprocal recommender systems (RRS), in which both people must accept a recommendation for it to succeed. They formalize reciprocal recommendation as two unilateral preference estimates combined by a fusion operator, organize content-based, collaborative-filtering, model-based, and hybrid approaches, and review representative systems including RECON, RCF, RWS, LFRR, and CCR. The survey reports that prior studies use success/failure rate, reciprocal rank, precision, recall, and AUC; examples include CCR's nearly 70% success rate—about twice a random-neighbor baseline—and RRK's 14–17% improvement over IBCF and CSVD on Czech dating data. It also emphasizes popularity bias, sparsity, cold start, scalability, limited live-user evaluation, and the lack of capacity-explicit formulations.

## 2. Experiment Critique

This is a survey, not a new empirical model. The quantitative findings are results reported from underlying studies, so they should be checked in those primary papers before use as decision-grade evidence. The source explicitly notes that most RRS evaluation is offline, live-user evaluation is rare, and reciprocity complicates A/B testing because people in different treatment groups may be recommended to one another.

## 3. Industry Contribution

The paper provides a useful implementation map for reciprocal ranking: estimate both directional preferences, fuse them with an operator such as the harmonic mean or cross-ratio uninorm, and evaluate outcomes as bilateral successes and failures. It also identifies load-balancing approaches such as RWS, stochastic/stable matching, and Walrasian-equilibrium formulations. Engineering cost and production latency are not quantified.

## 4. Novelty vs. Prior Work

The paper claims to be the first exhaustive modern analysis focused on RRS after foundational work by Pizzato et al. It organizes and compares Pizzato et al.'s *Reciprocal Recommenders* and *RECON*, Pizzato et al.'s *Recommending People to People*, Xia et al.'s *Reciprocal Recommendation System for Online Dating*, Cai et al.'s people-to-people collaborative filtering, and Guy et al.'s social-network invitation recommender.

## 5. Dataset Availability

The survey identifies commercial dating logs (Australian dating service, Baihe, Pairs, a Czech dating service), a 90,000-user/1.4-million-expression-of-interest dating dataset, and public Speed Dating, MITx/HarvardX, Twitter, Meetup, and XING RecSys Challenge datasets. Direct download links and a unified evaluation package are not specified in source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Mechanism.** The source directly supports reciprocal scoring through two directional preference estimates and a fusion function. It also describes popularity-aware RWS and stochastic/stable matching as mechanisms that spread recommendation load more evenly.  
**Metrics/effect.** Reciprocal success rate, failure rate, reciprocal rank, precision, recall, and AUC are source-supported. CCR reports nearly 70% success, about twice a random-neighbor baseline; RRK reports 14–17% improvement over IBCF/CSVD. Total matches, conversations, match Gini, wasted likes, and two-sided retention are **Not specified in source.**  
**Capacity/congestion.** The source recognizes overloaded popular profiles and underexposed users, but hard reply-capacity constraints and wasted-like accounting are **Not specified in source.**  
**Dating mapping.** High fit as a conceptual and bibliographic foundation for reciprocal scoring and popularity-aware balancing; the project should treat its capacity relevance as qualitative rather than as a validated capacity-allocation model.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md](./2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md) | Novelty vs. Prior Work — Background | Cites Palomares et al. (2021) as an RRS survey. |
| [2026_Wantedly_PersonalizedAggregation_Personalizing-Preference-Aggregation.md](./2026_Wantedly_PersonalizedAggregation_Personalizing-Preference-Aggregation.md) | Novelty vs. Prior Work — Background | Cites Palomares et al. (2021) as surveying reciprocal aggregation. |

## Meta Information

**Authors:** Iván Palomares, James Neve, Carlos Porcel, Luiz Pizzato, Ido Guy, Enrique Herrera-Viedma  
**Affiliations:** University of Granada; University of Bristol; Commonwealth Bank of Australia AI Labs; eBay Research; King Abdulaziz University  
**Venue:** Information Fusion  
**Year:** 2021 (published online 2020)  
**PDF:** available  
**Relevance:** Core  
**Priority:** 3

## Annotated Bibliography Fields

- **Title:** Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation
- **Authors/organization:** Iván Palomares, James Neve, Carlos Porcel, Luiz Pizzato, Ido Guy, Enrique Herrera-Viedma; University of Granada, University of Bristol, Commonwealth Bank of Australia AI Labs, eBay Research
- **Year:** 2021
- **Venue/type:** Information Fusion; journal survey
- **Link:** https://www.ujaen.es/grupos-de-investigacion/asia/sites/investigacion_asia/files/uploads/node_evento/revistas_indexadas/1-s2.0-S1566253520304267-mainext.pdf
- **Tier tag:** Tier 3
- **What they did (≤80 words):** Formalized reciprocal recommendation as fusion of two directional preference estimates; organized algorithms, fusion operators, metrics, datasets, and application areas; reviewed representative dating, recruitment, learning, and social-network systems; and identified research gaps in fairness, explainability, data sparsity, evaluation, and emerging applications.
- **Mechanism relevant to two-sided balancing (≤50 words):** Combine both sides' predicted preferences with mutuality-sensitive operators, then use popularity-aware weighting or stochastic/stable matching to avoid repeatedly recommending overloaded popular users while neglecting the long tail.
- **Metrics and reported effect:** Success/failure rate, reciprocal rank, precision, recall, AUC. CCR: nearly 70% success, about 2× random-neighbor baseline; RRK: 14–17% improvement over IBCF/CSVD. Market-health metrics requested by this project are otherwise not specified.
- **Dating-app fit:** High — directly surveys reciprocal dating recommendation and popularity-load balancing, though not hard capacity allocation.
- **Confidence:** High — peer-reviewed survey; quantitative claims remain secondary reports of cited studies.
