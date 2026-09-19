# From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation

**Source:** https://arxiv.org/pdf/2608.10182.pdf | **NLM source id:** 471fd316-4d94-413c-ba4e-ed61b92956ac | **Year / venue:** 2026, arXiv 2608.10182 | **Authors / affiliation:** Changshuai Wei, John Bencina, Phuc Nguyen, Andre Assuncao Silva T Ribeiro, Benjamin Zelditch — all LinkedIn (Seattle/Sunnyvale, USA) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Predictive targeting (rank by CTR/CVR) systematically misallocates marketing/notification spend to users who would act anyway. The paper proposes a decision-centric framework that jointly optimizes causal effects under global constraints: (1) an "Incrementality Transformer" — a Transformer backbone over touchpoint sequences feeding a DragonNet causal head that jointly predicts outcome-under-treatment, outcome-under-control, and propensity, plus CLIP-inspired outcome embeddings for cold-start/multi-product scoring; (2) "DragonBandit," a neural Thompson-sampling layer (Linearized Laplace Approximation) for uncertainty-aware exploration that prevents feedback-loop bias; (3) "ECLIPSE," a dual-decomposition LP solver for constrained allocation across tens of millions of users.
**Unit of credit:** per user-action allocation (user × campaign/business-line per round), not per-touch fractional credit. **Outcome optimized:** incremental impact (CATE/ITE) on long-term value (LTV) and conversion, under budget/volume/frequency constraints. **Bias handling:** DragonNet's propensity head acts as an architectural regularizer preventing the shared encoder from discarding propensity signal (propensity sufficiency); targeted regularization via the efficient-influence-function (TMLE clever covariate) gives Neyman-orthogonal CATE estimates; an explicit "no-recommendation" withhold action filters out predicted organic converters; randomized snapshot run-dates in training-log construction explicitly avoid last-touch labeling and preserve variable-length history; neural-bandit exploration expands causal overlap to counter feedback-loop/selection bias from the logging policy.

## 2. Evidence
- **Offline:** Open Bandit Dataset (~400K users, 34 products mapped to 4 business lines + no-rec action). Incremental+Constrained-Opt achieves avg net return $0.46±0.13 vs. $0.39±0.18 (Propensity+Constrained-Opt), $0.37±0.15 (Incremental+Ranking), $0.31±0.20 (Propensity+Ranking). Incremental+Constrained-Opt assigns 9% of users to no-rec (organic-converter identification) vs. 0% for Propensity+Constrained-Opt.
- **Multi-turn simulation:** Bandit-Incremental model overcomes initial logging bias and outperforms greedy variants after ~50 online learning rounds (short-term exploration cost, long-term gain).
- **Online A/B test:** 8-week test on LinkedIn Feed marketing traffic (50/50 split, tens of millions of users) vs. production two-tier BAU (propensity retrieval + propensity ranking) stack: statistically significant **+7.20% lift in LTV** (p=0.041, 95% CI [0.31%, 14.09%]).

## 3. Limitations
- Removing dense features lowers outcome AUROC (0.857→0.826) but is neutral/beneficial for uplift AUUC — dense features behave as prognostic (not treatment-effect) modifiers, adding variance to the shared DragonNet representation; authors call this a hypothesis, not an automated fix.
- Outcome-embedding cold-start diagnostic (CLIP-style) tested only on 9-of-10 held-out products with synthetic sampled embeddings — does not establish real zero-shot production effectiveness for genuinely new product launches.
- Exploration policy underperforms its greedy counterpart in the first ~1–25 online-learning rounds before it pays off.
- Framework needs joint tuning across multiple loss terms (outcome, propensity, targeted-regularization, reconstruction); shared-encoder feature sensitivity remains a limitation.

## 4. Prior works named
- Shi, Blei & Veitch (2019) — DragonNet: *Adapting Neural Networks for the Estimation of Treatment Effects*
- Basu, Ghoting, Mazumder & Pan (2020) — ECLIPSE extreme-scale LP solver
- Daxberger et al. (2021) — Laplace Redux (Linearized Laplace Approximation for neural Thompson sampling)
- Shalit, Johansson & Sontag (2017) — TARNET, generalization bounds for ITE estimation
- van der Laan & Rubin (2006) / Chernozhukov et al. (2018) — TMLE / Double/debiased machine learning (EIF-based targeted regularization)

## 5. Project Relevance
- **Answers:** Q1 (latest industry attribution/causal-targeting approach, 2026, LinkedIn production).
- **Attributes retention to individual interactions?** No — estimates user-level CATE for marketing-campaign allocation under LP constraints; does not do multi-touch sequence attribution or fractional per-interaction retention credit.
- **Transferable components:** Transformer sequence encoder over touchpoints (with days-since/day-of-week/positional embeddings); DragonNet joint outcome+propensity architecture for de-biasing "would have engaged anyway" users; randomized snapshot-date training-log construction to avoid last-touch leakage; explicit counterfactual/no-action baseline; neural-bandit exploration to expand overlap.
- **Required changes:** Move from user-level campaign allocation to per-touch (swipe/like/match/message) fractional credit; extend the touchpoint vocabulary to dating-funnel event types; re-anchor the outcome from LTV/conversion to a recurring daily N7-active binary label evaluated per rolling reference date.
- **On last-touch:** Explicitly states randomizing the training snapshot date "avoids a last-touch label, captures long-term action effects, and preserves variable-length histories" — a direct, named critique of last-touch labeling.
- **Transfer rating:** adaptable — the causal de-biasing and sequence-modeling machinery transfers, but the unit of credit and outcome must be redesigned for per-swipe daily retention.
