# Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method

- **Source index:** 114
- **Source ID:** `0e509aae-d04d-49d7-bfff-1f6322a88e31`
- **Model identifier:** codex-sol
- **Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)
- **Authors:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu
- **Year / venue:** 2024 / KDD
- **Direction / priority:** D8 reciprocal recommendation / Priority 3 (core)
- **URL:** https://arxiv.org/abs/2408.09748

## 1. Summary

The paper argues that evaluating each side of a reciprocal recommender with conventional ranking metrics misses the joint nature of a match. It introduces five metrics spanning overall coverage, bilateral stability, and balanced ranking. It then formulates recommendations as bilateral interventions in a potential-outcomes framework, proposes a model-agnostic causal reciprocal recommendation method, and adds reranking to maximize matching outcomes under the proposed metrics.

The indexed NotebookLM source contains the arXiv abstract rather than the paper body. It states that experiments on real recruitment and dating datasets support the metrics and approach, but dataset names, sample sizes, baselines, effect sizes, uncertainty, and ablations are **Not specified in source**. No quantitative claim is made here beyond that abstract-level statement.

## 2. Experiment Critique

The conceptual evaluation shift is well motivated: a match depends on both lists and both responses, so two independent NDCG values are insufficient. A causal formulation is also directionally appropriate for deciding whom to expose.

The available indexed content is insufficient to audit identification assumptions, treatment definition, propensity support, leakage, evaluation protocol, or results. “Bilateral intervention” may still face interference because recommending one person changes attention available to others. Offline real-data gains do not by themselves establish online incremental matches. These points require verification from the full paper before implementation.

## 3. Industry Contribution / Project Relevance

The five-metric framing is a useful checklist for the dating project: coverage guards against opportunity collapse, stability checks mutual compatibility, and balance prevents one side’s gains from hiding the other side’s losses. Treating exposure as an intervention aligns with the requirement to optimize incremental long-term value rather than predicted affinity.

However, the target system needs delayed retention/revenue, candidate congestion, and market-level interference. The abstract does not show that CRRS handles these. Use it as a metric and causal-reranking reference, then validate with randomized exposure and two-sided long-horizon outcomes.

## 4. Novelty

The stated novelty is a unified package of reciprocal-system metrics, bilateral potential-outcome formulation, model-agnostic causal scoring, and matching-oriented reranking.

## 5. Dataset Availability

The abstract reports one recruitment and one dating dataset. Names and licenses are **Not specified in source**. Code and dataset are linked at https://github.com/RUCAIBox/CRRS.

## 6. Community Reaction

Not specified in source beyond KDD 2024 publication.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## 8. Meta Information

- **Source-content completeness:** Abstract/metadata only
- **Method family:** Causal reciprocal recommendation and reranking
- **Evaluation dimensions:** Coverage, bilateral stability, balanced ranking
- **Quantitative results:** Not specified in source
- **Interference treatment:** Not auditable from indexed content
- **Project role:** Joint evaluation and causal-reranking reference
