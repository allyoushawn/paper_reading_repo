# Paper Analysis: Jointly Learning to Recommend and Advertise

**Source:** https://doi.org/10.1145/3394486.3403384  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Jointly Learning to Recommend and Advertise  
**Authors:** Xiangyu Zhao; Xudong Zheng; Xiwang Yang; Xiaobing Liu; Jiliang Tang  
**Abstract:** RAM is a two-level deep-RL framework for mixed recommendation/advertising lists. Level one selects recommendation items for long-term user experience; level two decides whether, which, and where to insert an ad, balancing immediate ad revenue against engagement harm.  
**Methodology:** Hierarchical DQNs operate on list selection and coupled ad decisions, trained/evaluated in a learned TikTok simulator.  
**Main results:** RAM-l achieved recommendation reward 19.61, advertising reward 9.76, and revenue 1.49; compared with DRQN these are reported improvements of 3.26%, 4.16%, and 16.42%, respectively. No live A/B test is specified.

## 2. Experiment Critique

**Design:** TikTok logs train a response/revenue simulator; comparisons include Wide&Deep, DeepFM, GRU, DRQN, and RAM variants.  
**Statistical validity:** Table reports standard errors and p-values; simulator validity and live effects remain uncertain.  
**Online experiments:** Simulated online environment only.  
**Reproducibility:** Paper says implementation code is released; data access details are Not specified.  
**Overall:** Demonstrates joint revenue/experience control, but evidence is simulator-based and the “long-term” reward is not retention/LTV.

## 3. Industry Contribution

**Deployability:** Architecture is plausible for rec/ads coordination; no production launch stated.  
**Problems solved:** Separately optimized recommender and ads teams causing suboptimal global outcomes.  
**Engineering cost:** Two RL levels, response/revenue simulator, ad auction integration, hierarchical action models.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Joint hierarchical optimization of recommendation list and three coupled ad-insertion decisions.  
**Prior work comparison:** Contrasts hybrid scoring, separate rec/ads optimization, and standard DQN recommenders.  
**Verification:** Indexed paper content only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| TikTok mixed rec/ads logs | Not specified in source. | Not specified | Used to train simulator. |

**Offline experiment reproducibility:** Code reportedly released; data availability Not specified.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D2  
**Problem setting:** Mixed recommendation/advertising slate optimization.  
**Objective and label definition:** Long-term simulated recommendation reward plus immediate advertising revenue; horizon, retention, delay, sparsity, and censoring are Not specified.  
**Prediction or incrementality:** Policy optimization, not uplift/CATE.  
**Model architecture:** Two-level deep Q-network with recommendation and ad-insertion policies.  
**Credit assignment:** Simulator supplies per-step/user-experience and ad-revenue rewards across a trajectory; causal item attribution is absent.  
**Training data and counterfactual handling:** Logged TikTok data plus learned simulator; no propensity correction specified.  
**Offline and online evaluation:** Simulator only.  
**Reported gains:** 3.26% recommendation reward, 4.16% ad reward, and 16.42% revenue versus DRQN.  
**Unverified claims:** Real-world lift and retention effects are Not specified.

## Project Relevance

**Low project relevance.** It is useful for explicitly balancing immediate monetization with longer-term experience in one policy, analogous to subscription/a-la-carte revenue versus match quality. It does not directly model retention, delayed LTV labels, incrementality, reciprocity, congestion, interference, or positive churn.

**Applicability note:** Useful objective-decomposition precedent for revenue versus experience trade-offs.  
Simulator-only evidence and lack of reciprocal-market modeling limit direct dating transfer.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Xiangyu Zhao et al.  
**Affiliations:** ByteDance; Michigan State University  
**Venue:** KDD  
**Year:** 2020  
**PDF:** Indexed from DOI source  
**Relevance:** Related  
**Priority:** 1
