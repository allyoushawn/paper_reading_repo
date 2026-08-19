# Paper Analysis: Off-Policy Evaluation and Learning for Matching Markets

**Source:** https://arxiv.org/pdf/2507.13608.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Off-Policy Evaluation and Learning for Matching Markets
- **authors or company:** Yudai Hayashi (Wantedly), Shuhei Goda, Yuta Saito (Cornell)
- **venue:** RecSys
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2507.13608.pdf
- **source type:** academic
- **direction:** D6
- **problem setting:** Reciprocal matching markets (job search, dating); standard OPE (DM/IPS/DR) fails under sparse terminal match labels and large action spaces.
- **objective and label definition:** Policy value \(V(\pi)=\frac{1}{|C|}\sum_c\sum_j \pi(j|c)\,q_s(c,j)\,q_r(c,j)\): expected number of mutual matches. First-stage \(s\): scout sent; second-stage \(r\): reply; terminal match \(m=s\cdot r\).
- **prediction or incrementality:** Estimates expected match outcomes under a target policy via OPE; predicts conditional q-functions, not causal uplift of exposure.
- **model architecture:** Not a ranking model—statistical estimators DiPS and DPR (and policy-gradient extensions DiPS-PG, DPR-PG) combining IPS on first-stage reward with regression imputation of second-stage response probability.
- **credit assignment:** Logged bandit tuples \((j_c,s_c,r_c)\) map first/second-stage rewards to company context \(c\) (date, interaction rank, company ID) and job seeker \(j\) (date, seeker ID).
- **training data and counterfactual handling:** Off-policy evaluation on logged data \(\mathcal{D}=\{(j_c,s_c,r_c)\}\) under logging policy \(\pi_0\); DiPS applies IPS to \(s_c\) and multiplies by \(\hat{q}_r\); DPR adds doubly robust control variate on match probability \(\hat{q}_m\).
- **offline and online evaluation:** Synthetic experiments plus Wantedly Visit A/B logs (21,736 companies, 17,460 seekers, 1.2% match rate); MSE and ErrorRate (policy selection). No live online estimator deployment—validated against historical A/B outcomes offline.
- **reported gains:** DiPS/DPR achieve significantly lower MSE than IPS/DR across synthetic configurations; DPR lowest MSE on Wantedly at all sample sizes; DiPS-PG/DPR-PG highest policy values under sparse rewards and large action spaces.
- **applicability note for a two-sided dating recommender:** Dating shares the two-stage funnel (like/scout → mutual match/reply); DiPS/DPR let you rank offline policies on match rate before expensive two-sided A/B tests.
  Estimators target sparse match labels, not 7–30 day retention/LTV—extend with surrogate short-horizon rewards for long-term ranking evaluation.
- **unverified claims:** none

## 1. Summary

First formal OPE/OPL framework for matching markets with two-stage reciprocal rewards. Standard IPS/DR on sparse terminal match labels suffer high variance; DiPS importance-weights the denser first-stage reward (scout/outreach) and imputes second-stage response via \(\hat{q}_r\); DPR adds a doubly robust match-probability control variate. Policy-gradient extensions enable offline policy learning. Validated on synthetic data and Wantedly Visit production A/B logs.

## 2. Experiment Critique

Strengths: real industrial reciprocal data with extreme sparsity (1.2% match rate), theoretical bias-variance analysis, both OPE and OPL. Weaknesses: logging/target policies estimated via GBDT (not observed propensities); ErrorRate can favor IPS over lower-MSE DPR due to systematic overestimation; requires explicit two-stage funnel structure; no retention/LTV horizon.

## 3. Industry Contribution

Practical offline gate for ranking-policy iteration in job/dating matching: predict which policy wins an A/B test from logs alone. Wantedly-scale validation (4M+ users platform). Reduces reliance on costly frequent live experiments.

## 4. Novelty vs. Prior Work

First matching-market-specific OPE/OPL estimators leveraging intermediate first-stage rewards. Builds on Saito & Joachims (2021–2023) recsys OPE, Su et al. (2022) matching-market ranking, CAB (Su et al. 2019), Switch-DR (Wang et al. 2017), Tomita et al. (2023) reciprocal recommendation.

## 5. Dataset Availability

- **Synthetic:** 10D context vectors, tunable sparsity parameter.
- **Wantedly Visit:** Industrial A/B testing logs; open-sourced processed dataset referenced in paper.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Maximize expected number of mutual matches. Retention, LTV, revenue: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Logged tuples \((j_c,s_c,r_c)\) tie rewards to company context (date, rank, company ID) and seeker ID. Detailed causal/delayed credit assignment: Not specified in source.

### (3) Label and horizon definitions; delay, sparsity, censoring
\(s\): scout sent; \(r\): reply given scout; \(m=s\cdot r\). Sparsity: DiPS/DPR use denser first-stage \(s\) to reduce variance. Horizon, delay, censoring: Not specified in source.

### (4) Short vs long-term head fusion
Not specified in source (OPE estimators, not online model heads). DiPS multiplies IPS-weighted \(s\) by \(\hat{q}_r\); DPR adds \(\hat{q}_m\) control variate.

### (5) Prediction vs incrementality
Predicts expected match outcomes via q-functions; not incrementality of exposure.

### (6) Offline and online evaluation
Offline MSE and ErrorRate on synthetic and Wantedly A/B logs. No live online evaluation of estimators.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Reciprocity: bidirectional mutual agreement modeled. Congestion, fairness, revenue vs match quality: Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Yudai Hayashi, Shuhei Goda, Yuta Saito
**Affiliations:** Wantedly, Independent Researcher, Cornell University
**Venue:** RecSys 2025
**Year:** 2025
**PDF:** https://arxiv.org/pdf/2507.13608.pdf
**Relevance:** Core
**Priority:** 1
