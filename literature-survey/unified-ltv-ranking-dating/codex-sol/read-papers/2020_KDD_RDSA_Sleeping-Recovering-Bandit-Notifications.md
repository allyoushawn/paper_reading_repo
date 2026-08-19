# Paper Analysis: A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications

**Source:** https://research.duolingo.com/papers/yancey.kdd20.pdf  
**Source ID:** 58fc435a-363d-4c95-92d4-f6100f86547e  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau; no conversational context.

---

## 1. Summary

**Title:** A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications  
**Authors:** Kevin P. Yancey; Burr Settles  
**Abstract:** The paper addresses recurring notification choice when templates are conditionally eligible and repeated exposure causes novelty decay. It introduces the Recovering Difference Softmax Algorithm (RDSA), deployed for millions of Duolingo reminders, and reports gains in daily active users and new-user retention.

**Key contributions:**

- Controls eligibility confounding by comparing an arm's reward when used with its reward when eligible but not used, corrected by importance sampling.
- Shrinks noisy small-sample arm estimates with an empirical-Bayes prior.
- Applies a per-user exponentially decaying recency penalty, then samples eligible arms with softmax to retain exploration.

**Methodology:** Historical behavior-policy propensities support weighted importance estimates of each template's relative reward. Template–UI-language pairs are arms; recency since a user last saw an arm adjusts its score before softmax selection.

**Main results:** Offline reward rose 1.8% over uniform random selection for template-plus-language arms and 1.9% with the recency penalty. A two-week production test reported +0.5% DAU, +0.4% lessons completed, and +2% new-user recurring retention.

---

## 2. Experiment Critique

**Design:** The study uses 34 days of uniformly randomized legacy traffic: 15 days/88M rows for training and 19 days/114M rows for testing, followed by a randomized online experiment against the mature uniform-template system. Offline weighted-importance evaluation, component comparisons, a recency grid search, and a production test provide complementary evidence.

**Statistical validity:** The offline tables report an uncertainty of about ±0.00015 and the recency increment is only reported at p<0.1. The indexed content does not specify confidence intervals or p-values for the headline online lifts, power calculations, or correction for multiple metrics.

**Online experiments:** Users were randomized between control and RDSA for two weeks. Metrics included DAU, lessons, and recurring retention. The duration is enough for near-term notification behavior but limited for durable habit or revenue effects; novelty and repeated-treatment effects remain central risks.

**Reproducibility:** Algorithm equations, hyperparameters (including a 15-day recency half-life, gamma 0.017, and softmax temperature 0.0025), and data volumes are described. Proprietary Duolingo logs and production eligibility systems are unavailable; code and random seeds are not specified in indexed content.

**Overall:** The evidence supports practical gains for notification-template optimization. It does not show that the short-horizon two-hour reward is itself causal for long-run retention, although the randomized retention lift is encouraging.

---

## 3. Industry Contribution

**Deployability:** Demonstrated at Duolingo scale. The method requires logging behavior propensities, arm eligibility, per-user exposure history, and outcomes.

**Problems solved:** Conditional action availability, novelty decay, small-sample instability, and ongoing exploration in a recurring engagement intervention.

**Engineering cost:** Moderate: periodic policy estimation plus online eligibility filtering and per-user recency state. The approach is simpler than a fully contextual or long-horizon reinforcement-learning system.

**Project relevance:** Core for prediction-versus-incrementality and delayed retention intervention design. Dating notifications, candidate exposure, or re-engagement actions can be treated as sleeping arms, and repeated exposure can receive a recovery penalty. The randomized policy and logged propensities offer a causal bridge missing from pure response prediction.

**Most important mismatch:** RDSA selects notification templates using a two-hour binary lesson reward; it neither ranks reciprocal people nor jointly models the impression→like→match→conversation→date/subscription cascade, congestion, subscriptions/à-la-carte value, or the success paradox. A dating system would need contextualization, candidate-side constraints, and a long-horizon causal value signal.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A practical algorithm combining sleeping arms and recovering rewards through eligibility-controlled relative differences, empirical-Bayes shrinkage, recency decay, and softmax exploration.

**Prior work comparison:** The paper contrasts conventional epsilon-greedy, softmax, and UCB with recovering bandits, rested bandits, and sleeping-bandit approaches such as EXP4-based priority ordering. RDSA emphasizes joint handling of both complications and real-world evaluation.

**Verification:** Novelty is reported from the indexed source only; no independent web audit was performed in this batch.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Duolingo notification log, training | Not specified in source | No | 15 days, 88M rows; proprietary. |
| Duolingo notification log, test | Not specified in source | No | 19 days, 114M rows; proprietary. |
| Production randomized experiment | Not specified in source | No | Millions of daily reminders; proprietary. |

**Offline experiment reproducibility:** Equations and aggregate data design are documented, but the proprietary log, eligibility rules, templates, and code prevent full reproduction.

---

## 6. Community Reaction

No significant community discussion was assessed in this source-content fallback batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Authors:** Kevin P. Yancey; Burr Settles  
**Affiliations:** Duolingo  
**Venue:** KDD  
**Year:** 2020  
**PDF:** Available at source URL  
**Relevance:** Core (selected row marked Core—inferred)  
**Priority:** 1  
**Direction:** D4 — retention / lifetime value / long-horizon value
