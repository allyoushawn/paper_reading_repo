# Our Agent Design — Audit Against the Survey

**Date:** 2026-04-19
**Subject:** `~/.claude/` setup (CLAUDE.md, 11 subagents, 18 skills, 1 hook, KB integration)
**Source notebook:** `23a9e735-8ad9-4d86-af53-5a1bb353e537` (40 first-party Anthropic/OpenAI/Google sources)
**Method:** Two targeted NLM queries extracting concrete if-then rules; map each rule against current config; classify compliance; rank action items by leverage.

---

## Existing Strengths (do not change)

These are rules from the sources where our setup is already aligned — explicitly noting them so we don't accidentally regress.

| Rule (source) | Our compliance |
|---|---|
| **Hooks for actions that must happen every time** (Anthropic Best Practices) | `kb-update-reminder.sh` PostToolUse hook on writes to `.claude/skills/`, `.claude/agents/` — already documented in `agent-design-principles.md` as the 4th enforcement layer. |
| **Circuit breakers for agent loops** (Google ADK + Anthropic) — explicit max-iter, replan escape, plateau detection, no silent recovery on retry 3+ | Encoded in CLAUDE.md "Circuit Breakers" section verbatim. |
| **Subagents for broad investigation to protect lead context** (Anthropic Claude Code Best Practices) | `reading-agent` + tiered file-size delegation rules in CLAUDE.md. `kb-retriever` enforces same pattern for KB reads. |
| **Static routing easy → cheap, hard → capable** (Anthropic Building Effective Agents) | Per-agent model routing table in CLAUDE.md + rationale in `agent-design-principles.md`. |
| **CLAUDE.md length within target** (Anthropic guidance: 150-200 lines) | 166 lines. Well within range. |
| **Skill descriptions state both what AND when** (Anthropic Skill authoring) | All 18 skills have explicit "Use when..." triggers. |
| **External durable session log outside context** (Anthropic Managed Agents) | KB approximates this for long-horizon project state — `log.md` per project, Compiled Truth README, `agents-failure.md`. |
| **Failure ledger as feedback loop** (matches Anthropic's eval-from-real-failures recommendation) | `document-agent-failure` skill + `agents-failure.md` ledger; three-strike threshold. |
| **Lazy / progressive disclosure of skills** (Anthropic 3-level + OpenAI container-loaded skills) | Built into Claude Code skill auto-discovery (metadata only loaded; full SKILL.md on trigger). |
| **Anti-pattern guard: infinite exploration** (Anthropic Best Practices) | reading-agent + kb-retriever pre-search + scope-narrowing in CLAUDE.md. |

---

## Action Items (by leverage)

### TIER 1 — High leverage, low cost (do these first)

#### A1. Add a dynamic subagent-count scaling rule to CLAUDE.md
- **Source rule:** "Use 1 agent for simple fact-finding, 2-4 subagents for direct comparisons, 10+ subagents for complex research." (Anthropic, *How we built our multi-agent research system*)
- **Current state:** No explicit guidance on how many subagents to spawn for a given task class. We default to 1 unless a skill says otherwise.
- **Concrete change:** Add to CLAUDE.md under "Delegate Non-Trivial Editing to Subagent" a small subsection:
  > **Subagent count scaling:** 1 subagent for fact-finding/single-file extraction; 2-4 for comparisons or parallel sub-investigations of the same artifact; 10+ only for genuinely independent research tracks. Default is 1.
- **Why high leverage:** Currently when a task could benefit from parallelism (e.g., comparing 3 designs, surveying 5 KB folders), we tend to do it serially. Explicit guidance + lead awareness will unlock latency wins at near-zero cost.

#### A2. Codify the subagent brief recipe (objective + output-format + tool-guidance + boundaries)
- **Source rule:** "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries. Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information." (Anthropic, multi-agent research system)
- **Current state:** CLAUDE.md "Subagent Output Protocol" section already requires `Return only: [schema/sentence]` (output format ✓). But objective / tool-guidance / boundaries are not explicitly required in briefs — they're implicit when we remember.
- **Concrete change:** Expand the "Delegate Non-Trivial Editing to Subagent" recipe in CLAUDE.md from the current "self-contained brief … exact file paths, line numbers, what to change, why, and any constraints" to an explicit four-part template:
  1. **Objective** (one sentence: what must be true when you finish)
  2. **Tool/source guidance** (which files/tools to use; which to avoid)
  3. **Boundaries** (what is NOT in scope; when to stop and surface)
  4. **Output format** (the existing `Return only:` directive)
- **Why high leverage:** We already encode 1 of 4 (output format). Adding the other 3 is a one-paragraph CLAUDE.md edit and prevents the named failure modes (duplicate work, gaps, missed info).

#### A3. Add a "subagent writes to filesystem; lead reads reference" rule for large outputs
- **Source rule:** "Subagents call tools to store their work in external systems, then pass lightweight references back to the coordinator. This prevents information loss during multi-stage processing and reduces token overhead." (Anthropic, multi-agent research system)
- **Current state:** Used informally — experiment-scribe writes notebooks; kb-organizer writes README.md; but the lead-→-subagent contract for "large output" doesn't require this.
- **Concrete change:** Add to CLAUDE.md "Subagent Output Protocol":
  > **Large outputs:** If the subagent's deliverable is >500 tokens of structured content (code diffs, full notes, datasets), the brief must instruct the subagent to write the artifact to a named file path and return only the path + 1-line confirmation. Never have the subagent return the full content as text.
- **Why high leverage:** Today, when reading-agent or knowledge-base-house-keeper produce long structured reports, those reports flood the lead context. A path + summary returns the same information for a fraction of the token cost.

#### A4. Rename `knowledge-base-house-keeper` → `kb-house-keeper` (namespace consistency)
- **Source rule:** "Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools … help agents select the right tools at the right time." (Anthropic, *Writing effective tools for AI agents*)
- **Current state:** Three KB agents use `kb-*` prefix (`kb-librarian`, `kb-retriever`, `kb-organizer`); one breaks the convention (`knowledge-base-house-keeper`). At routing time, the lead has to do extra work to associate the longer name with the same family.
- **Concrete change:** Rename → `kb-house-keeper`. Update references in: the agent file itself, `kb-sweep` skill (`/Users/fox/.claude/skills/kb-sweep/SKILL.md`), `agent-design-principles.md`, and any KB log entries.
- **Cost / risk:** ~5 file edits, all controllable. No runtime breakage (agent name is a string lookup).
- **Why high leverage:** Cheap, immediately reduces routing ambiguity, brings the KB-family to clean `kb-*` namespacing matching the Anthropic recommendation.

#### A5. Convert agent-failure ledger entries into the seed eval suite
- **Source rule:** "20-50 simple tasks drawn from real failures is a great start. … Evals get harder to build the longer you wait." (Anthropic, *Demystifying evals for AI agents*)
- **Current state:** `document-agent-failure` skill captures failures in `agents-failure.md`. Each entry is implicitly a regression candidate but is not tagged or formatted as a test case.
- **Concrete change:** Extend the `document-agent-failure` ledger schema with one optional field per entry:
  > `repro:` — minimal prompt + expected behavior (or expected refusal). One paragraph. Add when the failure has a clean repro; skip otherwise.
- Then later, when count → 3 triggers a fix, you have the test case ready to verify the fix worked. This costs ~30 seconds per logged entry and yields a real eval suite over months.
- **Why high leverage:** Closes the loop on the failure ledger — turns "we noticed this 3 times" into "we have 3 verifiable test cases for the fix". Aligns with the explicit Anthropic recommendation to start eval suites with 20-50 real-failure tasks.

### TIER 2 — Medium leverage, modest cost

#### B1. Define a 3-tier risk gate framework (extending the deletion-confirmation rule)
- **Source rule:** "Risk-rate each tool (low/med/high) by read vs write, reversibility, perms, financial impact; trigger guardrail check or human escalation for high-risk." (OpenAI, *A practical guide to building agents*)
- **Current state:** Only deletion is gated (the always-applied `confirm-file-deletion.mdc` rule). Other irreversible actions — `git push`, modifying skills/agents/CLAUDE.md, modifying memory items — are not consistently gated.
- **Concrete change:** Document a tier framework as a new section in `agent-design-principles.md`:
  - **HIGH (require explicit confirmation each time):** delete file, `git push --force`, modify hook scripts, modify CLAUDE.md, modify any agent definition, push to remote, write to `~/.claude/run-*-mcp.sh`.
  - **MEDIUM (require confirmation if user hasn't shown intent in current turn):** create/delete skill, create/delete agent, create file in `~/.claude/`, normal `git push`.
  - **LOW (proceed unless explicitly forbidden):** edit existing KB note, edit existing project file, run read-only commands.
  - Then surface the HIGH list as a short paragraph in CLAUDE.md (not the full table — too long; keep table in KB).
- **Why medium-not-high:** The biggest risk action (deletion) is already covered. This is incremental hardening. Useful but not urgent.

#### B2. Audit the 3 thinnest agent descriptions for "what + when" crispness
- **Source rule:** "Description includes both what the Skill does and when to use it." (Anthropic, *Skill authoring best practices*)
- **Current state:** Most agents have crisp descriptions. Three to verify:
  - `experiment-runtime` — has when (`Use after code-change or when execution_route is runtime_only`) ✓
  - `experiment-scribe` — short; verify
  - `experiment-code-change` — verify
- **Concrete change:** Read the three short descriptions; if any lack a clear "Use when…" trigger, add one. ~15 minutes total.
- **Why medium:** Routing ambiguity costs are real but small for our current scale (11 agents).

#### B3. Add a verification clause to the subagent-edit brief template
- **Source rule:** "Always provide verification (tests, scripts, screenshots). If you can't verify it, don't ship it." (Anthropic, Best Practices for Claude Code — anti-pattern: trust-then-verify gap)
- **Current state:** Our brief template ends with "Return only: one sentence confirming the edit was made, or a one-line error description." This confirms but does not verify.
- **Concrete change:** Strengthen to:
  > "Return only: [one-sentence confirmation] AND [one-line verification result — relevant lint output, test result, or '`<no test applicable>`'] OR a one-line error description."
- **Why medium:** Catches a class of failures (subagent claims success on uncompilable code) but adds slight friction for trivial edits where verification is overkill. Probably worth it.

### TIER 3 — Low leverage, defer or skip

| Item | Why deferred |
|---|---|
| Adopt OpenAI Responses API encrypted reasoning items / Gemini Thought Signatures | We use Claude Code natively, not the API. Not applicable. |
| Adopt Programmatic Tool Calling | No raw-data-aggregation workload in our current setup. Solution looking for a problem. |
| Adopt OpenAI shell tool / hosted containers | We have a real shell. Not applicable. |
| Migrate to Agent Builder / ADK | Same — Claude Code is our runtime. |
| Switch to A2A protocol for cross-framework agent calls | Single-framework setup (all subagents are Claude Code agents). No interop need. |
| Lazy tool search (defer_loading) | Handled automatically by Claude Code skill auto-discovery. No action needed. |
| Compute pass@k / pass^k | Premature without a programmatic eval harness. Tier-1 item A5 builds the precursor. |

---

## Things I Considered and Decided NOT to Do

1. **Prune CLAUDE.md.** Considered moving the per-agent model-routing rationale to KB. Decided against: the table in CLAUDE.md is concise and the rationale is in `agent-design-principles.md` already. Current state is correctly factored.

2. **Split the experiment-* family further.** Considered creating an explicit "experiment orchestrator" subagent. Decided against: the lead currently orchestrates the 6 experiment-* agents and that's working. Adding an orchestrator would add latency without clear quality gain. Revisit if the lead starts dropping experiment-pipeline rules.

3. **Add a "/clear between unrelated tasks" rule to CLAUDE.md.** Considered after the survey's "kitchen sink session" anti-pattern. Decided against: this is user discipline, not agent behavior — adding it to CLAUDE.md wouldn't change agent behavior, and would consume a CLAUDE.md line for low value.

4. **Memory directory.** `~/.claude/memory/` doesn't physically exist, but `agent-design-principles.md` and `claude-workflow.md` reference it. Verified: this is intentional — memory items have not been needed yet because CLAUDE.md serves the same enforcement role at our scale (per the agent-design-principles documented framework). No action.

---

## Citations

All if-then rules in this audit trace to the NotebookLM notebook `23a9e735-8ad9-4d86-af53-5a1bb353e537`, conversation `91161892-e254-490e-8c1e-baa11e59023e`, queries dated 2026-04-19. Specific source titles named in each rule above.
