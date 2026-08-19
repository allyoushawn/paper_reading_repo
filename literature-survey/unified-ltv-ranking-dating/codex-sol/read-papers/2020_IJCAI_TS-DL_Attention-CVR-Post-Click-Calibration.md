# Paper Analysis: An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration

**Source:** https://www.ijcai.org/proceedings/2020/487  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration  
**Authors:** Yumin Su; Liang Zhang; Quanyu Dai; Bo Zhang; Jinyao Yan; Dan Wang; Yongjun Bao; Sulong Xu; Yang He; Weipeng Yan  
**Abstract:** TS-DL transfers dense impression/click representations into sparse CVR modeling, uses attention over click histories, and dynamically recalibrates a survival hazard with post-click behavior that arrives before purchase.  
**Methodology:** Pretrained content embeddings, self/inner attention, two-stage conversion network, dynamic post-click hazard/survival model.  
**Main results:** Relative AUC improvements over DIN are 5.24%, 44.76%, and 8.02% across two WeChat placements and JD-MP. Delay-distribution JS divergence falls 23.9% on JD-MP test data versus DFM.

## 2. Experiment Critique

**Design:** Three real e-commerce datasets; DFM, DIN, Wide&Deep, GRU+attention and ablations.  
**Statistical validity:** Offline AUC/calibration comparisons; no uncertainty or online lift.  
**Online experiments:** Not specified.  
**Reproducibility:** Industrial data unavailable.  
**Overall:** Dynamic intermediate behavior improves delay modeling, but the task remains post-click CVR.

## 3. Industry Contribution

**Deployability:** Uses abundant post-click events to update delay estimates.  
**Problems solved:** Sparse conversion history, static-delay misspecification, false negatives.  
**Engineering cost:** Pretraining pipeline, behavior sequences, attention, hazard recalibration.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Dynamic post-click calibration of delayed CVR using attention and survival analysis.  
**Prior work comparison:** DIN, DFM, nonparametric delayed feedback.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Two WeChat placements; JD-MP | Not specified in source. | No | Impression/click/post-click/conversion data. |

**Offline experiment reproducibility:** Not specified.

## 6. Community Reaction

Not specified.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D7  
**Problem setting:** CVR prediction with seconds-to-weeks delay and sparse positives.  
**Objective and label definition:** Post-click conversion; dynamic hazard updated by post-click actions. Exact attribution window/censoring Not specified.  
**Prediction or incrementality:** Prediction, not uplift.  
**Model architecture:** Transfer embeddings + attention sequence model + survival-delay calibration.  
**Credit assignment:** Conversion assigned to clicked ad/item; no multi-exposure long-term attribution.  
**Training data and counterfactual handling:** Observational user behavior; transfer reduces sparsity, not confounding.  
**Offline and online evaluation:** Offline across three industrial datasets.  
**Reported gains:** Up to 44.76% relative AUC improvement over DIN.  
**Unverified claims:** Online and retention/revenue impact Not specified.

## Project Relevance

**Source-stated facts:** Post-click intermediate actions can dynamically update beliefs about a delayed outcome rather than freezing at exposure time.

**Survey inference:** In dating, likes, reciprocal likes, and early messages can update a retention/revenue hazard as the cascade unfolds. The architecture still needs exposure-level incrementality, bilateral state, congestion/interference controls, and protection against successful-match churn.

**Applicability note:** Useful dynamic-hazard component for a staged cascade-to-long-term head.  
Not evidence for a unified reciprocal LTV policy on its own.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Yumin Su et al.  
**Affiliations:** JD.com; Hong Kong Polytechnic University; Communication University of China  
**Venue:** IJCAI  
**Year:** 2020  
**PDF:** Available  
**Relevance:** Related  
**Priority:** 2
