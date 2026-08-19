# Paper Analysis: OneRec

**Source:** Not specified in source.  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment  
**Authors:** Jiaxin Deng; Shiyao Wang; Kuo Cai; Lejian Ren; Qigen Hu; Weifeng Ding; Qiang Luo; Guorui Zhou  
**Abstract:** OneRec replaces Kuaishou's retrieve/pre-rank/rank cascade with one autoregressive session generator over balanced semantic video identifiers, then aligns its output with a personalized reward model through iterative DPO.  
**Methodology:** An encoder-decoder with sparse mixture-of-experts encodes positive behavior histories and generates coherent multi-video sessions. Beam-search candidates are reward-scored; best/worst outputs become self-hard DPO pairs in iterative preference alignment.  
**Main results:** A 1% main-traffic A/B test reports +1.68% total watch time and +6.56% average view duration for the 1B+IPA model versus the multi-stage production system.

## 2. Experiment Critique

**Design:** Large industrial offline data, module/model-scale ablations, and production A/B comparisons of 0.1B, 1B, and 1B+IPA models.  
**Statistical validity:** Clear incremental online variants isolate scale and IPA effects, but confidence intervals, duration, and sample size are not specified beyond 1% traffic.  
**Online experiments:** Yes; Kuaishou main-page video recommendation.  
**Reproducibility:** Architecture is described, but industrial data, tokenization, reward model, and infrastructure are unavailable.  
**Overall:** Landmark end-to-end deployment evidence; reward-model alignment risks proxy exploitation and watch-time focus underweights other objectives.

## 3. Industry Contribution

**Deployability:** Deployed at Kuaishou scale with hundreds of millions of daily users; sparse MoE expands capacity efficiently.  
**Problems solved:** Cascade stage mismatch, handcrafted session assembly, flat next-item prediction, and scarce explicit preference pairs.  
**Engineering cost:** Multimodal semantic IDs, large encoder-decoder/MoE training, beam search, reward modeling, iterative DPO, and whole-stack replacement.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** One of the first industrial single-stage generative recommenders to beat a mature complete cascade online.  
**Prior work comparison:** Extends generative retrieval from candidate selection to final ranking and replaces point-wise generation with session-level generation and recommendation-specific DPO.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Kuaishou video interactions | Not specified in source. | No | Positive histories, sessions, and rewards. |
| Production A/B test | Not specified in source. | No | 1% main traffic. |

**Offline experiment reproducibility:** Low without proprietary data and reward/tokenization stack.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D9  
**Problem setting:** End-to-end short-video retrieval and ranking with session coherence and industrial-scale catalog.  
**Objective and label definition:** Generate high-value video sessions from positive interactions; a learned personalized reward ranks beam outputs for DPO. Online labels are watch time and average view duration.  
**Prediction or incrementality:** Predictive generation and preference alignment, not causal uplift.  
**Model architecture:** Balanced semantic tokens, encoder-decoder Transformer, sparse MoE, session-wise autoregressive generation, reward model, beam search, and iterative DPO.  
**Credit assignment:** Reward model scores complete generated responses/sessions; exact long-horizon or per-item attribution is not specified.  
**Training data and counterfactual handling:** Observational positive behavior histories and self-generated hard negatives; no exposure propensity correction specified.  
**Offline and online evaluation:** Offline accuracy/scaling/ablation plus production A/B.  
**Reported gains:** 1B+IPA +1.68% total watch time and +6.56% average view duration; 1B without IPA +1.21%/+5.01%.  
**Unverified claims:** Revenue increment, long-term retention, reward-model robustness, multi-objective health, and transfer to reciprocal ranking are not established.

## Project Relevance

**Source-stated facts:** OneRec unifies retrieval and ranking, generates an internally coherent slate, and aligns session outputs with a personalized value proxy.

**Survey inference:** Dating can generate a daily/refresh candidate slate whose ordering and diversity are optimized jointly, then preference-align with match/conversation/retention value. Reward pairs must be derived with exposure-aware counterfactuals and bilateral outcomes, not only a proxy model.

**Applicability note:** Core generative architecture reference for eliminating cascade objective mismatch.  
Adapt session rewards to reciprocal delayed value and audit proxy-reward failure modes.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|---|---|---|
| [2025_arXiv_OneRec-V2_Lazy-Decoder-Real-Feedback.md](./2025_arXiv_OneRec-V2_Lazy-Decoder-Real-Feedback.md) | Related Work | Explicitly mentions OneRec in baseline or comparison context. |

## Meta Information

**Authors:** Jiaxin Deng et al.  
**Affiliations:** Kuaishou  
**Venue:** arXiv  
**Year:** 2025  
**PDF:** Available  
**Relevance:** Core architecture analogue  
**Priority:** 1
