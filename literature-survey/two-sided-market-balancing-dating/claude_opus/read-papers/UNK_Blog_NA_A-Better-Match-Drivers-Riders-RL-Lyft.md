# Paper Analysis: A Better Match for Drivers and Riders: Reinforcement Learning at Lyft

**Source:** NotebookLM source_id `b0bf71c0-91b5-4806-aa47-ae062de27e76` (Lyft Engineering, per queue manifest)
**Date analyzed:** 2026-08-16

---

## EXTRACTION FAILED — source returned no grounded content

All three required NotebookLM queries for this source returned a hard API error (`RESOURCE_EXHAUSTED`, error code 8 — "Google rejected the query... may indicate account-level restrictions on programmatic access") rather than a normal response. This is distinct from the "empty `sources_used`" invalid-answer case, but the same rule applies: no grounded content was obtained, so nothing below is filled from paper content, title inference, or model background knowledge.

Retry history: initial 3-query batch failed identically for all three queries; retried the core query (Query 1) after a 30s wait — failed again; retried once more after a 90s wait — failed again. Five total attempts across ~4 minutes, all `RESOURCE_EXHAUSTED`. Per the batch brief's retry policy and the circuit-breaker rule against unbounded retries, this is recorded as a failure and the batch moves on rather than looping further.

None of the standard report-template sections (Summary, Experiment Critique, Industry Contribution, Novelty, Dataset Availability, Community Reaction) are populated, since no source content was retrieved.

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Unknown — extraction failed
**Affiliations:** Lyft (per queue manifest title only; not independently confirmed)
**Venue:** Unknown — extraction failed
**Year:** Unknown — extraction failed
**PDF:** Not fetched — NotebookLM source query failed (RESOURCE_EXHAUSTED)
**Relevance:** Unknown — extraction failed
**Priority:** 1 (per queue tier, from manifest — not independently verified)

---

## Bibliography Fields

- **title:** A Better Match for Drivers and Riders: Reinforcement Learning at Lyft (per queue manifest title)
- **authors or organization:** Unknown — extraction failed (manifest suggests Lyft)
- **year:** Unknown — extraction failed
- **venue or type:** Unknown — extraction failed
- **link:** Unknown — extraction failed
- **tier tag:** Tier 1 — Adjacent marketplace (rideshare), per queue manifest
- **what they did (≤80 words):** Not available — all three NotebookLM queries for this source returned a hard API error (RESOURCE_EXHAUSTED) rather than content; nothing was retrieved to summarize.
- **mechanism relevant to two-sided balancing (≤50 words):** Not available — extraction failed.
- **metrics used, and the reported effect:** Not available — extraction failed.
- **fit for a dating app:** unknown — cannot be assessed without retrieved content.
- **confidence that the item is real and described correctly:** low — no content was ever retrieved from this source; only the manifest's title/tier are known, and those are unverified against the actual source.

---

## Project Relevance

**Low project relevance.** Not because the topic is off-target (rideshare driver/rider matching is plausibly a strong Tier-1 analogue), but because extraction failed entirely — three independent NotebookLM queries against source_id `b0bf71c0-91b5-4806-aa47-ae062de27e76` all returned `RESOURCE_EXHAUSTED` errors with no content, across five total attempts and two retries with waits. This source should be re-queued for a later re-extraction attempt once NotebookLM API quota/rate-limit conditions clear, rather than treated as assessed-and-low-relevance.
