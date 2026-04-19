# Article Analysis: Effort parameter and adaptive thinking

**Source:** https://docs.anthropic.com/en/docs/build-with-claude/effort
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Effort — Claude API Docs
**Author/Publisher:** Anthropic
**Published:** 2025 (documentation, continuously updated)

**Key contributions:**
- Introduced the `effort` parameter as a GA feature to control token spend across text responses, tool calls, and extended thinking
- Defined four effort levels (max, high, medium, low) with clear use-case mapping
- Documented how effort replaces deprecated `budget_tokens` for Claude 4.6 models
- Showed effort's direct impact on tool use behavior (fewer calls, combined operations at lower effort)

**Core techniques described:**
- **Four effort levels:**
  - `max` — deepest reasoning, no token constraints (Opus 4.6, Sonnet 4.6, Mythos Preview only)
  - `high` — default, equivalent to not setting the parameter; complex reasoning and agentic tasks
  - `medium` — balanced speed, cost, and performance; recommended for agentic coding
  - `low` — most efficient, significant token savings; ideal for subagents and simple tasks
- **Tool use impact:** Lower effort → fewer tool calls, combined operations, no preamble, terse confirmations. Higher effort → more calls, plan explanations, detailed summaries, comprehensive comments.
- **Extended/adaptive thinking integration:** Effort replaces `budget_tokens` for Claude Opus 4.6 and Sonnet 4.6. At high/max effort, Claude almost always thinks deeply. At lower levels, may skip thinking for simple problems.
- **ZDR eligibility:** The effort feature is eligible for Zero Data Retention.

**Quantitative results:**
- No specific percentage benchmarks cited. Documentation describes improvements qualitatively: low effort provides "significant token savings" and can "significantly reduce response times and costs" for high-volume or speed-sensitive tasks.

---

## 2. Implementation Details

**API parameter:** Add `effort` to API requests. Accepts: `max`, `high`, `medium`, `low`.

**Model-specific configurations:**
- **Claude Opus 4.6 / Sonnet 4.6:** Combine with `thinking: {type: "adaptive"}`. Effort is the recommended control for thinking depth. `budget_tokens` deprecated.
- **Claude Opus 4.5 / other Claude 4:** Use effort alongside manual `thinking: {type: "enabled", budget_tokens: N}`.
- **Claude Mythos Preview:** Adaptive thinking by default (no thinking config required). `thinking: {type: "disabled"}` is rejected.

**Recommended defaults for Sonnet 4.6:**
- `medium` — recommended default for most applications (agentic coding, tool-heavy workflows)
- `low` — high-volume or latency-sensitive workloads (chat, non-coding)
- `high` — tasks requiring maximum Sonnet 4.6 intelligence
- `max` — absolute highest capability with no constraints

---

## 3. Limitations and Caveats

- **Not a strict constraint:** Effort is a behavioral signal, not a strict token budget. Claude may still think on difficult problems at low effort.
- **`max` restricted:** Only available on Mythos Preview, Opus 4.6, and Sonnet 4.6
- **Deprecation warnings:** `budget_tokens` still accepted on Opus 4.6/Sonnet 4.6 but deprecated; will be removed in future release
- **Latency trap:** Sonnet 4.6 defaults to `high`; not explicitly setting effort may cause unexpected latency
- **Thinking rejection:** On Mythos Preview, `thinking: {type: "disabled"}` is rejected

---

## 4. Related Techniques

- **Extended thinking / adaptive thinking:** Effort integrates with and replaces older methods of controlling thinking depth
- **Tool use:** Effort directly influences number of tool calls, operation combining, and verbosity of tool-related explanations
- **Zero Data Retention (ZDR):** Effort feature is ZDR eligible

---

## 5. Project Relevance

### (a) Directly applicable techniques for agentic workflows
- **Dynamic effort parameter:** Controls total token spend across text, tool calls, and thinking. Lower effort → fewer tool calls, combined operations, no preamble. Critical for controlling cost in tool-heavy agentic systems.
- **Adaptive thinking integration:** Model self-calibrates reasoning depth. Skip thinking on simple tasks, reason deeply on complex ones.

### (b) Interaction with subagent delegation
- **Low effort for subagents:** Documentation explicitly recommends `low` effort for subagents — "Simpler tasks that need the best speed and lowest costs, such as subagents."
- **Dynamic effort allocation:** Orchestrator at `high` or `medium` effort for complex planning; child agents at `low` effort for narrow, mechanical tasks.
- **Single model flexibility:** One model (e.g., Sonnet 4.6) can serve all tiers of the delegation pattern by adjusting effort per request.

### (c) Implementation priority
1. **First: Set effort parameter explicitly** across entire codebase. API defaults to `high` which maximizes token spend. Immediately change baseline to `medium` for Sonnet 4.6.
2. **Second: Implement dynamic effort** — any code spawning subagents or requesting simple lookups should override to `low` effort.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md | Adaptive thinking migration | Documents effort replacing budget_tokens on Claude 4.6; provides migration path from manual to adaptive thinking |
| 2026_DevTo_NA_Agents-Dont-Need-Sonnet.md | Core techniques | Implicitly references effort tuning; lower effort for subagents aligns with the 3-tier model routing strategy |
| 2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md | Output token premium | References output token management and reasoning depth control as cost lever for agents |

---

## Meta Information

**Publisher:** Anthropic
**Year:** 2025
**Type:** Official documentation
**Relevance:** Core
**Priority:** 1
