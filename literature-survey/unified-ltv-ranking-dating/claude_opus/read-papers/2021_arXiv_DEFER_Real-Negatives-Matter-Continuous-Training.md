# Paper Analysis: Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling

**Source:** /Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2021 (Alibaba) (Arxiv) [Defer] Real Negatives Matter - Continuous Training with Real Negatives for Delayed Feedback Modeling.pdf
**Date analyzed:** 2026-08-17

**Venue note:** The PDF header is an arXiv preprint (arXiv:2104.14121v1, submitted 29 Apr 2021). The document body uses ACM's generic "Woodstock '18, June 03–05, 2018" placeholder conference boilerplate — a known LaTeX-template artifact, not a genuine venue name — so the PDF itself does not state a confirmed conference/journal venue beyond "arXiv preprint."

## 1. Summary

**Title:** Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling
**Authors:** Siyu Gu, Xiang-Rong Sheng, Ying Fan, Guorui Zhou, Xiaoqiang Zhu (Alibaba Group)

**Abstract (paraphrase):** Continuous CVR training must balance freshness (ingesting fresh data quickly) against label certainty (waiting for the true conversion signal). Prior methods duplicate fake negatives with a positive label once conversion happens, but this changes the observed feature distribution relative to the actual distribution, and label certainty only ever comes from the scarce positive class. The paper proposes DElayed FEedback modeling with Real negatives (DEFER), which additionally ingests duplicated *real* negatives into the training pipeline, so that after duplication the observed feature distribution equals the actual distribution by construction, reducing bias and adding more label certainty. Importance sampling corrects the remaining distribution shift.

**Key contribution:** Identifies that prior delayed-feedback methods duplicate only fake negatives that later become positive, which itself distorts the observed feature distribution q(x) away from the true distribution p(x); proposes duplicating real negatives (samples confirmed not to convert within an attribution window) as well, restoring q(x) = p(x) by construction, and derives the corresponding importance-weighted loss (Eq. 12–13). Also proposes loss-function variants that let real-negative duplication augment FNW/FNC, and an offline multi-task variant for platforms that cannot support continuous training.

**Methodology:** Defines a waiting window w1 and an attribution window w2 (w2 > w1). A click is a **positive** if conversion occurs within w1; a **fake negative** if conversion occurs later but still within w2; a **real negative** if no conversion occurs by w2. DEFER duplicates and ingests both positives (once resolved) and real negatives (once w2 has passed) with correct labels; because both duplication types feed back into the pipeline, the resulting observed distribution matches the true feature distribution, and an importance-sampling loss (Eq. 11–13) corrects for the residual effect of duplicated real negatives. For long attribution windows, the real negative is approximated using a shorter window w3 (w1 < w3 < w2) to bound data-cache cost. An offline multi-task variant (Fig. 3) trains N+1 shared-bottom heads predicting p(z<w_n, y=1|x) for a discretized set of windows w1...wN, for platforms using batch/offline rather than continuous training.

**Main results:** On Criteo and a private "Taobao-30days" industrial dataset, DEFER outperforms Vanilla (with/without duplication or windowing), FNC, FNC-RN, FNW, FNW-RN and ES-DFM on AUC, PR-AUC and NLL (except a narrowly lower PR-AUC than FNW-RN on Taobao-30days), and closes the largest share of the gap to an Oracle model (RI-AUC 90.11% on Criteo). Two production A/B deployments are reported: an "Adding To Cart" scenario (1-day attribution window, continuous training) shows 8.5% CVR improvement over the pre-trained model; a "Purchase" scenario (7-day attribution window, offline multi-task training) shows 6% CVR improvement over the vanilla baseline.

## 2. Experiment Critique

- **Design:** Streaming/continuous-training simulation on Criteo and Taobao-30days, with hourly evaluation windows following industrial online-training conventions; a dedicated window-length sensitivity study (Fig. 4, z3 ∈ {1,3,5,7,9} days) probes how much the real-negative-duplication window can be shortened without hurting performance.
- **Statistical validity:** Table 2 reports point-estimate metrics (AUC, PR-AUC, NLL, and relative-to-oracle RI variants) without confidence intervals or significance tests, unlike the companion ES-DFM paper which reports t-test significance markers.
- **Online experiments:** Two separate production A/B deployments are described (different attribution windows, different training paradigms — continuous vs. offline), which is a stronger real-world validation than a single test, though neither reports sample size, duration precision, or confidence interval.
- **Reproducibility:** Code and data are stated to be open-sourced ("The code and data in this paper are now open-sourced," with a GitHub link on the title page) for at least part of the experiments.

## 3. Industry Contribution

- **Deployability:** Directly targets two realistic production regimes — continuous training with short attribution windows (1 day) and offline/batch training with long attribution windows (7 days) — and gives a concrete data-pipeline recipe (Fig. 1b: duplicate positives and real negatives) plus a shortened approximation window w3 to control infrastructure/cache cost for long windows.
- **Problems solved:** Removes the feature-distribution bias introduced by duplicating only fake negatives; increases label certainty in a data regime where positives are inherently scarce, by adding cheap, plentiful, certain real-negative signal.
- **Engineering cost:** Requires maintaining a data cache long enough to identify and duplicate real negatives (mitigated by the shortened w3 approximation for long attribution windows); requires per-sample fake-negative-probability estimation (f_dp classifier) for the importance-weighted loss.

## 4. Novelty vs. Prior Work

- **vs. FNW/FNC (Ktena et al., RecSys 2019):** FNW/FNC duplicate only fake negatives that later convert; DEFER additionally duplicates real negatives, and the paper shows FNW-RN/FNC-RN (FNW/FNC augmented with real-negative duplication) already improve over vanilla FNW/FNC, isolating real-negative duplication as the source of the gain.
- **vs. ES-DFM (Yang et al., AAAI 2021 — companion paper in this batch):** ES-DFM corrects observed-vs-true distribution bias purely through estimated importance weights without duplicating real negatives; DEFER instead changes the data pipeline itself (duplication) to make q(x) = p(x) by construction, then uses importance sampling only for the residual shift.
- **vs. DFM (Chapelle 2014):** DFM treats un-converted samples as unlabeled/negative without any duplication-based correction; DEFER explicitly reasons about which un-converted samples are "real" (permanently) negative versus still pending.

## 5. Dataset Availability

| Dataset | Type | Access | Size |
|---|---|---|---|
| Criteo conversion-log dataset | Public | https://labs.criteo.com/2013/12/conversion-logs-dataset/ | >15 million samples, 60-day period |
| Taobao-30days | Private, industrial (Alibaba) | Not released | ~120 million samples (20% of negatives, 1% of users sub-sampled), 30-day period, 2M users, 6.5M items |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling," Siyu Gu, Xiang-Rong Sheng, Ying Fan, Guorui Zhou, Xiaoqiang Zhu; Alibaba Group; arXiv:2104.14121, 2021; https://github.com/gusuperstar/defer.git |
| 2 | Source type | Academic preprint, industry-authored (Alibaba Group) |
| 3 | Direction | D7 |
| 4 | Problem setting | Continuous/streaming CVR prediction under delayed feedback, where prior fake-negative-duplication methods bias the observed feature distribution and label certainty comes only from scarce positives. |
| 5 | Objective and label definition | Binary CVR prediction. A sample is positive if conversion occurs within waiting window w1; a real negative once the attribution window w2 has passed without conversion; a fake negative in between. Horizon: business-set attribution windows of **1 day** (continuous-training deployment, "Adding To Cart") or **7 days** (offline multi-task deployment, "Purchase"); the waiting window w1 = 0.25 hour (15 minutes) in the offline experiments, following ES-DFM's setting. Delay is handled by hard right-censoring at the attribution window (anything unconverted past w2 is treated as a real negative) combined with importance sampling to correct the residual distributional effect of duplication. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Deep MLP (embeddings → fully-connected layers, hidden [256, 256, 128], Leaky ReLU, BatchNorm, Adam optimizer). For offline/batch platforms, a multi-task shared-bottom variant with N+1 heads, one per discretized attribution-window threshold plus a final p(y=1\|x) head. |
| 8 | Credit assignment | Not specified in source. Operates at single click → single conversion-label granularity; no multi-item slate or ranked-list credit assignment is addressed. |
| 9 | Training data and counterfactual handling | Public Criteo dataset and a private Taobao-30days industrial dataset (sub-sampled real traffic). No counterfactual or causal estimation — purely observational label-bias correction for a prediction target, via a redesigned data pipeline plus importance sampling. |
| 10 | Offline and online evaluation | Offline: AUC, PR-AUC, NLL, and relative-to-oracle metrics (RI-AUC, RI-PR-AUC, RI-NLL) on Criteo and Taobao-30days; a dedicated sensitivity study of the real-negative approximation window length. Online: two separate production A/B deployments in Alibaba's display advertising system (1-day attribution / continuous training scenario; 7-day attribution / offline multi-task scenario), reporting CVR as the online metric. |
| 11 | Reported gains | Offline (Criteo): DEFER achieves RI-AUC 90.11%, RI-PR-AUC 88.25%, RI-NLL 96.61% (share of the Oracle-minus-Pretrained gap closed); "the proposed method almost consistently outperforms other approaches on all performance metrics" except a narrowly lower PR-AUC than FNW-RN on Taobao-30days (DEFER 88.00% RI-PR-AUC vs. FNW-RN 89.70%). Online: "8.5% improvement on CVR" for the Adding-To-Cart / 1-day-attribution continuous-training deployment vs. the pre-trained model; "6% [improvement]... on CVR" for the Purchase / 7-day-attribution offline-training deployment vs. the vanilla baseline. |
| 12 | Applicability to a two-sided dating recommender | The real-negative-duplication recipe and its 7-day attribution-window deployment are the closest match in this batch to the project's delay scale, and the underlying idea (treat un-converted samples past a horizon as certain negatives, then correct via importance sampling) is directly reusable for a 30-day retention censoring rule. It remains a single binary-event label-bias correction, however — no retention/revenue objective, no incrementality, and no reciprocal-market mechanism. |
| 13 | Unverified claims | The claim that real-negative duplication "ensures the observed feature distribution equals the actual distribution" is a construction-level (definitional) claim, not separately, directly measured (e.g., no reported divergence metric between q(x) and p(x)); it is validated only indirectly through downstream AUC/PR-AUC/NLL gains — flagged as an assumption verified indirectly rather than measured directly. |

## Project Relevance

Speaks most directly to **Q3** (label/horizon definition and censoring: this paper's attribution-window-as-hard-censoring-boundary, reaching all the way to 7 days in production, is the paper in this batch structurally closest to the project's own 7–30 day retention censoring problem) and to **Q1** only weakly (the objective is still a short-term binary CVR label, not retention/revenue). Touches **Q6** (dual offline/online evaluation design) but not with any two-sided-market complication. Does **not** address Q2 (item/slate credit assignment), Q4 (short/long-term head fusion), Q5 (incrementality — explicitly out of scope), Q7 (reciprocity, congestion, fairness), or Q8 (migration path to a unified retention/revenue model).

The 1-day and 7-day attribution windows demonstrated here are still an order of magnitude short of the project's 30-day retention horizon and weeks-scale revenue horizon, but the mechanism — treat "no conversion within the attribution window" as a confirmed negative and duplicate it into training, then importance-weight for the resulting distribution shift — is the most directly transferable censoring pattern in this batch to the project's 30-day retention definition.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2019_RecSys_FNW-FNC_Addressing-Delayed-Feedback-Continuous-Training.md](./2019_RecSys_FNW-FNC_Addressing-Delayed-Feedback-Continuous-Training.md) | Related Work / Experiments | Names this paper's method (`DEFER`) |
| [2020_AdKDD_NBDFM_Negative-Binomial-Regression-Multiple-Conversions.md](./2020_AdKDD_NBDFM_Negative-Binomial-Regression-Multiple-Conversions.md) | Related Work / Experiments | Names this paper's method (`DEFER`) |
| [2022_WWW_DEFUSE_Asymptotically-Unbiased-Estimation-Label-Correction.md](./2022_WWW_DEFUSE_Asymptotically-Unbiased-Estimation-Label-Correction.md) | Related Work / Experiments | Names this paper's method (`DEFER`) |
| [2026_SIGIR_CM-DCM_Counterfactual-Multi-task-Learning-Delayed-Conversion.md](./2026_SIGIR_CM-DCM_Counterfactual-Multi-task-Learning-Delayed-Conversion.md) | Related Work / Experiments | Names this paper's method (`DEFER`) |

_4 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `DEFER` across all 133 cards._

## Meta Information

- **Authors:** Siyu Gu, Xiang-Rong Sheng, Ying Fan, Guorui Zhou, Xiaoqiang Zhu
- **Affiliations:** Alibaba Group, Beijing, China
- **Venue:** arXiv preprint (arXiv:2104.14121v1); PDF body uses placeholder ACM "Woodstock '18" conference text, not a confirmed publication venue
- **Year:** 2021
- **Relevance:** Core
- **Priority:** 2
- nlm:37991319
