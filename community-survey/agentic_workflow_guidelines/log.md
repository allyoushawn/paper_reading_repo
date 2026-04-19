# Log — Agentic Workflow Guidelines

## 2026-04-19 — community-survey-nlm run (full)
- Lens: Extract canonical, actionable design principles and patterns I can apply when building agents — emphasizing what each lab explicitly recommends (and warns against) for tool use, planning, evaluation, and safety in agentic workflows.
- Time window: Last 12 months (Anthropic Dec 2024 foundational post retained as out-of-window canonical reference)
- Scope: ONLY first-party Anthropic / OpenAI / Google-Gemini-DeepMind sources (HN, ProductHunt, Medium, X, Quora explicitly excluded per user constraint)
- Sources scanned: Anthropic(12), OpenAI(11), Google/Gemini/DeepMind(10) = 33 first-party sources
- Sources added to NLM notebook: 40 (33 URL + README ingested as text + 6 OpenAI URLs rescued via WebFetch and re-ingested as text after Cloudflare blocked direct ingestion)
- Output: community_survey_20260419.md
- Trajectory: Strong cross-lab convergence in 2025–26 on (a) decoupled sandboxed runtimes, (b) reasoning-state preservation across turns (OpenAI encrypted reasoning items ≅ Gemini Thought Signatures), (c) progressive/lazy loading of tools and skills (Anthropic 3-level + OpenAI container-loaded skills + ADK Workflow Agents). Persistent open problem: long-horizon context management is fundamentally lossy.
