# Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching

**Source:** https://arxiv.org/pdf/2602.15752.pdf | **NLM source id:** 54b047fc-b81a-40d6-84fd-d935a35cf0b2 | **Year / venue:** 2026, ICLR (arXiv 2602.15752) | **Affiliation:** Hanjuku-kaso, Co., Ltd. (Yuta Saito et al.) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
On two-sided matching platforms (online dating, recruiting), match-maximizing ranking concentrates matches on already-popular users while under-served users churn; fairness-of-exposure objectives are only a heuristic proxy for retention, not the real goal. The paper formally defines the problem of directly maximizing two-sided user retention and proposes **MRet** (Matching for Retention), a dynamic Learning-to-Rank algorithm. **Unit of "credit":** per candidate item/user y recommended to a receiving user x at each time step — this is a ranking/allocation score, not attribution/credit for a past event. **Outcome optimized:** user retention probability f(x, m), a concave function of cumulative match count m (personalized per user via context features, fit with XGBoost or cluster-based regression); retention is defined as logging in again the following month. **Bias handling:** none in the causal-attribution sense — MRet is a forward-looking allocation policy, not a method for attributing an observed retention outcome back to which past interaction caused it. It reduces the NP-hard joint (receiver + candidate) retention-gain maximization to a tractable O(N log N) per-item score via Jensen-type and concavity-based lower bounds.

## 2. Evidence
Synthetic experiment (1000 users/side, K=5, T=2000 steps, popularity skew κ, 10 seeds): MRet reaches ~62.5% retention vs ~55% for Max Match/Uniform and ~58.5% for FairCo, using only ~70% of the matches Max Match uses (~2.2 vs ~3.1 matches/user). Real-world data from a large Japanese online dating platform (1000x1000 match matrix via ALS imputation; separate 60k-record dataset with Feb→Mar 2025 login retention labels; T=3000 steps): under sparse matching, FairCo/Uniform fail (~52–55% retention); Max Match reaches ~63.5% retention with ~6 matches/user; MRet achieves ~66.5% retention (oracle MRet-best: ~67.5%) using only ~4.8 matches/user. Baselines: Max Match, Uniform, FairCo (Morik et al. 2020), MRet-best (oracle), and an exact NP-hard Optimal search on a small-scale setting (confirms MRet's lower-bound approximation is nearly identical to exact optimum).

## 3. Limitations
Assumes the match-probability matrix r(x,y) is given/pre-estimated rather than jointly learned online; retention functions f are fit offline from historical data rather than updated online with exploration-exploitation; treats both sides of the platform as equally weighted in retention, whereas real platforms may prioritize one side (e.g., paying users); real-world retention curves may not be strictly concave (though MRet is shown empirically robust to this).

## 4. Prior works named
- Morik et al. (2020) — *Controlling fairness and bias in dynamic learning-to-rank* (SIGIR '20) — dynamic LTR / FairCo, directly extended by MRet
- Pizzato et al. (2010) — *RECON: A reciprocal recommender for online dating* (RecSys '10)
- Singh & Joachims (2018) — *Fairness of exposure in rankings* (KDD '18)
- Wu et al. (2017) / Zou et al. (2019) — long-term engagement / RL for long-term engagement optimization
- Tomita & Yokoyama (2024) / Su et al. (2022) — doubly-stochastic-matrix formulations of two-sided matching, critiqued as computationally prohibitive for dynamic LTR

## 5. Project Relevance
- **Answers:** Q2 (partly — see below); not Q1
- **Attributes retention to individual interactions?** no — MRet is a forward-looking allocation/ranking policy driven by a learned retention-vs-match-count curve, not a backward-looking credit-assignment method over realized swipes/matches.
- **Transferable components:** the concave personalized retention curve f(x, m) as a reward shape for a credit/reward function; the two-sided retention-gain framing (crediting the value to both the swiper and the candidate); cluster/feature-based retention regression as a lightweight way to estimate the shape of f.
- **Required changes:** replace the ranking-time argsort with a true post-hoc sequence attribution architecture (e.g., sequence models, Shapley-style credit) over heterogeneous event types; move from a scalar cumulative-match count and monthly login label to a daily-recurring N7 target with time-aware/temporal modeling of swipe→match→message sequences.
- **On last-touch:** not discussed — comparison baselines are Max Match, Uniform, and FairCo; no mention of last-touch/last-click attribution.
- **Transfer rating:** adaptable — the retention-curve concept and two-sided gain framing are directly reusable as reward-shape priors, but the method itself is a ranking policy, not an attribution/credit-assignment technique.
