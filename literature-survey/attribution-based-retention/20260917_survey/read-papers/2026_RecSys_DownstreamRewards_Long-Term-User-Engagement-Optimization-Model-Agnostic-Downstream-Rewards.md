# Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning

**Source:** https://arxiv.org/html/2607.14192v3 | **NLM source id:** d6f303ed-3a73-4c04-8313-a1af62a453d2 | **Year / venue:** arXiv 2607.14192, accepted RecSys 2026 | **Affiliation:** Pinterest | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Optimizing only immediate engagement creates feedback loops that degrade long-term value and homogenize content; directly optimizing retention labels is hard because returns are sparse, delayed, noisy, and attributing them back to specific earlier recommendations across surfaces is difficult, and full RL is costly and reward-brittle at scale. The paper introduces an offline screening framework (Random Forest + User-Prevalence normalization) to find good proxy signals, then a model-agnostic Downstream Reward (DR) framework combining three reward families (deeper session engagement, negative "shallow closeup" penalties, use-case adoption) as auxiliary prediction heads. **Unit of credit:** per recommended item/Pin — the model predicts the probability an impression triggers a valuable downstream trajectory. **Outcome optimized:** proxy downstream rewards driving DAU/WAU/MAU, Successful Sessions, and time spent. **Bias handling:** User-Prevalence (UP) normalization divides pivot-day action density by impression count and subtracts the user's own median density over the prior two weeks — this is the paper's explicit fix for the "engaged users interact more" selection-bias problem, and it flips shallow clicks/diversity from positive to negative retention indicators once exposure is controlled for.

## 2. Evidence
Real Pinterest production logs across Homefeed, Search, Related Pins, Notifications; offline RF screening model gets AUC 0.65–0.70. Baseline: production TransAct-style multi-head models optimizing immediate engagement. Extensive live A/B (1.5% traffic, 3–4 week holdouts): Homefeed deeper-engagement reward: Successful Sessions +0.36%, time spent +0.10%, downloads/screenshots +0.7%; negative-reward (shallow closeup) variant: Successful Sessions +0.16%, unsuccessful sessions -0.40%, time spent +0.35%; use-case adoption reward: saves +0.42%, downloads +1.28%. Cross-surface: Search fulfillment +0.25%, Related Pins sessions >5min +0.70%, Notifications Successful Sessions +0.14%. Infra (Ray-based DRv2) cut experiment iteration time from ~3 weeks to ~2 days at <5% training overhead.

## 3. Limitations
A uniform shallow-closeup dwell-time threshold failed to produce positive DAU/WAU across all segments, requiring user-state-specific thresholds (core vs. non-core users, and a separate threshold for Related Pins). Public datasets lack the fine-grained session signals (closeups, saves, downloads) needed and could not be used for validation. Use-case adoption rewards depend on upstream interest-cluster embeddings and required manual threshold tuning. The core finding itself is a stated caution: naive unnormalized shallow signals look positively correlated with retention until exposure is controlled for.

## 4. Prior works named
- Xia et al. (2023) — TransAct: Transformer-based realtime user action model (Pinterest's production backbone)
- Wang et al. (2022) — Surrogate for Long-Term User Experience in Recommender Systems
- Sculley et al. (2015) / Chaney et al. (2018) — Hidden technical debt in ML systems / algorithmic confounding and homogeneity
- Cai et al. (2023) / Xue et al. (2025) — RLUR / AURO (RL retention-optimization baselines)
- Bergstra et al. (2013/2015) — HyperOPT

## 5. Project Relevance
- **Answers:** Q1 and Q2 (recent industry practice, 2026; partial per-interaction attribution)
- **Attributes retention to individual interactions?** Partly — proxy downstream rewards score the near-term engagement trajectory triggered by one impression/action, but the paper does not compute explicit offline multi-touch credit allocation (no Shapley values, no counterfactual path masking) across a user's full multi-day history.
- **Transferable components:** User-Prevalence normalization to remove exposure/selection bias (very close to the platform's own "engaged users swipe more" problem); negative rewards for shallow/low-intent actions; discounted downstream-trajectory proxy rewards (swipe→match→message chains); use-case/preference-expansion reward for diversity credit.
- **Required changes:** move from impression-level auxiliary prediction heads to an explicit sequence-attribution mechanism producing fractional credit labels per historical swipe; map the downstream event space onto the dating funnel (left/right swipe, match, message) with event-type weights; re-anchor the outcome to a rolling daily N7 active indicator instead of session continuation.
- **On last-touch:** The paper states directly that "even when downstream outcomes are observed, attributing them to specific earlier recommendations is challenging," and empirically shows that naive/shallow click-based signals flip to negative retention indicators once exposure bias is removed — a direct, recent (2026) argument against naive last-touch-style crediting.
- **Transfer rating:** adaptable — the UP-normalization debiasing technique is the most directly reusable selection-bias fix in this batch, even though the reward framework itself stops short of full sequence attribution.
