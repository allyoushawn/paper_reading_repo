# Paper Analysis: Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems

**Source:** arXiv:2208.04560 / KDD '22 (DOI: 10.1145/3534678.3539040) — nlm:b0d40032-08a0-4c62-ad6b-c138b9a2649d
**Date analyzed:** 2026-08-16

## 1. Summary

**Title:** Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems
**Authors:** Qihua Zhang, Junning Liu, Yuzhuo Dai, Yiyan Qi, Yifan Yuan, Kunlun Zheng, Fan Huang, Xianfeng Tan (Tencent Inc.)
**Venue:** KDD '22 (the paper's own PDF header carries a leftover ACM template placeholder, "Conference'17, July 2017, Washington, DC, USA" — this is a formatting artifact, not the real venue; the confirmed venue is KDD '22 via ACM DOI 10.1145/3534678.3539040 and arXiv metadata)

**Abstract (paraphrased):** Industrial ranking systems are typically built from two stages: a multi-task learning (MTL) model that predicts individual user feedback signals (clicks, likes, shares), and a multi-task fusion (MTF) model that combines those predictions into one final ranking score. The fusion step has received far less research attention than the MTL step despite being the last, decisive step of ranking. Existing MTF approaches (grid search, evolutionary strategies) are computationally expensive, cannot personalize fusion weights, and — critically — only optimize instant/greedy user return rather than long-term user satisfaction. The paper reframes MTF itself as a sequential decision problem and solves it with reinforcement learning.

**Key contributions:**
- Formulates the **session-based MTF task as a Markov Decision Process (MDP)**, so that the fusion weights themselves (not the recommended items) are the RL action.
- **BatchRL-MTF framework**: combines offline Batch-Constrained Deep Q-learning (BCQ) — restricting learned actions to stay near the historical action distribution to control extrapolation error — with an online "Mixed Multi-Exploration" policy that safely discovers higher-value fusion weights in production.
- **Conservative-OPEstimator**: a CQL-regularized offline policy value estimator that lets the team screen candidate policies before committing to a live A/B test, explicitly to avoid burning online experimentation budget on bad policies.
- Full production deployment on a Tencent short-video platform serving hundreds of millions of users, with the reward-tuned variant delivering **+2.550% App Dwell Time (ADTime)** and **+9.651% User Positive-Interaction Rate (UPIRate)**.

**Methodology:** The MDP is defined per recommendation session. **State** = user profile (age, gender, location) concatenated with interaction-history features over the user's last 500 watched videos. **Action** = a continuous, personalized fusion-weight vector α = (α₁,...,α₁₂) used in a log-linear fusion scoring function f(o) = Σ αᵢ·log(oᵢ+βᵢ), where oᵢ are the MTL model's per-task predicted scores. **Reward** (see Reference Card field 5 for the full definition) is a weighted sum of immediate per-item feedback signals, with weights set via offline statistical analysis of which behaviors predict future app dwell time. The **actor** is a conditional VAE that generates candidate fusion-weight actions constrained to resemble the historical (logged) action distribution, refined by a perturbation network bounded at ρ=0.15 and trained via deterministic policy gradient. The **critic** uses Clipped Double Q-Learning (twin Q-networks) to control overestimation bias, a known failure mode (extrapolation error) of naive off-policy RL trained on fixed logs. In production, two exploration streams — pure Gaussian random exploration and Gaussian-noise-perturbed exploitation — are mixed 50/50 to build the next training batch, which is why the paper calls this "Mixed Multi-Exploration."

**Main results:** On a held-out 10% test split of 3.142M sessions / 11.155M interactions, the Conservative-OPEstimator's offline value V(π_e) correctly rank-ordered policies that later succeeded or failed online: naive off-policy TD3 scored a catastrophic -648.162 offline (and indeed could not be deployed online at all — it produced unusable action values), while BatchRL-MTF scored a stable +4.126. A month-long online A/B test (baseline = Bayesian Optimization) confirmed this ordering: the reward-tuned deployment variant, BatchRL-MTF-Rinteraction, delivered +2.550% ADTime and +9.651% UPIRate, both reported as statistically significant (p<0.05).

## 2. Experiment Critique

**Design:** The paper combines a genuine offline/online concordance check (does the proposed offline estimator agree with what actually happens online?) with a real production A/B test — a notably strong design for this literature, since it directly demonstrates that Conservative-OPEstimator's offline ranking of policies (TD3 worst, CQL+SAC highest-but-volatile, BatchRL-MTF stable-and-strong) reproduced online: TD3 was excluded from online deployment entirely because it was deemed too risky (it produces exploding, out-of-distribution Q-values), and the online ranking of the remaining methods matched the offline V(π_e) ranking.

**Statistical validity:** Online improvements are explicitly reported with "p-value<0.05" against the Bayesian Optimization (BO) baseline (Table 1), which is a meaningfully more rigorous statistical disclosure than the other three papers in this batch. Offline, the Conservative-OPEstimator's V(π_e) is a point estimate per policy with no confidence interval or variance reported across independent training runs, so its reliability as a ranking signal (rather than just a directional one) is not independently quantified.

**Online experiments:** Genuine month-long production A/B test on a Tencent short-video platform (hundreds of millions of users), comparing BatchRL-MTF against Bayesian Optimization, Evolutionary Strategy, TD3, UWAC+TD3, and CQL+SAC. TD3 alone was excluded from the online test as unsafe to deploy — a useful negative result about naive off-policy RL in production fusion. The paper also reports a reward-function ablation online (Rtime/Rintegrity/Rinteraction variants), directly demonstrating a "reward seesaw": over-weighting play-time increases ADTime but decreases UPIRate, and vice versa for play-integrity — a concrete, named failure mode for anyone tuning a similar composite reward.

**Reproducibility:** Low-to-moderate. Full hyperparameters are disclosed (ρ=0.15, γ=0.95, learning rates, replay buffer size 100,000, batch size 256, 300,000 training epochs, 12-dimensional action space), which is unusually thorough. However, the underlying dataset (3.142M Tencent sessions) and the online platform are proprietary; no code or data release is mentioned. The reward weights wᵢ themselves — the actual mapping from raw behaviors to the reward label — are said to be set "via extensive statistic analysis" without giving the resulting numbers, so the reward function is not fully reproducible even if the RL algorithm is.

**Overall:** This is the most methodologically careful paper in the batch: it names and empirically documents specific failure modes (extrapolation error/TD3 explosion, the reward seesaw, perturbation-bound sensitivity ρ=0.10 too narrow vs. 0.30 too noisy), reports statistical significance for its headline online claim, and validates its own offline evaluator against ground-truth online outcomes rather than presenting the offline number as sufficient on its own. The main reproducibility gap is the proprietary dataset and unstated reward weights.

## 3. Industry Contribution

**Deployability:** Fully deployed to production on a large-scale Tencent short-video platform. The paper's framing is explicitly about solving a last-mile production problem — how to combine already-existing MTL prediction heads — rather than proposing a new prediction model, which makes it directly slottable into a ranking pipeline that already has a CTR/CVR-style MTL stage (this maps closely onto the survey's own "blend two scores after the fact" starting point).

**Problems solved:** Replaces a hand-tuned or grid-searched fusion weight (a single global set of weights, or at best evolutionary-strategy-tuned weights) with a personalized, learned policy that explicitly optimizes a long-term-oriented reward rather than the immediate MTL scores themselves. The Conservative-OPEstimator directly solves the practical engineering problem of not being able to A/B test every candidate policy: it lets the team screen out policies like TD3 before ever risking user experience online.

**Engineering cost:** Ranking-pipeline latency impact should be modest — the fusion weight vector α is only 12-dimensional and the fusion function itself is a simple log-linear combination (same computational shape as whatever hand-tuned fusion it replaces); the RL machinery (VAE + perturbation network + twin critics) lives in an offline/batch training loop, re-trained daily on the past three days of trajectory logs, not in the online serving hot path beyond computing the already-cheap policy forward pass. Feature engineering is modest (user profile + last-500-video interaction history, already standard in this kind of system). The main new infrastructure is the online Mixed Multi-Exploration logging (randomized and noise-perturbed serving buckets) needed to keep generating fresh, diverse training data — an operational commitment beyond just training a model once.

## 4. Novelty vs. Prior Work

**Claimed novelty:** First (or one of very few) successful applications of Batch RL specifically to the multi-task fusion step (as opposed to applying RL to select recommended items directly). Explicitly contrasts itself with prior RL-for-recommendation work whose action is "recommendation item(s)," noting its own action is instead the fusion weight vector.

**Prior work it positions against:**
- **Fujimoto et al., 2019 ("Off-policy deep reinforcement learning without exploration," ICML)** — the BCQ algorithm and the extrapolation-error diagnosis that BatchRL-MTF's actor network directly builds on.
- **Kumar et al., 2020 ("Conservative Q-learning for offline RL," arXiv)** — the CQL regularizer underlying the Conservative-OPEstimator.
- **Zhao et al., 2019 ("Recommending what video to watch next: a multitask ranking system," RecSys)** — cited to frame the standard industrial MTL/ranking pipeline this paper's fusion step sits downstream of.
- **Pei et al., 2019 ("Value-aware recommendation based on reinforced profit maximization...")** — i.e., Paper 4 in this same batch — cited as a pioneering prior attempt at RL-based fusion, which this paper explicitly extends from single-step/immediate profit to session-based long-term satisfaction.
- **Ma et al., 2018 ("Modeling task relationships in multi-task learning with multi-gate mixture-of-experts," KDD)** — the standard MTL architecture assumed upstream.
- **Fujimoto et al., 2018 ("Addressing function approximation error in actor-critic methods," ICML)** — source of the Clipped Double Q-Learning technique used in the critic.
- **Silver et al., 2014 ("Deterministic policy gradient algorithms," ICML)** — the optimization method for the perturbation network.

Notably, this paper directly cites and extends Paper 4 of this same batch (Pei et al.'s value-aware/reinforced profit maximization), explicitly framing its own session-level, long-term-satisfaction reward as a generalization of Pei et al.'s simpler profit-maximization reward — a real, paper-stated lineage between two references in this survey.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Tencent short-video batch dataset | Offline training/test | No — proprietary | 3.142M sessions, 11.155M interactions; first 90% (chronological) train, last 10% test |
| Tencent short-video online platform | Online A/B | No — proprietary | Month-long live deployment, hundreds of millions of users |

No public benchmark dataset used; no code or data release mentioned.

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems; Qihua Zhang, Junning Liu, Yuzhuo Dai, Yiyan Qi, Yifan Yuan, Kunlun Zheng, Fan Huang, Xianfeng Tan — Tencent Inc.; KDD '22; 2022; https://arxiv.org/abs/2208.04560 (DOI: https://doi.org/10.1145/3534678.3539040) |
| 2 | Source type | Industry paper (Tencent, peer-reviewed at KDD) |
| 3 | Direction | D1 |
| 4 | Problem setting | The last-mile ranking fusion step: combining an existing MTL model's per-task predictions (click, like, share, play-time, play-integrity, comment, etc.) into one final ranking score, reframed as a sequential decision problem instead of a static weight-search problem |
| 5 | Objective and label definition | MDP formulated per recommendation session. Reward label r(s,a) = Σ wᵢvᵢ, a weighted sum of immediate per-item user feedback (video play time, play integrity, and interaction behaviors: liking, sharing, commenting); weights wᵢ are set via offline statistical analysis of which behaviors predict future app dwell time. Horizon is the session (discount factor γ=0.95); no explicit delay/censoring handling — reward is computed from immediately observed feedback at each step, and long-term satisfaction is captured only implicitly through the discounted-cumulative-reward MDP formulation, not through any delayed-label modeling |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The upstream MTL model predicts user feedback outcomes; the RL policy predicts/optimizes an expected cumulative reward from those predictions. The paper's own words: "a Multi-Task Learning model (MTL) that predicts various user feedback... and a Multi-Task Fusion model (MTF) that combines the multi-task outputs into one final ranking score." No causal-effect-of-exposure framing, uplift, or counterfactual language appears anywhere |
| 7 | Model architecture | BCQ-style actor-critic: actor = conditional VAE (generates in-distribution candidate fusion-weight actions) + perturbation network (deterministic policy gradient, bound ρ=0.15); critic = twin Clipped Double Q-networks. Fusion function itself is a log-linear combination f(o)=Σαᵢlog(oᵢ+βᵢ) over MTL outputs, with the 12-dimensional α vector as the RL action |
| 8 | Credit assignment | Session-level MDP with item-level (pointwise) reward attribution: at each step t, the agent recommends one item, observes that item's immediate feedback, and assigns the resulting weighted-behavior score as the reward for that step; these are chained via the Bellman equation so the value function reflects expected cumulative session reward, but no joint slate-level reward and no delayed (multi-day) outcome are modeled — everything is same-session, one-item-at-a-time |
| 9 | Training data and counterfactual handling | Trained offline on logged (batch) trajectories via Batch-Constrained Q-learning specifically to control extrapolation error / out-of-distribution actions — this is itself the paper's core counterfactual-safety mechanism, constraining the learned policy's actions to resemble the logging policy's historical action distribution. Retrained daily on the trailing three days of logs. New data is generated online via a Mixed Multi-Exploration policy (50% pure random Gaussian exploration, 50% Gaussian-noise-perturbed exploitation) rather than through any propensity-weighted off-policy correction |
| 10 | Offline and online evaluation | Offline: proposed Conservative-OPEstimator (Fitted-Q-Evaluation + CQL regularizer) producing a policy value V(π_e) = "long-term user satisfaction per session," validated by comparing its ranking of methods to the actual online ranking. Online: month-long A/B test on a live Tencent short-video platform, hundreds of millions of users, metrics = App Dwell Time (ADTime) and User Positive-Interaction Rate (UPIRate), improvements reported with p<0.05 |
| 11 | Reported gains | Deployed variant BatchRL-MTF-Rinteraction: +2.550% ADTime and +9.651% UPIRate online A/B vs. Bayesian Optimization baseline, Tencent short-video platform (p<0.05). Standard BatchRL-MTF: +2.216% ADTime / +9.118% UPIRate online, and offline Conservative-OPEstimator value V(π_e)=4.126 vs. -648.162 for TD3 and -297.053 for UWAC+TD3 on the same held-out test set |
| 12 | Applicability to a two-sided dating recommender | High structural applicability: this is the closest architectural template in the batch to the survey's target — a learned RL policy replacing a hand-tuned/grid-searched fusion of existing prediction heads, explicitly optimized for a longer-horizon satisfaction signal rather than greedy engagement. It has no two-sided, reciprocal, or congestion modeling of its own, so those constraints would need to be added rather than reused |
| 13 | Unverified claims | The specific reward weights wᵢ mapping raw behaviors to the composite reward are asserted to come from "extensive statistic analysis" but the analysis itself and resulting weight values are not shown, so the reward design is not independently checkable. The claim that BatchRL-MTF is "one of the few" successful Batch RL applications to MTF is a positioning claim, not something the paper demonstrates via a systematic survey |

## Project Relevance

**Named seed reference — high project relevance.** This paper is a direct, close-to-complete architectural template for the survey's Q1 (replaces the exact "MTL model + hand-tuned/searched fusion" pattern the survey describes with a learned RL policy optimized for a longer-horizon satisfaction reward), Q4 (this is precisely a *learned fusion* of existing short-term prediction heads, one of the three fusion strategies Q4 asks about), and Q8 (documents a concrete migration path: keep the existing MTL heads unchanged, replace only the fusion step, using Batch RL trained on logged fusion-weight "actions" plus a live mixed-exploration policy to keep generating fresh data — directly analogous to how the target system could keep its CTR/CVR heads and replace the uplift-blend step with a learned policy). It also speaks concretely to Q6 (the Conservative-OPEstimator is a rare validated example of an offline evaluator whose policy ranking was confirmed against real online outcomes) and, more weakly, to Q3 (session-level horizon with a discount factor, but no delayed multi-day label or censoring handling — the survey's 7-30-day retention horizon and multi-week revenue horizon are both considerably longer and not addressed here). It does **not** address Q2 (credit assignment stays item-level/same-session; no delayed user-level outcome is distributed across items), Q5 (no uplift/incrementality anywhere — pure predicted-outcome optimization), or Q7 (no two-sided, reciprocal, or congestion treatment). The reward-seesaw finding (over-weighting one behavior type harms another) is directly relevant to the survey's "success paradox" constraint, since it is a concrete, measured example of two engagement objectives trading off against each other inside a single learned policy.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2019_WWW_Value-based-RL_Reinforced-Profit-Maximization-Ecommerce.md](./2019_WWW_Value-based-RL_Reinforced-Profit-Maximization-Ecommerce.md) | Related Work / Experiments | Names this paper's method (`BatchRL-MTF`) |
| [2025_WWW_xMTF_Formula-Free-Reinforcement-Learning-Multi-Task-Fusion.md](./2025_WWW_xMTF_Formula-Free-Reinforcement-Learning-Multi-Task-Fusion.md) | Related Work / Experiments | Names this paper's method (`BatchRL-MTF`) |

_2 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `BatchRL-MTF` across all 133 cards._

## Meta Information

- **Authors:** Qihua Zhang, Junning Liu, Yuzhuo Dai, Yiyan Qi, Yifan Yuan, Kunlun Zheng, Fan Huang, Xianfeng Tan
- **Affiliation:** Tencent Inc. (Shenzhen / Beijing, China)
- **Venue:** KDD '22 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- **Year:** 2022
- **Relevance:** Core — named seed reference, one of the survey's most important papers
- **Priority:** 1
- **NLM source:** nlm:b0d40032-08a0-4c62-ad6b-c138b9a2649d
