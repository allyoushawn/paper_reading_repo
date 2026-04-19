# Community Survey: Multi-Agent CLI Collaboration (Claude Code + Codex + Gemini CLI)

**Date:** 2026-04-19
**Time window:** last 30 days (with some Jan–Feb 2026 sources for trajectory)
**Mode:** full (first run)
**Lens:** Evaluating concrete patterns and tools to adopt for my own
Claude+Codex+Gemini setup — emphasis on (a) how agents share state/memory/context
across separate CLI sessions, (b) which orchestration patterns are battle-tested vs.
speculative, and (c) what infrastructure (MCP servers, file conventions, daemons)
is worth the build cost.

---

## Source Snapshots

### Hacker News

Two HN searches surfaced eight high-signal threads. Top picks:

- **["Multi-agent Claude Code setup – 3 roles, Markdown coordination, Docker"](https://news.ycombinator.com/item?id=47245373)** (~46 days old). Solo SaaS founder ("yego") iterated for months and landed on a 3-agent setup (CEO / Frontend / Backend), each in its own Docker container with a strict CLAUDE.md role definition. Coordination is exclusively via plain markdown files in a shared `docs/` repo (`docs/tasks/`, `docs/messages/`, `decisions.md`, `lessons-learned.md`). Famous **"CEO Incident"**: giving an agent broad organizational authority caused it to invent 20 roles and stop coding. Manual `/go` triggers; full auto-orchestration via watchexec was attempted and rolled back because agents drowned in self-generated status reports. Strongest single source in the survey.
- **[Show HN: Stoneforge — orchestration for parallel AI coding agents](https://news.ycombinator.com/item?id=47267105)** (~44 days old). Apache 2.0. Director→Worker→Steward model; **git worktrees over containers** (conflict surface is git, not the OS); JSONL as source of truth + SQLite as disposable cache; no approval gates by default; explicit handoff notes when context window fills. Works with Claude Code, Codex, OpenCode.
- **[Show HN: Optio — orchestrate AI coding agents in K8s ticket→PR](https://news.ycombinator.com/item?id=47520220)** (~24 days old, 88 points). K8s pods per repo, agents in git worktrees, polls CI every 30s, **self-healing feedback loop**: CI failures and review comments become the agent's next prompt. MCP configurable per repo (`.mcp.json` written into worktree); Claude skills surface as `.claude/commands/{name}.md`. Sparked a sharp debate in comments about HitL planning vs. autonomous loops.
- Other notable HN tools surfaced: **Corral**, **Diraigent**, **Praktor**, **eforge**, **reflectt-node**, **ysa** — every one of them an orchestration layer; the space is actively crowded.

### Big Tech Research Blogs

- **[Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies (Google Research, "MASS")](https://research.google/pubs/multi-agent-design-optimizing-agents-with-better-prompts-and-topologies/)**. Finding: simpler design spaces dominate; *prompts* matter more than agent count or topology complexity. Useful counter to the "more agents = better" instinct.
- **[Multi-Agent System for Cognitive Work Automation (Google Research, "Adversarial Review Panel")](https://research.google/pubs/multi-agent-system-for-cognitive-work-automation-using-an-adversarial-review-panel/)**. Designs distinct agent personas to critique each other from varied perspectives — supports the "adversarial collaboration" pattern.

### Big Tech Engineering Blogs

- **[Capacity Efficiency at Meta — Unified AI Agents](https://engineering.fb.com/2026/04/16/developer-tools/capacity-efficiency-at-meta-how-unified-ai-agents-optimize-performance-at-hyperscale/)** (April 16, 2026 — 3 days old). Meta separates **MCP Tools** (standardized interfaces — query profiling, fetch experiments, search code) from **Skills** (encoded domain reasoning patterns). Same tools power both "defense" (FBDetect catches regressions → AI Regression Solver auto-PRs a fix) and "offense" (turning conceptual perf opportunities into deployed PRs). Recovered hundreds of MW of power; collapsed ~10h investigations to ~30 min. Strong validation of the **MCP-as-shared-substrate** thesis.
- **[Ranking Engineer Agent (REA), KernelEvolve, Tribal Knowledge Mapping](https://engineering.fb.com/)** — Meta has a portfolio of long-running multi-agent systems. REA uses a **"Hibernate-and-Wake Mechanism"** for multi-week operation; Tribal Knowledge deploys 50+ specialized agents to index a 4,100-file codebase, reducing other agents' tool calls by 40%.
- **["Death of Traditional Testing" (Meta, Feb 11)](https://engineering.fb.com/2026/02/11/developer-tools/the-death-of-traditional-testing-agentic-development-jit-testing-revival/)**. Just-in-Time Tests generated per code change — addresses the fact that agentic dev breaks the assumptions of traditional CI test maintenance.

### ML/AI Specialized Blogs

- **[2026 Agentic Coding Trends — Implementation Guide (Hugging Face / Svngoku, Feb 9)](https://huggingface.co/blog/Svngoku/agentic-coding-trends-2026)**. Distillation of Anthropic's 2026 trends report into concrete architecture: orchestrator + agent runtime + context layer + verification layer + delivery layer + observability. Coordination patterns enumerated: **hierarchical (recommended default), router+specialists, blackboard, debate/consensus**. Risk-based escalation policy with explicit "ask-for-help" triggers. The reference architecture template that everyone else implicitly riffs on.
- **[Slipstream — Solving the Coordination Crisis (Hugging Face / Anthony Maio, Jan 5)](https://huggingface.co/blog/anthonym21/slipstream-for-agent-communication)**. Identifies the **"tokenizer tax"**: BPE tokenizers fragment JSON syntax (`REQ/TSK` becomes 3+ tokens, not 1), so dense custom message formats *increase* token cost. Counter-intuitive solution: communicate in natural English mnemonics (`RequestReview`) mapped to a shared dictionary (Universal Concept Reference, 4-D: Action/Polarity/Domain/Urgency). Claims 82% token reduction. Multi-agent coordination wastes 40–60% of compute budget today.
- **["I Accidentally Rebuilt OpenHands From Scratch" (HF / Charles Azam, Jan 2)](https://huggingface.co/blog/charles-azam/rebuilt-openhands)**. Practical lessons from building a multi-tenant agent framework: **state persistence is underrated** (git as backing store works surprisingly well for small projects); **agent frameworks help you start, not finish** — when you need anything custom, the 50-line raw loop wins.

### ProductHunt

- **[Exponent](https://www.producthunt.com/products/exponent)** — branded as "the most collaborative AI coding agent"; debugging Docker, SQL, incident response.
- **[crewAI](https://www.producthunt.com/p/replit/crewai)** — multi-agent interaction platform.
- **[Agno](https://www.producthunt.com/p/agno/agno)** — multi-modal reasoning agents framework.
- **[ALTAR 2.0 Personal Multi-Agent Workspace](https://www.producthunt.com/p/altar-4/altar-2-0-personal-multi-agent-workspace)** — closest analogue to a personal multi-agent setup.
- **[Tila](https://www.producthunt.com/p/self-promotion/tila-the-infinite-ai-workspace-that-adapts-to-your-creative-flow)** — "infinite AI workspace" with multi-agent capabilities.

### Medium / Substack

NLM ingestion failed for the two most relevant Medium posts (Medium blocks NLM's crawler), but they were captured via WebSearch summary:

- **[Gemini CLI vs Claude Code vs Codex: Honest Benchmark Verdict (Aniruddha Kawarase, Apr 2026)](https://medium.com/@anupkawarase.akz/gemini-cli-vs-claude-code-vs-codex-i-benchmarked-all-three-heres-the-honest-verdict-a9b830313cc5)**. Single-file fix: Gemini fastest (45s); multi-file refactor: Claude dominates 10/10; codebase Q&A: Gemini wins on speed, Claude on depth.
- **[Multi-Agent Systems and Subagents — Codex/Claude/Gemini (Dreamwalker / aristojeff, Mar 2026)](https://medium.com/@aristojeff/what-are-multi-agent-systems-and-subagents-a-comparison-of-codex-claude-code-and-gemini-cli-304376584f51)**. Defines subagent as a specialized helper with its own context window, prompt, tools, permissions — the unifying concept across all three vendors as of Feb 2026.
- **[Major AI Coding Tools Comparison 2026 (Terry Cho)](https://medium.com/@terrycho/major-ai-coding-tools-comparison-2026-claude-code-codex-gemini-55f1140cd05e)**. Claude Code leads SWE-bench (80.9%) on Opus 4.6 (1M ctx); Codex = "daily driver" (60–70% of work); Gemini for planning/spec to manage cost.
- **["I Tested All Three Back-to-Back" (AI in Plain English, Apr 2026)](https://medium.com/ai-in-plain-english/i-tested-claude-code-codex-gemini-cli-and-aider-back-to-back-heres-what-i-actually-bill-with-2aec70e75846)** — practitioner write-up.

### X / Twitter (indirect)

X URLs cannot be ingested. Captured via search snippets and secondary coverage:

- **[The Three-CLI Toolkit (Daniel Vaughan, codex.danielvaughan.com, Apr 11)](https://codex.danielvaughan.com/2026/04/11/three-cli-toolkit-codex-claude-gemini/)** — *the most directly relevant single source for this lens*. Codifies the **Explore→Plan→Execute** pattern: Gemini explores (1M ctx, free tier), Claude plans (architectural reasoning), Codex executes (Rust, OS-sandboxed). Surveys bridging tools (`ccb`, `Claude-Code-Workflow`, MCP). Tiered cost strategy under £35/mo for all three. Argues `AGENTS.md` is becoming the open standard (60k+ projects, 25+ tools, AAIF/Linux Foundation governance).
- **[AgentPipe (kevinelliott)](https://github.com/kevinelliott/agentpipe)** — 114-star CLI/TUI orchestrating shared "rooms" between 9+ AI CLIs (Amp, Claude, Codex, Cursor, Gemini, Qoder, Qwen, etc.). Native thread management for Amp, structured 3-part prompts, Prometheus metrics, per-agent rate limiting. Concrete and shippable today.
- **[Claude Code Bridge (ccb)](https://github.com/bfly123/claude_code_bridge)** — split-pane terminal; one daemon per provider (`askd`, `caskd`, `gaskd`, `oaskd`); 60s auto-shutdown.
- **[Claude-Code-Workflow (catlog22)](https://github.com/catlog22/Claude-Code-Workflow)** — JSON-driven multi-CLI workflow.
- **[dev.to: Claude Code vs Codex CLI vs Gemini CLI 2026](https://dev.to/rahulxsingh/claude-code-vs-codex-cli-vs-gemini-cli-which-ai-terminal-agent-wins-in-2026-55f5)** — confirms the consolidation around three vendor-native CLIs; mentions Anthropic's **Agent Teams** (3–5 Claude instances collaborating via mailbox pattern).

### Quora

Weak signal. Top results are old Claude Dev / Gemini CLI experience threads, none directly addressing multi-CLI collaboration. Notable sentiment: one Gemini CLI user calls it "probably the worst Google product I've ever seen" (agent design issues, not the underlying model). One commenter wishes POE had pursued "mutually collaborative agents" more aggressively.

---

## Synthesis (through the lens)

### Key Themes

1. **Markdown is winning as the universal coordination substrate.** Every battle-tested practitioner setup converges on plain-text files in a shared `docs/` repo over JSON, SQLite, or custom protocols. Reasons cited: human-readable, diffs cleanly in git, no extra tooling to break, doubles as documentation. Stoneforge uses JSONL+SQLite under the hood but exposes markdown to humans. AgentPipe routes through Markdown export. Even Anthropic's reference architecture recommends markdown-first conventions (ADRs, CODEOWNERS, lessons-learned files).

2. **Tiered, role-constrained orchestration is the dominant pattern.** Director/Worker/Steward (Stoneforge), CEO/Frontend/Backend (yego), Orchestrator/Specialists (Anthropic). Common rule: **orchestrator never codes**. The "CEO Incident" is now widely cited cautionary lore — agents given vague organizational authority manufacture bureaucracy.

3. **Git worktrees > Docker containers for parallel agents on one repo.** Stoneforge made the strongest case (sub-millisecond creation, share node_modules, conflict surface is already git). Optio uses both K8s pods AND worktrees inside them. Containers still useful for hard isolation (yego, multi-tenant SaaS), but for personal multi-agent setups, worktrees win.

4. **MCP (Model Context Protocol) is the de facto interop layer for multi-CLI setups.** Cited as "the natural bridge" for Claude Code + Codex + Gemini in The Three-CLI Toolkit; configurable per-repo by Optio; foundational for Meta's hyperscale agent platform; AAIF (Linux Foundation) now governs MCP and `AGENTS.md` standardization. **Every serious multi-CLI architecture uses MCP as the bridge.**

5. **Self-healing feedback loops with CI/review as the next prompt** — Optio's defining idea. Catches the failure mode where agents submit a PR and you become the bottleneck again. Caveat from comments: agents fix the exact error message they're given but are bad at recognizing they're stuck in a loop ("after the third retry, you get increasingly creative excuses for why the test is wrong").

6. **Persistent state across sessions via handoff-note pattern.** When context window fills: agent commits, writes structured handoff notes to a known location, exits. Next agent picks up from notes + diff. Stoneforge built around this; Anthropic recommends content-addressed artifacts (hash IDs); Charles Azam ("State persistence is underrated") confirms git-backed storage works surprisingly well.

7. **The "tokenizer tax" is real but the practitioner answer differs from the protocol answer.** Slipstream solves it with a custom semantic-quantization protocol (82% reduction). Practitioners solve it by **using fewer messages and writing in plain English** — exactly Slipstream's underlying insight, applied without the protocol overhead.

### Notable Tools & Projects

**Multi-CLI bridges (most relevant to your setup):**
- **AgentPipe** — 114★ Go CLI/TUI; 9+ adapters incl. Claude/Codex/Gemini; Amp thread management; Prometheus metrics; Docker-ready.
- **Claude Code Bridge (ccb)** — split-pane terminal; lightweight daemons per provider; `.ccb/history/` per-project context.
- **Claude-Code-Workflow** — JSON-driven cadence-team workflows across all three CLIs.
- **codex-plugin-cc** — OpenAI's official Codex↔Claude Code bridge.
- **AIPass** — referenced as "persistent multi-agent collaboration across Codex, Claude, Gemini" (worth follow-up).

**Single-CLI multi-agent orchestrators:**
- **Stoneforge** — Director/Worker/Steward, git worktrees, JSONL+SQLite, Apache 2.0. Best architectural fit if you stay single-CLI.
- **Optio** — K8s + worktrees, ticket→PR, self-healing CI loops, MCP per-repo.
- **yego/claude-code-docker** — the markdown-coordination reference setup.
- **Corral / Diraigent / Praktor / eforge / reflectt-node / ysa-ai/ysa** — crowded space.
- **Anthropic Agent Teams** (Opus 4.6, Feb 2026) — official 3–5 Claude-instance peer-to-peer mailbox pattern.

**Communication protocols:**
- **MCP (Model Context Protocol)** — the cross-CLI standard.
- **AGENTS.md** — emerging open standard (AAIF) for shared agent context; 60k+ projects.
- **Slipstream** — speculative; 82% token-reduction via semantic quantization; aspires to be "TCP/IP of agents."

**Frameworks (mostly de-emphasized):**
- LangGraph, AutoGen, smolagents, Pydantic-AI — useful for prototyping; practitioners write custom 50-line loops for production.
- Omniagents — minimal alternative (~2k LOC) showing what's actually needed.
- OpenHands (66k★) — full-fat reference implementation.

### Key Debates & Disagreements

| Debate | Pro side | Con side | Underlying trade-off |
|---|---|---|---|
| Parallel vs sequential agents | Stoneforge, Optio, Anthropic (DAG/parallel default) | yego (strictly sequential frontend→backend pipeline) | Throughput vs. architectural coherence |
| Manual vs auto orchestration | Optio (CI feedback loop autopilot) | yego (`/go` manual triggers; auto = bureaucracy) | Bottleneck removal vs. control & loop prevention |
| Structured (JSON/SQLite) vs unstructured (markdown) | Stoneforge (event-sourced JSONL+SQLite); Anthropic (DAGs) | yego, most practitioners (plain markdown wins) | Queryability vs. simplicity & token cost |
| Approval gates vs no-gates | reflectt-node, Anthropic risk policy | Stoneforge default, Optio | Throughput vs. production safety |
| Single-CLI multi-instance vs multi-CLI bridging | yego, Stoneforge (3–5 Claude instances) | Vaughan's Three-CLI Toolkit, AgentPipe | Architectural simplicity vs. cost optimization + model strengths |
| File/git sync vs daemon sync | Stoneforge worktrees, yego markdown | AgentPipe (HTTP+Prometheus), ccb (per-provider daemons) | Git resilience vs. real-time observability |
| Heavy framework vs custom loop | LangChain, AutoGen, Anthropic ref arch | Charles Azam, Omniagents, 50-line loop crowd | Quick prototyping vs. long-term controllability |

### Emerging Patterns

- **Explore → Plan → Execute** (Vaughan): Gemini explores (1M context, free), Claude plans (reasoning), Codex executes (sandboxed, fast). Maps cleanly to vendor cost tiers and to your existing setup.
- **Cross-Validation**: same diff to all three CLIs; agreement = confidence, disagreement = human decision needed. Cheap insurance.
- **Hibernate-and-Wake** (Meta REA): durable agent jobs that span weeks with checkpoint+resume.
- **Tools+Skills separation** (Meta): standardized MCP Tools vs. domain-specific Skills; you already have this in your `~/.claude/skills/` setup. Validates direction.
- **Anti-DRY for agent codebases**: duplication is now seen as *less* fragile than abstraction because agents read the whole codebase instantly. Counter-intuitive but recurring.
- **Personality cards / adversarial review**: agents with distinct critical personas catch what consensus misses (Google's Adversarial Review Panel paper).

### Open Questions

- **What's the right shared-state substrate for personal multi-CLI use?** Files + git is the practitioner answer; MCP is the protocol answer. Probably both, with MCP fronting persistent shared resources and files for ephemeral coordination.
- **How do you prevent context-window-handoff degradation?** Stoneforge's commit-then-handoff-notes works for Claude-Code-only setups; unclear how cleanly it transfers to Claude→Codex or Claude→Gemini handoffs.
- **At what scale does an MCP "agent bus" daemon stop being overkill?** 1 agent = no. 3 agents = unclear. 5+ = probably yes per reflectt-node's experience.
- **Can custom protocols like Slipstream actually catch on, or does plain English plus MCP win by inertia?** Bet leans toward inertia.
- **Is Anthropic's Agent Teams (Opus 4.6 mailbox pattern) production-ready enough to skip third-party orchestrators for Claude-only setups?** Worth testing directly.

---

## Limitations This Run

- **Reddit:** crawler blocked at platform level; not included.
- **X/Twitter:** direct fetch unavailable; coverage indirect (search snippets + secondary blogs).
- **Medium:** NLM cannot ingest medium.com URLs (their bot policy); two key Medium articles have full content only in the WebSearch summary, not in the trajectory notebook.
- **Time-window approximation:** search-engine indexing lag means very recent (< 48h) posts may be missing. The Meta Capacity Efficiency post (Apr 16) was the freshest captured.
- **First run:** trajectory queries are answered from in-source date metadata only; future runs will produce stronger longitudinal signal.

---

## Trajectory (from accumulated notebook of 13 sources spanning 2026-01-02 → 2026-04-16)

### Consensus shifts over time

The dominant view evolved sharply across one quarter:

- **Jan–Feb (theory phase):** focus on building heavy frameworks (LangGraph, AutoGen, smolagents), inventing custom protocols to solve theoretical bottlenecks (Slipstream's semantic quantization), and using sandboxed isolation (E2B, Docker). Anthropic's Feb trends report codified hierarchical orchestration + DAGs as the recommended default.
- **March (pragmatic backlash):** practitioners published their lessons. Frameworks dismissed as "help you start, not finish" (Azam). "CEO Incident" goes viral. **Plain markdown over structured tools** becomes the consensus. Stoneforge replaces containers with git worktrees.
- **April (heterogeneous stacks):** the field abandons the single-master-framework dream in favor of routing tasks to vendor-specific CLIs (Vaughan's Three-CLI Toolkit, April 11). MCP + `AGENTS.md` formalize as cross-vendor standards (under AAIF/Linux Foundation governance). Meta's hyperscale post (April 16) validates the same Tools+Skills MCP pattern at the largest scale.

**Net direction:** "build complex protocols and frameworks to make swarms communicate" → "constrain agents tightly, sync them via git/markdown, and route specific tasks to the specific vendor CLIs that do them best."

### What's gone quiet

- **Slipstream / semantic-quantization protocols** (last mention: Jan 5). Practitioners adopted the underlying insight ("speak English, send fewer tokens") without the protocol overhead.
- **Heavy agent frameworks (LangChain, smolagents, Pydantic-AI, LangGraph, AutoGen)** as the recommended primary layer (last endorsed: Feb 9 in Anthropic trends report). By March/April, used only as schema converters or learning tools; production setups write the loop themselves.
- **E2B sandboxing** as a primary execution backend (last mention: Jan 2). Replaced by git worktrees + Docker + native Codex/Claude OS sandboxes (Seatbelt, Landlock).
- **Open-ended "CEO" agents and watchexec-style auto-orchestration** (last cited cautionary tale: ~Mar 4). Now uniformly warned against.

### What's newly emerging

- **The Three-CLI Toolkit pattern** (Vaughan, Apr 11) — the most explicit codification of running Claude+Codex+Gemini together with task routing.
- **Self-healing CI feedback loops** as a first-class architectural element (Optio, ~24 days old). Was implicit before; now central.
- **Meta's Tools+Skills MCP pattern at hyperscale** (Apr 16) — strong external validation that the MCP layer + reusable Skills layer scales.
- **AGENTS.md as a Linux-Foundation-governed open standard** (60k+ projects). Was just one of many CLAUDE.md/AGENTS.md/conventions in early 2026; consolidating in April.
- **Anti-DRY / duplication-friendly philosophy for agent codebases** — emerging cultural shift against a 20-year orthodoxy.
- **A wave of orchestration tools** (Stoneforge, Optio, Corral, Diraigent, Praktor, eforge, reflectt-node, ysa, AIPass) all shipping in March/April. Indicates a Cambrian explosion phase; consolidation likely in Q3.

### Persistent open questions

The same problems keep appearing across all dates:

- **Coordination overhead / "agent bureaucracy"** (Jan: Slipstream identifies 40–60% compute waste; Mar: yego's CEO Incident shows it in practice; Apr: still listed as an unresolved sync subproblem).
- **Cross-session memory / context handoff** (Jan: "state persistence is underrated"; Mar: Stoneforge's handoff-notes workaround; Apr: still a stated open subproblem).
- **Parallel execution conflict resolution** (Feb: Anthropic suggests merge strategies; Mar: Optio author admits "let them fight it out at merge"; Apr: still flagged as a sync subproblem).
- **No consensus on the best sync substrate** (Jan: git vs Slipstream; Mar: markdown vs JSONL+SQLite; Apr: MCP vs files vs daemons — all coexist).
- Best-quoted summary: **"Everyone's holding the same genie, but everyone's rubbing the lamp differently. Maybe the best approach doesn't exist yet."** (yego, March 2026)
