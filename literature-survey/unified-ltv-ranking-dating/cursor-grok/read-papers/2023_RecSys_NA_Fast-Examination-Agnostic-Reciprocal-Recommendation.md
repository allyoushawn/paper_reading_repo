# Paper Analysis: Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets

**Source:** https://doi.org/10.1145/3604915.3608774  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets
- **authors or company:** Yoji Tomita, Riku Togashi, Yuriko Hashizume, Naoto Ohsaka (CyberAgent)
- **venue:** RecSys 2023
- **year:** 2023
- **URL:** https://doi.org/10.1145/3604915.3608774
- **source type:** industry paper
- **direction:** D8
- **problem setting:** Reciprocal recommendation in job posting and online dating matching markets; must encode mutual preference and avoid concentrating matches on popular users with limited capacity.
- **objective and label definition:** Maximize expected total matches (social welfare) via market-clearing TU equilibrium scores μ*_{c,j}; unilateral preferences p_{c,j}, p_{j,c} from matrix factorization; real dating logs subsampled to 200×200 and 1000×1000 with k-core filtering and ALS imputation; horizon/delay/censoring not specified in source.
- **prediction or incrementality:** Predicts absolute equilibrium match probabilities under global capacity constraints; not incrementality modeling.
- **model architecture:** Choo–Siow transferable-utility matching with Gumbel error specification; IPFP solver for outside-option factors A_c, B_j; (2d+2)-dimensional inner-product embedding for MIPS retrieval at inference.
- **credit assignment:** Not specified in source; market-level equilibrium aggregation, not per-exposure delayed-outcome decomposition.
- **training data and counterfactual handling:** Synthetic markets (n∈{50,100,200,500}, λ crowding) and Japanese online dating logs; Monte Carlo simulation for evaluation; no online A/B tests.
- **offline and online evaluation:** Offline synthetic + real dating Monte Carlo (10,000 runs on 200×200; 1,000 on 1000×1000); Gini index for match fairness; authors note live A/B as future work.
- **reported gains:** n=200 synthetic: TU 332.91 expected matches vs Naive 219.56 and Reciprocal 273.86; 1000×1000 male-proactive: TU 538.97 vs Naive 375.82 and Reciprocal 491.12 (SW infeasible); reactive-side Gini 0.1019 (TU) vs 0.3872 (Naive).
- **applicability note for a two-sided dating recommender:** Production-shaped reciprocal ranker that replaces naive product fusion with market-clearing scores and stays MIPS-compatible for real-time retrieval.
- **applicability note for a two-sided dating recommender:** Examination-agnostic and scales where SW Frank-Wolfe fails, but degrades at λ=1.0 crowding and IPFP may not converge at large β; no retention/LTV objective.
- **unverified claims:** none

## 1. Summary

**Core problems:** (1) naive reciprocal fusion concentrates likes on popular users; (2) SW optimization needs position-based examination functions and costly doubly stochastic policies; (3) BvN decomposition is too slow for industrial inference.

**Key contributions:** TU matching with IPFP equilibrium; examination-agnostic deterministic ranking; MIPS-compatible (2d+2) embedding for vector search; improved fairness (Gini) with match volume competitive to SW.

**Method:** Estimate bilateral preferences; solve TU market equilibrium via IPFP for A_c, B_j; rank by μ*_{c,j}=exp((p_{c,j}+p_{j,c})/2β)·A_c·B_j; concatenate embeddings for inner-product retrieval.

**Datasets/baselines:** Synthetic (n up to 500, λ crowding, inv/exp/log examination for SW ablations); Japanese dating 200×200 and 1000×1000. Baselines: Naive, Reciprocal, SW (+ misspecified SW variants).

## 2. Experiment Critique

**Design:** Comprehensive offline sweep across market size, crowding, examination misspecification, and real dating subsets; SW included only where computationally feasible.

**Statistical validity:** Synthetic results averaged over 10 simulation runs; real-data Monte Carlo with reported point estimates.

**Online experiments:** Not specified in source; authors explicitly call live platform A/B future work.

**Reproducibility:** Real dating data proprietary; synthetic generation and IPFP equations fully specified.

**Overall:** Strong evidence for examination-robustness and scalability vs SW; authors transparent about λ=1.0 failure mode and IPFP convergence limits at high β.

## 3. Industry Contribution

**Deployability:** MIPS-compatible scoring enables standard ANN retrieval; avoids BvN decomposition at serving time; CyberAgent dating/job platform context.

**Problems solved:** Congestion-aware reciprocal ranking without specifying user attention curves; feasible at 1000×1000 where SW cannot run.

**Engineering cost:** O(|J||C|) per IPFP timestep; authors evaluated only up to 1000×1000 and note need for more efficient implementation at tens/hundreds of thousands of users.

## 4. Novelty vs. Prior Work

**Claimed novelty:** First TU matching application to reciprocal recommendation with examination-agnostic IPFP and MIPS inference acceleration.

**Prior work named in source (top 5–7):**
1. Su et al. — social welfare ranking optimization (SW baseline)
2. Choo & Siow — transferable utility matching foundation
3. Neve & Palomares — bilateral aggregation via matrix factorization means
4. Tomita et al. (MTRS 2022 talk lineage) — TU matching in dating markets
5. Various reciprocal fusion baselines (arithmetic/geometric/harmonic means)
6. Position-based model / examination function literature
7. Frank-Wolfe stochastic policy optimization references

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---------|------|---------|-------|
| Synthetic matching markets | Simulated | N/A | n∈{50,100,200,500}, λ∈[0,1] |
| Japanese online dating logs | Proprietary | No | 200×200 and 1000×1000 k-core subsets |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**Low project relevance for retention/LTV ranking and credit assignment; high for two-sided reciprocal ranking under congestion.**

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Maximize expected total matches (social welfare proxy); retention, LTV, revenue, CTR not specified in source. |
| **(2) Credit assignment** | Not specified in source. |
| **(3) Label / horizon; delay / sparsity / censoring** | Like/match interaction logs; k-core + ALS for sparsity; horizon, delay, censoring not specified in source. |
| **(4) Short-term vs long-term head fusion** | Not specified in source; unilateral dot-product preferences aggregated via fixed TU equilibrium formula (not learned multi-head fusion). |
| **(5) Prediction vs incrementality** | Predicts absolute equilibrium match probabilities; incrementality not specified in source. |
| **(6) Offline / online eval** | Offline Monte Carlo on synthetic and real logs; Gini fairness metric; live A/B and delayed retention not specified in source. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Core: mutual preference + congestion control via market clearing; Gini improvements vs Naive/Reciprocal; revenue vs match trade-off not specified in source. |
| **(8) CTR → unified long-term migration** | Not specified in source. |

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yoji Tomita, Riku Togashi, Yuriko Hashizume, Naoto Ohsaka  
**Affiliations:** CyberAgent  
**Venue:** RecSys 2023  
**Year:** 2023  
**PDF:** https://arxiv.org/abs/2306.09060  
**Relevance:** Related  
**Priority:** 2
