# GBrain and Karpathy’s LLM Wiki

Focused comparison: how **[garrytan/gbrain](https://github.com/garrytan/gbrain)** positions itself relative to **[Andrej Karpathy’s LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)**.

**Last updated:** 2026-04-18

---

## Karpathy: LLM Wiki (the pattern)

**Source:** [llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — an “idea file” meant to be pasted into an agent; implementation is collaborative.

**Problem it solves:** Typical doc + LLM flows look like **RAG**: chunks are retrieved at query time and the model **re-derives** synthesis repeatedly, with little **accumulation** of structure.

**Core move:** The LLM **incrementally builds and maintains a persistent wiki** — interlinked markdown between you and **immutable raw sources**. On new sources, it integrates into entity/topic pages, updates summaries, and surfaces **contradictions**. Knowledge is **compiled and kept current**, not re-derived from scratch each question.

**Three layers (gist):**

| Layer | Role |
|--------|------|
| **Raw sources** | Curated inputs; LLM reads, does not edit. |
| **The wiki** | LLM-owned markdown (summaries, entities, cross-links). |
| **The schema** | Conventions + workflows (e.g. `CLAUDE.md` / `AGENTS.md`) so the agent behaves like a maintainer, not a generic chatbot. |

**Operations (gist):** **Ingest** (source → many wiki updates), **Query** (read wiki, synthesize; good answers can be filed back), **Lint** (contradictions, staleness, orphans, gaps).

**Navigation aids:** `index.md` (catalog), `log.md` (append-only timeline). Optional tooling (e.g. hybrid markdown search / MCP) at larger scale.

**Framing:** “Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.” Related in spirit to **Vannevar Bush’s Memex** — the missing piece historically was **who maintains the links**; the LLM is proposed as that maintainer.

---

## GBrain: operational extension of the same idea

**Source:** [garrytan/gbrain README](https://github.com/garrytan/gbrain) and **[docs/GBRAIN_RECOMMENDED_SCHEMA.md](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_RECOMMENDED_SCHEMA.md)** (system prompt / schema doc for agents).

**Authorship / intent:** Public **open-source** “knowledge brain” for AI agents, described as built for **YC President/CEO Garry Tan’s** real agent deployments (OpenClaw, Hermes, etc.), with **skills**, **hybrid search**, **graph-style linking**, **cron / overnight maintenance**, and **MCP** integration — i.e. a **productized runtime** around the wiki metaphor, not only a folder of markdown rules.

**Explicit link to Karpathy (schema doc):**

> “This is **Karpathy's LLM wiki pattern**, but **extended from research notes into a full operational knowledge base** — one that integrates with your **calendar, email, meetings, social media, and contacts** to stay continuously current.”  
> — `GBRAIN_RECOMMENDED_SCHEMA.md` (intro)

**Shared DNA with the gist:**

- **Synthesis pre-computed** vs RAG re-derivation:  
  > “This is the Karpathy wiki pattern's killer feature: **the synthesis is pre-computed.** Unlike RAG, where the LLM re-derives knowledge from scratch every query, your brain has already done the work. The cross-references are already there. The contradictions have already been flagged.”

**Where GBrain goes beyond the gist (per same doc):**

- **Operational pipelines:** enrichment on **every signal** (meetings, email, social, contacts), not only **manual** source drops:  
  > “This is what distinguishes an **operational brain** from **Karpathy's research wiki**. He describes ingesting sources **you manually add**. An operational brain goes further…”

- **Structured page model:** **Compiled truth** (above the fold, rewritten) + **Timeline** (append-only evidence below), aligned with “compiled” knowledge but with explicit **audit trail**.

- **Deterministic + LLM mix:** README emphasizes **skills as code**, **thin harness / fat skills**, **hybrid search** (e.g. RRF), **self-wiring** typed links without an LLM for every edge, benchmarks, **PGLite**, CLI, etc.

---

## Side-by-side (rough)

| Dimension | Karpathy LLM Wiki (gist) | GBrain (repo) |
|-----------|---------------------------|---------------|
| **Form** | Pattern / idea file | Full application + CLI + MCP + skills |
| **Ingest** | User-directed raw drops + agent ingest | Same *idea*, plus automated ingestion skills (email, meetings, media, etc.) per README |
| **Maintenance** | Lint + log; human/agent discipline | Cron / “dream” style jobs, citation fixers, enrich pipelines (as described in README & schema) |
| **Storage** | Markdown git repo + optional search | Brain-specific storage (e.g. PGLite), graph + hybrid retrieval per project docs |
| **Best for** | Anyone bootstrapping a **minimal** wiki-in-git workflow | Teams/agents wanting **batteries-included** operational brain |

---

## URLs (canonical)

- Karpathy gist: `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`
- GBrain repo: `https://github.com/garrytan/gbrain`

---

## Note

This note is **synthesis** from public README/schema text and the gist; it is not an endorsement or security review. For behavior and data handling, rely on upstream docs and your own threat model.
