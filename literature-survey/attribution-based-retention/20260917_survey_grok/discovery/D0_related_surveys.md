# D0 — Q2-Relevant Papers Harvested from Internal Surveys

**Harvest date:** 2026-09-17  
**Sources scanned:**
- `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/codex-sol/` (most complete variant; 120-source corpus)
- `/Users/fox/Projects/paper_reading_repo/literature-survey/two-sided-market-balancing-dating/codex-sol/` (45-source corpus)
- Parent read-papers index (2025_/2026_ filenames only; titles listed, not reprocessed)

**Q2 definition (this harvest):** Does the method produce **per-interaction credit** assigning user-level delayed retention (days-active, N-day return, active days) to a **specific in-app action or exposure**?

---

## Already in parent — do not reprocess

Titles only from `/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/read-papers/` (`2025_*`, `2026_*`):

| Year | Title |
|------|-------|
| 2025 | LiDDA: Data Driven Attribution at LinkedIn |
| 2025 | Amazon Ads Multi-Touch Attribution |
| 2025 | See Beyond a Single View: Multi-Attribution Learning for Conversion Prediction (MAL) |
| 2025 | Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations (CABB) |
| 2025 | Beyond Last-Click: Optimal Mechanism for Ad Attribution (PVM) |
| 2025 | Causal-Driven Attribution: Channel Influence from Aggregate Data |
| 2025 | DeepCausalMMM: A Deep Learning Framework for Marketing Mix Modeling with Causal Inference |
| 2025 | Generative Bid Shading in Real-Time Bidding Advertising |
| 2025 | Dynamic Synthetic Controls vs Panel-Aware Double Machine Learning for Geo-Level Marketing Impact Estimation |
| 2026 | Statistical Learning from Attribution Sets |
| 2026 | MAC: Conversion Prediction Benchmark Under Multiple Attribution Mechanisms |
| 2026 | Conversion Rate Prediction in Online Advertising: A Systematic Review |

**Note:** Parent corpus covers **conversion / ad / marketing attribution**, not in-app retention-to-action credit. LiDDA, Amazon causal-calibration MTA, MAL, CABB, and PVM assign credit to **touchpoints for conversion/purchase**, not to **N-day active/retention** from a recommender exposure.

---

## Q2-relevant papers from unified-ltv-ranking-dating (codex-sol)

### RLUR — Reinforcing User Retention in a Billion Scale Short Video Recommender System

| Field | Value |
|-------|-------|
| **Year** | 2023 |
| **Title** | Reinforcing User Retention in a Billion Scale Short Video Recommender System |
| **Venue** | WWW |
| **Company / dataset** | Kuaishou Technology; billion-scale short-video production logs |
| **URL** | https://arxiv.org/pdf/2302.01724 |
| **Per-interaction retention credit** | **Partial** — request-level MDP propagates inter-session return-time reward across requests via RL; does not identify one item/exposure's causal share of day-1/day-7 retention |
| **Method (1 sentence)** | Learns dynamic fusion weights over existing immediate-feedback score heads in an infinite-horizon request MDP that minimizes accumulated time between sessions. |
| **Attribution-based retention?** | **No (strict)** / **Partial (loose)** — optimizes retention through trajectory-level policy learning, not published per-touch causal attribution of N-day active days to a specific recommendation. |

---

### GFN4Retention — Modeling User Retention through Generative Flow Networks

| Field | Value |
|-------|-------|
| **Year** | 2024 |
| **Title** | Modeling User Retention through Generative Flow Networks |
| **Venue** | KDD |
| **Company / dataset** | City University of Hong Kong & Kuaishou Technology; KuaiRand-Pure, MovieLens-1M (simulated return via KuaiSim), Kuaishou production A/B |
| **URL** | https://arxiv.org/pdf/2406.06043 |
| **Per-interaction retention credit** | **Partial** — detailed-balance GFlowNet propagates terminal return-time/retention reward to intermediate session actions; trajectory RL credit, not identified exposure-level causality |
| **Method (1 sentence)** | Trains a continuous-action GFlowNet with step-wise engagement rewards and a terminal cross-session retention reward, deployed as dynamic score-ensemble weights in ranking stages. |
| **Attribution-based retention?** | **No (strict)** — source cards state outcome/policy optimization without incremental causal effect of an exposure; credit is flow-matching over observed trajectories. |

---

### AURO — Adaptive User Retention Optimization

| Field | Value |
|-------|-------|
| **Year** | 2025 |
| **Title** | AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems |
| **Venue** | arXiv |
| **Company / dataset** | Nanyang Technological University & Kuaishou Technology; retention simulator, MovieLens, live short-video platform (~25M DAU) |
| **URL** | https://arxiv.org/pdf/2310.03984 |
| **Per-interaction retention credit** | **No** — actor-critic RL with state abstraction for non-stationary retention optimization; no per-touch retention decomposition in indexed evidence |
| **Method (1 sentence)** | Adds state-abstraction and exploration modules to SAC-style RL so policies adapt as user return-time distributions shift across weeks. |
| **Attribution-based retention?** | **No** — retention is a session/trajectory RL objective; indexed extraction does not produce touch-level retention credits. |

---

### SEC — Stratified Expert Cloning for Retention-Aware Recommendation at Scale

| Field | Value |
|-------|-------|
| **Year** | 2025 |
| **Title** | Stratified Expert Cloning for Retention-Aware Recommendation at Scale |
| **Venue** | CIKM |
| **Company / dataset** | Kuaishou & Kuaishou Lite (200M+ DAU each); KuaiRand for offline expert stratification |
| **URL** | https://arxiv.org/html/2504.05628v2 |
| **Per-interaction retention credit** | **No** — clones policies from high-retention user strata; active-days lift at user/session level, not per-exposure credit |
| **Method (1 sentence)** | Imitation-learning framework that behavior-clones recommendation policies from users at multiple high-retention expert levels into a deployable policy network. |
| **Attribution-based retention?** | **No** — optimizes expected long-term retention via expert cloning, not attribution of active days to individual recommendations. |

---

### FID — Future Impact Decomposition in Request-level Recommendations

| Field | Value |
|-------|-------|
| **Year** | 2024 |
| **Title** | Future Impact Decomposition in Request-level Recommendations |
| **Venue** | KDD |
| **Company / dataset** | Kuaishou Technology; KuaiRand, MovieLens-1M |
| **URL** | https://arxiv.org/pdf/2401.16108 |
| **Per-interaction retention credit** | **Partial** — reward-based future decomposition assigns item-wise future impact within a request-level A2C critic; not N-day retention labels nor causal identification |
| **Method (1 sentence)** | Decomposes request-level future value in an MDP into per-item contributions via re-weighted A2C critics so list-wise policies respect uneven item-level future effects. |
| **Attribution-based retention?** | **Partial** — closest unified-survey mechanism to item-level delayed credit, but targets request-sequence future interactions, not published per-touch N-day retention attribution with causal backing. |

---

### RevisitMTL — Save, Revisit, Retain

| Field | Value |
|-------|-------|
| **Year** | 2026 |
| **Title** | Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems |
| **Venue** | AAAI |
| **Company / dataset** | Pinterest Inc.; Related Pins / Search (500M+ users; 24M-user A/B) |
| **URL** | https://arxiv.org/pdf/2511.18013.pdf |
| **Per-interaction retention credit** | **Partial** — deterministic save→profile-revisit linkage credits a Pin for same-/1-/7-day revisits; seven-day aggregation; confounding acknowledged |
| **Method (1 sentence)** | Adds a multi-task save/revisit head with a seven-day cross-session event pipeline and ranking boost for high joint save-revisit probability to lift active users. |
| **Attribution-based retention?** | **Partial** — rare industry example of **item-level multi-day surrogate attribution** tied to retention (+0.10% active users in A/B), but heuristic not causal; revisit credited only when user returns via profile, not all retention paths. |

---

### OCARM — Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling

| Field | Value |
|-------|-------|
| **Year** | 2026 |
| **Title** | Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling |
| **Venue** | arXiv |
| **Company / dataset** | Kuaishou Technology; industrial short-video RTB re-engagement (millions of users, billions of interactions) |
| **URL** | https://arxiv.org/abs/2604.25839 |
| **Per-interaction retention credit** | **No** — predicts LT1/LT7/LT30 at bid/user level using distilled post-conversion content representations; no per-touch credit vector |
| **Method (1 sentence)** | Teacher–student distillation: a privileged teacher encodes future onboarding content sequences; the student infers that representation from bid-time features to predict retention. |
| **Attribution-based retention?** | **No** — user-level retention **prediction** for re-engagement bidding, not attribution of retention days to a specific in-app recommendation action. |

---

### SlateQ — A Tractable Decomposition for Reinforcement Learning with Recommendation Sets

| Field | Value |
|-------|-------|
| **Year** | 2019 |
| **Title** | SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets |
| **Venue** | IJCAI |
| **Company / dataset** | Google / YouTube (Facebook applied RL platform cited for LTV labels) |
| **URL** | https://research.google/pubs/slateq-a-tractable-decomposition-for-reinforcement-learning-with-recommendation-sets/ |
| **Per-interaction retention credit** | **Partial** — decomposes slate LTV to item Q-values under Single Choice and Reward/Transition Dependence on Selection assumptions |
| **Method (1 sentence)** | Factorizes slate-level long-term value into additive item Q-values so RL can rank sets for LTV while reusing pCTR logits as relative appeal proxies. |
| **Attribution-based retention?** | **Partial (theoretical)** — item-level LTV decomposition under strong assumptions; unified survey notes it does not establish exposure-effect identification or N-day retention attribution in production. |

---

### ESMM — Entire Space Multi-Task Model (Q2 funnel factorization reference)

| Field | Value |
|-------|-------|
| **Year** | 2018 |
| **Title** | Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate |
| **Venue** | SIGIR |
| **Company / dataset** | Alibaba-affiliated (Taobao display advertising) |
| **URL** | https://doi.org/10.1145/3209978.3210104 |
| **Per-interaction retention credit** | **Partial (funnel only)** — probability-chain factorization links impression→click→conversion; not retention/active-days |
| **Method (1 sentence)** | Jointly trains CTR and CTCVR on all impressions and derives CVR via CTCVR=CTR×CVR with shared embeddings. |
| **Attribution-based retention?** | **No** — cited in unified survey Q2 as sequential factorization for **conversion funnel**, not attribution of N-day retention to exposures. |

---

## Q2-relevant paper from two-sided-market-balancing-dating (codex-sol)

### MRet — Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching

| Field | Value |
|-------|-------|
| **Year** | 2026 |
| **Title** | Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching |
| **Venue** | ICLR |
| **Company / dataset** | Synthetic two-sided data + undisclosed major online dating platform |
| **URL** | https://arxiv.org/abs/2602.15752 |
| **Per-interaction retention credit** | **No** (pair-level) — learns personalized retention curves and ranks pairs by **joint expected retention gain** for viewer and recommended user; no per-touch decomposition in indexed abstract |
| **Method (1 sentence)** | MRet dynamically ranks limited matching opportunities by marginal two-sided retention benefit from learned user-specific retention curves rather than match count or exposure fairness alone. |
| **Attribution-based retention?** | **No (strict)** / **Partial (market-level)** — directly optimizes ecosystem retention on dating data but does not publish per-interaction credit of N-day active to a specific shown profile; empirical magnitudes not in indexed source. |

---

## Cross-survey Q2 synthesis (from executive summaries)

**Unified LTV survey (codex-sol) Q2 finding:** Funnel factorization (ESMM), request-to-item decomposition (FID), slate Q-value decomposition (SlateQ), and trajectory reward propagation (GFN4Retention, RevisitMTL) appear in the selected corpus. **None identifies the causal contribution of one profile exposure to a later return amid many exposures and marketplace spillovers.**

**Two-sided balancing survey:** Retention enters as an ecosystem metric (MRet, ECDA horizon caveats); no per-touch retention attribution mechanism.

**Parent attribution papers (LiDDA, Amazon MTA, MAL, CABB, PVM):** Per-touch **conversion/ad** credit at industry scale; outcome is purchase/conversion, not days-active or N-day in-app retention from a recommender item.

---

## Five-line verdict: published industry attribution-based retention?

1. **Strict Q2 (per-touch causal credit of N-day retention/active-days to one in-app action):** **No** — neither internal survey nor parent corpus documents a deployed system that publishes this estimand for recommender retention.
2. **Closest partial cases:** Pinterest RevisitMTL (heuristic save→7-day revisit→active-user lift) and Kuaishou FID (item-wise future-impact decomposition within request MDP); both lack causal per-touch retention identification.
3. **Retention optimization ≠ attribution:** Kuaishou RLUR, GFN4Retention, AURO, SEC optimize retention via RL/imitation/flow networks at request or trajectory level without per-exposure retention credit tables.
4. **Adjacent industry attribution exists for conversions, not retention:** LinkedIn LiDDA, Amazon causal-calibration MTA, MAL, CABB, PVM assign touchpoint credit to **conversions**; they do not extend to **N-day active/retention** from organic in-app recommendations.
5. **Overall Q2 verdict:** **Partial** — published industry work has retention-aware ranking, surrogate multi-day item labels, and RL credit propagation, but **not** full attribution-based retention (identified per-interaction credit of days-active / N-day retention to a specific in-app action).
