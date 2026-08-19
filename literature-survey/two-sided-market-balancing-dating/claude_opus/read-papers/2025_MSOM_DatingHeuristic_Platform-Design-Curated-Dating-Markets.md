# Paper Analysis: Platform Design in Curated Dating Markets

**Source:** NotebookLM source `c17bdd53-6317-429b-83df-72b3bc0cec43` (submitted to Manufacturing & Service Operations Management; authors blinded for peer review)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Platform Design in Curated Dating Markets
**Authors:** Blinded for peer review (manuscript under review at Manufacturing & Service Operations Management)
**Abstract:**
Studies which subset of profiles a curated dating platform should show each user each period to maximize expected matches, under a taxonomy of platform designs varying (i) one-directional vs. two-directional interaction sequencing and (ii) sequential vs. non-sequential match timing. Proves worst-case failure of naive matching heuristics, derives constant-factor approximation guarantees via submodular optimization, and shows the practitioner-standard "Dating Heuristic" (DH, from Rios, Saban & Zheng 2023) achieves a robust 1−1/e guarantee across all platform designs, validated on real data from an undisclosed US dating app.

**Key contributions:**
- A unified framework spanning four platform designs (one/two-directional x sequential/non-sequential).
- Proof that Local Greedy and Perfect Matching have worst-case performance collapsing to O(1/n) as market size n grows (they ignore congestion).
- Constant-factor approximation guarantees (1−1/e down to 1/(3+ε)) via submodular/matroid structure for various designs.
- Proof that the integral Dating Heuristic (DH) — a one-period-lookahead mixed-integer program — achieves a 1−1/e approximation for every platform design, and 1/4e in the one-directional, large-market, most-selective-side-initiates case.
- Managerial guidance: initiate with the side generating the smallest expected backlog per displayed profile; a well-designed one-directional platform captures ≥50% of two-directional matches; non-sequential matches add negligible value.

**Methodology:**
Bipartite matching over a discrete T-period horizon; each user has a capacity K_l (max profiles shown per period) and a "backlog" of prior likes to potentially reciprocate. DH solves a mixed-integer program each period looking one period ahead, prioritizing profiles likely to yield sequential matches. Like-probabilities φ estimated via panel logit regression (user + period fixed effects, age/height/race/religion/education distance features) on real swipe logs.

**Main results:**
DH matches or beats Global Greedy and dominates Local Greedy/Perfect Matching across all four platform designs in simulation (100 runs, K_l=3, 173 women / 113 men from Houston, TX, Feb–Aug 2020). Women are far more selective (27.0% avg. like probability vs. 57.1% for men); DH with women initiating produces significantly more matches than men initiating.

---

## 2. Experiment Critique

**Design:**
Theory-first paper: worst-case proofs for baselines, constant-factor approximation proofs for DH, then simulation validation on real backlog/like-probability data. Baseline set (Local Greedy, Perfect Matching, Global Greedy variants, DH variants, and an LP-relaxation upper bound) is reasonably comprehensive for the matching-algorithm comparison, though it omits the platform's own production algorithm from the reported figures ("we also tested... our partner's algorithm... we decided to omit them" — no quantitative comparison given).

**Statistical validity:**
Like-probabilities are estimated from a panel logit with fixed effects (Pseudo R² = 0.386, N=396,226 evaluations) — solid for the offline estimation step. The core algorithmic comparison is simulation-based (100 runs per design) rather than a live A/B test, so results reflect the fitted choice model's fidelity, not an unconfounded field estimate.

**Online experiments (if any):**
None. All comparisons are simulations seeded by the fitted like-probability model on real historical data; no live A/B test of DH vs. incumbent policy is reported.

**Reproducibility:**
Full MIP formulations, matroid/submodularity proofs, and estimation procedure are given. The underlying dating-app dataset is proprietary under NDA and not released; app identity undisclosed.

**Overall:**
Results support the central claims (DH's design-robust 1−1/e guarantee, one-directional near-parity with two-directional, non-sequential timing's low marginal value). The authors are explicit that they omit history effects (recent match success negatively affects future swiping) to keep the theory tractable, and flag this as a simplification with a (small) known real effect.

---

## 3. Industry Contribution

**Deployability:**
High — DH is already described as "commonly used... due to its simplicity and effectiveness" in industry, and this paper's contribution is establishing when/why it's safe to use across platform-design variants, plus a proof that it's provably better than the naive local greedy/perfect-matching heuristics many platforms likely run instead.

**Problems solved:**
Directly addresses the exposure-allocation problem central to this project: which profiles to show whom each period. Explicitly analyzes the "who initiates" market-design lever (one-directional vs. two-directional) and congestion caused by ignoring interdependence between users' choices.

**Engineering cost:**
Moderate — DH requires solving a mixed-integer program per period (tractable at the batch sizes shown: ~113–173 users per side) plus a fitted like-probability model; no online learning loop is described.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First unified analysis of the Dating Heuristic's robustness across a taxonomy of platform designs (one/two-directional × sequential/non-sequential), with new worst-case impossibility proofs for naive baselines and new constant-factor guarantees derived from submodular optimization and matroid theory.

**Prior work comparison:** Direct extension of Rios, Saban & Zheng (2023) "Improving match rates in dating markets through assortment optimization" (M&SOM), which introduced DH for a single platform design; also builds on Ashlagi et al. (2022) and Kanoria & Saban (2021) on two-sided sequential assortment/search.

**Verification:** Consistent with the trajectory of the two-sided assortment-optimization literature cited (Ashlagi et al. 2022, Aouad & Saban 2022, Torrico et al. 2021); the multi-platform-design generalization and DH's guarantee proof appear to be this paper's distinctive contribution relative to the single-design Rios et al. 2023 precursor.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Undisclosed US dating app (real swipe/backlog logs, Houston TX users, Feb–Aug 2020) | proprietary, NDA | No | Sample of 173 women, 113 men for simulation |

**Offline experiment reproducibility:** Not reproducible outside the industry partner — no public dataset or code release mentioned; app name withheld under NDA.

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

**Authors:** Blinded for peer review
**Affiliations:** Unknown (blind review; industry partner is an undisclosed US dating app under NDA)
**Venue:** Submitted to Manufacturing & Service Operations Management
**Year:** ~2024–2025 (not stated in source; uses data through Aug 2020 and cites Rios et al. 2023 as prior work — exact submission year unconfirmed)
**PDF:** Not fetched directly — analyzed via NotebookLM source extraction
**Relevance:** Core
**Priority:** 1

---

## Bibliography Fields

- **title:** Platform Design in Curated Dating Markets
- **authors or organization:** Authors blinded for peer review (submitted to Manufacturing & Service Operations Management)
- **year:** ~2024–2025 (not stated in source; not fabricated — uses data through Aug 2020, cites Rios et al. 2023)
- **venue or type:** Manufacturing & Service Operations Management (under review)
- **link:** N/A (accessed via NotebookLM notebook source; not separately fetched)
- **tier tag:** Tier 2 — Applied research / field experiments on real matching or dating platforms

**What they did (80 words max):** Modeled the profile-subset-selection problem across four dating-platform designs (one/two-directional × sequential/non-sequential), proved naive matching heuristics (Local Greedy, Perfect Matching) can be arbitrarily bad, derived constant-factor approximations via submodular optimization, and proved the practitioner "Dating Heuristic" (one-period-lookahead MIP) achieves a 1−1/e guarantee robust to platform design. Validated theory and managerial recommendations (who should initiate, value of non-sequential matches) via simulation on real backlog/swipe data from an undisclosed US dating app.

**Mechanism relevant to two-sided balancing (50 words max):** Directly relevant: models each period's profile-display decision as a capacity-constrained (K_l) assortment problem accounting for both sides' backlogs and realized likes, and shows that platform-design choices (who initiates first) materially change match efficiency by managing congestion — the core exposure-allocation mechanism this project needs.

**Metrics used, and the reported effect:** Total expected matches per benchmark/platform-design combination (Figure 1); approximation-guarantee ratios (1−1/e ≈ 63.2% down to 1/(3+ε) for various designs, 1/4e for large-market one-directional non-sequential); like-probability asymmetry (27.0% women vs. 57.1% men); one-directional design captures ≥50% of two-directional matches.

**Fit for a dating app:** high — this is a dating-market-native paper solving exactly the per-period exposure-allocation problem central to the project, with real production-scale validation, though it optimizes total expected matches rather than match *spread*/Gini or reply-capacity-aware redistribution, and treats K_l as a display-slot cap rather than an explicit reply-capacity constraint.

**Confidence that the item is real and described correctly:** high — Query 1 and Query 2 were both grounded (`sources_used` matched the scoped source_id `c17bdd53...`), with detailed, internally consistent formulas, proposition numbers, and a real bibliography (citing Rios, Saban & Zheng 2023 M&SOM 25(4):1304–1323) matching the batch manifest's description. Query 3 (the dedicated project-relevance probe) could not be run — see Project Relevance note below.

---

## Project Relevance

*Note: the dedicated Query 3 project-relevance probe could not be completed — the NotebookLM API returned `RESOURCE_EXHAUSTED` errors on every attempt (5+ retries, including after `refresh_auth`), likely due to concurrent load from other batches sharing this notebook/account. The analysis below synthesizes project relevance from the grounded Query 1/Query 2 content above, not from a fresh NLM answer.*

Directly relevant, with one structural gap worth flagging. The paper's core mechanism — per-period, capacity-constrained (K_l) profile selection under submodular optimization, robust to platform design — is essentially the same exposure-allocation problem this project's Layer 2 (capacity-aware exposure allocation) needs to solve. Three things transfer well: (1) the **backlog mechanism** (tracking who has already liked whom, and prioritizing showing those profiles to close out likely matches) is a natural building block for reciprocal-scoring-aware ranking; (2) the **market-design lever analysis** (one-directional vs. two-directional, who initiates) is a direct example of a Layer 3 market-design intervention, with the concrete finding that having the *more selective* side initiate captures most of the value of full two-directional interaction at lower congestion cost — a testable lever for this project; (3) the proof that **naive greedy/perfect-matching baselines catastrophically fail** at scale (O(1/n) worst case) is a strong argument for why a naive "most compatible first" ranking is insufficient once congestion is considered.

The gap: K_l in this paper is a **display cardinality limit** (how many profiles a user sees per period), not an explicit **reply-capacity constraint** (how many likes a desirable user can realistically reciprocate before overload). The paper's objective is total expected matches, not match *spread* — it does not report or optimize any Gini-style concentration metric, wasted-likes metric, or two-sided retention outcome, and its "congestion" concept is about backlog/queueing dynamics rather than the specific overload-and-burnout dynamic (a small set of highly desirable users drowning in un-reciprocable likes) that is this project's central concern. Adapting DH's backlog-clearing logic to explicitly discount profiles nearing reply-capacity saturation — rather than just capping how many profiles a *viewer* sees — would be the natural extension needed to close this gap.
