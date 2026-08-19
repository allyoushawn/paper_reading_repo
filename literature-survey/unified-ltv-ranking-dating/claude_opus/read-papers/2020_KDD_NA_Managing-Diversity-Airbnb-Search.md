# Paper Analysis: Managing Diversity in Airbnb Search

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/05_Post-ranking/2020 (Airbnb) (KDD) Managing Diversity in Airbnb Search.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Abdool, Haldar, Ramanathan, Sax, Zhang, Manaswala, Yang, Turnbull, Zhang, and Legrand (Airbnb) describe a multi-year effort to manage result-set diversity in Airbnb's two-sided search-ranking system, motivated by the observation that its pairwise-loss DNN ranker (trained to score each listing independently given query/user features) produced top results tightly clustered on price and location, since the model had no mechanism to see or reason about the other listings ranked alongside it. They define diversity via two metrics — Mean Listing Relevance (MLR, a position-discounted, listing-similarity-penalized relevance score generalizing MMR) and distance-to-an-ideal-distribution (Hellinger distance) for specific attributes, first location (an ideal distribution built from a KD-tree over aggregated user-engagement signal per query) and then price (an ideal normal distribution centered on a query-specific expected price) — and try four successive second-stage rerankers layered on an unchanged base ranker: (1) a greedy MLR-maximizing reranker (net-negative online — over-diversified and created friction); (2) a location-specific reranker with a hand-derived NDCG + Hellinger-distance loss optimized via simulated annealing (positive online: +1% new-user bookings, +3.6% China bookings; launched to production for 2+ years); (3) a single combined differentiable loss (pairwise relevance + a novel surrogate cross-entropy loss enabling gradient-based distribution matching, mixing location and price diversity terms) that was neutral-to-negative online (hard to tune the price term, hurt new-guest bookings by over-showing expensive listings); and (4) a "query context embedding" model using an LSTM to encode the top-N candidate listings' listwise context into a single embedding, re-scoring the top-K by Euclidean distance to this learned "ideal listing" embedding — the best offline result across all diversity/relevance metrics simultaneously, and positive online (+1.2% NDCG, +0.44% overall bookings, +0.61% new-guest bookings), launched to production.

## 2. Experiment Critique

All approaches are evaluated identically: offline via % change in MLR/NDCG and location/price-diversity-distance metrics relative to the production DNN baseline (Tables 3–4), then online via A/B test on live Airbnb Search traffic. The paper is unusually candid about negative and neutral results (the greedy MLR reranker and the combined-loss approach), which strengthens its credibility as an engineering account, though exact sample sizes, test durations, and significance levels for the online tests are not given beyond the qualifier "statistically significant" attached to specific metrics. No holdout/replication study is described, and all evaluation is internal to Airbnb's proprietary search logs — fully unreproducible outside the company.

## 3. Industry Contribution

All four solutions are implemented as second-stage rerankers on top of an unchanged base DNN ranking model, a deliberately low-blast-radius integration pattern repeated across every iteration. The paper documents concrete engineering tradeoffs: groupwise-scoring/listwise-context architectures from prior literature were rejected upfront for latency risk; the KD-tree-based ideal-location-distribution required an offline aggregation pipeline over engagement data; the surrogate-loss trick for matching a bucketed target distribution (Table 1's abstracted TensorFlow code) was engineering effort spent specifically to make a non-differentiable objective trainable by gradient descent; and the final LSTM-based query-context-embedding model is scoped to a bounded top-N (~1000) candidate window with a further top-K rerank, controlling training-data size and keeping the online architecture aligned with what was trained offline.

## 4. Novelty vs. Prior Work

Builds on Ai et al.'s listwise context model for ranking refinement (SIGIR 2018) and groupwise scoring functions (ICTIR 2019) as motivating architectures, but states these did not fit Airbnb's problem formulation directly (groupwise scoring risked too much latency). Distinguishes its Mean Listing Relevance metric from classic MMR (Carbonell & Goldstein, 1998) by adding positional discounting (motivated by empirical CTR-by-position, Figure 4) and by using the mean rather than max over already-selected items as the aggregate distance penalty, to avoid MMR's implicit "one item per category" assumption. Also distinguishes itself from α-NDCG (Clarke et al., 2008), noting its subtopic-relevance framework does not map cleanly onto continuous-valued, highly variable listing attributes.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Airbnb Search logs/booking data | Offline (proprietary query/booking records) | No | Used for training the base DNN, all second-stage rerankers, and the KD-tree ideal-location-distribution aggregation |
| Airbnb Search live traffic | Online (multiple A/B tests across ~2+ years of iteration) | No | Each of the four approaches (greedy MLR, location diversity, combined loss, query context embedding) was tested online against the production baseline |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Managing Diversity in Airbnb Search," Mustafa Abdool, Malay Haldar, Prashant Ramanathan, Tyler Sax, Lanbo Zhang, Aamir Manaswala, Lynn Yang, Bradley Turnbull, Qing Zhang, Thomas Legrand (Airbnb), KDD 2020, pp. 2952–2960. URL: https://doi.org/10.1145/3394486.3403345 |
| 2 | Source type | Industry paper (Airbnb) |
| 3 | Direction | D8 |
| 4 | Problem setting | Two-sided marketplace search ranking (hosts vs. guests) where a pairwise-relevance-trained DNN produces top results overly concentrated on similar price/location, degrading guest choice and experience; a multi-year account of defining and optimizing for result-set diversity as a second-stage reranking problem on top of an unchanged base ranker. |
| 5 | Objective and label definition | No retention/revenue label — the target is a diversity metric (MLR, or Hellinger distance to an ideal location/price distribution) traded off against relevance (NDCG using binary booked/non-booked relevance). No time horizon beyond a single search session/result page; no delayed-label or censoring treatment anywhere — "booked" is the terminal, immediately observable label for the pairwise relevance loss. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. Every model is trained to predict booking probability (pairwise) and/or match a target listing-attribute distribution; there is no discussion of the causal effect of showing a more diverse result set versus what would have happened otherwise. |
| 7 | Model architecture | Base ranker: DNN trained with pairwise cross-entropy loss on booked vs. non-booked listing pairs. Four second-stage rerankers layered on top over time: (a) greedy MLR-maximizing selection; (b) a location-diversity reranker optimized via simulated annealing against a loss combining NDCG and Hellinger distance to a KD-tree-derived ideal location distribution; (c) a combined-loss DNN using a novel surrogate cross-entropy loss to make distribution-matching differentiable, jointly optimizing pairwise relevance + location distribution + price distribution losses; (d) a two-tower architecture where an LSTM encodes the top-N candidate listings into a "query context embedding" (concatenated with query/user features), and listings are re-scored on the top-K by Euclidean distance between their embedding and this learned ideal-listing embedding, trained with the same pairwise loss on embeddings. |
| 8 | Credit assignment | Not a temporal/session-outcome-to-item problem — this is a within-slate mechanism, structurally the same family as the Alibaba mutual-influence paper in this batch: an item's ranking score is explicitly made a function of the other items in the same result set, either via a hand-crafted distance-to-ideal-distribution penalty or, in the final architecture, via a learned listwise-context embedding that all items in the slate are then scored against. No cross-time or user-level-outcome attribution is present. |
| 9 | Training data and counterfactual handling | All models trained on logged booked/non-booked pairs from Airbnb's own historical search+booking logs, generated under the platform's existing (evolving) production ranking policy; no explicit counterfactual, IPS, or off-policy correction is discussed for this exposure bias in any of the four iterations. |
| 10 | Offline and online evaluation | Offline — % change in MLR and NDCG (Table 3), and % change in location/price-diversity-distance metrics (Table 4), relative to the production DNN baseline, for each of the four approaches. Online — A/B tests on live Airbnb Search traffic, reported via booking-rate and NDCG deltas; the paper explicitly flags that offline and online results diverged for two of the four approaches (greedy reranker: offline MLR gain but online-neutral-to-negative; combined loss: offline gains but online-neutral, attributed to over-showing extreme-priced listings). |
| 11 | Reported gains | Location diversity reranker (online A/B, production for 2+ years): +1% bookings from new users (statistically significant), +3.6% bookings from China. Query context embedding model (online A/B, launched to production): +1.2% NDCG ("one of the largest in the past few years"), +0.44% overall bookings, +0.61% bookings from new guests. Greedy MLR reranker and combined-loss model: offline MLR/diversity-distance gains (Tables 3–4) that did not translate to positive online bookings. |
| 12 | Applicability to a two-sided dating recommender | Directly relevant as a worked example of diversity-vs-relevance tradeoff engineering on a two-sided marketplace, including the discovery that over-optimizing a diversity metric alone degrades user experience (a success-paradox-adjacent lesson: more choice is not unconditionally better). It does not address reciprocity or the supply (host) side's own outcomes/congestion at all — diversity here is defined and evaluated purely from the demand (guest) side. |
| 13 | Unverified claims | The claim that "increasing the proportion of listings within extreme price ranges" caused the statistically significant decrease in new-guest bookings under the combined-loss approach is presented as "the most likely explanation" and a supported hypothesis, not a proven causal mechanism — the paper itself calls it a hypothesis and does not run a dedicated experiment isolating that specific mechanism. |

## Project Relevance

Speaks to **Q7** most directly among this batch: Airbnb explicitly frames its platform as two-sided, and the paper's central empirical finding — that a pure relevance-only pairwise model concentrates results in a way that hurts the user, and that naively maximizing a diversity metric (the greedy reranker) also hurts the user by over-diversifying — is a directly transferable caution for any dating-app ranking objective that adds a secondary term (diversity, revenue, retention) on top of a primary relevance/match-quality score: post-hoc, greedy optimization of the secondary term is shown here, empirically, to create friction and net-negative outcomes, while a differentiable single loss and, further, a *learned* listwise-context embedding, generalized far better online. This is a strong existence proof for the project's own preference (per the README) for a single unified model over a fixed post-hoc blend. Also touches **Q4**: the paper's own architectural arc — fixed heuristics, then a hand-weighted combined loss, then one learned listwise embedding — is a case study in the fixed-fusion → learned-fusion → single-value-head progression Q4 asks about, applied to a diversity objective rather than a long-term-value objective.

**Low relevance to Q1, Q2, Q3, Q5, Q8** as the survey defines them: there is no retention/revenue objective, no delayed label, no incrementality framing, and no item-level attribution of a *user-level delayed* outcome (credit assignment here is within-slate/diversity-based, not across time). It is included in this batch for its item-interaction and staged-migration-of-objective lessons, not as an LTV or credit-assignment reference per se.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Mustafa Abdool, Malay Haldar, Prashant Ramanathan, Tyler Sax, Lanbo Zhang, Aamir Manaswala, Lynn Yang, Bradley Turnbull, Qing Zhang, Thomas Legrand
- **Affiliations:** Airbnb
- **Venue:** KDD 2020 (Applied Data Science Track), pp. 2952–2960
- **Year:** 2020
- **Relevance:** Core
- **Priority:** 3
- **nlm:cf3ee103**
