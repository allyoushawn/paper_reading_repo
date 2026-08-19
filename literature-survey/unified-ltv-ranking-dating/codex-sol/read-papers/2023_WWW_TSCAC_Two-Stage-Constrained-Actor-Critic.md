# Paper Analysis: Two-Stage Constrained Actor-Critic for Short Video Recommendation

**Source:** https://arxiv.org/pdf/2302.01680  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Two-Stage Constrained Actor-Critic for Short Video Recommendation  
**Authors:** Qingpeng Cai; Zhenghai Xue; Chi Zhang; Wanqi Xue; Shuchang Liu; Ruohan Zhan; Xueliang Wang; Tianyou Zuo; Wentao Xie; Dong Zheng; Peng Jiang; Kun Gai  
**Abstract:** TSCAC maximizes cumulative watch time while constraining sparse auxiliary feedback such as likes, comments, follows, shares, and hates. It first trains separate auxiliary policies/critics, then trains the main policy with soft proximity constraints to those policies.  
**Key contributions:** Multi-critic evaluation with response-specific discounting; two-stage actor learning; production deployment.  
**Methodology:** A constrained MDP uses recommendation actions and vector feedback. Stage one learns one policy per auxiliary. Stage two maximizes the main watch-time critic while regularizing its actions toward auxiliary-optimal policies.  
**Main results:** On KuaiRand, TSCAC achieved 13.14 watch time (+2.23% over behavior cloning), with +4.35% click, +18.80% like, +15.6% comment, and −18.83% hate. It also significantly outperformed RCPO in live experiments, but exact live lifts are Not specified in the indexed passages.

## 2. Experiment Critique

**Design:** KuaiRand offline RL with 26,858 users, 10,221,515 items, 68,148,288 samples, and five responses; live comparison to the existing learning-to-rank baseline and RCPO.  
**Statistical validity:** Offline significance markers and live significance statements are present; A/B duration/sample size are Not specified.  
**Online experiments:** Production live test and full launch; exact gains Not specified.  
**Reproducibility:** KuaiRand is public; production environment is not.  
**Overall:** Supports constrained multi-objective RL under sparse signals, but the optimized horizon is cumulative session engagement rather than retention/LTV.

## 3. Industry Contribution

**Deployability:** Fully launched at Kuaishou.  
**Problems solved:** Prevents dense main signals from overwhelming rare auxiliary behaviors and avoids expensive multiplier search.  
**Engineering cost:** One critic/policy per response plus second-stage constrained policy and RL infrastructure.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Two-stage multi-critic constrained RL for heterogeneous sparse recommendation feedback.  
**Prior work comparison:** Contrasts RCPO/Lagrangian constraints, Pareto optimization, supervised rankers, and unconstrained recommendation RL.  
**Verification:** Indexed paper content only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| KuaiRand | https://kuairand.com/ | Yes | Unbiased short-video interactions; top 150 videos used for trajectories. |
| Kuaishou production logs | Not specified in source. | No | Live experiment. |

**Offline experiment reproducibility:** Partly reproducible on KuaiRand; complete code/hyperparameters Not specified.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D2  
**Problem setting:** Sequential short-video recommendation with one main and multiple sparse auxiliary objectives.  
**Objective and label definition:** Discounted cumulative watch time subject to interaction-response constraints; no retention/revenue horizon, delayed-label, or censoring definition.  
**Prediction or incrementality:** Outcome optimization, not incremental exposure-effect estimation.  
**Model architecture:** Multiple actor-critic policies/critics followed by a main actor regularized toward auxiliary actors.  
**Credit assignment:** MDP discounted returns assign cumulative response value to actions; no causal exposure attribution.  
**Training data and counterfactual handling:** Logged trajectories and live learning; explicit propensity correction is Not specified.  
**Offline and online evaluation:** KuaiRand plus live Kuaishou experiments.  
**Reported gains:** Offline gains above; exact online gains Not specified.  
**Unverified claims:** None beyond indexed content.

## Project Relevance

**Low project relevance.** The source does not directly optimize retention or revenue. Its useful contribution is architectural: separate critics preserve rare signals, while second-stage soft constraints prevent a dominant objective from erasing like/match/conversation quality.

**Survey inference:** A dating version could make long-horizon value the main critic and use like, match, conversation, mutual-quality, and fairness policies as constraints. That extension still needs delayed rewards, causal logging, reciprocal actions, congestion constraints, interference-aware tests, and protection against successful-match churn.

**Applicability note:** Useful constraint machinery for keeping sparse dating cascade signals alive under a long-term main objective.  
Not evidence for retention/revenue optimization or uplift by itself.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Qingpeng Cai et al.  
**Affiliations:** Kuaishou Technology; Hong Kong University of Science and Technology  
**Venue:** WWW  
**Year:** 2023  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
