# Article Analysis: Context Windows - Claude API Docs

**Source:** https://docs.claude.com/en/docs/build-with-claude/context-windows
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Context Windows - Claude API Docs
**Author/Publisher:** Anthropic
**Published:** Ongoing documentation (continuously updated)

**Key contributions:**
- Comprehensive guide on how Claude's context windows function as "working memory"
- Introduces server-side compaction as the primary strategy for long-running conversations
- Documents context awareness — models that track their own remaining token budget
- Details extended thinking token management with automatic stripping of previous thinking blocks
- Explains tool result clearing and thinking block clearing as fine-grained context editing strategies

**Core techniques described:**
- **Server-Side Compaction:** Automatically condenses earlier conversation parts via server-side summarization, enabling conversations beyond context limits. Currently in beta for Claude Opus 4.6 and Sonnet 4.6.
- **Context Editing:** Tool result clearing (removing old tool outputs in agentic workflows) and thinking block clearing (managing extended thinking blocks).
- **Automatic Stripping of Extended Thinking:** Previous thinking blocks are automatically stripped from context window calculations by the API when passed back. Effective formula: `context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens`.
- **Interleaved Thinking (Claude 4):** Claude 4 models can think between tool calls for more sophisticated reasoning after receiving tool results. Not supported on Claude Sonnet 3.7.
- **Context Awareness:** Available in Claude Sonnet 4.6, Sonnet 4.5, and Haiku 4.5 — models track remaining token budget throughout a conversation, receiving updates after each tool call.
- **Token Counting API:** Estimating token usage before sending messages to stay within limits.

**Quantitative results:**
- Context window: **1M tokens** for Claude Mythos Preview, Opus 4.6, Sonnet 4.6; **200k tokens** for Sonnet 4.5 and Sonnet 4
- Up to **600 images or PDF pages** per request (1M-token models); **100** for 200k-token models
- State-of-the-art on long-context benchmarks: **MRCR** and **GraphWalks**
- "Context rot" — accuracy and recall degrade as token count grows, making curation critical

---

## 2. Implementation Details

- **Tool Use with Extended Thinking:** Developers must return the entire, unmodified thinking block (including cryptographic signature portions) alongside the `tool_result`. After the tool use cycle completes and a new user turn begins, the API automatically strips previous thinking blocks (or developers can manually strip at that stage).
- **Token Counting API:** Use to estimate usage before sending messages to stay within context limits.
- **State Artifacts for Multi-Session Agents:** Design compact state artifacts for fast context recovery when new sessions start; leverage the memory tool's multi-session pattern.
- **Context Awareness:** Automatic — models with context awareness receive their total budget (1M or 200k) at session start, with remaining capacity updates after each tool call. No specific API parameter needed to enable.

---

## 3. Limitations and Caveats

- **Context Rot:** Larger context ≠ better performance; accuracy degrades as token count grows
- **Validation Errors:** Newer models (starting with Sonnet 3.7) return a validation error on token exceedance instead of silently truncating — requires more careful token management
- **Attachment Limits:** Hard caps on images/PDFs per request (600 for 1M-token models, 100 for 200k)
- **Thinking Block Authenticity:** Cryptographic signatures verify thinking blocks — modifying them breaks reasoning continuity and returns an API error
- **Interleaved Thinking:** Not supported on Claude Sonnet 3.7 (requires non-`tool_result` user turn in between)
- **Thinking Token Billing:** Billed as output tokens (once, during generation), count toward rate limits

---

## 4. Related Techniques

- Server-Side Compaction (beta for Opus 4.6 and Sonnet 4.6)
- Context Editing: tool result clearing and thinking block clearing
- Extended Thinking and Adaptive Thinking
- Interleaved Thinking (Claude 4 models)
- Memory Tool (multi-session pattern for context recovery)
- Token Counting API

---

## 5. Project Relevance

**(a) Directly applicable techniques for agentic workflows:**
- **Automatic stripping of extended thinking** preserves massive context space without manual intervention — critical when agents do multi-step planning
- **Context editing / tool result clearing** prevents stale file reads, test outputs, and error logs from filling the window
- **Server-side compaction** enables long-running multi-turn coding sessions to continue beyond context limits
- **Context awareness** lets the agent pace itself precisely during complex tasks rather than failing mid-flight

**(b) Interaction with subagent delegation:**
- Cryptographic thinking signatures must be preserved exactly during tool use cycles (including Task tool delegations)
- State artifacts should be designed for fast, compact context recovery — pass essential state between parent and child agents rather than raw conversation logs
- Model routing pairs well with subagent delegation: parent on Sonnet 4.6, children on Haiku 4.5 or local models

**(c) Implementation priority:**
1. **Prompt caching + tool search** — immediate 90% input cost reduction on static content
2. **Context editing / tool result clearing** — prevents the fastest-growing source of token waste
3. **Model routing + validation gates** — 60%+ cost reduction on per-action basis
4. **Server-side compaction + context awareness** — long-term resilience for indefinite sessions

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md | Implementation priority | Lists context compaction and pruning as third priority for long-running workflows |
| 2026_Anthropic_NA_Manage-Tool-Context.md | Context editing | Describes context editing as one of four composable tool context management approaches |
| 2026_DecodeClaude_NA_Compaction-System-Deep-Dive.md | Full article | Deep-dives the compaction system overviewed here — reverse-engineers microcompaction, auto-compaction, and structured summarization |
| 2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md | Agent cost compounding | References quadratic context growth and context rot as fundamental cost drivers requiring compaction |

---

## Meta Information

**Publisher:** Anthropic
**Year:** 2025
**Type:** Official documentation
**Relevance:** Core
**Priority:** 1
