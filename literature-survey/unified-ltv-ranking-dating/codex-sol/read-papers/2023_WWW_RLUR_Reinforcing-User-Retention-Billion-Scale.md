# Paper Analysis: Reinforcing User Retention in a Billion Scale Short Video Recommender System

**Source:** https://arxiv.org/pdf/2302.01724  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Reinforcing User Retention in a Billion Scale Short Video Recommender System  
**Authors:** Qingpeng Cai; Shuchang Liu; Xueliang Wang; Tianyou Zuo; Wentao Xie; Bin Yang; Dong Zheng; Peng Jiang; Kun Gai  
**Abstract:** RLUR formulates short-video recommendation as an infinite-horizon request-level MDP and directly minimizes accumulated inter-session return time. It learns dynamic weights over existing immediate-feedback scoring models while addressing noisy, biased, delayed retention rewards.  
**Key contributions:** Return-time normalization; activity-group policies; delayed-reward regularization and heuristic/intrinsic immediate rewards; billion-scale deployment.  
**Methodology:** At each request, the action is an ensemble-weight vector over base feedback scores; the ranked list produces immediate interactions. A predicted-return-time normalization reduces variance, segmented policies reduce activity bias, and soft regularization stabilizes delayed learning.  
**Main results:** After about 100 days, production gaps converged near +0.2% DAU, +0.053% day-1 retention, and +0.063% day-7 retention. The paper states +0.1% DAU and +0.01% retention are statistically significant at this scale.

## 2. Experiment Critique

**Design:** Offline comparisons and long-running live deployment; exact offline datasets/baselines are Not specified in the inspected passages.  
**Statistical validity:** Daily curves to 100+ days and platform significance thresholds are reported; confidence intervals and randomization details are Not specified.  
**Online experiments:** Fully launched at Kuaishou with day-1/day-7 retention and DAU monitoring.  
**Reproducibility:** Proprietary logs and infrastructure; code Not specified.  
**Overall:** Strong direct industrial evidence for retention-optimized learned fusion, though causal identification and interference are not addressed.

## 3. Industry Contribution

**Deployability:** Demonstrated at billion scale as a learned score-ensemble layer.  
**Problems solved:** Direct retention optimization under reward uncertainty, active-user bias, and hours-long delay.  
**Engineering cost:** Requires return-time model, user segmentation, RL policy training, base score heads, and long online stabilization.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** One of the first industrial systems to directly optimize retention rather than cumulative immediate feedback.  
**Prior work comparison:** Contrasts point/list-wise prediction and engagement-focused RL; cites deep RL recommendation and delayed-policy stabilization.  
**Verification:** Indexed paper content only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Kuaishou production interactions | Not specified in source. | No | Billion-scale short-video requests, immediate feedback, return intervals. |

**Offline experiment reproducibility:** Not specified in source.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D2  
**Problem setting:** Request-level short-video ranking across recurring sessions.  
**Objective and label definition:** Minimize cumulative time from one session’s last request to the next session’s first request; online metrics include day-1/day-7 retention and DAU. Delay is usually hours; normalization and immediate heuristic rewards address variance/delay. Censoring is Not specified.  
**Prediction or incrementality:** Policy optimization of observed outcomes; not exposure-effect/uplift estimation.  
**Model architecture:** Existing point-wise score heads plus an RL policy producing request-specific fusion weights.  
**Credit assignment:** Infinite-horizon request MDP propagates return-time reward across many requests; it does not identify one exposure’s causal effect.  
**Training data and counterfactual handling:** Production trajectories, segmented by activity; explicit off-policy correction/randomized propensities are Not specified.  
**Offline and online evaluation:** Offline experiments plus >100-day live curves and full launch.  
**Reported gains:** +0.2% DAU, +0.053% day-1 retention, +0.063% day-7 retention after convergence.  
**Unverified claims:** Exact offline metrics, test assignment, and code availability are Not specified.

## Project Relevance

**Source-stated facts:** RLUR replaces fixed score fusion with learned request-level weights and directly targets retention while retaining immediate heads as heuristic rewards. This is a close documented migration from a blend toward a unified objective.

**Survey inference:** The dating system could initially let the policy weight like/match/conversation and value heads, then train toward return/revenue. But unidirectional videos have no reciprocal consent, scarce attention, cross-user interference, or successful-match churn. Pure retention would risk optimizing addictive swiping rather than relationship success; bilateral and quality/revenue constraints are mandatory.

**Applicability note:** Directly relevant architecture and migration evidence for learned fusion of short- and long-term dating signals.  
Not sufficient for causal uplift or reciprocal-market allocation without major reward and policy extensions.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md](./2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow-Networks.md) | Experiments | Explicitly mentions RLUR in baseline or comparison context. |
| [2025_WWW_xMTF_Formula-Free-RL-Multi-Task-Fusion.md](./2025_WWW_xMTF_Formula-Free-RL-Multi-Task-Fusion.md) | Introduction / Summary | Explicitly names full title in the card evidence. |

## Meta Information

**Authors:** Qingpeng Cai et al.  
**Affiliations:** Kuaishou Technology  
**Venue:** WWW  
**Year:** 2023  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
