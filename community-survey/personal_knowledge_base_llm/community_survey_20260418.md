# Community Survey: Personal knowledge base LLM

**Date:** 2026-04-18  
**Time window:** last 30 days  
**Mode:** full

## Source Snapshots

### Hacker News

**Show HN: Memoriki – LLM Wiki + MemPalace** ([item 47711037](https://news.ycombinator.com/item?id=47711037))  
Template combining Karpathy’s LLM Wiki pattern (structured markdown with `[[wiki-links]]` and YAML frontmatter maintained by an LLM) with MemPalace (MCP server for semantic search and a temporal knowledge graph). Three layers: wiki pages, embedding-based semantic search (ChromaDB), and a typed knowledge graph with date validity (“what changed since last month?”). Positioned explicitly as **not RAG**: knowledge is compiled into wiki pages once and kept current as sources arrive; the graph tracks connections.

**Show HN: Atomic – Self-hosted, semantically connected personal knowledge base** ([item 47470433](https://news.ycombinator.com/item?id=47470433))  
Strong engagement in-thread. **Themes:** (1) **Privacy and granular control** — unease about large personal corpora being available to an AI without fine-grained policy; interest in “security-focused” agents and tools like greywall.io for approve/deny and learnable policies. (2) **Local vs cloud** — Ollama/local models vs ease of use and hardware limits. (3) **Developer workflow** — frustration with session compaction and flat “memory” markdown; desire for hooks so session insights flow into the KB automatically (MCP `create_atom` + semantic search). (4) **Product honesty** — author notes the graph visualization is more “fun” than core value today vs wiki generation, auto-tagging, and chat/MCP. **Stack notes:** SQLite (including vectors), RSS, web clipper, folder import (desktop), manual URL/atom; macOS signing was a pain point (later addressed in v1.1.0).

**Other recent adjacent threads (titles from search):** LLM-context-base (Git template for LLM-powered personal wikis with lint for stale content), LLM Wiki “idea file” discussion, Inquisitive (self-hosted KB with RAG).

### Engineering Blogs

**Meta — Engineering at Meta (April 2026)**  
[How Meta Used AI to Map Tribal Knowledge in Large-Scale Data Pipelines](https://engineering.fb.com/2026/04/06/developer-tools/how-meta-used-ai-to-map-tribal-knowledge-in-large-scale-data-pipelines/) describes an **organizational** analogue to personal KB tooling: 50+ specialized agents produced **59 concise “compass, not encyclopedia” context files** (~25–35 lines, ~1k tokens each) covering 4,100+ files across repos, capturing **50+ non-obvious patterns** (tribal knowledge). Reported **~40% fewer AI agent tool calls per task** in preliminary tests; multi-round critic passes; periodic jobs to validate paths, detect gaps, and refresh stale context. The post **engages with skepticism** from recent research suggesting AI-generated context files can *hurt* agents on well-known open-source codebases (models already “know” Django/matplotlib)—and argues their proprietary config-as-code setting is the opposite case: **concise, opt-in, quality-gated** context beats burning 15–25 exploratory tool calls.

**Other named company blogs (Anthropic, OpenAI, Google, Apple ML, Netflix, LinkedIn, x.ai):** No strong, topic-specific hits in this window surfaced by the broad `site:` query; signal this run is **Meta-heavy** for “big tech” blogging.

### ProductHunt

Search surfaced several **AI + documents / second brain** style products (names and positioning from listings; verify launch dates on PH): **Second Brain** (visual board + AI chat over interconnected KB), **Pocket LLM** (local/neural search over large document sets), **iWeaver** (summaries across videos, PDFs, web, podcasts), **MyMemo** (“digital brain,” ChatGPT-oriented), **Recall** (“Summarize Anything, Forget Nothing,” augmented browsing). Treat upvote ranks and “last 30 days” strictly as **approximate**—Product Hunt pages often mix historical launches with recent updates.

### Medium / Substack

**Dominant thread:** Karpathy **LLM Wiki** (early April 2026) and the shift from **retrieval to compilation** — persistent, cross-linked markdown wiki maintained by agents, `raw/` vs `wiki/` style layouts, Obsidian + Claude Code / Cursor as common stack.

**Examples fetched/previewed:**  
- *LLM Wiki Skill: Build a Second Brain With Claude Code and Obsidian* (Rezvani) — frames the gist’s traction (stars/forks in opening) and “compilation not retrieval” as the core reframing.  
- *I used Karpathy’s LLM Wiki to build a knowledge base that maintains itself with AI* (Kosuri) — narrative: scattered docs → working PKM quickly using Cursor + Obsidian; full article behind Medium paywall in fetch (teaser + responses only).

Additional search hits in the same window: posts titled around “living knowledge base,” Karpathy workflow explainers, and “your LLM has been forgetting everything” angle.

### X / Twitter (indirect)

Direct `x.com` fetches are not used per skill constraints. **Indirect signal** from search and secondary pages: heavy **cross-linking to Karpathy’s LLM Wiki gist** (fork/interest counts repeated in blog summaries), **dev.to** guides (e.g. 12-month SEO/experience posts, “what actually works” setup guides), and **GitHub ecosystem** names surfacing in summaries: e.g. **claude-memory-compiler**, **sage-wiki**, **llm-knowledge-base** — patterns: compile chat or papers into wikis, Obsidian integration, large-scale document counts claimed in README-style blurbs. **News-style pages** (e.g. AI tools directories, Frank’s World) echo the same “ingest / query / lint” trilogy for LLM Wiki-style systems.

### Quora

Top questions from search include **personal PKM tooling**, **resurfacing knowledge** in Roam/Obsidian-style tools, **LLM data storage for apps**, and **work logging for agent automation**. **Direct fetch of the top “How do you manage your personal knowledge base?” thread failed** (Quora error page); synthesis below relies on search snippets and general question framing, not full answers.

## Synthesis

### Key Themes

1. **Compilation over RAG** — Community consensus building around **maintained wiki/synthesis** instead of re-chunking raw docs every query; Karpathy’s gist as a focal artifact.  
2. **Agent + editor + notes stack** — Claude Code / Cursor / MCP as the “maintainer”; Obsidian (or similar) as the human-facing surface.  
3. **Trust and control** — Granular permissions, local models, and self-hosting recur whenever personal data volume grows.  
4. **Enterprise parallel** — Meta-style “tribal knowledge” pre-compute mirrors personal PKM goals at org scale (concise context, refresh jobs, critics).

### Notable Tools & Projects

| Area | Examples |
|------|-----------|
| HN / OSS patterns | Memoriki, Atomic, LLM-context-base, Karpathy LLM Wiki gist ecosystem |
| MCP / agents | MemPalace, Atomic MCP, “skills” that lint/update wiki |
| Products (PH) | Second Brain, Pocket LLM, iWeaver, MyMemo, Recall |
| Org-scale analogy | Meta context-file pipeline for data pipelines |

### Key Debates & Disagreements

- **RAG vs compiled wiki** — Memoriki-style projects argue compilation avoids repeated chunking; others still frame everything as “RAG” colloquially.  
- **Privacy vs convenience** — Local Ollama vs hosted models; whether policy/approval layers (e.g. greywall-like) are the right abstraction.  
- **AI-generated “context files”** — Academic result: can **hurt** on famous OSS repos; industry response (Meta): **short, opt-in, validated** context still wins on proprietary/tribal-heavy code. Analogous risk for **bloated** personal wikis may apply.  
- **Graph UX** — Atomic author: graph is cool but not yet the main value vs search/wiki/chat.

### Emerging Patterns

- **MCP-first** personal KBs connecting editors and agents.  
- **Lint / scheduled maintenance** for wikis (stale links, contradictions) as first-class ops.  
- **Multi-layer stores**: raw sources, compiled wiki, embeddings and/or graph (Memoriki).  
- **Prestige of “gist → ecosystem”** in April 2026 around LLM Wiki.

### Open Questions

- Which **personal** stacks get **durable adoption** vs short hype cycles around a single gist?  
- How do users **audit** compiled wikis for wrong merged facts at scale?  
- **Interoperability**: export, plain markdown ownership, and migration between Atomic-like apps and Obsidian vaults.  
- **Evaluation**: no single community metric for “quality” of a personal LLM KB beyond anecdotes.

## Limitations This Run

- **Reddit:** blocked at crawler level (Anthropic user-agent denied). Not included.  
- **X/Twitter:** direct fetch unavailable; coverage is indirect via search snippets and secondary articles.  
- **Time window** is approximate — search engine indexing lag may affect recency.  
- **Quora:** top thread could not be retrieved via WebFetch; answer-level detail omitted.  
- **Medium:** full text of some articles is paywalled or truncated in fetch.  
- **Product Hunt:** listing dates may not align strictly with “last 30 days.”
