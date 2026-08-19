# Optimizing Rankings for Recommendation in Matching Markets

- **Source index:** 118
- **Source ID:** `0139e40e-00b6-4551-8077-86cc02518a05`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Yi Su, Magd Bayoumi, Thorsten Joachims
- **Affiliation:** Cornell University
- **Year / venue:** 2021 / arXiv preprint
- **Direction / priority:** D8 matching-market ranking / Priority 3 (core)
- **URL:** https://arxiv.org/abs/2106.01941

## 1. Summary

The paper models an apply–accept market: proactive users inspect ranked options and apply; reactive users inspect applicants and accept. Both sides have relevance probabilities and limited attention. Because one user’s rank affects the load and examination order faced by everyone else, neither one-sided probability ranking nor a pairwise reciprocal score maximizes total matches. The proposed Social-Welfare Ranking jointly optimizes stochastic rankings for all proactive users via a tractable lower bound, while leaving final choices to users.

Synthetic tests show the largest advantage under steep examination drop-off and strong crowding. On a 925-person conference networking system, expected social welfare is 824.1 versus 763.8 for reciprocal relevance and 604.0 for naive relevance; over 88% of participants gain individual utility. On a 500×500 Libimseti dating sample, social welfare is 1199.2 versus 957.2 and 844.0. The reported values are model-based expected outcomes, not live match counts from a randomized policy test.

## 2. Experiment Critique

The framework explicitly models cascade attention, reciprocal relevance, and reactive-side capacity. It tests synthetic regimes and two real datasets, reports uncertainty over ten runs, and uses top-100 reranking to improve tractability.

The conference and dating evaluations infer relevance and simulate actions. Libimseti is restricted to the most active raters and imputes missing ratings with ALS, creating selection/model dependence. Relevance estimates are assumed accurate and unbiased in the theory. There is no causal online deployment comparison, and retention/adoption are discussed only as future strategic concerns.

## 3. Industry Contribution / Project Relevance

This is a strong template for replacing independent pair scores with joint slate allocation. In dating, expected value of A→B depends on how many other viewers see B and on where A appears in B’s inbound queue. The lower-bound optimization and top-k candidate generation suggest a feasible architecture: retrieve candidates, estimate bilateral long-term value, then globally rerank under load.

The paper’s welfare is expected match count, not retention or revenue. The project should define value over both users’ later trajectories, include conversation capacity and successful exits, and use causal exposure effects. A market-level optimizer can amplify model errors, so calibration and conservative constraints are critical.

## 4. Novelty

The contribution is joint optimization of personalized rankings in an apply–accept matching market with uncertain examination and capacity, rather than centralized assignment or local reciprocal scoring.

## 5. Dataset Availability

Libimseti is a known public dating-ratings dataset. The paper states the conference networking data will be published; an availability URL is **Not specified in source**. Paper code is **Not specified in source**.

## 6. Community Reaction

Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Protocol:** Proactive apply → reactive examination/accept
- **Objective:** Expected total matches/social welfare
- **Constraints:** Position-based attention and reactive-side capacity
- **Evaluation:** Synthetic plus networking and dating simulations
- **Online causal evidence:** None
- **Project role:** Joint market-level reranking blueprint
