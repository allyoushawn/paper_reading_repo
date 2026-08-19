# Paper Analysis: Fair Reciprocal Recommendation in Matching Markets

**Source:** https://doi.org/10.1145/3640457.3688130  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** Fair Reciprocal Recommendation in Matching Markets
- **authors or company:** Yoji Tomita, Tomohiko Yokoyama (CyberAgent)
- **venue:** RecSys 2024
- **year:** 2024
- **URL:** https://doi.org/10.1145/3640457.3688130
- **source type:** industry paper
- **direction:** D8
- **problem setting:** Two-sided reciprocal recommendation in matching markets (online dating, job matching); matches require mutual interest; recommendation opportunities concentrate on popular users, creating congestion and unfair exposure.
- **objective and label definition:** Maximize expected total matches (social welfare) subject to envy-freeness of recommendation opportunity; utility = expected match count per agent; labels from like/dislike and match/sorry interactions; 200×200 dense subsample for ALS preference estimation; horizon/delay/censoring not specified in source.
- **prediction or incrementality:** Predicts absolute expected match outcomes under a position-based ranking policy given offline-estimated asymmetric preference probabilities p₁(i,j), p₂(j,i); not incrementality modeling.
- **model architecture:** Probabilistic ranking policies π=(A,B) as doubly stochastic matrices under a position-based model; alternating Nash Social Welfare maximization via Frank-Wolfe on log NSW₁ and log NSW₂.
- **credit assignment:** Not specified in source; ranking policy optimized at market level, not per-exposure delayed-outcome attribution.
- **training data and counterfactual handling:** Synthetic markets (n=50/75, m=50, λ popularity bias) and Japanese online dating logs (200×200 ALS matrix factorization on male likes and female match/sorry); offline simulation only.
- **offline and online evaluation:** Offline Monte Carlo on synthetic and real dating logs reporting expected matches and envy counts; no live online A/B testing reported.
- **reported gains:** Real data (log examination): NSW 90.39 matches vs SW 111.37 with male envy 31 vs 434 and female envy 14 vs 331; inverse examination: NSW 59.37 matches vs SW 74.95 with male envy 19 vs 330 and female envy 8 vs 254.
- **applicability note for a two-sided dating recommender:** NSW post-processing on reciprocal preference scores is a concrete fairness layer when match-maximizing rankers starve low-popularity users of exposure.
- **applicability note for a two-sided dating recommender:** Does not address retention/LTV or credit assignment; cubic scaling (n²m + nm² variables) may limit production deployment at full catalog scale.
- **unverified claims:** none

## 1. Summary

**Core problem:** Match-maximizing reciprocal rankers concentrate recommendation opportunity on popular users, creating capacity bottlenecks and envy among less popular but similar users on both sides of a bipartite matching market.

**Key contribution:** Introduces envy-freeness of *being recommended* in reciprocal systems and proposes alternating Nash Social Welfare (NSW) maximization via Frank-Wolfe, with theoretical approximate double envy-freeness guarantees under mild preference-similarity assumptions.

**Method:** Models mutual match probability under a position-based examination model using doubly stochastic ranking matrices; defines opportunity matrices and envy across same-side agents; alternates left-side and right-side log-NSW Frank-Wolfe updates.

**Datasets/baselines:** Synthetic (balanced/unbalanced, λ∈[0,1], log/inverse examination); real Japanese dating 200×200 subset. Baselines: Naive, Prod, IterLP, TU, SW.

## 2. Experiment Critique

**Design:** Strong offline comparison across fairness-aware and welfare-maximizing baselines on both synthetic popularity sweeps and real dating interaction logs.

**Statistical validity:** Synthetic results averaged over simulation runs; real-data envy and match counts reported as point estimates without significance tests in source.

**Online experiments:** Not specified in source.

**Reproducibility:** Real dataset is proprietary; synthetic generation equations are specified; preference estimation via ALS described at high level.

**Overall:** Clear trade-off demonstrated between total matches and envy reduction; scalability flagged as a major practical limitation by authors.

## 3. Industry Contribution

**Deployability:** Conceptually a post-processing layer atop estimated reciprocal preferences; Frank-Wolfe over doubly stochastic matrices is computationally heavy at scale.

**Problems solved:** Individual-level fairness of recommendation opportunity in two-sided dating/job markets without abandoning reciprocal matching structure.

**Engineering cost:** Requires solving large doubly stochastic optimization; authors note potential limits for large-scale industrial scenarios.

## 4. Novelty vs. Prior Work

**Claimed novelty:** First envy-freeness formulation for reciprocal recommendation opportunity; NSW alternating maximization with approximate double envy-freeness theory.

**Prior work named in source (top 5–7):**
1. Saito & Joachims — envy-freeness and NSW for one-sided ranking fairness
2. Palomares et al. — reciprocal recommender systems survey
3. Su et al. — social welfare ranking optimization in matching markets
4. Tomita et al. — transferable-utility matching for congestion-aware reciprocal recommendation
5. Xia et al. (WE-Rec) — Walrasian equilibrium fairness in reciprocal recommendation
6. Do et al. — two-sided Lorenz-dominance fairness in rankings
7. Freeman et al. — double envy-freeness in matching meets fair division

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---------|------|---------|-------|
| Synthetic matching markets | Simulated | N/A | n=50/75, m=50, λ popularity parameter |
| Japanese online dating logs | Proprietary production | No | 200×200 active-user subsample |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**Low project relevance for retention/LTV ranking and credit assignment; high for two-sided market fairness.**

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Maximize expected total matches (social welfare); individual utility = expected match count. Retention, LTV, revenue, CTR proxies not specified in source. |
| **(2) Credit assignment** | Not specified in source. |
| **(3) Label / horizon; delay / sparsity / censoring** | Like/dislike and match/sorry signals; 200×200 dense subsample for sparsity; horizon, delay, censoring not specified in source. |
| **(4) Short-term vs long-term head fusion** | Not specified in source. |
| **(5) Prediction vs incrementality** | Predicts absolute expected match outcomes under a ranking policy; incrementality not specified in source. |
| **(6) Offline / online eval** | Offline simulation on synthetic and real dating logs only; delayed retention and two-sided interference not specified in source. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Core focus: reciprocal mutual-interest matching, popularity congestion, double envy-freeness across sides; revenue vs match quality trade-off not specified in source. |
| **(8) CTR → unified long-term migration** | Not specified in source. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yoji Tomita, Tomohiko Yokoyama  
**Affiliations:** CyberAgent  
**Venue:** RecSys 2024  
**Year:** 2024  
**PDF:** https://arxiv.org/abs/2409.00720  
**Relevance:** Related  
**Priority:** 2
