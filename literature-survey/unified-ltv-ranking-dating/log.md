# unified-ltv-ranking-dating — shared run log

## [2026-08-18] ingest | **codex-sol workplace complete** — 120 cards, 120-row comparison table, claim-evidence table, literature review, executive summary, method tracker, URL validation 120/120, and independent CLI review PASS under `codex-sol/`. NotebookLM corpus remained 146 sources; other model workplaces were not read or modified.
## [2026-08-17] ingest | cursor-grok continuation complete — 120 cards (was 90) + updated literature-review, executive-summary, method-tracker, cards-index under `cursor-grok/`. Independence vs `claude_opus/` preserved.
## [2026-08-16] init | Shared Survey 3 folder (README, requirements, queue, notebooklm-state)
## [2026-08-16] ingest | cursor-grok workplace complete — 90 cards + literature-review, executive-summary, method-tracker under `cursor-grok/`
## [2026-08-16] ingest | claude_opus run started — corpus expanded from 0 to 146 NotebookLM sources (3 discovery rounds + 43 local PDFs from the Awesome repo + 37 seed-verification URLs)
## [2026-08-17] ingest | **claude_opus workplace complete** — 133 cards + literature-review, executive-summary, method-tracker, comparison-table (133 rows), query-log under `claude_opus/`. Coverage 25/25 requirement items; Project Context fitness 8/9 (revenue-mix gap recorded as unaddressable from the literature).

---

### Notes from the claude_opus run that are useful to any later run

- **Independence preserved.** `claude_opus` has not read anything under `cursor-grok/`. The per-model
  workplace rule is being followed strictly so the two runs stay comparable.
- **NotebookLM became unusable mid-run.** The `notebook_query` endpoint returned `RESOURCE_EXHAUSTED`
  and the MCP server later disconnected. Phase 3 was completed instead by **downloading sources to
  local PDFs and reading them directly**. 76 PDFs now sit in `claude_opus/pdfs/` (gitignored). A
  later run blocked the same way can reuse that folder rather than re-fetching.
- **arXiv URL gotcha.** An `/abs/` or `/html/` URL that fails ingestion usually has a working
  `/pdf/<id>` form — converting 17 such URLs recovered every one of them. Separately, a `/pdf/<id>`
  that 404s may still resolve at `/pdf/<id>v1` or `v2` (the Palomares reciprocal survey needed `v2`).
- **A raw-URL title is not proof of a failed ingestion.** Sources added via `research_import` failed
  silently with no text; sources added via `source_add` showed raw-URL titles but held full text.
  Verify by querying the source, never by reading its title.
- **Six sources are confirmed to exist but are permanently unreachable** — listed at the end of
  `queue.md` under the Harvest Backlog so they are not searched for again. Two are brief seeds
  (Netflix RecSys 2023 reward innovation; Meta KDD 2026 surrogate metrics case study).
