# Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback

- **Source index:** 110
- **Source ID:** `67faf577-5c46-4fd6-ab18-c10c94e30ef7`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Xiao Zhang, Haonan Jia, Hanjing Su, Wenhan Wang, Jun Xu, Ji-Rong Wen
- **Affiliations:** Renmin University of China and Tencent
- **Year / venue:** 2021 / SIGIR
- **Direction / priority:** D7 delayed feedback / Priority 3
- **URL:** https://doi.org/10.1145/3404835.3462892

## 1. Summary

CBDF formulates streaming recommendation with immediate clicks and delayed conversions as a batched contextual bandit. Each episode splits observed feedback around a counterfactual deadline, fits a survival model, and uses importance sampling to modify incomplete rewards. The next batched-bandit policy trains on these corrected rewards. The paper proves unbiased reward estimation under its assumptions and a sublinear regret bound.

Evidence covers synthetic data, Criteo-derived simulators, and one month of WeChat coupon logs. Almost 70% of WeChat coupon conversions occur after day zero. On 216,568 WeChat instances across five coupon categories, CBDF reports CVR 0.7775 and click-through-conversion rate 0.3046, versus best listed baseline values of 0.7389 and 0.2807. Runtime is 66.5 seconds, close to SBUCB’s 60.9 and far below DFM-S’s 311.5. Results are averages over 20 runs; this is logged-data simulation/replay, not a live randomized deployment.

## 2. Experiment Critique

CBDF connects delayed-label correction to sequential policy learning rather than stopping at prediction, provides theory, and tests public plus commercial data. Multiple baselines and repetitions strengthen the evidence.

The Criteo “online environments” are learned simulators whose AUCs range from 0.70 to 0.90, so policy conclusions inherit model error. Importance weights depend on a correct delay/survival model and are truncated, introducing a practical bias–variance compromise. The WeChat experiment replays logged data; it does not establish live causal lift. Stationarity, positivity, and reward composition are material assumptions.

## 3. Industry Contribution / Project Relevance

Unlike purely supervised delay models, CBDF is close to the project’s desired decision loop: learn a policy while long-horizon rewards are incomplete. A dating version could combine immediate like/match signals with delayed retention or revenue and update in batches.

The reward definition must be redesigned. Coupons have one-sided actions; dating has mutual choice, scarce candidate attention, and interference. The method also does not solve attribution of a later return or subscription to a specific exposure. A safe use would begin as a delayed-reward bandit baseline with conservative propensities and marketplace guardrails, not as an unrestricted production optimizer.

## 4. Novelty

The paper’s central contribution is counterfactual importance-weighted reward modification inside a batched-bandit loop, with unbiasedness and regret analysis.

## 5. Dataset Availability

Criteo Conversion Logs are public. The WeChat coupon dataset is proprietary. Code availability is **Not specified in source**.

## 6. Community Reaction

Not specified in source beyond SIGIR 2021 publication.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2026_arXiv_DRL_Model-Agnostic-Downstream-Rewards-Learning.md](./2026_arXiv_DRL_Model-Agnostic-Downstream-Rewards-Learning.md) | Introduction / Summary | Explicitly contrasts with or discusses a limitation around full title. |

## 8. Meta Information

- **Immediate outcome:** Click
- **Delayed outcome:** Coupon conversion
- **Model:** Batched contextual bandit with corrected reward
- **Theory:** Unbiased reward under assumptions; sublinear regret
- **Live A/B test:** Not reported
- **Project role:** Delayed-reward policy-learning baseline
