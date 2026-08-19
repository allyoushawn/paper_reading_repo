# Paper Analysis: Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction

**Source:** https://arxiv.org/abs/2011.11826  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction  
**Authors:** Yanshi Wang; Jie Zhang; Qing Da; Anxiang Zeng  
**Abstract:** ESDF jointly addresses sparse conversions, clicked-sample selection bias, and delayed labels. It shares CTR/CVR embeddings over all impressions and uses discrete-day survival probabilities without a parametric delay assumption.  
**Methodology:** Multi-task CTR and click-through-conversion heads over the entire impression space, sequential behavior features, and a seven-slot neural survival model.  
**Main results:** Public AUC 0.7811 and product GAUC 0.6181, relative improvements of 4.93% and 6.68% over ESMM. About 20% of conversions arrive after day one.

## 2. Experiment Critique

**Design:** Public sample (30.6M impressions, 14.7K conversions) and product logs (11.1B impressions, 5.53M conversions), seven-day attribution, ESMM/naive/shift/DFM baselines.  
**Statistical validity:** Large-scale offline comparison; no online A/B or uncertainty intervals.  
**Online experiments:** Not specified in source.  
**Reproducibility:** A sampled delayed-conversion dataset is released, though the indexed URL placeholder is incomplete.  
**Overall:** Strong delayed-label engineering, but short-horizon CVR rather than retention/LTV.

## 3. Industry Contribution

**Deployability:** Distribution-free discrete survival design is production-friendly.  
**Problems solved:** False negatives from label immaturity, conversion sparsity, train/serve space mismatch.  
**Engineering cost:** Entire-space joins, shared multi-task model, seven-day maturation and survival targets.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First unified entire-space solution for sparsity, selection bias, and conversion delay.  
**Prior work comparison:** ESMM/ESM2, exponential DFM, nonparametric delay models.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| ESDF public sample | Not specified in source. | Claimed public | Impression/click/conversion/delay labels. |
| Alibaba product dataset | Not specified in source. | No | 11.1B impressions. |

**Offline experiment reproducibility:** Partial via sampled dataset.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D7  
**Problem setting:** Entire-space e-commerce CVR with delayed purchases.  
**Objective and label definition:** Conversion within seven days of click; delay discretized by day; immature observations enter survival likelihood.  
**Prediction or incrementality:** Prediction, not exposure uplift.  
**Model architecture:** Shared-embedding CTR/CTCVR/CVR multi-task network plus discrete survival-delay head.  
**Credit assignment:** Purchase attributed to click within seven days; no multi-touch or user-retention attribution.  
**Training data and counterfactual handling:** Observational impressions/clicks/conversions; entire-space tasks reduce selection bias but do not identify causal effects.  
**Offline and online evaluation:** Large offline product/public evaluation; no online test.  
**Reported gains:** 6.68% relative GAUC improvement over ESMM on product data.  
**Unverified claims:** Retention/revenue horizon beyond conversion and causal impact Not specified.

## Project Relevance

**Source-stated facts:** ESDF provides a practical template for a sparse delayed cascade head trained before all labels mature.

**Survey inference:** The dating team can adapt discrete hazards for 7–30-day retention or revenue and share representations with like/match/conversation heads. However, a click-conversion chain is unilateral; mutual match, candidate attention, interference, incrementality, and successful-match churn remain unsolved.

**Applicability note:** Useful label-maturity machinery for delayed dating value heads.  
Not a unified causal or reciprocal ranker by itself.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Yanshi Wang et al.  
**Affiliations:** Alibaba Group  
**Venue:** AAAI  
**Year:** 2021  
**PDF:** Available  
**Relevance:** Related  
**Priority:** 2
