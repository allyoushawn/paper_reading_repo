# Paper Analysis: Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Multi-task/2020 (Alibaba) (WWW) Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning
**Authors:** Wenhao Zhang, Wentian Bao, Xiao-Yang Liu, Keping Yang, Quan Lin, Hong Wen, Ramin Ramezani (UCLA / Alibaba Group / Columbia University)
**Venue/Year:** WWW 2020

**Abstract (paraphrased):** Post-click conversion rate (CVR) estimation in e-commerce is challenged by (1) selection bias — CVR models are conventionally trained only on the click space, but must serve predictions over the full exposure space, and clicks are not a random sample of exposures, so training data is Missing Not At Random (MNAR); and (2) data sparsity — clicks and especially conversions are rare, giving CVR estimators too little data relative to their parameter count. The paper proposes two causal (missing-data-theory) estimators, Multi-IPW and Multi-DR, that combine inverse-propensity-weighting and doubly-robust estimation with a multi-task learning module (to address sparsity via parameter sharing across the exposure → click → conversion chain), and proves both are theoretically unbiased under stated conditions.

**Key contributions:**
1. A formal proof, with a concrete counterexample, that ESMM (Ma et al. 2018's "Entire Space Multi-task Model," a very widely cited CVR baseline) is **not actually unbiased** despite being designed and marketed to solve the selection-bias problem — a direct negative result about a heavily used prior method.
2. **Multi-IPW**: a multi-task inverse-propensity-weighting CVR estimator that uses a jointly-trained CTR task's output as the propensity score to inversely weight the CVR loss, computed over the full exposure space (not just the click space).
3. **Multi-DR**: a multi-task doubly-robust CVR estimator that augments Multi-IPW with a third, jointly-trained imputation task estimating the CVR prediction error; unbiased if *either* the propensity score *or* the imputation model is accurate (not requiring both).
4. First paper (per the authors) to combine IPW/DR-based causal missing-data estimators with a multi-task learning framework, gaining the standard MTL benefits (parameter sharing addressing data sparsity, reduced embedding storage, faster training) on top of the causal debiasing.

**Methodology:** Three chained tasks — CTR, CVR, and (for Multi-DR only) an Imputation task — share an embedding lookup table over user and item features via multi-task parameter sharing, exploiting the sequential exposure → click → conversion pattern. Multi-IPW's loss weights each observed (u,i) pair's CVR cross-entropy loss by the inverse of the predicted CTR (used as the propensity of being "observed"/clicked), summed over the *entire exposure space* D rather than only the click space O. Multi-DR adds the imputation-task output as an unbiased-in-expectation correction term (Eq. 9), giving the classical doubly-robust guarantee.

**Main results:** On four large-scale Alibaba/Taobao production datasets (1.1B–11.5B exposures) and the public Ali-CCP dataset, Multi-IPW and Multi-DR consistently outperform ESMM and other causal/non-causal baselines on CTCVR-AUC and GAUC, while requiring less or equivalent training time and less parameter memory than the compared Joint-Learning-DR baseline (which does not use multi-task parameter sharing).

## 2. Experiment Critique

- **Design:** The paper's central theoretical contribution — a formal bias proof for both its own estimators (Theorem 3.1 for Multi-IPW, Theorem 3.2 for Multi-DR) and a formal bias proof *against* the widely-used ESMM baseline (Eq. 3, with a worked counterexample in Figure 2) — is a methodologically strong piece of experiment design: it is not just an empirical comparison but a mathematical demonstration of *why* a well-known prior method fails, under a clearly stated MNAR framework (Rubin's missing-data formalism).
- **Statistical validity:** Ali-CCP results (Table 3) are repeated 10 times with mean ± 1 std reported; production dataset results (Table 2) are reported as single-run point estimates across four dataset sizes (Set A–D) without confidence intervals or repeated runs, which is a comparative weakness relative to the Ali-CCP experiments.
- **Online experiments:** **None reported.** All evaluation in the reviewed pages is offline (CVR AUC, CTCVR AUC, GAUC on held-out production data), plus separate computational-efficiency benchmarking (training time, embedding size, hidden-layer parameter size, Figure 4). There is no live A/B test or online deployment result.
- **Reproducibility:** Public Ali-CCP dataset is used and cited with a source link (Tianchi Alibaba Cloud), making the Ali-CCP experiments independently reproducible; the four production datasets (Set A–D, 1.1B to 11.5B exposures from Mobile Taobao) are proprietary and not released.
- **Explicitly stated limitation (a genuine, self-acknowledged weakness):** the paper's own "Unbiased Evaluation" section (5.4) states that a truly unbiased test set — one collected via random exposure/forced random clicks — "is rather unobtainable in real practice," because the platform cannot force users to click on items to generate unbiased data. The paper therefore evaluates using CTCVR-AUC/GAUC as a *proxy* for unbiasedness, and explicitly flags this gap as something "further investigated in the future work" — i.e., the causal-debiasing claim is validated relative to a biased evaluation set, an important caveat the authors state plainly rather than gloss over.
- **Other limitation stated:** Multi-IPW's unbiasedness is contingent on accurately estimated propensities, described by the authors themselves as "too restricted" a condition in practice — which is precisely the motivation for the Multi-DR extension (its weaker, either/or unbiasedness condition).

## 3. Industry Contribution

- **Deployability:** Evaluated at real Alibaba/Taobao production scale (up to 11.5B exposures, 5.3 billion production-data samples vs. 5.3 billion parameters cited for context on the sparsity problem, 109 features across user/item/combination categories, a distributed cluster configuration with 100 workers/440 CPU cores/25 GPU cards is reported in Table 4), which is a strong deployability signal even without a reported online experiment.
- **Problems solved:** Directly targets a very common industrial pain point — the mismatch between the CVR training distribution (click space) and the serving/inference distribution (full exposure space) — with a principled, formally justified correction rather than a heuristic one, and does so while remaining compatible with standard multi-task CTR/CVR ranking pipeline structure (a chained CTR→CVR architecture very close to production ESMM-style models already in wide industrial use).
- **Engineering cost:** Multi-IPW and Multi-DR are shown (Figure 4, computational-cost radar diagrams) to require *less or equivalent* training time and smaller embedding/hidden-layer parameter footprints than the compared causal baselines (Naive IPW, Joint Learning DR), because the multi-task parameter-sharing module reduces duplicated embedding storage — a concrete, quantified engineering-cost advantage over prior causal CVR estimators, not just an accuracy one.
- **Ranking pipeline framing:** This is a CVR-prediction-stage model, feeding into the same architectural slot as ESMM in a standard CTR→CVR ranking pipeline; it is not itself a full ranking/serving model but a training-time debiasing method for one component (the conversion-probability estimate) of such a pipeline.

## 4. Novelty vs. Prior Work

Novelty is framed against three prior lines: (a) ESMM (Ma et al. 2018), the dominant prior industrial CVR estimator, which the paper formally proves is biased despite its unbiasedness claims — the single most load-bearing novelty claim in the paper; (b) prior single-task IPW-based recommender debiasing (Schnabel et al. 2016, "Naive IPW" baseline) and prior doubly-robust joint-learning estimators (Wang et al. 2019, "Joint Learning DR" baseline), neither of which the paper says is devised specifically for CVR's severe data-sparsity regime nor efficient at industrial scale (Joint Learning DR is shown to need more embedding/parameter memory and comparable-or-more training time); (c) the paper's own stated first-of-its-kind claim: combining IPW/DR-based causal estimators with a multi-task-learning architecture specifically to address CVR data sparsity, which it argues is a novel combination not previously proposed.

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| Ali-CCP | Yes — public | 84M exposures, 3.4M clicks, 18K conversions, 0.4M users, 4.3M items | Hosted on Alibaba Cloud Tianchi (link given in paper); the standard public CVR benchmark this literature uses |
| Alibaba Mobile Taobao production Set A–D | No — proprietary | 1.1B, 2.7B, 6.0B, 11.5B exposures respectively | 3-week transactional data from Mobile Taobao; 109 features (user, item, combination); Set A/B/C/D = first 5%/20%/50%/100% of the 3-week window |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning," Wenhao Zhang, Wentian Bao, Xiao-Yang Liu, Keping Yang, Quan Lin, Hong Wen, Ramin Ramezani, UCLA / Alibaba Group / Columbia University, WWW 2020, https://doi.org/10.1145/3366423.3380037 |
| 2 | Source type | Academic paper with industry (Alibaba) co-authors and production-scale data |
| 3 | Direction | D5 |
| 4 | Problem setting | Post-click conversion-rate (CVR) estimation in an e-commerce recommender, where the sequential exposure → click → conversion pattern causes the training distribution (click space) to differ systematically from the inference distribution (full exposure space), and where click/conversion events are rare (data sparsity). |
| 5 | Objective and label definition | Binary conversion label r_{u,i} ∈ {0,1} per (user, item) exposure pair; the observed/training label is only available for pairs the user actually clicked (o_{u,i}=1), and is treated as missing (not simply negative) for unclicked exposures — an MNAR (Missing Not At Random) framing, not a delayed-label framing. No time horizon beyond the immediate exposure→click→conversion event chain is modeled; "Not specified in source" for any longer-horizon or multi-day label. |
| 6 | **Prediction or incrementality** | Prediction only — and the distinction matters precisely: the paper's "causal" methods (Multi-IPW, Multi-DR) correct **selection bias in a prediction**, not estimate an incremental/causal **effect of exposure**. They apply inverse-propensity-weighting and doubly-robust techniques from the missing-data/potential-outcomes literature to produce an unbiased estimate of P(conversion=1 \| exposure) over the full exposure space, given that training data is only observed in the click subspace. This is a correction for MNAR sample selection into the *training set*, not an estimate of how much *showing* an item causally changes the probability of conversion relative to not showing it. The paper never defines or estimates a treatment/control contrast, an uplift, or a counterfactual-outcome-under-exposure quantity — it estimates a single conditional probability, debiased for who got observed, not for what would have happened under a different exposure decision. |
| 7 | Model architecture | Three-task chain (CTR, CVR, and for Multi-DR, an Imputation task) sharing a common embedding lookup table via multi-task parameter sharing; each task has its own fully-connected tower over the shared, concatenated embeddings. Multi-IPW's CVR loss is divided by the CTR task's predicted score (used as an estimated propensity) and summed over the full exposure space. Multi-DR adds the Imputation task's estimated prediction-error term combined via the classical doubly-robust formula. |
| 8 | **Credit assignment** | Standard pointwise, per-(user, item)-exposure credit assignment — each exposure is independently modeled and labeled; there is no journey-level, slate-level, or delayed backward attribution. This is the simplest form of credit assignment among the four papers in this batch. |
| 9 | Training data and counterfactual handling | Alibaba/Taobao production logs (Set A–D) and the public Ali-CCP dataset; the paper's central contribution *is* its counterfactual/missing-data handling — Multi-IPW and Multi-DR are explicitly designed to correct for the fact that conversion labels are only observed in the click subspace (MNAR), using propensity weighting (estimated via the jointly-trained CTR task) and, for Multi-DR, an auxiliary imputation model, with formal unbiasedness proofs given accurate propensities/imputation. |
| 10 | Offline and online evaluation | Offline only: CVR AUC, CTCVR AUC, and Group AUC (GAUC, exposure-weighted AUC grouped by page-view/user) on held-out data from both Ali-CCP and the four production sets; separate computational-efficiency comparison (training time, embedding parameter count, hidden-layer parameter count) across models on the same production cluster. No online/live A/B test is reported. |
| 11 | Reported gains | On Ali-CCP (Table 3, mean ± 1 std over 10 runs): Multi-DR CVR AUC 69.29 ± 0.31 / CTCVR AUC 65.43 ± 0.34, vs. ESMM CVR AUC 68.56 ± 0.37 / CTCVR AUC 65.32 ± 0.49. On production Set D (11.5B exposures, Table 2): Multi-DR CTCVR AUC 75.39 / GAUC 62.28, vs. ESMM CTCVR AUC 73.81 / GAUC 60.56. Multi-IPW and Multi-DR outperform all baselines (Base, Oversampling, ESMM, Naive Imputation, Naive IPW, Heuristic DR, Joint Learning DR) across all four production sets and Ali-CCP. |
| 12 | Applicability to a two-sided dating recommender | Directly relevant to the project's need to distinguish "prediction debiased for selection" from "incremental causal effect" — this paper is a clean worked example of the *former*, and its formal proof that ESMM (a common industrial multi-task CVR baseline, structurally similar to today's like/match/conversation predictor) is biased is a cautionary, technically grounded precedent for auditing whichever CTR/CVR-style component the project retains. It offers no reciprocity, congestion, fairness, or two-sided-market treatment, and — critically — offers no incrementality machinery the project's uplift-blend replacement could reuse directly; its causal machinery corrects sample selection, not exposure effects. |
| 13 | Unverified claims | The claim to be "the first paper" combining IPW/DR-based methods with multi-task learning is a novelty assertion by the authors, not independently verified. The postulate that "the exposure space is the entire item space" (i.e., every item is exposed to some user at least once) is explicitly flagged by the authors themselves as a simplifying relaxation of the true problem, not a proven property of their data. |

## Project Relevance

Speaks directly to **Q2** and the project's own north-star distinction, "**prediction vs. incrementality**" — but as a worked counter-example rather than a solution: this paper's "causal approaches" are entirely about debiasing a *prediction* against selection bias (MNAR from click-space training), and explicitly do **not** estimate the incremental effect of showing an item, which is exactly the gap the project's uplift model is meant to fill. It is valuable primarily as (a) a rigorous formal framework (Rubin MNAR / IPW / doubly-robust) the project could reuse if it needs to debias its own retained CTR/CVR-style predictions against selection bias, and (b) a load-bearing negative result — a formal proof that ESMM, a very common industrial multi-task CVR baseline structurally similar to a like/match/conversation predictor, is not actually unbiased, which is a useful caution when auditing any retained short-term-event model. It does not address Q1, Q3 (beyond the immediate click/conversion event, no delayed label), Q4 (no head-fusion question beyond the CTR-as-propensity trick), Q5 (no incrementality at all — the batch note's caution applies exactly here), Q6, Q7, or Q8.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md](./2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task-Model.md) | Related Work / Experiments | Names this paper's method (`MultiDR`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `MultiDR` across all 133 cards._

## Meta Information

- **Authors/Affiliations:** Wenhao Zhang, Ramin Ramezani (University of California, Los Angeles); Wentian Bao, Keping Yang, Quan Lin, Hong Wen (Alibaba Group); Xiao-Yang Liu (Columbia University)
- **Venue/Year:** WWW 2020
- **Relevance:** Core
- **Priority:** 1
- **NotebookLM source ID:** `nlm:311e06b5`
