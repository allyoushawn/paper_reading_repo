# log.md — two-sided-market-balancing-dating (claude_opus workspace)

## [2026-08-16 → 08-17] literature-survey-nlm + direct-PDF | claude_opus run — COMPLETE

**Phases complete:** 0, 0.5, 1, 2, 3 (partial), 3.7, 4, 5.

**Outputs**
- Shared root: `README.md`, `requirements.md`, `queue.md` (merged, 111 entries).
- `claude_opus/`: `queue-claude_opus.md` (98 sources, clobber-proof), `method-tracker.md`,
  `read-papers/` (62 files: 40 complete, 22 stubs/partials), `literature-review.md`
  (4 artifacts), `executive-summary.md`, `RESUME-HERE.md`.

**Coverage:** **86 extraction files covering 82 distinct works** — 40 high fit, 29 medium, 12 low.
Four files duplicate another work (blog+paper, preprint+published); both cited, never counted as
independent evidence. Synthesis regenerated 2026-08-18 over all 86.
(An earlier partial state of 40/98 was superseded by the direct-PDF pass described below.) Tier 1+2 share of the queue: 64.8% (floor was 60%). Direction coverage
D1=35 D2=22 D5=16 D3=11 D6=8 D4=5 D7=4 D8=5.

**NLM notebook source count:** 121 (added ~121 this run; 28 of those are empty shells whose
fetch was blocked and which are logged, not counted as coverage).

**Extraction pivot.** The NotebookLM account hit an account-level block on programmatic chat
(`RESOURCE_EXHAUSTED`, Google error 8) that survived a date rollover and a token refresh — so it was
quota/restriction, not auth (`nlm doctor` passed all checks). Rather than wait, the remaining sources
were extracted by **downloading the papers and reading the PDFs directly**. This proved *better* than
the NotebookLM path: agents read real results sections, and caught several citation errors that
metadata alone would have propagated. Original cause of the block: Two concurrent runs
(`claude_opus` and `cursor-grok`) shared one account; a cursor-grok Survey 3 run had already
exhausted quota earlier the same day, and this run's over-parallelized retries (up to 16
concurrent batch agents, each firing ~12 queries) accelerated it. `refresh_auth` did not help,
confirming quota rather than stale tokens.

**Both of the brief's blind spots were disproved.** Dating-app engineering blogs on ranking DO
exist (OkCupid Tech Blog JAX like-prediction 2021; Tinder Tech Blog Two-Tower P(Match);
CyberAgent/Tapple ×2; Eureka/Pairs; Grindr). Post-2021 reciprocal-recsys surveys DO exist
(Koprinska & Yacef, Springer Handbook 3rd ed. 2022; Neve, SpringerBriefs 2025;
Mashayekhi et al., ACM CSUR 2022).

**Citation corrections found by reading sources rather than metadata**
1. `iriosu.github.io/.../dating_alf.pdf` is "Platform Design in Curated Dating Markets" (blinded
   M&SOM submission), NOT seed C1 "Improving Match Rates in Dating Markets" (M&SOM 2022). C1 is
   not in the notebook.
2. The Fong source is the 2018 working paper "Search, Selectivity, and Market Thickness", not the
   published Marketing Science 2024 version.
3. "Multiple Randomization Designs" resolves to Masoero et al., Dec 2025 preprint — not
   "Bajari et al. 2021" as the brief states.
4. Spotify "Recommendations in a Marketplace" = RecSys 2019 **tutorial**, Mehrotra & Carterette.
5. Holtz et al. has five authors; BOSS (KDD 2023) is Gold Open Access on ACM DL; the Palomares
   et al. arXiv preprint was WITHDRAWN over an author dispute — cite the Information Fusion version.

**Operational findings worth reusing**
- Medium and Cloudflare-fronted hosts reject NLM `source_add`; Medium **RSS feeds** work but hold
  only the 10 most recent posts. `freedium.cfd` is a dead domain; `r.jina.ai` blocks this network
  (AS7922); the Internet Archive was down site-wide during the run.
- A blocked `source_add` still creates a **source record with no content**. NLM then answers
  fluently about it and has been observed inventing a title. The only reliable check is the
  `sources_used` array on each query response.
- The shared `queue.md` was overwritten by the concurrent runner despite its append-only rule.
  Keep a private authoritative copy per run.

**Remaining:** 58 sources unextracted. 18 recovery batches staged in
`scratchpad/recovery/rec_01..18.md` with brief at `scratchpad/recovery_brief.md`; run at
concurrency 2 with 20s spacing once quota resets. See `RESUME-HERE.md`.
