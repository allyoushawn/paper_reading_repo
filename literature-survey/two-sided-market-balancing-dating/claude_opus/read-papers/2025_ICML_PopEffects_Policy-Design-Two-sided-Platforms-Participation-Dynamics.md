# Policy Design for Two-sided Platforms with Participation Dynamics

- **notebook source_id:** `e0ef0297`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
This paper is the first to study recommender policy design on two-sided platforms (viewers and content providers) under **population effects**: viewer satisfaction grows with the provider population's quality, and the provider population grows with the exposure it receives, creating a feedback loop the authors call "growing the pie." They show via control- and game-theoretic analysis that the standard "myopic-greedy" policy (recommend on immediate utility only) can starve minority provider groups of exposure, shrink the provider population, and produce *lower* long-run welfare than even a uniform-random policy. They decompose regret into "population regret" (myopic policy ignoring future population shifts) and "policy regret," prove the myopic policy is optimal only when population effects are linear/homogeneous across provider groups, and propose a **look-ahead policy** that optimizes utility against the *projected future* population instead of the current one. On both a synthetic simulation and a real-data (KuaiRec) simulation, the look-ahead policy dominates myopic-greedy and is competitive with or better than uniform-random on total welfare.

## Method
- **Setup:** K viewer subgroups, L provider subgroups; policy π is a K×L stochastic matrix (probability of allocating provider group l to viewer group k). Viewer satisfaction `s_k = Σ_l π_{k,l} q_{k,l}` and provider exposure `e_l = Σ_k π_{k,l} λ_k` (λ = subgroup populations). Base utility decomposes as `q_{k,l} = b_{k,l} + f_{k,l}(λ_l)`, where `f_{k,l}` is a monotonically increasing "population effect" function (more providers in a group → higher perceived quality).
- **Population dynamics:** `λ_{t+1,k} = (1-η_k)λ_{t,k} + η_k λ̄_k(s_{t,k})` for viewers, symmetric for providers, with reactiveness hyperparameter η ∈ [0,1] and a reference-population function λ̄(·).
- **Game-theoretic equivalence:** the dynamics are exactly the gradient-ascent trajectory of a (K+L)-player concave game; a Nash equilibrium always exists (Theorem 1) and gradient-based two-sided dynamics provably converge to one when reactiveness is small enough — in contrast to prior one-sided-market results where NE existence/convergence can fail.
- **Sub-optimality of myopic-greedy:** Theorem 3 / Proposition 2 show myopic-greedy is guaranteed optimal only when the population-effect functions f are linear and homogeneous across provider groups; with heterogeneous f, myopic-greedy is provably sub-optimal because it ignores "population regret" (Theorem 2's regret decomposition).
- **Proposed algorithm — look-ahead policy:** `π^(d) := argmax_π R(π̄¹_t(π); λ̄_t(π))`, i.e., optimize against the *reference population that the policy π itself would induce* rather than the current population, using a softmax relaxation of the myopic policy for differentiability and gradient ascent (closed-form gradient given in Appendix A; autograd usable in practice). The deployed policy interpolates look-ahead and myopic-greedy: `π_t = β·π_t^(d) + (1-β)·π_t^(m)`, with β a tunable short-vs-long-term knob (β=1.0 is pure look-ahead).
- Dynamics/effect functions are estimated in practice via an explore-then-commit epsilon-greedy burn-in period plus supervised regression (Section 5.1).

## Datasets and Baselines
- **Synthetic simulation:** K=L=20 subgroups, base utility from random 20-dim Bernoulli embeddings, concave sigmoid population dynamics, heterogeneous population-effect functions across provider groups (Eq. 12–13). Small- and large-initial-population regimes tested.
- **Real-data (KuaiRec, dense variant; Gao et al. 2022):** 4,676,570 viewer-provider interactions, 1,411 viewers, 3,326 short-video providers, watch-ratio as feedback, neural collaborative filtering (He et al. 2017) for base utility, viewers/providers clustered into K=L=20 subgroups, population effects fit via smoothing splines (Reinsch 1967) on empirical data.
- **Baselines compared:** myopic-greedy (β=0), uniform random policy, and the look-ahead policy at β ∈ {0.0, 0.2, ..., 1.0}.

## Results
- **Synthetic (small initial population), Figure 1:** myopic-greedy policy's total welfare and provider population *decline* over 200 timesteps (welfare drops to roughly the low-20,000s range and provider population falls from ~1000 to well under 500), while the look-ahead ("long-term") policy and uniform-random both keep growing (welfare reaching roughly the mid-to-high 40,000s range).
- **Synthetic, Figure 2 (varying β):** pure look-ahead (β=1.0) increases provider populations while myopic-greedy (β=0.0) decreases them; β=1.0 achieves the highest total welfare and best (least negative) population regret among all β; all interpolated β values perform reasonably well.
- **KuaiRec real-data experiment (Figure 5):** unlike the synthetic setting, myopic-greedy *outperforms* uniform-random here, and look-ahead is competitive with myopic after convergence to the NE — but the myopic policy retains nonzero population regret while look-ahead retains nonzero policy regret. The interpolated policy at **β=0.6 performed best** among tested configurations, and "all interpolated policies with various β perform quite well." Look-ahead (β=1.0) achieves total welfare comparable to myopic-greedy while maintaining a provider population close to uniform-random's (the largest), showing it allocates exposure more efficiently across subgroups.
- No single p-value-style significance test is reported; results are comparative curves over 200 timesteps (synthetic) / real-data simulation, averaged implicitly via the deterministic dynamics model rather than repeated trials.

## Limitations
- The look-ahead objective (Eq. 10) is potentially non-convex; the paper relies on a softmax relaxation and gradient ascent rather than a global-optimality guarantee.
- Real-world dynamics estimation is imperfect: the KuaiRec experiment must estimate λ̄ and f via regression, and the authors add synthetic perturbation noise to population dynamics "to account for the difficulty in learning the real-world dynamics" — an acknowledged approximation.
- The framework assumes population-effect functions f are monotonically increasing and (in the linear-optimality theorem) requires linearity/homogeneity for guarantees; heterogeneous, concave, or saturating effects (which the authors say matter empirically) break the myopic-optimality result and are only handled heuristically by the look-ahead policy, not with formal optimality guarantees.
- The KuaiRec "real-data" experiment is still a *simulation* of population dynamics layered on top of real interaction data — not a live platform deployment.
- The interpolation weight β must be tuned; the paper shows β=1.0 works well in both settings but does not give a principled rule for choosing β a priori.

## Heavily Cited Prior Works
- Mladenov et al. (2020) — "Optimizing long-term social welfare in recommender systems: a constrained matching approach" (models provider departure/exposure thresholds; closest prior population-dynamics work)
- Huttenlocher et al. (2023) — "Matching of users and creators in two-sided markets with departures" (extends Mladenov et al. to viewer departures)
- Singh & Joachims (2018) — "Fairness of Exposure in Rankings" (motivates the exposure-fairness argument)
- Hron et al. (2022) — "Modeling content creator incentives on algorithm-curated platforms" (strategic content-provider game theory, fixed total population)
- Jagadeesan, Garg & Steinhardt (2022) — "Supply-side equilibria in recommender systems"
- Perdomo, Zrnic, Mendler-Dünner & Hardt (2020) — "Performative prediction" (related dynamics-under-policy framing)
- Wang & Joachims (2021) — "User fairness, item fairness, and diversity for rankings in two-sided markets"

## Bibliography Fields
- **title:** Policy Design for Two-sided Platforms with Participation Dynamics
- **authors or organization:** Haruka Kiyohara, Fan Yao, Sarah Dean — Cornell University & University of Virginia
- **year:** 2025
- **venue or type:** ICML 2025 (Proceedings of the 42nd International Conference on Machine Learning, PMLR vol. 267, Vancouver)
- **link:** https://raw.githubusercontent.com/mlresearch/v267/main/assets/kiyohara25a/kiyohara25a.pdf
- **tier tag:** Tier 3 academic method (real-data component uses a public offline dataset, KuaiRec, with simulated population dynamics — not a live platform deployment)
- **what they did (≤80 words):** Formalized "population effects" — feedback loops where viewer satisfaction depends on provider population size/quality and vice versa — in two-sided recommender platforms. Proved myopic-greedy exposure policies can shrink provider populations and social welfare relative to uniform-random allocation, characterized when myopic-greedy is/isn't optimal, and proposed a look-ahead policy optimizing against the population the policy itself would induce, validated on synthetic and KuaiRec-based simulations.
- **mechanism relevant to two-sided balancing (≤50 words):** Exposure-fair (vs. exposure-concentrated) allocation across provider subgroups prevents polarized equilibria and provider-population collapse; a look-ahead objective that anticipates policy-induced population shift, interpolated against short-term greedy via a tunable weight β, balances immediate utility against long-term ecosystem health.
- **metrics used, and the reported effect:** Total welfare (sum of viewer-side satisfaction), total viewer/provider population trajectories, cumulative/population/policy regret. Look-ahead (β=1.0) sustains provider-population growth and total welfare comparable to or exceeding myopic-greedy and uniform-random across both synthetic and KuaiRec-based experiments; myopic-greedy alone can cause provider-population collapse and depressed long-run welfare in the synthetic setting.
- **fit for a dating app:** high — directly models the feedback loop between exposure allocation and the "supply" population's health/departure, and formally shows that concentrating exposure on a favored subgroup produces population collapse and reduced total welfare — a close conceptual analogue to over-concentrating likes on top-desirability daters and starving/churning the rest.
- **confidence that the item is real and described correctly:** high — full paper text (including all theorems, algorithm, and both experiment sections) was read directly from the PDF.

## Project Relevance
Addresses **Layer 2 (capacity-aware exposure allocation)** and **Layer 4 (ecosystem metrics/experimentation)** directly. The paper's "population effect" feedback loop — exposure concentration causing provider-side collapse and reduced total welfare — is structurally the same failure mode the project worries about (a small set of highly desirable users absorbing likes while low-desirability users get little exposure, lose reply/interest, and churn). Its exposure-fair vs. exposure-concentrated policy contrast, and its formal regret decomposition into short-term ("policy regret") vs. long-term population effects ("population regret"), give a principled framework for reasoning about why myopic reciprocal-scoring/allocation choices can be locally optimal yet destroy the market over time. The look-ahead policy (optimize against the population the policy itself induces) is a reusable design pattern for capacity-aware, feedback-loop-aware exposure allocation.

**Disanalogy to flag:** the "capacity" limiting factor here is population growth/churn from under-exposure, not a hard reciprocal reply-capacity constraint — providers are content/video producers, not individual daters with finite time/attention to reply to matches. There is no explicit two-sided-consent (both-sides-must-like) matching mechanism in this paper; it is single-sided exposure allocation (viewers consume provider content) rather than reciprocal matching. The mechanism transfers at the level of "exposure concentration destroys the market," not at the level of reciprocal like-back modeling.

## Reverse Citation Map
