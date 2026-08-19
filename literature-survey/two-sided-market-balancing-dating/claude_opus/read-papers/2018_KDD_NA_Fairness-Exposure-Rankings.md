# Paper Analysis: Fairness of Exposure in Rankings

**Source:** NotebookLM source `51ed95ae-2945-409c-bb05-5761a57d9357` (KDD 2018)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Fairness of Exposure in Rankings
**Authors:** Ashudeep Singh, Thorsten Joachims (Cornell University)
**Venue / Year:** KDD 2018

Peripheral (Tier 3) academic methods paper — the field's foundational exposure-fairness paper, cited as a baseline by the Lorenz-dominance paper in this same batch. Core problem: the Probability Ranking Principle (sort strictly by relevance) allocates the scarce resource of **exposure** in a "winner-take-all" way — the paper's motivating example shows a 0.03 average-relevance gap between two candidate groups producing a 0.32 average-exposure gap. Method: models rankings as a doubly stochastic matrix `P` (marginal probability document i is placed at rank j), optimizes expected utility `u^T P v` as a linear program subject to a chosen linear fairness constraint `f^T P g = h`, and instantiates three concrete constraint families — **demographic parity** (equal average exposure across groups), **disparate treatment** (exposure proportional to group relevance, measured by a Disparate Treatment Ratio), and **disparate impact** (expected click-through rate proportional to group relevance, measured by a Disparate Impact Ratio). The resulting probabilistic ranking is converted to servable deterministic rankings via Birkhoff-von Neumann decomposition into a weighted mixture of permutation matrices. Evaluated on a synthetic 6-applicant job-seeker example and a subset of the Yow news-recommendation dataset (25 articles from two RSS-feed groups), against the unconstrained PRP baseline. Disparate treatment and disparate impact constraints reach DTR/DIR = 1.0 at near-zero DCG cost (job-seeker DCG 3.8193→3.8044/3.8025); demographic parity is markedly more expensive (DCG can approach zero if group relevance distributions are very unequal — the authors' own worked "cost of fairness" example). Authors' noted limitations: group-level constraints can leave severe *within-group* exposure disparities unaddressed; the LP can be infeasible when the required exposure ratio lies outside what any ranking can achieve; and the whole framework assumes access to unbiased relevance estimates, which are in practice ML-estimated and subject to selection bias in click logs.

---

## Bibliography Fields

- **title:** Fairness of Exposure in Rankings
- **authors or organization:** Ashudeep Singh, Thorsten Joachims (Cornell University)
- **year:** 2018
- **venue or type:** KDD 2018 (academic)
- **link:** N/A (accessed via NotebookLM notebook source; not separately fetched)
- **tier tag:** Tier 3 — Academic methods mapping to a lever, or surveys

**What they did (80 words max):** Formalized a linear-programming framework for ranking under exposure-fairness constraints, modeling rankings as doubly-stochastic probability matrices to make optimization tractable, and instantiated three classical fairness paradigms (demographic parity, disparate treatment, disparate impact) as linear constraints. Recovered servable deterministic rankings from the fair probabilistic solution via Birkhoff-von Neumann decomposition. Evaluated on a synthetic job-seeker ranking task and a real news-recommendation dataset against an unconstrained relevance-only baseline.

**Mechanism relevant to two-sided balancing (50 words max):** Single-sided, group-level exposure-fairness re-ranking (protected-group parity, treatment, or impact constraints) layered on top of a base relevance score via a linear program. No reciprocal/mutual-interest term, no individual capacity modeling — groups, not individual over-subscribed people, are the unit of fairness, though the framework can shrink groups to size one.

**Metrics used, and the reported effect:** Discounted Cumulative Gain (DCG, utility), Disparate Treatment Ratio (DTR), Disparate Impact Ratio (DIR). Job-seeker example: unconstrained DTR 1.7483→1.0000 (DCG 3.8193→3.8044); unconstrained DIR 1.8193→1.0000 (DCG →3.8025); demographic parity DCG 3.8193→3.8031 but authors show the cost can approach a full utility collapse under skewed group relevance. News dataset: similar pattern, disparate-treatment/impact constraints near-costless, demographic parity costliest.

**Fit for a dating app:** low — reason: this is a single-sided, static, offline group-fairness framework (protected demographic groups, not reciprocal match probability or individual reply capacity); the abstract lists "potential romantic partners" only as one example ranking domain among several (jobs, products, opinions), with no reciprocal or capacity-aware treatment developed for it anywhere in the paper.

**Confidence that the item is real and described correctly:** high for the summary above (Query 1 and Query 2 both returned grounded answers with `sources_used` matching the scoped source_id, and the formulas/results/citations are specific and internally consistent with the well-known Singh & Joachims KDD 2018 paper). See Project Relevance note below regarding Query 3.

---

## Project Relevance

**Low project relevance.** Query 3 (the dedicated project-context probe) could not be completed for this source: NotebookLM's API returned `RESOURCE_EXHAUSTED` (error code 8) on the initial call and on a retry, and remained exhausted through ~12 minutes of further retries and an auth-token refresh — this looks like an account/session-level quota shared across concurrently running survey batches, not a source-specific extraction failure. No Query 3 content was obtained and none is fabricated here.

Based only on the already-grounded Query 1/Query 2 content above (not on the unrun Query 3): the mechanism is single-sided and group-based — it optimizes exposure fairness between protected demographic groups using a static relevance score, with no reciprocal preference term, no notion of a receiver's reply capacity, no market-design levers, and no ecosystem-health or interference-aware evaluation. It is the direct methodological ancestor of the two-sided Lorenz-dominance paper in this same batch (which explicitly extends this exposure-fairness idea with a reciprocal-utility term and Pareto-efficiency guarantees), so its main project value is as historical/foundational context rather than a directly applicable mechanism. Recommend re-running Query 3 for this source in a later pass once notebook quota is available, to confirm this assessment with a grounded citation.

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |
