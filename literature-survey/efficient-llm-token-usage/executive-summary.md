Date: 2026-04-12

# Efficient LLM Token Usage for Agentic Workflows - Executive Summary

## Key Questions
- How can we minimize token waste in agentic Claude workflows?
- What are the highest-ROI token optimization techniques?
- How should prompt caching, model routing, and context management be combined?
- What is the optimal implementation order for a personal agentic system?

## Main Findings
Based on analysis of 10 articles from Anthropic docs, DEV Community, Decode Claude, and Zylos Research:

1. **Agentic workflows are 3–10x more expensive than simple chat completions** due to multi-turn context accumulation, tool call overhead, quadratic context growth, and the output token premium (3–8x input cost). A single complex agent task can cost $5–8 in API fees without optimization. (Source: Agent-Cost-Optimization-Token-Economics)

2. **Three dominant strategies compose to deliver 60–80% total cost reduction:** provider-level prompt caching (~90% on static tokens), model routing/cascading (up to 87% by matching task to model), and context compaction/pruning (~40% per-turn savings). These target different cost drivers and work without conflict. (Sources: Claude-API-Cost-Optimization, Agent-Cost-Optimization-Token-Economics, Manage-Tool-Context)

3. **The effort parameter is the single most powerful new lever for output token control.** Setting `effort: medium` (instead of the `high` default) for orchestration and `effort: low` for subagents reduces tool calls, thinking depth, and response verbosity — all at the output token premium that costs 3–8x input prices. (Sources: Effort-Parameter-Adaptive-Thinking, Token-Efficient-Tool-Use-Migration)

4. **Subagent delegation is a cost architecture, not just a parallelism tool.** Child agents in isolated contexts prevent parent bloat, can be routed to cheaper models, use low effort, and report back via 1–2 sentence delta summarization. (Sources: Compaction-System-Deep-Dive, Agents-Dont-Need-Sonnet)

5. **Context curation matters more than context capacity.** Even with 1M-token windows, "context rot" degrades accuracy as token count grows. Aggressive pruning, microcompaction, and tool search produce better results than filling the window. (Sources: Context-Windows-Guide, Manage-Tool-Context)

## Most Impactful Techniques (based on technique tracker)

| Rank | Technique | Composite Score | Key Benefit |
|------|-----------|----------------|-------------|
| 1 | Prompt Caching (Provider-Level) | 31 | Up to 90% input cost reduction; automatic prefix matching makes it trivial to adopt |
| 2 | Effort Parameter (Adaptive Thinking) | 28 | Single parameter controls all token spend — text, tools, thinking; `low` for subagents |
| 3 | Token-Efficient Tool Use | 26 | Up to 70% output reduction on tool calls; built-in for Claude 4+ (zero-effort) |
| 4 | Model Routing (Task-Based) | 26 | 60–87% savings by matching model to task; Haiku 12x cheaper than Sonnet |
| 5 | Context Editing / Tool Result Clearing | 25 | Prevents quadratic context growth; extends session lifetime |

## Technique Comparison

| Technique | Savings | Implementation Effort | Best For | Source |
|-----------|---------|----------------------|----------|--------|
| Prompt Caching | Up to 90% input cost | Low (add `cache_control` field) | Static system prompts, tool definitions | Prompt-Caching-With-Claude |
| Effort Parameter | Significant output reduction | Low (set `effort` param) | All API calls; differentiate orchestrator vs subagent | Effort-Parameter-Adaptive-Thinking |
| Token-Efficient Tool Use | Up to 70% output tokens | Zero (built-in Claude 4+) | Every tool call in every workflow | Token-Saving-API-Updates |
| Model Routing | 60–87% total cost | Medium (routing logic + validation) | Subagent delegation, mechanical tasks | Agents-Dont-Need-Sonnet |
| Context Pruning | ~40% per-turn input | Medium (summarization logic) | Multi-turn sessions > 12 messages | Claude-API-Cost-Optimization |
| Server-Side Compaction | Extends session indefinitely | Low (beta flag) | Long coding sessions approaching limits | Context-Windows-Guide |
| Text Editor Tool | Massive output reduction | Low (provide tool in request) | File editing in coding assistants | Token-Saving-API-Updates |
| Circuit Breakers | Prevents unbounded spend | Low (add iteration caps) | Every agent loop | Agent-Cost-Optimization-Token-Economics |
| Tool Search | Large context reduction | Medium (replace tool schemas) | Systems with 20+ tools | Manage-Tool-Context |
| Delta Summarization | Preserves parent budget | Low (instruct subagents) | All subagent delegations | Compaction-System-Deep-Dive |

## Recommendations for Agentic Workflow Optimization

Given the `~/.claude/` agentic system with skills, agents, rules, subagent delegation (via Task tool), and multi-turn sessions, the optimal implementation sequence proceeds in four phases ordered by ROI-to-effort ratio.

**Phase 1 — API-Level Quick Wins (implement immediately).** Enable prompt caching on all API calls by adding `cache_control` to request bodies. Since the system loads the same CLAUDE.md rules, skill schemas, and tool definitions on every invocation, these static prefixes are ideal caching candidates — 90% cost reduction on cached tokens with a 25% write markup that pays back on the second request (Prompt-Caching-With-Claude, Manage-Tool-Context). Simultaneously, set `effort: medium` as the default for Sonnet 4.6 orchestration and `effort: low` for all subagent delegations (reading-agent, explore, shell subagents). Anthropic's documentation explicitly recommends low effort for "simpler tasks that need the best speed and lowest costs, such as subagents" (Effort-Parameter-Adaptive-Thinking). Add circuit breakers — max iteration caps and per-trace token budgets — to every agent loop to prevent stuck reasoning loops from generating uncapped costs (Agent-Cost-Optimization-Token-Economics). These changes require no architectural work, only parameter additions to existing API calls.

**Phase 2 — Model Routing (implement within 1 month).** The current system delegates to `fast` and default model tiers via the Task tool. Formalize this into a 3-tier routing strategy: keep Sonnet/Opus for orchestration and complex reasoning (planning, debugging, security review), route reading-agent, explore, and mechanical subagents to Haiku ($0.25/M input vs $3/M for Sonnet — a 12x reduction), and consider local Ollama for high-frequency zero-reasoning tasks like commit message generation (Agents-Dont-Need-Sonnet). Add quality gates to validate cheaper model outputs before they flow back to the parent agent. Each skill in `~/.claude/skills/` should declare its minimum-viable model in metadata for deterministic routing (Agents-Dont-Need-Sonnet). Use 1-hour cache TTL for parent agent contexts when spawning subagents that may take longer than 5 minutes (Prompt-Caching-With-Claude).

**Phase 3 — Context Management (implement within 2–3 months).** Build context editing into multi-turn sessions: after a tool result has been used, remove stale tool_result blocks from conversation history (Manage-Tool-Context). Implement microcompaction for bulky tool outputs — keep a "hot tail" of recent results visible while offloading older ones to disk with reference paths (Compaction-System-Deep-Dive). Instruct all subagents to return delta summarizations (1–2 sentence incremental updates) rather than full state snapshots, preserving the parent's token budget (Compaction-System-Deep-Dive). Once the toolset grows past 20 tools, switch from loading all tool schemas upfront to a single `tool_search` tool for on-demand discovery (Manage-Tool-Context). Enable server-side compaction (beta) for long-running sessions (Context-Windows-Guide).

**Phase 4 — Observability and Governance (ongoing).** Deploy cost-per-trace logging to identify which skills, agents, and workflows consume the most tokens. Track cache hit rates to validate caching ROI. Monitor output token ratios to catch verbose reasoning runaway. Set spend anomaly alerts at >2σ from baseline (Agent-Cost-Optimization-Token-Economics). This data feeds back into routing decisions and effort tuning.

Frame around specific optimization layers:
1. **Prompt caching strategy for skill/tool definitions:** Cache the `~/.claude/CLAUDE.md` rules, skill schemas, and tool definitions at the top of every request. Use automatic caching for multi-turn sessions and explicit breakpoints for stable tool blocks. Apply 1-hour TTL for long subagent chains.
2. **Model routing (when to use Haiku vs Sonnet vs Opus):** Sonnet for orchestration and complex reasoning; Haiku for reading-agent, explore subagents, test runners, docs generation, git operations; local Ollama for commit messages and log summaries. Validate with quality gates; escalate on failure.
3. **Context window management (compaction, pruning):** Microcompact bulky tool outputs (Read, Bash, Grep). Prune stale tool results after use. Use structured summarization at task boundaries. Enable server-side compaction as safety net.
4. **Tool use optimization (token-efficient tools, tool search):** Built-in for Claude 4+ (no action needed). Switch to tool_search once toolset exceeds 20 tools. Use programmatic tool calling for repetitive sequences.
5. **Thinking/effort parameter tuning:** Default to `medium` effort on Sonnet 4.6. Use `low` for all subagent calls. Reserve `high`/`max` only for deep reasoning tasks (architecture planning, security review). Combine with `thinking: {type: "adaptive"}`.

## Next Steps
- [ ] Audit current `~/.claude/` API calls — identify which requests lack `cache_control` and explicit `effort` parameters
- [ ] Add `effort: low` to all subagent delegation calls (reading-agent, explore, shell, fast-model tasks)
- [ ] Implement model routing: map each skill in `~/.claude/skills/` to minimum-viable model tier (Sonnet/Haiku/local)
- [ ] Add circuit breakers (max_iterations, token_budget) to every agent loop
- [ ] Build cost-per-trace logging to track token usage per skill/agent/workflow
- [ ] Implement context editing — prune stale tool_result blocks from multi-turn sessions
- [ ] Evaluate microcompaction for bulky tool outputs (file reads, bash results, grep)
- [ ] Test local Ollama routing for commit message generation
- [ ] Deploy 1-hour cache TTL for parent contexts during long subagent chains

## Search Scope
- Survey period: 2023–2026
- Total articles: 10
- Sources: Anthropic official docs/blog (6), DEV Community (2), Decode Claude (1), Zylos Research (1)
- Focus: Tech blogs and engineering documentation only
- Techniques catalogued: 34 distinct techniques across all articles
- NLM synthesis: 5 cross-notebook queries across all 10 sources
