# Stratified Expert Cloning for Retention-Aware Recommendation at Scale

**Source:** https://arxiv.org/html/2504.05628v2 | **NLM source id:** 3428b363-efef-4206-9892-dcc167d97303 | **Year / venue:** CIKM 2025, Seoul | **Affiliation:** Kuaishou Technology, Peking University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
RL for retention is delayed, sample-inefficient, and costly to explore in production; plain behavior cloning (BC) collapses recommendation diversity and treats retention as binary. SEC is an imitation-learning framework: it stratifies high-retention "expert" users into K hierarchical retention tiers (e.g., by active-day quantiles), trains a separate cloning policy per tier, and at inference dynamically matches each user to the most appropriate expert tier (bounded by a historical-retention floor) rather than cloning power users onto everyone. **Unit of credit:** per recommendation action/policy assignment — SEC clones state-action sequences, it does not compute fractional attribution labels. **Outcome optimized:** long-term retention, measured as active days in a 7-day window / return time. **Bias handling:** multi-level stratification plus an inference-time constraint that matches users to reachable expert levels prevents forcing power-user policies onto low-activity users (the platform's core selection-bias concern), and Action Entropy Regularization (nuclear-norm maximization) prevents policy collapse onto popular items.

## 2. Evidence
Offline: KuaiRand-Pure + KuaiSim simulator, vs. TD3, SAC, DIN, CEM, RLUR, GFN4Retention. SEC gets the best offline return time (1.411 days vs. GFN's 1.496, a 5.7% reduction) and click/long-view rate improvements, at the cost of an 8.9% lower like rate than GFN. Live A/B on Kuaishou and Kuaishou Lite (200M+ DAU, 10% traffic, 2+ weeks): cumulative active-days lift of +0.098% (Kuaishou) and +0.122% (Kuaishou Lite), reported as >200,000 additional DAU per platform; valid interest-cluster expansion +1.31%/+1.14%.

## 3. Limitations
Requires a large, diverse pool of high-retention expert users — unsuitable for cold-start or nascent platforms. Adaptive expert selection depends on rich user-state representations, so new/sparse users get poor expert matches. Optimizing long-term retention traded off against immediate satisfaction (like rate -8.9% vs. GFN). Tested only on short-video platforms; generalization to other domains (e.g., e-commerce, dating) is unverified.

## 4. Prior works named
- Cai et al. (2023) — RLUR: Reinforcing User Retention in a Billion Scale Short Video Recommender System (baseline)
- Liu et al. (2024) — GFN4Retention: Modeling User Retention through Generative Flow Networks (state-of-the-art baseline)
- Zhao et al. (2023) — User Retention-oriented Recommendation with Decision Transformer (DT4Rec)
- Pomerleau (1991) / Ross et al. (2011) — foundational behavior cloning
- Schaeffer et al. (2024) — Maximum Manifold Capacity Representations (inspired the entropy regularizer)

## 5. Project Relevance
- **Answers:** neither directly — SEC is a policy-cloning method, not an attribution or industry-attribution paper (weakly Q2-adjacent by exclusion).
- **Attributes retention to individual interactions?** No — SEC clones expert state-action trajectories via behavior-cloning loss; it never isolates or scores the marginal contribution of an individual swipe/action.
- **Transferable components:** multi-level retention/activity stratification (mirrors the platform's own engaged-vs-casual user segmentation); Action Entropy Regularization to prevent the ranker from collapsing onto a narrow candidate set.
- **Required changes:** SEC would need to be replaced by, or paired with, an explicit credit-assignment layer (e.g., a causal/counterfactual model or attention-weight extraction) since it only clones policies; it also treats actions homogeneously and optimizes a fixed 7-day window rather than rolling daily N7 labels, so funnel-stage (swipe→match→conversation) modeling and rolling time-decay would need to be added.
- **On last-touch:** Not discussed — the paper compares against RL/GFN baselines on immediate-vs-long-term optimization, not attribution heuristics.
- **Transfer rating:** background — useful for the stratification and diversity-regularization ideas, but it is not itself an attribution mechanism and cannot directly produce per-swipe fractional credit.
