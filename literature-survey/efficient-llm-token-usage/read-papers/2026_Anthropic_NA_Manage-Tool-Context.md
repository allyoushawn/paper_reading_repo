# Article Analysis: Manage tool context

**Source:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Manage tool context — Claude API Docs
**Author/Publisher:** Anthropic
**Published:** 2026 (documentation)

**Key contributions:**
- Identified the core problem of context bloat from tool definitions and accumulated tool_result blocks
- Presented four composable approaches targeting different sources of context pressure: tool search, programmatic tool calling, prompt caching, context editing
- Provided a concrete prioritized adoption path for high-volume agents
- Framework for combining all techniques together in long-running agent systems

**Core techniques described:**
- **Tool search:** Provides a single `tool_search` tool instead of loading all tool schemas upfront. Claude discovers needed tools on demand. Recommended for 20+ tool toolsets.
- **Programmatic tool calling:** Collapses multiple sequential tool calls into a single executable script running in Anthropic's code execution sandbox. Intermediate tool_result roundtrips never enter conversation history.
- **Prompt caching:** Caches stable tool definitions so the prefix is reused across thousands of requests. Reduces token cost (not count) on subsequent requests.
- **Context editing:** Removes old, irrelevant tool_result blocks from conversation history without restarting the conversation.

**Quantitative results:**
- Cache writes carry **25% markup** over base input pricing; pays for itself by the **second request** hitting cache
- Tool search trades **one extra turn** of latency for large reduction in baseline context usage
- Tool search recommended once toolset grows past roughly **20 tools**
- Prompt caching reusable across **thousands of requests**

---

## 2. Implementation Details

**Tool search:**
- Replace all upfront tool schemas with a single `tool_search` tool
- Claude discovers specific tools on demand, keeping context lean
- Implement once toolset exceeds ~20 tools

**Programmatic tool calling:**
- Claude writes a single code block calling multiple functions
- Runs in Anthropic's code execution sandbox
- Intermediate results never enter conversation history
- Best for repetitive chains of small tool calls

**Prompt caching:**
- Cache stable tool definitions from day one
- 25% markup on cache writes pays back on second cache hit
- Does not reduce context window usage, only financial cost

**Context editing:**
- Trim old tool_result blocks from conversation history
- Implement once conversations run long enough that early results become irrelevant
- Allows continued conversation without restart

**Combining approaches:** All four compose without conflict. A long-running agent can use tool search (lean toolset) + prompt caching (amortize definitions) + context editing (trim stale results) + programmatic calling (batch operations).

---

## 3. Limitations and Caveats

- **Tool search latency:** Adds one extra turn for tool discovery
- **Prompt caching does not reduce context window size:** Only reduces financial cost, not actual token count in context
- **Cache write markup:** 25% over base input pricing (but pays back by second request)
- **Context exhaustion risk:** Without these techniques, long-running agents or agents with many tools can exhaust available context before task completion

---

## 4. Related Techniques

- **Tool definitions and tool_result blocks:** The core components causing context bloat
- **Anthropic's code execution sandbox:** Runtime for programmatic tool calling
- **Conversation history / context windows:** The underlying memory structure these techniques optimize

---

## 5. Project Relevance

### (a) Directly applicable techniques for agentic workflows
- **Tool search:** Instead of loading every skill and tool definition upfront, use a single tool_search tool for on-demand discovery. Directly reduces baseline context usage.
- **Programmatic tool calling:** Collapse sequential tool chains into single scripts. Prevents intermediate tool_result blocks from bloating multi-turn history.
- **Prompt caching:** Reduces token cost for stable tool definitions reused across thousands of requests.
- **Context editing:** Trim stale tool_result blocks from long-running coding sessions.

### (b) Interaction with subagent delegation
- **Lean child agents:** Using tool search, child agents start with minimal context and discover only needed tools for their delegated subtask (not the parent's full 50+ tool schemas).
- **Programmatic tool calling as pseudo-subagent:** Collapses complex sequences into one executed batch, keeping parent agent's context free of intermediate steps.
- **Post-delegation cleanup:** Context editing trims hundreds of intermediate results from child agent execution, retaining only final output.

### (c) Implementation priority
1. **First: Prompt caching** — enable from day one on stable tool definitions; 25% markup pays back on second cache hit
2. **Second: Tool search** — add once toolset exceeds ~20 tools or baseline context usage becomes noticeable
3. **Third: Context editing** — implement once individual sessions run long enough that early results become irrelevant
4. **Fourth: Programmatic tool calling** — adopt if repetitive chains of small tool calls emerge

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md | Implementation priority | Lists tool search as fourth priority once toolset exceeds ~20 tools |
| 2025_Anthropic_NA_Context-Windows-Guide.md | Context editing | References tool result clearing and thinking block clearing as fine-grained context editing strategies |
| 2026_DecodeClaude_NA_Compaction-System-Deep-Dive.md | Microcompaction | Extends context editing concepts with hot tail/cold storage split for tool results; adds structured summarization layer |

---

## Meta Information

**Publisher:** Anthropic
**Year:** 2026
**Type:** Official documentation
**Relevance:** Core
**Priority:** 1
