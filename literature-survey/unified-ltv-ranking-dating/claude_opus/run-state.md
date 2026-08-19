# Run State — claude_opus workplace

**Run started:** 2026-08-16
**Skill:** `literature-survey-nlm`
**Topic slug:** `unified-ltv-ranking-dating`
**Model:** Claude Opus 5 (1M context) — orchestrator

## Fixed parameters

| Parameter | Value |
|---|---|
| Target references | 120 (user-approved 2026-08-16) |
| Hard floor | 45 verified references |
| Industry-source ratio | ≥ 60% |
| Per-direction floor | ≥ 3 references for each of D1–D8, or a recorded null result |
| Core-direction rule | D1–D4 must reach ≥ 50% of total before D5–D9 expansion |
| Time window | 2018–2026, prefer 2021+ |
| NotebookLM notebook | `67046a44-7490-4fe5-b54a-3f39ef37fdd3` (`unified-ltv-ranking-dating`) |
| Source cap | 300 per notebook (Google AI Pro), overflow at 290 |

## Folder split

- **Shared root:** `README.md`, `requirements.md`, `queue.md`, `notebooklm-state.md`, `log.md`
- **This workplace (`claude_opus/`):** `read-papers/`, `literature-review.md`, `executive-summary.md`,
  `method-tracker.md`, `run-state.md`, `query-log.md`

## Notebook state

| Metric | Value |
|---|---|
| Total sources | 101 |
| With extractable content | 88 |
| Empty shells (host blocked the fetch) | 13 — marked `nlm:failed:no-content` in `queue.md` |

## Direction balance — OPEN ISSUE

| Direction | In queue | Assessment |
|---|---|---|
| D1 Long-term value objective | 13 | adequate |
| D2 RL for retention | 13 | adequate |
| D3 Surrogate metrics | 5 | **thin** |
| D4 User-level LTV, label design | 4 | **thin, and a core direction** |
| D5 Multi-task cascades | 8 | adequate |
| D6 Uplift in the ranker | 9 | adequate |
| D7 Delayed feedback | 23 | **over-weighted at 26%** |
| D8 Two-sided and reciprocal | 5 | **thin, and the most project-specific direction** |
| D9 Generative | 8 | adequate |

**The brief's core-direction rule is currently violated.** D1–D4 hold 35 of 88 papers, which is 40%.
The rule requires at least 50% before expanding D5–D9, and D5–D9 already hold 53.

Cause: the local Awesome repo is rich in delayed-feedback work, which inflated D7, and holds nothing
at all for D4 or D6.

**Fix in progress:** a second NotebookLM deep research targeting D3 and D4, plus a seed-verification
search prioritizing D8, D4 and D3. Both must land before the queue is rebalanced. To reach 120 total
with D1–D4 at 50%, the survey needs roughly **25 more core papers**.

## Phase 3 processing order

Deliberate: process **D1–D4 first**, then D5–D9. This satisfies the core-direction rule as a
processing rule, and it gives the gap-filling discovery time to land before the thin directions are
reached.

## Phase progress

| Phase | Status |
|---|---|
| Prerequisites | done |
| Phase 0 — state detection | done — fresh first run |
| Phase 0.5 — README.md | done |
| Phase 1 — requirements.md | done — 41 seeds recorded |
| Phase 1 Step 7 — consistency check | done — no direction cut, D3 and D4 given scope notes |
| Phase 2 — discovery round 1 | done — 96 hits, 37 ingested |
| Phase 2 — blocked-URL recovery | done — 8 of 13 recovered, 5 null results recorded |
| Phase 2 — Awesome repo scan | done — 43 local PDFs uploaded, 0 failures |
| Phase 2 — queue.md | done — 88 To Process, 13 Skipped |
| Phase 2 — discovery round 2 (gap fill) | **running** |
| Phase 2 — seed verification (41 seeds) | **running** |
| Phase 3 — wave 1 (D1–D4, Priority 1–2, 16 papers) | **running** — 4 batches |
| Phase 3 — remaining 72 papers | not started |
| Phase 3.5 / 3.7 | not started |
| Phase 4 / 5 | not started |

## Notes for log.md

- NotebookLM answers the Phase 3 per-paper queries, so **Gemini produces the paper cards**. Opus
  orchestrates, sets the extraction schema, and writes the synthesis. Record this so a later model
  comparison across `claude_opus/`, `gemini/`, `chatgpt/` and `codex/` reads the attribution correctly.
- Two template decisions departed from the stock skill, both recorded in the query log:
  1. A **13-field Reference Card** section was added to every paper file, because the brief demands
     fields the stock paper-reader template does not carry — in particular *prediction vs.
     incrementality* and *credit assignment*.
  2. **NotebookLM Query 3 was fixed rather than improvised per batch.** A per-batch improvised query
     would produce inconsistent cards across 88 papers and a comparison table full of holes. The
     fixed query also asks each paper what it does **not** address, so the synthesis can report where
     the field is silent.
- `## 6. Community Reaction` is set to `Not assessed in NotebookLM mode.` Social-media searches add
  nothing to an architecture decision and would roughly double the run cost.
- **Method note worth keeping:** a NotebookLM source whose title displays as a raw URL is *not*
  necessarily empty. Sources added via `research_import` failed silently; sources added via
  `source_add` showed raw-URL titles but held full text. Verify by querying the source, never by
  reading the title.
