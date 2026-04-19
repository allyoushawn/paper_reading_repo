# Article Analysis: Token-saving updates on the Anthropic API

**Source:** https://www.claude.com/blog/token-saving-updates
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Token-saving updates on the Anthropic API
**Author/Publisher:** Anthropic
**Published:** March 13, 2025

**Key contributions:**
- Introduced cache-aware rate limits where prompt cache read tokens no longer count against ITPM limits
- Simplified prompt caching with automatic prefix matching (no manual cache segment tracking)
- Released token-efficient tool use beta reducing output token consumption by up to 70%
- Introduced the text_editor tool for targeted document/code edits

**Core techniques described:**
- **Cache-aware rate limits:** Prompt cache read tokens no longer count against Input Tokens Per Minute (ITPM) limit for Claude 3.7 Sonnet, allowing developers to increase throughput without changing OTPM rate limits.
- **Simpler cache management:** Setting a cache breakpoint now triggers automatic identification and reading from the longest previously cached prefix, eliminating manual tracking of cached segments.
- **Token-efficient tool use:** Adding beta header `token-efficient-tools-2025-02-19` enables Claude to call tools in a token-efficient manner, reducing output token consumption by up to 70%.
- **Text_editor tool:** A specialized tool allowing Claude to make targeted edits to specific portions of text within documents, source code, or research reports, improving accuracy while reducing latency and token consumption.

**Quantitative results:**
- Prompt caching reduces costs by **up to 90%** for long prompts
- Prompt caching reduces latency by **up to 85%** for long prompts
- Token-efficient tool use reduces output token consumption by **up to 70%** (peak)
- Early users of token-efficient tool use saw an **average reduction of 14%** in output tokens

---

## 2. Implementation Details

- **Cache-aware rate limits & simpler cache management:** Apply prompt caching with Claude 3.7 Sonnet. When setting a cache breakpoint, Claude now automatically identifies and reads from the longest previously cached prefix. No manual tracking of cache segments needed.
- **Token-efficient tool use:** Add beta header `token-efficient-tools-2025-02-19` to tool use requests with Claude 3.7 Sonnet. If using the SDK, use the beta SDK with `anthropic.beta.messages`.
- **Text_editor tool:** Provide the `text_editor` tool in API requests and handle tool use responses. Available on the Anthropic API, Amazon Bedrock, and Google Cloud's Vertex AI.

---

## 3. Limitations and Caveats

- OTPM rate limit remains the same even with cache-aware ITPM limits
- Token-efficient tool use is currently in **beta** status only
- These specific updates are explicitly available for **Claude 3.7 Sonnet** (note: Claude 4+ models have built-in token-efficient tool use and the beta header has no effect)

---

## 4. Related Techniques

- **Prompt caching:** The foundational feature that stores and reuses frequently accessed context between API calls
- **Client-side tool use:** The existing capability for Claude to interact with external tools and functions, now optimized by the token-efficient beta
- **Anthropic SDKs:** Referenced for the `anthropic.beta.messages` integration needed for beta features

---

## 5. Project Relevance

### (a) Directly applicable techniques for agentic workflows
- **Simpler prompt caching:** Agentic workflows involve long, multi-turn sessions that repeatedly send large system prompts, skill schemas, and codebase context. Automatic prefix matching reduces input token waste by up to 90% without manual cache segment tracking.
- **Token-efficient tool use:** Since agentic systems rely fundamentally on tool calls, the beta header directly reduces output token consumption by up to 70%.
- **Text_editor tool:** For coding assistants, this replaces full file rewrites with targeted edits, massively reducing output token consumption.

### (b) Interaction with subagent delegation
- **Zero-overhead context sharing:** Child subagents can leverage the same cached prefixes already processed by the parent, making spawning heavily contextualized child agents cheaper and faster.
- **Rate limit protection for parallel agents:** Cache-aware ITPM limits allow multiple subagents to run concurrently on the same codebase without hitting throughput bottlenecks.
- **Lean context return:** Child agents using text_editor return only targeted edits rather than full file rewrites, preventing parent context bloat.

### (c) Implementation priority
1. **First: Implement prompt caching** — up to 90% cost reduction and 85% latency reduction; automatic prefix matching makes this easy to adopt.
2. **Second: Adopt text_editor tool and token-efficient beta headers** — up to 70% output token reduction; ensures the agent spends its budget on reasoning rather than formatting.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2025_Anthropic_NA_Prompt-Caching-With-Claude.md | Core techniques | Provides comprehensive documentation of the prompt caching feature introduced here, including detailed pricing, TTL options, and cache hierarchy mechanics |
| 2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md | Core techniques | Documents token-efficient tool use becoming built-in for Claude 4+ (no beta header needed); references text_editor tool version updates |
| 2026_Anthropic_NA_Manage-Tool-Context.md | Core techniques | Lists prompt caching as one of four composable approaches to managing tool context bloat |
| 2025_DevTo_NA_Claude-API-Cost-Optimization.md | Implementation Details | References prompt caching and tool definition caching for production cost reduction; cites 65% system prompt savings |
| 2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md | Caching Strategies | Identifies provider-level prompt caching as "most impactful single optimization" for agents; cites ~90% cached token reduction |

---

## Meta Information

**Publisher:** Anthropic
**Year:** 2025
**Type:** Tech blog
**Relevance:** Core
**Priority:** 1
