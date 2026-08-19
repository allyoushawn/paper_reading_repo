# Resume point — claude_opus run, 2026-08-16

## State

- Phases 0, 0.5, 1, 2: **complete**. `README.md`, `requirements.md`, `queue.md` (merged, 111 entries),
  `claude_opus/queue-claude_opus.md` (98 sources, clobber-proof), `method-tracker.md` all written.
- Phase 3: **40 of 98 sources extracted** into `claude_opus/read-papers/`
  (16 high fit, 17 medium, 7 low). 22 files are stubs/partials.
- Phases 3.7 / 4 / 5: **not done.**

## Hard blocker

NotebookLM returns account-level `RESOURCE_EXHAUSTED` (Google error 8). Not auth — `refresh_auth`
reloaded tokens and the error persisted; ~10 min at zero load did not clear it. This is the daily
query quota, exhausted by this run (500+ queries, inflated by over-parallelized retries).

**To unblock:** the user runs `! nlm login` (if it is auth after all), or wait for the daily reset.

## Next action, ready to run

Synthesis (Phases 3.7 + 4) via Codex — does NOT need NotebookLM. Everything is staged:

- Prompt: `scratchpad/review/p2_prompt.txt` — change "Read exactly ONE file" to
  "Read these SIX files, one per tool call".
- Corpus: `scratchpad/review/context/corpus-part1.md` … `corpus-part6.md` (each <30 KB).
- Command shape:
  `codex exec --sandbox read-only --skip-git-repo-check -c model_reasoning_effort="low" "$(cat prompt)" </dev/null > out.txt 2>&1`
- Prior attempts: v1 killed (40 separate reads at max effort — too slow);
  v2 correctly returned `UNREADABLE` (single 150 KB file truncated on read). The 6-part split fixes both.

## Then

- Phase 3 recovery: 18 batches in `scratchpad/recovery/rec_01..18.md`, brief at
  `scratchpad/recovery_brief.md`. **Concurrency 2 max, 20s between NLM calls.** Agents skip
  already-complete sources.
- Phase 5 executive summary via Codex.
- Append run entry to `claude_opus/log.md` and an `ingest` line to
  `knowledge_base/projects/attribution_based_retention/log.md`.

## Carry these forward — corrections found by reading sources, not metadata

1. `c17bdd53` is "Platform Design in Curated Dating Markets" (blinded M&SOM), NOT the brief's seed
   C1 "Improving Match Rates in Dating Markets" (M&SOM 2022). C1 is NOT in the notebook.
2. `c02339ea` is the 2018 working paper "Search, Selectivity, and Market Thickness", not the
   published Fong 2024 version.
3. `ecffd79a` is Masoero et al., Dec 2025 preprint — not "Bajari et al. 2021" as the brief says.
4. Spotify "Recommendations in a Marketplace" = RecSys 2019 **tutorial**, Mehrotra & Carterette.
5. Holtz et al. has five authors; BOSS KDD 2023 is Gold OA; the Palomares arXiv preprint was
   WITHDRAWN (cite the Information Fusion version only).

## Both of the brief's blind spots were DISPROVED

- Dating-app engineering blogs on ranking DO exist: OkCupid Tech Blog (JAX like-prediction, 2021),
  Tinder Tech Blog (Two-Tower P(Match)), CyberAgent/Tapple ×2, Eureka/Pairs, Grindr.
- Post-2021 reciprocal-recsys surveys DO exist: Koprinska & Yacef (Springer Handbook 3rd ed. 2022),
  Neve (SpringerBriefs 2025), Mashayekhi et al. (ACM CSUR 2022, free on arXiv).

## Highest-value findings so far

- **CyberAgent/Tapple**: real production dating-app numbers — match **Gini 0.75 → 0.60** under a TU
  matching model; 0.9 vs 0.2 recall gap by gender; they **explicitly rejected hard exposure caps**
  over match-volume risk.
- **LiJAR (LinkedIn KDD 2017)**: +6.5% applications to underserved jobs, −8.7% to over-served,
  total flat, distribution entropy +12%. Closest transferable mechanism.
- **Kanoria & Saban (MS 2021)**: cites real Tinder wasted-like statistics; supplies directional
  search and information hiding as levers.
- **Anti-patterns**: Tinder Smart Photos and its on-device successor optimize single-viewer appeal
  and likely worsen skew. Grindr is a negative control (distance sort, no algorithm).

## Concurrency warning

A `cursor-grok` run shares this folder and the notebook. It **overwrote** the shared `queue.md` at
21:31 despite the append-only rule; I merged both and keep a private copy. It also edited
`~/.claude/hooks/repo-path-guard.py` and `settings.json`. Re-check shared files before trusting them.
