# Paper Analysis: Designing Recommendation Exposure and Favorite Lists: A Field Experiment on a Spot-Work Platform

**Source:** NotebookLM source `733a9204-805a-4e36-9be7-120f1a3531dd` (arXiv, Aug 2026)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Designing Recommendation Exposure and Favorite Lists: A Field Experiment on a Spot-Work Platform
**Authors:** Not stated in the NotebookLM-extracted excerpts (self-citation pattern suggests overlap with the Timee-platform research group behind Kanayama & Otani 2024/2026 and Otani 2025 — unconfirmed).
**Abstract:**
Studies Timee, Japan's largest spot-work platform, where a greedy recommender that maximizes predicted "favoriting" probability causes **misdirected concentration**: exposure piles onto popular job templates with few actual openings, while templates with real unmet labor demand go unseen. Proposes Thresholded Eligibility Control (TEC), a fully parallelizable exposure-reallocation algorithm, validated in both calibrated simulation and a live prefecture-level randomized field experiment.

**Key contributions:**
- An economic model of the spot-work matching process (recommend → favorite → apply → FCFS match).
- Static Quota (SQ) and Adaptive Quota (AQ) baselines using capacity-based exposure quotas via round-robin Random Serial Dictatorship (RSD).
- **Thresholded Eligibility Control (TEC):** approximates AQ's capacity-aware reallocation logic but replaces AQ's sequential RSD with precomputed per-template eligibility thresholds, making recommendation-list construction independent and parallelizable per worker (O(|K_i|) per worker).
- A prefecture-level randomized field deployment (Aomori=treatment vs. Iwate=control) explicitly designed to avoid user-level interference/spillovers in a matching market.

**Methodology:**
Each template k accrues an exposure-demand score from posted capacity (x⁰_k) and unfilled capacity (x¹_k); scores are capped (no template exceeds 1 slot's worth of eligibility mass, excess redistributed proportionally) and converted into eligibility thresholds τ_k. Workers get randomized per-round selection timings; a template is eligible at a given step iff τ_k ≥ timing. Scores carry across rounds, decremented only by realized exposure — so low-favoriting-probability but high-demand templates are not starved.

**Main results:**
Simulation (calibrated to 2024 Hokkaido data): per-round job-finding rate rises from 57.6% (Greedy) → 64.2% (SQ) → 69.5% (AQ) → 70.0% (TEC); fill rate 67.4% → 82.2%. Field experiment (Jan 12–Feb 11, 2026): TEC increased matches by +9.045 per prefecture-day (DID, p<0.05) and recommendations-per-active-template by +0.571, while daily favorites were statistically unchanged — i.e., the same favoriting volume redirected toward higher-value templates.

---

## 2. Experiment Critique

**Design:**
Clean four-arm comparison (Greedy / SQ / AQ / TEC) in simulation, plus a genuinely causal live rollout. The field design uses **prefecture-level randomization** (Aomori treated, Iwate control) specifically to avoid the user-level interference/spillover problem inherent to matching-market experiments — the same problem the project's ecosystem-metrics layer needs to handle.

**Statistical validity:**
DID/ITT regressions with prefecture and date fixed effects, HAC standard errors. Authors are explicit that with only one treated and one control unit, results are "not supported by large-cluster asymptotics" and should be read as evidence from this one rollout, not as asymptotically justified inference — an honest and unusually candid caveat.

**Online experiments:**
Yes — a full month-long production A/B-style rollout on a real platform (Timee), alongside the offline simulation used to select TEC before deployment. This dual simulation-then-field-validate pipeline is a strong template for de-risking exposure-allocation changes before a live rollout.

**Reproducibility:**
All scoring/thresholding formulas are fully specified (Appendix B). Underlying production data (Timee, Hokkaido 2024; Aomori/Iwate Jan–Feb 2026) is proprietary and not released.

**Overall:**
Results support the central claim: reallocating exposure toward under-served, capacity-rich templates raises market-level matching without hurting aggregate engagement (favorites unchanged). Authors are candid that slower-moving stock variables (subscribers/template, fill rate) did not move significantly within the one-month window and may need a longer horizon — an honest negative/null result rather than overclaiming.

---

## 3. Industry Contribution

**Deployability:**
High. TEC is the production-deployed algorithm on part of a live platform at scale (over a million users/vacancies per month, per the paper), designed explicitly to be embarrassingly parallel and to replace a sequential RSD-style baseline that was too slow to run in production.

**Problems solved:**
Exposure concentration under capacity constraints in a multi-sided marketplace — recommending toward "popular but effectively out of stock" items rather than items with real unmet demand — with a specific worked solution to the round-robin RSD scalability bottleneck.

**Engineering cost:**
Moderate: needs per-listing posted/unfilled-capacity signals, a per-round score update job, and precomputed thresholds; no change needed to the existing favoriting-probability model, since TEC layers a capacity-aware eligibility filter on top of it.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First fully parallelizable capacity-aware exposure-reallocation mechanism (TEC) that matches sequential Adaptive-Quota-style RSD performance without its scalability bottleneck, validated with both simulation and a genuine field experiment on a production platform.

**Prior work comparison (top cited):**
- Horton (2017) — effects of algorithmic labor-market recommendations, field experiment.
- Behaghel et al. (2024) — recommender systems for directing job search, large-scale experiment.
- Crépon et al. (2013) — displacement effects of labor market policies, clustered RCT (motivates prefecture-level randomization to avoid interference).
- Manshadi, Rodilitz, Saban & Suresh (2025) — redesigning VolunteerMatch's ranking algorithm for more equitable volunteer access.
- **Rios, Saban & Zheng (2023) — "Improving match rates in dating markets through assortment optimization"** (directly cited as the dating-market analogue of this paper's exposure-concentration problem).
- Tomita, Togashi, Hashizume & Ohsaka (2023) — fast, examination-agnostic reciprocal recommendation in matching markets.
- Belot, Kircher & Muller (2019) — low-cost advice to jobseekers, online experiment.

**Verification:** The paper explicitly positions itself against the dating-market assortment/reciprocal-recommendation literature (Rios-Saban-Zheng; Tomita et al.) and distinguishes itself by targeting an FCFS, high-frequency, instantly-clearing market rather than a mutual-consent one — a distinction directly relevant to how far its mechanism transfers to dating.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Timee simulation calibration data (Hokkaido, 2024) | proprietary | No | 838 templates, 1,000 simulated workers |
| Timee field experiment (Aomori/Iwate, Jan 2–Feb 11, 2026) | proprietary | No | Few thousand workers, ~10K offerings per prefecture |

**Offline experiment reproducibility:** Not reproducible outside Timee — no public dataset or code release mentioned; all formulas are specified so the algorithm itself could be reimplemented against a different platform's data.

---

## 6. Community Reaction

Not checked — out of scope for this NotebookLM-sourced batch pass (no web search performed).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Not specified in NotebookLM-extracted excerpts
**Affiliations:** Timee (Japan spot-work platform); likely academic co-authors overlapping with the Kanayama/Otani Timee-research group (unconfirmed)
**Venue:** arXiv preprint (dated August 11, 2026)
**Year:** 2026
**PDF:** Not fetched directly — analyzed via NotebookLM source extraction
**Relevance:** Core
**Priority:** 2

---

## Bibliography Fields

- **title:** Designing Recommendation Exposure and Favorite Lists: A Field Experiment on a Spot-Work Platform
- **authors or organization:** Not specified in NotebookLM-extracted excerpts; institutional context is Timee (Japan spot-work platform)
- **year:** 2026
- **venue or type:** arXiv preprint
- **link:** N/A (accessed via NotebookLM notebook source; not separately fetched)
- **tier tag:** Tier 2 — Applied research / field experiments on real matching or dating platforms

**What they did (80 words max):** Modeled Timee's spot-work matching process, showed that maximizing predicted "favoriting" probability causes exposure to concentrate on popular-but-capacity-starved job templates ("misdirected concentration"), and designed Thresholded Eligibility Control (TEC) — a capacity-aware, fully parallelizable exposure-reallocation algorithm. Validated via simulation calibrated to real 2024 Hokkaido data and a live, prefecture-level randomized field experiment (Aomori vs. Iwate, Jan–Feb 2026) explicitly designed to avoid matching-market interference/spillovers.

**Mechanism relevant to two-sided balancing (50 words max):** Direct structural analogue of capacity-aware exposure allocation: per-listing scores from posted/unfilled capacity, capped and converted to eligibility thresholds that throttle over-subscribed listings and redistribute exposure to under-served ones — parallelizable, unlike LiJAR-style sequential RSD. Field-tested causal evidence that this raises market-level matches without reducing engagement.

**Metrics used, and the reported effect:** Per-round job-finding rate: Greedy 57.6% → SQ 64.2% → AQ 69.5% → TEC 70.0% (simulation). Field DID: matches +9.045/prefecture-day (p<0.05), recommendations-per-active-template +0.571, daily favorites unchanged (null, p>0.10), repeat-view rate down (1.35→1.19).

**Fit for a dating app:** high — TEC is a rigorously field-validated, production-scale capacity-aware exposure-reallocation mechanism directly citing the dating-assortment-optimization and reciprocal-recommendation literatures as its nearest relatives; the prefecture-level interference-avoidance experimental design is itself a reusable template for A/B-testing exposure changes on a matching platform. Caveat: the underlying market is FCFS/unilateral (no mutual-consent matching), so the ranking signal itself would need to become a reciprocal/bilateral score before reuse.

**Confidence that the item is real and described correctly:** high — all three NotebookLM queries were grounded (`sources_used` matched the scoped source_id), with detailed formulas, exact result tables, and a coherent, internally consistent citation list.

---

## Project Relevance

Directly relevant to modeling layer (2) capacity-aware exposure allocation — this is one of the closest real-world analogues found so far to the project's core ask, and unlike most sources in this survey it is **field-experiment validated on a live platform, not just simulated or theoretical**.

What transfers well: (1) the capacity-based scoring formula (exposure demand from "posted capacity" + "unfilled capacity") maps directly onto "receiver's unreplied-message backlog" or "estimated reply capacity" as the dating-market capacity signal; (2) **score capping** — no single listing can absorb more than one slot's worth of eligibility mass per round — is a directly reusable mechanism for preventing a handful of superstar profiles from dominating every recommendation batch; (3) TEC's parallelizable eligibility-threshold construction solves the exact scalability problem that makes LiJAR-style sequential RSD hard to run at dating-app scale; (4) the **prefecture-level randomized rollout design**, chosen explicitly to avoid user-level interference/spillovers in a matching market, is a directly reusable experimental template for A/B-testing exposure-redistribution policies under interference — precisely the project's experimentation-under-interference need; (5) the paper explicitly cites Rios-Saban-Zheng (2023, dating assortment optimization) and Tomita et al. (reciprocal recommendation) as its nearest relatives, situating itself in the same literature this survey is mapping.

What does not transfer: Timee's underlying match rule is **first-come-first-served, not mutual consent** — a worker's application instantly consumes a job slot without the employer selecting among candidates. TEC's ranking signal is therefore a **unilateral** favoriting probability, not a reciprocal/bilateral compatibility score; porting the mechanism to dating requires layering the eligibility-threshold exposure-control machinery on top of (not in place of) a genuine reciprocal-scoring model. The paper also does not measure two-sided retention, match-Gini, or wasted-likes directly — its closest analogue metric is the reduction in the share of low-exposure template-days, which is structurally similar to "share of users with near-zero exposure" but not identical to match spread across the *receiving* population.
