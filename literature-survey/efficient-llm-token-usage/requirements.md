Date: 2026-04-12
Topic: Efficient LLM Token Usage for Agentic Workflows

# Efficient LLM Token Usage for Agentic Workflows - Survey Requirements

## Request

Survey of tech blog articles (not academic papers) covering best practices, techniques, and strategies for using LLM tokens efficiently and effectively — with a focus on Claude/Anthropic but including general LLM optimization techniques. Limited to at most 10 of the most relevant articles. Results will be applied to the user's own agentic workflow system.

## Core Keywords

- Claude token optimization
- LLM prompt efficiency
- Context window management
- Prompt caching (Anthropic)
- Token cost reduction LLM
- Agentic workflow token usage
- LLM API cost optimization

## Target Conferences / Journals

N/A — this survey focuses exclusively on tech blogs and engineering posts.

## Target Engineering Blogs

Primary (Anthropic/Claude-specific):
- docs.anthropic.com (official documentation and guides)
- anthropic.com/research and anthropic.com/news
- Anthropic cookbook / developer guides

Secondary (general LLM optimization, applicable to Claude):
- openai.com/blog (token optimization patterns transfer across providers)
- huggingface.co/blog
- wandb.ai/fully-connected
- engineering blogs from companies using LLMs at scale (Stripe, Shopify, etc.)
- Simon Willison's blog (simonwillison.net) — prominent LLM practitioner
- Latent Space blog / podcast

Tertiary (community / practitioner posts):
- Medium / Substack posts from LLM practitioners
- dev.to, hashnode posts on Claude/LLM optimization

## Search Query List

1. "Claude token optimization" best practices
2. "prompt caching" Anthropic Claude
3. LLM token efficiency agentic workflows
4. "context window" management Claude tips
5. reduce Claude API cost techniques
6. Anthropic Claude prompt engineering efficiency
7. LLM agent token budget optimization
8. "extended thinking" Claude token usage
9. Claude batch API cost optimization
10. efficient tool use Claude tokens

## Survey Scope and Constraints

- Target number of articles: 10 (hard cap)
- Source type: tech blogs and engineering posts only (no academic papers)
- Year range: 2023–2026 (Claude era)
- Must include:
  - Anthropic's official guidance on token efficiency
  - Prompt caching techniques
  - Context window management strategies
  - Agentic/tool-use token patterns
- Exclude:
  - Academic papers
  - Generic "intro to Claude" posts without optimization content
  - Marketing/sales content
  - Paywalled content
- Adjacent-field expansion: general LLM optimization (OpenAI, open-source) if Claude-specific coverage is thin

## Project Context

This survey supports a personal agentic workflow system built around Claude (managed in ~/.claude/ with skills, agents, and rules). The goal is to build a knowledge base project on efficient token usage so that findings can be directly applied to improve how the agentic system operates — reducing waste, improving response quality per token spent, and making better architectural decisions about when to delegate to subagents, how to structure prompts, when to use caching, and how to manage context windows in multi-turn agent sessions.

"Relevant" means: a technique or insight that can be concretely applied to reduce token cost or improve output quality in an agentic coding assistant workflow. Especially valuable are articles covering:
- Prompt structure patterns that reduce tokens without losing quality
- Caching strategies for repeated tool/skill invocations
- Context window management in long agent sessions
- Cost-effective delegation patterns (when to use cheaper/faster models)
- Batching and prefilling techniques

## Summary of Actual Search Results

- Total articles: 10
- Number of categories: 3 (Caching and Cost Reduction Strategies; Model Routing and Output Optimization; Context Window Management and Compaction)
- Sources: Anthropic official docs/blog (6), DEV Community (2), Decode Claude (1), Zylos Research (1)
- Techniques catalogued: 34 distinct techniques across all articles
- Key findings: Provider-level prompt caching is the single highest-ROI optimization (up to 90% input cost reduction with minimal code changes), followed by model routing (60–87% total cost reduction by matching task complexity to model capability) and context compaction/pruning (~40% per-turn savings). Combined, these techniques deliver 60–80% total cost reduction. The effort parameter and built-in token-efficient tool use provide additional low-effort output token savings. For the target agentic system (~/.claude/), the optimal implementation order is: (1) enable prompt caching + set effort parameter + add circuit breakers, (2) implement 3-tier model routing with quality gates, (3) build context editing and microcompaction, (4) deploy cost observability.
