# Estimating long-term outcome of algorithms (Long-term Off-Policy Evaluation and Learning)

**Source:** https://research.atspotify.com/2024/05/estimating-long-term-outcome-of-algorithms | **NLM source id:** 36958832-a712-4f91-8e1f-65d73cdca0ce | **Year / venue:** 2024, Spotify Research blog (underlying paper: WWW 2024) | **Affiliation:** Spotify Research | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Measuring an algorithm's long-term outcome (e.g., retention months later) via a full online experiment is slow and risky. Existing offline alternatives both have structural flaws: Long-term Causal Inference (LCI) assumes short-term surrogates (clicks, likes) fully explain the long-term outcome ("surrogacy"), which is often violated and biases estimates; standard Off-Policy Evaluation (OPE, e.g. IPS/Doubly Robust) avoids that assumption but ignores short-term signals entirely, producing high variance when long-term outcomes are sparse/noisy. LOPE (Long-term Off-Policy Evaluation) decomposes `long-term reward ≈ surrogate effect + action effect`. **Unit of credit:** per action/candidate policy — this is a policy-level evaluation method, not a per-touch attribution method. **Outcome optimized/estimated:** long-term outcome (e.g., retention) of an entire recommendation policy. **Bias handling:** the surrogate effect is estimated via importance weighting over short-term rewards (reducing variance), and the residual action effect is estimated via reward regression (removing the bias LCI incurs by assuming away action-specific effects) — this targets model-selection bias, not swipe-level selection bias.

## 2. Evidence
Monte Carlo simulations varying sample size (n=200–1,000), noise level, and degree of surrogacy violation, plus real-world A/B test logs at Spotify. Baselines: the infeasible "skyline" long-term experiment, LCI, and OPE (IPS, Doubly Robust). Results: LOPE achieves the lowest MSE among feasible methods in all tested conditions — a 36% MSE reduction vs. Doubly Robust OPE at n=200 (driven by variance reduction from using short-term signals), and a 71% MSE reduction vs. LCI at n=1,000 (driven by eliminating surrogacy bias). On real Spotify A/B tests, LOPE consistently gave more accurate long-term estimates than the alternatives.

## 3. Limitations
If surrogacy holds perfectly, LOPE's extra action-effect regression step is unnecessary overhead versus plain LCI (though still unbiased). Requires both historical data and short-term trial data with observable surrogate rewards, which is an added data-availability requirement. In extremely small samples (n<200) with very sparse/noisy long-term outcomes, LOPE's variance can still exceed naive LCI's despite lower bias.

## 4. Prior works named
- Athey et al. — Surrogate Index / Long-term Causal Inference (LCI) framework
- Horvitz & Thompson — Inverse Propensity Scoring (IPS)
- Bang & Robins — Doubly Robust estimators
- Off-Policy Evaluation literature in recommender systems (general)
- Short-term surrogate outcome theory in causal inference (general)

## 5. Project Relevance
- **Answers:** Q1 (recent, 2024, industry-published long-term evaluation method) — not Q2, since it evaluates policies, not individual interactions.
- **Attributes retention to individual interactions?** No — LOPE estimates the aggregate long-term outcome of an entire algorithm/policy from short-term experiment data; it does not decompose retention into per-swipe or per-touch fractional credit.
- **Transferable components:** the surrogate-effect/action-effect decomposition — separating "this candidate got a lot of short-term swipes" (surrogate) from "this candidate has real incremental retention value" (action effect) — maps directly onto the platform's "would have swiped anyway" selection-bias problem; counterfactual/importance weighting of short-term signals to reduce label variance.
- **Required changes:** shift the unit of analysis from policy-level evaluation to per-touch fractional credit; incorporate heterogeneous touchpoints (swipe/match/message) into the short-term surrogate reward; re-anchor to a rolling daily N7 retention target rather than a single long-horizon evaluation window.
- **On last-touch:** Not named explicitly, but the paper's critique of the surrogacy assumption — that short-term signals alone (which is what last-touch attribution effectively uses) can badly misrepresent long-term causal impact, by up to 71% higher MSE — is functionally the same critique the platform has of last-touch attribution.
- **Transfer rating:** adaptable — the surrogate/action-effect decomposition is conceptually the best available tool in this batch for separating genuine incremental retention value from "engaged users swipe more anyway," even though it operates at policy level rather than per-swipe.
