# Policy Design for Two-sided Platforms with Participation Dynamics

**Source:** https://arxiv.org/pdf/2502.01792.pdf | **NLM source id:** 7fdbc3ee-d5de-4e48-b7ba-5b4f17b60ed2 | **Year / venue:** ICML 2025 (PMLR 267) | **Authors / affiliation:** Haruka Kiyohara, Sarah Dean (Cornell University); Fan Yao (University of Virginia) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Standard recommender policies (contextual bandits) assume static viewer and provider populations. In real two-sided platforms, viewers and providers engage in self-reinforcing "population effects": providers produce more when exposure increases, viewers stay when satisfaction increases, and provider growth further improves viewer satisfaction. Myopic-greedy policies that always match viewers to their currently-best providers concentrate exposure on already-large provider groups, driving minority-provider departures and reducing long-run social welfare. The paper formalizes co-evolving two-sided dynamics: viewer satisfaction s_k=Σ_l π_{k,l}q_{k,l}, provider exposure e_l=Σ_k π_{k,l}λ_k, with utility q_{k,l}=b_{k,l}+f_{k,l}(λ_l) split into static base preference and a population-driven quality term. It proves gradient dynamics converge to a stable Nash equilibrium, that myopic-greedy is optimal only under linear/homogeneous population effects, decomposes sub-optimality into policy regret (short-term) and population regret (long-term), and proposes a differentiable "look-ahead" policy (interpolation parameter β) that optimizes social welfare at a projected future reference population rather than the current one.

Unit of decision: per viewer-subgroup/provider-subgroup matching probability π_{k,l} (K viewer groups × L provider groups), not per individual touch. Outcome optimized: long-term social welfare R(π;λ)=Σ_k λ_k s_k (total viewer satisfaction weighted by population size) — not retention/engagement of individual users per se, but analogous aggregate welfare under population dynamics. Bias/exposure handling: the paper's core concern is exposure concentration (a structural, not individual, selection-bias analogue) — myopic-greedy over-allocates exposure to large provider groups; the look-ahead policy and an exposure-fairness constraint (Σ_k π_{k,l} ≤ 4η⁻¹/(C1C2)) prevent this, and dynamics are estimated via an explore-then-commit (ε-greedy burn-in + supervised learning) scheme.

## 2. Evidence
- **Synthetic:** K=L=20 subgroups, concave/sigmoid population dynamics, 20-dim quality features; two initial-population regimes (small: λ~N(20,10²); large: λ~N(100,30²)).
  - Small initial population: look-ahead (β=1.0) final welfare ~48,500 vs. myopic-greedy (β=0.0) ~25,000 vs. uniform random ~45,000 — nearly 2x myopic-greedy. Provider population grew to ~1,550 under look-ahead vs. collapsing to ~400 under myopic-greedy.
  - Large initial population: look-ahead sustains ~48,500 while myopic-greedy collapses to ~25,000 from provider departures.
- **KuaiRec real data** (4,676,570 watch-ratio samples, 1,411 viewers, 3,326 providers, clustered into K=L=20 via NCF embeddings): interpolated look-ahead (β=0.6) and pure look-ahead (β=1.0) reach ~9,500 total welfare vs. ~4,500 for uniform random (>2x), while preserving provider diversity.
- Baselines: myopic-greedy (β=0.0), uniform random, interpolated look-ahead (β∈[0.2,1.0]).

## 3. Limitations
- The look-ahead objective is non-convex; optimized via gradient ascent on a softmax approximation, without global-optimum guarantees.
- Framework operates at discrete subgroup granularity (K viewer groups × L provider groups); scaling to per-user granularity increases dimensionality substantially.
- Pure look-ahead (β=1.0) incurs short-term policy regret while building provider populations; an intermediate β (0.6) slightly outperformed β=1.0 on KuaiRec.
- Performance depends on accurately estimating population-dynamics functions during the burn-in period.

## 4. Prior works named
- Singh & Joachims 2018 — *Fairness of exposure in rankings* (KDD'18; exposure-fairness foundation)
- Mladenov et al. 2020 — *Optimizing long-term social welfare in recommender systems: A constrained matching approach* (ICML'20; long-term welfare under provider departure)
- Perdomo et al. 2020 — *Performative prediction* (ICML'20; stateful dynamics where policy shifts environment population)
- Li et al. 2010 — *A contextual-bandit approach to personalized news article recommendation* (WWW'10; standard static-population bandit baseline)
- Gao et al. 2022 (KuaiRec dataset) / He et al. 2017 (Neural Collaborative Filtering) — real-world benchmark and embedding model used

## 5. Project Relevance
- **Answers:** Q2
- **Attributes retention to individual interactions?** no — optimizes viewer-subgroup/provider-subgroup exposure allocation for aggregate long-term social welfare under population dynamics; does not attribute retention/engagement/active-days to individual interactions at all.
- **Transferable components:** two-sided participation-dynamics framing (swiper satisfaction and candidate-profile "supply" reinforcing each other); exposure-distributing / "growing the pie" allocation to avoid concentrating exposure on already-popular profiles; the policy-regret vs. population-regret decomposition as a conceptual lens for evaluating short-term vs. long-term costs of an attribution/ranking policy.
- **Required changes:** move entirely from subgroup-level matching-probability optimization to individual per-swipe sequence attribution; replace aggregate viewer-satisfaction/provider-exposure metrics with heterogeneous per-touch event modeling (swipe, like, match, message); re-anchor the welfare objective to a daily-recurring rolling N7 active-retention indicator per user.
- **On last-touch:** does not discuss last-touch/last-click attribution by name, but rigorously shows myopic-greedy policies (which optimize only immediate utility) are optimal only under a narrow linear/homogeneous condition and otherwise cause population collapse — a structural analogue to the critique that last-touch (a myopic heuristic) ignores dynamics beyond the immediate touchpoint.
- **Transfer rating:** background — a control/game-theoretic two-sided marketplace policy-design paper, not an attribution or retention-credit model; useful conceptually (population dynamics, exposure fairness) but not a direct building block for per-swipe credit assignment.
