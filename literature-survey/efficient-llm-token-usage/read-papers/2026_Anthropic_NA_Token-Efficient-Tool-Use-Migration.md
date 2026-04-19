# Article Analysis: Token-efficient tool use migration guide

**Source:** https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/token-efficient-tool-use
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Migration guide — Claude API Docs
**Author/Publisher:** Anthropic
**Published:** 2026 (documentation, continuously updated for Claude 4.6)

**Key contributions:**
- Comprehensive migration guide for Claude 4.6 models covering breaking changes, deprecations, and behavioral shifts
- Documents the transition from `budget_tokens` (extended thinking) to adaptive thinking with the `effort` parameter
- Details token-efficient tool use becoming built-in for all Claude 4+ models (beta header no longer needed)
- Covers prefill removal, structured outputs migration, and sampling parameter constraints

**Core techniques described:**
- **Adaptive thinking:** Replaces deprecated `budget_tokens` on Claude 4.6 models. Uses `effort` parameter (low/medium/high/max) to calibrate reasoning depth per step. Particularly suited for autonomous multi-step agents, computer use agents, and bimodal workloads.
- **Assistant message prefill removal:** Prefilling returns 400 error on Claude 4.6. Migration paths: structured outputs, `output_config.format`, system prompt instructions, moving continuations to user messages.
- **Sampling parameter constraints:** Must use only `temperature` OR `top_p`, not both (breaking change from Claude 3.x).
- **Built-in token-efficient tool use:** All Claude 4+ models have built-in token-efficient tool use; beta headers `token-efficient-tools-2025-02-19` and `output-128k-2025-02-19` have no effect.
- **New stop reasons:** Applications must handle `refusal` and `model_context_window_exceeded` stop reasons.

**Quantitative results:**
- Sonnet 4.6 and Sonnet 4.5: **$3/M input tokens, $15/M output tokens**
- Haiku 4.5: **$1/M input tokens, $5/M output tokens**
- Haiku 4.5: increased output capacity of **64k tokens**
- Claude Sonnet 4.6: **best-in-class accuracy on computer use evaluations** using adaptive mode
- Temporary budget_tokens during migration: **~16k tokens** recommended to prevent runaway usage

---

## 2. Implementation Details

**Model ID updates:** `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-sonnet-4-5-20250929`, `claude-haiku-4-5-20251001`

**Prefill removal migration:**
- Controlling output format → use structured outputs or `output_config.format`
- Eliminating preambles → add system prompt instruction: "Respond directly without preamble"
- Continuations → move to user message: "Your previous response was interrupted..."
- Context hydration → inject reminders into user turn instead

**Adaptive thinking migration:**
- Change from `thinking: {type: "enabled", budget_tokens: N}` to `thinking: {type: "adaptive"}`
- Control depth via `effort` parameter (high for agents, medium for balanced, low for chat)
- Moves from `client.beta.messages.create` to `client.messages.create`

**Header cleanup:** Remove deprecated beta headers: `effort-2025-11-24`, `fine-grained-tool-streaming-2025-05-14`, `interleaved-thinking-2025-05-14`, `token-efficient-tools-2025-02-19`, `output-128k-2025-02-19`

**Tool version updates:** `text_editor_20250728`, `code_execution_20250825`; remove `undo_edit` command

---

## 3. Limitations and Caveats

- **JSON string escaping:** Claude 4.6 may handle Unicode/forward-slash escaping differently in tool call arguments; standard JSON parsers handle this automatically, but custom string-based parsing may break
- **Trailing newlines in tools:** Claude 4.5+ preserves trailing newlines in tool call parameters that older models stripped
- **Behavioral shifts:** Claude 4+ models have more concise, direct communication style; prompts may need updating for explicit direction
- **Default effort latency:** Sonnet 4.6 defaults to `high` effort; not setting explicitly may cause unexpected latency increase vs. Sonnet 4.5
- **Extended thinking impacts prompt caching:** Using extended thinking reduces prompt caching efficiency
- **Separate rate limits:** Haiku 4.5 has separate rate limits from Haiku 3.5/3

---

## 4. Related Techniques

- **Claude Managed Agents:** Alternative runtime that automatically handles most request-shape changes
- **Interleaved thinking:** Automatically enabled with adaptive thinking on Opus 4.6 and Sonnet 4.6
- **Fine-grained tool streaming:** Transitioned from beta to GA
- **Context awareness:** New capability in Haiku 4.5 with 64k output capacity
- **Prompt caching:** Efficiency impacted by extended thinking usage

---

## 5. Project Relevance

### (a) Directly applicable techniques for agentic workflows
- **Adaptive thinking with effort parameter:** Replaces legacy extended thinking. Allows the agent to dynamically scale reasoning depth — skip thinking for simple tasks, reason deeply for complex ones.
- **Structured outputs over prefills:** Eliminates verbose, unstructured outputs. `output_config.format` enforces strict schema adherence.
- **Built-in token-efficient tool use:** No beta header needed on Claude 4+; all tool calls are already token-efficient.

### (b) Interaction with subagent delegation
- **Tiered model routing:** Orchestrator agent runs on Sonnet 4.6 with `effort: high`; child agents for mechanical subtasks route to Haiku 4.5 ($1/M input) or use `effort: low`.
- **Context isolation:** Child agents should not inherit the orchestrator's full conversation history. Use delta summarization.
- **Subagent cache hits:** Standardized child agents (fixed system prompt + toolset) reliably trigger prompt cache hits.
- **Circuit breakers:** Pair delegation with max iteration caps or strict token budgets to prevent runaway subagent costs.

### (c) Implementation priority
1. **First: Prompt and tool definition caching** — up to 90% input token savings, minimal code changes
2. **Second: Model routing and adaptive thinking** — route simple tasks to Haiku 4.5 or lower effort settings to cut output token costs
3. **Third: Context compaction and pruning** — requires significant architectural engineering but critical for long-running workflows
4. **Fourth: Tool search** — only necessary once toolset exceeds ~20 tools

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2025_Anthropic_NA_Effort-Parameter-Adaptive-Thinking.md | Core techniques | Provides detailed documentation of the effort parameter and adaptive thinking that this migration guide introduces as replacing budget_tokens |
| 2026_DevTo_NA_Agents-Dont-Need-Sonnet.md | Core techniques | Builds on model routing concept introduced here with a concrete 3-tier strategy (Sonnet/Haiku/Ollama) |
| 2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md | Model Routing | References model routing and cascading patterns at enterprise scale; cites 87% cost reduction from well-implemented cascades |

---

## Meta Information

**Publisher:** Anthropic
**Year:** 2026
**Type:** Official documentation
**Relevance:** Core
**Priority:** 1
