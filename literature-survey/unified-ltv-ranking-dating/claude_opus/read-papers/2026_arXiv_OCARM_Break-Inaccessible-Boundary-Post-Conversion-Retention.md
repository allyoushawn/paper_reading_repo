# Paper Analysis: Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2604.25839.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling
**Authors:** Tianbao Ma, Ruochen Yang, Chengen Li, Yuexin Shi, Jiangxia Cao, Linxun Chen, Zhaojie Liu, Yanan Niu, Han Li, Kun Gai (Kuaishou Technology, Beijing, China)
**Venue/Year:** arXiv:2604.25839, 2026. Note: the PDF carries an ACM conference-template header ("Conference acronym 'XX, June 03–05, 2018, Woodstock, NY") that is a generic boilerplate placeholder, not a real accepted venue — treated here as an arXiv preprint.

**Abstract (paraphrased):** In real-time bidding (RTB) systems for user re-engagement, the retention model must predict future revisit probability at bidding time, before the user converts or consumes any content. Post-conversion content ("Onboarding Content" — what the user watches or does after opening the app) is highly informative for retention but is inaccessible at bidding time; using it directly in training causes severe feature leakage and a train/serve gap. The paper proposes OCARM, a two-stage distillation-aligned framework that lets the model implicitly capture future-content signal using only observable features at inference. Offline and online experiments show consistent improvements in a real growth scenario.

**Key contributions:**
- Names and formalizes the "inaccessibility boundary" at the conversion node in RTB retention prediction: everything left of conversion (profile, history, ad context) is observable at decision time; everything right of it (onboarding content and its interaction feedback) is not.
- Stage 1 (Onboarding Content Leakage Encoding): deliberately leaks the onboarding-content sequence into training, and trains a Hierarchical Attention Encoder (HAE) — intra-day cross-attention, then inter-day causal self-attention — to produce teacher representations jointly optimized against the actual LT1...LT_D retention labels.
- Stage 2 (User Representation Distillation Alignment): trains a Sequence Fusion Encoder (SFE), built on Q-Former-compressed behavior sequences plus per-horizon TaskTowers, to align to the frozen Stage-1 teacher via a stop-gradient cosine-similarity distillation loss, using only bidding-time-observable features.
- At inference, only SFE + the retention model run; the HAE teacher is discarded entirely, so no future/inaccessible information is required at serving time.

**Methodology:** Retention backbone is PPNET. Stage 1 loss is BCE against the real LT1...LT_D labels using the leaked-content-derived embedding concatenated with the retention model's own features. Stage 2 loss combines the retention BCE with an alignment loss (cosine-similarity, stop-gradient on the teacher side to prevent representation collapse) between the student (SFE) and frozen teacher (HAE) representations, per task/horizon.

**Main results:** Table 1 — full OCARM improves AUC over the "Base" (no augmentation) PPNET model from 0.7297→0.7369 (LT1) and 0.6903→0.6949 (LT7), approaching but not reaching the Stage-1 "upper bound" (0.7468/0.7002) that requires actual leaked content. Stage-2-only training (no frozen teacher) degrades below Base. Online A/B test on Kuaishou's RTB system (Table 3): Re-engaged Devices +20.468% (non-uninstalled users) / +34.430% (uninstalled users); LT30 retention +11.548% / +22.179%.

## 2. Experiment Critique

**Design:** Purely internal ablation — no third-party academic baselines are run (not even the decision-transformer retention models the paper itself cites in related work). The Stage-1 "upper bound" comparison is a real internal-validity strength, establishing the achievable ceiling if leakage were allowed, and the encoder-architecture ablation (Table 2) combined with the representation-similarity-vs-gain correlation (Figure 3) build a reasonably careful mechanistic case that distillation quality — not just added parameters — drives the improvement.

**Statistical validity:** No confidence intervals, standard deviations, or significance tests are reported for any AUC/GAUC number (Tables 1, 2) or for the online A/B percentages (Table 3). Dataset size is given only qualitatively ("millions of users and billions of interaction records"); A/B duration is given only as "multiple days," with no arm sizes or traffic percentage stated.

**Online experiments:** Yes — a real production A/B test on Kuaishou's RTB system (Table 3), a genuine strength for an industry paper, though thin on methodological detail (no randomization-unit description, no arm sizes, no significance testing).

**Reproducibility:** Proprietary Kuaishou dataset, not released; no code released. Key hyperparameters (alignment-loss weight λ, number of Q-Former query tokens, HAE dimensionality, number of days D in the onboarding sequence) are not given numerically in the source text. Not independently reproducible.

## 3. Industry Contribution

**Deployability:** Deployed and A/B tested in Kuaishou's production RTB system, with a deliberately lightweight inference-time architecture — only the student (SFE) and retention model run at serving time, since the heavyweight HAE teacher is discarded after training — avoiding new latency or feature dependencies on the bidding critical path.

**Problems solved:** Addresses a general and recurring recsys-engineering problem — training/serving skew from using post-decision information as a naive input feature ("feature leakage" of information that literally does not exist at serving time). The teacher-on-privileged-information / distilled-student-at-serving-time pattern is architecture-agnostic in principle (demonstrated here on top of PPNET) and broadly reusable beyond notifications or short video.

**Engineering cost:** Two full training stages (frozen teacher + student alignment), a Q-Former-based sequence compressor, and per-horizon TaskTowers — meaningfully more complex than the single-stage PPNET baseline, though the added cost is confined to offline/training compute since inference only runs the lighter Stage-2 path. In recsys terms this is a "privileged information at training time" pattern applied to the retention-scoring stage of an ad-bidding pipeline, requiring no change to serving-time feature engineering or latency budget.

## 4. Novelty vs. Prior Work

The paper frames prior work as incorporating post-conversion content directly "as the vehicle for observational inputs or reward features in retention prediction" without addressing the resulting train/serve leakage; OCARM's stated contribution is the two-stage distillation-with-stop-gradient design that lets a model benefit from that signal's information without requiring the signal at inference. It cites but does not benchmark against decision-transformer-based retention models (Liu et al., "Modeling user retention through generative flow networks," KDD 2024; Zhao et al., "User retention-oriented recommendation with decision transformer," WWW 2023) and a "Foresight Prediction Enhanced Live-Streaming Recommendation" paper from an overlapping author group (Cao et al., WSDM 2026) whose precise relationship to OCARM is not clarified in the source text.

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| Kuaishou industrial RTB/retention dataset | No — proprietary/internal | Millions of users, billions of interaction records | Not released; no public benchmark used; internal-only baselines |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Value |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling," Tianbao Ma, Ruochen Yang, Chengen Li, Yuexin Shi, Jiangxia Cao, Linxun Chen, Zhaojie Liu, Yanan Niu, Han Li, Kun Gai (Kuaishou Technology), arXiv:2604.25839, 2026. URL: https://arxiv.org/abs/2604.25839 |
| 2 | Source type | Industry paper (arXiv preprint, Kuaishou Technology) |
| 3 | Direction | D4 |
| 4 | Problem setting | Retention prediction in a real-time-bidding (RTB) ad system for user re-engagement, where the bid decision must be made before conversion and before any post-conversion in-app content is observed, while that content is highly predictive of retention — a structural feature-leakage risk if used naively in training. |
| 5 | Objective and label definition | Multi-horizon revisit-frequency labels LT1...LT_D (reported: LT1, LT7 — 1-day and 7-day post-conversion revisit), predicted as p(y\|x_u) using only bidding-time-observable user features at serving time. No explicit censoring/survival treatment is described for incomplete observation windows. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. It predicts revisit probability conditional on observable features and does not estimate the causal effect of the bid/ad-delivery decision on retention. |
| 7 | Model architecture | Two-stage distillation framework (OCARM). Stage 1: Hierarchical Attention Encoder (HAE) — per-day cross-attention over leaked onboarding-content items, then causal self-attention across days — trained jointly with a PPNET-based retention head as teacher. Stage 2: Sequence Fusion Encoder (SFE) — Q-Former-compressed behavior/ad-context sequences plus per-horizon TaskTowers — aligned to the frozen Stage-1 teacher (cosine-similarity, stop-gradient) while jointly optimizing retention BCE. Only SFE + retention model run at inference. |
| 8 | Credit assignment | The delayed, user-level revisit outcome is attributed to a single bidding-time decision point (the ad-delivery/bid opportunity at conversion); the distillation objective is itself the mechanism letting pre-conversion, decision-time features carry credit for signal that does not exist until after conversion. |
| 9 | Training data and counterfactual handling | Proprietary Kuaishou industrial dataset (millions of users, billions of interaction records); no counterfactual/causal-inference machinery — training uses deliberately leaked post-conversion content as a training-only teacher signal (explicit, acknowledged leakage used by design, then removed at inference to prevent train/serve skew). |
| 10 | Offline and online evaluation | Offline: AUC/GAUC on LT1/LT7 for Base vs. Stage-1-only (upper bound) vs. Stage-2-only vs. full OCARM (Table 1), an encoder-architecture ablation (Table 2), and a representation-similarity-to-gain correlation analysis (Figure 3). Online: production A/B test on Kuaishou's RTB system over multiple days (Table 3), split by non-uninstalled vs. uninstalled users. |
| 11 | Reported gains | Internal Kuaishou dataset: full OCARM improves AUC over the Base PPNET model from 0.7297→0.7369 (LT1) and 0.6903→0.6949 (LT7) (Table 1). Online A/B (Table 3): Re-engaged Devices +20.468% (non-uninstalled) / +34.430% (uninstalled); LT30 retention +11.548% (non-uninstalled) / +22.179% (uninstalled). |
| 12 | Applicability to a two-sided dating recommender | Directly transferable to the project's post-match blackout: distill a teacher representation from the (normally inaccessible) private post-match conversation during training, then discard the teacher and serve only a student encoder trained on pre-match/observable features, avoiding the same train/serve leakage the platform would otherwise face. The stop-gradient two-stage recipe — and its documented failure mode when skipped — is a concrete, reusable design template. The paper's setting is single-sided (one user's revisit), with no reciprocity or congestion to model. |
| 13 | Unverified claims | The PDF's venue header is a generic ACM template artifact, not a real venue — treated as unconfirmed publication venue. No confidence intervals or significance tests are given for any reported AUC/GAUC or A/B percentage. The relationship between this paper and the same authors' "Foresight Prediction Enhanced Live-Streaming Recommendation" is not clarified in-text. Hyperparameters (λ, Q-Former query count, sequence length D) are not disclosed. |

## Project Relevance

Most directly answers **Q2** (attribution of a delayed, inaccessible outcome to a single upstream decision) and touches **Q3** (multi-horizon LT1/LT7 label definition) and **Q8** (a concrete migration/engineering pattern: train with privileged future signal via distillation, serve without it). This is the batch's most structurally relevant paper to the dating-app setting: the platform's own post-match conversation is the direct analogue of this paper's "onboarding content" — content the system cannot observe but that drives the delayed retention outcome it must still predict from what it *can* observe at ranking time. The two-stage leak-then-distill recipe, and its explicit failure mode when the stop-gradient/frozen-teacher design is skipped (Table 1, "w/ Stage 2" alone underperforms Base), is a reusable design lesson worth carrying into the executive summary's migration-path section. Per field 6, this remains a pure prediction paper — no incrementality/causal-effect estimation is present, so it does not answer Q5.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `OCARM`._

## Meta Information

- **Authors:** Tianbao Ma, Ruochen Yang, Chengen Li, Yuexin Shi, Jiangxia Cao, Linxun Chen, Zhaojie Liu, Yanan Niu, Han Li, Kun Gai
- **Affiliations:** Kuaishou Technology, Beijing, China
- **Venue:** arXiv preprint (PDF header carries an unrelated ACM template placeholder, not a confirmed conference venue)
- **Year:** 2026
- **Relevance:** Core
- **Priority:** 2
- **nlm:dc23ab85**
