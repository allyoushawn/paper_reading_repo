Date: 2026-04-12 (last updated)
Topic: Efficient LLM Token Usage for Agentic Workflows

# Efficient LLM Token Usage - Technique Tracking

## Technique Table

| Technique | First Described In | Mention Count | Token Savings Reported | Complexity (1-5) | Applicability to Agentic Workflows (1-5) | Composite Score |
|-----------|-------------------|---------------|----------------------|-------------------|------------------------------------------|-----------------|
| Prompt Caching (Provider-Level) | Token-Saving-API-Updates | 6 | Up to 90% input cost reduction | 2 | 5 | 31 |
| Effort Parameter (Adaptive Thinking) | Effort-Parameter-Adaptive-Thinking | 4 | Significant (qualitative); skip thinking on simple tasks | 1 | 5 | 28 |
| Token-Efficient Tool Use | Token-Saving-API-Updates | 3 | Up to 70% output token reduction (avg 14%) | 1 | 5 | 26 |
| Model Routing (Task-Based) | Claude-API-Cost-Optimization | 4 | 60–87% cost reduction | 3 | 5 | 26 |
| Context Editing / Tool Result Clearing | Manage-Tool-Context | 3 | Prevents quadratic context growth | 2 | 5 | 25 |
| Delta Summarization | Compaction-System-Deep-Dive | 3 | Preserves parent token budget (qualitative) | 2 | 5 | 25 |
| Text Editor Tool | Token-Saving-API-Updates | 2 | Reduces output vs full file rewrites | 1 | 5 | 24 |
| Context Window Pruning | Claude-API-Cost-Optimization | 3 | ~40% input token reduction per turn | 3 | 5 | 24 |
| Server-Side Compaction | Context-Windows-Guide | 2 | Enables conversations beyond context limits | 1 | 5 | 24 |
| Circuit Breakers (Iteration/Token Caps) | Agent-Cost-Optimization-Token-Economics | 2 | Prevents runaway costs (qualitative) | 2 | 5 | 23 |
| Automatic Prefix Matching | Token-Saving-API-Updates | 2 | Simplifies caching (enables 90% savings) | 1 | 4 | 21 |
| Extended TTL (1-Hour Cache) | Prompt-Caching-With-Claude | 2 | Prevents cache misses for long subagent tasks | 1 | 4 | 21 |
| Tool Search (On-Demand Discovery) | Manage-Tool-Context | 3 | Large reduction for 20+ tool toolsets | 3 | 4 | 21 |
| Microcompaction (Hot Tail/Cold Storage) | Compaction-System-Deep-Dive | 2 | Reduces tool output bloat | 4 | 5 | 21 |
| Automatic Thinking Block Stripping | Context-Windows-Guide | 2 | Frees context space for reasoning | 1 | 4 | 21 |
| Skill-Based Declarative Routing | Agents-Dont-Need-Sonnet | 1 | Enables optimal model per skill | 2 | 5 | 21 |
| Explicit Cache Breakpoints | Prompt-Caching-With-Claude | 2 | Fine-grained control over cached segments | 2 | 4 | 20 |
| Quality Gates / Validation Scripts | Agents-Dont-Need-Sonnet | 2 | Prevents bad cheap-model outputs | 2 | 4 | 20 |
| Structured Summarization (Checklist) | Compaction-System-Deep-Dive | 1 | Preserves task continuity across compaction | 3 | 5 | 20 |
| Structured Outputs / Output Schema | Token-Efficient-Tool-Use-Migration | 2 | Prevents verbose free-text bloat | 2 | 4 | 20 |
| Context Awareness (Token Budget Tracking) | Context-Windows-Guide | 1 | Prevents mid-task context exhaustion | 1 | 4 | 19 |
| Auto-Compaction (Headroom Accounting) | Compaction-System-Deep-Dive | 2 | Safety net for long sessions | 4 | 4 | 18 |
| Manual Compaction (/compact) | Compaction-System-Deep-Dive | 1 | Frees context at task boundaries | 2 | 4 | 18 |
| Local Model Inference (Ollama) | Agents-Dont-Need-Sonnet | 1 | Zero API cost for mechanical tasks | 3 | 4 | 17 |
| Automatic Escalation (Model Cascade) | Agents-Dont-Need-Sonnet | 2 | Ensures quality while routing cheaply | 3 | 4 | 17 |
| Post-Compaction Rehydration | Compaction-System-Deep-Dive | 1 | Restores working state after compaction | 3 | 4 | 17 |
| LLM FinOps / Cost Observability | Agent-Cost-Optimization-Token-Economics | 1 | Enables data-driven optimization | 3 | 4 | 17 |
| Interleaved Thinking | Token-Efficient-Tool-Use-Migration | 2 | More sophisticated post-tool reasoning | 2 | 3 | 17 |
| Cache-Aware Rate Limits | Token-Saving-API-Updates | 1 | Higher throughput for cached requests | 1 | 3 | 16 |
| Thinking Block Caching | Prompt-Caching-With-Claude | 1 | Saves thinking tokens across tool calls | 1 | 3 | 16 |
| Batch API (Async Processing) | Claude-API-Cost-Optimization | 2 | 50% cost discount | 2 | 2 | 14 |
| Programmatic Tool Calling | Manage-Tool-Context | 1 | Eliminates intermediate roundtrips | 3 | 3 | 14 |
| Semantic Caching (Vector Similarity) | Agent-Cost-Optimization-Token-Economics | 1 | ~31% query elimination | 4 | 3 | 13 |
| Prompt Compression (LLMLingua) | Agent-Cost-Optimization-Token-Economics | 1 | Up to 20x compression | 4 | 3 | 13 |

**Composite Score = (Mention Count × 2) + (Applicability × 3) + (6 - Complexity)**

---

## Top Technique Analysis

### Rank 1: Prompt Caching (Provider-Level) (Composite: 31)
- Why important: Single highest-ROI optimization — reduces input token costs by up to 90% with minimal code changes, applicable to every API call
- Best source: [2025_Anthropic_NA_Prompt-Caching-With-Claude.md](./read-papers/2025_Anthropic_NA_Prompt-Caching-With-Claude.md)
- Reported savings: Up to 90% cost reduction, 85% latency reduction; cache reads at 10% of base input price
- Implementation effort: Low — add `cache_control` field to requests; automatic prefix matching handles the rest

### Rank 2: Effort Parameter (Adaptive Thinking) (Composite: 28)
- Why important: Controls total token spend across text, tool calls, and thinking with a single parameter — directly maps to cost tiers for agentic delegation
- Best source: [2025_Anthropic_NA_Effort-Parameter-Adaptive-Thinking.md](./read-papers/2025_Anthropic_NA_Effort-Parameter-Adaptive-Thinking.md)
- Reported savings: Qualitative "significant token savings" at low effort; skips thinking for simple problems
- Implementation effort: Low — add `effort` parameter to API calls; default should be `medium` for most agentic workflows

### Rank 3: Token-Efficient Tool Use (Composite: 26)
- Why important: Agentic systems are fundamentally tool-call-heavy; reducing output tokens per tool call compounds across every interaction
- Best source: [2025_Anthropic_NA_Token-Saving-API-Updates.md](./read-papers/2025_Anthropic_NA_Token-Saving-API-Updates.md)
- Reported savings: Up to 70% peak output token reduction; 14% average reduction; built-in for Claude 4+
- Implementation effort: Low — built into Claude 4+ models; no action needed for current-gen models

### Rank 4: Model Routing (Task-Based) (Composite: 26)
- Why important: Matching model capability to task complexity avoids paying frontier-model prices for mechanical work — 90% of agent tasks don't need the most capable model
- Best source: [2026_DevTo_NA_Agents-Dont-Need-Sonnet.md](./read-papers/2026_DevTo_NA_Agents-Dont-Need-Sonnet.md)
- Reported savings: 60–87% cost reduction; Haiku is 12x cheaper than Sonnet; frontier models cost up to 190x more than small models
- Implementation effort: Medium — requires task classification, validation gates, and fallback logic

### Rank 5: Context Editing / Tool Result Clearing (Composite: 25)
- Why important: Tool results are the fastest-growing source of context bloat in agentic workflows — stale file reads, bash outputs, and grep results accumulate rapidly
- Best source: [2026_Anthropic_NA_Manage-Tool-Context.md](./read-papers/2026_Anthropic_NA_Manage-Tool-Context.md)
- Reported savings: Prevents quadratic context growth; extends session lifetime
- Implementation effort: Low-Medium — remove old tool_result blocks from conversation history

### Rank 6: Delta Summarization (Composite: 25)
- Why important: Subagent delegation is the primary scaling pattern for agentic workflows — delta summarization keeps parent context lean when children report back
- Best source: [2026_DecodeClaude_NA_Compaction-System-Deep-Dive.md](./read-papers/2026_DecodeClaude_NA_Compaction-System-Deep-Dive.md)
- Reported savings: 1-2 sentence incremental updates vs full state snapshots
- Implementation effort: Low — instruct subagents to return minimal summaries

### Rank 7: Text Editor Tool (Composite: 24)
- Why important: Replaces full file rewrites with targeted edits — prevents massive output token waste in coding assistant workflows
- Best source: [2025_Anthropic_NA_Token-Saving-API-Updates.md](./read-papers/2025_Anthropic_NA_Token-Saving-API-Updates.md)
- Reported savings: Massive output token reduction vs full file rewrites
- Implementation effort: Low — provide text_editor tool in API requests

### Rank 8: Context Window Pruning (Composite: 24)
- Why important: Without pruning, full conversation history resent every turn causes 128K context to cost 64x more than 8K context
- Best source: [2025_DevTo_NA_Claude-API-Cost-Optimization.md](./read-papers/2025_DevTo_NA_Claude-API-Cost-Optimization.md)
- Reported savings: ~40% reduction in input tokens per turn
- Implementation effort: Medium — requires summarization logic and message management

### Rank 9: Server-Side Compaction (Composite: 24)
- Why important: Enables conversations to continue beyond context window limits without manual intervention — critical for long-running coding sessions
- Best source: [2025_Anthropic_NA_Context-Windows-Guide.md](./read-papers/2025_Anthropic_NA_Context-Windows-Guide.md)
- Reported savings: Extends session lifetime indefinitely
- Implementation effort: Low — built-in beta feature for Opus 4.6/Sonnet 4.6

### Rank 10: Circuit Breakers (Composite: 23)
- Why important: Without guardrails, stuck reasoning loops run indefinitely — a single runaway agent task can cost $5–8 in API fees
- Best source: [2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md](./read-papers/2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md)
- Reported savings: Prevents catastrophic spend from stuck loops
- Implementation effort: Low — add max iteration caps and per-trace token budgets
