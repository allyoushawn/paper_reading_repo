# Privacy-Robust Incrementality Measurement for Advertising Systems under Signal Loss

**Source:** https://arxiv.org/pdf/2606.03878.pdf | **NLM source id:** 2e9a3300-7b3b-43da-87d8-2b068a86c466 | **Year / venue:** 2026, arXiv:2606.03878 | **Authors / affiliation:** Prashant Shekhar (corresponding), Caroline Howard — Department of Mathematics, Embry-Riddle Aeronautical University | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Randomized lift tests are the gold standard for ad incrementality, but modern privacy-preserving reporting (Privacy Sandbox, IPA, etc.) degrades the observed signal through six layers: match-rate loss, linkability loss, attribution-window loss, aggregation-threshold suppression, randomized reporting noise, and segment-heterogeneous loss. The paper formulates this as a robust causal decision problem: given an ambiguity set U of plausible degradation mechanisms, it projects the "compatibility fiber" of clean experimental worlds consistent with a degraded report onto the incrementality functional, yielding a sharp population decision frontier and a practitioner-facing three-state rule — **Certify** (lower bound clears the business threshold), **Reject** (upper bound falls below it), or **Unresolved** (crosses it). **Unit of decision:** per segment/campaign/cell — the authors explicitly distinguish this from MTA ("attribution distributes credit; we ask what causal decision remains certified"). **Outcome:** incremental conversion/visit/spend lift Δ_s vs. a business threshold b_s. **Bias handling:** starts from a clean *randomized* experiment (handling ordinary confounding/selection bias via randomization); the novel contribution is bounding privacy-induced signal loss separately via a reportable-retention multiplier and ambiguity set, not addressing engagement-based selection bias.

## 2. Evidence
Criteo Uplift (2M rows, clean lift 0.001117) and Hillstrom email (64K rows, clean lift 0.004955). Population-level certification survives to retention q=0.65 (Criteo) and q=0.35 (Hillstrom), but once finite-sample randomization uncertainty and DP-style reporting noise are added, all tested settings in both datasets become Unresolved. Segment-level certification in Hillstrom drops from 100% of coarse cells to 36.0% of very fine cells, while aggregation-threshold suppression rises to 39.5%. Sample-complexity: reaching a tight radius (ε=0.005) at low retention (q_min=0.15) requires ~107.5M observations per arm.

## 3. Limitations
Certification is sensitive to how the ambiguity set U is specified — an overly narrow set can produce false-optimistic certification. Empirical evaluation uses synthetic stress layers over public A/B datasets, not real production privacy-API traces (no paired pre/post-privacy data exists publicly). Finite-sample decisions are frequently "unresolved" in practice. Aggregate-level certified incrementality does not imply subgroup/segment safety.

## 4. Prior works named
- Gordon et al. (2019/2023) — observational vs. randomized ad measurement divergence
- Dwork (2008) / Dwork & Roth (2014) — differential privacy foundations
- Horowitz & Manski (2000) / Imbens & Manski (2004) — partial identification, confidence intervals
- Case et al. (2023) / Google Privacy Sandbox (2025a,b) — Interoperable Private Attribution, Attribution/Private Aggregation APIs
- Johnson, Lewis & Nubbemeyer (2017) / Vaver & Koehler (2011) — Ghost Ads, geo-experiments

## 5. Project Relevance
- **Answers:** Q1
- **Attributes retention to individual interactions?** No — explicitly defines its target as a decision-certification layer downstream of attribution, not credit distribution across touchpoints, and operates at segment/campaign granularity.
- **Transferable components:** The three-state Certify/Reject/Unresolved discipline (refusing an overconfident point estimate when signal is too degraded/sparse) and the reporting-granularity-vs-noise tradeoff diagnostic are useful design patterns for any per-swipe credit system built on incomplete/censored interaction logs.
- **Required changes:** Aggregate segment-level bounds would need to become per-swipe/per-sequence micro attribution; the scalar retention multiplier would need to become heterogeneous, temporally-decaying event-type features (swipe/match/message); the one-time lift target Δ_s would need to become a recurring daily N7 outcome.
- **On last-touch:** Contrasts itself with MTA generally (not last-touch specifically) and proves that under degraded/incomplete signal, any forced binary decision rule has worst-case error ≥1/2 — a formal argument for why heuristic point-attribution (including last-touch) can be overconfident when the underlying signal is weak.
- **Transfer rating:** background — a decision-theoretic layer for macro-level ad measurement under privacy constraints, not an in-app sequence-attribution algorithm.
