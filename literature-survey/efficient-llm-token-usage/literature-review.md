Date: 2026-04-12
Topic: Efficient LLM Token Usage for Agentic Workflows
Article count: 10

# Efficient LLM Token Usage - Literature Review

## Executive Summary

Across 10 tech blog articles and official documentation sources, a clear consensus emerges: agentic workflows are inherently expensive — consuming 3–10x more tokens than simple chat interactions due to multi-turn loops, quadratic context growth, and output token premiums (3–8x input cost). However, three dominant optimization strategies compose to deliver 60–80% total cost reduction. Provider-level prompt caching is the single highest-ROI technique (up to 90% input cost reduction with minimal code changes), followed by model routing (up to 87% cost reduction by matching task complexity to model capability), and context compaction/pruning (~40% per-turn input savings). For Claude-based agentic systems specifically, the effort parameter and built-in token-efficient tool use provide additional low-effort output token savings that compound across every tool call.

### Most Promising Approaches
1. **Prompt Caching:** Up to 90% input cost reduction — cache static tool definitions and system prompts; automatic prefix matching handles multi-turn growth
2. **Model Routing with Effort Tuning:** Up to 87% cost reduction — route mechanical tasks to Haiku/Ollama; use `effort: low` for subagents, `effort: medium` for orchestrators
3. **Context Compaction & Editing:** ~40% per-turn savings — trim stale tool results, use microcompaction for bulky outputs, enable server-side compaction for long sessions

### Practical Recommendations

**Short term (1–3 months):**
- Enable automatic prompt caching with `cache_control` on all API calls — immediate 90% savings on static tokens
- Set `effort: medium` as default for Sonnet 4.6 orchestration, `effort: low` for all subagent calls
- Add circuit breakers (max iteration caps) to every agent loop to prevent runaway costs
- Route reading/exploration subagents to Haiku ($0.25/M vs $3/M input tokens)

**Mid term (3–6 months):**
- Implement context editing to prune stale tool_result blocks from long sessions
- Add skill-based declarative routing so each skill declares its minimum-viable model
- Build microcompaction for bulky tool outputs (file reads, bash results → hot tail/cold storage split)
- Deploy cost observability (per-trace token tracking) to identify optimization opportunities

---

## 1. Caching and Cost Reduction Strategies (4 articles)

Prompt caching is the foundational optimization layer for agentic workflows. By storing KV representations of static prompt prefixes (system instructions, tool schemas, knowledge bases), subsequent API calls that match the cached prefix pay only 10% of the base input token price. This category covers the mechanics of Anthropic's caching system, production implementation patterns, and the broader cost landscape that makes caching essential.

### Token-saving updates on the Anthropic API (Anthropic 2025)
- Source: Anthropic 2025
- Detailed analysis: [read-papers/2025_Anthropic_NA_Token-Saving-API-Updates.md](./read-papers/2025_Anthropic_NA_Token-Saving-API-Updates.md)

Relevance to efficient token usage:
Introduces three complementary API-level optimizations — cache-aware rate limits (cached reads don't count against ITPM), automatic prefix matching (no manual cache tracking), and token-efficient tool use beta (up to 70% output token reduction). Also introduces the text_editor tool for targeted edits instead of full file rewrites. Together these updates reduce both input and output costs with minimal code changes.

### Prompt caching — Claude API Docs (Anthropic 2025)
- Source: Anthropic 2025
- Detailed analysis: [read-papers/2025_Anthropic_NA_Prompt-Caching-With-Claude.md](./read-papers/2025_Anthropic_NA_Prompt-Caching-With-Claude.md)

Relevance to efficient token usage:
Comprehensive documentation of prompt caching mechanics: automatic vs explicit breakpoints, hierarchical cache order (tools → system → messages), TTL options (5-min default, 1-hour at 2x cost), and cache invalidation rules. Cache reads cost 0.1x base input price. Critical for agentic workflows where static tool definitions and system prompts are resent on every turn. Minimum cacheable lengths vary by model (1024–4096 tokens).

### Claude API Cost Optimization: Caching, Batching, and 60% Token Reduction (DEV Community 2026)
- Source: DEV Community (Atlas Whoff) 2026
- Detailed analysis: [read-papers/2025_DevTo_NA_Claude-API-Cost-Optimization.md](./read-papers/2025_DevTo_NA_Claude-API-Cost-Optimization.md)

Relevance to efficient token usage:
Production-validated methodology achieving ~60% per-session cost reduction across an autonomous agent ("Atlas"). Five concrete techniques with real numbers: prompt caching (~65% system prompt savings), tool definition caching, context window pruning (keep last 6 message pairs = ~40% input reduction), Batch API (50% for async workloads), and model routing (Haiku for ~30% of tasks). Demonstrates these techniques working in combination.

### AI Agent Cost Optimization: Token Economics and FinOps (Zylos Research 2026)
- Source: Zylos Research 2026
- Detailed analysis: [read-papers/2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md](./read-papers/2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md)

Relevance to efficient token usage:
Comprehensive framework covering four pillars: token cost landscape, caching strategies, model routing, and LLM FinOps. Quantifies why agents are expensive (3–10x more calls, 50x tokens in loops, output 3–8x premium). Introduces advanced techniques not covered elsewhere: semantic caching (~31% query elimination), prompt compression (LLMLingua, up to 20x), and FinOps governance. Reports combined caching + routing + compression delivers 60–80% total reduction.

---

## 2. Model Routing and Output Optimization (3 articles)

The output token premium (3–8x input cost) makes controlling what the model generates just as important as controlling what it receives. This category covers adaptive thinking via the effort parameter, the transition to built-in token-efficient tool use in Claude 4+, and practical multi-tier routing strategies that match model capability to task complexity.

### Migration guide — Claude 4.6 (Anthropic 2026)
- Source: Anthropic 2026
- Detailed analysis: [read-papers/2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md](./read-papers/2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md)

Relevance to efficient token usage:
Documents the transition to adaptive thinking (effort parameter replacing budget_tokens), built-in token-efficient tool use for all Claude 4+ models, and the removal of prefill in favor of structured outputs. Provides concrete implementation priority: (1) prompt/tool caching, (2) model routing + adaptive thinking, (3) context compaction, (4) tool search for 20+ tool systems. Key for understanding the current-gen Claude API surface.

### Effort parameter — Claude API Docs (Anthropic 2025)
- Source: Anthropic 2025
- Detailed analysis: [read-papers/2025_Anthropic_NA_Effort-Parameter-Adaptive-Thinking.md](./read-papers/2025_Anthropic_NA_Effort-Parameter-Adaptive-Thinking.md)

Relevance to efficient token usage:
Defines the effort parameter as a single dial controlling total token spend across text, tool calls, and thinking. Four levels (max/high/medium/low) map directly to agentic delegation patterns. Low effort → fewer tool calls, combined operations, terse output. Anthropic explicitly recommends `low` effort for subagents and `medium` for agentic coding on Sonnet 4.6. A single model can serve all delegation tiers by adjusting effort per request.

### Most of your Claude Code agents don't need Sonnet (DEV Community 2026)
- Source: DEV Community (Edward Kubiak) 2026
- Detailed analysis: [read-papers/2026_DevTo_NA_Agents-Dont-Need-Sonnet.md](./read-papers/2026_DevTo_NA_Agents-Dont-Need-Sonnet.md)

Relevance to efficient token usage:
Practical 3-tier model routing: Sonnet for reasoning (planning, debugging, security) → Haiku for pattern-matching (code review, commits, docs) at 12x less → Ollama for mechanical tasks (commit messages) at zero API cost. Includes validation gates, automatic escalation (Ollama→Haiku→Sonnet), and a realistic daily cost breakdown ($0.37/day tiered vs $0.90/day all-Sonnet). Introduces skill-based declarative routing where each skill declares its minimum-viable model.

---

## 3. Context Window Management and Compaction (3 articles)

Agentic workflows naturally accumulate context — tool definitions, tool results, conversation history, thinking blocks — until the window fills and costs compound quadratically. This category covers four composable approaches (tool search, programmatic calling, caching, context editing), the mechanics of Claude's compaction system, and strategies for staying within context limits while maintaining task continuity.

### Manage tool context — Claude API Docs (Anthropic 2026)
- Source: Anthropic 2026
- Detailed analysis: [read-papers/2026_Anthropic_NA_Manage-Tool-Context.md](./read-papers/2026_Anthropic_NA_Manage-Tool-Context.md)

Relevance to efficient token usage:
Presents four composable approaches to tool context bloat: (1) tool search — on-demand discovery instead of loading all schemas, recommended for 20+ tools; (2) programmatic tool calling — collapse sequential calls into one script, intermediate results never enter history; (3) prompt caching — amortize stable tool definitions, 25% write markup pays back on second hit; (4) context editing — trim stale tool_result blocks. All four compose without conflict.

### Context Windows — Claude API Docs (Anthropic 2025)
- Source: Anthropic 2025
- Detailed analysis: [read-papers/2025_Anthropic_NA_Context-Windows-Guide.md](./read-papers/2025_Anthropic_NA_Context-Windows-Guide.md)

Relevance to efficient token usage:
Documents context windows as "working memory" (1M tokens for Opus/Sonnet 4.6) and the critical concept of "context rot" — larger context ≠ better performance. Introduces server-side compaction (beta for Opus/Sonnet 4.6) for automatic conversation condensation, context awareness (model tracks remaining budget), automatic thinking block stripping (previous thinking blocks removed from context calculations), and tool result clearing. Newer models return validation errors on overflow rather than silently truncating.

### Inside Claude Code's Compaction System (Decode Claude 2026)
- Source: Decode Claude 2026
- Detailed analysis: [read-papers/2026_DecodeClaude_NA_Compaction-System-Deep-Dive.md](./read-papers/2026_DecodeClaude_NA_Compaction-System-Deep-Dive.md)

Relevance to efficient token usage:
Reverse-engineers Claude Code's three-layer compaction pipeline: (1) microcompaction — splits tool outputs into "hot tail" (recent, visible) and "cold storage" (older, saved to disk with reference); (2) auto-compaction — headroom accounting triggers summarization before context exhaustion; (3) manual compaction (`/compact` at task boundaries). Introduces structured summarization (checklist-style capturing intent, decisions, errors, next steps) and post-compaction rehydration (re-read 5 recent files, restore todos). For subagents: delta summarization — 1–2 sentence incremental updates rather than full state snapshots.

---

## Cross-Cutting Themes

### Theme 1: Composability of Techniques
Multiple sources emphasize that optimization techniques compose without conflict. The recommended stack: prompt caching (input cost) + effort parameter (output cost) + model routing (per-task cost) + context editing (session longevity). Each targets a different cost driver. (Sources: Manage-Tool-Context, Claude-API-Cost-Optimization, Agent-Cost-Optimization-Token-Economics)

### Theme 2: Output Tokens Are the Hidden Cost Driver
Output tokens cost 3–8x more than input tokens. Agents generating verbose chain-of-thought, full file rewrites, or detailed tool call preambles pay this premium on every step. The effort parameter, token-efficient tool use, structured outputs, and text_editor tool all attack this asymmetry. (Sources: Agent-Cost-Optimization-Token-Economics, Effort-Parameter-Adaptive-Thinking, Token-Saving-API-Updates)

### Theme 3: Subagent Delegation as Cost Architecture
Spawning subagents is not just about parallelism — it's a cost management strategy. Child agents run in isolated context (preventing parent bloat), can be routed to cheaper models, use low effort, and report back via delta summarization. The parent stays lean. (Sources: Compaction-System-Deep-Dive, Agents-Dont-Need-Sonnet, Token-Efficient-Tool-Use-Migration)

### Theme 4: Context Rot Makes Curation Critical
More context is not automatically better. All sources agree that curating what's in context matters as much as how much space is available. Context rot degrades accuracy as token count grows. Pruning, compaction, and tool search all serve this goal. (Sources: Context-Windows-Guide, Agent-Cost-Optimization-Token-Economics, Claude-API-Cost-Optimization)

---

## Open Problems and Limitations

1. **Cache invalidation fragility:** 100% exact prefix matching means any change to tool definitions, images, or thinking parameters invalidates the cache. No graceful degradation. (Prompt-Caching-With-Claude)
2. **Quality-cost tradeoff in routing:** Smaller models miss subtle vulnerabilities and generate plausible-but-wrong debugging hypotheses. No automated way to know when a task genuinely needs Sonnet. (Agents-Dont-Need-Sonnet)
3. **Compaction information loss:** Both truncation and summarization are lossy. Structured summarization mitigates but doesn't eliminate the risk of dropping critical context. (Compaction-System-Deep-Dive)
4. **Semantic caching security:** Vector similarity caches are vulnerable to key-collision attacks and require careful threshold tuning. (Agent-Cost-Optimization-Token-Economics)
5. **FinOps visibility gap:** Most teams know total spend but can't attribute costs to specific workflows, models, or users. (Agent-Cost-Optimization-Token-Economics)
6. **Effort parameter is a hint, not a contract:** Claude may still think deeply on hard problems at low effort. Token savings are probabilistic, not deterministic. (Effort-Parameter-Adaptive-Thinking)

---

## Methodology

- **Search period:** 2023–2026
- **Sources examined:** Anthropic official docs/blog (6), DEV Community (2), Decode Claude (1), Zylos Research (1)
- **Inclusion criteria:** Must describe concrete, applicable techniques for reducing token cost or improving output quality in agentic workflows
- **Exclusion criteria:** Academic papers, marketing content, generic introductions without optimization content
- **Analysis tool:** NLM cross-notebook queries for cross-source synthesis
- **Technique tracking:** 34 distinct techniques catalogued across all articles (see [method-tracker.md](./method-tracker.md))
