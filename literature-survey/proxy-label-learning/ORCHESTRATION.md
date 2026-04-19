# Orchestration brief — proxy-label-learning (authoritative)

This file mirrors `/Users/fox/Desktop/survey2-proxy-label-learning-handoff.md` as of the **Google AI Pro** update. Agents must follow this for execution order and notebook policy.

## Notebooks

- **Main (all synthesis + all new sources):** `6fbcf9e6-3833-4660-8b56-67b0b98bf394`
- **Former overflow:** merged into main and notebook deleted (2026-04-12). Create a new overflow notebook only if main source count ≥ 290.

**Policy:** This account supports **~300 sources** on the main notebook. Do **not** use the old 45-source overflow rule. Only the main notebook receives `source_add`. Phase 4–5 queries use **main only** (no `source_ids` filter).

## Step 0 — Merge overflow into main (COMPLETE 2026-04-12)

1. `notebook_get(<overflow-notebook-id>)` — list sources *(historical; overflow deleted)*.
2. Re-add each overflow source to main via `source_add` (URL or `file_path`), `wait=True`.
3. Update **`queue.md` Done** lines: replace overflow `nlm:<uuid>` with new main source IDs.
4. `notebook_delete` on overflow with `confirm=True` *(done)*.
5. **`notebooklm-state.md`:** `overflow_notebooks:` empty *(done)*.

## Step 1 — queue.md

**To Process** must list only `nlm:pending` lines (no `| DONE` stragglers). Move any completed rows to **Done**.

## Step 2 — Phase 3 (delegation required)

`/literature-survey-nlm` / lead policy: the **orchestrator must not** process every paper inline. For **each batch of 3–5** consecutive pending papers, spawn a **fresh `generalPurpose` subagent** (Task tool) with a self-contained brief:

- `notebook_id = 6fbcf9e6-3833-4660-8b56-67b0b98bf394`
- Paper list: title, URL or file path, priority, relevance
- Exact two NLM queries from the handoff; `source_ids=[id]`; **no** `conversation_id`
- Output: `read-papers/`; paper-reader filename rules; blank Reverse Citation Map; Priority 3 = one short summary only
- Paywall: ACM/IEEE/Springer/Elsevier without free PDF → **Skipped** + `nlm:failed:paywall`

Optional: batch subagent may run `scripts/nlm_process_pending.py` from survey root (uses main ID and 290-source overflow guard).

## Step 3 — Phase 3.5

Finalize `method-tracker.md` (sort, composite scores, top-10 one-liners) per skill.

## Step 4 — Phase 3.7

Reverse citation maps for all `read-papers/*.md` (may delegate ~20 files per subagent).

## Step 5 — Phase 4

Five full-notebook queries on **main only** → `literature-review.md` (template: `literature-survey` skill).

## Step 6 — Phase 5

`executive-summary.md` + coverage ≥95%; proxy / Shapley attribution section; Most Fundamental Methods; update `requirements.md` summary if applicable.

## Log

Append progress lines to `orchestration-log.md` (create if missing).
