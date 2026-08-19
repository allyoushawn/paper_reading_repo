# cursor-grok paper card instructions

Workplace: `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/cursor-grok/`
Write cards only under `read-papers/`. Do not edit shared `README.md`, `requirements.md`, `queue.md`, `notebooklm-state.md`, or any other model's subfolder (`claude_opus/`, etc.).

Notebook ID: `67046a44-7490-4fe5-b54a-3f39ef37fdd3`

## NLM query protocol

1. Call `GetMcpTools` for `user-notebooklm-mcp` / `notebook_query` before the first query.
2. Then `CallMcpTool` server=`user-notebooklm-mcp` toolName=`notebook_query`.
3. Independent queries — do NOT pass `conversation_id`.
4. Scope every query with `source_ids=[<this paper's source_id>]`.
5. If a response contains refusal language ("I cannot answer", "not mentioned in the source", "I don't have enough information"), replace that section with `Not specified in source.`

### Query 1

> For the paper in this source, provide all of the following clearly labeled:
> (1) Core problem and key contribution
> (2) Proposed method or architecture in detail
> (3) Datasets used for evaluation and comparison baselines

### Query 2

> For the paper in this source, provide all of the following clearly labeled:
> (1) Key quantitative results and improvements over baselines
> (2) Limitations, failure modes, or negative results noted by the authors
> (3) Top 5–7 most heavily cited prior works named in the related work or introduction

### Query 3

> For this source, extract only what the source states (not inferences). If a point is absent, write "Not specified in source."
> (1) Ranking objective: retention / LTV / revenue vs CTR-like proxies
> (2) Credit assignment: how a user-level delayed outcome maps to an item-level decision (one exposure or one slate)
> (3) Label and horizon definitions; delay, sparsity, censoring handling
> (4) How short-term event heads combine with long-term heads: fixed fusion, learned fusion, or one value head
> (5) Prediction vs incrementality: does the model predict the outcome, or the effect of the exposure?
> (6) Offline and online evaluation, especially delayed/noisy retention and two-sided interference
> (7) Reciprocity, congestion, fairness across sides, revenue vs match quality trade-off
> (8) Any migration path from a CTR-like model toward a unified long-term model

## Filename

`YYYY_Venue_MethodName_Paper-Title.md`

- Venue abbreviations: KDD, WWW, RecSys, WSDM, SIGIR, CIKM, IJCAI, AAAI, NeurIPS, ICML, arXiv, Blog, TechCrunch
- MethodName: primary named method, or `NA`
- Paper-Title: title-cased, hyphens, max ~6 words

## File body (required order)

Start with the **Survey Card** (brief-mandated fields). Then the paper-reader sections.

```markdown
# Paper Analysis: [full title]

**Source:** [working URL]
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:**
- **authors or company:**
- **venue:**
- **year:**
- **URL:** [must be a working URL]
- **source type:** blog / industry paper / academic
- **direction:** D1–D9
- **problem setting:**
- **objective and label definition:** [horizon + delay handling]
- **prediction or incrementality:** [predicts outcome vs effect of exposure]
- **model architecture:**
- **credit assignment:** [user-level outcome → item-level decision]
- **training data and counterfactual handling:**
- **offline and online evaluation:**
- **reported gains:**
- **applicability note for a two-sided dating recommender:** [exactly 2 lines]
- **unverified claims:** [mark as such, or "none"]

## 1. Summary
...
## 2. Experiment Critique
...
## 3. Industry Contribution
...
## 4. Novelty vs. Prior Work
...
## 5. Dataset Availability
...
## 6. Community Reaction
No significant community discussion found.  [do not spend a web-search round unless a claim is disputed]

## Project Relevance
[Query 3 answer, structured. Prefix with **Low project relevance.** if it does not address retention/LTV ranking, credit assignment, delayed labels, or two-sided markets.]

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information
**Authors:**
**Affiliations:**
**Venue:**
**Year:**
**PDF:**
**Relevance:** Core / Related / Peripheral
**Priority:** 1 / 2 / 3 / 4
```

Rules:
- Do not invent titles, venues, or results.
- Separate what the source states from what you infer. Label inferences as inference.
- Every card needs a working URL.
- For Priority 3–4 / Peripheral papers: one-paragraph summary + Survey Card + Project Relevance only.
