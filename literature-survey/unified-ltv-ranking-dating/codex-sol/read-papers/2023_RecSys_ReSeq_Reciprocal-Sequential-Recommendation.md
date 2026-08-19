# Paper Analysis: Reciprocal Sequential Recommendation

**Source:** https://arxiv.org/abs/2306.14712  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Reciprocal Sequential Recommendation  
**Authors:** Bowen Zheng; Yupeng Hou; Wayne Xin Zhao; Yang Song; Hengshu Zhu  
**Abstract:** ReSeq formulates reciprocal recommendation as bilateral sequence matching, capturing how both parties' active and passive preferences evolve rather than using static user representations.  
**Methodology:** Transformers encode each user's chronological behavior under active-selector and passive-candidate roles. Fine-grained co-attention supplies micro-level matching; an efficient macro-level student learns from it through self-distillation and is used at serving time.  
**Main results:** ReSeq outperforms competitive baselines across five real datasets from recruitment and social scenarios. Distillation cuts per-batch prediction latency from about 8.71-8.77 ms for fine-grained matching to 0.283-0.292 ms, near SASRec's 0.102-0.108 ms.

## 2. Experiment Critique

**Design:** Five real-world datasets, two reciprocal domains, two ranking perspectives, ablations, hyperparameter studies, latency profiling, and recruitment text-enhancement tests.  
**Statistical validity:** Multiple datasets and component ablations strengthen the comparison, but uncertainty intervals and significance tests are not specified in the indexed content.  
**Online experiments:** Not specified in source.  
**Reproducibility:** Code is public at https://github.com/RUCAIBox/ReSeq/ and hardware/latency protocol is described.  
**Overall:** Strong dynamic reciprocal representation work; offline implicit-ranking labels do not establish causal or long-horizon value.

## 3. Industry Contribution

**Deployability:** The distilled macro matcher preserves most fine-grained knowledge with roughly thirtyfold lower latency than the micro matcher.  
**Problems solved:** Bilateral preference drift, role asymmetry, expensive cross-sequence interaction, and serving efficiency.  
**Engineering cost:** Requires two role-specific histories per user, transformer sequence encoders, teacher/student training, and fresh interaction features.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First reciprocal recommender to jointly model the dynamic behavior sequences of both parties as a sequence-matching task.  
**Prior work comparison:** Extends static RRS and unilateral sequential recommenders with dual-role encodings, multi-scale co-attention, and micro-to-macro distillation.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Five recruitment/social datasets | Not specified in source. | Mixed/not specified | Design, Sale, Technology, StackOverflow, and one additional dataset. |
| ReSeq code | https://github.com/RUCAIBox/ReSeq/ | Yes | Model implementation. |

**Offline experiment reproducibility:** Moderate to high where dataset preprocessing is available with the public code.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Academic/industry paper  
**Direction:** D8  
**Problem setting:** Dating and recruitment recommendation where both users' preferences evolve and each acts as selector and candidate.  
**Objective and label definition:** Bilateral top-N matching score learned from chronological reciprocal interactions with Bayesian personalized ranking and self-distillation losses.  
**Prediction or incrementality:** Predictive ranking, not causal incrementality.  
**Model architecture:** Active/passive embeddings, dual Transformer sequence encoders, time-sensitive micro co-attention teacher, macro matching student, and self-distillation.  
**Credit assignment:** Historical matching events update both role-specific sequences; no attribution beyond the interaction edge.  
**Training data and counterfactual handling:** Observational implicit sequences with sampled ranking negatives; no propensity or exposure correction.  
**Offline and online evaluation:** NDCG/Hit Rate-style offline metrics, ablations, and latency on five datasets; no online test.  
**Reported gains:** Best overall offline results; distilled latency about 0.28-0.29 ms versus 8.71-8.77 ms without distillation. Exact ranking lift is not specified in the indexed content.  
**Unverified claims:** Online engagement, retention, revenue, fairness, exposure bias, and dynamic marketplace interference are not evaluated.

## Project Relevance

**Source-stated facts:** ReSeq explicitly models two-sided, time-varying preferences for online dating and recruitment and provides a low-latency serving student.

**Survey inference:** Its bilateral sequential representation is a strong backbone for a unified dating ranker, especially when recent swipes and conversations change intent. It should be trained with exposure correction and multi-horizon value heads rather than only implicit pairwise ranking.

**Applicability note:** Strong architecture candidate for dynamic mutual-affinity features.  
Needs causal debiasing, delayed LTV targets, and marketplace constraints.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Bowen Zheng et al.  
**Affiliations:** Renmin University of China; BOSS Zhipin  
**Venue:** RecSys  
**Year:** 2023  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 2
