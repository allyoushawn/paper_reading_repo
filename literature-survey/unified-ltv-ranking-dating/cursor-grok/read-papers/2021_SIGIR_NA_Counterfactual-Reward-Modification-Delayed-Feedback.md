# Paper Analysis: Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback

**Source:** http://ai.ruc.edu.cn/uploads/20210728/258dff20dc157be8fd2a68ef6f2c6f01.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback
- **authors or company:** Xiao Zhang, Haonan Jia, Hanjing Su, Wenhan Wang, Jun Xu, Ji-Rong Wen (Renmin University of China; Tencent)
- **venue:** SIGIR
- **year:** 2021
- **URL:** https://doi.org/10.1145/3404835.3462892
- **source type:** industry paper
- **direction:** D7
- **problem setting:** Streaming coupon recommendation on Tencent WeChat where click is immediate but conversion is delayed; models retrained frequently on short collection windows with incompletely labeled instances.
- **objective and label definition:** Reward R = λ·click + (1−λ)·conversion, where conversion Y may be unobserved if it occurs after data collection (true conversion V latent). CBDF modifies delayed reward via counterfactual importance sampling: R_mod = λ·C + (1−λ)·w·Y with w = Pr(V=1|S)/Pr(Y=1|S). Batched bandit (LinUCB-style) policy updated each episode on modified rewards. λ set from estimated CVR (e.g., 0.7 on WeChat).
- **prediction or incrementality:** Counterfactual importance sampling yields unbiased estimate of expected true delayed reward Pr{V=1|S}—addresses bias from censored conversions, not full causal incrementality of recommendation on user LTV.
- **model architecture:** CBDF = Counterfactual Reward Modification (CRM algorithm estimating delay hazard per action) + batched contextual bandit (UCB policy, Eq. 11–12). Linear reward model per action arm; episodes of B steps with periodic batch updates.
- **credit assignment:** Per (context, recommended item) pair; immediate click and delayed conversion combined into scalar reward; importance weights correct downward bias when conversions not yet observed. ~70% of WeChat coupon conversions delayed past collection day.
- **training data and counterfactual handling:** Core contribution: CRM reweights observed delayed feedback using learned hazard models on action-specific subsets; counterfactual deadline ξ at 50% of batch horizon; hold-out set for hazard estimation. Compared to discard, DFM-S, SBUCB, EXP3-B baselines.
- **offline and online evaluation:** Synthetic bandit (N=40 episodes, B=10k, d=10); Criteo display-ad dataset; Tencent WeChat coupon logs. CBDF achieves highest average reward on synthetic data after ~10 episodes; outperforms baselines on Criteo and WeChat. Regret bound O(√dT) with suitable batch size B = C²_B·N/d, C_B ≈ 75–80.
- **reported gains:** CBDF converges faster than unmodified-reward bandits on synthetic data; beats DFM-S, SBUCB, EXP3-B, SBUCB-D on all three datasets (exact metric values vary by dataset; WeChat is production coupon traffic).
- **applicability note for a two-sided dating recommender:** Theoretically grounded pattern for unbiased reward estimation when match/conversation labels arrive after daily retrain windows—importance-weighted delayed rewards applicable before retention labels mature.
- **applicability note for a two-sided dating recommender:** Coupon click→conversion setting is single-sided; reward is immediate+delayed binary events, not 7–30 day retention or subscription revenue; bandit formulation differs from large-scale neural rankers.
- **unverified claims:** none

## 1. Summary

**Title:** Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback
**Authors:** Xiao Zhang et al. (RUC / Tencent)
**Abstract:** Proposes CBDF, combining counterfactual importance-sampled reward modification for delayed conversions with batched contextual bandit learning for streaming recommendation. Proves unbiased delayed-reward estimates and sublinear regret.

**Key contributions:**
- CRM algorithm correcting biased delayed feedback via importance weights.
- CBDF framework integrating CRM with batched bandit policy updates.
- Theoretical regret analysis and experiments on synthetic, Criteo, and WeChat data.

**Methodology:** Model delayed conversion observability with hazard functions; reweight rewards; UCB exploration on modified rewards per episode.

**Main results:** CBDF outperforms discard and heuristic delayed-feedback baselines across datasets.

## 2. Experiment Critique

**Design:** Synthetic simulation matching delayed-feedback statistics; public Criteo; real WeChat coupon data with reported delay distribution.

**Statistical validity:** Average reward curves over 20 runs on synthetic; regret bounds provided theoretically.

**Online experiments (if any):** WeChat production coupon data used for evaluation; live A/B not explicitly reported in abstract.

**Reproducibility:** Criteo public; WeChat data proprietary; SIGIR paper PDF available from author host.

**Overall:** Valuable theory-backed delayed-feedback correction for streaming bandits; reward is click+conversion, not long-horizon retention.

## 3. Industry Contribution

**Deployability:** Designed for frequent retraining on short windows (WeChat coupon scenario); bandit scale may limit direct neural-ranker transfer.

**Problems solved:** Biased training when ~70% conversions arrive after collection cutoff.

**Engineering cost:** Moderate—hazard model per action + batch bandit update; simpler than full neural continuous-training stacks.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First counterfactual online approach to streaming recommendation with delayed feedback in batched bandit setting.

**Prior work comparison:** DFM (Chapelle), batched bandits (Perchet et al.), counterfactual learning (Joachims et al.), LinUCB.

**Verification:** Synthetic and WeChat experiments support unbiasedness claim; neural LTV ranking not addressed.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic | Described in paper | Yes | Simulated delays |
| Criteo | Public | Yes | Display ads |
| Tencent WeChat coupons | Not public | No | Delay stats in Figure 1 |

**Offline experiment reproducibility:** Synthetic and Criteo reproducible; WeChat not.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Click + delayed conversion composite reward—not retention/revenue unified objective.

**(2) Credit assignment:** Importance-weighted correction maps censored delayed labels to unbiased conversion expectation per context—relevant precursor to honest delayed retention credit.

**(3) Label and horizon definitions:** Conversion delay exponential on WeChat; batch collection windows; λ from CVR.

**(4) Short-term + long-term heads:** Single composite reward R = λ·click + (1−λ)·conversion rather than separate fusion.

**(5) Prediction vs incrementality:** Counterfactual debiasing of observed rewards toward true delayed outcome probability.

**(6) Offline and online evaluation:** Bandit average reward and regret; no retention A/B or two-sided metrics.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Could inform reward modification layer atop streaming trainer when match labels are delayed—orthogonal to unified LTV architecture but supports honest delayed labels.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Xiao Zhang, Haonan Jia, Hanjing Su, Wenhan Wang, Jun Xu, Ji-Rong Wen
**Affiliations:** Renmin University of China; Tencent
**Venue:** SIGIR 2021
**Year:** 2021
**PDF:** http://ai.ruc.edu.cn/uploads/20210728/258dff20dc157be8fd2a68ef6f2c6f01.pdf
**Relevance:** Core
**Priority:** 1
