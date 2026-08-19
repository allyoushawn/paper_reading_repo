# Phase 3 batch brief — DIRECT PDF mode (constant block)

Use this variant when NotebookLM is unavailable. It replaces the three `notebook_query` calls with
direct reading of a local PDF. Everything downstream — the card structure, the 13-field Reference
Card, the depth rule, the writing rules — is identical to the NotebookLM variant.

You are processing a batch of papers for a literature survey. Zero prior context assumed.

## Hard constraints

- **DO NOT SPAWN SUBAGENTS.** Do all work yourself. Never call the Agent tool.
- **Do not call any NotebookLM tool.** That service is unavailable. Do not try.
- **Do not use web search.** Everything you need is in the PDF.

## Output

`/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/read-papers/`

Create only `.md` files there, one per paper. Create nothing else. Do not touch `/Users/fox/.claude/`.
Do not modify `queue.md`, `requirements.md`, or `README.md` — the lead updates those.

## How to read each paper

Use the **Read** tool on the local PDF path given in your batch table.

- PDFs over 10 pages **require** the `pages` parameter, maximum 20 pages per request.
- Start with `pages: "1-12"`. That usually covers abstract, introduction, method, and the start of
  experiments.
- If results, limitations, or related work are not yet covered, make a second call for later pages.
- **Two Read calls per paper is the normal budget. Three is the maximum.** Do not read a long paper
  end to end — target the sections the card needs.

## Project Context — the north star

Read `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/README.md`
once, before starting. Its `## Project Context` section governs what you extract.

Summary to hold in mind for every paper:

- The team ranks candidate profiles (user B) for a viewer (user A) on a dating app.
- Today: a CTR/CVR-style model predicts like, match and conversation. A separate uplift model
  estimates the extra retention and revenue those events cause. The two are blended after the fact.
- Target: **one unified model** predicting the retention and revenue that follow from showing B to A,
  with retention and revenue as the training objective.
- Constraints: reciprocity, congestion, a cascade from impression to subscription, low base rates,
  delayed labels (retention 7–30 days, revenue over weeks), a revenue mix of subscriptions and a la
  carte features, and a success paradox where a good match can end a user's tenure.
- **Prediction vs. incrementality is the distinction to track in every paper.** Retention conditional
  on exposure is not the effect of the exposure.

## What to extract — same three groups as the NotebookLM variant

**Group 1 (from abstract, introduction, method):** core problem and key contribution; the proposed
method or architecture in detail; datasets used and comparison baselines.

**Group 2 (from experiments, limitations, related work):** key quantitative results and improvements
over baselines; limitations, failure modes or negative results the authors state; the 5–7 most
heavily cited prior works named in related work or introduction.

**Group 3 — the project-specific group that carries the survey. Answer each separately:**
1. What is the training objective, and exactly how is the label defined? State the time horizon and
   how delay or censoring is handled.
2. Does the model predict an outcome, or estimate the causal effect of the exposure?
3. How does a user-level or delayed outcome get assigned to an item-level decision — one impression,
   one item, or one slate?
4. Does the paper deal with a two-sided or reciprocal market, congestion for a shared limited
   resource, or fairness across two sides?
5. How is the method evaluated offline, and how online?
6. What does the paper **not** address among these points?

**If the PDF does not state something, write `Not specified in source.`** Never infer a value and
present it as the paper's. Never invent a number, a venue, or a baseline.

## Filename rule

`YYYY_Venue_MethodName_Paper-Title.md`

- `Venue`: `KDD`, `WWW`, `RecSys`, `CIKM`, `SIGIR`, `WSDM`, `AAAI`, `IJCAI`, `NeurIPS`, `arXiv`, or
  `Blog`.
- `MethodName`: the primary named method (`ESMM`, `DEFUSE`, `OneRec`). Use `NA` if unnamed.
- `Paper-Title`: title-cased, hyphen-separated, special characters removed, max ~6 words.

## Markdown structure — 11 sections in this order

1. `# Paper Analysis: [Title]` with `**Source:**` (the local PDF path) and `**Date analyzed:**`
2. `## 1. Summary` — title, authors, abstract, key contributions, methodology, main results
3. `## 2. Experiment Critique` — design, statistical validity, online experiments, reproducibility
4. `## 3. Industry Contribution` — deployability, problems solved, engineering cost, framed in
   recommender-engineering terms: latency, online serving, feature engineering, ranking pipelines
5. `## 4. Novelty vs. Prior Work`
6. `## 5. Dataset Availability` — a table
7. `## 6. Community Reaction` — write exactly `Not assessed in direct-PDF mode.`
8. `## 7. Reference Card` — the 13 fields below
9. `## Project Relevance`
10. `## Papers That Mention This Paper (Reverse Citation Map)` — leave the placeholder row
11. `## Meta Information` — authors, affiliations, venue, year, relevance, priority, `nlm:<source_id>`

### `## 7. Reference Card` — 13 fields, every paper

| # | Field | Note |
|---|---|---|
| 1 | Title, authors or company, venue, year, URL | |
| 2 | Source type | blog / industry paper / academic |
| 3 | Direction | D1–D9, as given in your batch table |
| 4 | Problem setting | |
| 5 | Objective and label definition | include horizon and delay handling |
| 6 | **Prediction or incrementality** | Never blank. If the paper does not address incrementality, write `Prediction only — the paper does not address incrementality.` |
| 7 | Model architecture | |
| 8 | **Credit assignment** | How a user-level outcome maps to an item-level decision |
| 9 | Training data and counterfactual handling | |
| 10 | Offline and online evaluation | |
| 11 | Reported gains | dataset and metric named, never a bare percentage |
| 12 | Applicability to a two-sided dating recommender | exactly 2 lines |
| 13 | Unverified claims | anything asserted without evidence, marked as such |

### `## Project Relevance`

Name which of the eight research questions the paper speaks to. If it does not meaningfully address
the project's needs, prefix with `**Low project relevance.** [reason]`. That is a useful signal, not
a failure.

## Depth rule

- **Priority 1–2:** fill every section.
- **Priority 3–4 or Peripheral:** one-paragraph summary plus the full Reference Card and Project
  Relevance. Do not pad the rest.

## Writing rules

- Factual only. Separate the paper's claims from your assessment.
- Cite results with dataset and metric together: "AUC +0.3% on the Criteo delayed-feedback benchmark",
  never "+0.3%".
- No paper abbreviations. Write "author et al., full paper title, venue year".
- If experiments are weak, say so plainly.

## Return format

```
BATCH COMPLETE
Written: <n> files
Skipped: <filename> | <reason>   (or "none")
New candidate papers found in related work:
[Title] | [URL if stated] | [Relevance: Core/Related/Peripheral]
...
Methods seen (for method-tracker):
[Method] | [used as baseline: yes/no] | [variant of: X or none] | [component count]
...
```

No preamble. No per-paper recap. No file contents.
