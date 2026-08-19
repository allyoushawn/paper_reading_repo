# Paper Analysis: Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/25355.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

Hongzu Su, Zhekai Du, Jingjing Li, Lei Zhu, and Ke Lu (University of Electronic Science and Technology of China; Shandong Normal University), "Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction," AAAI 2023 (AAAI-23). The paper targets LTV prediction on a data-scarce advertising platform by transferring knowledge from a data-abundant "source" platform advertising the same product (in their five Tencent Games datasets, the source has roughly 30x more samples than the target). The proposed framework, CDAF, first pre-trains a "source expert" feature-embedding-and-predictor model on the source platform using a ZILN-style loss (a cross-entropy payment-indicator term plus a lognormal negative-log-likelihood term for the positive part), then initializes a target model from it and jointly (a) minimizes the sliced Wasserstein discrepancy between encoded source and target user representations to learn domain-invariant information, and (b) trains two separate predictors — one for each domain — while minimizing the ℓ1 distance between their outputs (Dual Predictors Optimization) to preserve domain-specific information without losing the shared signal. The final target-domain LTV prediction is the mean of the two predictors' outputs. Across five real-world datasets from Tencent Games advertising and eight different feature-embedding backbones (DNN, WDL, DCN, DeepFM, FiBiNet, GateNet, DCNv2, and a Mixed GateNet+DCNv2 model), CDAF improves AUC by an average of 6.8-14.5% and normalized Gini by 7.8-13.2% over single-domain-trained models, and outperforms a straightforward fine-tuned source-expert baseline as well.

## 2. Experiment Critique

Evaluated on five paired source/target datasets (G1-G5) sampled from three months of historical Tencent Games advertising data, with a held-out evaluation and test split for each domain (Table 1). The comparison spans eight feature-embedding backbones in two settings (single-domain "single" vs. CDAF), plus a fine-tuning baseline and a four-way ablation (Table 4) isolating the Wasserstein-discrepancy loss, the ℓ1 dual-predictor loss, and each predictor individually. No statistical significance tests (p-values, confidence intervals) are reported for the AUC/Gini improvements in Tables 2-3, and no online A/B test is described anywhere in the paper — all results are offline. The ablation study (Table 4) shows the contribution of each component varies noticeably by dataset (Wasserstein discrepancy and target predictor dominate on G1; ℓ1 distance and source predictor dominate on G2), which the authors note themselves rather than presenting a single clean attribution story.

## 3. Industry Contribution

Motivated by a concrete industry problem stated in the introduction: new or smaller advertising platforms have far fewer consumption samples than established ones (illustrated by a >4-order-of-magnitude funnel from ad request to consumption in their own data, Fig. 1a), and directly training a DNN-based LTV model on scarce target data underperforms. CDAF is explicitly designed to be backbone-agnostic — it is evaluated on top of eight different CTR-style feature-embedding architectures already in industrial use — which makes it easy to bolt onto an existing production LTV pipeline. It has not been reported as deployed in production in the retrieved text; the evaluation is entirely on historical Tencent Games data.

## 4. Novelty vs. Prior Work

Claims to be "the first attempt at domain adaptive LTV prediction in the community." Builds its base loss directly on Wang, Liu & Miao's ZILN paper ("A deep probabilistic model for customer lifetime value prediction," arXiv 2019 — already a core reference in this survey) and its domain-adaptation machinery on Wasserstein GAN theory (Arjovsky, Chintala & Bottou 2017) and sliced Wasserstein discrepancy (Lee, Batra, Baig & Ulbricht, "Sliced Wasserstein Discrepancy for Unsupervised Domain Adaptation," CVPR 2019). Cites Vanderveld et al., "An Engagement-Based Customer Lifetime Value System for E-commerce," KDD 2016, and Xing et al., "Learning Reliable User Representations from Volatile and Sparse Data to Accurately Predict Customer Lifetime Value" (TSUR), KDD 2021, as prior ML-based LTV approaches it positions against for requiring abundant labeled target-domain data; also cites Bauer & Jannach, "Improved Customer Lifetime Value Prediction With Sequence-To-Sequence Learning and Feature-Based Models," ACM TKDD 2021, as a related sequence-based approach.

## 5. Dataset Availability

| Dataset | Size | Label | Public? |
|---|---|---|---|
| G1-G5 (Tencent Games advertising, source/target pairs) | Source: 2.9M-6.7M train samples per dataset; target: 2,530-183,413 train samples per dataset (Table 1) | Total consumption over trailing 7 days, linked via anonymous ad identifier | No — proprietary Tencent advertising platform data |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

1. **Title, authors, venue, year, URL:** "Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction," Hongzu Su, Zhekai Du, Jingjing Li, Lei Zhu, Ke Lu, Proceedings of the 37th AAAI Conference on Artificial Intelligence (AAAI-23), 2023. Code: https://github.com/TL-UESTC/CDAF
2. **Source type:** Academic (UESTC, Shandong Normal University), using proprietary industry (Tencent Games advertising) data.
3. **Direction:** D4.
4. **Problem setting:** Cross-domain LTV prediction for online advertising platforms, where a newly launched or lower-traffic platform lacks sufficient labeled consumption data to train an accurate LTV model directly.
5. **Objective and label definition:** LTV label = total consumption over the trailing 7 days, linked across a data-abundant "source" platform and a data-scarce "target" platform via anonymous advertisement identifier (e.g., IDFA). Horizon: fixed 7-day window; no censoring or survival treatment is discussed. Zero-inflation/heavy-tail handling: the paper explicitly "follow[s] the assumption that the underlying LTV data conform to lognormal distribution and optimize[s]... with a variant of ZILN loss" — a cross-entropy term on a payment indicator plus, conditional on payment, a lognormal negative-log-likelihood term (Eq. 1-2). **Differs from ZILN:** this paper does not modify the zero-inflated-lognormal loss itself — it reuses ZILN's formulation unchanged as the supervised loss for both the source expert and the two "dual predictors." Its actual novel contribution is a cross-domain adaptation layer around that unchanged loss: sliced Wasserstein discrepancy minimization between source- and target-domain encoded user representations, plus ℓ1-distance alignment between the two predictors' output distributions, aimed at data scarcity in the target domain rather than at the label or loss formulation.
6. **Prediction or incrementality:** Prediction only — the paper does not address incrementality. Both the source expert and the target dual-predictors regress a customer's future 7-day ad-driven consumption directly from features; there is no treatment/exposure counterfactual framing, and the "adaptation" machinery is a domain-transfer (distribution-shift) technique, not a causal-effect estimate.
7. **Model architecture:** Two-stage: (1) a "source expert" (feature-embedding model + predictor) pre-trained on abundant source-domain data with the ZILN-variant loss; (2) a target model with its own feature-embedding model (initialized from the source expert) and two predictors — a source predictor and a target predictor — trained with sliced Wasserstein discrepancy minimization on encoded representations plus ℓ1-distance minimization between the two predictors' outputs. Final prediction = mean of the two predictors. Feature-embedding backbone is interchangeable with standard CTR architectures (Wide&Deep, DCN, DeepFM, FiBiNet, GateNet, DCNv2, or a Mixed GateNet+DCNv2 model).
8. **Credit assignment:** Not specified in source — user-level consumption over a fixed 7-day window aggregated by advertisement identifier; no per-exposure or per-impression decomposition, since this is a customer-level LTV regression, not a ranking or credit-assignment problem.
9. **Training data and counterfactual handling:** Historical logged interaction data from two advertising platforms of Tencent Games, five paired source/target datasets (G1-G5); purely observational supervised regression/classification. No counterfactual or propensity-weighting correction — the alignment technique is distributional (domain adaptation), not causal.
10. **Offline and online evaluation:** Offline only. AUC of the payment-probability indicator and normalized Gini coefficient of predicted vs. actual LTV, on held-out target-domain test sets across G1-G5 (Table 2). No online A/B test is reported.
11. **Reported gains:** CDAF improves AUC by an average of 13.2%, 9.7%, 14.5%, 9.9%, 6.8%, and 9.6% over single-domain-trained DNN, WDL, DCN, DeepFM, FiBiNet, GateNet, DCNv2, and Mixed-model backbones respectively, on the Tencent Games G1-G5 advertising datasets (Table 2). Normalized Gini improves by 16.6-27.4% relative to the single-domain Mixed model across G1-G5. CDAF also beats a fine-tuned source-expert baseline by 3.2-9.6% AUC and 7.4-24.7% Gini across G1-G5 (Table 3).
12. **Applicability to a two-sided dating recommender:** Not applicable — this is a single-sided advertising-platform LTV regression problem (predicting a user's 7-day ad-driven consumption) with no reciprocal match, congestion, or exposure-ranking decision. The only transferable idea is the source-to-target domain-adaptation technique, potentially useful for transferring retention/LTV knowledge from a data-rich market or cohort to a data-scarce one, but the paper never frames a two-sided market.
13. **Unverified claims:** The claim to be "the first attempt at domain adaptive LTV prediction in the community" is a priority claim not independently verified here. The statement that removing components in the ablation study (Table 4) "does not lead to severe performance degradation" is somewhat inconsistent with the actual numbers shown — e.g., removing the target predictor drops AUC from 0.740 to 0.717 and Gini from 0.625 to 0.593 on G1 — so this framing should be read as the authors' interpretation rather than a strictly supported characterization.

## Project Relevance

Speaks to **Q3** (label = 7-day consumption window; zero-inflated distribution handled via a ZILN-derived loss, already covered by the survey's core ZILN reference) and marginally **Q1** (training objective is value regression via that ZILN-style loss). The paper's genuinely new content — cross-domain distributional alignment for data-scarce target advertising platforms — does not map onto any of the eight research questions directly; it is a transfer-learning technique, not a retention/revenue-ranking-objective, credit-assignment, or two-sided-market technique. Does not address **Q2, Q4, Q5, Q6, Q7, Q8**. Given the survey already holds ZILN and Kuaishou's billion-user LTV system, this paper adds only the idea of cross-domain LTV transfer — potentially useful if the project needed to bootstrap a retention/revenue model for a new, data-scarce market or cohort, but otherwise tangential to the core migration question.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `CDAF`._

## Meta Information

- **Authors:** Hongzu Su, Zhekai Du, Jingjing Li, Lei Zhu, Ke Lu
- **Affiliations:** University of Electronic Science and Technology of China (Su, Du, Li, Lu); Institute of Electronic and Information Engineering of UESTC in Guangdong (Li); Shandong Normal University (Zhu)
- **Venue:** AAAI (AAAI-23)
- **Year:** 2023
- **Relevance:** Related
- **Priority:** 4
- **NotebookLM source:** nlm:f0fa7383
