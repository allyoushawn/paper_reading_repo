# Paper Analysis: Reciprocal Sequential Recommendation

**Source:** https://arxiv.org/pdf/2306.14712 (Zheng et al.; RecSys 2023)
**Date analyzed:** 2026-08-16

## 1. Summary

**Title:** Reciprocal Sequential Recommendation
**Authors:** Bowen Zheng et al. (RUCAIBox — Beijing Key Laboratory of Big Data Management and Analysis Methods)
**Venue:** RecSys '23 (17th ACM Conference on Recommender Systems), Singapore

**Abstract (paraphrased from source):** Reciprocal recommender systems (RRS), which model two-way matching between two parties (online dating, recruitment), have mostly captured only static user preferences, ignoring both parties' evolving tastes over time. Sequential recommendation models dynamic preference well but is built for a one-sided (user-selects-static-items) setting, whereas in RRS every user plays a dual role — active selector and passive candidate — making dynamic two-sided sequence modeling non-trivial. This paper formulates reciprocal recommendation as a sequence-matching task and proposes **ReSeq**, which represents users with separate active/passive embeddings, encodes their behavior sequences with Transformers at both a macro (efficient, deployed) and micro (fine-grained, training-only) scale, and uses micro-to-macro self-distillation so that only the cheap macro module is needed at serving time.

**Key contributions:**
1. Formulates reciprocal recommendation as a **sequence matching task** — prediction is based on matching the historical dynamic behavior sequences of both parties, rather than static profiles or static latent factors.
2. **ReSeq**: dual-perspective (active/passive) user embeddings, decomposed and partially shared across the two sides of the market, encoded via Transformers with different attention masks (unidirectional for time-sensitive active behavior, bidirectional for more stable passive behavior).
3. **Multi-scale matching**: an efficient macro-level dot-product match plus a fine-grained, time-sensitive micro-level co-attention match (TiSensiMatch) that alleviates sequence sparsity.
4. **Micro-to-macro self-distillation** (Margin-MSE loss): transfers the micro-level module's matching quality into the macro-level module during training, so only the O(d) macro module is deployed at serving time, avoiding the O(n²d) cost of the micro module in production.

**Methodology.** Each user maintains two embedding matrices — an active/"preference" embedding (used when selecting others) and a passive/"feature" embedding (used when being selected) — decomposed with a shared bilateral matrix C so the two sides' representation spaces are properly aligned (M_U^p = A·C, M_V^f = B·C). Behavior sequences are encoded by two Transformers: a **unidirectional** one for active dynamic behavior (recency-weighted, reflecting that active preferences shift quickly) and a **bidirectional** one for passive dynamic behavior (reflecting that passive traits are comparatively stable), each producing a macro ([CLS]-token) representation and a micro (per-position) representation. Macro-level matching is a simple sum of two dot products: y(i,j) = p(u_i)^T·f(v_j) + p(v_j)^T·f(u_i). Micro-level matching (TiSensiMatch) computes a fine-grained n×n matching matrix between micro active and passive representations, aggregated via co-attention with a learnable, recency-weighted time term, to alleviate the sparsity of any single macro-level signal. Training jointly optimizes a macro BPR loss, a micro BPR loss, and a Margin-MSE self-distillation loss that aligns the macro module's positive-negative score margins with the micro module's (teacher); at inference, only the macro module is deployed.

**Main results.** Across five real-world datasets — three from a Chinese online recruitment platform (Design, Sale, Technology; candidate-recruiter pairs that reached a physical interview are positives) and two from Stack Exchange Q&A (StackOverflow, AskUbuntu; questioner-answerer mutual matching) — ReSeq substantially outperformed all collaborative-filtering, one-sided-sequential, and person-job-fit baselines. On Design, ReSeq reached HR@5 0.4435 vs. the best baseline DPGNN's 0.2422 (~83% relative improvement) and more than double SASRec's 0.2033. On Technology, ReSeq reached HR@5 0.7597 (candidates) / 0.7809 (recruiters) vs. DPGNN's 0.4521/0.4409. On AskUbuntu, ReSeq's questioner HR@5 was 0.5259 vs. the best sequential baseline FMLP-Rec's 0.2706. Self-distillation cut per-batch matching latency from 8.71ms (micro-level, no distillation) to 0.28ms (macro-level, with distillation) — roughly a 30x speedup — while ReSeq's deployed latency (0.28ms) remained only modestly above the one-sided SASRec baseline's 0.10ms.

## 2. Experiment Critique

**Design.** Five real-world datasets across two genuinely distinct reciprocal domains (recruitment and Q&A expert-matching), each split chronologically (last two weeks held out for recruitment; 8:1:1 time-based split for Q&A) with sequences truncated to the current interaction time to prevent leakage. Three baseline families are compared: collaborative filtering (BPR, LFRR, NeuMF, LightGCN), one-sided sequential models (SASRec, SSE-PT, BERT4Rec, FMLP-Rec), and recruitment-specific person-job-fit models (PJFNN, BPJFNN, IPJF, PJFFF, DPGNN).

**Statistical validity.** The paper reports paired t-tests at the 0.01 significance level for its main results tables (marked with "*"), which is a genuine strength relative to several other papers in this batch — ReSeq's improvements over the best baseline on every reported dataset/metric are flagged as statistically significant at that level.

**Online experiments.** None. All evaluation is offline, on historical interaction logs with negative sampling (100 randomly sampled negatives per positive instance, per side).

**Reproducibility.** Strong: code is publicly released (github.com/RUCAIBox/ReSeq), full hyperparameters are given for both ReSeq and every baseline, and dataset statistics (users, interactions, sparsity) are tabulated. The three recruitment datasets themselves are proprietary (from an unnamed Chinese recruitment platform) and not shareable, but the two Q&A datasets (Stack Exchange) are public.

**Overall.** The ablation-style comparison across model families (CF vs. one-sided sequential vs. person-job-fit vs. ReSeq) is thorough and the improvements are large and statistically tested. The main disclosed weakness is a real engineering trade-off, not a swept-under-the-rug failure: the self-distillation coefficient μ is sensitive (too small = no effective knowledge transfer from micro to macro; too large = the model over-prioritizes distillation alignment at the expense of ranking accuracy), and the deployed macro module still carries a latency premium over a one-sided model, which the authors describe as an "inevitable" cost of dual-perspective matching.

## 3. Industry Contribution

**Deployability.** Designed explicitly for production serving cost: the paper's central engineering move is to train with an expensive O(n²d) micro-level matching module but deploy only an O(d) macro-level module distilled from it, so validation, testing, and live inference all use the cheap module. This is a directly reusable pattern for any two-sided sequential ranking system that wants sequence-aware accuracy without sequence-aware serving latency.

**Problems solved.** Extends sequential recommendation — well studied for one-sided user-to-item settings — into the reciprocal setting, where naively applying a one-sided sequential model (e.g., SASRec) to one side of the market ignores that the same user is simultaneously being sequentially "consumed" by the other side; ReSeq's dual active/passive embeddings and dual attention-mask design (unidirectional for fast-changing active preference, bidirectional for slower-changing passive traits) directly targets that asymmetry.

**Engineering cost.** Two Transformer encoders per side (active + passive) roughly doubles sequence-encoding cost relative to a one-sided sequential model, though this is a training-time-only cost for the micro module. The distillation hyperparameter μ requires tuning per dataset (best values differed: 0.005 vs. 0.01 across two datasets in the paper's own sweep), adding an extra tuning axis relative to a single-loss sequential model.

## 4. Novelty vs. Prior Work

**Claimed novelty.** The paper states this is "the first time that dynamic behavior sequences of two parties are considered in reciprocal recommendation" — prior RRS work modeled only static preferences (profiles or static latent factors), and prior sequential-recommendation work modeled only one side of a market at a time.

**Prior work named in the source (Query 2, part 3):**
- Pizzato et al., "RECON: a reciprocal recommender for online dating," RecSys 2010 — foundational RRS definition and profile-based matching framework.
- Neve and Palomares, "Latent factor models and aggregation operators for collaborative filtering in reciprocal recommender systems," RecSys 2019 — the LFRR baseline used for comparison.
- Kang and McAuley, "Self-attentive sequential recommendation," ICDM 2018 — SASRec, the primary one-sided sequential baseline and architectural basis for ReSeq's Transformer encoders.
- Rendle et al., "BPR: Bayesian personalized ranking from implicit feedback," UAI 2009 — the BPR loss used to train both the macro and micro matching heads.
- Yang et al., "Modeling Two-Way Selection Preference for Person-Job Fit," RecSys 2022 — DPGNN, the strongest person-job-fit baseline, and source of the dual-perspective ranking metrics (HR@k, NDCG@k, MRR@k) used for evaluation.
- Sun et al., "BERT4Rec: Sequential recommendation with bidirectional encoder representations...," CIKM 2019 — a bidirectional-attention sequential baseline.
- Vaswani et al., "Attention is all you need," NeurIPS 2017 — the Transformer architecture ReSeq's active/passive sequence encoders are built on.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Design (recruitment) | 12,274 candidates, 9,141 recruiters, 139,355 interactions, 99.88% sparse | Not public | Chinese recruitment platform, 100+ days of logs; interview-reached pairs are positives. |
| Sale (recruitment) | 15,831 candidates, 12,757 recruiters, 112,340 interactions, 99.94% sparse | Not public | Same platform/protocol as Design. |
| Technology (recruitment) | 56,620 candidates, 48,071 recruiters, 808,376 interactions, 99.97% sparse | Not public | Same platform/protocol as Design; largest of the three recruitment sets. |
| StackOverflow | Questioner-answerer mutual-matching interactions | Public | Stack Exchange Q&A data; 5-core filtered. |
| AskUbuntu | Questioner-answerer mutual-matching interactions, smaller scale | Public | Stack Exchange Q&A data; 5-core filtered. |

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Reciprocal Sequential Recommendation; Bowen Zheng et al. (RUCAIBox); RecSys 2023; https://arxiv.org/abs/2306.14712 |
| 2 | Source type | Academic |
| 3 | Direction | D8 |
| 4 | Problem setting | Modeling dynamic, evolving preferences on both sides of a reciprocal (two-way) matching market — online recruitment, Q&A expert matching — where existing RRS work captures only static preferences and existing sequential-recommendation work is one-sided. |
| 5 | Objective and label definition | Objective: joint loss L = L_ma + λ·L_mi + μ·L_sd, where L_ma and L_mi are BPR ranking losses at the macro and micro scale respectively, and L_sd is a Margin-MSE self-distillation loss aligning macro (student) score margins to micro (teacher) score margins. Label: a positive is a bilateral, mutually-agreed interaction — a candidate-recruiter pair that reached a physical interview (recruitment datasets), or a matched questioner-answerer pair (Q&A datasets). Horizon: sequences are truncated to the current interaction time step T to prevent leakage; no calendar-time retention/conversion window (e.g., 7-day, 30-day) is defined. **Delay and censoring are not addressed** — the paper works entirely with static, already-resolved historical logs sliced by sequence position, not by elapsed real time. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. It predicts a matching-degree/propensity score for a user pair; it does not estimate a causal or counterfactual effect of exposure. Paper's own wording: "Our target is to construct a matching function y(i,j) = →g(u_i, S^T_{u_i}, v_j, S^T_{v_j}) + ←g(u_i, S^T_{u_i}, v_j, S^T_{v_j}) that **predicts the matching degree or score** y(i,j) between both users by dual-perspective modeling of their historical behavior sequences." |
| 7 | Model architecture | Dual embedding matrices per user (active/preference and passive/feature), decomposed and partially shared across the market's two sides via a common projection matrix C. Two Transformer encoders per side — unidirectional-masked for time-sensitive active behavior, bidirectional-masked for stable passive behavior — each yielding a macro ([CLS]) and micro (per-token) representation. Macro matching is a dot-product sum; micro matching (TiSensiMatch) is a fine-grained co-attention over the n×n matching matrix with a learnable recency weight. Micro-to-macro self-distillation (Margin-MSE) lets only the macro module be deployed at serving time. |
| 8 | Credit assignment | Pointwise, item-level (one bilateral pair). "We do not explicitly use the term of item, since each side can play the roles of users... and items... as in traditional recommender systems." The output score y(i,j) attaches to a specific pair (u_i, v_j); the paper does not model slate-level, impression-level, or coordinate-based credit assignment. |
| 9 | Training data and counterfactual handling | Trained on historical, observational sequential interaction logs (candidate-recruiter pairs that reached interview; questioner-answerer matches), with 100 randomly sampled negatives per positive per side for the BPR losses. No off-policy correction, propensity weighting, or counterfactual estimator of any kind is used or discussed. |
| 10 | Offline and online evaluation | Offline only: Hit Ratio (HR@5), NDCG@5, and MRR@5, computed dual-perspective (both sides of the market), plus per-batch serving latency (ms) to validate the self-distillation speedup. **No online evaluation** — the paper does not report or mention any live A/B test. |
| 11 | Reported gains | Design (recruitment), candidate side: ReSeq HR@5 0.4435 vs. best baseline DPGNN 0.2422 (~83% relative gain) and SASRec 0.2033. Technology (recruitment), candidate side: ReSeq HR@5 0.7597 vs. DPGNN 0.4521. AskUbuntu (Q&A), questioner side: ReSeq HR@5 0.5259 vs. best sequential baseline FMLP-Rec 0.2706. Latency: 0.2832 ms/batch (ReSeq, with self-distillation) vs. 8.7105 ms/batch (ReSeq, without self-distillation) on Design — a ~30x reduction — vs. 0.1024 ms/batch for the one-sided SASRec baseline. |
| 12 | Applicability to a two-sided dating recommender | Explicitly designed for dual-role, two-sided sequential settings — directly analogous to a dating app where both A and B have evolving preferences and behavior histories; the active/passive dual-embedding design and the self-distillation serving pattern (train fine-grained, deploy cheap) are both directly reusable engineering patterns. It has **no congestion or capacity treatment** — every match in its evaluation is scored independently, with no shared-resource constraint across candidates competing for the same counterpart's attention. |
| 13 | Unverified claims | The "first to consider dynamic behavior sequences of two parties in reciprocal recommendation" claim is self-reported, not independently verified here. The recruitment datasets are proprietary, so the headline HR@5 gains on Design/Sale/Technology cannot be independently reproduced (only the Stack Exchange results can). The authors' claim that ReSeq's latency overhead versus SASRec is "inevitable" is asserted, not proven to be a lower bound. |

## Project Relevance

Relevant to **Q2/credit assignment** as a pointwise, per-pair architecture consistent with the project's per-candidate-profile decision granularity, and to **Q3/label definition** as one more confirmation that this literature works exclusively with static, already-resolved historical logs — sequence truncation by position, not by elapsed calendar time — with **no delay or censoring handling**, which is a direct gap relative to the project's 7–30 day retention horizon. Its main positive contribution to the survey is architectural rather than objective-related: the self-distillation "train fine-grained, deploy cheap" pattern (Q8, migration paths) is a directly transferable serving-cost-reduction technique that could let a future unified retention/revenue model use a fine-grained two-sided interaction signal in training while keeping inference-time cost low, echoing (in a different mechanism) the model-distillation approach seen elsewhere in this survey's non-D8 batches. On the batch's two required extractions: **reciprocity** is modeled not as a fusion of two independently-trained one-sided scores, but as a single joint architecture with shared, decomposed active/passive embeddings across both sides — a genuinely different mechanism from both the Palomares-survey harmonic-mean approach and the CyberAgent TU-matching equilibrium approach in this same batch. **Congestion is explicitly not addressed** — confirmed directly by NotebookLM's Query 3 part 4 answer ("No... The paper does not address physical capacity limits, resource constraints, or market-wide congestion"), making this the one paper in the batch with a clean, unambiguous negative result on that dimension. As with the rest of this batch, it is also a clean **negative finding for Q1/Q5**: the objective is exclusively short-term match/interview propensity, with no retention or revenue term and no causal/incrementality framing anywhere in the paper.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `ReSeq`._

## Meta Information

- **Authors:** Bowen Zheng et al.
- **Affiliations:** RUCAIBox / Beijing Key Laboratory of Big Data Management and Analysis Methods
- **Venue:** RecSys '23 (ACM Conference on Recommender Systems)
- **Year:** 2023
- **Relevance:** Core
- **Priority:** 1
- **nlm:84a66338-bc3e-41a8-86b0-7881ded409a6**
