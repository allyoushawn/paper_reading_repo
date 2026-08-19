# Balanced Neighborhoods for Multi-sided Fairness in Recommendation

- **notebook source_id:** `1dccf951`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Recommender systems on multisided platforms must sometimes be fair not just to consumers but also to item/service providers. The paper defines C-fairness (consumer-side), P-fairness (provider-side), and CP-fairness (both), and proposes "balanced neighborhoods" — a modification of the Sparse Linear Method (SLIM) that adds a regularization term forcing each user's (or item's) k-nearest-neighbor set to have equal aggregate weight from a protected and an unprotected group. On MovieLens (consumer fairness, gender as protected attribute) the balanced version brings genre-recommendation equity close to parity with under 2% NDCG loss; on Kiva.org microloans (provider fairness, geographic region as protected attribute) it improves both equity and ranking accuracy simultaneously.

## Method
Extends SLIM-U (user-based) and SLIM (item-based) collaborative filtering, where a sparse weight matrix W predicts ratings as Ŝ = WR. The paper adds a "neighborhood balance" term to SLIM's loss: for each user i, define p_k = +1 if user k is in the protected class U+ and -1 if in the unprotected class U-; the balance penalty is b_i = (Σ_{k} p_k w_ik)², i.e., the squared difference between the summed neighbor-weights from the protected group and from the unprotected group. Full loss: L = ½‖R−WR‖² + λ1‖W‖₁ + (λ2/2)‖W‖² + (λ3/2)Σ_i b_i, minimized via coordinate descent (closed-form per-weight update, same structure as vanilla SLIM but with an added λ3·p_k·Σp_l·w_il term). λ3 controls how strongly the optimizer is pushed toward class-balanced neighborhoods. The user-based variant (BN-SLIM-U) targets C-fairness by balancing each user's peer neighborhood; the item-based variant (BN-SLIM) targets P-fairness by balancing each item's neighborhood of similar items.

## Datasets and Baselines
- **MovieLens 1M** (6,040 users, 4,000 movies): consumer-fairness scenario constructed artificially (the paper explicitly notes movie preference is "not an obvious candidate for fairness-aware recommendation" and the setup is for expository purposes only). Protected class = female users (1,709 of 6,040). Baseline = unmodified SLIM-U vs. BN-SLIM-U.
- **Kiva.org microloans** (~1M loans, 5-core filtered to 3,593 pseudo-items / 29,342 users / 393,035 ratings, pulled from Kiva's public API, Sept 2016): provider-fairness scenario. Protected regions = Africa, Middle East, Central America (higher unfunded-loan rates); unprotected = North America, Eastern Europe, South America, Asia. Baseline = unmodified SLIM vs. BN-SLIM.
- Implemented via LibRec 2.0's existing SLIM implementation; evaluated with 5-fold cross-validation.

## Results
**MovieLens (C-fairness):** λ1=0.1, λ2=0.001, λ3=25. On the five lowest-equity genres (Film-Noir, Mystery, Horror, Documentary, Crime), the equity score E_c@10 (ratio of protected/unprotected recommendation rate for the genre, 1.0 = parity) moved closer to 1.0 under BN-SLIM-U for every genre; the largest gain was in "Horror," about +0.09 (~10 percentage points) in equity score. Ranking accuracy: NDCG@10 = 0.053 (SLIM-U) vs. 0.052 (BN-SLIM-U) — roughly a 2% loss. For female-preferred genres (Fantasy, Animation, Romance, War, Western) equity scores were already near 1.0 for both algorithms; one anomaly — "War" — became *more* skewed under BN-SLIM-U (1.07→1.16), which the authors flag as unexplained.

**Kiva.org (P-fairness):** λ1=0.01, λ2=0.001, λ3=0.9. Table 3: SLIM baseline NDCG@10 = 0.046, E_p@10 = 0.90 (loans from protected regions under-recommended); BN-SLIM: NDCG@10 = 0.049, E_p@10 = 1.05. Both ranking accuracy *and* equity improved simultaneously under the balanced-neighborhood version — the authors call this "interesting" since it is not the fairness/accuracy trade-off usually assumed.

## Limitations
- The additive/utilitarian equity measures (E_c@k, E_p@k) are aggregate group-level ratios; they do not reveal whether individual users/providers experience a Pareto improvement or whether some subgroups are worse off even as the group average improves — explicitly flagged as unknown for the Kiva result.
- The MovieLens fairness scenario is acknowledged as artificially constructed for demonstration only, not a real-world fairness need in movie recommendation.
- The "War" genre result moved in the wrong direction under balancing, and the authors state they do not know why.
- System/stakeholder utilities are described as "highly domain-specific," making it hard to find appropriate datasets or generalize findings across recommendation scenarios.
- CP-fairness (balancing both consumer and provider fairness simultaneously) is explicitly left as future work; this paper only handles one side at a time.
- λ3 must be tuned much higher than λ1/λ2 because the balance term (a difference of sums) is naturally much smaller in magnitude than the reconstruction/regularization terms — a fragile hyperparameter-scaling dependency the paper notes but does not resolve generally.

## Heavily Cited Prior Works
- Ning and Karypis (2011) — SLIM: Sparse Linear Methods for top-N recommender systems (the base algorithm being extended)
- Zemel, Wu, Swersky, Pitassi, Dwork (2013) — Learning Fair Representations (ICML) — source of the "fair prototype" idea generalized here to neighborhoods
- Dwork, Hardt, Pitassi, Reingold, Zemel (2012) — Fairness through awareness
- Pizzato, Rej, Chung, Koprinska, Kay (2010) — RECON: a reciprocal recommender for online dating — cited as the origin of bilateral/reciprocal-recommendation fairness considerations
- Burke, Abdollahpouri, Mobasher, Gupta (2016) — Towards multi-stakeholder utility evaluation of recommender systems
- Abdollahpouri, Burke, Mobasher (2017) — Recommender Systems as Multistakeholder Environments
- Yao and Huang (2017a, 2017b) — Beyond Parity: Fairness Objectives for Collaborative Filtering; New Fairness Metrics that Embrace Differences

## Bibliography Fields
- **title:** Balanced Neighborhoods for Multi-sided Fairness in Recommendation
- **authors or organization:** Robin Burke, Nasim Sonboli, Aldo Ordoñez-Gauger (School of Computing, DePaul University)
- **year:** 2018
- **venue or type:** Conference on Fairness, Accountability, and Transparency (FAT*) 2018 — Proceedings of Machine Learning Research, vol. 81, pp. 1–13
- **link:** http://proceedings.mlr.press/v81/burke18a/burke18a.pdf
- **tier tag:** Tier 3 academic method
- **what they did (≤80 words):** Introduced C-/P-/CP-fairness taxonomy for multistakeholder recommenders and proposed "balanced neighborhoods" — a SLIM regularization term that penalizes the imbalance between protected- and unprotected-group neighbor weights for each user (BN-SLIM-U, consumer fairness) or item (BN-SLIM, provider fairness). Evaluated on MovieLens (gender/genre, artificial scenario) and Kiva.org microloans (geographic region), showing improved outcome equity with minimal (MovieLens) or no (Kiva) ranking-accuracy loss.
- **mechanism relevant to two-sided balancing (≤50 words):** A learned re-ranking/regularization lever that redistributes exposure across a protected/unprotected group split by penalizing neighborhood imbalance directly inside a collaborative-filtering objective — a concrete, generalizable exposure-fairness re-ranking mechanism (project layer 2), though built for group demographic fairness, not capacity/reciprocity.
- **metrics used, and the reported effect:** Equity ratio E_c@k / E_p@k (protected vs. unprotected recommendation rate, 1.0=parity) and NDCG@10. MovieLens: equity gains up to +0.09 (Horror genre) with ~2% NDCG@10 loss (0.053→0.052). Kiva: equity improved 0.90→1.05 *and* NDCG@10 improved 0.046→0.049 simultaneously.
- **fit for a dating app:** medium — the neighborhood-balance regularization is a real, transferable exposure-redistribution mechanism, and the Kiva case specifically models scarce, single-use supply units (a funded loan disappears, much like a person's finite reply capacity), which is structurally closer to dating than the MovieLens case. But the mechanism targets demographic-group parity, not reciprocal like-back probability or per-user capacity constraints, and has no reciprocity/feedback-loop or ecosystem-health notion at all.
- **confidence that the item is real and described correctly:** high — full 13-page paper read directly; all numbers quoted are taken from the paper's own tables (Table 2, Table 3) and figures (Figure 2, Figure 3).

## Project Relevance
Medium project relevance, narrowly on layer 2 (capacity-aware exposure allocation). The neighborhood-balance regularization term is a concrete instance of an exposure-fairness re-ranking lever: it directly modifies a collaborative-filtering objective to redistribute recommendation exposure between a protected and unprotected group without a separate post-hoc re-ranking pass, which is architecturally relevant to building exposure-fairness constraints into a dating recommender's scoring function. The Kiva.org P-fairness experiment is the more relevant of the two: loans are one-time, scarce, single-recipient supply units ("once funded, disappears from Kiva.org and is not available for other lenders to view or support" — loans have 1–330 funders vs. movies rated by thousands), which is a genuine capacity-scarcity analogy to a person's finite reply capacity, unlike the MovieLens case where supply (movies) is unlimited. However, the paper does **not** address reciprocal scoring (layer 1) — there is no mutual like-back probability or two-way interest modeling anywhere — nor does it model per-user variable capacity, desirability skew, wasted likes, or any ecosystem/interference metric (layers 3–4). It also targets static demographic-group fairness rather than a market-design lever like like-limits, pacing, or signaling. **Disanalogy flagged:** the MovieLens half of the paper explicitly has unlimited supply-side capacity (movies can be watched by unrestricted numbers of viewers), unlike dating's scarce, human reply capacity; only the Kiva half avoids this disanalogy.

## Reverse Citation Map
