# Parallel and Mini-Batch Stable Matching for Large-Scale Reciprocal Recommender Systems

- **notebook source_id:** `df9568a2`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Reciprocal recommender systems (RRSs) for two-sided matching platforms (job markets, online dating) have applied stable-matching theory with transferable utility (TU) to reduce recommendation concentration and increase total matches. However, the standard IPFP (Iterative Proportional Fitting Procedure) solver for TU matching has computational and memory costs that scale quadratically with the number of users, making it impractical beyond roughly tens of thousands of users. The paper proposes a GPU-parallel ("batch") reformulation of IPFP as matrix-vector operations, plus a memory-efficient ("mini-batch") variant that assumes low-rank matrix-factorization-style preference structure so only a partition of users' factor vectors need be held in memory at once. Experiments on a real online-dating dataset (Libimseti) and synthetic markets show the method matches or exceeds baseline recommenders in expected total matches while scaling to 1 million users on a single GPU without losing match count — where the standard batch approach runs out of memory beyond roughly 100,000 users.

## Method
The paper adopts the transferable-utility (TU) matching model (Choo & Siow 2006; Galichon & Salanié 2022): candidates `x` and employers/receivers `y` have observable joint utility `phi_{x,y} = p_{x,y} + q_{y,x}` plus unobserved Gumbel (type-I extreme value) noise. Under this structure, the expected-match-count-maximizing (social-welfare-maximizing) match probability matrix `mu` is the solution to a convex optimization problem that is the dual of an entropy-regularized optimal transport (OT) problem, with regularization weight `beta` controlling how uniform vs. preference-concentrated the resulting matching is.

- **IPFP (baseline solver):** a coordinate-descent algorithm (closely related to Sinkhorn's algorithm for OT) that alternately updates scaling vectors `u` (candidate side) and `v` (employer side) via `u = sqrt(n + s^2) - s`, `v = sqrt(m + s^2) - s`, where `s` involves a sum over the exponentiated joint-utility matrix — the pointwise-loop version scales in memory and time as O(|X||Y|).
- **Batch IPFP:** rewrites the same updates as matrix-vector products (`A v`, `Aᵀ u`, with `A = exp(Φ/2β)`), so the update can be computed as parallel matrix multiplication on a GPU rather than a per-pair loop.
- **Mini-batch IPFP:** assumes preferences factorize via low-dimensional factor vectors (matrix-factorization style — `p_{x,y} = <f_x, g_y>`, `q_{y,x} = <k_x, l_y>`, dimension `D << |X|,|Y|`). The user population is partitioned into mini-batches, and only one partition's factor vectors are loaded and updated at a time, reducing space complexity from O(|X||Y|) to roughly O(|X|) or O(|Y|), adjustable by batch size.
- Once `u`/`v` converge, the stable match pattern `mu` is recovered in closed form from the factor vectors (Eq. 11 in the paper).

## Datasets and Baselines
- **Real data:** Libimseti (online dating platform) — 500 male x 500 female users with the highest number of reciprocal ratings; missing ratings imputed via probabilistic matrix factorization (alternating least squares, ALS).
- **Synthetic data:** 500 employers x 1,000 candidates, preference matrices generated with a tunable "crowding" parameter λ ∈ {0, 0.25, 0.5, 0.75} controlling how concentrated preferences are across the market (method from Su et al. 2022); observed binary interactions sampled from Bernoulli distributions over the generated preferences; factor vectors recovered via implicit ALS (iALS).
- **Baselines:** Naive (unidirectional candidate-side preference only), Reciprocal (product of both-side preferences), CR (cross-ratio uniform of preferences, from Su et al. 2022 — could not be run to completion in tractable time on either dataset), Batch IPFP, Mini-batch IPFP.
- **Metric:** expected total number of matches (= social welfare in the TU model), computed using an exponentially decaying position-based examination function `v(k) = 1/exp(k-1)` (k = rank position).
- **Compute environment:** Intel Core i9-12900K CPU + single NVIDIA GeForce RTX 3080 (10GB) GPU; source code built on OTT-JAX (JAX-based optimal transport library).

## Results
- **Libimseti (500x500 real data):** Batch and mini-batch IPFP achieved the highest expected number of total matches among all five methods tested (Naive, Reciprocal, CR, Batch IPFP, Mini-batch IPFP), evaluated over 10 repeated runs with error bars (Figure 3; exact values not printed in text, shown only as a bar chart in the ~100–130-match range).
- **Synthetic data, crowding sweep (λ = 0, 0.25, 0.5, 0.75):** the IPFP-based methods (batch and mini-batch) maintain a higher expected match count than the Naive/Reciprocal/CR baselines as crowding increases, and degrade less under increased preference concentration; mini-batch IPFP's match count is slightly lower than batch IPFP's because the preference matrix is only approximated via the factor-vector product, but the gap is small (Figure 4).
- **Computational efficiency (synthetic, varying sample size n from 10² to 10⁶):**
  - GPU implementations are faster than CPU for both batch and mini-batch IPFP (Figure 5).
  - Batch IPFP (vanilla, full matrix in memory) hits an out-of-memory error beyond a data size of 10⁵ in the paper's hardware environment.
  - Mini-batch IPFP handles sample sizes up to 10⁶ (one million users) on a single GPU; memory usage scales near-linearly with sample size (not quadratically), largely independent of batch size `B` ∈ {1, 10, 100} tested (Figure 6). Execution time increases with batch size (as a roughly constant multiplicative factor) at fixed data size.
  - Varying factor-vector dimension `D` at fixed batch size (B=100) and n=10⁴: both execution time and memory usage of mini-batch IPFP increase in an almost linear relationship with `D` (Figure 7).

## Limitations
- The mini-batch method's memory efficiency depends on assuming preferences admit a low-rank, matrix-factorization-style factor structure — this is a modeling assumption, not a universally applicable guarantee.
- Mini-batch IPFP shows a slight reduction in the expected number of matches relative to batch IPFP, attributed explicitly to the factor-vector approximation of the true preference matrix.
- The CR (cross-ratio) baseline from prior work (Su et al. 2022) could not be run to completion in tractable time on either dataset, so it is excluded from the head-to-head comparison in some places.
- Evaluation is limited to one real dataset (Libimseti, subsampled to 500x500 users) plus synthetic markets — no live/field platform deployment or A/B test is reported (unlike the field-experiment paper on CoupLink in this same batch).
- Authors flag as future work: applying low-rank Sinkhorn factorization to further reduce the transport cost matrix's complexity, and computing derivatives of the preference matrix to backpropagate through to a unilateral recommendation model — i.e., the pipeline is not yet end-to-end differentiable/learnable.

## Heavily Cited Prior Works
- Choo, E. & Siow, A. (2006) — "Who marries whom and why," *Journal of Political Economy*. Origin of the TU matching market model.
- Galichon, A. & Salanié, B. (2021/2022) — "Cupid's invisible hand: Social surplus and identification in matching models," *Review of Economic Studies*. Establishes the TU-matching / entropy-regularized OT duality this paper builds on.
- Chen, K.-M., Hsieh, Y.-W., Lin, M.-J. (2023) — "Reducing recommendation inequality via two-sided matching: a field experiment of online dating," *International Economic Review*. Applied TU matching to RRSs with a live field experiment (~1,000 male-female matching data).
- Tomita, Y., Togashi, R., Hashizume, Y., Ohsaka, N. (2023) — "Fast and examination-agnostic reciprocal recommendation in matching markets," RecSys. Prior memory-efficient TU-matching inference method for reciprocal scores that this paper directly extends.
- Cuturi, M. (2013) — "Sinkhorn distances: Lightspeed computation of optimal transport," NeurIPS. Foundational OT/Sinkhorn algorithm.
- Knopp, P. & Sinkhorn, R. (1967) — "Concerning nonnegative matrices and doubly stochastic matrices," *Pacific Journal of Mathematics*. Origin of Sinkhorn scaling.
- Koren, Y., Bell, R., Volinsky, C. (2009) — "Matrix factorization techniques for recommender systems," *Computer*. Basis for the factor-vector representation used in the mini-batch method.

## Bibliography Fields
- **title:** Parallel and Mini-Batch Stable Matching for Large-Scale Reciprocal Recommender Systems
- **authors or organization:** Kento Nakada (Sony Network Communications, Inc.), Kazuki Kawamura (The University of Tokyo), Ryosuke Furukawa (Sony Network Communications, Inc.)
- **year:** 2024
- **venue or type:** RecSys in HR '24 (4th Workshop on Recommender Systems for Human Resources, co-located with the 18th ACM Conference on Recommender Systems), Bari, Italy; also posted as arXiv:2411.19214
- **link:** https://arxiv.org/pdf/2411.19214
- **tier tag:** Tier 3 academic method
- **what they did (≤80 words):** Reformulated TU (transferable-utility) stable matching for reciprocal recommender systems as an entropy-regularized optimal-transport problem solved by IPFP/Sinkhorn coordinate descent, then proposed GPU-parallel ("batch") and memory-efficient factor-vector-based ("mini-batch") computation methods. Showed the approach scales to 1 million users on a single GPU without losing expected match count, validated on a real dating dataset (Libimseti) and synthetic markets with varying preference crowding.
- **mechanism relevant to two-sided balancing (≤50 words):** Provides a scalable computational engine (Sinkhorn/IPFP) for solving capacity-constrained two-sided matching at real-platform scale (up to 1M users on one GPU) — the missing computational bridge between "we know exposure should be redistributed by capacity" and "can we actually compute it fast enough" for a live app.
- **metrics used, and the reported effect:** Expected total number of matches (social welfare); batch/mini-batch IPFP matched or exceeded Naive/Reciprocal/CR baselines on Libimseti and degraded less as synthetic-market crowding rose from 0 to 0.75; mini-batch IPFP scaled to n=10⁶ with near-linear memory, versus batch IPFP's out-of-memory failure beyond n=10⁵, at a small cost in match count from the low-rank approximation.
- **fit for a dating app:** high — explicitly built and tested for dating/job reciprocal recommendation at scale, using a real online-dating reciprocal-ratings dataset (Libimseti), and directly targets the production-scale computability of capacity-aware allocation.
- **confidence that the item is real and described correctly:** high — extracted directly from the full 8-page PDF, including all figures, tables, algorithms, and the reference list.

## Project Relevance
Directly relevant to **Layer 2 (capacity-aware exposure allocation)**: the TU-matching/Sinkhorn framework is a computational mechanism for solving capacity-constrained allocation at production scale, which is the missing piece between "redistribute exposure by capacity" mechanisms (e.g., LiJAR-style redistribution) and actually computing them fast enough for a live dating app with a large user base. The batch/mini-batch IPFP contributions are engineering-level scalability results that would let a capacity-aware allocation policy run over a full user base rather than a small candidate shortlist.

**Disanalogy to flag:** this paper's TU-matching objective maximizes aggregate expected matches under a general utility/entropy-regularization structure — it does not itself model or bound a *receiver's* reply capacity (no explicit per-user cap on likes or matches, unlike the ECDA mechanism in the "Integrating Predictive Models" paper from this same batch). It supplies the computational engine for capacity-aware allocation, not a capacity-modeling framework; capacity constraints (e.g., a q_j-style cap on expected likes/dates per receiver) would need to be layered on top. Does not address market-design levers (Layer 3, e.g., like limits or signaling) or ecosystem-level/interference-aware experimentation (Layer 4) — it is a pure computation/scalability paper for a fixed matching objective, with no field experiment or interference analysis.

## Reverse Citation Map
