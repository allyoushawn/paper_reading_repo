# Creator-Side Recommender System: Challenges, Designs, and Applications

- **notebook source_id:** `e2743fe8`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Kuaishou (Kwai) engineers observe that typical "user-side" recommender systems only optimize which items to show a requesting user, which concentrates exposure on a few items/creators and leaves most creators under-exposed, hurting creator satisfaction and long-term platform health. They introduce **DualRec**, a "creator-side" recommender system that mirrors the user-side system by swapping the roles of users and items: given an uploaded item, find the best user set to dispatch it to. They show retrieval/ranking algorithms from user-side recommenders can be mirrored into creator-side versions with only small changes, and they identify and solve a creator-side-specific problem — the **user availability issue** — via a User Availability Calculation (UAC) module that tracks which users can still be shown more items without exceeding their consumption capacity. DualRec is live in Kwai (100M+ users, 10M+ creators) and significantly improves creator-side metrics (Daily Active Creator, exposure reach) with successive versions.

## Method
- **Formulation:** user-side recommendation is `C_u = R^U(u, C, K)` (pick K items from item set C for user u); creator-side is the mirror `U_i = R^C(i, U, L)` (dispatch item i to L users from user set U).
- **Retrieval — similarity-based:** user-side has user-similarity retrieval (u2u2i) and item-similarity retrieval (u2i2i). By symmetry, creator-side similarity-based retrievals (i2i2u, i2u2u) reuse the *same* underlying similarity services (no extra model training needed) — a key simplification finding.
- **Retrieval — two-tower model:** trains a user tower and item tower with inner-product logit; user-side retrieval builds an item ANN index and queries by user embedding, creator-side retrieval builds a *user* ANN index and queries by item embedding — `U_i^two-tower = Top_{u∈U} {e_u · e_i}`.
- **Ranking — prediction model changes:** (1) sample augmentation — drop the item-ID feature and train on both original and augmented samples to force the model to learn from side features (helps long-tail items with sparse IDs); (2) added item-side features (recently-interacted users, video-understanding similarity). Score integration changes the ranking coefficients to weight explicit interactions (likes/comments/follows) more heavily than watch time, since creators cannot perceive watch time but can perceive likes/comments.
- **User Availability Calculation (UAC) — the core creator-side-specific contribution:** maintains an available-user set `Ũ = {u ∈ U : a_u=1, |D_u| < Q}`, where `a_u` is a predicted future-activity flag (XGBoost model on 30-day activity features, run daily) and `D_u` is the running set of items already matched to user u, capped at a maximum consumable quantity Q (set to 10 in the live experiment). Creator-side retrieval and ranking run only over this available-user pool, and `D_u` is updated after each match, removing users once they hit capacity Q.
- **Combined recommendation:** creator-side matches are cached (`D_u`) and injected into the user-side ranking score with a boosting term: `f'_{ui} = f_{ui} + λ·g_{ui}` if `i ∈ D_u`, else `f_{ui}` — i.e., items the creator-side system flagged for a user get a score boost (not a hard override) in the final user-facing ranking.
- **Evaluation design:** a user-creator co-diverted A/B test (partition creators into disjoint control/treatment pools, then assign users to the pool matching their group) rather than a standard user-diverted test, to avoid treatment leakage across creators sharing the same exposed item pool.

## Datasets and Baselines
- Live production data from **Kwai**, a short-video platform with 100M+ users, 10M+ creators, 4M+ videos uploaded daily.
- **Baseline ("Base"):** a traditional user-side recommender augmented with extra strategies for new/low-exposure items, inspired by FairRec — extra retrievals surfacing low-exposure items and score boosting for new items in the ranking module.
- Iterative ablation baselines: DualRec-v1 (basic two-tower + UAC) → v2 (+ sample augmentation & extra item features) → v3 (+ i2i2u content-similarity retrieval) → v4 (+ i2u2u user-similarity retrieval) → v5 (+ score-integration bias term θ_u).

## Results
- **Table 2 — ExpoReach gains over previous baseline** (live A/B, confidence level > 0.95):
  - DualRec-v1 vs. Base: **+11.7% ExpoReach-1K, +8.4% ExpoReach-10K**
  - DualRec-v2 vs. v1: +4.9% / +5.4%
  - DualRec-v3 vs. v2: +3.2% / +4.8%
  - DualRec-v4 vs. v3: +0.59% / +0.78%
  - DualRec-v5 vs. v4: +3.7% / +3.5%
- **21-day integrated experiment:** Daily Active Creator (DAC) gain rises to **+2.9%** by the end of the period (Figure 7); the paper reports "every 1% increase in ExpoReach corresponds to a 0.13% increase in DAC."
- **New item coverage (Figure 8):** user-side two-tower retrieval covers only **13.6%** of new items; creator-side two-tower without UAC covers **41.7%**; creator-side two-tower **with UAC covers 82.3%**.
- **Exposure ratio across creator-side retrieval types (Table 3):** two-tower 58.7%, i2i2u 38.5%, i2u2u 2.79%.
- **Offline ranking-model AUC (Table 4):** baseline (w/o sample augmentation, w/o extra features) 0.901; +extra features only 0.908 (+0.7pp); +sample augmentation only 0.911 (+1.0pp); both combined **0.913 (+1.2pp)**.
- **UAC hit-rate impact:** without the user-activity-prediction module, the hit rate of matched users who actually visit the next day is only **49%**; with it, hit rate rises to **82%**.
- **User-matching-set distribution (Figure 9):** without the available-user store, some users are matched with 0 items while others exceed 10,000 items (way beyond consumption capacity); with the store, the vast majority fall in the 1–50 item range.
- **Score-integration (DualRec-v5) side effects:** the bias-penalizing integration increases the liking rate of items in the experimental group by **0.78%** and the following rate by **1.472%**, in addition to enhancing ExpoReach.

## Limitations
- The paper does not report user-side satisfaction metrics for these experiments ("out of this paper's scope... regarded as constraints of DualRec"), i.e., improvements are creator-facing and the user-experience trade-off is not quantified here.
- DAC is slow-moving and hard to observe in a single short experiment, forcing reliance on the ExpoReach proxy metric and a separate 21-day integrated experiment to see the DAC effect.
- Q (max items a user can consume) is set as a single constant across all users for simplicity, despite the paper itself noting "different users can consume different numbers of items."
- DualRec only dispatches 200 users per item directly; the paper notes the *additional* future exposure gain (beyond those 200) comes from user-side recommender systems picking up items DualRec found — i.e., DualRec's measured effect is partly indirect/downstream rather than a fully isolated causal estimate of the creator-side system alone.
- No discussion of long-tail/adversarial gaming risk (e.g., creators optimizing for whatever signal DualRec rewards).

## Heavily Cited Prior Works
- FairRec (Patro et al., 2020) — "Fairrec: Two-sided fairness for personalized recommendations in two-sided platforms" (baseline strategy inspiration)
- Zheng et al. — "Reciprocal sequential recommendation" (RecSys 2023)
- Xiao et al. (2024) — "Deep Evolutional Instant Interest Network for CTR Prediction" (WSDM 2024)
- He et al. (2017) — "Neural collaborative filtering" (WWW 2017) — backbone CF model used for base utility
- Chen & Guestrin (2016) — "XGBoost: A scalable tree boosting system" — used for user activity prediction
- Su et al. (2018) — "Pixie: A System for Recommending 3+ Billion Items to 200+ Million Users in Real-Time" (WWW 2018)
- Zhu et al. (2021) — "Fairness among new items in cold start for recommender systems" (SIGIR 2021)

## Bibliography Fields
- **title:** Creator-Side Recommender System: Challenges, Designs, and Applications
- **authors or organization:** Xiaoshuang Chen, Yibo Wang, Yao Wang, Husheng Liu, Kaiqiao Zhan, Ben Wang, Kun Gai — Kuaishou Technology (Kun Gai unaffiliated)
- **year:** 2025
- **venue or type:** WWW '25 Companion (Companion Proceedings of the ACM Web Conference 2025, Sydney, NSW, Australia)
- **link:** https://arxiv.org/pdf/2502.20497
- **tier tag:** Tier 1 industry (live A/B-tested and deployed in production on Kwai)
- **what they did (≤80 words):** Built DualRec, a creator-side mirror of Kuaishou's user-side recommender that finds the best users to dispatch each newly-uploaded video to, reusing user-side retrieval/ranking algorithms with minor modifications. Solved the "user availability" problem — the risk of over-matching a small set of active users beyond their consumption capacity — with a UAC module that tracks per-user matched-item counts against a capacity cap and predicted next-day activity. Deployed live at scale.
- **mechanism relevant to two-sided balancing (≤50 words):** Explicit per-user consumption-capacity cap (`|D_u| < Q`) combined with predicted future activity, used to gate which users are even eligible to receive more creator-side matches — a direct, deployed instance of "per-user capacity constraint" exposure allocation, plus a soft boosting mechanism to blend supply-side (creator) and demand-side (user) ranking objectives.
- **metrics used, and the reported effect:** ExpoReach-1K/10K (new-item exposure reach), Daily Active Creator (DAC), new-item coverage, offline AUC, user-matching hit rate, liking/following rate. DAC +2.9% over 21 days; ExpoReach gains of +0.6% to +11.7% per iterative component; new-item coverage jumps from 13.6% (user-side only) to 82.3% (creator-side + UAC).
- **fit for a dating app:** high — the UAC module's per-user capacity cap and available-user store is structurally identical to a dating app's reply-capacity constraint (don't keep sending likes/matches to a user who is already saturated and won't respond), and the paper reports a live, measured platform-health benefit from enforcing it.
- **confidence that the item is real and described correctly:** high — full 9-page paper (through references) was read directly from the PDF, including all tables and figures.

## Project Relevance
Strong fit for **Layer 2 (capacity-aware exposure allocation)**: the UAC module is essentially a deployed per-user capacity constraint and exposure-fairness re-ranking mechanism (cap matches per user at Q, remove saturated users from the eligible pool, predict who will actually be available to consume more) — directly transferable to gating who receives more likes/impressions based on remaining reply bandwidth. The "combined recommendation module" (soft score boost rather than hard override, `f' = f_ui + λ·g_ui`) is also a reusable pattern for blending a viewer-desirability signal with a reciprocal/capacity signal in dating-app ranking. Touches **Layer 3 (market-design levers)** lightly via the "which side searches" framing (creator-side push vs. user-side pull) and **Layer 4** via ExpoReach/coverage as proxy ecosystem-health metrics and the user-creator co-diverted A/B design (relevant to interference-aware experimentation).

**Disanalogy to flag:** the underlying interaction is single-sided consumption (a viewer watches/likes a video; the creator never has to reciprocally "accept" a specific viewer), not mutual reciprocal consent — there is no analogue here to "a match requires both sides to like." The capacity constraint (Q, max items consumed) caps how much content a *consumer* can absorb, not how much reply bandwidth a *desirable person* has to respond to individual suitors — closer to the viewer-attention side of the project's model than the reply-capacity side, though the mechanism (a hard per-entity cap gating eligibility) is directly reusable for the latter.

## Reverse Citation Map
