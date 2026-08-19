# Paper Analysis: Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2021 (Tencent) (SIGIR) Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Title: Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback. Authors: Xiao Zhang, Haonan Jia, Hanjing Su, Wenhan Wang, Jun Xu, Ji-Rong Wen. Affiliations: Gaoling School of AI / Renmin University of China; Tencent Inc. Venue: SIGIR '21 (44th International ACM SIGIR Conference), July 11-15 2021, Virtual Event, Canada.

Abstract/contribution: proposes CBDF (Counterfactual Bandit with Delayed Feedback) for streaming recommendation with delayed conversion feedback (motivating example: coupon recommendation, where a click is immediate but conversion may occur much later or not at all). The problem is framed as a batched contextual bandit (sequential decision-making), and a counterfactual reward-modification step uses importance sampling to reweight the observed (possibly still-censored) delayed reward toward an unbiased estimate of the true (eventual) delayed reward, before each batch policy update. The paper proves the modified reward is an unbiased estimator of the true expected delayed reward (Theorem 4.1, with a finite-sample error bound) and derives a sublinear regret bound for the resulting batched-bandit policy (Theorem 5.1).

Methodology: 7-tuple batched-bandit formulation ⟨S,A,π,R,γ,N,B⟩; reward R = λĈ + (1-λ)Ȳ combines immediate click feedback Ĉ and delayed conversion feedback Ȳ. Each episode introduces a "counterfactual deadline" ξ that splits the collected data buffer into an observed set (conversions confirmed before ξ) and a hold-out set, used to fit per-action survival/hazard models (assuming an exponential delay distribution) via maximum likelihood. The fitted hazard model gives an importance weight w(S) = 1/Pr{D=1|V=1,S} that corrects the observed delayed reward Ȳ into a modified reward R^mod = λĈ + (1-λ)·w·Ȳ. A ridge-regression/UCB-style batch policy update (closed-form linear bandit, analogous to LinUCB) is then trained on the modified rewards for the next episode's online recommendations.

Main results: experiments on a synthetic dataset, the public Criteo conversion-logs dataset (two campaign subsets: 5 actions/75,021 instances and 15 actions/1,278,556 instances), and a real dataset from Tencent's WeChat coupon-recommendation system (216,568 instances, 1-month period, 86 numerical + 16 categorical features). CBDF is compared against SBUCB (Sequential Batch UCB, LinUCB fed batched data), EXP3-B (batched EXP3), SBUCB-D (SBUCB with incomplete instances discarded), and DFM-S (a sequential/online adaptation of Chapelle's 2014 Delayed Feedback Model). CBDF achieves the highest average reward on all four environments and converges faster than the baselines.

## 2. Experiment Critique

Design: theoretically grounded (Theorem 4.1 unbiasedness proof, Theorem 5.1 sublinear regret bound, both proved in the appendix). Empirically, all algorithms run 20 times and average performance reported (mean ± std given for the WeChat real-data experiment, Table 2), but the Criteo and synthetic experiments (Figures 6-7) show only reward curves without confidence bands or explicit significance tests. Online experiments: none — all evaluation is offline/simulated; the WeChat "real dataset" experiment still trains a DFM model of the true CVR/delay process offline and uses it to simulate feedback, because, per the authors, real online experimentation was not available for this study ("Due to the limitation of real online experiments, in this study we still trained DFM ... as the online environment"). Reproducibility: hyperparameters are given (weighting via C_λ, regularization μ range [0.5:+0.1:2], counterfactual-deadline C_ξ=50%, importance-weight cap w_max∈[1:+0.1:2], batch-size formula B=C_B²N/d with C_B∈[75,80] empirically verified in Section 6.5.1); code release is not stated; the WeChat dataset is proprietary, only the Criteo dataset is public.

## 3. Industry Contribution

CBDF is designed explicitly for a production streaming-recommendation loop where a policy is retrained every episode on the most recent, partially-censored feedback rather than waiting for delay to resolve — directly matching the paper's stated industry constraint that "models need to be updated very frequently... over very short time scales." Running time on WeChat data (66.5±9.7s) is reported as comparable to the SBUCB baseline (60.9±3.2s) and far below DFM-S (311.4±10.9s), so the reward-modification step adds negligible cost relative to a plain bandit. Engineering cost: requires maintaining a per-action hazard/survival model (re-fit via MLE each episode) plus an observed/hold-out data split by counterfactual deadline — added infrastructure relative to a plain bandit, but no separate delay-resolution wait period or extra feature engineering.

## 4. Novelty vs. Prior Work

The paper positions CBDF against the Batched Bandit Framework (BBF) of prior statistics/learning-theory literature, noting BBF assumes rewards are fully known at the end of a batch, whereas CBDF explicitly models delayed and biased rewards within the batch. It also contrasts with prior delayed-feedback CTR/CVR literature (Chapelle 2014 DFM, exponential delay model; Yasui et al. 2020 feedback-shift correction via importance weighting; Saito et al. 2020 dual learning; Ktena et al. 2019 neural continuous training) by being, per the authors, the first to formulate streaming recommendation-with-delayed-feedback explicitly as a sequential decision-making / batched-bandit problem with a theoretically unbiased reward-correction step and a regret guarantee, rather than a static offline retraining correction.

## 5. Dataset Availability

| Dataset | Type | Size | Availability |
|---|---|---|---|
| Synthetic | Simulated | N=40 episodes, B=10,000, 5 actions, d=10 | Not public (generative procedure fully specified in paper, reproducible from description) |
| Criteo conversion-logs (recent-5actions / all-15actions) | Public benchmark | 75,021 instances / 1,278,556 instances | Public — https://labs.criteo.com/2013/12/conversion-logs-dataset/ |
| Tencent WeChat coupon dataset | Proprietary, real commercial | 216,568 instances, 1-month, 5 coupon-category actions | Not available — proprietary |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback," Zhang, Jia, Su, Wang, Xu, Wen; Renmin University of China / Tencent; SIGIR '21; 2021; https://doi.org/10.1145/3404835.3462892 |
| 2 | Source type | Academic paper with industry (Tencent) co-authorship and a real Tencent WeChat commercial dataset |
| 3 | Direction | D7 |
| 4 | Problem setting | Streaming (continuously retrained) recommendation where the reward has an immediate component (click) and a delayed component (conversion) that may not yet be observed at model-update time; motivating use case is coupon recommendation in WeChat. |
| 5 | Objective and label definition | Reward R = λĈ + (1-λ)Ȳ, a linear combination of the immediate click indicator Ĉ=C and the delayed conversion indicator Ȳ=Y (whether a conversion is observed before the data-collection cutoff). The true target is the unobservable eventual-conversion variable V (=1 if the user will ever convert). Horizon: delay time γ (time between click and conversion) is modeled as exponentially distributed, motivated by an empirical WeChat plot showing ~70% of conversions delayed past day 0, decaying roughly exponentially over ~14 days (Fig. 1). Delay/censoring handling: a per-episode "counterfactual deadline" ξ acts as a virtual data-collection cutoff, splitting each batch into an observed set (confirmed conversions before ξ) and a hold-out set used to fit a per-action exponential hazard model; the fitted model estimates Pr{V=1｜S} and reweights the observed reward before every batch policy update, rather than waiting for the delay window to fully resolve. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The "counterfactual" in this paper's title and method refers to correcting the observed (censored) conversion label toward the unobserved true eventual-conversion outcome V, not to estimating the causal effect of the recommendation/exposure itself. The importance weight w = Pr{V=1｜S}/Pr{Y=1｜S} is an inverse-probability-of-censoring correction (a survival-analysis-style debiasing of a delayed label, mathematically parallel to IPCW), not a treatment-effect estimator. The bandit still maximizes an outcome-prediction reward (expected click+eventual-conversion given context and action), not an incremental/uplift quantity relative to a counterfactual non-exposure. |
| 7 | Model architecture | Linear contextual bandit: policy π_n(S) = argmax_A ⟨θ_A^n, S⟩ + μ√(Sᵀ(Φ_A^n)^{-1}S), a UCB-style ridge-regression bandit with θ_A updated in closed form each episode from the modified rewards. The reward-correction step (CRM, Algorithm 2) fits per-action MLE hazard parameters β_A via an exponential-hazard survival model, hazard h_A(S)=exp(⟨β_A,S⟩). |
| 8 | Credit assignment | Single impression/action-level: each (context, action, delayed-reward) tuple corresponds to one recommended coupon shown to one user in one interaction step; there is no multi-touch or multi-item credit split — the debiasing operates purely on the observed-vs-true conversion label for that one action, not on distributing a user-level outcome across multiple items or a slate. |
| 9 | Training data and counterfactual handling | Training data is an online-collected batch buffer D_n = {(S_i,A_i,C_i,Y_i,c_i,e_i)} gathered under the current policy each episode (on-policy bandit data, not logged/off-policy replay). Counterfactual handling: importance-sampling reweighting of the delayed reward via the estimated survival/hazard model (Section 4.2), proven unbiased under the exponential-delay assumption (Theorem 4.1) with an explicit finite-sample error bound of order T^(-1/2). |
| 10 | Offline and online evaluation | Offline only — average-reward curves over training episodes on the synthetic dataset, two Criteo campaign subsets, and the WeChat dataset (WeChat additionally reports CVR, CTCVR, and running time). No live online A/B test is run; the WeChat "real dataset" experiment uses an offline-trained DFM model of the true CVR/delay process as a simulated environment because real online experimentation was not available for this study. |
| 11 | Reported gains | On the Tencent WeChat dataset (Table 2): CBDF achieves CVR 0.7775±0.0056 and CTCVR 0.3046±0.0025, an improvement of 3.86% CVR and 2.39% CTCVR over the second-best baseline (SBUCB: CVR 0.7307±0.0015, CTCVR 0.2807±0.0008), with running time (66.5±9.7s) close to SBUCB (60.9±3.2s) and far below DFM-S (311.4±10.9s). On synthetic and Crieo data, CBDF shows the highest average-reward curves throughout training (Fig. 6), converging within ~10 episodes on the synthetic dataset. |
| 12 | Applicability to a two-sided dating recommender | Not two-sided — this is a single-sided platform-to-user coupon recommendation with no reciprocity or congestion. Its relevance is narrower: the counterfactual-deadline reweighting mechanism for correcting a still-censored delayed label inside a frequently-retrained (streaming) loop is a directly transferable building block for training on impressions whose 7-30 day retention/revenue outcome has not yet resolved, though the exponential-delay assumption and single-action-per-impression structure would need adaptation to a slate/reciprocal setting. |
| 13 | Unverified claims | The exponential-delay assumption for conversion time is empirically motivated only by the WeChat delay histogram (Fig. 1) and is not validated against alternative delay-distribution families in this paper. The claim that CBDF's advantage grows because baseline bandits "use the unmodified rewards" and DFM-S "was originally developed for batch learning... resulting in low sample efficiency when applied to sequential decision making" is the authors' own interpretation of their results, not independently benchmarked against a DFM variant purpose-built for the streaming setting. |

## Project Relevance

Speaks most directly to **Q3** (label/horizon definitions for delayed outcomes, delay/censoring handling) — CBDF's counterfactual-deadline + hazard-model reweighting is the most sophisticated delayed-label-correction mechanism in this batch, explicitly designed for a frequently-retrained streaming loop, which matches the project's need to train on impressions whose 7-30 day retention or weeks-scale revenue outcome is still unresolved. Also touches **Q6** (offline/online evaluation under delay) via its regret-bound theory and simulated-environment evaluation methodology, and weakly touches **Q5** (uplift/incrementality) only to the extent that field 6 above clarifies the paper does *not* address incrementality despite the "counterfactual" framing — a distinction the project must track carefully, since the paper's own terminology could otherwise be mistaken for causal-effect estimation. **Low relevance to Q1, Q2, Q4, Q7, Q8** — the paper does not treat retention/LTV as the training objective (target is a click+conversion reward), has no credit-assignment problem beyond a single action, does not combine short- and long-term heads, and has no two-sided/reciprocal-market structure.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2008_KDD_NA_Learning-Classifiers-Positive-Unlabeled-Data.md](./2008_KDD_NA_Learning-Classifiers-Positive-Unlabeled-Data.md) | Related Work / Experiments | Names this paper's method (`CBDF`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `CBDF` across all 133 cards._

## Meta Information

- **Authors:** Xiao Zhang, Haonan Jia, Hanjing Su, Wenhan Wang, Jun Xu, Ji-Rong Wen
- **Affiliations:** Gaoling School of Artificial Intelligence / Beijing Key Laboratory of Big Data Management and Analysis Methods / School of Information, Renmin University of China; Tencent Inc.
- **Venue:** SIGIR '21 (44th International ACM SIGIR Conference on Research and Development in Information Retrieval)
- **Year:** 2021
- **Relevance:** Core
- **Priority:** 1
- **nlm:67faf577**
