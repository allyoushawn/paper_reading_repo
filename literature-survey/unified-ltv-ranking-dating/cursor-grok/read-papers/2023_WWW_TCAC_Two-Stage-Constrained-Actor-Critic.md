# Paper Analysis: Two-Stage Constrained Actor-Critic for Short Video Recommendation

**Source:** https://arxiv.org/pdf/2302.01680.pdf  
**Date analyzed:** 2026-08-16

## Survey Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Two-Stage Constrained Actor-Critic for Short Video Recommendation; Qingpeng Cai, Zhenghai Xue, Chi Zhang, Wanqi Xue, Shuchang Liu, Ruohan Zhan, Xueliang Wang, Tianyou Zuo, Wentao Xie, Dong Zheng, et al. (Kuaishou); WWW 2023; https://arxiv.org/pdf/2302.01680.pdf |
| 2 | Source type | Industry paper |
| 3 | Direction | D2 |
| 4 | Problem setting | Short-video CMDP: maximize cumulative WatchTime while balancing sparse interaction signals (Like, Follow, Share, Comment, Hate); dense WatchTime overwhelms sparse signals in joint reward models. |
| 5 | Objective and label definition | Main: long-term cumulative WatchTime r_1; auxiliaries: Click, Like, Comment, Hate, Follow, Share, etc.; horizon = user session; γ≈0.99 offline, 0.95 production; WatchTime dense per view, interactions sparse; hate extremely sparse. Retention/LTV/revenue not specified as direct objectives. |
| 6 | Prediction or incrementality | Policy-value optimization (expected cumulative WatchTime under constraints); not causal incrementality at training time. |
| 7 | Model architecture | Multi-critic actor-critic: Stage 1 separate actor/critic per auxiliary response; Stage 2 main WatchTime actor regularized via KL to auxiliary policies with closed-form product-of-policies solution. |
| 8 | Credit assignment | Step-level vector reward r_t(s_t,a_t) at each recommendation; standard Bellman TD credit over session—not explicit user-level delayed outcome → item attribution beyond immediate feedback. |
| 9 | Training data and counterfactual handling | Offline: logged trajectories with NCIS evaluation; importance-sampling first-order correction vs behavior policy π_β; compared to RCPO, Pareto, supervised Wide&Deep/DeepFM/LTR. |
| 10 | Offline and online evaluation | Offline: KuaiRand (NCIS, DCG), TripAdvisor; online A/B on Kuaishou short-video app vs production LTR baseline. |
| 11 | Reported gains | KuaiRand WatchTime NCIS 13.14 vs BC 12.85 (+2.23%); Like +18.80%, Comment +15.6% vs BC; online vs LTR: WatchTime +0.379%, Share +3.376%, Download +1.733%, Comment −0.619%. |
| 12 | Applicability to a two-sided dating recommender | Two-stage constrained fusion of dense engagement (time-on-app) with sparse match/super-like signals mirrors dating’s watch-time vs match-rate tension; KL soft constraints avoid hand-tuned Lagrangian grids. One-sided; no reciprocity or match-market balance. |
| 13 | Unverified claims | λ sensitivity: too small or too large λ hurts both main and auxiliary metrics; universal online Comment drop across all RL methods attributed to WatchTime–Comment trade-off. |

## 1. Summary

**Title:** Two-Stage Constrained Actor-Critic for Short Video Recommendation  
**Authors:** Qingpeng Cai et al. (Kuaishou)  
**Venue:** WWW 2023

**Abstract (from source):** Short-video platforms receive dense WatchTime and sparse interaction feedback. Naive constrained RL (RCPO with summed rewards) fails because dense signals dominate sparse ones and multi-dimensional Lagrangian search is costly. TSCAC learns separate critics and stage-one policies per auxiliary signal, then softly constrains the main WatchTime policy to stay near them via KL regularization with a closed-form optimal policy.

**Key contributions:**
- CMDP formulation for short-video recommendation.
- Multi-critic policy estimation with response-specific discount factors.
- Two-stage actor learning with theoretical closed-form Lagrangian solution.
- Full production deployment on Kuaishou.

**Methodology:** Stage 1: train π_{θ_i}, V_{φ_i} per auxiliary via A2C-style updates. Stage 2: optimize main WatchTime policy with actor update using product of auxiliary policy probabilities weighted by λ_i and main advantage. Offline IS correction; deterministic extension for continuous preference embeddings.

**Main results:** Best WatchTime and most auxiliaries on KuaiRand and TripAdvisor offline; online beats LTR on WatchTime and interactions while all RL methods reduce Comments.

## 2. Experiment Critique

**Design:** Comprehensive offline baselines including RCPO, RCPO-Multi-Critic, Pareto, BC, supervised models; separate TripAdvisor generalization; online bucket test vs production LTR.

**Statistical validity:** Authors state +0.1% WatchTime and +1% interaction lifts are statistically significant on platform; offline percentages vs BC reported.

**Online experiments:** Multi-day training then fixed-policy evaluation; RCPO and Interaction-AC ablations included.

**Reproducibility:** KuaiRand public; TripAdvisor public; production logs not public.

**Overall:** Honest about Comment trade-off and λ tuning difficulty; RCPO single-critic failure on sparse Hate validates multi-critic design.

## 3. Industry Contribution

**Deployability:** Fully launched on popular short-video platform; deterministic Gaussian policy in live setting with dot-product ranking.

**Problems solved:** Multi-response optimization when observation frequencies and discount needs differ; avoids grid search over many Lagrangian multipliers.

**Engineering cost:** Multiple critics and two-stage training; equal λ across constraints in production (fine-tuning could improve further).

## 4. Novelty vs. Prior Work

**Claimed novelty:** Two-stage soft constraint vs standard RCPO; separate evaluation for dense/sparse responses; closed-form multi-constraint policy.

**Prior work named in source:**
- Tessler et al., RCPO (2018).
- Sutton & Barto, RL textbook (2018).
- Chen et al., multi-aspect preference / Pareto RL (WWW 2021).
- Ge et al., long-term fairness in recommendation (2021).
- Chen et al., tree-structured policy gradient (AAAI 2019).
- Zhao et al., pairwise DRL with negative feedback (KDD 2018).
- Zou et al., long-term user engagement RL (KDD 2019) — NCIS methodology.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| KuaiRand | https://kuairand.com/ | Yes | 26,858 users, 68M+ samples |
| TripAdvisor reviews | Public academic set | Yes | 20,277 customers, 150 hotels |
| Kuaishou production logs | Proprietary | No | Live A/B |

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

Strong **Q4** reference: fuses dense session engagement (WatchTime) with sparse interaction heads via two-stage policy constraint rather than scalar reward sum. **Q1** optimizes cumulative WatchTime, not CTR alone. **Q8** documents LTR → TSCAC migration on production. Weak on **Q2** item-level delayed credit beyond step rewards; no **Q7** two-sided fairness/reciprocity.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| *(To be filled in during Phase 3.7)* | | |

## Meta Information

- **Authors:** Qingpeng Cai et al.
- **Affiliations:** Kuaishou
- **Venue:** WWW 2023
- **Year:** 2023
- **Relevance:** Core
- **Priority:** 1
- **Workplace:** cursor-grok
- **nlm:** 7b46f4f0-1894-4ce7-a0e3-603669e259f8
