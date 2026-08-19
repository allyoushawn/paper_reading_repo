# MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets

- **notebook source_id:** `0a3983b2`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Matching platforms (job boards, dating apps) need reciprocal recommender systems (RRSs) that account for preferences on both sides, but concentrating recommendation opportunity on a few popular users causes congestion and dissatisfaction. The paper formalizes "optimality of direct effects" — whether a user's own recommendation list is the best possible given everyone else's lists — and defines "mutual optimality" as a state where every user's list is simultaneously optimal in this sense (a pure-strategy Nash-equilibrium analogue). It proposes MODE (Mutually Optimal recommendation in Direct Effects), a deterministic iterative algorithm that computes such lists efficiently using a closed-form recursion for ranking probabilities. On synthetic and real online-dating data, MODE matches or beats existing stochastic optimal-social-welfare methods in expected number of matches while running orders of magnitude faster, and substantially outperforms deterministic baselines (Naive, Reciprocal-score, TU) at scale.

## Method
Framework (following Su et al. 2022): candidates (proactive side) each get a ranked list of K employers/matches; they apply to the k-th item with position-based-model (PBM) examination probability v_{i,k} and application probability p_{i,σ_ik}. Employers (reactive side) receive ranked lists of applicants (size ≤ L), examine them with probabilities w_{j,ℓ}, and accept ("match") with probability q_{j,τ}. A user's utility is split into a **direct effect** (from their own recommendation list) and an **indirect effect** (from other users' lists, since being ranked well on someone else's list raises the chance of matching). MODE optimizes only direct effects, defining a recommendation list σ*_i as *optimal in direct effects* if it maximizes i's own utility given everyone else's lists σ_{-i}, and *mutually optimal* if this holds for all i simultaneously — the pure-strategy Nash equilibrium of the induced game. Algorithm: (1) **RankingProbability** (Algorithm 1) recursively computes, for each employer j, the probability distribution of a candidate's rank in j's applicant list under any deterministic policy, in closed form (Proposition 3.3), avoiding the combinatorial sum used by prior work. (2) **MODE** (Algorithm 2) iterates: given current policy σ^{t-1}, compute ranking probabilities, then for each candidate i compute a "gain" g_{i,j} = p_{i,j} · Σ_ℓ r_{i,j,ℓ} · w_{j,ℓ} · q_{j,i} for every possible target j, and set i's new list to the top-K targets by gain. If the policy stops changing, it is mutually optimal (a pure-strategy NE) and returned; if it cycles or hits a max-iteration cap T, the algorithm returns whichever policy in the iteration history had the highest expected social welfare.

## Datasets and Baselines
**Synthetic data:** randomly generated markets with J = n employers, I = 1.5n candidates, n ∈ {10, 20, 50, 100}; preference scores blend a random uniform term and a popularity term controlled by crowding parameter λ ∈ {0, 0.1, …, 1.0}; three examination-probability shapes ("log", "inv" = 1/k, "exp").
**Real-world data:** behavioral data (~1,000 users of gender A and ~1,000 of gender B) from "a large online dating platform," covering "like"/"nope" actions and "thank"/"sorry" responses; preferences (p, q) estimated via matrix factorization with ALS.
**Baselines:** Naive (rank by own preference p_{i,j} only), Reciprocal (rank by p_{i,j}·q_{j,i} product), TU (Tomita et al. 2023 — matching score from a transferable-utility economic matching model), ApproxSW (Su et al. 2022 — Frank-Wolfe optimization of a lower-bound approximation of social welfare), DirectSW (Frank-Wolfe optimization of the exact social welfare using RankingProbability).

## Results
- **Real-world 200×200 users** (normalized to Naive = 1.00, Gender A proactive): Reciprocal 1.363, TU 1.379, ApproxSW 1.505, DirectSW 1.499, **MODE 1.466**. Gender B proactive: Reciprocal 1.779, TU 1.737, ApproxSW 1.923, DirectSW 1.927, **MODE 1.867**. MODE trails the (much more expensive) stochastic methods only slightly and beats all deterministic baselines.
- **Real-world 1,000×1,000 users** (ApproxSW/DirectSW infeasible at this scale): Gender A proactive — Naive 1.000, Reciprocal 1.165, TU 1.251, **MODE 1.438**; Gender B proactive — Naive 1.000, Reciprocal 1.314, TU 1.436, **MODE 1.687**. MODE's expected matches are >10% higher than the next-best deterministic method (TU) in both cases.
- **Synthetic data (n=50, λ=0.8, "inv" exam):** MODE achieves expected-match counts as high as the stochastic ApproxSW/DirectSW methods across most λ, and higher than Naive/Reciprocal/TU, especially at large λ (heavy popularity skew).
- **Sum of sub-optimality of direct effects** (regret, summed over candidates) is "almost zero in all cases" under MODE and substantially lower than other methods; proportion of candidates with non-zero sub-optimality under MODE is about 10% at n=50 default settings, versus 55–75% for Naive/Reciprocal.
- **Compute cost at n=100:** ApproxSW and DirectSW need >10 hours; MODE needs only a few seconds — "substantially faster."
- **Convergence:** MODE converges to a true mutually-optimal (fixed) policy in 82% of samples under the default synthetic setting (n=50, λ=0.8, "inv"); convergence rate varies by examination type and market size but non-convergence has "little effect on social welfare" (the returned max-history policy performs comparably).
- Appendix reports Gini index of user utilities and % of users better off under MODE vs. each baseline — MODE dominates Naive and Reciprocal on both fairness metrics; comparison to ApproxSW/DirectSW/TU depends on the parameter setting.

## Limitations
- MODE is a heuristic: mixed-strategy Nash equilibria are intractable to compute in general (PPAD-hard), and pure-strategy mutual optimality is not guaranteed to exist, so MODE can fail to converge and fall into a cycle (documented empirically: 18–100% non-convergence depending on settings).
- Framework assumes a position-based examination model with known/estimated examination probabilities per user — real-world examination behavior may deviate.
- Illustrated primarily as a job-posting-style K/L slot-limited matching problem; while online dating is stated as directly analogous, the empirical real-world experiment section is relatively brief (single platform, single snapshot).
- No formal guarantee that a mutually optimal policy, when it exists, is unique or socially optimal — it addresses individual-level direct-effect optimality/fairness, not global welfare maximization (that is what ApproxSW/DirectSW target instead, at far higher compute cost).

## Heavily Cited Prior Works
- Su, Bayoumi, Joachims (2022) — "Optimizing rankings for recommendation in matching markets," ACM Web Conference — source of the RRS ranking framework and ApproxSW.
- Tomita, Togashi, Hashizume, Ohsaka (2023) — "Fast and examination-agnostic reciprocal recommendation in matching markets," RecSys — source of the TU method.
- Choo, Siow (2006) — "Who marries whom and why," JPE — matching-with-transferable-utility model underlying TU.
- Xia, Yin, Xu, Yu (2019) — "WE-Rec: a fairness-aware reciprocal recommendation based on Walrasian equilibrium."
- Tomita, Yokoyama (2024) — "Fair reciprocal recommendation in matching markets," RecSys.
- Tomita, Yokoyama (2026) — "Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach," ACM Trans. on Recommender Systems.
- Nash (1950, 1951) — foundational game-theory papers on equilibrium in n-person games, motivating the mutual-optimality/NE analogy.

## Bibliography Fields
- **title:** MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets
- **authors or organization:** Yoji Tomita (CyberAgent, Inc., Tokyo, Japan)
- **year:** 2026
- **venue or type:** RecSys '26 — 20th ACM Conference on Recommender Systems, Sept 27–Oct 02, 2026, Minneapolis, MN, USA (ACM, DOI 10.1145/3773078.3831764)
- **link:** https://arxiv.org/pdf/2608.01731
- **tier tag:** Tier 2 applied-on-real-platform-data (academic single-author method, but evaluated on real online-dating behavioral data from an industry platform; author is at CyberAgent, a company operating dating apps)
- **what they did (≤80 words):** Defined "mutual optimality of direct effects" for reciprocal recommender lists (an NE-style fairness/stability notion) and proposed MODE, an iterative deterministic algorithm using a closed-form ranking-probability recursion to compute near-mutually-optimal recommendation lists efficiently, evaluated against social-welfare-optimizing and heuristic baselines on synthetic and real dating-platform data.
- **mechanism relevant to two-sided balancing (≤50 words):** Iteratively re-ranks each user's K/L-slot recommendation list by expected gain given the current state of everyone else's lists, converging toward a state where no user could improve their own list unilaterally — directly limiting concentration of exposure/opportunity on popular users under fixed slot capacity.
- **metrics used, and the reported effect:** Expected number of matches (social welfare), sum/proportion of per-candidate sub-optimality (regret), Gini index of utilities, computation time. MODE reaches near-SW-optimal expected matches (within ~2–4% of the best stochastic method) at a small fraction of the compute cost, and cuts sub-optimality/inequality sharply versus Naive/Reciprocal baselines.
- **fit for a dating app:** high — built and evaluated directly on reciprocal, capacity-limited (K applications, L examined applicants) dating-platform data; targets exactly the "concentration of opportunities on popular users" problem the project frames as wasted likes/reply-capacity scarcity.
- **confidence that the item is real and described correctly:** high — read directly from the PDF (arXiv 2608.01731, RecSys '26 camera-ready), all details independently verified against the text/figures/tables.

## Project Relevance
Directly relevant to three of the four modeling layers. **Layer 1 (reciprocal scoring):** the gain function g_{i,j} = p_{i,j}·Σ r_{i,j,ℓ}·w_{j,ℓ}·q_{j,i} is exactly a like-back-probability-conditioned score, using the reactive side's expected examination/acceptance behavior. **Layer 2 (capacity-aware exposure allocation):** the K/L slot limits and the ranking-probability recursion model per-user recommendation capacity explicitly, and MODE's whole objective — preventing "opportunities from being concentrated too heavily on a few popular users" — is precisely the wasted-likes/skewed-desirability problem in the project's north star. **Layer 4 (ecosystem metrics):** the appendix's Gini index of utilities and sub-optimality distribution are directly usable as match-Gini-style fairness metrics. No engagement with market-design levers (layer 3, e.g. like limits or signaling) or with interference-aware experimentation.

## Reverse Citation Map
