# Paper Analysis: Mini-Game Lifetime Value Prediction in WeChat

**Source:** https://arxiv.org/html/2506.11037v3  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Mini-Game Lifetime Value Prediction in WeChat  
**Authors:** Aochuan Chen; Yifan Niu; Ziqi Gao; Yujie Sun; Shoujun Liu; Gong Chen; Yang Liu; Jia Li  
**Abstract:** GRePO-LTV predicts user-item mini-game purchase contribution under ~0.1% purchase rates. Graph representations transfer collaborative signal, while Pareto optimization balances 3-, 7-, and 30-day LTV objectives.  
**Methodology:** User/item graph representation learning, multi-horizon towers, ZILN-style targets, and Pareto gradient balancing.  
**Main results:** Online: +9.91%/+9.83% LTV/GMV at 3 days, +7.80%/+7.93% at 7 days, +7.73%/+7.60% at 30 days; +8.4% average GMV. Prediction instability is about half the baseline.

## 2. Experiment Critique

**Design:** Proprietary WeChat mini-game offline data, multiple baselines/ablations, online A/B and adjacent-day stability.  
**Statistical validity:** Online relative lifts reported; duration, confidence intervals, and assignment are Not specified.  
**Online experiments:** Yes, WeChat mini-game traffic.  
**Reproducibility:** Proprietary dataset.  
**Overall:** Strong multi-horizon item-level LTV evidence, but observational prediction and ad/game context limit causal transfer.

## 3. Industry Contribution

**Deployability:** Production online validation.  
**Problems solved:** 0.1% purchase sparsity, correlated horizon conflicts, daily model instability.  
**Engineering cost:** Large graphs, multi-horizon towers, Pareto optimizer, stability monitoring.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Graph-represented Pareto-optimal multi-horizon LTV.  
**Prior work comparison:** LTV, graph recommendation, ZILN, Pareto multi-task optimization.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| WeChat mini-game recommendation | Not specified in source. | No | User-item purchases and 3/7/30-day GMV. |

**Offline experiment reproducibility:** Not specified.

## 6. Community Reaction

Not specified.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D4  
**Problem setting:** User-item LTV prediction for mini-game advertising.  
**Objective and label definition:** Cumulative purchase contribution at 3, 7, and 30 days; low base rate ~0.1%; multi-horizon objectives mitigate delayed maturity. Censoring Not specified.  
**Prediction or incrementality:** Conditional prediction, not exposure uplift.  
**Model architecture:** Graph representations + multi-horizon backbone/towers + Pareto optimization.  
**Credit assignment:** LTV is defined for a user and particular mini-game/item, giving item-level labels; attribution mechanism from repeated exposures is Not specified.  
**Training data and counterfactual handling:** Observational recommendation/purchase data; no propensity correction.  
**Offline and online evaluation:** Offline metrics, live A/B, stability analysis.  
**Reported gains:** +8.4% average GMV and multi-horizon lifts above.  
**Unverified claims:** Incremental effect and exposure attribution absent.

## Project Relevance

**Source-stated facts:** Directly shows a 3/7/30-day item-specific LTV head under extremely rare purchase labels and multi-horizon conflict.

**Survey inference:** Dating can use analogous profile-exposure revenue heads for subscription and a-la-carte spend, with graph signals helping sparse outcomes. Yet repeated candidate exposures, active-user confounding, reciprocity, candidate capacity, interference, and successful-match churn require causal and marketplace layers beyond GRePO-LTV.

**Applicability note:** Strongest revenue-label/horizon and low-base-rate architecture in this batch.  
Must be paired with exposure-level incrementality and reciprocal-market constraints for dating ranking.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Aochuan Chen et al.  
**Affiliations:** Tencent; HKUST (Guangzhou)  
**Venue:** KDD  
**Year:** 2025  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
