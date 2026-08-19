# Matching Theory-based Recommender Systems in Online Dating

- **Source index:** 117
- **Source ID:** `f842d07a-9922-43b0-8909-5665c54cd553`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Yoji Tomita, Riku Togashi, Daisuke Moriwaki
- **Year / venue:** 2022 / RecSys Industrial Talk Poster
- **Direction / priority:** D8 reciprocal recommendation / Priority 3 (core)
- **URL:** https://arxiv.org/abs/2208.11384

## 1. Summary

This short industrial-poster source positions online dating recommendation as an interaction between reciprocal recommender systems and matching theory. It reports an ongoing project to deploy a matching-theory-based recommender system (MTRS) on a real online dating platform. The basic motivation is that users are agents on both sides, so successful recommendation depends on bilateral preference and allocation, not one-sided relevance.

The indexed NotebookLM content is only the arXiv metadata and abstract. Algorithm details, objective equations, platform identity, sample size, offline metrics, deployment design, and results are **Not specified in source**. It therefore provides evidence of industrial intent and problem framing, not evidence of effectiveness.

## 2. Experiment Critique

The industrial setting and explicit planned deployment make the work relevant, and matching theory is a principled response to reciprocal capacity and congestion.

No experiment can be critiqued from the indexed source because none is described. “Ongoing project” should not be interpreted as a completed launch or positive result. The source gives no causal design, uncertainty, downstream outcomes, fairness analysis, or computational assessment. Any use beyond background requires the full poster/paper or subsequent deployment publication.

## 3. Industry Contribution / Project Relevance

The paper is direct evidence that production dating teams have explored replacing independent pair scoring with a market-level matching layer. This supports treating recommendation allocation—not just affinity prediction—as a core system component.

For the unified LTV project, the source does not specify how matching-theoretic allocations connect to retention, revenue, delayed labels, or the success paradox. It should serve as lineage for later CyberAgent/Tomita work, not as an implementation recipe.

## 4. Novelty

At abstract level, the stated novelty is an industrial effort to connect matching theory and reciprocal recommendation for real online dating deployment. Further novelty is **Not specified in source**.

## 5. Dataset Availability

A real dating platform is mentioned, but data details and public availability are **Not specified in source**. Code is **Not specified in source**.

## 6. Community Reaction

Accepted as a RecSys 2022 Industrial Talk Poster; further reaction is **Not specified in source**.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Source-content completeness:** Abstract/metadata only
- **Domain:** Online dating
- **Method family:** Matching-theory-based reciprocal recommendation
- **Deployment status:** Described as ongoing in 2022
- **Quantitative evidence:** Not specified in source
- **Project role:** Industrial lineage and framing
