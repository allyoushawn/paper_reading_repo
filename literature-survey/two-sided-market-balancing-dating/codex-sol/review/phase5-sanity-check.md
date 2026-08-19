# Phase 5 Draft vs. NotebookLM Sanity Check

Date: 2026-08-19

## Agreement

The full-notebook response independently recovered the executive summary’s six required dimensions: bilateral preference modeling; finite capacity and congestion; constrained exposure allocation; product-level market design; multi-sided market-health metrics; and interference-aware experimentation. It also supported the draft’s central framing that a recommender in a capacity-limited matching market is an allocation device, not merely a one-sided relevance ranker.

Specific overlaps include reciprocal active/passive scoring, receiver exposure budgets, market-clearing scarcity factors, Gini or Lorenz distribution metrics, distinct reciprocal outcomes, cluster/two-sided randomization, and linear-program shadow prices. The response’s Airbnb figure of 19.76% matches the selected primary card and remains qualified as specific to one pricing meta-experiment.

## Discrepancies and Resolution

| Discrepancy | Resolution in final executive summary |
|---|---|
| NotebookLM synthesized sources outside the selected 45-card corpus, including Pigouvian congestion pricing, demand-information disclosure, strategic manipulation, long-term population dynamics, and several 2026 preprints. | Excluded from the executive summary unless represented in an own card; the final remains grounded in the reviewed codex-sol corpus. |
| NotebookLM described a broad field-wide “major paradigm shift.” | Narrowed to “the 45-source review supports” a layered market system; no field-consensus claim is made. |
| NotebookLM blended theory, simulation, offline replay, and field evidence in one narrative. | Each pattern states its evidence type or limitation where decision-relevant, and the final evidence-limit paragraph forbids pooled effects. |
| NotebookLM treated expected matches, coverage, Gini, effective dates, and retention as a common market-health family. | Retained as a scorecard, but not aggregated into a single validated metric or model objective. |
| NotebookLM’s capacity section included application costs and disclosure mechanisms not present in the selected bibliography. | Final recommendations use supported levers from the own cards: receiver budgets, demand redistribution, caps, curated menus, signals, and initiation rules. |
| NotebookLM suggested simulation/model-building after the answer. | Ignored because the survey’s role is to organize evidence, not design a model. |
| `notebook_get` at sanity-query time reported notebook `d3071ac8-16ef-4460-8991-7701679974c8`, title `two-sided-market-balancing-dating`, with **142** sources, while `discovery-notes.md` records 141→143 (+2). | Treated as a live-state discrepancy; synthesis is unaffected, but final verification and the shared log must report the fresh authoritative count rather than silently asserting 143. |

## Decision

No substantive synthesis gap was found: the draft covers all six NotebookLM themes and is more conservative about evidence strength. The source-count discrepancy remains an audit issue to recheck with a fresh `notebook_get` immediately before completion.
