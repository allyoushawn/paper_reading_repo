# Coverage Evaluation — Codex-sol

Date: 2026-08-19

Status key: **Covered** = sufficient evidence for a decision; **Thin—covered** = decision-relevant evidence exists but transfer, causal, or anchor coverage is limited; **Gap** = insufficient evidence. Thin—covered items count as covered under the Phase 5 decision-making criterion.

## Request Outputs (4/4 covered)

| Item | Status | Evidence |
|---|---|---|
| R1. Industry-first reference list | Covered | `literature-review.md` contains 45 annotated items; Tier 1+2 is 39/45 (86.7%). |
| R2. Per-reference mechanism, metric/effect, and dating-app map | Covered | Every bibliography item has mechanism, metrics/effect, fit, confidence, link, year, venue/type, and tier fields. |
| R3. Synthesis of design patterns | Covered | Seven patterns plus a six-row design-pattern matrix cover reciprocal scoring, capacity-aware scoring, constrained reranking, market design, metrics, and evaluation. |
| R4. Gaps and next searches | Covered | Six open questions and exactly five next searches appear in `literature-review.md`. |

## Core Keywords (6/6 covered)

| Keyword | Status | Evidence |
|---|---|---|
| Two-sided market balancing | Covered | Layered market-system synthesis and market-wide allocation evidence. |
| Reciprocal recommendation | Covered | D1 has 11 primary entries and 19 multi-tagged entries. |
| Exposure allocation | Covered | D4 and the matrix cover stochastic exposure, assortment, eligibility control, and redistribution. |
| Capacity-constrained recommendation | Thin—covered | LiJAR, CapMF/CapBPR, application limits, Thresholded Eligibility Control, and Exposure-Constrained Deferred Acceptance cover several capacity definitions; calibrated conversation capacity is unresolved. |
| Congestion in matching markets | Covered | D3 plus market-design evidence explain overapplication, screening load, and concentration. |
| Dating-app recommendation | Covered | Direct Tinder, Hinge, OkCupid, Tapple, Baihe, and dating-research evidence anchors transfers from adjacent markets. |

## Must-Include Clusters (5/5 covered)

| Cluster | Status | Evidence and explicit anchor omissions/substitutions |
|---|---|---|
| A. Dating platforms describing their matching | Thin—covered | Selected: Tinder newsroom and TinVec, OkCupid, and Hinge’s 2025 explainer; omitted anchors: Hinge “Most Compatible,” Hinge Gini coverage, eHarmony “Data Science of Love,” Coffee Meets Bagel infrastructure, and Bumble Tech, with Bumble recorded as a null. |
| B. Industry reciprocal/two-sided balancing | Covered | Selected CyberAgent, BOSS Zhipin, LinkedIn LiJAR and impression discounting, Spotify fairness, and adjacent reranking; omitted anchors: Spotify “Recommendations in a Marketplace,” Airbnb host-preference modeling, and Airbnb embedding ranking. |
| C. Applied real dating/matching data | Covered | Selected assortment theory, search restrictions, congestion, signaling, market thickness, online-dating behavior, and reciprocal dating data; omitted anchors: *Improving Match Rates in Dating Markets Through Assortment Optimization* and *Online Dating Recommendations: Matching Markets and Learning Preferences*. |
| D. Two-sided experimentation | Covered | Selected two-sided randomization, multiple randomization, Airbnb cluster meta-experiment, UniCoRn, matching-market off-policy evaluation, and shadow prices; omitted anchors: Lyft’s engineering post and DoorDash’s switchback post, with primary papers or other industry evidence substituting. |
| E. Academic lever-mapped methods | Covered | Selected reciprocal survey, people-to-people RECON lineage, Lorenz fairness, exposure fairness, and capacity constraints; omitted as direct cards: Kleinerman et al.’s weighted-harmonic paper, the original short RECON paper, and Neve–Palomares latent-factor aggregation, although Kleinerman and RECON are represented in the finalized tracker through verified descendants or the longer dating study. |

## Search Directions (8/8 covered)

| Direction | Status | Evidence |
|---|---|---|
| D1 Reciprocal recommendation | Covered | 11 primary / 19 tagged; strongest area. |
| D2 Market and ecosystem framing | Thin—covered | 5 primary / 7 tagged; decision-ready fairness and exposure evidence, but hard capacity calibration is sparse. |
| D3 Capacity and congestion | Covered | 4 primary / 8 tagged; forecasts, caps, penalties, and receiver budgets. |
| D4 Constrained allocation and reranking | Covered | 4 primary / 14 tagged; broad mechanisms, with limited direct dating field replication. |
| D5 Market-design levers | Covered | 6 primary / 10 tagged; caps, scarce signaling, menu size, initiation rules, and market thickness. |
| D6 Objectives and metrics | Thin—covered | 5 primary / 8 tagged; match distribution and wasted contacts are strong, while conversations and two-sided retention magnitudes are sparse. |
| D7 Interference-aware evaluation | Covered | 6 primary / 8 tagged; multiple deployed or empirical adjacent-market designs plus reciprocal off-policy evaluation. |
| D8 Chinese and Japanese sources | Thin—covered | 4 primary / 7 tagged; useful Japanese industry and Chinese experimentation evidence, but official Chinese dating-ranking engineering sources were null. |

## Project Context Fitness (8/8 addressed; PASS)

| Project-context statement | Status | Directly addressing cluster/evidence |
|---|---|---|
| P1. A match requires mutual likes and each impression consumes viewer attention plus recipient reply capacity. | Covered | Reciprocal-scoring cluster establishes bilateral success; capacity/congestion cluster establishes scarce receiver attention. |
| P2. Skewed desirability overloads a small group, wastes surplus likes, and starves others. | Covered | OkCupid concentration, online-dating desirability, LiJAR demand buckets, and market-clearing/congestion evidence directly diagnose the failure mode. |
| P3. Optimize total matches, conversations, match spread, and retention on both sides—not single-viewer CTR/CVR. | Thin—covered | Reciprocal coverage, entropy, Gini/Lorenz, effective interactions, and retention are all represented, but no selected study measures the entire outcome set together. |
| P4. Treat the problem as allocation under capacity limits with feedback loops. | Covered | LiJAR, congestion limits, capacity constraints, assortment allocation, Thresholded Eligibility Control, and Exposure-Constrained Deferred Acceptance form the core allocation cluster. |
| P5. Reciprocal scoring should combine like-back probability with the other side’s capacity. | Thin—covered | Bilateral scoring and capacity-aware allocation are separately strong, and transferable-utility or receiver-budget methods connect them; no field study jointly calibrates actual reply capacity and like-back probability. |
| P6. Capacity-aware exposure allocation should cover per-user limits, redistribution, assortment, fairness reranking, or pacing. | Covered | The capacity-aware and constrained-reranking matrix rows cover every named mechanism class except a directly tested dating pacing controller. |
| P7. Market-design levers include like limits, curated batches, signaling, and which side searches. | Covered | Application limits, choice restriction, virtual roses, directional search, and market-thickness evidence directly address these levers. |
| P8. Ecosystem metrics and experiments must address concentration, wasted likes, two-sided retention, and interference. | Covered | D6 supplies the scorecard; D7 supplies two-sided, cluster, multiple-randomization, shadow-price, and off-policy designs. |

## Result

- Covered requirement items: **31/31 = 100%** (4 Request + 6 keywords + 5 Must-Include clusters + 8 directions + 8 Project Context statements).
- Thin—covered items: 7; they are evidence limitations or transfer risks, not decision-blocking gaps.
- Gaps: **0**.
- Project-context fitness: **PASS**, explicitly including reciprocal scoring, capacity-aware allocation, market-design levers, and metrics/interference.
- Scope caveat: the codex-sol bibliography has 45 references, within the authoritative 30–50 target; the industry mix is high and every required decision dimension has sufficient analyzed evidence, while omitted anchors are listed above rather than silently counted as covered.
