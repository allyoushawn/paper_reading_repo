# Paper Analysis: Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations

**Source:** https://arxiv.org/pdf/2402.17152.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations
- **authors or company:** Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, et al. (Meta / MRS)
- **venue:** ICML
- **year:** 2024
- **URL:** https://arxiv.org/pdf/2402.17152.pdf
- **source type:** industry paper
- **direction:** D9
- **problem setting:** Large-scale ranking and retrieval on a Meta internet platform with billions of users; reformulates recommendation as sequential transduction over high-cardinality user action sequences.
- **objective and label definition:** Generative Recommenders (GRs) trained in streaming one-pass settings on user action sequences (items + action types + timestamps). Ranking uses multi-task Normalized Entropy (NE) on main engagement task (E-Task) and main consumption task (C-Task); retrieval uses log perplexity. Public benchmarks use next-item hit rate / NDCG. No explicit retention, LTV, or revenue labels in the training objective.
- **long-term retention/revenue reward:** **No.** Training optimizes engagement/consumption NE and retrieval perplexity; online A/B reports E-Task and C-Task wins (+12.4% / +4.4%). Impact statement discusses aligning long-term user outcomes, but no retention, LTV, or revenue reward appears in the objective or reported online metrics.
- **prediction or incrementality:** Predicts next actions / ranks candidates from sequential representations—predictive modeling of engagement intensity and ordering, not causal incrementality of exposure on retention.
- **model architecture:** HSTU (Hierarchical Sequential Transduction Unit): pointwise-aggregated attention with relative positional/temporal biases, elementwise gating (SiLU on U), fused kernels; replaces DLRM feature interaction + sequential modules. M-FALCON inference for scoring many candidates; stochastic length (SL) for training efficiency. Deployed GR up to 1.5T parameters.
- **credit assignment:** Fully sequential formulation over user action history; targets are next engagement/consumption events in the sequence—implicit credit via autoregressive transduction, not user-level delayed outcome attribution to a single slate exposure.
- **training data and counterfactual handling:** 100B-example industrial streaming jobs; public MovieLens/Amazon Books for ablations. Standard supervised / generative training on logged interactions; no counterfactual or delayed-feedback correction.
- **offline and online evaluation:** Offline NE on E/C tasks, HR@K, NDCG on public data; scaling-law studies to GPT-3/LLaMa-2 compute scale. Online A/B: GR ranking +12.4% E-Task, +4.4% C-Task vs DLRM; retrieval add-source +6.2%/+5.0%, replace +5.1%/+1.9%. HSTU 5.3×–15.2× faster than FlashAttention2 Transformers at 8192 length.
- **reported gains:** Up to 65.8% NDCG lift on Amazon Books (HSTU-large vs SASRec); 12.4% online E-Task win; 285× more complex GR with higher QPS than DLRM at 1024–16384 candidates via M-FALCON.
- **applicability note for a two-sided dating recommender:** Useful architecture reference for scaling sequential user-behavior models that unify feature interaction and history encoding—applicable to modeling swipe/match event sequences at scale.
- **applicability note for a two-sided dating recommender:** Does not train on retention/revenue objectives or delayed labels; E/C engagement proxies do not substitute for unified LTV ranking or bilateral match credit assignment.
- **unverified claims:** none

## 1. Summary

**Title:** Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations
**Authors:** Jiaqi Zhai et al. (Meta)
**Abstract:** Proposes Generative Recommenders and the HSTU architecture, reformulating ranking/retrieval as sequential transduction. HSTU outperforms DLRMs and Transformers at scale, with power-law scaling to trillion-parameter deployments and double-digit online metric wins.

**Key contributions:**
- HSTU encoder with pointwise attention and gating for non-stationary streaming recsys data.
- GR paradigm unifying retrieval and ranking in a generative sequential framework.
- Production deployment at 1.5T parameters with demonstrated scaling laws.

**Methodology:** Stream-trained sequential transducers; M-FALCON for efficient candidate scoring; stochastic length and activation-memory optimizations.

**Main results:** Large offline and online lifts on engagement/consumption tasks; superior compute efficiency vs Transformers.

## 2. Experiment Critique

**Design:** Strong public-dataset baselines (SASRec, BERT4Rec, GRU4Rec) and industrial DLRM baselines tuned over years; systematic HSTU ablations.

**Statistical validity:** NE improvements of 0.001 treated as significant internally; no p-values for main online wins.

**Online experiments (if any):** Platform A/B on E-Task and C-Task; retrieval source add/replace experiments.

**Reproducibility:** Code at facebookresearch/generative-recommenders; industrial data proprietary.

**Overall:** High-quality systems paper for generative sequential recsys; long-term retention/revenue is aspirational in discussion only, not in training or reported online objectives.

## 3. Industry Contribution

**Deployability:** Deployed on multiple surfaces for billions of users; open-sourced reference implementation.

**Problems solved:** DLRM compute scaling failure; quadratic attention cost for long histories; feature-engineering complexity via unified action sequences.

**Engineering cost:** Very high at production scale (100B-example jobs, 64–256 H100s, custom kernels).

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** GR formulation + HSTU architecture with demonstrated industrial scaling laws.

**Prior work comparison:** DLRMs, SASRec, Transformers/FlashAttention, scaling-law work in recsys (Shin et al.).

**Verification:** Online A/B and open code support core claims; retention/LTV claims are not evidenced in objectives.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| ML-1M, ML-20M, Amazon Books | Public | Yes | Traditional sequential eval |
| Meta industrial logs | Not public | No | Streaming NE experiments |

**Offline experiment reproducibility:** Public benchmarks reproducible; industrial results not.

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

**(1) Ranking objective:** Engagement and consumption NE—short-to-medium horizon proxies, not retention/revenue unified objective.

**(2) Credit assignment:** Sequential next-event prediction; no delayed user-level outcome mapping to item decisions.

**(3) Label and horizon definitions:** E-Task/C-Task NE in streaming setting; public data uses standard next-item labels.

**(4) Short-term + long-term heads:** Multi-task NE (E + C) but no explicit long-horizon retention head.

**(5) Prediction vs incrementality:** Predictive ranking from action sequences.

**(6) Offline and online evaluation:** NE, HR, NDCG offline; E/C online wins; no retention A/B reported.

**(7) Reciprocity, congestion, fairness, revenue vs match quality:** Not specified in source.

**(8) Migration path from CTR-like model:** Shows path from DLRM cascades to unified GR/HSTU on action sequences—architectural, not LTV-objective migration.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Jiaqi Zhai, Lucy Liao, Xing Liu, Yueming Wang, Rui Li, et al.
**Affiliations:** Meta (MRS)
**Venue:** ICML 2024
**Year:** 2024
**PDF:** https://arxiv.org/pdf/2402.17152.pdf
**Relevance:** Core
**Priority:** 2
