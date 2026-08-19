# Paper Analysis: DRN: A Deep Reinforcement Learning Framework for News Recommendation

**Source:** https://doi.org/10.1145/3178876.3185994  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** DRN: A Deep Reinforcement Learning Framework for News Recommendation  
**Authors:** Guanjie Zheng; Fuzheng Zhang; Zihan Zheng; Yang Xiang; Nicholas Jing Yuan; Xing Xie; Zhenhui Li  
**Abstract:** DRN uses a dueling deep Q-network to plan future news clicks, augments click feedback with user-return patterns, and adds exploration for diversity in a rapidly changing catalog.  
**Methodology:** State encodes users/context/news; dueling Q separates state value and action advantage; user-activeness features capture return frequency; exploration includes DQN-based gradient perturbation.  
**Main results:** Six-month offline and one-month production experiments significantly improved accuracy and diversity. Exact lift values are Not specified in the inspected indexed passages; best reported intra-list similarity is 0.1216 for the full method.

## 2. Experiment Critique

**Design:** 541,337 users/1,355,344 news offline, 64,610 users/157,088 news online; LR, FM, Wide&Deep, bandit, and DQN baselines.  
**Statistical validity:** Exact uncertainty/significance values are Not specified.  
**Online experiments:** One-month commercial news-app deployment.  
**Reproducibility:** Proprietary dataset.  
**Overall:** Early evidence that return behavior can supplement click rewards, but retention is not directly optimized and the reward horizon is unclear.

## 3. Industry Contribution

**Deployability:** Production-tested.  
**Problems solved:** Dynamic catalog/interests, myopic clicks, low diversity.  
**Engineering cost:** Dueling DQN, frequent updates, activeness modeling, exploration.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Future-aware DQN news recommendation with return-pattern feedback and diversity exploration.  
**Prior work comparison:** Contrasts supervised CTR models and online bandits.  
**Verification:** Indexed content only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Commercial news app | Not specified in source. | No | Six-month offline, one-month online. |

**Offline experiment reproducibility:** Not specified.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D2  
**Problem setting:** Dynamic online news recommendation.  
**Objective and label definition:** Long-run click reward with user-return activeness as supplemental feedback; exact return horizon/delay/censoring Not specified.  
**Prediction or incrementality:** Outcome optimization, not incremental exposure effect.  
**Model architecture:** Dueling deep Q-network with activeness and exploration modules.  
**Credit assignment:** Q-learning future return across interactions; no identified item-level retention attribution.  
**Training data and counterfactual handling:** Historical/live clicks and requests; no propensity correction specified.  
**Offline and online evaluation:** Six-month offline and month-long live evaluation.  
**Reported gains:** Significant accuracy/diversity improvements; exact lift Not specified.  
**Unverified claims:** Retention and revenue impact absent.

## Project Relevance

**Low project relevance.** The paper shows a return-pattern auxiliary signal and future-aware policy, but optimizes clicks/news engagement, not delayed retention or revenue. It lacks reciprocity, congestion, interference, uplift, and positive-churn treatment.

**Applicability note:** Historical foundation for adding return behavior and exploration to a recommender policy.  
Too indirect to guide a unified reciprocal dating LTV ranker without newer methods.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Guanjie Zheng et al.  
**Affiliations:** Microsoft Research Asia; Pennsylvania State University  
**Venue:** WWW  
**Year:** 2018  
**PDF:** Indexed from DOI source  
**Relevance:** Related  
**Priority:** 1
