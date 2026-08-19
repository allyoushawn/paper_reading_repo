# Paper Analysis: Real-time Personalization using Embeddings for Search Ranking at Airbnb

**Source:** NotebookLM source `aad314c0-211d-46c7-b208-cf3fc48928ba` (KDD 2018)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Real-time Personalization using Embeddings for Search Ranking at Airbnb
**Authors:** Mihajlo Grbovic, Haibin Cheng (Airbnb, Inc.)
**Abstract:**
Airbnb is a two-sided marketplace where search ranking must satisfy both guests (relevance) and hosts (booking-acceptance preferences), under the constraint that a listing can only accept one guest per date range. The paper introduces listing embeddings (skip-gram over click sessions, with the eventual booking treated as global context and negatives drawn from the same geographic market) for short-term/session-level personalization, and user-type/listing-type embeddings (trained on booking sequences, grouped by rule-based metadata buckets to fight sparsity) for long-term personalization — with host rejections encoded as explicit negative pairs during training.

**Key contributions:**
- Real-time re-ranking using embeddings of the user's most recent in-session clicks, computed online rather than via precomputed offline tables.
- Congregated-search-aware negative sampling: adds market-local negatives alongside global random negatives to fix within-market similarity degradation.
- Treats the booked listing as a "global context" term always predicted regardless of window position.
- User-type / listing-type embeddings in a shared vector space to solve booking-data sparsity (avg. 1–2 bookings/user/year) and enable cold start.
- "Rejections as explicit negatives" — host booking rejections are used as an explicit negative training signal, pushing rejected (user-type, listing-type) pairs apart in the embedding space.

**Methodology:**
Listing embeddings (d=32) trained via skip-gram + negative sampling over 800M click sessions, with the objective extended to include the booked listing as global context and same-market negative sampling. User-type/listing-type embeddings trained similarly over 50M users' booking sequences, with rejection pairs added as an explicit negative term in the same objective. Both embedding families feed cosine-similarity features (EmbClickSim, EmbSkipSim, UserTypeListingTypeSim, etc.) into a GBDT LambdaRank ranking model with multi-valued utility labels: booking=1, contact=0.25, click=0.01, view=0, host rejection=−0.4.

**Main results:**
Offline: the full model (`d32 book + neg`) best-ranks the eventually-booked listing versus ablations without booking-context or market-negatives. Adding embedding features to the GBDT ranker gave +2.27% NDCU overall, +2.58% booking-DCU, with rejection-DCU flat (+0.31%, not significant) — i.e., bookings improved without inflating host rejections. Similar-Listings carousel via embedding k-NN gave +21% CTR and +4.9% more in-carousel bookings versus the prior algorithm.

---

## 2. Experiment Critique

**Design:**
Strong ablation structure for the embeddings themselves (d32 vs. d32+booking-context vs. d32+booking-context+market-negatives) and a clean offline/online pipeline for the ranking model (with-vs-without embedding features). The Similar Listings carousel change was also validated via a genuine online A/B test against the prior production algorithm.

**Statistical validity:**
The paper reports the online booking gain from the ranking-model A/B test as "statistically significant" but does not give p-values or confidence intervals in the extracted text; the later back-test (removing embedding features caused a booking regression) is a useful naturalistic robustness check.

**Online experiments (if any):**
Two online A/B tests: (1) GBDT ranker with vs. without embedding features — statistically significant booking gain, launched to production; (2) Similar Listings carousel — embedding k-NN vs. prior algorithm, +21% CTR / +4.9% bookings, launched to production. A subsequent back-test removing embedding features produced negative bookings, corroborating the original result.

**Reproducibility:**
Full mathematical objectives are given (equations 1–9 in the paper) and the approach is a well-known, widely reproduced industry pattern (this paper is itself frequently cited as the template for "listing2vec"/session-embedding ranking systems). Airbnb's proprietary click/booking logs are not released.

**Overall:**
Results support the claims; the "rejections as explicit negatives" and "market-local negative sampling" ablations are the most convincing evidence that the two-sided (host + guest) aspects of the design carry their own measurable value, not just guest-side relevance.

---

## 3. Industry Contribution

**Deployability:**
High — production-deployed at Airbnb at 4.5M listings / 50M users scale; real-time online scoring architecture (sharded embeddings across search machines) is explicitly described.

**Problems solved:**
Real-time session personalization without offline recommendation tables; cold-start for new listings (average-of-3-nearest-neighbors fallback); sparsity in booking-level long-term signal (solved via type-level embeddings); reducing host booking rejections via explicit negative training.

**Engineering cost:**
Substantial infra: MapReduce-based daily embedding retraining, Kafka-based real-time short-term-history sets (Hc, Hlc, Hs, Hw, Hi, Hb per user), sharded in-memory embedding storage across search machines for online cosine-similarity scoring.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Real-time (vs. offline table-based) application of item embeddings; congregated-search-aware negative sampling; treating conversions (bookings) as global context; type-level (not per-user) long-term embeddings for sparsity; and using host rejections as explicit negative training signal — this last point is the paper's most direct engagement with the two-sided nature of the marketplace.

**Prior work comparison:** Builds directly on Mikolov et al. 2013 (skip-gram/negative sampling), Grbovic et al. 2015 ("E-commerce in your inbox"), Burges et al. 2011 (LambdaRank), Weston et al. 2013 and Djuric et al. 2014 (user embeddings). Notably also cites Liu 2017 "Personalized Recommendations at Tinder: The TinVec Approach" as related work, indicating the authors were aware of the dating-app analogue of this technique.

**Verification:** Novelty claims are reasonable and specific (the paper is widely regarded as an industry-standard reference for real-time embedding-based search ranking); the "rejections as explicit negatives" idea is the most original two-sided-marketplace-specific contribution and does not appear to be present in the CF/embedding baselines cited.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Airbnb click sessions | proprietary | No | 800M sessions, 4.5M listings |
| Airbnb booking sessions | proprietary | No | 50M users, 500K user types, 500K listing types |

**Offline experiment reproducibility:** Not reproducible outside Airbnb; no public dataset release. The skip-gram/negative-sampling core is reproducible on any click/booking log with the same schema.

---

## 6. Community Reaction

Not checked — out of scope for this NotebookLM-sourced batch pass (no web search performed). Note: this paper is broadly known in industry recsys practice as a foundational "session embeddings for ranking" reference (e.g. frequently cited alongside Airbnb engineering blog posts), though that assessment was not independently web-verified for this entry.

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Mihajlo Grbovic, Haibin Cheng
**Affiliations:** Airbnb, Inc.
**Venue:** KDD 2018 (Applied Data Science Track)
**Year:** 2018
**PDF:** Not fetched directly — analyzed via NotebookLM source extraction
**Relevance:** Related
**Priority:** 2

---

## Bibliography Fields

- **title:** Real-time Personalization using Embeddings for Search Ranking at Airbnb
- **authors or organization:** Mihajlo Grbovic, Haibin Cheng (Airbnb, Inc.)
- **year:** 2018
- **venue or type:** KDD 2018, Applied Data Science Track
- **link:** N/A (accessed via NotebookLM notebook source; not separately fetched)
- **tier tag:** Tier 1 — Adjacent marketplaces (job / ride / home / creator)

**What they did (80 words max):** Built real-time listing embeddings (skip-gram over click sessions, booking as global context, market-local negative sampling) and long-term user-type/listing-type embeddings (booking sequences, rule-based type buckets) for Airbnb search ranking, with host rejections encoded as explicit negatives. Fed resulting similarity features into a GBDT LambdaRank ranker with multi-valued utility labels (booking/contact/click/rejection). Deployed to production; validated offline (NDCG-style DCU lift) and via two online A/B tests.

**Mechanism relevant to two-sided balancing (50 words max):** "Rejections as explicit negatives" is the one genuinely two-sided mechanism: host rejection events push (user-type, listing-type) embeddings apart, encoding host-side preference alongside guest relevance. No capacity/backlog signal exists — rejection is used as a static historical relevance filter, not a real-time load-balancing or exposure-redistribution mechanism.

**Metrics used, and the reported effect:** NDCU (+2.27% overall), booking-DCU (+2.58%), rejection-DCU (+0.31%, flat/non-significant — meaning rejections did not increase). Similar Listings carousel: +21% CTR (+23% dated pages, +20% dateless), +4.9% in-carousel bookings, both from online A/B tests.

**Fit for a dating app:** medium — the multi-valued utility-label ranking scheme (booking=1, contact=0.25, click=0.01, rejection=−0.4) maps cleanly onto a dating label set (match=1, like-sent=0.25, view=0.01, left-swipe=−0.4), and "rejections as explicit negatives" is a genuine reciprocal-preference-encoding pattern; however there is no capacity-throttling or exposure-redistribution mechanism, since Airbnb listings self-limit via calendar availability rather than algorithmic exposure control, which a dating app cannot rely on (profiles never "sell out").

**Confidence that the item is real and described correctly:** high — all three NotebookLM queries returned grounded, internally consistent answers (`sources_used` correctly scoped), with specific formulas, dataset scale (800M sessions, 4.5M listings, 50M users), and A/B results matching the well-known published KDD 2018 Airbnb paper.

---

## Project Relevance

**Medium project relevance, concentrated in one mechanism.** The paper's "rejections as explicit negatives" training scheme is the most directly transferable idea to reciprocal/mutual-interest scoring: a dating app could similarly collect (swiper-type, swipee-type) pairs from left-swipe/rejection events and use them as an explicit negative term in a shared embedding objective, pulling apart the vectors of users unlikely to reciprocate — directly analogous to Airbnb pushing apart guest-types that hosts tend to reject. The multi-valued LambdaRank utility-label scheme (booking=1, contact=0.25, click=0.01, rejection=−0.4) also transfers cleanly as a template for jointly optimizing a dating ranker across match/like/view/reject outcomes instead of guest-side relevance alone.

What does not transfer: the embedding method and negative sampling scheme account for host *preference* (who tends to reject whom) but not host *capacity* at all — there is no backlog, load, or "currently oversubscribed" signal anywhere in the architecture. Airbnb listings self-throttle through calendar-based availability (a booked listing is mechanically removed from the pool for those dates), a natural capacity limiter that has no equivalent in dating, where profiles remain permanently visible and cannot "sell out." A direct port of this paper's method would solve reciprocal-interest prediction but would need an entirely separate mechanism bolted on to handle capacity-aware exposure allocation and redistribution away from over-subscribed users — this paper offers no template for that half of the problem.
