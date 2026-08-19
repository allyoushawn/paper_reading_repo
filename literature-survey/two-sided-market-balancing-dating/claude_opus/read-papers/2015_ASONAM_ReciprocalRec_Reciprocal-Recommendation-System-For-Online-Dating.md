# Reciprocal Recommendation System for Online Dating

- **notebook source_id:** `f3e7044f`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Online dating recommendation differs from item recommendation because a good match must also be interested back in the service user, not just match the service user's taste. The authors build a generalized reciprocal-recommendation framework that computes a "reciprocal score" as the harmonic mean of two directional compatibility scores between a service user and a candidate, using both profile-attribute (content) similarity and message-graph-based similarity (who contacts/receives from whom). Evaluated on 200,000 users and ~2M messages from a major Chinese dating site (Baihe.com), their collaborative-filtering variants (CF1-CF4) significantly beat prior content-based (RECON) and hybrid collaborative-filtering (HCF) baselines in precision/recall of predicting actual reciprocated contacts, and effective recommendations land in the top 30-50% of the ranked list. They also find a gender asymmetry: males optimize for their own interest and ignore their attractiveness to others, while females weight both directions (their own attractiveness and the other side's interest).

## Method
**Algorithm 1 — Reciprocal Score(x, y):** for service user x and candidate y, compute two directional compatibility scores s(x,y) and s(y,x) by summing a similarity function over each user's neighbor set in a directed message graph, normalize each by neighbor-set size, then combine as the harmonic mean: `2 / (s(x,y)^-1 + s(y,x)^-1)`, or 0 if either side is non-positive. `Neighbor_1`/`Neighbor_2` and `Similarity_1`/`Similarity_2` are pluggable, giving a family of algorithms:
- **Content-based (CB1=RECON, CB2):** neighbors = out-contacts Se(); similarity = profile-attribute overlap (CB1 bins numeric attributes into categories; CB2 keeps numeric attributes continuous, avoiding information loss at bin boundaries).
- **Collaborative-filtering (CF1-CF4):** built from two graph-based Jaccard-coefficient similarity measures over the bipartite message graph — *interest similarity* (do x and y send messages to the same people?) and *attractiveness similarity* (do x and y receive messages from the same people?). CF1-CF4 differ in which direction (out-neighbors Se() vs in-neighbors Re()) and which similarity function is applied to each side, giving four distinct combinations of "mutual attractiveness," "mutual interest," and asymmetric interest/attractiveness pairings.

## Datasets and Baselines
Real-world dataset from Baihe.com (major Chinese online dating site): 200,000 users sampled November 2011 (139,482 male / 60,518 female), full profile attributes (39 features, 20 hand-selected) plus two months of message send/receive traces. Service users filtered to those with ≥5 messages in a 10-day training window (24,602 male, 8,250 female), yielding 730,110 training messages and 270,294 test messages. Baselines: **RECON** (Pizzato et al. 2010, content-based) and **HCF** (Krzywicki et al. 2010, hybrid collaborative filtering) — both reproduced as CB1 and compared against directly.

## Results
- Initial-contact reply rates (Table 1): male→female 1,586,059 initial contacts, 150,917 reciprocated (9.5% reply rate); female→male 328,645 initial contacts, 58,946 reciprocated (17.9% reply rate).
- CB2 (continuous numeric similarity) significantly outperforms CB1/RECON in both I-Precision/I-Recall and R-Precision/R-Recall; the improvement is more pronounced for females than males.
- CF1-CF4 (the paper's collaborative-filtering algorithms) significantly outperform HCF for both genders on both metric families. For males, CF4 (interest of service user in candidate + attractiveness of candidate to service user) is the strongest, especially on I-Precision/I-Recall. For females, CF1 and CF2 perform similarly to each other; CF3 overtakes the others at large top-K on R-metrics; no single algorithm dominates for females.
- Ranking effectiveness: across CF1-CF4, relevant (actually-reciprocated) recommendations land, on average, in the top 30-50% of the recommendation list (except CF3 for females, which ranks around the halfway point).
- All precision/recall/ranking-position numbers are reported only as bar charts and line plots in the paper (Figs. 8-16); no exact numeric precision/recall table is given beyond the dataset statistics above. No significance tests (p-values) are reported for the CF-vs-baseline gaps.

## Limitations
The paper only models on-platform communication and cannot observe if users move contact off-platform. The site is strictly heterosexual, so the network is a fixed male/female bipartite graph — their approach does not generalize as-is to non-binary matching structures. No single CF variant dominates across genders and metrics, so a real system would need to pick a variant per use case. The reciprocal-score construction (harmonic mean of two similarity-derived scores) has no formal capacity or exposure-budget notion — it ranks candidates for one service user in isolation, with no cross-user allocation or fairness constraint.

## Heavily Cited Prior Works
- Pizzato, Rej, Chung, Koprinska, Kay (2010) — RECON: a reciprocal recommender for online dating (RecSys)
- Krzywicki, Wobcke, Cai, Mahidadia, Bain, Compton, Kim (2010) — Interaction-based collaborative filtering for online dating (WISE)
- Li & Li (2012) — MEET: a generalized framework for reciprocal recommender systems (CIKM)
- Tu, Ribeiro, Jensen, Towsley, Liu, Jiang, Wang (2014) — Online Dating Recommendations: Matching Markets and Learning Preferences (WWW SocialRecSys workshop) — companion paper in this same batch
- Kutty, Nayak, Chen (2010) — A people-to-people recommendation system using graph mining techniques (WWW)
- Cai, Bain, Krzywicki, Wobcke, Kim, Compton, Mahidadia (2010) — Learning collaborative filtering for people-to-people recommendation (ICDM)
- Brozovsky & Petricek (2007) — Recommender system for online dating service

## Bibliography Fields
- **title:** Reciprocal Recommendation System for Online Dating
- **authors or organization:** Peng Xia, Benyuan Liu, Yizhou Sun, Cindy Chen — University of Massachusetts Lowell / Northeastern University
- **year:** 2015
- **venue or type:** ASONAM (IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining), per manifest — the PDF read is the arXiv preprint (arXiv:1501.06247v2) and does not itself print a venue banner, but the conference/year is consistent with the manifest tag and no contradicting evidence was found.
- **link:** https://arxiv.org/pdf/1501.06247
- **tier tag:** Tier 2 applied-on-real-platform-data
- **what they did (≤80 words):** Built a generalized reciprocal-recommendation framework for online dating combining content-based (profile attribute) and graph-based (message-history) similarity measures into a single reciprocal score (harmonic mean of two directional compatibility scores). Evaluated content-based and collaborative-filtering variants against prior RECON and HCF baselines on 200K users / 2M messages from a Chinese dating site, showing large precision/recall gains and a gender asymmetry in how users weight own-interest vs. own-attractiveness.
- **mechanism relevant to two-sided balancing (≤50 words):** The reciprocal-score harmonic mean of two directional compatibility scores is a clean, reusable formalization of "like-back probability" for Layer 1 (reciprocal scoring); it is per-candidate-pair and carries no exposure budget or capacity constraint, so it does not itself deliver Layer 2 (capacity-aware allocation).
- **metrics used, and the reported effect:** I-Precision/I-Recall (recommended users actually contacted) and R-Precision/R-Recall (recommended users who reciprocated); reported only via bar charts, no exact figures in text. Baseline reply rates: 9.5% (male→female), 17.9% (female→male). CF1-CF4 significantly beat HCF; CB2 significantly beats CB1/RECON; no p-values reported.
- **fit for a dating app:** high — this is a reciprocal-scoring method (Layer 1) validated on a real dating platform with real reply-behavior ground truth, directly transferable as a like-back probability model, though it has no capacity-awareness of its own.
- **confidence that the item is real and described correctly:** high — full 24-page PDF read directly; the paper is corroborated by cross-citation in a companion paper (Tu et al. 2014, this same batch) which also cites it.

## Project Relevance
Addresses **Layer 1 (reciprocal scoring)** directly: the reciprocal-score algorithm is a working, real-data-validated instance of "like-back probability" estimation, built from exactly the kind of interaction-graph signal (who messages whom, who replies) a dating platform would have. It does not address **Layer 2 (capacity-aware exposure allocation)** — the score is computed for one service user's candidate list at a time, with no notion of the candidate's finite reply capacity or of redistributing exposure away from over-subscribed, highly attractive users. It does not touch **Layer 3 (market-design levers)** or **Layer 4 (ecosystem metrics/interference)** at all — evaluation is single-user precision/recall, not match-Gini, share-with-≥1-match, or two-sided retention. The paper's own finding that CF4 (own-interest-weighted) wins for males while CF1/CF2/CF3 (mutual/attractiveness-weighted) are more competitive for females is a useful empirical data point for a reciprocal-scoring model that may need gender- or role-conditioned formulations.

## Reverse Citation Map
