# Paper Analysis: OneRec-V2 Technical Report

**Source:** https://arxiv.org/abs/2508.20900  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** OneRec-V2 Technical Report  
**Authors:** OneRec Team  
**Abstract:** OneRec-V2 makes Kuaishou's end-to-end generative recommender scalable with a lazy decoder-only architecture and aligns it directly with user interaction feedback rather than only a learned reward model.  
**Methodology:** Context is processed once and shared as cross-attention keys/values while model capacity is concentrated on target generation. Duration-aware reward shaping removes raw watch-time length bias; gradient-bounded policy optimization with adaptive ratio clipping trains on live-policy feedback.  
**Main results:** Computation falls 94% and training resources 90%, enabling scale from 0.5B to 8B parameters. Online App Stay Time improves 0.467% on Kuaishou and 0.741% on Kuaishou Lite versus OneRec-V1.

## 2. Experiment Critique

**Design:** Architecture/scaling ablations, reward-model versus direct-feedback experiments, and extensive A/B tests on platforms totaling about 400M daily active users.  
**Statistical validity:** Production scale is exceptional, but confidence intervals and test duration are not specified. A no-cache subgroup reveals large ecosystem tradeoffs masked by aggregate engagement.  
**Online experiments:** Yes; Kuaishou and Kuaishou Lite, including a 1% fully uncached experimental group.  
**Reproducibility:** Detailed architecture and equations, but data, reward rules, and industrial system are proprietary.  
**Overall:** Strong scaling and online evidence with unusually candid ecosystem harms; the reward still heuristically links short- and long-term returns.

## 3. Industry Contribution

**Deployability:** Lazy computation supports an 8B recommender under industrial budgets and uses deployed traffic for continual preference alignment.  
**Problems solved:** Encoder compute imbalance, RL reward-model sampling cost/hacking, duration bias, unstable policy updates, and multi-objective see-saw.  
**Engineering cost:** Massive generative training, shared-context cache, online feedback pipeline, reward shaping, GBPO, and ecosystem monitoring.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Lazy decoder-only computation focused almost entirely on loss-bearing target tokens plus direct real-feedback generative-RL alignment.  
**Prior work comparison:** Improves OneRec-V1's encoder-decoder and reward-model RL while borrowing GQA/KV sharing and PPO-family optimization ideas.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Kuaishou/Kuaishou Lite interaction logs | Not specified in source. | No | Watch time and explicit interaction signals. |
| Production A/B tests | Not specified in source. | No | Roughly 400M DAU ecosystem. |

**Offline experiment reproducibility:** Low without proprietary data and serving/training infrastructure.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry technical report  
**Direction:** D9  
**Problem setting:** End-to-end generative video recommendation at massive scale with multiple engagement and ecosystem objectives.  
**Objective and label definition:** Autoregressive next-item generation post-trained on duration-adjusted real interactions; main online outcome is App Stay Time.  
**Prediction or incrementality:** Policy optimization over logged/live feedback, not explicit causal uplift.  
**Model architecture:** Lazy decoder-only Transformer, shared context KV, grouped-query cross-attention, dense/MoE scaling to 8B, and GBPO post-training.  
**Credit assignment:** Duration-aware shaping adjusts video-level watch feedback; short/long returns are linked by hand-designed rules rather than direct long-term-value optimization.  
**Training data and counterfactual handling:** Chronological newest-impression training and real OneRec-policy feedback; no explicit propensity correction specified.  
**Offline and online evaluation:** Loss/compute/scaling ablations plus large online A/B and an uncached subgroup.  
**Reported gains:** App Stay Time +0.467%/+0.741%; compute -94%, training resources -90%. Uncached traffic also showed cold-start views -44.7%/-36.7% and cluster density +11.7%/+7.9%.  
**Unverified claims:** Direct long-term value, causal attribution, and absence of ecosystem harm under full rollout remain unresolved.

## Project Relevance

**Source-stated facts:** OneRec-V2 trains a unified generative policy on real user feedback, explicitly corrects duration bias, and exposes severe cold-start/diversity side effects despite engagement gains.

**Survey inference:** Dating can use lazy shared-context computation for large mutual candidate models and learn from live multi-event feedback. Its most important lesson is objective governance: optimizing stay time can crowd out new candidates, just as message/retention optimization can concentrate dating attention or discourage successful exits.

**Applicability note:** Strong architecture and feedback-alignment reference for unified ranking.  
Guard with candidate exposure, fairness, successful-match, and long-term welfare metrics.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** OneRec Team  
**Affiliations:** Kuaishou  
**Venue:** arXiv  
**Year:** 2025  
**PDF:** Available  
**Relevance:** Core architecture analogue  
**Priority:** 1
