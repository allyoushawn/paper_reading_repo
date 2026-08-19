# User Fairness, Item Fairness, and Diversity for Rankings in Two-Sided Markets

- **notebook source_id:** `722d4cc7`
- **extraction method:** direct PDF read (NotebookLM unavailable)

**CITATION CORRECTION:** manifest said "User Item Fairness Diversity Two Sided Markets" (no year/venue given), the document says the paper is Wang & Joachims, **ICTIR '21** (ACM SIGIR International Conference on the Theory of Information Retrieval, July 2021, Virtual/Canada).

## Summary
Wang and Joachims prove theoretically that user fairness, item fairness, and diversity in two-sided-market ranking are three independent objectives: optimizing any one alone can drive the other two to zero utility and can fail Pareto-efficiency for them. To resolve this, they propose **TSFD Rank** (Two-Sided Fairness and Diversity ranking), the first ranking algorithm that explicitly enforces all three simultaneously — a convex-optimization step that jointly satisfies user fairness (a concave social-welfare objective over user groups) and item fairness (merit-proportional exposure across item groups), followed by a novel Birkhoff–von Neumann (BvN) decomposition step that samples diverse rankings consistent with the fairness-optimal exposure matrix. On a new benchmark movie-recommendation dataset with actor-race item groups and synthetic male/female user-intent groups, TSFD achieves perfect item fairness and near-best user fairness and diversity simultaneously, while single-objective baselines each sacrifice the other two.

## Method
Rankings are represented by a marginal rank-probability matrix Σ^{π,q} (doubly stochastic: rows/columns sum to 1), from which a policy's utility, user-group fairness, item-group fairness, and diversity are all defined as functions of Σ (plus, for diversity, the actual sampled permutation). **User fairness** is a concave social-welfare function UF(π|q) = Σ_UG ρ_UG · f(U(π|UG,q)) over user groups' utilities (f concave, e.g., log, giving diminishing returns / equalizing incentive). **Item fairness** adopts merit-exposure disparate-treatment constraints from Singh & Joachims 2018: exposure per item group must be proportional to that group's merit, E(π|DG_m,q)/M(DG_m,q) = E(π|DG_n,q)/M(DG_n,q) for all group pairs. **Diversity** is a submodular (diminishing-returns) function of per-ranking intent coverage. TSFD Rank runs in two steps: (1) solve a convex program that maximizes UF(Σ|q) subject to the item-fairness linear constraints and doubly-stochastic constraints on Σ (solved globally optimally, e.g., via MOSEK); (2) since many different ranking policies can realize the same Σ, decompose Σ into a distribution over permutation (ranking) matrices via a greedy BvN decomposition algorithm that, at each iteration, uses local search to pick the feasible permutation maximizing diversity, subtracts its selection probability from Σ, and repeats until Σ is exhausted. The authors formally show (Theorems 1–4, Tables 1–2) that maximizing utility, item fairness, user fairness, or diversity alone can each zero out or fail Pareto-efficiency for the other criteria, motivating the combined optimization.

## Datasets and Baselines
The authors construct the first benchmark dataset with intent, user-group, and item-group annotations: 100 movies across 5 genres (Romance 20, Comedy 25, Action 25, Thriller 15, Sci-Fi 15; treated as "intents"), with lead-actor race as item group ({black-lead: 20, white-lead: 80}); item relevance to a genre-intent is each movie's IMDB rating minus 6 (to expand relevance range). Users are split into two synthetic groups (male, female; default male proportion ρ_male = 0.6) with distinct, tunably-similar intent distributions over the 5 genres. Compared policies: (a) maximize overall utility (PRP baseline), (b) maximize item fairness only, (c) maximize user fairness only, (d) maximize diversity only, and (e) TSFD Rank — all combined with the same greedy BvN decomposition for sampling, using a submodular greedy approximation algorithm with two matroid constraints for the diversity step. Results averaged over 5,000 samples of 15 randomly-selected movies each (equivalent to 50,000-sample averaging per reported figure).

## Results
Default-setup comparison (Table 3; standard error of every reported value < 0.001):

| Policy optimizing | Utility | Item unfairness | User fairness | Diversity | Diversity UB |
|---|---|---|---|---|---|
| Utility | 1.518 | 0.186 | 1.447 | 1.016 | 1.016 |
| Item fairness | 1.509 | **0.000** | 1.437 | 1.010 | 1.013 |
| User fairness | 1.498 | 0.193 | **1.476** | 1.052 | 1.062 |
| Diversity | 1.428 | 0.185 | 1.390 | **1.214** | 1.214 |
| **TSFD Rank** | 1.489 | **0.000** | 1.466 (2nd-best) | 1.045 (3rd-best) | 1.055 |

TSFD achieves item unfairness of exactly 0.000 (tied best), the second-best user fairness (1.466, essentially matching the user-fairness-only policy's 1.476), and third-best diversity (1.045, close to the second-best 1.052) — while sacrificing only a small amount of raw utility (1.489 vs. 1.518 max). Sensitivity analyses (Figure 2, a–h) show: as user-intent similarity between the two groups decreases from 0.9 to 0, the minority (female) group's utility ratio U_female/U_male drops sharply for policies not optimizing user fairness, while TSFD tracks almost the same (near-flat) ratio as the user-fairness-only policy; as male group proportion rises from 0.6 to 0.9, the same pattern holds; under simulated extrinsic bias to black-lead-movie relevance (bias factor b), TSFD tracks the item-fairness-only policy's near-linear, controlled exposure ratio while utility-/user-fairness-/diversity-only policies amplify the bias. No p-values are reported (deterministic-style simulation averages with reported standard errors, not hypothesis tests).

## Limitations
- Assumes user-group and item-group membership are known at ranking time; the paper notes elsewhere that group membership is "typically not known" in practice, a gap it does not resolve.
- The item merit function M(DG,q) is application-specific and chosen ad hoc (they use average within-group relevance); different merit definitions would change item-fairness results.
- TSFD's two-step design explicitly prioritizes user and item fairness first and treats diversity as secondary — a stated value judgment — so it does not guarantee maximal diversity or maximal intent coverage (their own Table 1 shows TSFD, unlike an intent-coverage-focused policy, does not guarantee covering the maximum amount of intent).
- Finding the diversity-maximizing permutation within a BvN step is NP-hard in general; the paper uses a local-search heuristic (switching pairs of items) and reports it tried more expensive exhaustive search up to position 3 and "found the difference to be small," i.e., the diversity step is not globally optimal.
- The benchmark dataset (movies, actor-race groups, synthetic user intents) is constructed by the authors for this paper, not drawn from a live two-sided marketplace or reciprocal-recommendation setting.

## Heavily Cited Prior Works
- Singh & Joachims 2018 — "Fairness of Exposure in Rankings" (KDD) — source of the merit-exposure disparate-treatment item-fairness constraints adopted here
- Patro, Biswas, Ganguly, Gummadi, Chakraborty 2020 — "FairRec: Two-Sided Fairness for Personalized Recommendations in Two-Sided Platforms" (WebConf) — envy-free two-sided fairness baseline discussed in related work
- Gale & Shapley 1962 — "College admissions and the stability of marriage" — foundational two-sided matching-market theory
- Biega, Gummadi, Weikum 2018 — "Equity of Amortizing Individual Fairness in Rankings" (SIGIR) — amortized/individual exposure fairness
- Sühr, Biega, Zehlike, Gummadi, Chakraborty 2019 — "Two-sided fairness for repeated matchings in two-sided markets: A case study of a ride-hailing platform" (KDD) — closest prior two-sided repeated-matching fairness work
- Zehlike & Castillo 2020 — "Reducing disparate exposure in ranking: A learning to rank approach" (WebConf)
- Patro, Chakraborty, Ganguly, Gummadi 2020 — "Incremental fairness in two-sided market platforms: On smoothly updating recommendations" (AAAI)

## Bibliography Fields
- **title:** User Fairness, Item Fairness, and Diversity for Rankings in Two-Sided Markets
- **authors or organization:** Lequn Wang, Thorsten Joachims (Department of Computer Science, Cornell University)
- **year:** 2021
- **venue or type:** ICTIR '21 — ACM SIGIR International Conference on the Theory of Information Retrieval (academic)
- **link:** https://par.nsf.gov/servlets/purl/10309937
- **tier tag:** Tier 3 academic method
- **what they did (≤80 words):** Formally proved that user fairness, item fairness, and diversity are independent, mutually conflicting ranking objectives in two-sided markets (each can zero out or fail Pareto-efficiency for the others), then proposed TSFD Rank, a two-step convex-optimization-plus-BvN-decomposition algorithm that jointly enforces all three, and validated it on a new benchmark movie-recommendation dataset with intent, user-group, and item-group annotations.
- **mechanism relevant to two-sided balancing (≤50 words):** Merit-proportional exposure constraints (item fairness) throttle over-exposure of any one item group, analogous to redistributing exposure away from over-subscribed "superstar" profiles; the concave social-welfare user-fairness objective is a ready-made way to weight allocation decisions toward the worse-off user group.
- **metrics used, and the reported effect:** Utility, item unfairness (deviation from merit-proportional exposure), concave user-welfare fairness score, submodular diversity score, and a diversity upper bound. TSFD achieves 0.000 item unfairness and near-best (2nd of 5) user fairness (1.466 vs. best 1.476) and diversity (1.045 vs. best 1.214) simultaneously, at a small utility cost (1.489 vs. max 1.518).
- **fit for a dating app:** medium — the merit-proportional exposure mechanism and concave-welfare group-fairness objective are directly reusable as a capacity-aware allocation lever, but items here (movies) have no capacity of their own that exposure depletes, unlike a dating profile's scarce reply bandwidth — see disanalogy below.
- **confidence that the item is real and described correctly:** high — all theorems, algorithm structure, dataset description, and Table 3/Figure 2 numbers were read directly from the paper's body text and tables.

## Project Relevance
Relevant to **layer 2 (capacity-aware exposure allocation)**: the item-fairness merit-exposure constraint is precisely the "redistribute exposure away from over-subscribed profiles toward the merit-deserving long tail" lever the project needs, with a convex-optimization guarantee of global optimality and a formally proven non-zero-utility guarantee for every group. The paper's zero-utility and utility-efficiency theorems (any single-objective policy can starve the other objectives) are directly citable justification for why the project's four modeling layers must be co-optimized rather than bolted on independently — exactly the failure mode described (e.g., a pure reciprocal-scoring optimizer could starve capacity-aware allocation, or vice versa). **Disanalogy that must be flagged:** this is not a reciprocal/mutual-interest setting — items (movies) have unlimited "capacity" to be shown to any number of users, so "item fairness" here allocates exposure over a static, non-depleting supply. There is no notion of a shown profile's own reply budget being consumed by the exposure it receives, which is the core scarce resource in the project's dating-market framing. The paper also has **no reciprocal-scoring layer** (no mutual like-back probability model — user preferences are one-directional relevance scores), **no market-design levers** (no like limits, curated batches, or signaling), and **no ecosystem/interference metrics** (no match Gini, wasted-likes rate, or two-sided retention; fairness is measured in a single static ranking, not over repeated interactions or online experimentation). The mechanism (convex fairness optimization + BvN-based diverse sampling) is a strong candidate building block for layer 2, but needs to be paired with a genuine reciprocal-capacity model before it addresses the project's central "wasted likes" problem.

## Reverse Citation Map

