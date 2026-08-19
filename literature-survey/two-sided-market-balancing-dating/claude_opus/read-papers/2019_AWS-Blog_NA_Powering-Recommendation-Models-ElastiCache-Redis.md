# Paper Analysis: Powering recommendation models using Amazon ElastiCache for Redis at Coffee Meets Bagel

**Source:** AWS Database Blog — Daniel Pyrathon and David O'Steen, 16 Jan 2019 (https://aws.amazon.com/blogs/database/powering-recommendation-models-using-amazon-elasticache-for-redis-at-coffee-meets-bagel/)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Powering recommendation models using Amazon ElastiCache for Redis at Coffee Meets Bagel
**Authors:** Daniel Pyrathon, David O'Steen (Coffee Meets Bagel / AWS)
**Abstract:**
Coffee Meets Bagel (CMB) engineering blog post describing a hybrid offline/online recommendation architecture built on Amazon ElastiCache for Redis. Serves >1.5M daily users; solves the problem of pre-computing per-user match queues cheaply (avoiding quadratic storage) and filtering already-seen profiles efficiently, replacing a previous Cassandra-based system.

**Key contributions:**
- Hybrid architecture: offline batch job (7 AM daily, 6–7 hrs) trains item-based collaborative filtering to produce 100 latent features/user, written to Redis; online layer computes cosine similarity between a user's vector and candidates' vectors, ranks by similarity, and stores results in Redis sorted sets (2–4ms reads).
- Custom Bloom filters implemented directly on Redis bit operations (SETBIT/GETBIT, fixed size 2^17 bits/user) to replace quadratic-space exclusion sets (n_users × n_users) with linear-space seen-profile filtering (n_users × bloom_filter_size), filtering tens of thousands of candidates in ~170ms.
- Migrated off Cassandra (eventual-consistency latency spikes, high ops burden) to Redis/ElastiCache for consistency and lower maintenance.

**Methodology:**
Offline: item-based collaborative filtering on match history → 100 latent features/user. Online: cosine similarity ranking of candidates against a user's previously-liked profiles, stored in Redis sorted sets; Bloom-filter-based seen/unseen filtering via Redis bit vectors.

**Main results:**
Reads: 2–4ms average. Writes: 3–4 seconds/user in small batches. Bloom filter bulk evaluation: ~170ms for tens of thousands of candidates. Storage complexity reduced from quadratic (raw exclusion sets) to linear (Bloom filters).

---

## 2. Experiment Critique

**Design:**
No controlled experiment — this is a systems/infrastructure engineering post. Comparisons to Cassandra and pure on-demand Elasticsearch are qualitative production-experience narratives, not controlled A/B tests.

**Statistical validity:**
Not applicable — latency and throughput numbers are point-in-time production averages with no variance, sample size, or significance reporting.

**Online experiments (if any):**
None described; no A/B test of recommendation quality is reported (the post is about serving infrastructure, not model quality).

**Reproducibility:**
Code snippets for cosine similarity and Bloom filter bit operations are given inline, but no full codebase, dataset, or model hyperparameters are released.

**Overall:**
Credible as an infrastructure case study; latency/throughput claims are plausible for the described architecture but unverified by controlled comparison. No claims are made about recommendation *quality*, match rate, or user outcomes — only about system performance.

---

## 3. Industry Contribution

**Deployability:**
Directly deployable pattern — described as already running in production at CMB (>1.5M daily users), using a managed AWS service (ElastiCache for Redis).

**Problems solved:**
Solves two concrete engineering problems relevant to recsys serving: (1) precomputing large personalized candidate queues without quadratic storage growth, via Redis sorted sets + nightly batch scoring; (2) efficient seen-item exclusion at scale via custom Bloom filters on Redis bitmaps instead of raw sets.

**Engineering cost:**
Moderate — requires an offline ML/batch pipeline (Spark/NumPy/Pandas/S3/Parquet implied) feeding Redis, plus hand-rolled Bloom filter logic (noted by the authors as "fairly hard to debug"; they recommend a prebuilt library/Redis's ReBloom module instead).

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Not applicable — no novelty claims; this is an engineering case study, not a research contribution.

**Prior work comparison:** The post itself compares only against the company's own prior infrastructure (Cassandra) and an alternative approach (pure on-demand Elasticsearch), not against academic literature.

**Verification:** Not specified in source. Per NotebookLM's query, the post cites no academic works — only three technical references (a Bloom Filter Calculator, a Redis pipelining guide, and the Redis "ReBloom" module documentation).

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| CMB internal match history | N/A | No | Internal production data, hundreds of days of match history, not public |

**Offline experiment reproducibility:**
Not reproducible — no public dataset; architecture and code snippets are illustrative only.

---

## 6. Community Reaction

No significant community discussion found (not investigated as part of this NotebookLM-based extraction).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Daniel Pyrathon, David O'Steen
**Affiliations:** Coffee Meets Bagel; published via AWS (Amazon)
**Venue:** AWS Database Blog (engineering blog post)
**Year:** 2019
**PDF:** Not available — web article, accessed via NotebookLM source
**Relevance:** Related
**Priority:** 2

---

## Bibliography Fields

- **title:** Powering recommendation models using Amazon ElastiCache for Redis at Coffee Meets Bagel
- **authors or organization:** Daniel Pyrathon, David O'Steen; Coffee Meets Bagel / AWS
- **year:** 2019
- **venue or type:** AWS Database Blog (engineering blog post)
- **link:** https://aws.amazon.com/blogs/database/powering-recommendation-models-using-amazon-elasticache-for-redis-at-coffee-meets-bagel/
- **tier tag:** Tier 1 — Dating-platform primary source

**what they did (≤80 words):** Coffee Meets Bagel describes a hybrid offline/online recommendation architecture: nightly item-based collaborative filtering produces 100 latent features per user, an online layer ranks candidates by cosine similarity to previously-liked profiles and stores results in Redis sorted sets, and a custom Bloom-filter-on-Redis-bitmaps mechanism filters already-seen profiles in linear rather than quadratic space, replacing a Cassandra-based system that suffered consistency and maintenance problems.

**mechanism relevant to two-sided balancing (≤50 words):** None. Per NotebookLM, recommendations rank candidates unilaterally by the viewer's taste similarity; no reciprocal-interest check, no per-user reply-capacity limit, and no exposure redistribution away from over-subscribed profiles exist — candidates are treated as infinite-capacity items to filter and rank.

**metrics used, and the reported effect:** Read latency 2–4ms; write latency 3–4s/user in batches; Bloom-filter bulk seen-filtering ~170ms for tens of thousands of candidates; storage complexity reduced from O(n²) (raw exclusion sets) to O(n) (Bloom filters). All are systems/infra metrics — no recommendation-quality or match-outcome metric reported.

**fit for a dating app:** high — reason: it is a real dating platform's production recommendation-serving stack, useful as an engineering reference, but it addresses serving infrastructure, not the market-balancing problem itself.

**confidence that the item is real and described correctly:** high — all three NotebookLM queries returned `sources_used` matching this source_id, with detailed, internally consistent, and specific technical content (byline, date, code snippets, URL).

---

## Project Relevance

**Low project relevance.** This source is a serving-infrastructure case study, not a market-balancing or matching-quality mechanism. NotebookLM's direct answer confirms the system treats every candidate as an unconstrained, infinite-capacity "item" to rank by unilateral taste-similarity — there is no reciprocal-interest scoring (no check that the candidate would also like the viewer back), no per-user reply-capacity accounting, no demotion of over-subscribed "superstar" profiles, and no match-distribution-fairness metric anywhere in the architecture. The one loosely relevant detail is CMB's own stated problem framing — a noon push notification creates simultaneous traffic spikes and a "quality over quantity" curated-queue design — which is adjacent to the project's market-design lever of curated batch delivery, but the post does not describe *how* (or whether) the batch composition accounts for a candidate's capacity to reply. Useful only as an engineering reference for how a real dating app serves precomputed recommendation queues at scale (Redis sorted sets, Bloom-filter seen-exclusion) — not as a source of mechanisms for reciprocal scoring, capacity-aware allocation, or ecosystem-health metrics.
