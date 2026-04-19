# Article Analysis: Prompt caching with Claude

**Source:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Prompt caching — Claude API Docs
**Author/Publisher:** Anthropic
**Published:** 2025 (documentation, continuously updated)

**Key contributions:**
- Comprehensive documentation of prompt caching: automatic and explicit breakpoint modes
- Detailed caching hierarchy (tools → system → messages) and invalidation rules
- Pricing model: cache reads at 0.1x base input price, 5-min writes at 1.25x, 1-hour writes at 2x
- Support for mixing TTLs, caching with extended thinking blocks, and workspace-level isolation

**Core techniques described:**
- **Automatic caching:** Add a single `cache_control` field at the top level of the request. System auto-applies cache breakpoint to last cacheable block and moves it forward as conversations grow.
- **Explicit cache breakpoints:** Place `cache_control` on individual content blocks for fine-grained control. Up to 4 breakpoints per prompt.
- **Hierarchical caching order:** Cache prefixes build in strict order: tools → system → messages. Any modification invalidates that level and subsequent levels.
- **TTL settings:** Default 5-minute lifetime (ephemeral cache); optional 1-hour TTL at 2x base input token price.
- **Caching with extended thinking:** Thinking blocks are automatically cached alongside other content when subsequent API calls include tool results.
- **Data isolation:** As of Feb 5, 2026, caches are isolated per workspace. Prompt caching is ZDR eligible.

**Quantitative results:**
- Cache reads cost **0.1x** (10%) of base input token price
- 5-minute cache write cost: **1.25x** base input token price
- 1-hour cache write cost: **2x** base input token price
- Minimum cacheable prompt lengths: 4096 tokens (Opus 4.6/4.5, Haiku 4.5), 2048 tokens (Sonnet 4.6, Haiku 3.5/3), 1024 tokens (Sonnet 4.5, Opus 4.1/4, Sonnet 4/3.7)
- Improved time-to-first-token for long documents

---

## 2. Implementation Details

**Automatic caching:**
- Add single `cache_control` field at top level of request body
- System auto-applies breakpoint to last cacheable block; moves forward as conversations grow
- Supports 5-minute or 1-hour TTL

**Explicit cache breakpoints:**
- Place `cache_control` on individual content blocks
- Up to 4 explicit breakpoints per prompt
- Place static content (tools, system instructions, context) at beginning of prompt
- Mark end of reusable content with `cache_control` parameter

**Cache hierarchy:** tools → system → messages (each level builds on previous)

**Automatic prefix checking:**
- Cache writes happen only at breakpoints
- Cache reads look backward up to 20 positions per breakpoint
- System finds longest previously-written prefix automatically

**Performance tracking:** Monitor via `cache_creation_input_tokens`, `cache_read_input_tokens`, and `input_tokens` in response usage fields.

**Mixing TTLs:** Longer TTL entries must appear before shorter ones. API determines three billing positions (A, B, C) for mixed-TTL requests.

---

## 3. Limitations and Caveats

- **Minimum token thresholds:** Below-minimum prompts processed without caching, **no error returned** (silent failure)
- **20-block lookback window:** If a growing conversation pushes the breakpoint 20+ blocks past the last cache write, the lookback misses it. Mitigation: add a second breakpoint closer to that position.
- **100% exact matching required:** Any text or image modification invalidates cache
- **Invalidation sensitivity:** Modifying tool definitions, tool_choice, images, extended thinking parameters, web search/citations toggles can all invalidate cache
- **Uncacheable elements:** Empty text blocks, sub-content blocks (citations), and thinking blocks cannot be explicitly marked with cache_control
- **Automatic caching edge cases:** Returns 400 error if 4 explicit breakpoints already exist or if last block has different TTL
- **Parallel request timing:** Cache entry only available after first response begins; concurrent requests before that miss cache

---

## 4. Related Techniques

- **Extended thinking (thinking blocks):** Interacts heavily with caching; thinking blocks count as input tokens when read from cache; non-tool-result user content can strip previously cached thinking blocks
- **Zero Data Retention (ZDR):** Prompt caching is ZDR eligible
- **Tool use (agentic tools):** Tool definitions form the first level of cache hierarchy
- **Batch API:** Pricing modifiers from caching stack with Batch API discount
- **Citations, web search, images:** Usage toggles affect system and message caches

---

## 5. Project Relevance

### (a) Directly applicable techniques for agentic workflows
- **Automatic caching for multi-turn sessions:** Single `cache_control` field enables automatic caching of growing conversation history. Cache point moves forward automatically.
- **Explicit caching for tools and context:** Static tool definitions and codebase context placed at prompt beginning can be explicitly cached, drastically reducing iterative code change costs.
- **Thinking block caching during tool use:** Extended thinking blocks auto-cached alongside tool results, saving input token costs on subsequent reasoning steps.

### (b) Interaction with subagent delegation
- **1-hour TTL for side-agents:** Default 5-min cache expires if spawned subagent takes longer. Apply 1-hour TTL to parent agent's context to prevent cache misses when child returns.
- **Parallel subagent execution:** Must wait for first agent's response before sending parallel requests — cache entries only available after first response starts.
- **Hierarchical prefix sharing:** If multiple subagents share the same tool schemas and system prompts, placing these at the top of requests ensures all child agents hit the same cached prefix.

### (c) Implementation priority
1. **First: Enable automatic caching** — simplest approach, handles breakpoint management automatically for multi-turn conversations
2. **Second: Reorder and explicitly cache static content** — restructure requests so largest static elements (tool definitions, system instructions) appear first with explicit breakpoints
3. **Third: Optimize TTLs** — apply 1-hour TTL (2x write cost) for long-running subagent delegations

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2025_Anthropic_NA_Token-Saving-API-Updates.md | Core techniques | Announces simpler cache management with automatic prefix matching and cache-aware rate limits as improvements to the caching system documented here |
| 2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md | Limitations | Notes that extended thinking usage reduces prompt caching efficiency |
| 2026_Anthropic_NA_Manage-Tool-Context.md | Core techniques | References prompt caching for stable tool definitions; notes cache writes carry 25% markup but pay back on second hit |
| 2025_Anthropic_NA_Context-Windows-Guide.md | Related Techniques | References caching with extended thinking blocks; thinking blocks auto-cached alongside tool results |
| 2025_DevTo_NA_Claude-API-Cost-Optimization.md | Implementation Details | Implements prompt caching with explicit breakpoints; structures static content first; cites 10% cache read cost and 8x reduction |
| 2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md | Caching Strategies | Provides quantitative framework citing 90% cached token cost reduction and 75-85% latency reduction from prompt caching |

---

## Meta Information

**Publisher:** Anthropic
**Year:** 2025
**Type:** Official documentation
**Relevance:** Core
**Priority:** 1
