# Phase 3 batch brief — constant block (reused for every batch)

You are processing a batch of papers for a literature survey using NotebookLM. Zero prior context assumed.

## Notebook and output

- **Notebook ID:** `67046a44-7490-4fe5-b54a-3f39ef37fdd3`
- **Output folder:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/read-papers/`

## FILE ALLOWLIST — strict

Create only `.md` files inside the output folder above, one per paper in your batch. Create nothing else. Do not touch `/Users/fox/.claude/`. Do not modify `queue.md`, `requirements.md`, or `README.md` — the lead updates those. Make no NotebookLM writes: never call `source_add`, `source_delete`, or `notebook_create`.

## Tool loading

`ToolSearch(query: "select:mcp__notebooklm-mcp__notebook_query", max_results: 3)`

## Project Context — the north star for Query 3

Read `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/README.md` in full before you start. Its `## Project Context` section governs what you extract.

Summary you must hold in mind while reading every paper:

- The team ranks candidate profiles (user B) for a viewer (user A) on a dating app.
- Today: a CTR/CVR-style model predicts like, match, and conversation. An uplift model estimates the extra retention and revenue those events cause. The two are blended after the fact.
- Target: **one unified model** that predicts the retention and revenue following from showing B to A, with retention and revenue as the training objective.
- Constraints: reciprocity, congestion, a cascade from impression to subscription, low base rates, delayed labels (retention 7–30 days, revenue over weeks), a revenue mix of subscriptions and a la carte features, and a success paradox where a good match can end the user's tenure.
- **Prediction vs. incrementality is the distinction to track for every paper.** Retention conditional on exposure is not the effect of the exposure.

## Per paper: three independent queries

Use **independent** queries. Do **not** pass `conversation_id`. Threading contaminates answers across questions.

Scope every query with `source_ids=["<the source_id for this paper>"]`.

**Query 1:**
> "For the paper in this source, provide all of the following clearly labeled: (1) Core problem and key contribution (2) Proposed method or architecture in detail (3) Datasets used for evaluation and comparison baselines"

**Query 2:**
> "For the paper in this source, provide all of the following clearly labeled: (1) Key quantitative results and improvements over baselines (2) Limitations, failure modes, or negative results noted by the authors (3) Top 5–7 most heavily cited prior works named in the related work or introduction"

**Query 3 (project-specific — this one carries the survey):**
> "For the paper in this source, answer each of the following separately and label them. (1) What is the training objective, and exactly how is the label defined? State the time horizon and how delay or censoring is handled. (2) Does the model predict an outcome, or does it estimate the causal effect of the exposure? Quote the paper's own wording if it addresses this. (3) How does a user-level or delayed outcome get assigned to an item-level decision — one impression, one item, or one slate? (4) Does the paper deal with a two-sided or reciprocal market, congestion for a shared limited resource, or fairness across two sides? (5) How is the method evaluated offline, and how is it evaluated online? (6) State what the paper does NOT address among these points."

**Refusal handling.** After each response, scan for refusal language: "I cannot answer", "not mentioned in the source", "I don't have enough information", or similar. Replace that section's content with exactly `Not specified in source.` Never copy NotebookLM refusal boilerplate into the markdown.

## Filename rule

`YYYY_Venue_MethodName_Paper-Title.md`

- `YYYY` — publication year (arXiv submission year if no venue).
- `Venue` — `KDD`, `WWW`, `RecSys`, `CIKM`, `SIGIR`, `WSDM`, `AAAI`, `IJCAI`, `NeurIPS`, `arXiv`, or `Blog` for a company engineering post.
- `MethodName` — the primary named method (`ESMM`, `RLUR`, `xMTF`, `OneRec`). Use `NA` when the paper names no method.
- `Paper-Title` — title-cased, hyphen-separated, special characters removed, max ~6 words.

## Markdown structure for each paper

Follow the paper-reader report template, with the survey additions. Sections in this order:

1. `# Paper Analysis: [Title]` with `**Source:**` and `**Date analyzed:**`
2. `## 1. Summary` — title, authors, abstract, key contributions, methodology, main results (from Query 1)
3. `## 2. Experiment Critique` — design, statistical validity, online experiments, reproducibility, overall (from Query 2)
4. `## 3. Industry Contribution` — deployability, problems solved, engineering cost. Frame in recommender-engineering terms: latency, online serving, feature engineering, ranking pipelines.
5. `## 4. Novelty vs. Prior Work` — claimed novelty and the prior work named in Query 2 part 3
6. `## 5. Dataset Availability` — datasets table
7. `## 6. Community Reaction` — write `Not assessed in NotebookLM mode.` Do not run web searches for this.
8. `## 7. Reference Card` — **the survey's core deliverable.** See the field list below.
9. `## Project Relevance` — see below.
10. `## Papers That Mention This Paper (Reverse Citation Map)` — leave the placeholder row. Phase 3.7 fills it.
11. `## Meta Information` — authors, affiliations, venue, year, relevance, priority, `nlm:<source_id>`

### `## 7. Reference Card` — 13 fields, every paper, in this order

| # | Field | Note |
|---|---|---|
| 1 | Title, authors or company, venue, year, URL | |
| 2 | Source type | blog / industry paper / academic |
| 3 | Direction | D1–D9, as given in your batch list |
| 4 | Problem setting | |
| 5 | Objective and label definition | include horizon and delay handling — Query 3 part 1 |
| 6 | **Prediction or incrementality** | Query 3 part 2. Never leave blank. If the paper does not address it, write `Prediction only — the paper does not address incrementality.` |
| 7 | Model architecture | |
| 8 | **Credit assignment** | Query 3 part 3. How a user-level outcome maps to an item-level decision. |
| 9 | Training data and counterfactual handling | |
| 10 | Offline and online evaluation | Query 3 part 5 |
| 11 | Reported gains | with dataset and metric named, never a bare percentage |
| 12 | Applicability to a two-sided dating recommender | exactly 2 lines. Use Query 3 part 4. |
| 13 | Unverified claims | anything the source asserts without evidence, marked as such |

### `## Project Relevance`

Assess whether and how this paper's method addresses the project need described in the Project Context. Be specific — name which of the eight research questions it speaks to.

If the paper does not meaningfully address the project's needs, **prefix the section with** `**Low project relevance.** [reason]`. That is a useful signal, not a failure — it flags a retrieval mismatch.

## Depth rule

- **Priority 1–2 papers:** fill every section.
- **Priority 3–4 or Peripheral papers:** write a one-paragraph summary plus the full Reference Card and Project Relevance. Do not pad the other sections.

## Writing rules

- Be factual. Do not editorialize past what the paper claims. Separate the paper's claims from your assessment.
- Cite results with dataset and metric together. Write "AUC +0.3% on the Criteo delayed-feedback benchmark", never "+0.3%".
- No abbreviations for papers. Write "author et al., full paper title, venue year".
- If experiments are weak, say so plainly. Do not soften a critique.

## Return format

```
BATCH COMPLETE
Written: <n> files
Skipped: <filename> | <reason>   (or "none")
New candidate papers found in related work:
[Title] | [arXiv/URL if available] | [Relevance: Core/Related/Peripheral]
...
Methods seen (for method-tracker):
[Method] | [used as baseline: yes/no] | [variant of: X or none] | [component count]
...
```

No preamble. No per-paper recap. No file contents.
