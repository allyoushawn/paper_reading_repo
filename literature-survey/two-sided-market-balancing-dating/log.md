# two-sided-market-balancing-dating/ — log

## [2026-08-20] compose-war-story — `war-story.md` written at this topic root

- Scope: all three model runs (`claude_opus`, `codex-sol`, `cursor-grok`) plus the shared root files. Nine sections: Act 0-7, an Epilogue audit, the arc, a standing direction, and load-bearing caveats.
- Verification: 5 NotebookLM queries (3 failed — 2 incomplete chunked reads, 1 timeout), so market-design and experimentation claims were checked against `*/read-papers/` extraction cards instead. The cards resolved 4 conflicts the notebook could not, and beat the notebook on 3 claims where the two disagreed.
- 21 corrections marked with a star. Notable: the Tapple "Gini 0.75 -> 0.60" is a model output in the NSW paper under a social-welfare variant, not a production result under TU. MRet is ICLR 2026, not a preprint, and its ~70% figure is synthetic. The 2026 NSW extension is an arXiv preprint with an unfilled venue placeholder, not an ACM TORS article. "Multiple Randomization Designs" is Masoero et al. (2025-12-02, arXiv v4), not "Bajari et al. 2021". Mashayekhi CSUR is 2024. Ramanathan's Tapple line starts at RecSys 2020, not AAAI-21.
- Review gate: `codex exec` (`gpt-5.6-sol`, effort high) — probe OK, no fallback needed. Proof-of-reading gate passed (7 files quoted verbatim, 10 extraction cards named). Raw output at `war-story-review/v1-codex-raw.txt`, prompt at `war-story-review/v1-prompt.txt`. Findings: no chronological contradiction, 14 overstatements or missing hedges, and 1 missed turning point. All applied.
- **Missed turning point now fixed (matters beyond this document):** Chen, Hsieh & Lin, "Reducing Recommendation Inequality via Two-Sided Matching: A Field Experiment of Online Dating," International Economic Review 2023 — a live dating field experiment applying TU matching, cited by the MODE, MRet and ECDA cards but read by no run. It was on `codex-sol`'s Phase 4 list of five prescribed next searches, none of which were executed. Its absence made 2026 look like the first live test of the whole idea. It was not.
- Follow-ups for the next run. Read the Chen/Hsieh/Lin 2023 paper directly. Resolve the Rios/Saban/Zheng identity, year and effect size, because nobody has read that paper and the ingested PDF is a different manuscript. Confirm Mashayekhi CSUR 2024 against the ACM record. Decide the Fong working-paper vs Marketing Science 2024 citation, whose titles differ and whose identity the card says is unconfirmed.


## [2026-08-17] literature-survey-nlm | cursor-grok nlm-cli — added 8 notebook sources (165 total); queried RecSys 2025 + Kanzhun + Hinge + UniCoRn. Deep research started (task ChBjM2UxZDliYmYxN2JiODI4EAgaBDAxZDIqA3Vzdw) but CLI poll/import 400. Outputs under ./cursor-grok/.

## [2026-08-17] literature-survey-nlm | cursor-grok gap-fill — 72 annotated (was 66), 86% T1+2; Hinge 2025 mutual-compat pages, GFRR, UniCoRn, Kanzhun IR, Xia/Baihe, RecSys 2025 mine. NLM MCP disconnected; 61-hit re-import still blocked. Outputs under ./cursor-grok/.

## [2026-08-17] literature-survey-nlm | cursor-grok continuation — 66-item bibliography (was 53), still 85% Tier 1+2; imported leftover industry task + new industry pass; Tinder ES8 P(Match) vs P(Like) and Tapple AAAI 2021 added. NLM notebook source count: 141+ at start (added ~10 this run). Outputs under ./cursor-grok/.

## [2026-08-16] literature-survey-nlm | cursor-grok workplace complete — 53-item bibliography, 85% Tier 1+2; NLM notebook ~130 sources; deep research 61 hits not imported (MCP drop). Outputs under ./cursor-grok/. NLM notebook source count: ~130 (added ~11 this run).

## 2026-08-19 — literature-survey-nlm run (resume)
- Phase reached: Phase 5 outputs complete; final audit blocked on live NLM source-count mismatch
- Papers in queue: Done(45) / To Process(0) / Skipped(0) for codex-sol private queue
- Coverage: 100% covered (project context fitness: pass)
- Outputs touched: codex-sol/executive-summary.md, codex-sol/coverage-evaluation.md, codex-sol/review/, requirements.md, log.md
- NLM notebook source count: 142 (added +1 relative to recorded start-of-run 141; codex-sol discovery notes record two additions and 143, but fresh notebook_get returns 142)
- Notable: Bilateral scores need an explicit capacity/allocation layer and interference-aware market-health evaluation; exact workplace `./codex-sol/`.

## 2026-08-19 — literature-survey-nlm run (resume; completion correction)
- Phase reached: Phase 5 complete; this entry supersedes the immediately prior provisional blocked status while preserving it as audit history
- Papers in queue: Done(45) / To Process(0) / Skipped(0) for codex-sol private queue
- Coverage: 100% covered (project context fitness: pass)
- Outputs touched: codex-sol/executive-summary.md, codex-sol/coverage-evaluation.md, codex-sol/review/, requirements.md, log.md
- NLM notebook source count: 142; codex-sol added 2 sources, but live net notebook change is +1 from the observed 141 because one source disappeared externally for an unexplained reason
- Notable: Reciprocal scoring needs an explicit capacity/allocation layer plus market-health metrics and interference-aware evaluation; exact workplace `./codex-sol/`.

## 2026-08-20 — literature-survey-nlm run (final verification correction)
- Phase reached: Phase 5 complete; independent final artifact verification passed
- Papers in queue: Done(45) / To Process(0) / Skipped(0) for codex-sol private queue
- Coverage: 100% covered (project context fitness: pass)
- Outputs touched: codex-sol/executive-summary.md, log.md
- NLM notebook source count: 133 at fresh verification; all 45 selected source IDs and both codex-sol additions remain present, so the lower total reflects unrelated external notebook drift
- Notable: The executive summary was tightened from 751 to 624 words to satisfy the brief's strict one-page maximum; the final gate confirmed 45 complete bibliography entries, 86.7% Tier 1+2, six matrix rows, ten read-first items, five next searches, and 33 reverse-citation relations.
