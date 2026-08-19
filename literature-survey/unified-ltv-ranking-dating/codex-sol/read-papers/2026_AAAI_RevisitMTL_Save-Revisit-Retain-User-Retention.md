# Paper Analysis: Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems

**Source:** https://arxiv.org/pdf/2511.18013.pdf  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems  
**Authors:** Weijie Jiang; Armando Ordorica; Jaewon Yang; Olafur Gudmundsson; Yucheng Tu; Huizhong Duan  
**Abstract:** Pinterest builds surrogate attribution from a search-surface save to same-/cross-day profile revisitation, aggregates seven-day cross-session events, and adds revisitation as an auxiliary ranking task.  
**Methodology:** Deterministic save→revisit linkage, seven-day event pipeline, multi-task save/revisit prediction, ranking boost for high joint probability.  
**Main results:** Two-month, 24M-user A/B test: +1.18% actions/user and +1.42% unique-user propensity on 7-day revisits; +0.10% active users; additional time/session gains. Deployed to 500M+ users without added compute.

## 2. Experiment Critique

**Design:** Large behavior analysis, offline metrics, and April–June 2025 A/B with ~12M users per arm.  
**Statistical validity:** Table reports p-value tiers; active-user lift significant at p<0.05.  
**Online experiments:** Yes, Pinterest Related Pins.  
**Reproducibility:** Proprietary event logs.  
**Overall:** Rare direct evidence that an auxiliary item-level long-term surrogate lifts active users; attribution is heuristic, not identified causal effect.

## 3. Industry Contribution

**Deployability:** Lightweight deployed pipeline.  
**Problems solved:** Multi-day attribution and scalable label construction.  
**Engineering cost:** Cross-surface seven-day event joins and an extra MTL head; no inference-cost increase.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Scalable surrogate attribution for multi-day item revisitation explicitly tied to retention.  
**Prior work comparison:** Contrasts immediate-action rankers and long-sequence RL.  
**Verification:** Indexed paper only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Pinterest save/revisit events | Not specified in source. | No | Cross-session/surface labels. |

**Offline experiment reproducibility:** Not specified.

## 6. Community Reaction

Not specified.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D4  
**Problem setting:** Search/Related Pins ranking for multi-day revisitation and retention.  
**Objective and label definition:** Save followed by revisit of the saved item, including same-day, 1-day, and 7-day grid/impression outcomes; seven-day aggregation handles delay. Highly active users dominate labels; censoring beyond seven days is truncated by design.  
**Prediction or incrementality:** Predictive surrogate attribution, not causal exposure uplift.  
**Model architecture:** Existing multi-task ranker plus save/revisit auxiliary task and scalable features.  
**Credit assignment:** Revisit is credited only to the previously saved Pin when revisited from the user profile, reducing but not eliminating confounding.  
**Training data and counterfactual handling:** Observational linked events; randomized A/B validates policy impact, but training has no counterfactual correction.  
**Offline and online evaluation:** Extensive offline plus 24M-user two-month A/B.  
**Reported gains:** +0.10% active users; +1.18%/1.42% 7-day revisit volume/propensity.  
**Unverified claims:** Authors call links causal, but the paper itself notes confounding; treat the label as surrogate attribution.

## Project Relevance

**Source-stated facts:** This is an auxiliary-head-first migration using explicit item-level multi-day labels and demonstrates an active-user lift.

**Survey inference:** Dating can link a shown profile to later mutual match/conversation and 7-day return using conservative windows, but reciprocal outcomes require B’s action and compete for B’s attention. Heuristic attribution can over-credit naturally active users; randomized/propensity-aware learning and marketplace tests are still needed. Positive churn also makes active users an incomplete success metric.

**Applicability note:** One of the most actionable label-pipeline and staged-migration references in the batch.  
Its heuristic one-sided attribution must be upgraded for reciprocal, incremental dating outcomes.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Weijie Jiang et al.  
**Affiliations:** Pinterest Inc.  
**Venue:** AAAI  
**Year:** 2026  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
