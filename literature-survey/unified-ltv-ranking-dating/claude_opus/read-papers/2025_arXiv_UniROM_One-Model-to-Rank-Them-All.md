# Paper Analysis: One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning

**Source:** arXiv:2505.19755 (Meituan); also accepted at CIKM 2025 as "UniROM: Unifying Online Advertising Ranking as One Model" (ACM DOI 10.1145/3746252.3761044)
**Date analyzed:** 2026-08-16

## 1. Summary

UniROM (Qiu, Wang, Zhang, Zheng, Zhu, Fan, Zhang, Wang, Wang — Meituan) targets the Multi-stage Cascading Architecture (MCA) that dominates industrial ad ranking: recall → pre-ranking → ranking → auction, each stage independently trained and progressively filtering a candidate pool from roughly 10^5 down to 10^1 items. The authors identify two structural failure modes of MCA: (1) **stage inconsistency** — divergent optimization targets and capacity gaps between lightweight early stages and heavy downstream stages create prediction discrepancies that degrade final ad quality, and (2) **ignored externalities** — most stages assume CTR is independent per-ad, missing mutual influence and permutation effects among candidates shown together.

The proposed fix is UniROM, described as "the first industrial-grade end-to-end generative architecture" to unify all four MCA stages into a single model that directly generates an optimal ad sequence from the full ~10^5-item candidate corpus for a location-based-services (LBS) request. Three components carry this: a **Hybrid Feature Service (HFS)** that decouples static ad-feature storage (local, low-latency) from dynamic user/context features (single RPC, broadcast to all candidates) to make scoring 10^5 candidates per request tractable; **RecFormer**, a cluster-attention Transformer variant (Global Cluster-Former for O(N·N_c·d) intra-sequence attention instead of O(N²d), plus a Mid-fusion Interest-Former combining target- and context-attention) that jointly models user interest and cross-ad externalities; and **AucFormer**, a non-autoregressive generator that produces the winning ad allocation directly (rather than filtering a shortlist), paired with a permutation-aware evaluator (reward model) and a payment network enforcing incentive compatibility (IC) and individual rationality (IR) constraints. Training is bi-stage: supervised pre-training on click cross-entropy (set-aware pCTR, with popularity-sampled unexposed ads), followed by post-training with Reinforcement Learning from Auction Feedback (RLAF) that optimizes the generator against the frozen evaluator's revenue-based reward, jointly with a Lagrangian-regularized payment network.

Main results: on Meituan's industrial LBS dataset (200M requests / 2M+ users / ~10M ads, April–October 2024), UniROM beats the strongest baseline (FS-LTR, a state-of-the-art unified-training MCA variant) by Recall@50 +20.4%, AUC +1.48%, eCTR +8.3%, eRPM +11.4%, and cuts the incentive-compatibility regret metric Ψ from 9.1% to 2.3%. A 7-day live A/B test on Meituan's platform shows CTR +5.2%, RPM +13.6%, advertiser ROI +3.1%, with only a 2.2% (~5ms) increase in response time despite scoring hundreds of times more candidates than the deployed MCA ranking stage.

## 2. Experiment Critique

**Design.** The offline comparison is reasonably controlled: UniROM, MCA, and FS-LTR are evaluated on the same held-out 14-day window, offline experiments repeated 5 times with different seeds (mean ± std reported), and an ablation isolates each of the three architectural components (UniROM−gcf, UniROM−mif, UniROM−auf) plus a separate cross-feature-removal study. The ablations are informative and directionally consistent (each component contributes, AucFormer removal hurts eRPM most).

**Statistical validity.** Offline metrics carry variance estimates; the online A/B test reports point-estimate percentage lifts (CTR +5.2%/RPM +13.6%/ROI +3.1% over 7 days) with no confidence intervals, significance test, or traffic-split description beyond "large-scale." The paper's own abstract claims "statistically significant improvements" but the significance test itself is not shown in the material retrieved from this source.

**Online experiments.** A single 7-day window (Nov 18–24, 2024) against a single incumbent (fully deployed MCA) is the only live evidence. No FS-LTR-vs-UniROM online comparison is reported (FS-LTR is offline-only), so the online lift is attributable to UniROM over the actually-deployed MCA, not over the strongest offline baseline.

**Reproducibility.** The dataset is proprietary and results are explicitly stated to have been transformed to protect business secrets ("some transformations were applied to the results... designed to maintain the statistical [properties]"), so absolute numbers are not independently verifiable. No code release is mentioned. Architecture and hyperparameters (layer counts, popularity-sampling ratios N_s=2995, K=5) are specified in enough detail to reproduce the method conceptually on a different dataset, but not to reproduce these exact numbers.

**Overall.** Internally consistent and reasonably rigorous by industry-paper standards (seeded offline reruns, ablations, a real online test), but the online claim rests on one short window against one baseline, and the "first industrial-grade" priority claim is unverifiable from this source alone.

## 3. Industry Contribution

UniROM's central engineering claim is collapsing four independently-trained, independently-served models (SASRec recall, DSSM pre-ranking, DIN ranking, GSP auction) into one model and one serving path. This has real deployability implications framed directly in the paper: the **Hybrid Feature Service** is explicitly an algorithm/engine co-design to solve the feature-transmission bottleneck of scoring 10^5 candidates per request — static ad features are stored locally (memory/SSD) rather than fetched by RPC per stage, and dynamic user/context features are fetched once and broadcast, which is what keeps response-time growth to ~5ms despite the much larger candidate set. The **cluster-attention mechanism** (O(N·N_c·d) vs. O(N²d)) is a direct answer to the latency cost of full-candidate-set attention at production scale. Collapsing four models into one also removes a class of engineering cost that MCA papers rarely quantify: maintaining consistent feature pipelines, retraining schedules, and monitoring across four separately-owned stages — UniROM trades that operational surface for a single, larger, harder-to-debug model with a two-stage (pretrain → RLAF) training pipeline that itself introduces new operational complexity (frozen-evaluator reward model training, Lagrangian dual tuning for the payment network).

## 4. Novelty vs. Prior Work

The claimed novelty is being the first industrial-grade, fully end-to-end generative architecture to replace the entire MCA — prior unification attempts (FS-LTR, COPR) only harmonize training objectives *across* MCA stages via relabeling, without removing the cascade itself. The paper positions itself against: **DIN** (Zhou et al., "Deep interest network for click-through rate prediction," KDD 2018) as the ranking-stage attention baseline; **SIM** (Pi et al., "Search-based user interest modeling with lifelong sequential behavior data for click-through rate prediction," CIKM 2020) for lifelong sequence retrieval; **SASRec** (Kang & McAuley, "Self-attentive sequential recommendation," ICDM 2018) as the recall-stage sequence encoder; **DSSM** (Huang et al., "Learning deep structured semantic models for web search using clickthrough data," CIKM 2013) as the pre-ranking dual-tower baseline; **FS-LTR** (Zheng et al., "Full stage learning to rank: A unified framework for multi-stage systems," WWW 2024) as the strongest unified-training MCA competitor; **GSP** (Edelman, Ostrovsky & Schwarz, "Internet advertising and the generalized second-price auction," American Economic Review 2007) as the classic non-learned auction mechanism; and **CGA** (Zhu et al., "Contextual Generative Auction with Permutation-level Externalities for Online Advertising," arXiv:2412.11544, 2024) as the theoretical basis for AucFormer's incentive-compatibility proof.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Meituan industrial LBS dataset | Offline (200M requests, 2M+ users, ~10M ads, Apr–Oct 2024) | No — proprietary, results transformed to protect business secrets | 200 days pretrain / 50-day sampled post-train / 14-day test split |
| Meituan online A/B traffic | Online (7-day live test, Nov 18–24 2024) | No — proprietary | Single window, single incumbent baseline (MCA) |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning," Junyan Qiu, Ze Wang, Fan Zhang, Zuowu Zheng, Jile Zhu, Jiangke Fan, Teng Zhang, Haitao Wang, Xingxing Wang (Meituan), arXiv, 2025, https://arxiv.org/abs/2505.19755 (also CIKM 2025, DOI 10.1145/3746252.3761044) |
| 2 | Source type | Industry paper (arXiv preprint; accepted CIKM 2025) |
| 3 | Direction | D1 |
| 4 | Problem setting | Replacing a 4-stage MCA (recall→pre-ranking→ranking→auction) in online advertising with a single end-to-end model over a ~10^5-item LBS candidate pool, addressing stage inconsistency and ignored ad-to-ad externalities |
| 5 | Objective and label definition | Binary click labels (ζ_clk ∈ {0,1}): current-request clicks for the K exposed ads, platform-wide/same-session clicks for N_s popularity-sampled unexposed ads. No retention or revenue horizon is defined, no delay or censoring handling — temporal scope is a single session/request |
| 6 | Prediction or incrementality | Prediction only. The paper states "ad systems output the pCTR denoting the probability that the user clicks the ad" and the evaluator "aims to predict the permutation-aware values for each ad" — no causal/incrementality framing is present |
| 7 | Model architecture | Hybrid Feature Service (decoupled local/remote feature storage) + RecFormer (Global Cluster-Former + Mid-fusion Interest-Former, cluster-attention) + AucFormer (non-autoregressive generator + permutation-aware evaluator/reward model + payment network), trained bi-stage: CE pretraining then RLAF post-training with a Lagrangian-dual payment network |
| 8 | Credit assignment | Slate/sequence-level: the reward for ad a_yi in a generated sequence Y is its marginal contribution to platform revenue, r_yi = b_yi·q_yi − Σ(other ads' bid×pCTR in the best sequence excluding it); this per-ad marginal-contribution reward is what RLAF's policy gradient uses, i.e. credit is assigned via each item's counterfactual removal effect on total sequence revenue, not via a user-level outcome |
| 9 | Training data and counterfactual handling | Logged impression/click data from real requests, K exposed + N_s popularity-sampled unexposed ads per sample; no counterfactual or off-policy correction — supervised CE on logged outcomes, then on-policy RLAF against a learned (not logged) reward model |
| 10 | Offline and online evaluation | Offline: Recall@50, AUC, eCTR, eRPM, and Ψ (IC/regret metric) on a 200M-request held-out set, 5 seeded reruns. Online: 7-day live A/B test on Meituan's platform measuring CTR, RPM, ROI, and response time |
| 11 | Reported gains | Recall@50 +20.4%, eRPM +11.4%, and Ψ (regret) reduced from 9.1% to 2.3% vs. FS-LTR on the Meituan offline industrial dataset (200M requests); online CTR +5.2%, RPM +13.6%, ROI +3.1% vs. the deployed MCA baseline in a 7-day Meituan A/B test, with only +2.2% (~5ms) response-time increase |
| 12 | Applicability to a two-sided dating recommender | No reciprocity, congestion, or two-sided fairness treatment — UniROM is single-sided (advertiser vs. platform, mediated by an auction). Its architectural pattern (unify a multi-stage cascade into one generative model, pretrain on existing myopic labels then RL-post-train toward a platform objective) is a directly reusable migration template if the reward is swapped from ad revenue to retention/revenue and reciprocity constraints are added |
| 13 | Unverified claims | "First industrial-grade" end-to-end unification is a priority claim not independently checked here. Offline numbers are explicitly stated to be transformed for confidentiality, so absolute magnitudes are not verifiable. The scaling-law analysis (Section 5.5) shows diminishing returns from stacking more blocks but the authors state that testing larger data/sequence scales is "beyond the scope" of the study — i.e., whether the plateau is fundamental or an artifact of the tested data scale is untested |

## Project Relevance

Directly on **Q8** (migration path): the bi-stage training strategy — pretrain on existing myopic click labels, then RL-post-train toward a platform-level objective while freezing the pretrained backbone — is a concrete, literal template for migrating a CTR-model-plus-blend system into a single model without discarding the existing feature/label infrastructure. Directly on the survey's **"one unified model"** structural target (D1, Core): UniROM is a real, deployed instance of exactly this migration, with a documented staged rollout and quantified engineering cost (HFS to control latency, response-time delta reported). Partially on **Q4** (fusion): AucFormer's evaluator produces a single permutation-aware value used for both ranking and payment, closer to a "one value head" design than a fixed/learned fusion of separate heads.

It does **not** answer Q1/Q3 as posed — the objective is still click/revenue-per-impression (eCTR/eRPM), not retention or a delayed, censored label — and it does not address Q2 (no user-level-to-item-level delayed-outcome attribution; credit assignment here is intra-slate revenue attribution, not outcome attribution over time), Q5 (no causal/incrementality treatment), or Q7 (no reciprocity/congestion/fairness — single-sided ad auction). Its primary value to this survey is architectural/engineering precedent for Q8, not label or evaluation methodology for Q1–Q3.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `UniROM`._

## Meta Information

- **Authors:** Junyan Qiu, Ze Wang, Fan Zhang, Zuowu Zheng, Jile Zhu, Jiangke Fan, Teng Zhang, Haitao Wang, Xingxing Wang
- **Affiliations:** Meituan (Shanghai / Chengdu / Beijing, China)
- **Venue:** arXiv preprint 2505.19755 (2025); accepted CIKM 2025 (ACM DOI 10.1145/3746252.3761044)
- **Year:** 2025
- **Relevance:** Core
- **Priority:** 2
- **nlm:7eab8b6f-1e09-402a-83bf-f2f04bc7fe66**
