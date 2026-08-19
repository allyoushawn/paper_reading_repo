# Paper Analysis: Building a Large-Scale Recommendation System: People You May Know

**Source:** LinkedIn Engineering Blog, authored by Viral Gupta, Aman Gupta, Aastha Nigam (Feb 6, 2024), NotebookLM source_id `72b12e20-b22c-44df-8084-499d857af2dc`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Building a Large-Scale Recommendation System: People You May Know
**Authors:** Viral Gupta, Aman Gupta, Aastha Nigam (LinkedIn)
**Abstract:**
Engineering blog describing how LinkedIn's "People You May Know" (PYMK) connection-recommendation feature was scaled over two years into a four-stage funnel that scores hundreds of billions of candidate connections daily for 1B+ members, balancing relevance, fairness, and diversity while keeping serving latency low.

**Key contributions:**
- A four-stage funnel architecture — L0 candidate generation, L1 light ranker, L2 rich ranker, Re-Ranker — each reducing the search space for the next while using progressively heavier models.
- Reciprocal-style scoring in L2: deep neural networks predict both the probability an invitation is *sent* and the probability it is *accepted*.
- A Re-Ranker stage combining fairness re-ranking (age/gender parity), diversity re-ranking, and explicit throttling of over-recommended "platform power users," with weights tuned via Bayesian optimization.
- Reports that offline metrics (Recall@k, AUC, ECE) routinely diverge from online A/B results, so online testing is treated as the trusted signal.

**Methodology:**
L0 candidate generation combines graph-based random walks, embedding-based retrieval, and location/heuristic sources, evaluated via Recall@k (k≈3–5k). L1 uses logistic regression/XGBoost to calibrate and reduce candidates from these heterogeneous sources to a few hundred (Recall@k, k≈500–800). L2 uses deep neural networks over member-candidate pair features to predict invite-sent / invite-accepted probability and value (AUC, Precision@k, ECE). The Re-Ranker applies fairness, diversity, and power-user-throttling adjustments, with per-model combination weights estimated via Bayesian optimization.

**Main results:**
No specific numbers are disclosed. The authors state only that launching the multi-stage system "delivered some of the biggest improvements in member engagement and retention in the past 6 years."

---

## 2. Experiment Critique

**Design:** Internal comparisons only — L0 candidate-generation sources against each other, calibrated vs. uncalibrated L1 combination, and the new pipeline against LinkedIn's prior production PYMK system. No external baselines.

**Statistical validity:** Not specified in source — no sample sizes, confidence intervals, or significance tests reported.

**Online experiments (if any):** A/B tests run over multiple months are described as the authoritative evaluation method, explicitly because offline metrics (Recall@k, AUC, ECE) are said to diverge from online performance due to presentation bias, deployment errors, and train/serve data-distribution shift. No concrete lift numbers are given.

**Reproducibility:** Not reproducible — proprietary production graph and interaction logs, no code or data release.

**Overall:** A credible, detailed industrial case study, but not independently verifiable; claims of "biggest improvements in 6 years" are qualitative only.

---

## 3. Industry Contribution

**Deployability:** Already deployed in production at LinkedIn scale (1B+ members, hundreds of TB of data and hundreds of billions of candidate connections processed daily).

**Problems solved:** Real-time, multi-objective candidate scoring for a reciprocal "connection" recommendation problem (relevance, invite-accept likelihood, fairness, diversity, anti-power-user throttling) under billion-item latency constraints.

**Engineering cost:** High — four distinct model classes (graph/embedding/heuristic generators, XGBoost calibration, deep neural rankers, Bayesian-optimization re-ranking) plus ongoing challenges the authors name explicitly: stage-coupling tradeoffs (tight coupling = more accurate but slower to iterate) and unresolved feedback loops across a multi-stage system.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Practical scaling/productionization of a multi-stage funnel over two years, not a novel algorithm; positioned as the successor to LinkedIn's own 2020 PYMK architecture ("Building a Heterogeneous Social Network Recommendation System").

**Prior work comparison:** Cites foundational scaling techniques (negative sampling, hierarchical softmax, adaptive importance sampling), XGBoost for the L1 calibration stage, and general fairness-in-recommendation / ecosystem re-ranking literature for the Re-Ranker.

**Verification:** Not independently verifiable — an engineering blog post with no external benchmarking against non-LinkedIn systems.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| LinkedIn production social graph & interaction logs (1B+ members, hundreds of TB/day) | — | Not accessible (proprietary) | Internal telemetry only |

**Offline experiment reproducibility:** Not reproducible — no data or code released.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Viral Gupta, Aman Gupta, Aastha Nigam
**Affiliations:** LinkedIn
**Venue:** LinkedIn Engineering Blog
**Year:** 2024
**PDF:** Not fetched — analyzed via NotebookLM source; not accessed as local file
**Relevance:** Related — strong adjacent-marketplace system design (reciprocal invite scoring + power-user throttling), but no disclosed formulas or numeric results
**Priority:** 1 (per queue tier)

---

## Bibliography Fields

- **title:** Building a Large-Scale Recommendation System: People You May Know
- **authors or organization:** Viral Gupta, Aman Gupta, Aastha Nigam — LinkedIn Engineering
- **year:** 2024
- **venue or type:** LinkedIn Engineering Blog (industry engineering post, not peer-reviewed)
- **link:** LinkedIn Engineering Blog, "Building a Large-Scale Recommendation System: People You May Know" — exact URL not confirmed from source content
- **tier tag:** Tier 1 — Adjacent marketplace (professional-network reciprocal connections), multi-stage ranking + fairness re-ranking
- **what they did (≤80 words):** Describes LinkedIn's four-stage PYMK funnel (candidate generation → light ranker → rich ranker → re-ranker) built over two years to score >1B members and hundreds of billions of candidate connections/day. The rich ranker predicts both invite-sent and invite-accepted probabilities; the final re-ranker applies fairness (age/gender parity), diversity, and power-user-throttling adjustments tuned via Bayesian optimization, validated via online A/B testing rather than offline metrics alone.
- **mechanism relevant to two-sided balancing (≤50 words):** L2 ranker jointly predicts P(invite sent) and P(invite accepted) — a bilateral-interest proxy; the Re-Ranker explicitly throttles over-recommended "power users," directly analogous to capping exposure to over-subscribed desirable users and redistributing it to under-exposed candidates.
- **metrics used, and the reported effect:** Recall@k (L0/L1), AUC/Precision@k/ECE (L2), log-likelihood/diversity metrics (Re-Ranker), online A/B member engagement & retention; no numeric lift disclosed beyond "some of the biggest improvements ... in the past 6 years."
- **fit for a dating app:** medium — reciprocal accept/send scoring and power-user throttling transfer conceptually well, but the domain (professional networking, not mutual romantic interest) and the total absence of disclosed formulas/numbers limit direct transferability.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with extensive direct quotes across all three queries; source_id validated each time; matches a real, publicly findable LinkedIn engineering blog post by named authors).

---

## Project Relevance

This source contains two mechanisms that transfer directly to the dating-market framing. First, the L2 rich ranker's joint prediction of "invitation sent" and "invitation accepted" probabilities is a reciprocal-interest proxy structurally close to what a dating platform needs: predicting P(A likes B) × P(B likes back) rather than one-sided attractiveness. Second, the Re-Ranker's explicit "power-user throttling" — penalizing over-recommendation of already-oversubscribed members — is a direct analogue of capacity-aware exposure allocation away from over-subscribed, highly desirable users; on a dating app the same logic would throttle exposure of "superstar" profiles once their reply capacity is saturated, redistributing impressions to under-exposed but qualified candidates. The source's insistence on trusting online A/B results over offline metrics because of feedback-loop and distribution-shift effects also reinforces the project's north star of ecosystem-level, interference-aware evaluation over single-viewer offline metrics — though the source explicitly flags that multi-stage feedback loops remain an unsolved problem, which is directly relevant to interference-aware A/B testing under the project's capacity constraints. The source does **not** address market-design levers (like limits, curated batches, signaling) at all — it is purely an algorithmic ranking/re-ranking system.
