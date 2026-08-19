# Paper Analysis: KuaiSim: A Comprehensive Simulator for Recommender Systems

**Source:** https://arxiv.org/abs/2309.12645
**Date analyzed:** 2026-08-17
**Workplace:** cursor-grok

## Survey Card

- **title:** KuaiSim: A Comprehensive Simulator for Recommender Systems
- **authors or company:** Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai (City University of Hong Kong / Kuaishou Technology)
- **venue:** NeurIPS (arXiv 2309.12645)
- **year:** 2023
- **URL:** https://arxiv.org/abs/2309.12645
- **source type:** academic paper with industry co-authorship (Kuaishou)
- **direction:** D2
- **problem setting:** RL recommender simulator supporting three nested task levels—request-level list-wise ranking, whole-session sequential RL, and cross-session retention optimization—built from KuaiRand-Pure short-video logs (27,077 users, 7,551 items, 1.44M interactions, 246,738 sessions) with portability demo on MovieLens-1M.
- **objective and label definition:** Simulator environment, not a single ranker objective. Cross-session level: return day Y(R) ∈ {1,…,10} days (Geometric(p_ret) with D=10 cap) and binary user-retention ratio; immediate feedback includes click/like/comment/follow/forward/hate; leave signal ends session when user temper drops below threshold.
- **prediction or incrementality:** Prediction/simulation only—User Retention Module predicts next-day return probability p_ret = personal bias + λ₁·session immediate reward + global bias; no causal incrementality or treatment-effect estimation.
- **model architecture:** Three chained modules (Algorithm 1): (1) User Immediate Response Module—Transformer over profile+history, DNN behavior attention, item-correlation diversity penalty; (2) User Leave Module—temper depletes by immediate reward; (3) User Retention Module—p_ret combines personal DNN bias, response bias proportional to session total immediate reward, and global bias fit to geometric return-time distribution.
- **credit assignment:** Session-level only: response retention bias attributes return probability to aggregate session immediate reward, not to individual impressions; no item-level delayed-outcome credit assignment.
- **training data and counterfactual handling:** All three modules pretrained by supervised binary cross-entropy on KuaiRand-Pure (random-exposure "unbiased" logs) and ML-1m; RL agents trained via online interaction with fitted simulator; users sampled from dataset during simulation (no separate user generator).
- **offline and online evaluation:** All evaluation inside simulator—no live online A/B. Cross-session benchmarks (Table 5, 5 runs mean±std): RLUR return day 3.481±0.010 / user retention 0.607±0.002 vs TD3 3.556±0.010 / 0.581±0.001 vs CEM 3.573±0.012 / 0.572±0.002. Simulator fidelity (Table 6): KuaiSim click-response AUC 0.7234±0.0021 vs next-best VirtualTaobao 0.6866±0.0014 (p<0.05).
- **reported gains:** See offline/online eval above; request-level ListCVAE best max L-reward 4.042±0.001; whole-session HAC best total reward 10.1742±0.0634.
- **applicability note for a two-sided dating recommender:** Three-level request/session/retention hierarchy is a useful template for modeling delayed engagement, but KuaiSim is single-sided (viewer vs passive catalog)—no reciprocity, congestion, or bilateral matching constraints.
- **applicability note for a two-sided dating recommender:** **Circular retention risk:** the retention module's response bias is proportional to the same immediate-reward signal RL policies optimize, so higher session reward mechanically raises simulated return probability by construction—KuaiSim retention gains (e.g., RLUR vs TD3) compare policies inside one fixed behavioral model, not independently validated real DAU/retention lifts.
- **unverified claims:** Claim that KuaiSim "excels in approximating real-world environments" rests on aggregate click-response AUC and in-simulator RL metrics only; retention module individual-level predictive accuracy against held-out real return days is not separately reported.

## 1. Summary

**Title:** KuaiSim: A Comprehensive Simulator for Recommender Systems
**Authors:** Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai
**Abstract:** Proposes a comprehensive RL simulator with multi-behavior immediate feedback, session leave modeling, and cross-session retention (return-day) simulation at three task levels, pretrained on KuaiRand-Pure and demonstrated on ML-1m, with benchmarks against RecoGym, RecSim, RL4RS, and VirtualTaobao.

**Key contributions:**
- Three-level simulator (request / whole-session / cross-session) with evaluation protocols and baseline algorithms.
- User sampling from real logs (no separate user generator) and supervised pretraining of response modules.
- Comparative simulator-fidelity analysis on KuaiRand.

**Methodology:** Chained UIRM + leave + retention modules (Algorithm 1); RL baselines include ListCVAE, HAC, RLUR, TD3, CEM across three task levels.

**Main results:** KuaiSim statistically significantly outperforms four prior simulators on click-response AUC; RLUR best on cross-session retention metrics inside KuaiSim.

## 2. Experiment Critique

**Design:** Five-run averages with standard deviations reported for benchmark tables; simulator comparison uses DDPG-trained agents across simulators.

**Statistical validity:** Two-sided t-test p<0.05 for KuaiSim vs best baseline in Table 6; retention predictive accuracy not isolated.

**Online experiments (if any):** None—all results are in-simulator.

**Reproducibility:** Code released (github.com/Applied-Machine-Learning-Lab/KuaiSim); KuaiRand-Pure and ML-1m public.

**Overall:** Strong simulator engineering contribution; retention signal is synthetic and partially circular with immediate-reward optimization.

## 3. Industry Contribution

**Deployability:** Pre-online verification environment for RL recommenders at Kuaishou scale; not a production ranker.

**Problems solved:** Offline RL evaluation gap for multi-behavior, session, and retention tasks without live A/B.

**Engineering cost:** Pretraining three modules on logs; hyperparameter search documented in Appendix B.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Only simulator supporting request-level, whole-session, and cross-session tasks on real data (Table 1).

**Prior work comparison:** vs RecoGym, RecSim, RL4RS, VirtualTaobao—adds retention module and cross-session task; cites RLUR as cross-session SOTA baseline.

**Verification:** Table 6 fidelity comparison supports immediate-feedback module; retention module validation limited to distributional fit.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| KuaiRand-Pure | https://kuairand.com/ | Yes | 27,077 users, 7,551 items, 1.44M interactions |
| MovieLens-1M | https://grouplens.org/datasets/movielens/1m/ | Yes | Portability demo |

**Offline experiment reproducibility:** Code and public datasets support reproduction of simulator benchmarks.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Simulator for RL policy evaluation, not a ranking objective—provides retention/return-day as cross-session reward signal.

**(2) Credit assignment:** Session-aggregate immediate reward feeds retention bias; no per-impression delayed retention attribution.

**(3) Label and horizon definitions:** Return day ~ Geometric(p_ret), capped at 10 days; multi-behavior immediate labels; KuaiRand random-exposure for unbiased offline pretraining.

**(4) Short-term + long-term heads:** Chained modules separate immediate response, session leave, and cross-session retention—not a unified ranking head fusion.

**(5) Prediction vs incrementality:** Simulates outcomes; does not estimate incremental effect of exposures.

**(6) Offline and online evaluation:** Simulator-only benchmarks; no production A/B; retention comparisons are internal to KuaiSim's learned MDP.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Single-sided short-video domain; fairness/diversity explicitly listed as future work in limitations.

**(8) Migration path from CTR-like model to unified long-term model:** Not specified—KuaiSim is an evaluation environment, not a migration path for production rankers.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Kesen Zhao, Shuchang Liu, Qingpeng Cai, Xiangyu Zhao, Ziru Liu, Dong Zheng, Peng Jiang, Kun Gai
**Affiliations:** City University of Hong Kong; Kuaishou Technology
**Venue:** NeurIPS 2023
**Year:** 2023
**PDF:** https://arxiv.org/pdf/2309.12645.pdf
**Relevance:** Related
**Priority:** 4
