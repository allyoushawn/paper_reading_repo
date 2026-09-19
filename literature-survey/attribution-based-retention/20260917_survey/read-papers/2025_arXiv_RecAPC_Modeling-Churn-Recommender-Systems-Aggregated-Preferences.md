
# Modeling Churn in Recommender Systems with Aggregated Preferences

**Source:** https://arxiv.org/pdf/2502.18483.pdf | **NLM source id:** 20670606-4205-4316-938c-c86aaaec03b0 | **Year / venue:** 2025, arXiv 2502.18483 | **Authors / affiliation:** Gur Keinan, Omer Ben-Porat — Technion, Israel Institute of Technology | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Motivated by privacy regulation (GDPR/CCPA, iOS ATT) forcing recommenders to rely on aggregated personas/clusters instead of individual histories, the paper models sequential recommendation to an anonymous user as a POMDP/belief-walk ("Rec-APC") where the RS holds a prior over user-type clusters, recommends a content category each round, and a single dislike causes **immediate, total session churn** (0 future reward). **Unit of decision:** per recommended content category per round (not individual-user credit — this is a planning/policy paper, not an attribution paper). **Outcome optimized:** expected social welfare = expected cumulative number of liked recommendations before churn. **Confounding/selection handling:** none in the attribution sense; instead, Bayesian belief updates over user-type clusters after each *positive* feedback (negative feedback ends the session, so no further learning from it), explicitly trading off immediate reward vs. moving the belief to a more informative point for future rounds. Proves (Theorem 4.1) that for instances with distinct preferences, the optimal policy provably converges to a fixed myopic recommendation after finite time, and shows the naive myopic policy can be arbitrarily suboptimal (Proposition 2.5).

## 2. Evidence
- **Synthetic benchmark:** instances with |user types| ∈ {5,...,100} and varying category counts, generated via cosine-similarity latent vectors.
- **Real-world benchmark:** MovieLens 1M (1M ratings, 6,040 users, 3,706 movies) turned into probability/prior matrices via Spectral Co-clustering.
- **Baselines:** myopic policy, best-fixed-action policy, SARSOP (state-of-the-art point-based POMDP solver).
- **Results:** the paper's branch-and-bound algorithm matches SARSOP's solution quality while running faster — e.g., at M=100 user types/K=10 categories, ~15ms vs. SARSOP's ~175ms (>10× speedup); on MovieLens 60×60, ~0.22s vs. SARSOP's ~0.45s (>2× faster). Belief-uncertainty decay under the optimal policy fits an exponential curve with R²≥0.98.
- No deployment or online experiment; this is a purely algorithmic/simulation paper.

## 3. Limitations
- Binary churn assumption: a single dislike causes total, immediate departure — ignores partial tolerance or graded satisfaction (explicitly flagged as a simplification, with a sketched POMDP extension for richer feedback left unimplemented).
- Branch-and-bound degrades relative to SARSOP when categories vastly outnumber user types (e.g., ~660ms vs. SARSOP's ~125ms at K=100), since its branching factor scales with K.
- No polynomial-time algorithm or NP-hardness proof is given for the exact optimal policy.
- Assumes a static, known preference matrix P and prior q — no modeling of non-stationary preferences or within-session drift.

## 4. Prior works named
- Ben-Porat, Cohen, Leqi, Lipton & Mansour (2022) — "departing bandits" attrition-under-churn model; the closest prior formulation, restricted to 1–2 users/categories vs. this paper's general matrices.
- Kurniawati, Hsu & Lee (2009), **SARSOP** — point-based POMDP solver used as the benchmark.
- Pineau, Gordon & Thrun (2003) — point-based value iteration for POMDPs.
- Dhillon (2001) / George & Merugu (2005) — spectral co-clustering used to derive user-type/category matrices from MovieLens.
- Dwork (2006) / Javanmard & Mirrokni (2024) — differential privacy / anonymous lookalike-clustering motivation for the aggregated-preference setting.

## 5. Project Relevance
- **Answers:** Q2 (background/negative case — a 2025 recsys paper studying session engagement under churn, but not attributing multi-day retention to individual interactions).
- **Attributes retention to individual interactions?** No — optimizes cumulative in-session likes before churn; does not perform multi-touch credit assignment or attribute multi-day active-day/retention outcomes to historical interactions.
- **Transferable components:** Bayesian belief tracking over user-persona clusters updated on positive feedback; upper/lower value bounds for pruning candidate sequences by churn risk; the finite-time exploration→exploitation convergence result.
- **Required changes:** would need to shift from *online single-session policy planning* to *offline sequence-level credit attribution*; extend binary like/dislike-terminates-session feedback to heterogeneous multi-stage funnel events where negative feedback (a left swipe) does not end the session; retarget the objective from in-session cumulative likes to a daily-recurring N7 active-retention label.
- **On last-touch:** not discussed at all — the paper neither mentions nor critiques last-touch/last-click attribution.
- **Transfer rating:** background — a well-executed churn/exploration-exploitation POMDP paper adjacent to engagement modeling, but it is a policy-planning method, not an attribution method, and requires substantial reformulation to be relevant.
