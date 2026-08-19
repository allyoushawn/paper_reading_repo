# Paper Analysis: Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou

**Source:** CIKM 2022 (ACM DOI 10.1145/3511808.3557152)
**Date analyzed:** 2026-08-16

## 1. Summary

Li, Shao, Yang, Fang, and Song (Kuaishou) tackle LTV prediction at billion-user scale under two compounding problems standard approaches ignore. First, Kuaishou's LTV distribution is not merely long-tailed but "atypical" — it has a raised tail (a disproportionate mass of high-value users relative to a standard long-tail shape), which conventional MSE-based or ZILN-style single-distribution models fit poorly. Second, the business needs LTV at multiple horizons simultaneously (30/90/180/365-day active days), and these horizons have a strict ordered dependency by construction (ltv30 ≤ ltv90 ≤ ltv180 ≤ ltv365); naive multi-task learning across horizons ignores this constraint and produces business-illogical predictions where a shorter horizon's estimate exceeds a longer horizon's.

The paper's contribution is the **Order Dependency Monotonic Network (ODMN)**, a shared-bottom multi-task architecture with two components. **MDME (Multi Distribution Multi Experts)** attacks the imbalanced-distribution problem per horizon via divide-and-conquer: a Distribution Segmentation Module first classifies each sample into a coarse sub-distribution (isolating high-frequency values like zero into their own sub-distribution), then a Sub-Distribution Modeling stage further buckets each sub-distribution (sized so buckets hold roughly equal sample counts) and regresses a fine-grained bias within the chosen bucket — turning a hard imbalanced-regression problem into a cascade of easier, balanced classification problems, with ordinal-regression towers distilling order information into the classification towers. **ODMN's monotonic coupling** connects the horizon tasks in series via "Mono Units" — MLPs with strictly non-negative weights — that inject the upstream (shorter-horizon) task's output distribution into the downstream (longer-horizon) task's logits, with gradient truncation so noisy downstream tasks cannot destabilize easier upstream tasks, plus an explicit calibration loss penalizing any case where a shorter-horizon prediction exceeds an adjacent longer-horizon prediction. The paper also introduces **Mutual Gini**, a new evaluation metric measuring the area between the true and predicted Lorenz curves — addressing a specific weakness of the standard normalized Gini coefficient, which can report a perfect ratio even when the two curves do not actually overlap.

Evaluated on 180 million Kuaishou users against Two-Stage (XGBoost) and ZILN baselines across all four horizons, ODMN wins on every metric at every horizon (e.g., 30-day AMBE reduced 68.3% relative to ZILN), with gains growing larger at longer horizons. A live production A/B test against a ZILN-based system delivers ROI uplifts of +11.9% (7-day), +12.8% (14-day), and +14.7% (30-day).

## 2. Experiment Critique

**Design.** Offline comparison against Two-Stage (XGBoost) and ZILN baselines across all four horizons on the same 180M-user dataset, plus two dedicated ablations isolating each claimed contribution: MDME components (four variants — NM, NMB, NMO, MDME) and ODMN components (four variants — S, SM, SC, ODMN).

**Statistical validity.** Offline metrics (NRMSE, NMAE, AMBE, Mutual Gini, Gini*) are reported as single point values per method per horizon, with no confidence intervals, standard errors, or repeated-run variance — a notably lower statistical bar than the ZILN paper's 50-run KDD Cup analysis in this same batch. The online A/B test uses a 10% control / 10% experimental traffic split and reports ROI only as relative uplift (absolute values withheld "for company privacy"), with no significance test or confidence interval given for the online percentages.

**Online experiments.** A real production A/B test on Kuaishou's user-growth advertising platform, accumulated over 7/14/30 days and measured against a non-trivial baseline (a ZILN-based system that was itself the prior state-of-the-art), not a strawman.

**Reproducibility.** The 180M-user dataset is proprietary and not released. Architecture and loss functions (MDME cascade, Mono Units, calibration loss) are specified in full mathematical detail sufficient for conceptual reimplementation. No code release is mentioned.

**Overall.** A well-designed ablation structure that cleanly isolates the two claimed contributions, backed by a genuine online deployment against a strong baseline — but the absence of any variance or significance reporting, for both the offline table and the online ROI figures, weakens confidence in the precise magnitude of the headline claims.

## 3. Industry Contribution

The central engineering claim is one shared-bottom multi-task backbone serving four horizon-specific LTV heads (30/90/180/365-day) instead of training and maintaining four separate models — directly reducing training and serving surface area at billion-user scale. The gradient-truncation (stop_gradient) mechanism between upstream and downstream Mono Units is a concrete, reusable pattern for any multi-horizon head sharing a backbone: it lets an easy short-horizon task assist a hard long-horizon task without the noisier downstream task destabilizing the upstream one. The paper states the model is fully deployed with day-level training and prediction over the full user volume, with predictions cached for real-time serving — an unusually concrete production detail among this batch's academic-leaning papers. The authors also make a deliberate feature-engineering choice to exclude highly personalized identifiers (user_id, item_id) to preserve model generalization, a directly statable, reusable engineering decision.

## 4. Novelty vs. Prior Work

The claimed novelty is being the first system to jointly model ordered dependencies across multi-horizon LTV tasks via a monotonic network, and to attack the imbalanced/long-tailed LTV distribution via a divide-and-conquer bucket-classification module, in one industrial system — plus introducing Mutual Gini as a new distribution-fit evaluation metric. Prior work discussed: **Wang, Liu & Miao, "A deep probabilistic model for customer lifetime value prediction," arXiv:1912.07753, 2019** — the ZILN paper (also in this batch), used directly as the strongest prior baseline and as the source of the Lorenz-curve/Gini methodology this paper's Mutual Gini extends. **Drachen et al., "To be or not to be... social: Incorporating simple social features in mobile game customer lifetime value predictions," ACSW 2018** — source of the Two-Stage (XGBoost) baseline. **Fader, Hardie & Lee, "RFM and CLV: Using iso-value curves for customer base analysis," Journal of Marketing Research 2005** — the classical RFM/BTYD baseline family. **Xing et al., "Learning Reliable User Representations from Volatile and Sparse Data to Accurately Predict Customer Lifetime Value," KDD 2021** — TSUR, a user-representation-learning approach explicitly excluded as a baseline on the grounds that it is complementary and could be integrated into ODMN's embedding encoder rather than compared against it. **Ma, Zhao, Yi, Chen, Hong & Chi, "Modeling task relationships in multi-task learning with multi-gate mixture-of-experts" (MMoE), KDD 2018** — cited as an alternative, extendable shared-bottom backbone. **Fu, Gong, Wang, Batmanghelich & Tao, "Deep ordinal regression network for monocular depth estimation," CVPR 2018** — source of the Ordinal Regression mechanism used in the DOT/BOT towers.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Kuaishou User Growth Dataset | Offline (180M new users sampled, from a platform of 320M DAU / 1B+ MAU) | No — proprietary, no public dataset exists for this domain | Features: user profile, channel-related information, first-7-day day-level behavior sequences; label = active days at 30/90/180/365-day horizons |
| Kuaishou user-growth advertising live traffic | Online (10% control / 10% experimental split; ROI accumulated over 7/14/30 days) | No — proprietary | ROI-based A/B test against a ZILN-based production baseline |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou," Kunpeng Li, Guangcui Shao, Naijun Yang, Xiao Fang, Yang Song (Beijing Kuaishou Technology Co., Ltd.), CIKM 2022, https://doi.org/10.1145/3511808.3557152 |
| 2 | Source type | Industry paper (CIKM 2022) |
| 3 | Direction | D4 |
| 4 | Problem setting | Multi-horizon (30/90/180/365-day) LTV prediction at billion-user scale under an atypical "raised-tail" long-tailed distribution, where conventional multi-task learning ignores the natural ordered dependency between horizons and produces business-illogical predictions (e.g., predicted 30-day LTV exceeding predicted 90-day LTV) |
| 5 | Objective and label definition | Label is the number of active days the user contributes to the platform over four fixed future horizons — 30, 90, 180, and 365 days from registration — predicted jointly from the user's first-7-days behavior. **No survival/censoring correction is modeled** — the paper sidesteps censoring exactly as the ZILN paper does, by drawing from historical cohorts where all four windows have already fully elapsed by data-collection time |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. It frames the task as "predicting the value it will bring to the platform in the next N days," a direct regression/classification-cascade point estimate with no propensity, policy, or counterfactual component |
| 7 | Model architecture | Shared-bottom multi-task network with a per-horizon MDME module (Distribution Segmentation Module + Sub-Distribution Modeling Module — a coarse-to-fine multi-classification-plus-bias-regression cascade with ordinal-regression-guided distillation), with horizons connected via non-negative-weight "Mono Units" that propagate the upstream horizon's output distribution into the downstream horizon's logits, plus an explicit ordered-dependency calibration loss penalizing any case where a shorter-horizon prediction exceeds an adjacent longer-horizon prediction |
| 8 | Credit assignment | Not applicable in the item/slate sense — this is pointwise user-level LTV regression, not a ranking decision. The paper's real "assignment" problem is temporal: allocating learning signal across the 30/90/180/365-day horizon tasks via the Mono Unit and calibration loss, not mapping a user-level outcome to a candidate item |
| 9 | Training data and counterfactual handling | 180M users' first-7-day behavior sequences plus profile/channel features, with active-day labels observed over the fully-elapsed subsequent year. No counterfactual, inverse-propensity, or causal adjustment is applied — pure supervised regression on observed platform activity; selection effects from which acquisition channel brought which users are not addressed |
| 10 | Offline and online evaluation | Offline: NRMSE, NMAE, AMBE, normalized Gini, and the proposed Mutual Gini on the 180M-user dataset, with two dedicated ablation studies (MDME components, ODMN components). Online: a real production A/B test (10%/10% traffic split) on Kuaishou's user-growth ad-delivery platform, measuring cumulative ROI at 7/14/30 days against a ZILN-based production baseline |
| 11 | Reported gains | Offline, 30-day horizon on the 180M-user Kuaishou dataset: AMBE reduced 68.3% relative to ZILN (0.0423 vs. 0.1336) and Mutual Gini improved 44.7% relative to ZILN (0.0125 vs. 0.0226); gains grow substantially larger at longer horizons (365-day AMBE reduced 96.3% relative to ZILN). Online: ROI uplift of +11.9% (7-day), +12.8% (14-day), +14.7% (30-day) over the ZILN-based production baseline in a live Kuaishou A/B test |
| 12 | Applicability to a two-sided dating recommender | Single-sided (platform-to-user) LTV regression with no reciprocity, congestion, or match-fairness treatment. The ordered-dependency-across-horizons technique is directly reusable if the dating app's unified model predicts retention/revenue at multiple horizons simultaneously (e.g., 7-day and 30-day retention) and needs those predictions to remain internally, monotonically consistent |
| 13 | Unverified claims | The online ROI-uplift percentages are reported without confidence intervals or significance tests, and absolute ROI values are withheld "for company privacy," so the magnitude cannot be independently sanity-checked. The claim that TSUR was excluded as a baseline because it is "complementary" rather than competitive is asserted, not demonstrated by an actual combined experiment in this paper |

## Project Relevance

Directly and heavily on **Q3**: the multi-horizon label definition (30/90/180/365-day active days) together with the ordered-dependency-across-horizons technique is a strong, citable precedent for how the dating app's unified model could keep 7-day and 30-day retention/revenue predictions mutually consistent within one architecture. Also speaks to **Q4** (a single, per-horizon value head — no separate short-term CTR/CVR head is fused with it in this paper) and **Q1** (the training objective is engagement/monetary value directly, not a CTR-like proxy). Touches **Q6** with both a real offline ablation protocol and a genuine online A/B test against a strong production baseline.

Does **not** address **Q2** (no item/slate-level credit assignment — pointwise user regression), **Q5** (no incrementality or causal treatment — the paper's own framing is pure prediction), **Q7** (no two-sided, reciprocal, or congestion treatment — single-sided platform-to-user), or **Q8** (no staged-migration narrative from a prior production system; ZILN is used only as an offline/online evaluation baseline, not as a system ODMN incrementally replaces).

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `ODMN`._

## Meta Information

- **Authors:** Kunpeng Li, Guangcui Shao, Naijun Yang, Xiao Fang, Yang Song
- **Affiliations:** Beijing Kuaishou Technology Co., Ltd.
- **Venue:** CIKM 2022 (31st ACM International Conference on Information and Knowledge Management)
- **Year:** 2022
- **Relevance:** Core
- **Priority:** 1
- **nlm:80cf2edd-3189-41ee-8bb3-15129f84505a**
