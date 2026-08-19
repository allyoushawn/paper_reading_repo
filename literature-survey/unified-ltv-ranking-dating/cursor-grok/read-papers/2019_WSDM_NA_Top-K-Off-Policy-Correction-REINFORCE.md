# Survey Card

| Field | Value |
|-------|-------|
| **Title** | Top-K Off-Policy Correction for a REINFORCE Recommender System |
| **Authors / Company** | Minmin Chen, Alex Beutel, Paul Covington, Sagar Jain, Francois Belletti, Ed H. Chi / Google |
| **Venue / Year** | WSDM 2019 |
| **URL** | https://doi.org/10.1145/3289600.3290999 |
| **Source type** | Industry paper |
| **Direction** | D2 |
| **Problem setting** | YouTube neural candidate generator (RNN policy, millions of items): REINFORCE on logged trajectories with off-policy correction for multi-item (top-K) slate generation |
| **Objective + label + horizon + delay** | Immediate reward on clicked/watched items; long-term reward R aggregated over **4–10 hour** future window; primary online metric ViewTime |
| **Prediction or incrementality** | Policy optimization (REINFORCE policy gradient with off-policy importance weighting) |
| **Architecture** | CFN-RNN user state + softmax policy π_θ; separate behavior head β_θ′ (gradient blocked from RNN); sampled softmax training, ANN serving; Boltzmann exploration at serve |
| **Credit assignment** | Trajectory-level discounted return R_t assigned via policy gradient to each action in sequence; not item-level retention decomposition |
| **Training / counterfactual** | Off-policy correction π/β with weight capping (c=e³); top-K correction multiplier λ_K = K(1−π)^{K−1}; neural context-dependent β estimator trained on all logged items |
| **Offline / online eval** | Synthetic 10-action simulation; live YouTube candidate-gen A/B on ViewTime and videos viewed |
| **Reported gains** | Standard off-policy: no significant ViewTime lift but +0.53% videos viewed; top-K (K=16) vs standard (K=1): avoids −0.66% ViewTime drop; K=8 vs K=16: +0.15% ViewTime; raising cap c to e⁵: −0.52% ViewTime |
| **Dating applicability** | Off-policy top-K correction is directly relevant when ranking multiple candidates per impression from biased logs. Multi-hour reward horizon is a middle ground between instant match CTR and multi-day retention. |
| **Unverified claims** | None beyond NLM source; Q2/Q3 follow-up queries failed (MCP disconnect). |

**Community Reaction:** No significant community discussion found.

---

## 1. Core Problem and Key Contribution

**Core problem:** Industrial recommenders learn from logged feedback biased by historical policies; standard off-policy correction optimized for K=1 collapses softmax mass onto a single item, hurting multi-item slate quality. Online exploration is infeasible at YouTube scale.

**Key contributions:**
1. Scale REINFORCE to production candidate generation (millions of actions, billions of users).
2. Neural context-dependent behavior-policy estimator β from logged actions.
3. **Top-K off-policy correction** preserving probability mass for sub-top items in K-item slates.
4. Live experiments demonstrating off-policy correction and controlled Boltzmann exploration value.

## 2. Proposed Method or Architecture

**Policy π_θ:** CFN-RNN state transition; softmax π_θ(a|s) = exp(sᵀv_a/T)/Σ exp(sᵀv_a′/T); sampled softmax in training; ANN top-M approximate softmax at serve.

**Behavior β_θ′:** Second softmax on same RNN state with **blocked gradients** into RNN; trained on all trajectory items (including zero-reward impressions) vs π trained only on rewarded items.

**Top-K correction:** Probability item appears in size-K deduplicated set: α_θ(a|s) = 1−(1−π_θ(a|s))^K. Off-policy gradient uses α/β and multiplier λ_K = ∂α/∂π = K(1−π)^{K−1}, which aggressively boosts low-π items then zeros gradient once π is sufficient for top-K inclusion.

**Variance reduction:** Weight cap min(π/β, c); NIS and TRPO tested with limited online gain beyond capping.

**Exploration:** Boltzmann sampling over ANN top-M items; mix top-K′ deterministic + sample K−K′ from remainder.

## 3. Datasets and Baselines

**Simulation:** Stateless 10-action MDP; r(a_i)=i; skewed β(a_i)=(11−i)/55.

**YouTube production:** RNN candidate generator on homepage/watch-next; continuous training with <24h lag.

**Baselines:** Uncorrected policy gradient; standard K=1 off-policy correction; deterministic vs stochastic serving; varying K∈{1,2,8,16,32}; weight cap c∈{e³,e⁵}.

## 4. Key Quantitative Results

- **Standard off-policy vs control:** No statistically significant ViewTime change; **+0.53%** videos viewed (significant); ~3× more nominations from outside control top ranks.
- **Top-K vs standard (K=16 prod vs K=1):** **−0.66%** ViewTime for K=1; K=2 still **−0.35%** vs K=16; K=32 similar to baseline; follow-up K=8: **+0.15%** ViewTime (significant).
- **Weight cap:** c=e⁵ vs c=e³: **−0.52%** ViewTime (propensity overfitting).
- **Stochastic exploration (T=1):** No significant ViewTime change vs deterministic serve.
- **Simulation:** Uncorrected PG mimics biased β; standard correction converges to π(a₁)≈1; top-K retains mass on suboptimal high-reward items.

## 5. Limitations and Failure Modes

- No real-time online policy updates; must learn from historical mixture of policies.
- Simulation assumes stateless MDP; set-reward = sum of independent item rewards; sampling-with-replacement dedup makes final slate size variable.
- Separating π and β RNN encoders adds cost with **no metric improvement**.
- NIS and TRPO did not improve metrics beyond weight capping online.
- Brute-force ε-greedy exploration deemed harmful to UX at scale.
- Long-term reward still proxy (4–10h ViewTime), not multi-day retention.

## 6. Top Cited Prior Works

1. REINFORCE (Williams) — base policy-gradient algorithm.
2. Strehl et al. — off-policy correction with estimated behavior policy.
3. Covington et al. — YouTube recommender / RNN candidate generation context.
4. Schnabel et al. — IPS for biased feedback / cost of exploration.
5. Swaminathan & Joachims — propensity overfitting / batch learning from logged bandit feedback.
6. Schulman et al. (TRPO) — policy divergence regularization tested.
7. Joachims et al. — position/presentation bias in implicit feedback.

---

## Project Relevance (Q3)

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | **CTR-like proxies** (clicks) and **engagement proxy** (watch time / ViewTime). Retention, LTV, and revenue not specified as objectives. |
| **(2) Credit assignment** | Trajectory-level discounted return over **4–10 hours** back-propagated via REINFORCE to each recommended item action; not user-level multi-day retention decomposition. |
| **(3) Label / horizon; delay / sparsity / censoring** | Immediate zero reward on non-clicked items; long-term R over **4–10 hour** window; extreme action-space sparsity discussed. Multi-day retention delay/censoring not specified in source. |
| **(4) Short-term vs long-term head fusion** | Not specified in source (single policy head, not multi-task heads). |
| **(5) Prediction vs incrementality** | **Policy optimization / incrementality** via REINFORCE with off-policy correction. |
| **(6) Offline / online eval; delayed retention; two-sided interference** | Simulation + live YouTube A/B on ViewTime; **4–10 hour** delayed reward horizon. Multi-day delayed retention and two-sided interference not specified in source. |
| **(7) Reciprocity, congestion, fairness, revenue vs match quality** | Not specified in source. |
| **(8) Migration path from CTR-like model to unified long-term model** | Extend logged-feedback policy learning with **off-policy correction** and **top-K slate-aware gradients** before optimizing longer-horizon rewards; neural β estimator for mixed historical policies. |

---

## Reverse Citation Map

*(blank)*

---

## Meta Information

| Field | Value |
|-------|-------|
| **Date analyzed** | 2026-08-16 |
| **Workplace** | cursor-grok |
| **NLM source ID** | 7a977c61-586e-4d30-bdfb-ed4d50db5e0e |
| **Notebook ID** | 67046a44-7490-4fe5-b54a-3f39ef37fdd3 |
