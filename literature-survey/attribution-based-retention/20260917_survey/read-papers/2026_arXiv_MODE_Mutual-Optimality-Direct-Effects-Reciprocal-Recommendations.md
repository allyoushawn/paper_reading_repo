# MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets

**Source:** https://arxiv.org/pdf/2608.01731.pdf | **NLM source id:** c951f48e-7cc6-4e8c-a92c-dccc076edab6 | **Year / venue:** RecSys 2026 (arXiv 2608.01731) | **Authors / affiliation:** Yoji Tomita (CyberAgent, Inc., Tokyo) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries; Query A required one retry due to an empty first response)

## 1. Summary
On two-sided matching platforms (online dating, job posting), reciprocal recommender systems (RRSs) must balance mutual preferences while avoiding congestion — a small fraction of highly popular users receive most applications/likes, but their match capacity is physically limited. Prior fixes either solve computationally expensive stochastic linear programs (Su et al.'s approximated social welfare via Frank-Wolfe) or use deterministic transferable-utility scores (Tomita et al. 2023) that ignore competition dynamics, and over-mitigating congestion for platform-wide welfare can sacrifice individual satisfaction. The paper decomposes a user's utility into a direct effect (from their own recommendation list) and an indirect effect (from others' lists, via downstream ranking competition), and defines "mutual optimality of direct effects" — a Nash-equilibrium-like solution where every user's own list is optimal given everyone else's lists (no individual is sacrificed for aggregate welfare). It derives a recursive algorithm (Algorithm 1) to compute exact ranking probability distributions r_{i,j,ℓ}=Pr(rank of i among j's applicants = ℓ | σ), then proposes MODE (Algorithm 2), an iterative best-response method updating top-K lists by candidate gain g_{i,j}=p_{i,j}·Σ_ℓ r_{i,j,ℓ}·w_{j,ℓ}·q_{j,i} until convergence or cycle detection.

Unit of decision/utility: per user recommendation list σ_i / candidate-employer (or swiper-candidate) pair. Outcome optimized: social welfare = total expected matches SW(σ)=ΣᵢΣⱼ P^σ_{i,j}·P^σ_{j,i}, and mutual optimality (minimizing per-candidate sub-optimality/regret). This is not a retention/engagement attribution paper — bias handling here means correcting for two-sided congestion/competition (position-based examination model, recursive ranking-probability computation) rather than selection bias in a retention outcome.

## 2. Evidence
- **Synthetic markets:** n∈{10,20,50,100} employers, 1.5n candidates, congestion parameter λ∈[0,1], three examination-probability types (log/inv/exp).
- **Real-world online dating logs** (~1,000 male / ~1,000 female users; like/nope and thank/sorry actions; preferences estimated via ALS matrix factorization), tested at 200×200 and 1000×1000 scale.
- At 1000×1000: MODE achieved 1.438x (Gender A proactive) and 1.687x (Gender B proactive) normalized expected matches vs. Naive baseline (1.0x), beating Reciprocal (1.314x) and TU (1.436x).
- At 200×200: MODE 1.466x/1.867x (Gender A/B) vs. Naive 1.0x, close to but slightly below stochastic ApproxSW (1.505x/1.923x) and DirectSW (1.499x/1.927x).
- Computation speed at n=100: MODE runs in a few seconds vs. >10 hours for ApproxSW/DirectSW (~10,000x speedup).
- Sub-optimality: near-zero summed regret across candidates in most settings; ~10-18% of synthetic trials fall into non-convergent cycles (resolved by returning the best historical policy).
- Baselines: Naive (rank by p_i,j), Reciprocal (p_i,j·q_j,i), TU (transferable-utility matching), ApproxSW, DirectSW (Frank-Wolfe social welfare).

## 3. Limitations
- Pure-strategy convergence is not guaranteed (game-theoretic cycles occur in ~18% of default synthetic settings); mixed-strategy equilibria always exist but are PPAD-hard to compute.
- In smaller markets, MODE's deterministic policy is slightly below stochastic welfare-maximizing baselines (ApproxSW/DirectSW).
- Depends entirely on pre-estimated two-sided preference scores (p_i,j, q_j,i from offline matrix factorization); degrades if these are misspecified.
- Ignores post-match interaction quality — optimizes expected matches only, not conversation length or downstream retention.

## 4. Prior works named
- Su, Bayoumi & Joachims 2022 — *Optimizing rankings for recommendation in matching markets* (WWW'22; approximated social welfare via Frank-Wolfe)
- Tomita et al. 2023 — *Fast and examination-agnostic reciprocal recommendation in matching markets* (RecSys'23; transferable-utility (TU) matching score baseline)
- Nash 1950/1951 — equilibrium theory (game-theoretic foundation for "mutual optimality")
- Joachims, Swaminathan & Schnabel 2017 — position-based examination model (PBM)
- Pizzato et al. 2010/2013 — RECON, early reciprocal-recommender foundations for online dating

## 5. Project Relevance
- **Answers:** Q2
- **Attributes retention to individual interactions?** no — MODE optimizes reciprocal-recommendation list ranking to maximize expected mutual matches under a game-theoretic mutual-optimality criterion; it does not attribute retention, engagement, or active-day outcomes to individual interaction logs at all.
- **Transferable components:** two-sided preference and position-based examination modeling (proactive swipe preference p_i,j and reactive match preference q_j,i); recursive ranking-probability computation for estimating true match likelihood under competition/congestion; the mutual-optimality guarantee that no individual user's experience is sacrificed for aggregate platform gains.
- **Required changes:** shift entirely from static list-ranking/match-maximization to sequence-level fractional retention-credit attribution; extend the binary like/nope, thank/sorry action set to a full heterogeneous funnel (swipe, like, match, message); replace the single-period expected-matches objective with a daily-recurring rolling N7 active-retention target.
- **On last-touch:** does not discuss last-touch/last-click by name, but shows naive one-sided preference ranking (analogous to any non-causal heuristic) creates severe congestion and yields substantially fewer matches than mutually-optimal two-sided ranking.
- **Transfer rating:** background — a game-theoretic two-sided matching/congestion algorithm for match-list optimization, not an attribution or retention-credit model; useful context on dating-market dynamics (congestion, reciprocal preference) but not a building block for the per-swipe credit pipeline itself.
