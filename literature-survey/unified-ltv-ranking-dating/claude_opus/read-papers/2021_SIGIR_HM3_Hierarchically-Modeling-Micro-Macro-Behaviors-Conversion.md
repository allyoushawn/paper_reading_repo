# Paper Analysis: Hierarchically Modeling Micro and Macro Behaviors via Multi-Task Learning for Conversion Rate Prediction

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Multi-task/2021 (Alibaba) (SIGIR) [HM3] Hierarchically Modeling Micro and Macro Behaviors via Multi-Task Learning for Conversion Rate Prediction.pdf`
**Date analyzed:** 2026-08-16

## 1. Summary

Wen, Zhang, Lv, Bao, Wang, and Chen (Alibaba Group / University of Sydney) extend their own prior work, ESM², by observing that macro behaviors alone (cart-add, wishlist, as modeled in ESM²) miss a finer tier of **micro behaviors** — item-detail-page interactions such as clicking item pictures, checking Q&A, chatting with sellers, reading comments, or clicking the cart-control button — that are far more abundant than macro behaviors (Figure 1a shows micro-behavior edge frequencies up to 26.38%, versus macro-conversion rates around 9.78–17.81%) and provide finer-grained supplementary supervision the macro-only graph ignores. The proposed **HM³** model hierarchically inserts *both* a micro-behavior node and a macro-behavior node between click and purchase: each is split into a **Deterministic set** (D-Mi/D-Ma — behaviors with clear purchase-relevance and abundant labels; D-Mi = clicking pictures/Q&A/chat/comments/cart-control-button, D-Ma = adding to cart or wishlist) and an **Other set** (O-Mi/O-Ma — everything else), producing the graph "impression→click→D(O)-Mi→D(O)-Ma→purchase," with micro nested *before* macro in the path. A shared Feature Embedding Module (FEM) feeds six parallel sub-networks predicting six hidden probability variables (y1...y6) corresponding to the graph's six explicit sub-paths (impression→click, click→D-Mi, D-Mi→D-Ma, D-Ma→purchase, O-Mi→D-Ma, O-Ma→purchase), which are combined via the conditional-probability rule into four auxiliary targets — CTR, D-Mi rate, D-Ma rate, and CTCVR (= CTR × CVR) — each trained with its own cross-entropy loss over the entire impression space.

Evaluated on three proprietary Alibaba "Shopping Recommendation" (SR) offline datasets of increasing scale — SR-S (32M users, 4.9B impressions), SR-M (68M users, 14.8B impressions), SR-L (107M users, 31.7B impressions) — against BASE (single-task), ESMM, ESM², GMCM (a prior micro-behavior-only GCN model), ESM²+Mi (ESM² naively extended with micro behaviors), and HM³−R (HM³ with micro/macro order reversed, an ablation). On SR-L, HM³ achieves the best CVR AUC (0.85726) and CTCVR AUC among all methods, beating BASE by +0.00794 and beating its nearest ablation HM³−R by a smaller margin, confirming that the specific micro-before-macro ordering matters. A genuine two-week online A/B test (2020-10-08 to 2020-10-21) on Alibaba's SR module shows HM³ delivering +8.27% CVR gain and +8.32% GMV (Gross Merchandise Volume) gain over BASE — the largest online margin reported across the ESMM→ESM²→HM³ lineage (ESMM: +2.76%/+3.02%).

## 2. Experiment Critique

**Design.** Three datasets of increasing volume (SR-S/M/L) evaluated against six comparison methods (BASE, ESMM, ESM², GMCM, ESM²+Mi, HM³−R), including two dedicated ablations that isolate the paper's two specific claims: ESM²+Mi isolates "does naively adding micro behaviors help," and HM³−R isolates "does the specific micro-before-macro hierarchy order matter."

**Statistical validity.** Offline AUC values (Tables 3-4) are reported as single point estimates per method per dataset size, with no mean±std, no repeated-run variance, and no significance test — a notably lower statistical bar than ESMM's own 10-run mean±std protocol in this same author lineage, and similar to ESM²'s single-point-estimate practice. The reported HM³ vs. HM³−R gains are numerically small (on the order of 0.0006–0.0027 AUC across the three datasets), and without variance reporting the precision of these differences cannot be independently assessed. The online test reports CVR/GMV gain as single point percentages with no confidence interval or significance test, over one two-week window.

**Online experiments.** A real production A/B test on Alibaba's SR module over a full two-week period (2020-10-08 to 2020-10-21) — a genuine, sustained online deployment, consistent in direction with, and larger in magnitude than, the online results reported for ESMM and ESM² elsewhere in this lineage.

**Reproducibility.** All three datasets (SR-S/M/L) and the online test are fully proprietary Alibaba traffic; the authors state explicitly, in a footnote, that "there are no available large-scale public datasets containing both micro and macro behaviors to benchmark our method," and none is released here. Architecture and the six-way conditional-probability decomposition (Eq. 1-4) are specified in full mathematical detail; no code release is mentioned.

**Overall.** A well-targeted ablation design (isolating "adding micro" and "ordering micro before macro" as two separate claims) backed by a genuine two-week online deployment with the largest margin in this lineage, but weakened — as with ESM² — by the complete absence of offline variance or significance reporting, which matters more here given how numerically small some of the claimed AUC gains are.

## 3. Industry Contribution

HM³ is explicitly framed as lightweight relative to its added complexity: the Feature Embedding Module (shared across all six sub-networks) "makes up the majority of the parameters," while combining the six probability variables into final CVR/auxiliary targets requires no extra learned parameters (a parameter-free composition network, the same pattern used in ESM²'s SCM), so the paper states the model "is well suited for online deployment and responding to users' requests in a low latency." The stated engineering payoff is deepening ESM²'s data-sparsity mitigation: by injecting even-more-abundant micro-behavior labels (some micro-behavior edges exceed 26% frequency, versus macro-conversion edges around 10-18%) as additional supervisory signal, HM³ lets "abundant supervisory signals from micro behaviors... better supervise the learning towards the final purchase target." Engineering cost roughly doubles the number of parallel sub-networks relative to ESM² (six vs. four), but the dominant embedding-module parameter cost keeps total serving overhead growth modest. Framed in recommender-engineering terms: latency inherits ESM²'s low-latency, parameter-free composition pattern (no additional stated online cost beyond the extra towers); feature engineering extends only with micro-behavior interaction logs already generated on the item-detail page (picture clicks, Q&A views, chat, comments, cart-control clicks), which the paper notes are lower-friction to log than deliberate macro actions like adding to cart; and the ranking-pipeline substitution mirrors ESMM/ESM²'s drop-in CVR-score replacement pattern, validated online with the largest GMV lift (+8.32%) reported across the three-paper Alibaba lineage in this batch.

## 4. Novelty vs. Prior Work

HM³'s claimed novelty is being the first to jointly and explicitly model *both* micro and macro post-click behaviors within one unified entire-space multi-task framework. The authors state the gap directly: "How to explicitly model both micro and macro behaviors in a unified framework for CVR prediction still remains unexplored" — positioning HM³ as the union of two previously separate lines of prior work. Prior work discussed: **Ma, Zhao, Huang, Wang, Hu, Zhu, Gai, "Entire space multi-task model" (ESMM), SIGIR 2018** — cited as the entire-space training foundation this paper builds on. **Wen, Zhang, Wang, Lv, Bao, Lin, Yang, "Entire space multi-task modeling via post-click behavior decomposition" (ESM²), SIGIR 2020** — the direct macro-behavior predecessor HM³ extends by adding the micro tier; used as both a baseline and the architectural template HM³'s SCM/DPM-style composition follows. **Bao, Wen, Guo, Zhao, Zhu, Liu, Ou, "GMCM: Graph-based micro-behavior model for post-click conversion rate estimation," SIGIR 2020** — the prior work that modeled micro behaviors alone via graph convolutional networks, explicitly critiqued by HM³'s introduction: it "ignores the macro behaviors, which have been demonstrated their value" (by ESM²) — the specific gap HM³'s introduction identifies and fills. **Zhou, Ding, Tang, Yan, Zhang, Huang, "Micro behaviors: A new perspective in e-commerce recommender systems," WSDM 2018** — cited as the first work to use micro-behaviors in e-commerce recommendation. **Gu, Ding, Zhang, Yin, "Hierarchical User Profiling for E-commerce Recommender Systems," WSDM 2020** — cited for a hierarchical profiling framework combining both macro and fine-grained micro signals. **Feng, Lv, Shen, Wan, Fu, Zhu, Yang, "Deep Session Interest Network for Click-Through Rate Prediction," arXiv 2019** — cited as related sequential CTR-modeling context.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| SR-S (Alibaba Shopping Recommendation, small) | Offline | No — proprietary | 32M users, 50M items, 4.9B impressions, 146M clicks, 36M D-Mi, 19M D-Ma, 5M purchases; collected 2020-09-29 |
| SR-M | Offline | No — proprietary | 68M users, 76M items, 14.8B impressions, 434M clicks, 102M D-Mi, 58M D-Ma, 16M purchases; collected 2020-09-23 to 2020-09-29 |
| SR-L | Offline | No — proprietary | 107M users, 84M items, 31.7B impressions, 925M clicks, 235M D-Mi, 122M D-Ma, 32M purchases; collected 2020-09-16 to 2020-09-29 (largest window, last day held out as test) |
| Alibaba SR module live traffic | Online (A/B test) | No — proprietary | Two-week window, 2020-10-08 to 2020-10-21; reports CVR gain and GMV gain of BASE/ESMM/HM³ |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Hierarchically Modeling Micro and Macro Behaviors via Multi-Task Learning for Conversion Rate Prediction," Hong Wen, Jing Zhang, Fuyu Lv, Wentian Bao, Tianyi Wang, Zulong Chen (Alibaba Group; University of Sydney), SIGIR 2021 (Short Research Paper III), https://doi.org/10.1145/3404835.3463053 |
| 2 | Source type | Industry paper (SIGIR 2021) |
| 3 | Direction | D5 |
| 4 | Problem setting | Post-click CVR prediction where modeling only macro behaviors (as in ESM²) leaves out abundant, finer-grained micro-behavior signal (item-detail-page interactions) that could further mitigate sample selection bias and data sparsity for the sparse purchase task, requiring a unified framework that models both behavioral tiers hierarchically in a single entire-space graph |
| 5 | Objective and label definition | Four cross-entropy losses (CTR, D-Mi rate, D-Ma rate, CTCVR), all computed over the entire impression space, following the same immediate/session-scoped label convention as ESMM/ESM²: click, micro-behavior (item-detail-page interaction), macro-behavior (cart/wishlist), and purchase, all observed within the same session. No multi-day horizon is stated; no delay or censoring handling is discussed — purchase is treated as immediately resolvable once click occurs, identical to ESMM/ESM² |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. As with ESMM and ESM², entire-space modeling here corrects a **sample selection bias in a prediction task** (each of the six sub-targets trained/served over the same entire impression space); it is not an estimate of the causal/incremental effect of the impression |
| 7 | Model architecture | Shared Feature Embedding Module (FEM) → six parallel sub-networks predicting the six hidden conditional-probability variables (y1–y6) for the graph's explicit sub-paths (impression→click, click→D-Mi, D-Mi→D-Ma, D-Ma→purchase, O-Mi→D-Ma, O-Ma→purchase) → parameter-free composition combining y1–y6 into CTR, D-Mi rate, D-Ma rate, and CTCVR per the conditional-probability chain rule (Eq. 1-4); four cross-entropy losses trained jointly, all over the entire impression space |
| 8 | Credit assignment | Single impression → single item (not slate-level), same granularity as ESMM/ESM². HM³'s contribution is adding a second, finer intra-item behavioral tier (micro, nested before macro) to the same click→purchase decomposition chain — still not a mapping from a delayed, user-level outcome onto one of several candidate items |
| 9 | Training data and counterfactual handling | Up to 31.7B impressions (SR-L) with click, micro-behavior, macro-behavior, and purchase binary labels, trained over the entire space with no counterfactual, propensity, or causal adjustment — pure supervised multi-task learning via the six-way chain-rule factorization |
| 10 | Offline and online evaluation | Offline: CVR AUC and CTCVR AUC on three proprietary datasets of increasing scale (SR-S/M/L), against six baselines/ablations. Online: a genuine two-week production A/B test on Alibaba's SR module (2020-10-08 to 2020-10-21), measuring CVR gain and GMV gain versus BASE |
| 11 | Reported gains | CVR AUC 0.85726 vs. BASE's 0.84932 (+0.00794) on the SR-L (107M-user, 31.7B-impression) offline dataset, the best result among all six compared methods; CVR gain +8.27% and GMV gain +8.32% over BASE in a live two-week Alibaba SR-module A/B test — the largest online margin reported among BASE/ESMM/HM³ in Table 5 |
| 12 | Applicability to a two-sided dating recommender | The micro-nested-before-macro hierarchical decomposition is a template for adding intermediate, finer-grained signal stages to the dating cascade (e.g., profile-view depth or message-drafting signals nested before "like"), reusable if the project has comparably fine-grained interaction logs. Like ESMM and ESM², it never leaves the same-session/immediate-purchase horizon, so it contributes a cascade-decomposition technique but no evidence at all on delayed 7-30 day retention or revenue labels, which the project actually needs |
| 13 | Unverified claims | No confidence interval, standard deviation, or significance test is reported for any offline AUC value across SR-S/M/L or for the online CVR/GMV gain percentages, so the precision of the reported (often sub-0.01 AUC) differences between HM³ and its nearest ablation, HM³−R, cannot be independently verified; the claim that GMCM "ignores the macro behaviors" is asserted as motivation but is not re-demonstrated empirically by running a macro-augmented GMCM as a control in this paper's own experiments |

## Project Relevance

Speaks strongly to **Q2** (the finest-grained entire-space credit-assignment decomposition in this batch — a six-way conditional split nesting two behavioral tiers) and weakly to **Q1** (still a short-term CVR proxy, not LTV, though optimized directly). Also weakly relevant to **Q3**, only in the negative sense: it confirms, alongside ESMM and ESM², that this entire sub-lineage of entire-space multi-task papers never engages a delayed or multi-day label — worth noting as a consistent gap across all three papers in the ESMM→ESM²→HM³ line. Partially informs **Q6**: it has both real offline ablations targeted at the paper's specific claims and a genuine two-week online test, offset by no offline variance or significance testing.

Does **not** address **Q4** in the long-vs-short-horizon fusion sense the project needs (the composition module only fuses short-horizon heads), **Q5** (pure prediction, no incrementality), **Q7** (no two-sided, reciprocal, or congestion treatment — single-sided e-commerce funnel), or **Q8** (no staged-migration narrative — HM³ is offered as a wholesale replacement for BASE/ESMM/ESM², not documented as an incremental migration step from a prior production system).

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2021_KDD_AITM_Sequential-Dependence-Audience-Multi-step-Conversions.md](./2021_KDD_AITM_Sequential-Dependence-Audience-Multi-step-Conversions.md) | Related Work / Experiments | Names this paper's method (`HM3`) |
| [2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md](./2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md) | Related Work / Experiments | Names this paper's method (`HM3`) |

_2 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `HM3` across all 133 cards._

## Meta Information

- **Authors:** Hong Wen, Jing Zhang, Fuyu Lv, Wentian Bao, Tianyi Wang, Zulong Chen
- **Affiliations:** Alibaba Group; The University of Sydney
- **Venue:** SIGIR 2021 (44th ACM SIGIR Conference on Research and Development in Information Retrieval, Short Research Paper III)
- **Year:** 2021
- **Relevance:** Core
- **Priority:** 2
- **nlm:ad032348**
