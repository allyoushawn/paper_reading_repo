# From Clicks to Conversions: Recommendation for long-term reward

**Source:** https://arxiv.org/pdf/2009.00497 | **NLM source id:** cc6d80d3-4a03-479f-b5fc-eb0d2322dfcb | **Year / venue:** 2020, REVEAL '20 workshop (RecSys) | **Affiliation:** ENS Paris Saclay & Criteo | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Industry conversion-optimized recommendation relies heavily on last-click sales attribution, which rewards clicks merely correlated with conversions rather than causing them. The paper extends the RecoGym simulator from a static contextual-bandit environment into a full RL environment where ad recommendations actively change the user's hidden conversion state, and shows this exposes and fixes last-click attribution's failure mode. **Unit of credit:** per recommendation action/ad click. **Outcome optimized:** conversion/sales volume (a long-term reward), moving away from CTR. **Bias handling:** each click updates a hidden user "conversion feature" vector as a convex combination `δ ← (1-κ)δ + κΛ_a`; the paper introduces a causal graph that allows conversions unmediated by any ad click, and applies a discounting mechanism to attributed sales — under an assumed strict "post-click incrementality," this discount separates causally-incremental clicks from merely-correlated ones, directly targeting the "would have converted anyway" selection-bias problem.

## 2. Evidence
Evaluated entirely inside an extended RecoGym simulation (no live A/B or production data). Baselines: standard contextual-bandit agents and last-click-attribution-optimized agents. Result stated qualitatively: the discounted-attribution agent "outperforms all state-of-the-art bandit baselines" in driving sales; as a 3-page workshop paper, detailed numeric tables and full parameter sweeps are explicitly deferred to a promised full-length follow-up.

## 3. Limitations
Validated only in simulation (RecoGym), not on live ad traffic. The user-state update is a simplified linear convex combination, a strong structural assumption versus real-world intent dynamics. The discounting mechanism's correctness rests on a strict "post-click recommendation incrementality" assumption. The paper is explicitly a preliminary report — full experiments and sensitivity analysis are deferred to a subsequent publication.

## 4. Prior works named
- Rohde et al. (2018) — RecoGym: a reinforcement learning environment for product recommendation in online advertising (the simulator extended here)
- Sutton (1985) — Temporal Credit Assignment in Reinforcement Learning
- Xin et al. (2020) — Self-Supervised Reinforcement Learning for Recommender Systems
- Mann et al. (2019) — Learning from Delayed Outcomes via Proxies with Applications to Recommender Systems
- Wen et al. (2019) — Conversion Rate Prediction via Post-Click Behaviour Modeling

## 5. Project Relevance
- **Answers:** Q2 (directly about attribution, but for conversions, not retention/engagement/days-active)
- **Attributes retention to individual interactions?** No — this models e-commerce conversion attribution, not user retention, engagement, or days-active; it does not touch in-app return behavior at all.
- **Transferable components:** the hidden-state-update mechanism for how a click shifts user intent; the discounting/de-biasing logic that separates causally-incremental clicks from merely-correlated ones; the shift from static bandit to full sequential RL where actions change state.
- **Required changes:** the target outcome must move from a one-time e-commerce conversion event to a daily recurring N7 active-retention indicator; RecoGym's homogeneous ad-click event space needs to become a heterogeneous dating funnel (swipe/like/match/message) with event-specific embeddings; and the mechanism needs to produce explicit per-touch fractional credit rather than a single discount factor on the final click.
- **On last-touch:** This is the paper's central topic — it explicitly names and critiques last-click conversion attribution as an industry billing heuristic that is "not a perfect reward-shaping mechanism," biased toward clicks correlated with, not causing, conversions; it proposes a discounting alternative as a fix.
- **Transfer rating:** adaptable — the clearest and most directly on-topic articulation in this batch of *why* last-touch/last-click attribution is biased, though its fix (a single discount factor under a simulation-only, one-shot-conversion setting) needs real extension to fractional, multi-day, multi-event dating-platform credit.
