# Paper Analysis: Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/cikm2017.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems
**Authors:** Qingyun Wu, Hongning Wang (University of Virginia), Liangjie Hong (Etsy Inc.), Yue Shi (Yahoo Research; work done while authors were at Yahoo Research)
**Venue/Year:** CIKM 2017

**Abstract (paraphrased):** Most recommendation algorithms optimize immediate click feedback only, implicitly assuming user return behavior is independent of the recommendations made — an assumption the authors argue is false: a "bad" recommendation can drive a user to leave the system early. The paper formalizes long-term engagement optimization as a sequential decision-making (contextual bandit) problem and proposes a bandit-based solution balancing immediate click, expected future clicks from user return, and exploration. The authors prove a sublinear regret bound for their method and a linear (unbounded) regret bound for algorithms that ignore return behavior. Extensive simulation and real-world experiments verify the improvement.

**Key contributions:**
- Formalizes optimizing long-term user engagement as maximizing cumulative reward from a population of users over time, where each recommendation risks losing the user (via non-return) as well as earning an immediate click.
- Derives a tractable one-step-ahead approximation (Eq. 2/3) to an otherwise intractable infinite-horizon value function, combining immediate click probability with the probability of returning within a fixed threshold τ.
- Proposes r²Bandit (reward-return bandit): two per-user generalized linear models (logistic-link for click, exponential/inverse-link for return time), combined via a UCB-type action-selection rule with GLM-derived confidence bounds.
- Proves r²Bandit achieves sublinear cumulative regret with high probability, and proves that any algorithm ignoring user return behavior incurs linear regret.

**Methodology:** Value function (Eq. 1) is the expected total future clicks resulting from a recommendation, summed over an infinite horizon of possible future returns — intractable because the future candidate item pool is unknown ahead of time. The paper approximates it (Eq. 2/3) by assuming (a) a stationary marginal click probability ε_u independent of the specific future item, and (b) that only one-step-ahead lookahead is needed since return probability decays over time. Click and return-time probabilities are estimated online per user via MLE on generalized linear models; actions are selected via a UCB rule (Eq. 6) combining the estimated payoff with confidence-bound exploration terms for both the click and return models.

**Main results:** In simulation, r²Bandit accumulates the most clicks with the steepest slope and smallest variance across 10 runs, correctly preferring high-click/short-return items while click-only baselines get trapped on high-click/long-return items. On a real 4-week news-recommendation log (18,882 users, 9,984,879 events), evaluated via an unbiased offline-replay protocol, r²Bandit achieves roughly 2x the CTR of GLM-UCB/rGLM-UCB and over 5x that of UCB1-style baselines, 1.8x the return rate of GLM-UCB, and a naive-r²Bandit variant reduces normalized average return time by 18-25% versus the logged production policy.

## 2. Experiment Critique

**Design:** Two complementary evaluations — a fully-controlled synthetic simulation (known ground-truth parameters, four deliberately constructed item archetypes to stress-test the click/return tradeoff) and a large real-world offline-replay evaluation using an established unbiased contextual-bandit evaluation protocol (Li et al., WSDM 2011), extended here to also validate return-time-triggered events. This combination is a real strength for a paper without a live online experiment.

**Statistical validity:** Simulation results are reported as mean ± standard deviation over 10 independent runs — a genuine strength. Real-dataset results (Figure 3) are shown as time-series curves without confidence bands or significance tests; relative-magnitude claims ("about twice," "5 times") in the text are not backed by formal hypothesis tests.

**Online experiments:** None. This is a simulation-plus-offline-replay evaluation only; no live production A/B test is reported, despite two of the four authors being at industry labs (Yahoo Research, Etsy) at the time.

**Reproducibility:** The real-world dataset (a major web portal's news logs) is proprietary and not released, though preprocessing (PCA to 23 article-feature dimensions, 30-minute session-inactivity threshold, 8-level discretized return time, τ=24 hours) is described in enough detail to closely replicate the pipeline on a different dataset. The algorithms (GLM-UCB, rGLM-UCB, r²Bandit) are given as full pseudocode with explicit confidence-bound formulas (Algorithms 1, 2), which supports methodological reproducibility even without the original data.

## 3. Industry Contribution

**Deployability:** No production deployment or live A/B test is reported — unusual for a paper with two industry-lab co-authors. The strongest evidence offered is the real-data offline replay, not a live system result, which is a meaningfully weaker industry-deployment story than the other three papers in this batch.

**Problems solved:** Provides a theoretically grounded (regret-bounded) way to fold "will the user come back" directly into the per-item ranking/selection decision via a bandit reward function, rather than treating retention as a downstream metric measured only in aggregate. It also formally proves why click-only optimization is suboptimal (linear regret) when return behavior depends on recommendation quality — the theoretical counterpart to the empirical volume/fatigue results in Papers 1 and 4 of this batch.

**Engineering cost:** Requires per-user online MLE updates for two GLMs (click, return) at every interaction, plus a UCB exploration-bonus computation involving a per-user matrix inverse. The authors explicitly flag that independent per-user parameters limit practicality for sparse users. In recsys-engineering terms, this is an online-learning ranking layer requiring near-real-time per-user model updates, a heavier operational lift than the batch-trained GBDT (Paper 1) or decision-transformer (Paper 4) approaches elsewhere in this batch.

## 4. Novelty vs. Prior Work

The paper's stated novelty is being (to the authors' knowledge) the first bandit algorithm to directly optimize long-term user engagement under the explicit possibility that users leave the system due to bad recommendations — prior bandit recommendation work (e.g., GLM-UCB) implicitly assumes users always return, i.e., that return probability is independent of the recommendation made. It differentiates itself from the survival-analysis line of work on return-time prediction (Kapoor et al., WSDM 2015 and KDD 2014; Du et al., KDD 2016) by integrating return-time modeling directly into an online decision-making/bandit loop with a formal regret guarantee, rather than treating return-time prediction as an offline analysis task or a feature for a separately-trained ranker.

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| Synthetic simulation environment | Generated by the authors; not released as a fixed artifact | N=100 users, K=200 candidates/user | Fully controlled ground-truth θ_u, β_u; 4 item archetypes used to stress-test the click/return tradeoff |
| Major Web portal news recommendation logs (2016, ~4 weeks) | No — proprietary/internal | 18,882 users, 188,384 articles, 9,984,879 logged events, 1,123,583 sessions | Not released; evaluated via unbiased offline-replay protocol, not a public benchmark |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Value |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems," Qingyun Wu, Hongning Wang (University of Virginia), Liangjie Hong (Etsy Inc.), Yue Shi (Yahoo Research), CIKM 2017. URL: https://doi.org/10.1145/3132847.3133025 |
| 2 | Source type | Academic (industry co-authorship; real-world dataset from an industry setting) |
| 3 | Direction | D2 |
| 4 | Problem setting | Online content recommendation (news articles) framed as a contextual-bandit sequential-decision problem, where a "bad" recommendation can reduce the probability a user returns, making click-only optimization potentially suboptimal for cumulative long-term engagement. |
| 5 | Objective and label definition | Maximize cumulative expected reward = immediate click probability + ε_u-weighted probability of return within a fixed horizon τ — a one-step-ahead approximation (Eq. 2/3) to a full infinite-horizon value function the authors state is intractable given an unknown future candidate pool. Return "label" is continuous time-to-next-visit Δ, thresholded at τ; no formal censoring model for non-returning users (4-week cutoff = hard "no return" on the real dataset). |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality in the causal/uplift sense. The model predicts click and return probability conditional on the chosen item and selects greedily/UCB-optimally among predictions; it does not estimate a counterfactual or causally-isolated incremental effect of exposure versus a control condition. |
| 7 | Model architecture | r²Bandit — two per-user generalized linear models (logistic-link click model, exponential/inverse-link return-time model), estimated online via MLE, combined into a single UCB-type action-selection rule (Eq. 6) with GLM-derived confidence-bound exploration terms (Eqs. 4, 5). |
| 8 | Credit assignment | Single-item, single-interaction granularity — each recommended item is directly credited with both the immediate click outcome and the subsequent return-time interval that follows that specific recommendation. No slate-level attribution. |
| 9 | Training data and counterfactual handling | Online bandit learning (no fixed training set) on synthetic simulation and real Web-portal news logs; evaluated offline via the unbiased contextual-bandit replay protocol of Li et al. (WSDM 2011), which discards logged events where the algorithm's chosen action differs from the logged action — a counterfactual-evaluation technique for the evaluation step, not a causal-effect-estimation method for the model itself. |
| 10 | Offline and online evaluation | Offline only — synthetic simulation (cumulative reward, item-type-selection distribution, preferred-type ratio, 10-run mean±std) and real-data offline replay (reweighted cumulative clicks, CTR, average return time, return rate, improved-user ratio, no-return count). No live online A/B test. |
| 11 | Reported gains | Real news-recommendation dataset (offline replay): r²Bandit achieves the highest CTR, about 2x that of GLM-UCB/rGLM-UCB and over 5x that of r²GLM-UCB1/r²UCB1; the highest return rate, about 1.8x GLM-UCB and 3.5x r²UCB1/r²GLM-UCB1; naive-r²Bandit reduces normalized average return time 18-25% versus the logged production baseline; roughly 63% of users achieve a shorter return time than the production baseline's recorded average. |
| 12 | Applicability to a two-sided dating recommender | Gives a formally regret-bounded template for folding "will this recommendation make the user come back" directly into per-candidate ranking scores, and proves click-only ranking incurs unbounded (linear) regret when recommendation quality affects return — directly supporting the project's premise that a CTR/CVR-only ranker is structurally insufficient. Does not transfer the reciprocity/congestion machinery the dating app needs, and has no live production validation. |
| 13 | Unverified claims | Relative-magnitude claims ("about twice," "5 times," "1.8 times," "3.5 times") are stated from figures without accompanying confidence intervals or significance tests. The "first bandit algorithm" novelty claim is the authors' own, not independently verified here. |

## Project Relevance

Directly answers **Q1** (reframes the ranking objective around a return-based long-term reward instead of click-only) and **Q3** (an explicit return-time-to-threshold-τ label definition — one of the clearest formal "retention label" definitions in this batch), with a formal regret-theoretic argument for why click-only optimization fails. Per the batch note, this paper is cited by several other papers already in the corpus as the origin of optimizing long-term engagement through return behavior, establishing it as a foundational Q1/Q3 reference even though its industry-deployment evidence is weaker than the batch's other three papers (Section 2/3 above). Low relevance to **Q5** (no uplift/incrementality machinery), **Q7** (no two-sided/reciprocal element), and **Q8** (no staged-migration narrative — this is a from-scratch bandit method, not a migration path from an existing CTR system).

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `r2Bandit`._

## Meta Information

- **Authors:** Qingyun Wu, Hongning Wang, Liangjie Hong, Yue Shi
- **Affiliations:** University of Virginia; Etsy Inc.; Yahoo Research (work done while authors were at Yahoo Research)
- **Venue:** CIKM 2017
- **Year:** 2017
- **Relevance:** Core
- **Priority:** 1
- **nlm:0029e13b**
