# Log — Unified Retention/Revenue Ranking for Dating

## 2026-08-18 — literature-survey-nlm run (initial)
- Model identifier: `codex-sol` (runtime model family: `gpt-5.6-sol`)
- Phase reached: Phase 5 complete; independent CLI review PASS after two fix rounds
- Papers: selected/carded 120; substantive NotebookLM extraction 118; metadata-only failures 2
- Coverage: 31/31 structural requirements represented (project-context representation: 8/8; implementation validation remains out of survey scope)
- Source mix: industry/company/industry-lab 97/120 (80.8%); academic 23/120
- Direction floors: D1=17, D2=22, D3=10, D4=11, D5=9, D6=10, D7=14, D8=22, D9=7; D1–D4=60/120
- URL validation: 120/120 resolved (94 direct HTTP, 24 browser-public, 2 canonical replacements, 0 unresolved)
- Outputs touched: 120 `read-papers/` cards, `comparison-table.md`, `claim-evidence-table.md`, `literature-review.md`, `executive-summary.md`, `method-tracker.md`, `coverage-evaluation.md`, `cross-reference-summary.md`, `url-validation.md`, and review transcripts
- NLM notebook source count: 146 (added 0 this run)
- Notable: Rank 1 is a constrained reciprocal multi-task LTV ranker serving on 30-day return plus 30-day net revenue; 90-day revenue remains shadow-only. The package is a strategic proposal, not an implementation-ready specification.
