# Paper Analysis: Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2021 (Alibaba) (AAAI) [ESDF] Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction.pdf
**Date analyzed:** 2026-08-16

## 1. Summary

Yanshi Wang, Jie Zhang, Qing Da, and Anxiang Zeng, of Alibaba Group, tackle three CVR-prediction challenges jointly — data sparsity, sample selection bias (SSB, the mismatch between training on clicks and inferring over all impressions), and delayed feedback — in a single framework, **ESDF**. It combines an ESMM-style entire-space multi-task structure (shared embeddings across a pCTR tower and a pCTCVR tower, following the "impression → click → conversion" sequential-behavior chain, which addresses sparsity and SSB) with a delay-time model built on survival analysis rather than a parametric hazard: delay time is discretized into day-slots {1, …, T, T+1} (T=7 in the experiments, with the T+1 bin absorbing all conversions after day 7), and a deep network predicts a softmax "survival" distribution over slots, explicitly avoiding the exponential (Chapelle 2014) or Weibull-mixture (Ji, Wang & Zhu 2017) distributional assumptions. Training treats the eventual-conversion indicator C as a hidden variable and uses EM: samples split into three observed groups — clicked-and-converted, clicked-and-not-yet-converted, and not-clicked — with the E-step computing a posterior weight for the "not-yet-converted" group directly from the model's current survival-tail estimate, and the M-step maximizing the resulting expected log-likelihood. The paper releases a new public sampled dataset (impressions, clicks, and delayed conversion labels together, which it states is the first such public dataset) alongside a much larger industrial "Product Dataset," and evaluates against ESMM, a naive fake-negative-removal baseline, a window-extension heuristic (SHIFT), and a DNN-reimplemented DFM.

## 2. Experiment Critique

One-paragraph summary (priority 3, per depth rule): the evaluation is offline only, on a newly released public dataset (30.6M impressions, 0.74M clicks, 14.7K conversions, 7-day attribution) and a much larger industrial Product Dataset (11.1B impressions, 291M clicks, 5.53M conversions, same 7-day attribution). Metrics are AUC (public dataset, chosen because sparse per-request impressions under random sampling would collapse group AUC to 0.5) and group-AUC (GAUC, industrial dataset), plus a RelaImpr metric normalized against the ESMM baseline; no confidence intervals or significance tests are reported, and there is no online A/B test. A useful secondary analysis (Figure 3) breaks log loss out specifically on delayed-feedback samples by day, showing all methods perform best on first-day-observed data and that ESDF and DFM are the only methods that track this degradation gracefully — though the paper also candidly notes DFM "is a bit unstable on the public dataset," attributing this to the mismatch between the true delay distribution and DFM's exponential assumption.

## 3. Industry Contribution

One-paragraph summary (priority 3, per depth rule): the paper is framed around a genuine production trade-off — click-based CVR training data is small and selection-biased relative to the impression space it must serve, and conversions arrive late — and ESDF's entire-space multi-task design directly reuses the now-standard ESMM serving pattern (shared embeddings, additional prediction head), so the marginal engineering cost over an existing ESMM deployment is one extra delay-slot softmax head, discarded at serving time just as DFM's hazard head is. The public dataset release (the first, per the authors, to include impression/click/delayed-conversion labels together) is itself a durable contribution to the sub-field's reproducibility, independent of the paper's modeling claims.

## 4. Novelty vs. Prior Work

One-paragraph summary (priority 3, per depth rule): the explicit novelty claim is being "the first attempt to unitedly solve" data sparsity, sample selection bias, and delayed feedback simultaneously — a claim about scope/combination rather than a new individual mechanism, though the non-parametric discretized-survival delay head is itself a genuine departure from Chapelle's exponential assumption. The most heavily cited/discussed prior works are Ma et al. (2018), ESMM, the entire-space multi-task founding method this paper's sparsity/SSB handling directly extends; Wen et al. (2020), ESM², a generalization of ESMM's behavior chain, also extended here; Chapelle (2014), the delayed-feedback founding paper (this batch's paper 1, reimplemented with a DNN backbone as the DFM baseline); Ji, Wang & Zhu (2017), a Weibull-mixture delay-distribution alternative to Chapelle's exponential assumption; and Yoshikawa & Imai (2018), a non-parametric delayed-feedback model, the closest prior distribution-free delay approach.

## 5. Dataset Availability

| Dataset | Size | Description | Public? |
|---|---|---|---|
| Public Dataset (released with this paper) | Feature dimension 1.7B, 240 feature fields, 30.6M impressions, 0.74M clicks, 14.7K conversions, 7-day attribution window | First public dataset (per the authors) with impression, click, and delayed-conversion labels together, sampled from an industrial e-commerce search system | Yes — the paper states a URL is provided in the camera-ready version |
| Product Dataset | Feature dimension 5.0B, 544 feature fields, 11.1B impressions, 291M clicks, 5.53M conversions, 7-day attribution window | Full industrial e-commerce click/conversion streaming logs (2020-05-30 to 2020-06-06) | No — proprietary Alibaba data |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

1. **Title, authors, venue, year, URL:** "Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction," Yanshi Wang, Jie Zhang, Qing Da, Anxiang Zeng, Alibaba Group, AAAI 2021 (arXiv:2011.11826). https://arxiv.org/abs/2011.11826
2. **Source type:** Industry paper (Alibaba Group; peer-reviewed at AAAI).
3. **Direction:** D7.
4. **Problem setting:** Post-click CVR prediction in e-commerce search/recommendation, addressing data sparsity, sample selection bias (train-on-clicks vs. infer-on-impressions), and delayed/censored conversion feedback jointly, from an entire-space (ESMM-style) perspective.
5. **Objective and label definition:** Entire-space multi-task prediction of pCTR = P(click=1|x) and pCTCVR = P(conversion=1, click=1|x) (pCVR = pCTCVR/pCTR); delay handled by discretizing time into day-slots {1,…,T,T+1} (T=7 in experiments; the final bin absorbs conversions occurring later than day 7) and predicting a softmax survival distribution over slots via a deep network, with no parametric assumption on the delay's shape. Horizon: a 7-day attribution window for both released datasets (the paper's own Figure 2 shows ~80% of conversions occur on day 0, the remainder trailing through day 6+) — the shortest, and closest to the project's own 7-day retention floor, of any paper in this batch.
6. **Prediction or incrementality:** Prediction only — the paper does not address incrementality.
7. **Model architecture:** Shared-embedding multi-task deep network (Figure 1) with three towers — pCTR, pCTCVR, and a time-delay softmax head over discretized day-slots — with the eventual-conversion indicator C trained as a latent variable via EM (E-step: posterior weight from the model's current survival-tail estimate; M-step: weighted log-likelihood over three observed sample groups).
8. **Credit assignment:** Not specified in source. As with the rest of this batch, the prediction unit is one click/impression and its own (possibly delayed) conversion; the entire-space multi-task structure addresses sample-selection bias between click space and impression space, not a user-level-to-item-level aggregation problem.
9. **Training data and counterfactual handling:** A newly released public sampled dataset plus a much larger industrial Product Dataset (see Dataset Availability). No importance sampling or sample duplication is used; censored ("not-yet-converted") samples are handled purely through the EM latent-variable machinery, using the model's own current delay-slot predictions as the source of the pseudo-label weight. The paper offers no formal unbiasedness or consistency proof for this EM estimator — unlike FSIW's Theorem 5.1 or DEFUSE's appendix proof, ESDF's claim of correctly handling censoring is empirical (comparative AUC/GAUC), not proven.
10. **Offline and online evaluation:** Offline only. Metrics: AUC (public dataset) and group-AUC/RelaImpr relative to an ESMM baseline (industrial dataset). No online (live A/B) evaluation is reported.
11. **Reported gains:** ESDF achieves a 4.93% RelaImpr over the ESMM baseline on the public dataset (AUC 0.7679 to 0.7811, Table 3) and a 6.68% RelaImpr on the industrial Product Dataset (GAUC 0.6107 to 0.6181). Versus the strongest delay-aware baseline (DFM, reimplemented with a DNN backbone), ESDF improves RelaImpr by 0.82% (public dataset) and 3.16% (product dataset).
12. **Applicability to a two-sided dating recommender:** The non-parametric discretized-survival delay head avoids DFM's exponential assumption and this paper's 7-day attribution window is the closest of any paper in this batch to the project's own 7-day retention floor — but it is still far short of the 30-day upper bound or multi-week revenue horizon, and the entire-space (ESMM-style) sequential-behavior chain is single-sided with no reciprocity, congestion, or two-sided fairness treatment for a dating market.
13. **Unverified claims:** The claim to be "the first attempt to unitedly solve" all three challenges simultaneously is a novelty claim, not independently falsifiable from within the paper, though consistent with its own related-work review. Unlike FSIW and DEFUSE, this paper provides no formal unbiasedness or consistency proof for its EM-based delay estimator — flagged here as **Not specified in source** whether the estimator is even asymptotically unbiased; its correctness claim rests entirely on comparative empirical AUC/GAUC gains.

## Project Relevance

This paper speaks most directly to **Q3** (label/horizon/delay handling) — its 7-day attribution window is the closest in this batch to the project's own 7-day retention floor, and its discretized non-parametric survival mechanism is a genuinely different tool from both DFM's exponential hazard and FSIW/DEFUSE's importance weighting. It touches **Q2** only superficially: the entire-space multi-task structure addresses *sample selection bias* between click-space and impression-space training, which is a related but distinct problem from attributing a delayed user-level outcome to a specific item-level decision, so it should not be read as answering Q2 as posed. It does not meaningfully address **Q1** (the objective is still short-horizon post-click conversion, not retention/LTV), **Q4–Q5** (no long/short-term head fusion, no incrementality), **Q6** (no online evaluation), or **Q7** (no two-sided/reciprocal market treatment).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md](./2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md) | Related Work / Experiments | Names this paper's method (`ESDF`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `ESDF` across all 133 cards._

## Meta Information

- **Authors:** Yanshi Wang, Jie Zhang, Qing Da, Anxiang Zeng
- **Affiliations:** Alibaba Group
- **Venue:** AAAI 2021
- **Year:** 2021
- **Relevance:** Core
- **Priority:** 3
- **NotebookLM source:** nlm:25c2b5cc
