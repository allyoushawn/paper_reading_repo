# Paper Analysis: Long-term Off-Policy Evaluation and Learning

**Source:** https://arxiv.org/pdf/2404.15691  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Long-term Off-Policy Evaluation and Learning  
**Authors or company:** Spotify  
**Abstract:** The paper addresses high-variance evaluation and learning for policies whose long-term rewards are slow and noisy. Its Long-term Off-Policy Evaluation (LOPE) framework decomposes long-term reward into a short-term-surrogate effect and a residual action effect, using surrogate importance weights plus reward regression to reduce variance without requiring full surrogacy.

**Key contributions:**

- LOPE, an off-policy estimator that uses early outcomes while permitting a direct action effect on long-term reward.
- A Conditional Pairwise Correctness condition under which the estimator remains unbiased when strict surrogacy fails.
- LOPE-PG, a policy-gradient extension for offline optimization of long-term policy value.

**Methodology:** For context `x`, action `a`, early outcome `s`, and long-term reward `r`, the paper decomposes `q(x,a,s)=g(x,s)+h(x,a,s)`. It importance-weights the surrogate component by the target-to-logging ratio over `s` and estimates the residual action component with a regression model. Historical logs contain `(x,a,s,r)` under the logging policy; an optional short experiment under the target policy supplies early outcomes.

**Main results:** In synthetic tests LOPE reduced mean-squared error by 36% versus doubly robust estimation at `n=200`, by 71% versus long-term causal inference at `n=1,000`, and by 45% versus doubly robust estimation under high reward noise. In Spotify's roughly four-million-user experiment, using day-7 streams/clicks/likes/dislikes to estimate day-21 streams, LOPE reduced mean-squared error by 9.2%–15.0% versus the doubly robust baseline across three policies. These are source-stated results.

---

## 2. Experiment Critique

**Design:** Synthetic experiments vary sample size, long-term-reward noise, policy distance, and violations of surrogacy. A three-week Spotify randomized experiment provides a real-world benchmark with three candidate policies, more than 1,000 possible content actions, and a long-term experimental mean as the reference value. Baselines include long-term causal inference, inverse propensity scoring, doubly robust estimation, regression-based learning, IPS-PG, and DR-PG.

**Statistical validity:** Mean-squared error against a long-running experimental reference is appropriate for estimator evaluation. The source reports policy-selection rates and multiple noise/sample regimes, but uncertainty intervals and significance tests for all reported estimator differences were not specified in the extraction.

**Online experiments (if any):** The source uses a three-week A/B test conducted in May 2023 with about four million Spotify users. The paper's aim is to predict the long-term policy value from historical and short-horizon observations, not to report a subsequent product lift from deploying LOPE-PG.

**Reproducibility:** The synthetic setup is described (1,000 users, 30 actions, context/action features, controlled surrogacy violations). Availability of production logs, code, seeds, and full hyperparameters was not specified in the source extraction.

**Overall:** The results support lower-variance policy evaluation at a three-week horizon. The source itself notes that seasonal distribution shift can violate comparability, preprocessing of high-dimensional surrogates remains open, and annual retention or revenue was not empirically validated.

---

## 3. Industry Contribution

**Deployability:** LOPE can be used as an offline gate for candidate ranking policies when logged propensities and long-horizon outcomes are available. It requires reliable exposure-policy probabilities and overlap between logging and target policies.

**Problems solved:** It reduces the variance of long-term off-policy evaluation while avoiding the strict assumption that short-term proxies fully mediate the action's long-term effect.

**Engineering cost:** A deployment needs propensity logging, target-policy early-outcome data, an action-effect regression model, surrogate density-ratio estimation, and monitoring for temporal comparability and support violations.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** LOPE combines surrogate-based long-term causal inference with off-policy evaluation through reward decomposition, and extends the estimator to policy-gradient learning.

**Prior work comparison:** The paper contrasts itself with the surrogate index, inverse propensity scoring, and doubly robust evaluation. Frequently cited foundations include Athey et al., *The Surrogate Index* (2019); Dudík et al., *Doubly Robust Policy Evaluation and Learning* (2011); Rosenbaum and Rubin on propensity scores (1983); Prentice on surrogate endpoints (1989); Kallus and Mao on efficient use of surrogates (2020); and Hohnhold et al., *Focus on the Long-Term* (2015).

**Verification:** This comparison reflects source-scoped NotebookLM extraction only; no independent novelty web review was performed.

---

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic LOPE environment | Not specified in source. | Not specified in source. | 1,000 users, 30 actions, controlled surrogacy violation and reward noise. |
| Spotify three-week experiment | Not specified in source. | No | Production data; approximately four million users. |

**Offline experiment reproducibility:** The synthetic study is partially reconstructable from the described setup, but the production evaluation cannot be reproduced without Spotify logs and policy propensities.

---

## 6. Community Reaction

No significant community discussion found in the source-scoped extraction.

---

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D2  
**Problem setting:** Estimate and learn recommendation policies for delayed, noisy long-term outcomes using historical logs and short-horizon experiment data.  
**Objective and label definition:** General bounded long-term reward; Spotify instantiates day-21 streams, with day-7 streams, clicks, likes, and dislikes as short-term surrogates. Annual retention and revenue are motivating examples, not evaluated labels. Delay handling comes from combining historical mature outcomes with early target-policy outcomes. Censoring handling is not specified in source.  
**Prediction or incrementality:** Counterfactual policy-value estimation under potential outcomes and logged propensities; it estimates the value change from adopting a target policy, not merely conditional user outcome prediction and not a per-exposure CATE score.  
**Model architecture:** Reward decomposition, surrogate importance weighting, residual action-effect regression, and an optional neural policy trained with LOPE-PG.  
**Credit assignment:** The source assigns a long-term reward to logged context-action pairs and separates the portion mediated by early outcomes from a residual direct action effect. It does not solve multi-touch attribution across many historical exposures.  
**Training data and counterfactual handling:** Historical `(x,a,s,r)` logs under a known logging policy plus optional early outcomes from the target policy; importance weights and reward regression perform off-policy correction.  
**Offline and online evaluation:** Synthetic estimator/learning tests and a three-week randomized Spotify benchmark; no reported online product deployment lift.  
**Reported gains:** 9.2%–15.0% lower mean-squared error than doubly robust estimation on the Spotify policies; synthetic reductions and policy-learning improvements are summarized above.  
**Unverified claims:** Venue assignment as WWW 2024 is taken from survey metadata; author names, code availability, and statistical uncertainty were not specified in the source-scoped extraction.

---

## Project Relevance

**Source-stated facts:** LOPE supports long-term off-policy policy evaluation when early engagement signals arrive before the mature outcome. It explicitly permits an action effect not mediated by the proxies, and it uses logged policy probabilities to estimate a target policy's expected reward.

**Survey inference:** A dating system could use likes, matches, and conversations observed over the first week as surrogates for 7–30-day retention or weeks-long revenue, evaluating a unified target ranker before waiting for all mature labels. This is best viewed as an evaluation/learning layer rather than evidence that one exposure can be causally credited for all downstream retention or revenue. Bilateral reciprocity, candidate congestion, cross-user interference, and the successful-match churn paradox are outside the source's unilateral action model and require separate market-aware reward and experiment design.

**Applicability note:** LOPE is a strong candidate for evaluating long-term dating ranking policies with less variance and shorter experiments.  
It does not by itself solve reciprocal allocation, interference, positive churn, or exposure-level uplift estimation.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Not specified in source.  
**Affiliations:** Spotify  
**Venue:** WWW  
**Year:** 2024  
**PDF:** Available at source URL  
**Relevance:** Related  
**Priority:** 1
