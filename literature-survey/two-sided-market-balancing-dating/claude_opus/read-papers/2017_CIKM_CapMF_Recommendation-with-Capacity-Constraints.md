# Recommendation with Capacity Constraints

- **notebook source_id:** `433bf032`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Many recommendation settings have a hard maximum capacity per item (POI seats, book copies, class enrollment slots) — if too many users are pointed at the same item, it overloads (long queues, out-of-stock, congestion). Existing recommenders (PMF, BPR, GeoMF) optimize purely for accuracy/ranking and ignore this constraint. The authors introduce a weighted-objective framework that adds a soft "capacity loss" term — penalizing the gap between an item's expected usage (propensity-weighted sum of predicted scores across users) and its fixed capacity — to the standard prediction/ranking loss, yielding Cap-PMF, Cap-BPR, Cap-GeoMF, Cap-GeoBPR. On MovieLens (item rec) and Foursquare/Gowalla (POI rec), the capacity-constrained variants sharply reduce capacity violations at a real but often modest accuracy cost, and in several capacity-definition/dataset combinations actually *improve* top-N recommendation quality (weighted AP) over both the unconstrained models and a simple post-processing baseline.

## Method
- **User propensity** p_i ∈ [0,1]: probability that user i follows the system's recommendation (estimated from data, e.g. p_i = observed ratings by i / total items, or other schemes tested in §5.1).
- **Item capacity** c_j > 0: max number of users who can simultaneously use item j (POI seats, book copies, etc.).
- **Expected usage** of item j: E[usage(j)] = Σ_i p_i · σ(r̂_ij), the propensity-weighted sum of sigmoid-squashed predicted scores across all M users (sigmoid used instead of thresholding r̂_ij to {0,1} for differentiability).
- **Capacity loss:** average over items of an indicator that usage exceeds capacity, 1[c_j ≤ E[usage(j)]]; since the indicator isn't optimization-friendly, it's replaced by a convex surrogate on Δ(c_j, E[usage(j)]) = c_j − E[usage(j)] — logistic loss log(1+exp(−Δ)) is the primary surrogate (hinge and exponential loss also tested).
- **Overall (weighted) objective:** (1−α)·[prediction or ranking loss] + α·[capacity loss] + regularization, with trade-off parameter α ∈ [0,1]. Applied to four base models: Cap-PMF and Cap-GeoMF (square/rating-prediction loss, Eq. 7-8), Cap-BPR and Cap-GeoBPR (pairwise ranking loss, Eq. 9). Gradients derived via chain rule (Eq. 10-13) and optimized by alternating minimization / gradient descent (Adagrad).
- **Baseline comparator — post-processing:** given any unconstrained model's predicted scores r̂_ij, for each item j greedily rank users by predicted score and recommend to only the top c_j users (Algorithm 1), by construction respecting capacity but not accounting for it during training.
- **GeoMF/GeoBPR** for POI recommendation additionally model each user's latent "activity area" vector and each POI's "influence vector" (precomputed via kernel density estimation over geographic tiles) alongside the standard MF/BPR latent factors.

## Datasets and Baselines
**Datasets:** MovieLens 100K (943 users, 1,682 items, 100K ratings) and MovieLens 1M (6,040 users, 3,706 items, 1M ratings) for item recommendation (explicit + binarized implicit feedback); Foursquare (2,025 users, 2,759 POIs, 85,988 check-ins) and Gowalla (7,104 users, 8,707 POIs, 195,722 check-ins) for POI recommendation (implicit check-in data). Capacities and propensities are not given in any of these public datasets, so the authors construct six synthetic capacity-assignment schemes (actual/usage-proportional, binning, uniform-k, linear max, linear mean, reverse binning — inversely proportional to usage) and three propensity schemes (actual = observed-rating fraction, median-split, linear).

**Baselines:** unconstrained PMF, BPR, GeoMF, GeoBPR; "onlyCap" (α=1, capacity loss only, no accuracy objective); post-processing variants PostMF, PostBPR (rank-and-cut to capacity after the fact).

**Metrics:** RMSE (Cap-PMF/Cap-GeoMF, rating prediction), 0/1 Pairwise Loss (Cap-BPR/Cap-GeoBPR, fraction of incorrectly ordered pairs), Capacity Loss (Eq. 16, average logistic-surrogate violation), Average Precision AP@k (k=1,5,10), and a new metric Weighted AP@top (WAP@top, Eq. 18) — AP@top averaged across users weighted by their propensity p_i, used specifically to evaluate top-N quality under the capacity-constrained setting.

## Results
- **Rating prediction vs. capacity loss (α sweep, Fig. 3):** as α increases 0→1, capacity loss falls and RMSE rises monotonically across all four datasets, confirming the trade-off is real and controllable.
- **Cap-PMF/Cap-GeoMF vs. unconstrained (α=0.2):** MovieLens 100K — Cap-PMF cuts Capacity Loss from 11.29 (PMF) to 1.65, at the cost of RMSE rising from 0.38 to 0.71. Foursquare (POI) — Cap-GeoMF cuts Capacity Loss from 2.35 (GeoMF) to 0.15, RMSE rises from 0.66 to 0.97. Similar trend on Gowalla.
- **Cap-BPR/Cap-GeoBPR vs. unconstrained:** MovieLens 100K — Cap-BPR achieves Capacity Loss 0.08 vs. 4.51 (BPR), at 0/1 Pairwise Loss 0.14 vs. 0.12 (a small degradation). Foursquare — Cap-GeoBPR achieves Capacity Loss 0.02 vs. 0.81 (GeoBPR), and *better* 0/1 Pairwise Loss 0.28 vs. 0.31.
- **onlyCap (α=1) vs. Cap- (α=0.2):** MovieLens 100K — onlyCap improves Capacity Loss further (1.65→0.04) but RMSE worsens sharply (0.71→1.43); onlyCap also gives worse 0/1 pairwise loss (0.17 vs. 0.14 for Cap-BPR).
- **Top-N quality (Table 2, WAP@{10,50}):** results are mixed and capacity-definition-dependent, with an asterisk marking the best capacity-respecting method per row. Selected rows — MovieLens 100K, Actual capacity, square loss, WAP@10: MF 0.152, PostMF **0.153\***, CapMF 0.138 (post-process best here). Foursquare, Actual capacity, square loss, WAP@10: MF 0.016, PostMF 0.016, CapMF **0.041\***; WAP@50: MF 0.011, PostMF 0.011, CapMF **0.027\***. Foursquare, Actual capacity, pairwise loss, WAP@10: BPR 0.056, PostBPR 0.049, Cap-BPR **0.084\***. The authors conclude that capacity definitions analogous to usage ("actual", "binning") give the best top-N results for the weighted-objective (Cap-) approach, and that Cap- methods "largely outperform the post-process solution," sometimes even beating the unconstrained model outright — evidence that respecting capacity can *improve*, not just constrain, recommendation quality.
- **Sensitivity (§5.5):** logistic and hinge surrogate losses perform similarly for MovieLens; hinge is best for Foursquare/Gowalla (POI). 'Median'/'linear' propensity definitions (which push more users to higher propensity) increase both RMSE and Capacity Loss relative to 'actual' propensity. Trends are similar for implicit vs. explicit MovieLens feedback (Fig. 10).

## Limitations
- Capacities and propensities are not available in any public dataset used, so both had to be synthetically constructed under six/three alternative schemes — real capacity/propensity values were never validated against ground truth.
- The framework only handles the batch (offline) setting; the authors explicitly defer online/bandit formulations to future work ("In the future, we will consider the online or bandit setting").
- User propensity is treated as static per Section 3, even though the paper acknowledges propensity can vary by time, context, and who the recommendation comes from; dynamic propensity estimation is named as future work, not implemented.
- The paper models item capacity as a single global inventory constraint (one item shared across many users); it does not model bilateral/reciprocal capacity (an item that is itself a *person* with a capacity to reciprocate), so it is fundamentally single-sided.
- No statistical significance testing (no p-values, no variance across seeds) is reported for any of the results tables.

## Heavily Cited Prior Works
- Koren, Bell, Volinsky (2009) — "Matrix Factorization Techniques for Recommender Systems" — foundational MF framing (PMF built on this line).
- Rendle, Freudenthaler, Gantner, Schmidt-Thieme (2009) — BPR: "Bayesian Personalized Ranking from Implicit Feedback" — the pairwise ranking objective extended into Cap-BPR.
- Lian, Zhao, Xie, Sun, Chen, Rui (2014) — GeoMF: "Joint Geographical Modeling and Matrix Factorization for Point-of-interest Recommendation" — the geo-aware base model extended into Cap-GeoMF/Cap-GeoBPR.
- Zhang, Zhao, Zhang, Friedman, Zhang, Ma (2016) — "Economic Recommendation with Surplus Maximization" — related resource-allocation-under-capacity work explicitly contrasted with this paper's approach (focus on individual utility vs. platform-wide surplus).
- Gupta, Liang, Tseng, Chen, Rosales (2016) — email volume allocation under a non-personalized capacity constraint, contrasted as a related-but-different (non-personalized) capacity problem.
- Xia, Cong, Li, Pham, Naswamy (2015) — Rank-GeoFM: ranking-based geographical factorization for POI recommendation.
- Karatzas & Shreve (2012) — queueing-theory / stochastic calculus reference, cited as a conceptual analogy (capacity constraints as queue waiting-time minimization).

## Bibliography Fields
- **title:** Recommendation with Capacity Constraints
- **authors or organization:** Konstantina Christakopoulou (University of Minnesota), Jaya Kawale (Netflix), Arindam Banerjee (University of Minnesota)
- **year:** 2017
- **venue or type:** CIKM '17 (ACM International Conference on Information and Knowledge Management), November 6-10, 2017, Singapore
- **link:** https://arindam.cs.illinois.edu/papers/17/rec-capacity-cikm17.pdf
- **tier tag:** Tier 3 academic method
- **what they did (≤80 words):** Extended three latent-factor recommenders (PMF, BPR, GeoMF/GeoBPR) with a weighted-objective framework that adds a differentiable "capacity loss" penalizing when an item's propensity-weighted expected usage exceeds its fixed capacity, trading off against the usual prediction/ranking loss via parameter α. Evaluated on MovieLens (item) and Foursquare/Gowalla (POI) data with synthetically assigned capacities/propensities, showing constraint-satisfying recommendations at modest-to-negligible cost to (and sometimes improvement of) top-N accuracy.
- **mechanism relevant to two-sided balancing (≤50 words):** A generic template for capping *expected exposure per item* (here: item capacity) inside the training objective itself, rather than post-hoc — directly transferable to capping expected likes/impressions a person receives relative to their reply capacity, i.e., a soft, differentiable version of capacity-aware exposure allocation (layer 2).
- **metrics used, and the reported effect:** RMSE, 0/1 Pairwise Loss, Capacity Loss, AP@k, and a novel Weighted AP@top (WAP@top). Capacity Loss reductions of ~85-95% (e.g., MovieLens 100K: 11.29→1.65; Foursquare: 2.35→0.15) at RMSE cost of roughly +0.3 (e.g., 0.38→0.71); in several capacity-definition/dataset settings, Cap- methods raised WAP@10/50 above both unconstrained and post-process baselines (e.g., Foursquare CapMF WAP@10 0.041 vs. MF/PostMF 0.016).
- **fit for a dating app:** medium — the mechanism (propensity-weighted expected-usage penalty against a hard capacity, trained jointly with the ranking objective) is a strong, directly reusable template for capacity-aware exposure allocation once "item capacity" is reinterpreted as "a person's reply capacity." Disanalogy: this paper's capacity is single-sided/supply-side (an item like a POI or book has no preferences and doesn't reciprocate); it does not model bilateral acceptance, reciprocal scoring, or two-sided retention at all, so it needs to be paired with a reciprocal-scoring layer to fit dating.
- **confidence that the item is real and described correctly:** high — full 10-page paper read directly; all figures/table values transcribed from Table 2 and the text of §5.3-5.5 as printed.

## Project Relevance
Directly relevant to layer 2 (capacity-aware exposure allocation): this is essentially a worked example of turning "cap the expected load on a person/item" into a differentiable training-time penalty rather than a post-hoc filter, and it empirically shows that respecting the constraint during training (not just at serving/ranking time) can *improve* top-N quality relative to a naive post-process cutoff — a directly actionable finding for a "reply-capacity-aware" reranker. It is not reciprocal (layer 1) — item capacity here is about supply-side load, not about the item (person) themselves preferring or reciprocating — so it must be combined with a reciprocal-scoring signal to become dating-relevant. **Disanalogy flag:** the paper's worked examples (movies, POIs) have effectively elastic or non-human capacity semantics; only the general mechanism (propensity × expected-usage penalty vs. a cap) transfers, not the specific capacity-estimation heuristics, which assume static, easily observable usage/capacity data unlike a human's fluctuating reply capacity. No market-design levers (layer 3) or ecosystem/interference metrics (layer 4) are addressed.

## Reverse Citation Map
