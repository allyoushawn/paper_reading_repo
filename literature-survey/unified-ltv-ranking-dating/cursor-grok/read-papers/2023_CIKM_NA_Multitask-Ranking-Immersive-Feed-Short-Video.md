# Paper Analysis: Multitask Ranking System for Immersive Feed and No More Clicks: A Case Study of Short-Form Video Recommendation

**Source:** https://doi.org/10.1145/3583780.3615489
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Multitask Ranking System for Immersive Feed and No More Clicks: A Case Study of Short-Form Video Recommendation
- **authors or company:** Qingyun Liu, Zhe Zhao, Liang Liu, Zhen Zhang, Junjie Shan, Yuening Li, Shuchao Bi, Lichan Hong, Ed H. Chi (Google / Google DeepMind)
- **venue:** CIKM 2023
- **year:** 2023
- **URL:** https://doi.org/10.1145/3583780.3615489
- **source type:** industry paper
- **direction:** D1
- **problem setting:** Ranking stage on a large short-form video (SFV) platform with immersive feed UI (one video at a time, no click-to-select); tens of MTL tasks with label means as sparse as 1e-4–1e-5.
- **objective and label definition:** Multi-task prediction of user behaviors (watches, likes, comments, shares, etc.) from impression logs; sparse tasks (e.g., comments ~1 per 1000 watches) vs. dense watch/engagement tasks; no explicit retention/LTV horizon label—live metrics include Overall Enjoyment and task-specific engagement counts.
- **prediction or incrementality:** Supervised multi-task ranking heads predict per-behavior probabilities; final ranking score is a weighted combination of task predictions (multi-objective fusion at serving), not a direct policy for long-term retention.
- **model architecture:** Shared-bottom embeddings → MMoE experts → task towers; debias shallow towers model watch-trail position bias per task; disentangle regularization on MMoE; sparse-task loss upweighting; meta-learner MLP selects sparse-task loss weights from gradient/label-mean features.
- **credit assignment:** Per-impression / per-video-in-sequence labels from user logs; trail-bias correction attributes position-in-watch-sequence effects; no user-level delayed outcome decomposed to individual slate items beyond standard impression labels.
- **training data and counterfactual handling:** Tens of billions of interactions on millions of items; trail-bias debias towers trained jointly; imbalance learning (sampling, focal loss, upweighting) for sparse tasks; meta-learner trained on enumerated weight configurations using limited log subsamples (5–20%) vs. full grid search.
- **offline and online evaluation:** Offline AUC (classification) and RMSE (regression); 2+ week live A/B on production traffic; Overall Enjoyment and task-specific metrics with 95% CI significance; deployed 6+ months.
- **reported gains:** Trail debias on all tasks: +1.96% Overall Enjoyment live; disentangle regularization: up to +0.33% Overall Enjoyment; sparse co-training with upweight 50: +0.29% Overall Enjoyment and +3.07% on sparse task metric vs. separate sparse training; meta weight selection at 20% data matches handpicked live performance; 60% parameter reduction from co-training vs. separate sparse towers.
- **applicability note for a two-sided dating recommender:** MMoE + sparse-task upweighting + meta weight selection is a direct template when dating ranking must jointly optimize dense swipe/like signals and ultra-sparse match/message heads without separate models per objective.
- **applicability note for a two-sided dating recommender:** Watch-trail debiasing addresses sequential position bias in immersive feeds, not reciprocity, counterparty congestion, or bilateral match-quality credit assignment; no retention/LTV head or delayed label pipeline is described.
- **unverified claims:** none

## 1. Summary

**Title:** Multitask Ranking System for Immersive Feed and No More Clicks: A Case Study of Short-Form Video Recommendation
**Authors:** Qingyun Liu, Zhe Zhao, Liang Liu, Zhen Zhang, Junjie Shan, Yuening Li, Shuchao Bi, Lichan Hong, Ed H. Chi (Google)
**Abstract:** SFV immersive feeds remove click-based position biases and make sparse engagement labels (comment, share) far rarer than in click-filtered systems. The paper proposes an MMoE MTL ranker with watch-trail bias correction, disentangle regularization, sparse-task loss upweighting, and meta-learning for efficient sparse-task weight selection, deployed on a major SFV platform.

**Key contributions:**
- Identifies "watch trail biases" in sequential SFV recommendation (no click-based position bias).
- Debias shallow towers + disentangle regularization + sparse-task co-training with imbalance learning.
- Meta-learner for sparse-task weight selection using fraction of logs instead of live grid search.

**Methodology:** Shared embeddings, MMoE, per-task towers; debias logits from trail features; disentangle loss on expert outputs; unified upweight on sparse task losses; meta MLP predicts combined AUC from gradients and label statistics.

**Main results:** Production deployment 6+ months; live gains up to +1.96% Overall Enjoyment (trail debias), +0.29% (sparse co-training upweight 50); meta learner matches handpicked weights using 20% data.

## 2. Experiment Critique

**Design:** Strong industrial evaluation—offline AUC/RMSE plus multi-week live A/B with significance testing; ablations on debias scope, disentangle λ, IL strategies, and weight-selection methods.

**Statistical validity:** Live metrics marked * at 95% CI; offline tables report AUC numerically; some offline debias tables omitted for brevity in paper.

**Online experiments:** Real production SFV platform; Overall Enjoyment as primary north-star alongside task metrics; co-training without IL degrades sparse tasks (consistent with prior MTL literature cited).

**Reproducibility:** Proprietary Google SFV logs; TFRS/TPU stack described; no public dataset.

**Overall:** Credible industrial MTL case study for clickless immersive UI; engagement-focused rather than explicit retention modeling.

## 3. Industry Contribution

**Deployability:** 6+ month production deployment on one of the largest SFV platforms; tens of tasks, billions of interactions.

**Problems solved:** Trail bias in sequential feeds; extreme sparse/dense task conflict in MTL; expensive live grid search for task weights.

**Engineering cost:** Adds debias towers, disentangle loss, and meta-learner training loop; co-training reduces parameters ~60% vs. separate sparse models.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First systematic treatment of MTL ranking under immersive no-click SFV UI; watch-trail bias; meta-learning for sparse-task weight selection at scale.

**Prior work comparison:** Builds on MMoE [Ma et al. KDD 2018], disentangle MTL [Chen et al.], uncertainty reweighting [Kendall et al.], Covington et al. YouTube DNN, Instagram/TikTok-style SFV literature.

**Verification:** Trail bias and sparse-task co-training pain points are well motivated; components are incremental but integration and live evidence are the contribution.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Google SFV production logs | Not public | No | Tens of billions of interactions |

**Offline experiment reproducibility:** Not reproducible without proprietary data.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Multi-objective engagement (watch, like, comment, share, etc.) via MTL task heads; Overall Enjoyment live metric—not explicit retention/LTV or revenue optimization.

**(2) Credit assignment:** Per-impression labels from user behavior signals on each recommended SFV in the watch sequence; trail-bias correction for position in sequence; not specified in source: user-level delayed outcome → single exposure.

**(3) Label and horizon definitions:** Per-behavior binary/regression labels from logs; sparse tasks at 1e-4–1e-5 positive rate; comments cited as <1 per 1000 watches; no retention horizon or censoring model stated.

**(4) Short-term + long-term heads:** Multiple parallel task towers on shared MMoE; serving combines task predictions into multi-objective ranking score (fixed/learned fusion at serving layer per figure); no separate long-term value head.

**(5) Prediction vs incrementality:** Predicts per-task engagement probabilities; does not model treatment effect of exposure on long-term outcome.

**(6) Offline and online evaluation:** Offline AUC/RMSE; 2+ week live A/B with 95% CI; no delayed retention evaluation; two-sided interference not specified in source.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Extends standard MMoE MTL ranker with trail debias + sparse-task IL + meta weights for clickless immersive feed; replaces click-filtered post-click label construction.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Qingyun Liu, Zhe Zhao, Liang Liu, Zhen Zhang, Junjie Shan, Yuening Li, Shuchao Bi, Lichan Hong, Ed H. Chi
**Affiliations:** Google / Google DeepMind
**Venue:** CIKM 2023
**Year:** 2023
**PDF:** https://doi.org/10.1145/3583780.3615489
**Relevance:** Core
**Priority:** 1
