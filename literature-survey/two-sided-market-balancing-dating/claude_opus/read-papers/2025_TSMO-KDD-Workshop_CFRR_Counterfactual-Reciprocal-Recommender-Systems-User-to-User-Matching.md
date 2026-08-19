# Counterfactual Reciprocal Recommender Systems for User-to-User Matching

- **notebook source_id:** `3f25d802`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Reciprocal recommender systems (dating, gaming, talent matching) suffer from exposure bias: historical logging policies over-expose popular users, and naive training on logged data amplifies this into a self-reinforcing feedback loop that hurts both accuracy and fairness. The authors propose Counterfactual Reciprocal Recommender Systems (CFRR), which learns pair-level display propensities and reweights the training objective with Self-Normalized Inverse Propensity Scoring (SNIPS), optionally combined with weight truncation and doubly robust (DR) augmentation. Across a synthetic dataset and two real-world graphs (DBLP-CoAuthor, Epinions-Trust), CFRR-SNIPS improves NDCG@10 by up to 3.5%, expands long-tail user Coverage@10 by up to 51% (0.504 to 0.763 on Synthetic), and cuts Gini-Exposure inequality by up to 24% (0.708 to 0.535 on Synthetic), relative to strong RRS baselines.

## Method
CFRR treats user-to-user recommendation as counterfactual risk estimation under a historical logging (display) policy. For a candidate pair (u,v), the platform's observed display decision O(u,v) is governed by an unknown propensity θ(u,v) = P(O=1|u,v); outcome r(u,v) (e.g., mutual acceptance) is only observed when O=1. The population risk is the expectation over a uniform target distribution over all pairs, but naive loss minimization on displayed pairs is biased toward popular, over-exposed users.
- **Propensity estimation:** a parametric model θ̂(u,v) = σ(g(φ(u), ψ(v); β)) is trained via maximum likelihood on logged exposure (φ, ψ = user features/embeddings; g = e.g. gradient-boosted trees in experiments, LightGBM with 100 estimators).
- **IPS objective:** reweight each observed pair's loss by 1/θ̂(u,v) (Horvitz-Thompson form) to get an unbiased estimate of true population risk (Eq. 2).
- **SNIPS (Self-Normalized IPS):** divide by the sum of weights instead of the pair count (Eq. 4) — reduces variance from extreme/near-zero propensities at the cost of a small finite-sample bias; this self-normalization is described as acting like an implicit regularizer that stabilizes training on high-imbalance, rarely-shown pairs.
- **Variance-reduction extensions:** (1) weight truncation/clipping at threshold c (c=50 in experiments) to cap the influence of tiny-propensity pairs; (2) Doubly Robust (DR) augmentation — a pre-trained outcome model m̂(u,v) estimating E[R(u,v)|u,v] is combined with the SNIPS objective (Eq. 5, "SNIPS-DR") for added robustness when the propensity model is misspecified.
- **Joint propensity learning (Algorithm 1):** alternates between updating recommender parameters Θ via minibatch SGD on the SNIPS/SNIPS-DR loss and updating propensity parameters β via MLE on observed exposure O(u,v), across the logged data D_log.
- Debiased scores s(u,v;Θ*) can then feed downstream top-k recommendation, maximum-weight bipartite matching under capacity constraints, or Gale-Shapley stable matching.

## Datasets and Baselines
**Datasets:** (1) Synthetic — 5K users, 16D latent factors, known ground-truth R(u,v) (sigmoid of latent-factor dot products), tunable exposure bias via popularity-based logging propensity, ~50K logged pairs; (2) DBLP-CoAuthor — up to 10K authors, mutual co-authorship as positive reciprocal interaction, exposure bias arises because prolific/highly-cited authors are over-represented; (3) Epinions-Trust — up to 5K users from Epinions.com, reciprocal match defined as mutual trust, bias arises because highly-trusted "influencer" users are more visible. Negative sampling used for real-world datasets (equal number of non-linked pairs as negatives). Time-based splits for DBLP/Epinions; random 70/10/20 splits for Synthetic. 10 random seeds per configuration; 20 training epochs with early stopping on validation NDCG@10.

**Baselines:** LFRR (latent-factor RRS model, ignores selection bias), CausE (early causal item-recommendation debiasing approach adapted to RRS), IPW-MF (direct IPS applied to matrix factorization for RRS), DICE (disentangles interest from conformity/popularity effects), StableDR (state-of-the-art Stabilized Doubly Robust method, adapted with pair-level propensities and a baseline RRS model's predictions for the DR estimator).

**Metrics:** NDCG@10, MRR (accuracy); Coverage@10 (fraction of users appearing at least once in any other user's top-10 list — higher better); Gini-Exposure (Gini coefficient of the user exposure/recommendation-count distribution — lower better, 0 = perfect equality).

## Results
Table 1 (mean ± std over 10 seeds):

| Dataset | Method | NDCG@10 | MRR | Coverage@10 | Gini-Exposure |
|---|---|---|---|---|---|
| Synthetic | LFRR | 0.299±0.005 | 0.511±0.007 | 0.504±0.003 | 0.708±0.005 |
| Synthetic | **CFRR-SNIPS** | **0.307±0.005** | **0.527±0.007** | **0.763±0.004** | **0.535±0.003** |
| DBLP-CoAuthor | LFRR | 0.459±0.007 | 0.666±0.012 | 0.419±0.023 | 0.688±0.008 |
| DBLP-CoAuthor | **CFRR-SNIPS** | **0.475±0.012** | **0.677±0.016** | **0.449±0.023** | 0.686±0.006 (StableDR best at 0.685) |
| Epinions-Trust | LFRR | 0.468±0.008 | 0.678±0.013 | 0.432±0.025 | 0.695±0.007 |
| Epinions-Trust | **CFRR-SNIPS** | **0.472±0.010** | **0.680±0.016** | **0.448±0.022** | 0.679±0.007 |

Headline deltas (CFRR-SNIPS vs. LFRR baseline): NDCG@10 +2.7% (Synthetic), +3.5% (DBLP), +0.9% (Epinions); Coverage@10 +51% relative (Synthetic: 0.504→0.763); Gini-Exposure −24% relative (Synthetic: 0.708→0.535). Improvements in NDCG@10/MRR for CFRR-SNIPS were statistically significant (paired t-tests, p<0.05, Bonferroni-corrected) vs. the next-best baseline on each dataset.

**Ablations (Synthetic, ground truth known):** SNIPS vs. IPS — Coverage@10 rose from 0.557 (CFRR-IPS) to 0.763 (CFRR-SNIPS), a 37% relative improvement (p<0.05); Gini-Exposure fell from 0.688 to 0.535 (22% relative reduction, p<0.05); NDCG@10 0.301→0.307, MRR 0.515→0.527. Doubly robust variant: under well-specified propensities (AUC>0.9) DR performs similarly to SNIPS (NDCG@10 0.307, Coverage@10 0.763); under intentionally misspecified propensities (features removed, AUC≈0.7), DR degrades less (NDCG@10 0.302 vs. 0.295 for SNIPS; Coverage@10 0.745 vs. 0.720 for SNIPS), demonstrating DR's robustness value. Outcome model AUC: >0.85 on Synthetic, >0.75 on real-world datasets. Compute overhead: SNIPS weighting adds ~5-10% training time; DR variant adds ~20% additional training time.

## Limitations
- Positivity assumption (θ(u,v) > 0 for all relevant pairs) is difficult at marketplace scale with trillions of potential pairs; the authors propose restricting debiasing to "economically viable/plausible" pairs from candidate generation as a practical compromise, not a rigorous fix.
- Propensity model misspecification remains a real risk; DR augmentation only partially compensates.
- Negative sampling for real-world datasets (equal random non-linked pairs) "may not perfectly reflect true non-interactions" — true negatives are unavailable, a known limitation the authors flag explicitly and defer ("sophisticated negative sampling with CFRR is future work").
- Effect sizes (Cohen's d) deferred to supplementary material, not in the main paper as read.
- Generalization of the "fairness-growth feedback loop" (Discussion §3) from synthetic to real platforms "requires careful validation on a case-by-case basis" — explicitly flagged as unproven at platform scale.
- Extension to dynamic/time-varying treatments (e.g., dynamic pricing), network effects, and continuous A/B-test-informed exploration are named as open future work, not solved here.

## Heavily Cited Prior Works
- Schnabel, Swaminathan, Singh, Chandak, Joachims (2016) — "Recommendations as Treatments: Debiasing Learning and Evaluation" (foundational IPS-for-recsys framing).
- Swaminathan & Joachims (2015) — SNIPS ("Counterfactual Risk Minimization"/self-normalized estimator), the core variance-reduction technique CFRR builds on.
- Zheng, Zheng (2023) — StableDR ("Stabilized Doubly Robust Learning for Recommendation on Data Missing Not At Random"), the strongest baseline, adapted here to pair-level RRS.
- Zhu, Hou, Zhang, Caverlee (2020) — CausE-style causal/propensity debiasing for item recommendation, adapted as a baseline.
- Zheng, Gao, Li, He, Jin (2021) — DICE, disentangling interest from conformity/popularity, used as a baseline.
- Palomares, Porcel, Pizzato, Guy, Herrera-Viedma (2021) — "Reciprocal Recommender Systems: Analysis of state-of-the-art literature, challenges and opportunities towards social recommendation" (survey grounding the RRS problem framing).
- Suhr, Biega, Zehlike, Gummadi, Chakraborty (2019) — "Two-Sided Fairness for Repeated Matchings in Two-Sided Markets: A Case Study of a Ride-Hailing Platform" (fairness/two-sided constraints framing).

## Bibliography Fields
- **title:** Counterfactual Reciprocal Recommender Systems for User-to-User Matching
- **authors or organization:** Kazuki Kawamura, Takuma Udagawa, Kei Tateno (Sony Group Corporation, Japan)
- **year:** 2025
- **venue or type:** TSMO '25 — Workshop on Two-sided Marketplace Optimization: Search, Discovery, Matching, Pricing & Growth, co-located with KDD 2025 (Toronto, Canada); arXiv:2508.01867
- **link:** https://arxiv.org/pdf/2508.01867
- **tier tag:** Tier 3 academic method
- **what they did (≤80 words):** Proposed CFRR, a causal-inference framework for reciprocal (user-to-user) recommenders that estimates pair-level display propensities and trains a self-normalized IPS (SNIPS) objective, optionally with weight truncation and doubly robust augmentation, to correct exposure/popularity bias. Validated on one synthetic and two real-world (DBLP co-authorship, Epinions trust) datasets, showing simultaneous gains in ranking accuracy, long-tail coverage, and exposure-Gini fairness over five RRS/causal baselines.
- **mechanism relevant to two-sided balancing (≤50 words):** Pair-level (bilateral) inverse-propensity reweighting directly targets exposure imbalance — the same phenomenon as desirability skew in dating: over-exposed/popular users dominate training signal and get more recommendation slots, starving long-tail users of visibility and match opportunity.
- **metrics used, and the reported effect:** NDCG@10 (+2.7–3.5% vs. baseline), MRR, Coverage@10 (+51% relative on Synthetic, 0.504→0.763), Gini-Exposure (−24% relative on Synthetic, 0.708→0.535); all with 10-seed mean±std and paired t-tests (p<0.05, Bonferroni-corrected).
- **fit for a dating app:** high — the paper explicitly targets dating platforms as a motivating RRS use case, treats bilateral acceptance as the outcome, and its exposure-fairness / long-tail-coverage machinery maps directly onto exposure allocation (layer 2) and, via propensity-based reweighting of match likelihood, could inform reciprocal scoring (layer 1). It does not model *reply capacity* directly (exposure ≠ capacity), so it addresses exposure fairness rather than capacity-aware allocation per se.
- **confidence that the item is real and described correctly:** high — full 9-page paper read directly, all numbers taken from Table 1, Figures 1-2, and the ablation subsection as printed.

## Project Relevance
Directly relevant to layer 2 (capacity-aware exposure allocation) and partially to layer 1 (reciprocal scoring). CFRR's pair-level IPS/SNIPS reweighting is a mechanism to counteract exactly the "small set of highly desirable users absorbs most likes" dynamic named in the project context — it debiases the *training signal* so that popularity-driven over-exposure doesn't get baked into future recommendations, and its Coverage@10/Gini-Exposure metrics are close cousins of the project's "spread of matches" and "match Gini" ecosystem metrics (layer 4). Caveat: CFRR corrects for exposure/display bias in observed data, not for *reply capacity* limits explicitly — it reweights based on how often a user was *shown*, not on their finite capacity to reply once shown, so it is a fairness-of-exposure lever rather than a capacity-of-response lever. It would need combination with an explicit capacity constraint (e.g., LiJAR-style redistribution) to close that gap. No market-design levers (layer 3, e.g. like limits, curated batches) are addressed.

## Reverse Citation Map
