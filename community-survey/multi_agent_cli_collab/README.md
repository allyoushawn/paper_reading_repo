# Community Survey Topic — Multi-Agent CLI Collaboration (Claude Code + Codex + Gemini CLI)

**Created:** 2026-04-19

## Why tracked

Actively building a personal multi-agent setup combining Claude Code (lead),
OpenAI Codex CLI, and Google Gemini CLI. Want to learn from what others are
doing AND build longitudinal signal on how this fast-moving space evolves.

## Audience

Self only — informal working notes; no need to polish for external readers.

## Lens

Evaluating concrete patterns and tools to adopt for my own Claude+Codex+Gemini
setup — emphasis on (a) how agents share state/memory/context across separate
CLI sessions, (b) which orchestration patterns are battle-tested vs. speculative,
and (c) what infrastructure (MCP servers, file conventions, daemons) is worth
the build cost.

## Working assumptions (project context as of 2026-04-19)

- Claude Code is the default lead. Codex and Gemini are consultants/workers.
- Hybrid trigger model: Claude decides when to invoke Codex/Gemini, with human override.
- Open to all sync substrates (files, git, daemon, MCP) — comparing trade-offs.
- Six identified sync subproblems: intent, progress, context, locking, conflict
  resolution, cross-session memory.
