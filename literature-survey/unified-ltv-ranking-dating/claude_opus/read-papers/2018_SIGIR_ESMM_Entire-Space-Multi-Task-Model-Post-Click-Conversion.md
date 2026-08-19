# Paper Analysis: Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Multi-task/2018 (Alibaba) (SIGIR) [ESMM] Entire Space Multi-Task Model - An Effective Approach for Estimating Post-Click Conversion Rate.pdf`
**Date analyzed:** 2026-08-16

## 1. Summary

Ma, Zhao, Huang, Wang, Hu, Zhu, and Gai (Alibaba) address two task-specific problems that make post-click conversion rate (CVR) prediction hard in practice: **sample selection bias (SSB)** — conventional CVR models are trained only on clicked impressions but must serve predictions over the entire impression space, so training and inference distributions diverge — and **data sparsity (DS)** — conversion events are 1-3 orders of magnitude rarer than clicks, starving the CVR model of training signal. The proposed **Entire Space Multi-task Model (ESMM)** solves both simultaneously by modeling the sequential user-action pattern *impression → click → conversion*. Rather than training pCVR directly on clicked samples, ESMM treats pCVR as an intermediate variable satisfying the chain rule p(y=1, z=1|x) = p(y=1|x) × p(z=1|y=1,x), i.e. pCTCVR = pCTR × pCVR. Two auxiliary tasks — post-view click-through rate (pCTR) and post-view click-through&conversion rate (pCTCVR) — are trained directly and only over the **entire space of all impressions**, and pCVR is recovered implicitly as the multiplicative factor, never given its own loss term. This avoids the numerically unstable "divide by a small pCTR" approach (DIVISION baseline). ESMM further shares the embedding (feature representation) layer between its CTR and CVR sub-networks, so the CVR tower benefits from the much richer click-level training signal (feature representation transfer), directly attacking DS. The architecture (Figure 2) is two parallel Embedding→field-wise-pooling→concatenate→MLP (360×200×80×2) towers (CVR network and CTR network) with a shared embedding lookup table; CTCVR is computed as the elementwise product of the CVR and CTR tower outputs.

Evaluated on traffic logs from Taobao's recommender system — a released 1% public sample (0.4M users, 4.3M items, 84M impressions, 3.4M clicks, 18K conversions) and the full proprietary product dataset (8.9 billion samples) — against BASE (direct CVR training on clicked samples), AMAN (negative sampling), OVERSAMPLING, UNBIAS (rejection sampling), DIVISION (separately-trained CTR/CTCVR networks divided post hoc), and ESMM-NS (ESMM without embedding sharing). ESMM achieves an absolute AUC gain of 2.56% (CVR task) and 3.25% (CTCVR task) over BASE on the public dataset, and 2.18% / 2.32% on the full product dataset, described by the authors as "significant" given that "0.1% AUC gain is remarkable" for this industrial application. This is a 4-page short paper with no online A/B test reported.

## 2. Experiment Critique

**Design.** Comparison against five baselines (BASE, AMAN, OVERSAMPLING, UNBIAS, DIVISION) plus one dedicated ablation (ESMM-NS, isolating the effect of embedding sharing) on two datasets — the released public 1% sample and the full 8.9B-sample product dataset — with an additional sweep across training-set sampling rates (1%, 20%, 40%, 100%) on the product dataset.

**Statistical validity.** All offline AUC results are reported as mean ± std over 10 repeated runs (Table 2), a relatively disciplined practice for a 4-page short paper. No explicit significance test (t-test, p-value) is reported despite the repeated-run variance being available.

**Online experiments.** None. This paper reports offline evaluation only.

**Reproducibility.** The public 1% sample (38GB, Taobao Tianchi dataId=408) was released by the authors specifically "to enable future research" — a genuinely reproducible artifact and, per the authors, the first public dataset with sequential click-and-conversion labels for CVR modeling. The 8.9B-sample product dataset is proprietary and not released. Loss function and architecture (Eq. 1-3, Figure 2) are specified in full mathematical detail; no code release is mentioned.

**Overall.** A disciplined ablation structure (isolating the entire-space principle via ESMM-NS from the embedding-sharing contribution) backed by repeated-run variance reporting, but weakened by the complete absence of any online validation and by no significance testing despite the reported standard deviations.

## 3. Industry Contribution

The BASE architecture is explicitly described as "the latest version which serves the main traffic in our real system," meaning ESMM's starting point is itself production-validated; ESMM extends it with only two additional output heads (CTR, CTCVR) that share the CVR network's embedding table, at essentially the cost of one extra multiplication at inference. The central engineering claim is eliminating the fragile heuristics of prior fixes — AMAN's negative-sampling rate search, UNBIAS's importance-weighted rejection sampling, DIVISION's numerically unstable divide-by-small-probability step — with a single principled multiplicative reformulation trained end-to-end. Engineering cost is minimal: one shared embedding lookup table, two small MLP towers, and a multiplication at inference; no additional feature engineering is needed beyond the fields BASE already used. Framed in recommender-engineering terms: latency is unaffected in any material way (a second small forward pass sharing embeddings with the first, though no explicit latency number is given); no new features are required; and pCVR can substitute directly wherever a CVR score already feeds a ranking or bidding pipeline (the paper cites OCPC — optimized cost-per-click — bidding as the motivating downstream consumer).

## 4. Novelty vs. Prior Work

ESMM's claimed novelty is being the first approach to jointly solve SSB and DS for CVR modeling via a single principle — entire-space training plus an implicit chain-rule pCVR (recovered by multiplication, never trained directly) plus embedding-sharing transfer learning — rather than the heuristic corrections used by prior work. Prior work discussed: **Zadrozny, "Learning and evaluating classifiers under sample selection bias," ICML 2004** — the formal statement of the SSB problem this paper targets. **Weiss & McCarthy (Weiss, G.M.), "Mining with rarity: a unifying framework," SIGKDD Explorations 2004** — source of the OVERSAMPLING baseline concept for rare positive classes. **Zhang, Zhou, Zhu, Deng, "Bid-aware gradient descent for unbiased learning with censored data in display advertising," KDD 2016** — source of the UNBIAS rejection-sampling baseline. **Lee, Orten, Dasdan, Li, "Estimating conversion rate in display advertising from past performance data," KDD 2012** — cited for OCPC bidding's dependence on accurate CVR. **Zhu, Li, Zhang, Zhang, Xiong, Wang, Gai, "Optimized cost per click in Taobao display advertising," KDD 2017** — cited as the industrial motivation for accurate CVR (used in bidding). **Cheng, Koc et al., "Wide & deep learning for recommender systems," DLRS 2016** — a cited reference for the Embedding&MLP-style architecture that BASE follows. **Zhou et al., "Deep interest network for click-through rate prediction," arXiv 2017** — cited as a recent deep CTR method, noted as substitutable for ESMM's sub-network without changing the entire-space framework.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Public Dataset (Taobao, 1% sample) | Offline | Yes — released by the authors on Alibaba Tianchi (dataId=408), ~38GB | 0.4M users, 4.3M items, 84M impressions, 3.4M clicks, 18K conversions; authors state this is the first public dataset with sequential click/conversion labels for CVR modeling |
| Product Dataset (Taobao, full traffic) | Offline | No — proprietary | 48M users, 23.5M items, 8.95B impressions, 324M clicks, 1.774M conversions |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate," Xiao Ma, Liqin Zhao, Guan Huang, Zhi Wang, Zelin Hu, Xiaoqiang Zhu, Kun Gai (Alibaba Inc.), SIGIR 2018 (Short Research Papers II), https://doi.org/10.1145/3209978.3210104 |
| 2 | Source type | Industry paper (SIGIR 2018) |
| 3 | Direction | D5 |
| 4 | Problem setting | Post-click CVR prediction for ranking/bidding in e-commerce recommendation, where conventional models suffer sample selection bias (trained on clicked impressions, served on all impressions) and data sparsity (conversions are 1-3 orders of magnitude rarer than clicks) |
| 5 | Objective and label definition | Two cross-entropy losses over ALL impressions: y (clicked, binary) and y&z (clicked AND converted, binary); pCVR itself is never given a direct loss. No time horizon is stated — click and conversion are treated as resolving within the same logged interaction/session. No delay or censoring handling is discussed |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. Entire-space modeling here corrects a **sample selection bias in a prediction task** (training/serving distribution mismatch for pCVR); it is not an estimate of the causal/incremental effect of showing the impression |
| 7 | Model architecture | Two parallel Embedding → field-wise pooling → concatenate → MLP (360×200×80×2) towers (CVR network, CTR network) with a shared embedding lookup table; CTCVR is the elementwise product of CVR-tower and CTR-tower outputs; loss is computed only on CTR and CTCVR, both over the entire impression space |
| 8 | Credit assignment | Single impression → single item (not slate-level). pCTR/pCVR/pCTCVR are computed per (user, item) impression-feature vector; the paper's real problem is a train/serve space mismatch, not attributing a delayed outcome across multiple candidate items |
| 9 | Training data and counterfactual handling | 8.9B (product) / 84M (public 1% sample) impressions with click and click-and-conversion binary labels, trained over the entire space with no counterfactual, propensity, or causal adjustment — pure supervised multi-task learning exploiting the chain-rule factorization |
| 10 | Offline and online evaluation | Offline only: AUC on CVR and CTCVR tasks, mean±std over 10 runs, on both the public 1% sample and the full 8.9B-sample product dataset across varying training sampling rates (1%/20%/40%/100%). No online A/B test reported |
| 11 | Reported gains | Absolute AUC gain over BASE of 2.56% (CVR task) and 3.25% (CTCVR task) on the public Taobao 1% sample dataset (ESMM 68.56±0.37 / 65.32±0.49 vs. BASE 66.00±0.37 / 62.07±0.45); absolute AUC gain of 2.18% (CVR) and 2.32% (CTCVR) over BASE on the full 8.9B-sample Taobao product dataset |
| 12 | Applicability to a two-sided dating recommender | The entire-space training principle — train auxiliary tasks over ALL impressions and recover the target via chain-rule multiplication — directly transfers to the dating cascade's twice-compounded selection bias (conversation observed only after match, match only after like). It offers no template for delayed multi-day retention/revenue labels or for a cascade beyond two steps, so it must be extended (e.g., via AITM, read in this same batch) before it covers the project's full impression→...→subscription chain |
| 13 | Unverified claims | Baseline tuning ("best results reported are searched" for AMAN/OVERSAMPLING/UNBIAS sampling rates) is not described as exhaustive; the conclusion that ESMM-NS's AUC gap over DIVISION "indicates its good generalization performance" is not backed by a significance test despite reporting std across 10 runs; the framing that this addresses "industrial applications" rests entirely on offline evaluation of the 8.9B-sample dataset, with no online deployment result reported in this paper |

## Project Relevance

Speaks directly and strongly to **Q2** (the chain-rule entire-space decomposition is precisely the credit-assignment/selection-bias-correction mechanism the project's twice-compounded selection problem — conversation-after-match-after-like — needs) and touches **Q1** (the training objective is optimized directly rather than left as an untouched proxy, though it remains a short-term click/conversion proxy, not retention or revenue). Also weakly informs **Q6** via its rigorous repeated-run offline evaluation protocol.

Does **not** address **Q3** (no delayed or multi-day horizon — click and conversion are treated as immediately resolvable), **Q4** (no fusion of a short-term head with a long-term head — only two short-term heads), **Q5** (pure prediction, no incrementality), **Q7** (no two-sided, reciprocal, or congestion treatment — single-sided e-commerce funnel), or **Q8** (no staged-migration narrative; ESMM is presented as a standalone architecture, not a step in a documented migration path).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Recommendation.md](./2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Recommendation.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2020_IJCAI_TS-DL_Attention-Model-CVR-Delayed-Feedback.md](./2020_IJCAI_TS-DL_Attention-Model-CVR-Delayed-Feedback.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2020_SIGIR_ESM2_Entire-Space-Multi-Task-Post-Click-Behavior-Decomposition.md](./2020_SIGIR_ESM2_Entire-Space-Multi-Task-Post-Click-Behavior-Decomposition.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR-Multi-task.md](./2020_WWW_MultiDR_Causal-Debiasing-Post-Click-CVR-Multi-task.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2021_AAAI_ESDF_Delayed-Feedback-Modeling-Entire-Space.md](./2021_AAAI_ESDF_Delayed-Feedback-Modeling-Entire-Space.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2021_KDD_AITM_Sequential-Dependence-Audience-Multi-step-Conversions.md](./2021_KDD_AITM_Sequential-Dependence-Audience-Multi-step-Conversions.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2021_SIGIR_HM3_Hierarchically-Modeling-Micro-Macro-Behaviors-Conversion.md](./2021_SIGIR_HM3_Hierarchically-Modeling-Micro-Macro-Behaviors-Conversion.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md](./2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Rate-Prediction.md](./2025_CIKM_MAL_Multi-Attribution-Learning-Conversion-Rate-Prediction.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2025_SIGIR_SORT-Gen_Generative-Re-ranking-List-level-Multi-objective.md](./2025_SIGIR_SORT-Gen_Generative-Re-ranking-List-level-Multi-objective.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |
| [2026_RecSys_FSM-MMoE-VST_Multi-Objective-Ranking-Live-Streaming.md](./2026_RecSys_FSM-MMoE-VST_Multi-Objective-Ranking-Live-Streaming.md) | Related Work / Experiments | Names this paper's method (`ESMM`) |

_11 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `ESMM` across all 133 cards._

## Meta Information

- **Authors:** Xiao Ma, Liqin Zhao, Guan Huang, Zhi Wang, Zelin Hu, Xiaoqiang Zhu, Kun Gai
- **Affiliations:** Alibaba Inc.
- **Venue:** SIGIR 2018 (41st ACM SIGIR Conference on Research and Development in Information Retrieval, Short Research Papers II)
- **Year:** 2018
- **Relevance:** Core
- **Priority:** 2
- **nlm:f9d15f60**
