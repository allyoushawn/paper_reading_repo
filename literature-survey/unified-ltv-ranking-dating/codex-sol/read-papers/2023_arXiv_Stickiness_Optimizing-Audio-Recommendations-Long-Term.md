# Paper Analysis: Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective

**Source:** https://arxiv.org/pdf/2302.03561  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective  
**Authors:** Lucas Maystre; Daniel Russo; Yu Zhao  
**Abstract:** Spotify describes a deployed podcast recommender that optimizes listening journeys over months. Instead of estimating the tiny effect of one recommendation on noisy app-wide usage, it models how the exposure changes a user’s item-specific relationship and future “stickiness,” yielding a structured partial Q-function for policy improvement.

**Key contributions:** Content-relationship state; item-level stickiness value functions; a decomposition of short-term response, state transition, and long-term item value; industrial policy-improvement deployment.  
**Methodology:** The incumbent system remains fixed except for one recommendation component. A partial state-action value estimates the benefit of deviating at one position. Immediate engagement determines a content-relationship transition; a stickiness model values the resulting item-level habit.  
**Main results:** One A/B test increased 60-day listening time attributable to recommendations by 81% among affected users. A broader test significantly improved app-level outcomes. Structured estimation reduced illustrative sample requirements by up to 120,000× versus holistic black-box estimates.

## 2. Experiment Critique

**Design:** Offline randomized-recommendation analyses compare holistic long-term, local long-term, and stickiness-based estimators; online A/B tests cover targeted and broad deployment.  
**Statistical validity:** The paper shows one-standard-deviation confidence intervals and emphasizes noise reduction. Exact broad-test lift, test duration, and full sample sizes are Not specified in the inspected content.  
**Online experiments:** Yes; 81% attributable listening-time lift over 60 days for affected users and significant overall app-level improvement.  
**Reproducibility:** Production data and implementation are not public; Not specified in source.  
**Overall:** Strong industrial evidence for domain-structured long-horizon credit assignment, with the caveat that retention is modeled as exogenous and the objective is listening rather than causal retention.

## 3. Industry Contribution

**Deployability:** Proven at Spotify for hundreds of millions of listeners as a component-level policy update.  
**Problems solved:** Long-horizon attribution, coordination across a large recommender, and extreme signal-to-noise in app-wide outcomes.  
**Engineering cost:** Requires randomized recommendation data, item-relationship state, immediate-response models, transition models, and long-horizon stickiness models.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A domain-specific decomposition that makes long-term partial-Q estimation data efficient enough for industrial deployment.  
**Prior work comparison:** Contrasts contextual-bandit/myopic rankers, black-box RL, and proxy metrics; cites long-term engagement and offline-RL literature.  
**Verification:** Indexed source content only; no independent web novelty check.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Spotify podcast recommendation logs | Not specified in source. | No | Randomized recommendations, immediate listening, and 60-day item-level outcomes. |

**Offline experiment reproducibility:** Not possible without proprietary logs.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D2  
**Problem setting:** Improve one podcast recommendation component for months-long user journeys.  
**Objective and label definition:** Long-term expected listening reward; operational evidence uses 60-day listening time attributable to recommendations and item-level listening habit. Retention is assumed exogenous; revenue, censoring, and sparsity rules are Not specified.  
**Prediction or incrementality:** A partial Q-function estimates the effect of a short-term deviation from the incumbent policy; randomized data support causal component-level improvement, but this is not a general per-user uplift model.  
**Model architecture:** Content-relationship state, direct-response model, relationship-state transition, item stickiness value model, and decomposed partial Q-function.  
**Credit assignment:** Long-term value is localized to the recommended item and attributed through the immediate response and resulting relationship-state change, rather than assigned from holistic app activity.  
**Training data and counterfactual handling:** Historical plus randomized recommendation data; incumbent-policy component update. Detailed propensity/off-policy estimator is Not specified in the inspected passages.  
**Offline and online evaluation:** Structured offline estimator comparisons plus industrial A/B tests.  
**Reported gains:** +81% 60-day attributable listening time for affected users; up to 120,000× illustrative sample-efficiency improvement; unspecified significant app-level gains.  
**Unverified claims:** Original survey year is 2023 although the indexed manuscript is dated 2024; exact broad-test lift is not stated.

## Project Relevance

**Source-stated facts:** The paper explicitly uses dating partners as an example of recurring recommendation and solves long-term attribution by localizing value to an item relationship. It supports staged migration by updating one component while leaving the incumbent system in place.

**Survey inference:** The dating analogue is a candidate-relationship state for `(A,B)`, with immediate like/match/conversation response, transition in relationship state, and downstream value. However, Spotify items do not reciprocate or become congested; success does not remove both sides from the market. A dating implementation would need bilateral state/value, capacity constraints, revenue and match-quality reward terms, interference-aware evaluation, and explicit positive-churn handling.

**Applicability note:** One of the strongest migration and credit-assignment references for replacing a post-hoc blend incrementally.  
Its unilateral habit model must become a bilateral relationship-value model before use in dating.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md](./2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md) | Introduction / Summary | Explicitly mentions Stickiness in baseline or comparison context. |

## Meta Information

**Authors:** Lucas Maystre; Daniel Russo; Yu Zhao  
**Affiliations:** Spotify; Columbia University  
**Venue:** arXiv  
**Year:** 2023  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
