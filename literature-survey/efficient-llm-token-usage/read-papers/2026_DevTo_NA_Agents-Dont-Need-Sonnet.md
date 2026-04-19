# Article Analysis: Most of your Claude Code agents don't need Sonnet

**Source:** https://dev.to/edwardkubiak/most-of-your-claude-code-agents-dont-need-sonnet-4587
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Most of your Claude Code agents don't need Sonnet
**Author/Publisher:** Edward Kubiak on DEV Community
**Published:** ~April 2026

**Key contributions:**
- Demonstrates that default Claude Code setup wastes money by running all agents on the same expensive model
- Proposes a 3-tier model routing strategy: Sonnet (reasoning) → Haiku (pattern-matching) → Ollama (mechanical, local)
- Includes a validation gate + automatic escalation mechanism to ensure quality while routing cheaply
- Open-sourced as the CAST framework (castframework.dev, claude-agent-team, cast-hooks)

**Core techniques described:**
- **Tier 3 (Sonnet):** Reserved for deep reasoning — planning, debugging, security review, complex multi-file implementation. "Cost of a wrong answer exceeds cost of the API call."
- **Tier 2 (Haiku):** Workhorse for pattern-matching tasks — code review against checklists, test running, commit messages, docs, DevOps config, git operations. 12x cheaper than Sonnet.
- **Tier 1 (Ollama):** Local models on Apple Silicon for highly mechanical, high-frequency tasks. The `tavernari/git-commit-message` 8B model processes at 40+ tokens/sec with zero API cost.
- **Quality Gate / Validation Script:** Intercepts cheaper model outputs, checks for empty output, hallucination markers ("As an AI"), length bounds, format compliance.
- **Automatic Escalation:** Failed validation → escalate Ollama→Haiku→Sonnet. Every escalation logged for analysis.
- **Skill-based declarative routing:** Each skill declares minimum-viable model in metadata (referenced from tokrepo.com comment).

**Quantitative results:**
- **Cost comparison:** Haiku at $0.25/1M input vs Sonnet at $3/1M = **12x price difference**
- **Daily cost:** 50 agent calls/day: ~$0.37/day (tiered) vs ~$0.90/day (all Sonnet) = **up to 60% reduction**
- **Local performance:** Ollama at 40+ tokens/sec on Apple Silicon, zero API cost, zero network latency
- **Latency:** Local Ollama has no network round-trip — "feels instant" for frequent tasks

---

## 2. Implementation Details

- **Agent Configuration:** Audit agent calls; identify "structured input → structured output" tasks; change model assignment to Haiku (one config change per agent).
- **Local Ollama Setup:** Install Ollama with purpose-built models (e.g., `tavernari/git-commit-message` 8B) running on Apple Silicon.
- **Validation Script:** Intercept model output; check for: empty output, hallucination markers, length bounds (too short/too long), format compliance (e.g., commit message imperative mood).
- **Fallback Escalation:** Configure `fallback_models` setting; failed validation → auto-escalate Ollama→Haiku→Sonnet; log every escalation.
- **Framework:** LiteLLM for model configuration; CAST framework (`claude-agent-team` + `cast-hooks`) provides agent definitions and validator scripts.

---

## 3. Limitations and Caveats

- **Context Window Constraints:** Local models (7B/8B) degrade rapidly past 8K context — keep them on short-context tasks only
- **Tasks that MUST stay on Sonnet:** Security analysis (small models miss subtle vulns), root cause debugging (7B models generate plausible but wrong hypotheses), planning/task decomposition (requires full codebase context), complex code generation (subtle bugs pass review but fail at runtime)
- **Validation Required:** Routing to cheap models is only safe with a reliable quality gate — without it, bad outputs can corrupt the codebase
- **Rule of thumb:** "If the cost of a wrong answer is 'I regenerate it,' route it cheap. If the cost is 'I debug it for an hour,' keep it on Sonnet."

---

## 4. Related Techniques

- **Ollama:** Local model runtime for Tier 1 inference on Apple Silicon
- **LiteLLM:** Model configuration and routing framework
- **CAST Framework:** Open-source framework for Claude Code agent management (castframework.dev)
- **Skill-based declarative routing (tokrepo.com):** Skills declare minimum-viable model in metadata for deterministic routing
- **Claude Code agent system:** Primary framework being optimized (subagent spinning for code review, testing, commits, debugging)

---

## 5. Project Relevance

**(a) Directly applicable techniques:**
- **3-tier model routing** maps directly to current system: Sonnet for orchestration/planning, Haiku for exploration/reading subagents, Ollama for commit messages and log summaries
- **Skill-based declarative routing** — each skill in `~/.claude/skills/` could declare its minimum-viable model in metadata
- **Quality gates** — validation scripts prevent bad subagent outputs from corrupting the codebase

**(b) Interaction with subagent delegation:**
- Parent orchestrator (Sonnet) spawns Haiku child agents for mechanical tasks, isolating their token usage
- Automatic escalation ensures child agents that fail get transparently retried on a more capable model before returning to parent
- Subagent isolation means Haiku/Ollama children can run multi-turn loops without polluting parent context with expensive Sonnet tokens

**(c) Implementation priority:**
1. **Drop structured tasks to Haiku** — one config change per agent, immediate 12x cost reduction on those tasks
2. **Add validation gate** — never let cheap model output flow unchecked into codebase
3. **Implement local Ollama routing** — zero cost for high-frequency mechanical tasks (commit messages easiest starting point)

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Article | Section | Summary of Mention |
|-------------------|---------|-------------------|
| 2026_Zylos_NA_Agent-Cost-Optimization-Token-Economics.md | Model Routing and Cascading | Describes model routing and cascading at framework level; cites 87% cost reduction and 90% queries handled by smaller models |

---

## Meta Information

**Publisher:** DEV Community
**Year:** 2026
**Type:** Tech blog
**Relevance:** Core
**Priority:** 2
