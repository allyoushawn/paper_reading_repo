# Community Survey: Agentic Workflow Guidelines (Anthropic / OpenAI / Google-Gemini)

**Date:** 2026-04-19
**Time window:** Last 12 months (foundational guides may pre-date the window)
**Mode:** full (first run on this topic)
**Lens:** Extract canonical, actionable design principles and patterns I can apply when building agents — emphasizing what each lab explicitly recommends (and warns against) for tool use, planning, evaluation, and safety in agentic workflows.
**Scope:** ONLY first-party Anthropic, OpenAI, and Google/Gemini/DeepMind sources. No HN, no third-party blogs, no community discourse. (Per project README scope constraint.)

---

## Source Snapshots

### Anthropic (12 sources)
- **Building Effective AI Agents** (Dec 19, 2024) — foundational architecture post; defines workflows vs agents; "find the simplest solution possible"; introduces patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, autonomous agents).
- **How we built our multi-agent research system** (Jun 13, 2025) — orchestrator-worker pattern (Lead Researcher + parallel sub-agents); 90.2% lift over single-agent on internal research eval; multi-agent uses ~15× tokens of chat; quantified guidance on scaling effort to query complexity.
- **Scaling Managed Agents: Decoupling the brain from the hands** — three-way split: brain (LLM + harness) / hands (sandboxes + tools) / session (append-only event log); session lives outside context window with `getEvents()` interface; sandbox security boundary so untrusted Claude-generated code never sees credentials.
- **Writing effective tools for AI agents — using AI agents** — tool design as ACI (agent-computer interface); namespacing (`asana_projects_search`); `search_*` over `list_*`; `response_format` enum (concise vs detailed); prompt-engineer error responses; consolidated tools (`schedule_event` vs `list_users`+`list_events`+`create_event`); 25k-token cap default.
- **Introducing advanced tool use on the Claude Developer Platform** (Nov 24, 2025) — 3 betas: Tool Search Tool (`defer_loading: true`, 85% token reduction, accuracy 49% → 74% Opus 4), Programmatic Tool Calling (37% token reduction), Tool Use Examples (72% → 90% accuracy on complex parameter handling).
- **Demystifying evals for AI agents** (Jan 09, 2026) — 8-step eval methodology; start with 20–50 tasks; capability vs regression evals; `pass@k` vs `pass^k` for non-determinism; LLM-as-judge calibration; eval saturation problem.
- **Introducing Agent Skills** + **Skill authoring best practices** + **Agent Skills overview** (Oct 2025+) — filesystem-based skills with 3-level progressive disclosure (metadata always loaded, SKILL.md on trigger, supporting files on demand); "concise is key"; degrees-of-freedom matching; "scripts solve, don't punt".
- **Best Practices for Claude Code** — context as primary resource; planning before implementation; subagents for investigation; `/clear` between unrelated tasks; CLAUDE.md kept lean; common failure patterns named (kitchen sink session, infinite exploration, trust-then-verify gap).
- **Using CLAUDE.md files** — concise project-level config (150–200 lines target); only include things Claude can't figure out; convert recurring corrections into hooks.
- **Building agents with the Claude Agent SDK** (Sep 29, 2025) — renamed from Claude Code SDK; "give your agents a computer"; `gather context → take action → verify work → repeat` loop; subagents for parallelism + context isolation; MCP for out-of-the-box integrations.

### OpenAI (11 sources, 6 ingested as text after Cloudflare blocked URL fetch)
- **A practical guide to building agents** (PDF guide) — definition (LLM-driven workflow execution + tools + dynamically selected within guardrails); when to build (complex decisions / unmaintainable rulesets / unstructured data); 3 components (Model + Tools + Instructions); 3 tool types (Data / Action / Orchestration); single-then-multi orchestration; manager pattern + decentralized handoffs; layered guardrails.
- **New tools for building agents** (Mar 11, 2025) — Responses API debut + built-in tools (web search, file search, computer use) + Agents SDK (successor to Swarm) + integrated observability/tracing.
- **New tools and features in the Responses API** (May 21, 2025) — remote MCP server support; image generation tool; Code Interpreter; background mode for async long tasks; reasoning summaries; encrypted reasoning items (ZDR).
- **Why we built the Responses API** (Sep 22, 2025) — historical narrative: Completions → Chat Completions → Assistants (failed) → Responses; Responses framed as "structured loop for reasoning and acting"; preserves reasoning state across turns (TAUBench +5%).
- **Equipping the Responses API with a computer environment** (Mar 11, 2026) — shell tool (Unix utilities, GPT-5.2+ trained for shell); container context (file system, SQLite, sidecar egress proxy with domain-scoped secret injection); native server-side compaction; agent skills as folder bundles.
- **Better performance from reasoning models using the Responses API** (May 11, 2025) — encrypted reasoning items persist across turns via `previous_response_id`; reasoning tokens previously discarded between turns now retained.
- **Agents SDK guide** (platform.openai.com) — when to use SDK vs Agent Builder vs raw client libs; reading order (quickstart → agent definitions → running agents → orchestration → guardrails → results+state); voice agents are SDK-only.
- **Agent Builder guide** — visual canvas; 3-step process (design → publish → deploy); ChatKit for embedding; trace graders for in-canvas evaluation.
- **Running agents** — agent loop definition (call model → inspect output → execute tool calls → handoff or final answer); 4 conversation strategies (replay, session, conversationId, previous_response_id); approvals as **paused runs, not new turns**.
- **Orchestrating Agents: Routines and Handoffs** (Oct 2024 cookbook) — original "routines" + handoff concept; pre-Agents-SDK Swarm proof-of-concept.
- **Agents (Developers learn track)** — definition, distinguishes agents from chatbots.

### Google / Gemini / DeepMind (10 sources)
- **Agents Overview (Gemini API)** — agent definition (Gemini + tools + reasoning); `thinking_level` for reasoning depth control; instructions should explicitly enforce persistence, risk assessment, proactive planning (~5% benchmark lift); Deep Research Agent as pre-built example.
- **Choose a design pattern for your agentic AI system** (Cloud Architecture Center, Oct 8, 2025) — comprehensive taxonomy: single-agent / sequential / parallel / loop / coordinator / hierarchical task decomposition / swarm / human-in-the-loop / iterative refinement; cost vs flexibility trade-offs per pattern; explicit warnings about infinite loops in loop and swarm patterns.
- **Building AI Agents with Gemini 3 and Open Source Frameworks** (Nov 19, 2025) — Gemini 3 features: `thinking_level`, **Thought Signatures** (encrypted reasoning state passed back to maintain train of thought), `media_resolution` for multimodal token control, large context for "reasoning drift" mitigation.
- **Build Your First ADK Agent Workforce** — three core patterns (build autonomous agents / empower with tools / orchestrate multi-agent).
- **Overview of Agent Development Kit** (Vertex AI Agent Builder) — multi-language ADK (Python/Java/Go/TS); Workflow Agents; Session management; A2A; HITL via ToolConfirmation; deploy to Vertex AI Agent Engine Runtime.
- **Develop an ADK agent** (Vertex AI Agent Builder docs) — function definition guidance (clear comments describing params/return); Memory Bank + `PreloadMemoryTool`; ADK App architecture.
- **Announcing ADK for Java 1.0.0** (Mar 30, 2026) — App + Plugin architecture (LoggingPlugin, ContextFilterPlugin, GlobalInstructionPlugin); event compaction with sliding window + summarizer; ToolConfirmation for HITL; native A2A protocol; new tools (GoogleMapsTool, UrlContextTool, ContainerCodeExecutor, VertexAiCodeExecutor).
- **Multi-agent AI system in Google Cloud** — coordinator agent + A2A protocol + MCP for tools + MCP Toolbox for Databases (centralized tool management without redeploying agents); Model Armor for prompt-injection / sensitive-data inspection; deployment options (Cloud Run / GKE / Vertex AI Agent Engine).
- **Updating the Frontier Safety Framework** (DeepMind) — three components: Critical Capability Levels (CCLs), early-warning evaluations, mitigation plans; tiered security; deceptive-alignment risk explicitly addressed; heightened security for ML R&D capabilities.
- **Taking a responsible path to AGI** (DeepMind) — four risk categories: misuse, misalignment, accidents, structural; proactive planning + collective-action framing.

---

## Synthesis (through the canonical-design-principles lens)

### Key Themes

**1. Three-component agent definition is now universal — but emphasis differs.**
All three labs converge on a "brain + hands + something else" definition.
- **OpenAI:** Model + **Tools** + **Instructions/guardrails** (instructions and guardrails are the third component).
- **Anthropic:** brain (LLM + harness) + hands (sandboxes + tools) + **session** (append-only event log decoupled from context window).
- **Google:** Gemini model (brain) + tools (hands) + **orchestration framework / system prompt** (memory, plan loops, tool chaining).

The third-component divergence is meaningful: OpenAI prioritizes *behavioral control surfaces*, Anthropic prioritizes *durable state outside the context window*, Google prioritizes *the orchestration runtime itself*.

**2. "Start simple, escalate only when needed" is now consensus.**
All three labs agree that the default should be the simplest solution that works:
- Anthropic (Dec 2024): "find the simplest solution possible, only increase complexity when needed".
- OpenAI: "Maximize single agent first" — split only on complex logic or tool overload.
- Google: "If your workload is predictable / executable in a single call, non-agentic solutions are more cost-effective".

**3. Multi-agent orchestration is justified by *parallelism* and *context isolation*, not raw capability.**
- Anthropic measured 90.2% improvement on research evals from multi-agent setup, but at ~15× token cost. Token usage explained 80% of variance — multi-agent works because it lets you spend more tokens.
- OpenAI's two named patterns: **manager** (agents-as-tools, central control) and **decentralized** (handoffs, peer transfer of control + state).
- Google's much wider taxonomy: sequential, parallel, loop, coordinator, hierarchical decomposition, swarm, iterative refinement, HITL.

**4. Context engineering is the central operational problem.**
Every provider treats the context window as the most critical scarce resource:
- Lazy/progressive loading of skills (Anthropic 3-level disclosure; OpenAI container-loaded skills).
- Deferred tool loading (Anthropic Tool Search Tool: 85% token savings + accuracy 49%→74%).
- Sub-agent context isolation as compression (Anthropic, Google).
- Compaction (OpenAI native server-side compaction items; Google ADK event compaction with summarizer; Anthropic `/compact` and memory tool).
- Decoupling durable state from context window (Anthropic session log; Google ADK Session/Memory services with `LoadMemoryTool`/`PreloadMemoryTool`; OpenAI conversationId/previous_response_id).

**5. The agent loop has matured from client-side `while` to stateful, reasoning-aware, pause-able.**
- Old (Oct 2024 OpenAI Cookbook): client-side loop appending tool results until no more tool calls.
- New: server-managed, reasoning-state-preserving loop. OpenAI Responses API persists encrypted reasoning items across turns (TAUBench +5%); Google Gemini 3 ships **Thought Signatures** for the same purpose.
- Approvals/HITL must **pause** the loop, not start a new turn (OpenAI Running Agents; Google ADK ToolConfirmation auto-injects confirmation into next request).

### Notable Tools, Frameworks & Primitives

| Provider | SDK / Framework | Visual Builder | Key 2026 Primitives |
|---|---|---|---|
| Anthropic | Claude Agent SDK (renamed from Claude Code SDK, Sep 2025) | — | Agent Skills, Tool Search Tool, Programmatic Tool Calling, Tool Use Examples, Managed Agents (decoupled session/sandbox) |
| OpenAI | Agents SDK (Python/TS) — successor to Swarm | Agent Builder + ChatKit | Responses API, shell tool, hosted containers w/ sidecar egress, native compaction items, agent skills, remote MCP |
| Google | Agent Development Kit (Python/Java/Go/TS) v1.0 | — | A2A protocol, Memory Bank + PreloadMemoryTool, ToolConfirmation, App + Plugin architecture, Model Armor, Workflow Agents (sequential/parallel/loop) |

**Common protocol layer:** All three support **MCP** (OpenAI joined MCP steering committee; Google uses MCP Toolbox for Databases; Anthropic ships first-class MCP support including Tool Search Tool optimized for MCP server overflow).

**Common interop layer (emerging):** Google's **Agent2Agent (A2A)** protocol — local agents can wrap remote agents (in any framework) as `RemoteA2AAgent`; mentioned as cross-framework standard in Google Cloud's multi-agent architecture docs.

### Key Debates & Disagreements

**1. Workflow vs Agent: strict Anthropic line vs Google's expansive umbrella.**
- Anthropic draws a *strict* architectural distinction: workflows have predefined code paths; agents are LLM-directed. By that definition, Google's *sequential* and *parallel* patterns (which use predefined logic, no LLM consulted for orchestration) are workflows, not agents.
- Google's Cloud Architecture Center happily includes both under "agentic design patterns" — a more inclusive taxonomy.

**2. When to go multi-agent: cost-driven vs capability-driven.**
- OpenAI: only when *single-agent prompts/tools become unmaintainable* (complex branches, tool overlap).
- Anthropic: when you need to **scale token spend** beyond what one context window can hold — explicit acknowledgment that multi-agent is fundamentally a token-spending mechanism for parallelizable tasks.
- Google: proactively for **debate / synthesis / specialization** (swarm pattern for ambiguous problems benefiting from iterative refinement among experts).

**3. Code-first vs declarative orchestration.**
- OpenAI: explicitly code-first; calls out declarative graph frameworks (LangGraph-style) as cumbersome, requiring you to "pre-define every branch".
- Google: declarative *Workflow Agents* (sequential, parallel, loop) are a first-class pattern, presented alongside coordinator/swarm patterns.
- Anthropic: code-first by design (build patterns in a few lines of LLM API calls rather than adopting frameworks).

**4. How heavyweight should "skills" be?**
- Anthropic and OpenAI converge on filesystem-based skills with progressive disclosure (metadata at startup, content on trigger). Both call the file `SKILL.md`.
- Anthropic adds explicit authoring guidance: "scripts should solve, not punt" + "consistent terminology" + "match degrees of freedom to task fragility".
- OpenAI's skills concept is much newer (Mar 2026 source) and lighter on authoring guidance; instead emphasizes the runtime mechanics (container fetch → unpack → context update with metadata + path).

### Emerging Patterns (cross-lab convergence in 2025–2026)

1. **"Agent-Computer Interface" thinking.** Tools must be designed for token-bound agents, not for software callers. Search-not-list, response-format toggles, prompt-engineered error messages, namespacing.
2. **Reasoning state preservation across turns.** OpenAI encrypted reasoning items + Google Thought Signatures are functionally identical — both encode chain-of-thought into opaque tokens that survive multi-turn execution.
3. **Decoupled sandboxed execution environments.** Anthropic's brain/hands/session split, OpenAI's hosted containers + shell tool, Google's ContainerCodeExecutor / VertexAiCodeExecutor — all converge on "the model proposes; an isolated runtime executes; only synthesized results return to context".
4. **HITL as a pause primitive (not a re-prompt).** OpenAI: "treat approvals as paused runs, not new turns." Google ADK: ToolConfirmation auto-injects confirmation into next request context. Both treat approval as continuation rather than restart.
5. **Lazy loading everything.** Skills (3-level progressive disclosure), tools (defer_loading + Tool Search Tool), instructions (CLAUDE.md keep-it-lean), memories (PreloadMemoryTool turn-by-turn retrieval).
6. **Risk-rated tools + tiered security.** OpenAI's tool safeguards (low/med/high based on read/write, reversibility, perms, financial impact) parallels DeepMind's tiered Frontier Safety Framework.

### Open Questions (problems consistently flagged across sources, time periods, and labs)

1. **Long-horizon context: every compaction is a lossy decision.** Anthropic explicitly: "irreversible decisions to selectively retain or discard context can lead to failures. It is difficult to know which tokens the future turns will need." Even with native compaction (OpenAI) and event summarizers (Google ADK), the fundamental "what to keep" problem is unsolved.
2. **Eval saturation.** As frontier models near 80%+ on existing benchmarks (SWE-Bench Verified), capability lifts become invisible. Anthropic flags this explicitly; the response so far is custom agentic eval frameworks per team.
3. **Non-determinism in evaluation.** `pass@k` (any-success) and `pass^k` (all-success) tell opposite stories at k=10. There's no clean way to summarize agent reliability for non-coding, customer-facing tasks where consistency matters.
4. **Multi-agent coordination overhead.** Anthropic: synchronous execution bottlenecks the system; asynchronous adds coordination/state-consistency/error-propagation problems. Direct subagent → filesystem outputs help but don't solve the "game of telephone" loss through a coordinator.
5. **Infinite loop / runaway execution risk.** Google explicitly warns about loop and swarm patterns lacking robust exit conditions. Anthropic's "infinite exploration" failure mode in Claude Code. No standard solution beyond explicit max-iteration caps and prompt heuristics.
6. **Deceptive alignment.** DeepMind raises this as an unresolved frontier risk specific to autonomous, long-horizon agents. Other providers don't address it directly in agent-building guides; the field's response is automated monitoring of instrumental reasoning.

---

## Limitations This Run

- **Scope is intentionally narrow.** Only first-party Anthropic, OpenAI, Google/DeepMind sources. Excludes the practitioner discourse (HN, Medium, Substack, X) that the standard `community-survey` would surface, and excludes third-party engineering blogs (Meta, Netflix, Uber, etc.) — by user's explicit constraint.
- **Cloudflare blocked 6 OpenAI URLs** during NLM ingestion (`platform.openai.com/docs/guides/agents`, `agent-builder`, several `openai.com/index/...` posts). These were rescued via direct WebFetch and ingested as text sources, with original URLs preserved in source headers. Some inline navigation/footer chrome may still appear in NLM excerpts but content is intact.
- **Time window approximation.** The user-selected 12-month window is approximate; the canonical Anthropic "Building Effective AI Agents" post (Dec 19, 2024) sits just outside the strict window but is the universally cited foundation, so it was retained.
- **No DeepMind agent-specific guide.** DeepMind's agent-relevant content is mostly safety-framework-focused (Frontier Safety Framework, AGI risk taxonomy). The lab does not publish a "build agents like this" guide of the same shape as Anthropic/OpenAI/Google Cloud.
- **No coverage of Google Vertex AI Agent Garden / pre-built agent marketplace** — the survey focused on design-principle docs rather than agent catalogs.

---

## Trajectory (from accumulated notebook of 40 sources spanning Dec 2024 → Apr 2026)

*Note: this is the first run, so trajectory is derived purely from the dated sources ingested today, not from prior survey snapshots. Subsequent runs will accumulate true longitudinal signal.*

### Consensus shifts over time

**(a) Single vs Multi-agent:**
- **Late 2024:** Anthropic strongly favored simplicity ("Building Effective AI Agents", Dec 19, 2024). OpenAI's Swarm was an experimental proof-of-concept ("Orchestrating Agents", Oct 10, 2024).
- **Mid-2025:** Anthropic's "How we built our multi-agent research system" (Jun 13, 2025) declared "once intelligence reaches a threshold, multi-agent systems become a vital way to scale performance" — 90.2% lift on internal research evals. Google's design-pattern doc (Oct 8, 2025) published a wide multi-agent taxonomy.
- **2026 consensus:** "Start single, split for complexity." All three labs converged on this. Google's ADK 1.0 (Mar 30, 2026) added the A2A protocol for cross-framework agent collaboration as the new ecosystem-level enabler.

**(b) Tool/Skill loading:**
- **Early 2025:** all tools loaded upfront in system prompt.
- **Late 2025 / early 2026:** mass shift to lazy / on-demand loading. Anthropic Tool Search Tool (Nov 24, 2025) reports 85% context savings. Anthropic Agent Skills (Oct 2025) introduced 3-level progressive disclosure. OpenAI adopted the same skill concept in March 2026 (Equipping Responses API).

**(c) Agent loop:**
- **Late 2024:** simple client-side `while` loop.
- **Mid-late 2025:** stateful, reasoning-aware loops. OpenAI Responses API (Sep 22, 2025) preserves encrypted reasoning items; Google Gemini 3 (Nov 19, 2025) ships Thought Signatures for the same.
- **Late 2025 → 2026:** loops are decoupled (Anthropic brain/hands/session) and pausable for HITL (OpenAI "approvals as paused runs", Google ADK ToolConfirmation).

### What's gone quiet

- **Swarm (OpenAI)** — last mentioned Mar 11, 2025 as the experimental predecessor to the Agents SDK. Officially retired.
- **Assistants API (OpenAI)** — slated for mid-2026 deprecation; "never achieved mass adoption". Superseded entirely by Responses API.
- **Completions API / `/v1/completions`** — referenced only as historical milestone in the Sep 2025 Why-We-Built-Responses post.
- **Claude Code SDK (Anthropic)** — renamed to **Claude Agent SDK** (Sep 29, 2025). The "Claude Code" name persists for the CLI product, but the underlying SDK is no longer scoped to coding.
- **Strands Agents SDK, Rivet, Vellum** — third-party frameworks mentioned in Anthropic's Dec 2024 guide; absent from all later Anthropic publications. Anthropic's stance: "start with LLM APIs directly".

### What's newly emerging (2026 only)

- **OpenAI shell tool** (Mar 2026) — generalizes beyond Python-only Code Interpreter.
- **OpenAI native server-side compaction items** (Mar 2026) — encrypted, automatic, configurable threshold.
- **OpenAI sidecar egress proxy + domain-scoped secret injection** (Mar 2026) — model never sees raw credentials.
- **Google ADK App + Plugin architecture** (Mar 2026) — global plugins (LoggingPlugin, ContextFilterPlugin, GlobalInstructionPlugin) applied across agent hierarchies.
- **Google A2A protocol** (Mar 2026) — `RemoteA2AAgent` / `AgentCard` for cross-framework agent interop.
- **Google ToolConfirmation HITL primitive** (Mar 2026) — formal pause/resume contract.
- **Google Memory Bank + PreloadMemoryTool** (Apr 2026) — Vertex AI Agent Engine Memory Bank with explicit retrieval tooling.
- **Google new grounding tools** — GoogleMapsTool, UrlContextTool (Mar 2026).
- **Anthropic eval saturation framing** (Jan 2026) — naming the problem of >80% benchmark scores hiding capability lifts.
- **Anthropic `pass@k` vs `pass^k` heuristic** (Jan 2026) — formalizing the non-determinism trade-off.
- **Anthropic 1M-context Claude Code sessions + parallel desktop agents + routines in Claude Code** (Apr 2026, sidebar references) — not deeply analyzed in this run; flagged for next survey.

### Persistent open questions (cross-source, cross-time)

- **Long-horizon context management:** every compaction is a lossy decision; we still lack a way to know which tokens future turns will need (Anthropic Managed Agents post explicitly).
- **Evaluating non-deterministic agents:** `pass@k` vs `pass^k` is the current best heuristic, but no clean single metric exists.
- **Eval saturation:** how to measure incremental capability when all baseline benchmarks are >80%.
- **Runaway execution / infinite loops:** explicit warnings in Google's loop and swarm patterns; Anthropic's "infinite exploration" Claude Code failure mode. No standard solution.
- **Multi-agent coordination at scale:** sync vs async, "game of telephone" through coordinators, error propagation (Anthropic multi-agent research-system post).
- **Deceptive alignment:** DeepMind explicitly flags as unresolved for highly autonomous systems; no agent-builder-level guidance yet.

### User-defined trajectory query

*Not provided this run.*

---

## Quick-Reference: Quantitative Results from Sources

| Result | Source |
|---|---|
| Multi-agent (Opus 4 lead + Sonnet 4 subs) **+90.2%** vs single-agent on internal research eval | Anthropic, How we built multi-agent research system |
| Multi-agent uses **~15× tokens** of chat | Anthropic, ibid. |
| Token usage explains **80% of perf variance** on BrowseComp | Anthropic, ibid. |
| Tool Search Tool: **85% token reduction**, accuracy **49% → 74%** (Opus 4) on MCP eval | Anthropic, advanced tool use |
| Programmatic Tool Calling: **37% token reduction** on complex tasks | Anthropic, ibid. |
| Tool Use Examples: parameter accuracy **72% → 90%** | Anthropic, ibid. |
| Allowing agent to rewrite tool descriptions: **40% reduction** in task completion time | Anthropic, multi-agent research system |
| Parallel tool calling: **up to 90%** time reduction on complex queries | Anthropic, ibid. |
| Concise tool response uses **~⅓ tokens** of detailed | Anthropic, writing effective tools |
| Responses API + reasoning items: **+5%** TAUBench | OpenAI, Why we built Responses API |
| Computer use (CUA): OSWorld **38.1%**, WebArena **58.1%**, WebVoyager **87%** | OpenAI, New tools for building agents |
| Web search (GPT-4o): SimpleQA **90%** | OpenAI, ibid. |
| Gemini 3 explicit reasoning instructions: **~5% lift** on agentic benchmarks | Google, Agents Overview |

---

## NotebookLM Notebook

- **ID:** `23a9e735-8ad9-4d86-af53-5a1bb353e537`
- **URL:** https://notebooklm.google.com/notebook/23a9e735-8ad9-4d86-af53-5a1bb353e537
- **Sources:** 40 (33 URL + 7 text including README and 6 OpenAI rescued)
- **Conversation ID for follow-up:** `91161892-e254-490e-8c1e-baa11e59023e`
