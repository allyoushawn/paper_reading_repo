# Paper Analysis: Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems

**Source:** https://arxiv.org/pdf/2208.04560  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems  
**Authors:** Qihua Zhang; Junning Liu; Yuzhuo Dai; Yiyan Qi; Yifan Yuan; Kunlun Zheng; Fan Huang; Xianfeng Tan  
**Abstract:** BatchRL-MTF learns personalized request/session fusion weights over 12 multi-task prediction scores. A batch-RL policy optimizes accumulated stickiness/activeness rewards from fixed logs, conservative offline evaluation controls extrapolation, and bounded online exploration escapes local optima.  
**Methodology:** State combines profile and 500-video history; action is a 12-dimensional fusion-weight vector; reward heuristically combines user stickiness and activeness; discount factor is 0.95.  
**Main results:** A one-month production A/B test improved app dwell time by 2.550% and positive-interaction rate by 9.651%.

## 2. Experiment Critique

**Design:** Billion-sample temporal 90/10 split, conservative offline policy estimator, baselines, reward-weight sensitivity, and one-month online A/B test.  
**Statistical validity:** Robustness/extrapolation analyses are reported; confidence intervals and retention metrics are Not specified.  
**Online experiments:** Yes; production short-video platform serving hundreds of millions.  
**Reproducibility:** Proprietary data; architecture hyperparameters are described but data/code unavailable.  
**Overall:** Strong migration evidence from fixed fusion to learned long-term fusion, but “satisfaction” is a heuristic engagement reward rather than observed retention/LTV.

## 3. Industry Contribution

**Deployability:** Deployed industrially.  
**Problems solved:** Personalized fusion, offline RL safety, online local-optimum escape.  
**Engineering cost:** Batch-RL actor/critic/generative networks, 12 base heads, conservative OPE, controlled exploration.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Batch RL applied to industrial multi-task fusion with a conservative evaluator and bounded online exploration.  
**Prior work comparison:** Contrasts grid/Bayesian weight search, evolutionary fusion, simulators, on-policy RL, FQE, and CQL.  
**Verification:** Indexed paper content only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Tencent short-video logs | Not specified in source. | No | Billion-sample sessions; temporal split. |

**Offline experiment reproducibility:** Not possible without proprietary logs.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D2  
**Problem setting:** Final-stage fusion of multiple short-video feedback predictors.  
**Objective and label definition:** Discounted accumulated heuristic reward combining stickiness and activeness; exact retention/revenue horizon, delay, sparsity, and censoring are Not specified.  
**Prediction or incrementality:** Policy outcome optimization, not incremental exposure-effect estimation.  
**Model architecture:** Offline batch-RL policy generating personalized 12-head fusion weights, conservative OPE, bounded online perturbation.  
**Credit assignment:** Session MDP discounted return; no identified item-level causal attribution.  
**Training data and counterfactual handling:** Fixed logged sessions; conservative value estimation reduces out-of-distribution action optimism, followed by controlled exploration.  
**Offline and online evaluation:** Temporal offline split and month-long A/B test.  
**Reported gains:** +2.550% dwell time; +9.651% positive-interaction rate.  
**Unverified claims:** Direct retention/LTV gains are not reported.

## Project Relevance

**Source-stated facts:** The paper exactly replaces manually tuned multi-task fusion with a personalized RL fusion policy while keeping base heads, offering a staged migration template.

**Survey inference:** A dating version can initially fuse like/match/conversation, retention, and revenue heads. Yet its heuristic satisfaction reward and unilateral setting do not establish incrementality, reciprocity, congestion, interference, or positive-churn safety; these must be added as reward/constraint and evaluation layers.

**Applicability note:** Excellent architectural migration precedent for replacing CTR/CVR-style fixed blends with learned fusion.  
Evidence is indirect for retention/revenue because reported online gains remain engagement metrics.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2025_WWW_xMTF_Formula-Free-RL-Multi-Task-Fusion.md](./2025_WWW_xMTF_Formula-Free-RL-Multi-Task-Fusion.md) | Introduction / Summary | Explicitly mentions BatchRL-MTF in baseline or comparison context. |
| [2025_arXiv_AURO_Adaptive-User-Retention-Optimization.md](./2025_arXiv_AURO_Adaptive-User-Retention-Optimization.md) | Introduction / Summary | Explicitly mentions full title in baseline or comparison context. |

## Meta Information

**Authors:** Qihua Zhang et al.  
**Affiliations:** Tencent Inc.  
**Venue:** KDD  
**Year:** 2022  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
