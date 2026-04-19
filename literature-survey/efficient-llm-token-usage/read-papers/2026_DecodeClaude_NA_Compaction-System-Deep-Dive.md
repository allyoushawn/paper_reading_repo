# Article Analysis: Inside Claude Code's Compaction System

**Source:** https://decodeclaude.com/compaction-deep-dive/
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Inside Claude Code's Compaction System
**Author/Publisher:** Decode Claude
**Published:** January 21, 2026

**Key contributions:**
- Reverse-engineered Claude Code's three-layer compaction system from a shipped bundle
- Detailed the complete compaction pipeline: microcompaction → auto-compaction → manual compaction
- Introduced the concept of structured summarization as a "compaction contract" with checklist-style prompts
- Documented post-compaction rehydration: restoring recent files, todos, and continuation instructions
- Explained delta summarization for background/subagent task tracking

**Core techniques described:**
- **Microcompaction:** Splits tool outputs into "hot tail" (recent, fully visible) and "cold storage" (older, saved to disk with reference path). Applies to: Read, Bash, Grep, Glob, WebSearch, WebFetch, Edit, Write.
- **Auto-Compaction:** Driven by headroom accounting — reserves "output headroom" (space to finish response) and "compaction headroom" (space to run summarization). Triggers when free space drops below reserved thresholds.
- **Manual Compaction:** User-facing `/compact` trigger at natural task boundaries. Supports "focus hints" to ensure critical details survive summarization.
- **Structured Summarization:** Checklist-style prompt capturing: user intent, technical decisions, files touched, errors encountered, pending tasks, next steps. Not open-ended "summarize this."
- **Post-Compaction Rehydration:** Boundary marker → summary message → re-read 5 most recent files → restore todo/plan state → continuation instruction.
- **Delta Summarization:** For background/subagent contexts — 1-2 sentence incremental updates rather than full working state snapshots.

**Quantitative results:**
Not specified in source. The article focuses entirely on architectural design and operational mechanics rather than benchmark metrics. Re-reads the 5 most recently accessed files as a specific operational rule.

---

## 2. Implementation Details

- **Microcompaction:** Implement as cache policy + persistence format. Define: how many recent results to keep inline, what size triggers offloading, and a stable serialization format with enough metadata to interpret later.
- **Auto-Compaction:** Configure headroom thresholds: output headroom (so responses don't get truncated) and compaction headroom (so summarization doesn't fail mid-flight). Don't compact tiny sessions. Re-check periodically based on session growth rate.
- **Structured Compaction Prompt:** Provide model with checklist-style summarization job. Must document: user intent, technical decisions, files touched, errors, pending tasks, next steps. Project-level focus hints can be appended.
- **Rehydration Sequence:** After summarization: inject boundary marker → summary message → re-read 5 most recently accessed files → restore todo list → restore plan state → inject continuation message.
- **Tuning Knobs:** Output headroom reservation, auto-compaction threshold (percent or "minimum free space"), microcompaction policy (tool result budgets + hot tail size), manual compaction affordance (command/API/UI).

---

## 3. Limitations and Caveats

- **Tiny Sessions:** Auto-compaction avoids compacting sessions that are too small to be worth it
- **Periodic Checks:** Headroom calculation is not per-token but on a cadence based on session growth rate — may miss rapid bursts
- **Background Agents:** Full compaction is too heavy; delta summarization (1-2 sentence incremental updates) used instead
- **Truncation is lossy:** Simple truncation loses information entirely
- **Standard summarization loses detail:** Compaction goes beyond basic summarization by adding structured restoration

---

## 4. Related Techniques

- **Subagents (Task tool):** Heavy exploration in isolated contexts keeps main conversation clean
- **Delta Summarization:** Incremental 1-2 sentence updates for background agent progress tracking
- **CLI Commands:** `/compact` (manual compaction), `/clear` (reset context), `/context` (monitor space usage)
- **MCP Servers:** External integrations that consume context space — should be monitored/disabled when unused
- **Related architectures:** Context window ops, session memory, telemetry-first architecture

---

## 5. Project Relevance

**(a) Directly applicable techniques:**
- **Microcompaction** solves the biggest source of token waste in coding agents — bulky tool outputs from file reads, bash commands, grep results
- **Auto-compaction with headroom accounting** prevents sessions from crashing when approaching limits
- **Structured summarization** preserves task intent and continuity across long coding sessions
- **Context clearing between unrelated tasks** prevents pollution of one task's context into another

**(b) Interaction with subagent delegation:**
- **Isolated contexts:** Child agents run in completely separate context, preventing tool output bloat from polluting parent
- **Delta summarization:** Subagents report back with 1-2 sentence incremental updates instead of full state snapshots — preserves parent's token budget
- **Subagents for exploration:** Heavy code exploration happens in separate context, keeping main conversation clean

**(c) Implementation priority:**
1. **Microcompaction** — address the immediate bloat from bulky tool outputs (file reads, bash results). Implement as cache policy + persistence format.
2. **Manual compaction affordance** — `/compact` at task boundaries. Simpler to implement than auto-compaction; best practice to compact when context is clean.
3. **Auto-compaction** — add as safety net after microcompaction and manual triggers are in place. Requires headroom accounting logic.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2025_Anthropic_NA_Context-Windows-Guide.md | Managing context with compaction | Introduces server-side compaction as the recommended approach; this article reverse-engineers the full implementation |
| 2026_Anthropic_NA_Token-Efficient-Tool-Use-Migration.md | Subagent delegation | Recommends delta summarization for child agent context isolation; concept detailed in this article |
| 2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md | Implementation priority & Subagent delegation | References advanced context compaction as third-priority technique; cites delta summarization for subagent reporting |

---

## Meta Information

**Publisher:** Decode Claude
**Year:** 2026
**Type:** Tech blog (reverse engineering analysis)
**Relevance:** Core
**Priority:** 1
