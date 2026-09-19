# Attribution-based retention — copy-paste prompts

Read [`SURVEY-MANUAL.md`](./SURVEY-MANUAL.md) for questions, follow list, and pipeline. This file is only the paste text.

Replace `YYYYMMDD` with today's date (example: `20261015`). Paste into a **new** agent session.

Topic root:

`/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/`

---

## Prompt A — kick off a new follow-up (primary)

```text
Run a NEW dated follow-up of the attribution-based-retention literature study.

Read and follow:
/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/SURVEY-MANUAL.md

Also load: ~/.claude/skills/literature-survey-nlm/SKILL.md (pipeline for cards + Codex synthesis ONLY — do not use its Phase 0 resume on the parent slug), paper-reader, notebooklm, cli-review.

## Output folder (create; write only here)
/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/YYYYMMDD_survey/

Do NOT write to the topic root, to 20260917_survey/, or to 20260917_survey_grok/.
Do NOT edit SURVEY-MANUAL.md or PROMPTS.md unless the standing pipeline changed.
Do NOT invoke /literature-survey-nlm with slug attribution-based-retention (that resumes the 2026-04 parent).

## NotebookLM
Reuse notebook 6a3b8a8e-6f2f-4efe-99eb-283983fc95d9. Do not notebook_create.
Q2-adjacent notebooks (classify per-interaction credit, do not re-survey): 67046a44-7490-4fe5-b54a-3f39ef37fdd3 and d3071ac8-16ef-4460-8991-7701679974c8.

## Questions
Q1. Latest industry attribution. Window: 2026-09-18 → today, plus newest work from the follow list in SURVEY-MANUAL.md.
Q2. Published attribution-based retention (per-interaction credit for retention/engagement/days-active)? No date limit; skip titles already carded in parent read-papers/ or any prior YYYYMMDD_survey/read-papers/. Academic counts iff production dataset or deployment.
Deliverable. Confirm or revise the 2026-09-17 v1 (predictive deletion residual, NOT incremental) → v2 (experiment-calibrated causal sequence + survival) → v3 (optional front-door/flow) replacement for last-touch N7 → latest swipes. Map credit onto swipe / like / match / conversation.

## Must-do process
1. Copy discovery/harvest.py from 20260917_survey/; run mechanical OpenAlex+arXiv follow-list + topic harvest. Log nothing-new. Do not launch 4 parallel LLM discovery agents.
2. D3 (Q2 + company negative evidence) and D4 (engineering blogs) as capped LLM agents with incremental writes.
3. Ingest new sources into the shared notebook (wait=False, arXiv pdf URLs, jina fallback for blogs).
4. 40–60 new cards in THIS folder via NLM, 2 independent queries/paper, batches 3–5.
5. Classify every Q2 paper TRUE / PARTIAL / NOT attribution (rubric in SURVEY-MANUAL.md).
6. Compact review/context/ (<30KB files) + 4 NLM cross-source queries.
7. Codex gpt-5.6-sol with skill claude-literature-survey-nlm ONLY (not claude-literature-survey). Adapt 20260917_survey/review/codex-draft-prompt-v3-nlm.txt to this folder. Write method-tracker.md, literature-review.md, executive-summary.md. Proof-of-reading required.
8. Independent CLI review by a different model. Verify numbers against cards. Apply evidence-backed fixes only.

## DONE-WHEN
- [ ] dated folder exists with README (Q1 window filled), queue.md, log.md, notebooklm-state.md
- [ ] follow-list log includes nothing-new rows
- [ ] ≥40 cards in THIS read-papers/ (or shortfall + reason)
- [ ] three synthesis files exist; executive-summary has direct Q1, direct Q2 with TRUE/PARTIAL/NOT, last-touch replacement, confirm/revise 2026-09-17 plan
- [ ] Codex raw + independent review raw in review/
- [ ] no writes outside THIS folder

Return: the three file paths, card count, and a 10-line Q1 / Q2 / recommendation recap.
```

---

## Prompt B — independent parallel run (second model)

```text
Independent PARALLEL follow-up of the attribution-based-retention study. Same questions as the primary dated run, different folder, different answers.

Read and follow:
/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/SURVEY-MANUAL.md

## Output folder (write only here)
/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/YYYYMMDD_survey_grok/

Reuse NotebookLM notebook 6a3b8a8e-6f2f-4efe-99eb-283983fc95d9. Do not notebook_create.

Independence: you MAY copy process (folder layout, harvest.py, Codex prompt shape, review/context builder) from 20260917_survey/. You may NOT read sibling YYYYMMDD_survey/ executive-summary.md, literature-review.md, or method-tracker.md until YOUR three synthesis files exist. Do not merge folders. Do not edit SURVEY-MANUAL.md or PROMPTS.md.

Questions, Q2 TRUE/PARTIAL/NOT rubric, last-touch baseline, and v1-not-incremental rule: same as SURVEY-MANUAL.md.

Target 25–50 new cards. Skip parent read-papers/ and any titles already carded in a prior dated run (you may still write your own cards for titles you ingest if they are not in THIS folder).

Pipeline: harvest.py → D3/D4 → NLM cards (2 queries/paper) → compact review surface → Codex claude-literature-survey-nlm (3.5-lite / 4-B / 5) → independent review by a different model.

DONE-WHEN: ≥25 cards, three synthesis files with direct Q1/Q2/recommendation, review/ raw drafts, writes only in THIS folder.

Return: paths, card count, 10-line recap.
```

---

## Prompt C — resume an incomplete dated folder

```text
RESUME and FINISH the incomplete attribution follow-up at:

/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/YYYYMMDD_survey_grok/

(If you mean the 2026-09-17 Grok run, use …/20260917_survey_grok/ . Read that folder's queue.md, log.md, and read-papers/ first: discovery is done; cards may already exist; synthesis may still be missing.)

Read:
/Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/SURVEY-MANUAL.md
Then this folder's README.md, requirements.md, queue.md, log.md, discovery/*.md.

Follow literature-survey-nlm for Phase 3 onward only. Do not redo Phase 1/2. Do not rewrite README except Result summary at the end. Do not edit SURVEY-MANUAL.md or PROMPTS.md.

Reuse notebook 6a3b8a8e-6f2f-4efe-99eb-283983fc95d9. Do not notebook_create.

Process remaining queue rows into read-papers/ (NLM, 2 queries/paper). Expand from discovery/*.md only if count < 25. Cap 50. Skip parent ../read-papers/.

Then: compact review/context/ → 4 NLM cross-source queries → Codex skill claude-literature-survey-nlm (NOT claude-literature-survey) → method-tracker.md, literature-review.md, executive-summary.md → independent review by a different model.

Independence: do not copy Q1/Q2/v1–v3 claims from ../20260917_survey/ synthesis files until YOUR three files exist. Classify Q2 as TRUE / PARTIAL / NOT. v1 credit is not incremental unless a cited paper estimates that N7 contrast.

Write only in this folder. Ask before deleting.

DONE-WHEN: queue processed or skipped with reason; ≥25 cards; three synthesis files with direct Q1, Q2, last-touch replacement; review/ raw + independent review; Result summary + final log.md line.

Return: paths, card count, 10-line recap.
```

---

## Prompt D — recap completed run(s) (no new survey)

```text
Recap the attribution-based-retention follow-up surveys. Do not start a new run.

Read:
- /Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/SURVEY-MANUAL.md (questions + standing recommendation)
- /Users/fox/Projects/paper_reading_repo/literature-survey/attribution-based-retention/20260917_survey/executive-summary.md
- If it has synthesis files, also …/YYYYMMDD_survey/executive-summary.md and …/YYYYMMDD_survey_grok/executive-summary.md

Delegate large files to reading-agent. Do not re-process papers.

Return three sections only:
1. Questions we wanted answered (Q1, Q2, last-touch replacement)
2. Answers, with named papers. If two runs exist, say where they agree and where they disagree (especially TRUE vs PARTIAL vs NOT on Q2).
3. Next steps for the product (v1/v2/v3) and for the survey (only if a run is incomplete).
```
