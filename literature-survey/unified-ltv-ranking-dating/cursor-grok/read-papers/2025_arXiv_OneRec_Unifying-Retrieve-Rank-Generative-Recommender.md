# Paper Analysis: OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment

**Source:** https://arxiv.org/pdf/2502.18965
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment
- **authors or company:** Jiaxin Deng, Shiyao Wang, Kuo Cai, Lejian Ren, Qigen Hu, Weifeng Ding, Qiang Luo, Guorui Zhou (Kuaishou)
- **venue:** arXiv
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2502.18965
- **source type:** industry paper
- **direction:** D9
- **problem setting:** Kuaishou short-video main feed: replace multi-stage recall → pre-rank → rank cascade with a single encoder–decoder generative model that autoregressively generates semantic item IDs for an entire session slate.
- **objective and label definition:** Session training: autoregressive next semantic-token prediction on user history (likes, follows, shares, effective watches) and session target lists tokenized via multi-level balanced residual K-Means on aligned multimodal embeddings; IPA stage: Direct Preference Optimization with self-hard negatives from beam search ranked by a pretrained personalized reward model — no explicit retention-day or subscription LTV label in training objective.
- **long-term retention/revenue reward:** **No.** Training optimizes NTP and DPO preference alignment on watch-behavior sessions; online A/B reports Total Watch Time and Average View Duration — engagement/revenue proxies, not stated retention or LTV reward terms.
- **prediction or incrementality:** Generates session item lists via autoregressive semantic IDs; DPO aligns to reward-model preferences — predictive generative ranking, not causal incrementality of exposure on retention.
- **model architecture:** Encoder–decoder with sparse MoE scaling; session-wise list generation (not pointwise next-item); balanced residual K-Means semantic tokenization (avoids RQ-VAE hourglass); Iterative Preference Alignment (IPA): beam-search self-hard negatives + personalized reward model scores for DPO pair selection; deployed OneRec-1B with KV-cache and mixed-precision inference.
- **credit assignment:** Session-level generative targets and DPO on chosen vs rejected full session responses from beam search; reward model provides per-user preference scores for hard-negative mining — not user-level delayed LTV attribution to one impression.
- **training data and counterfactual handling:** Industrial interaction logs; seed model trained with LNTP then IPA/DPO; 1% main-traffic online A/B; on-policy DPO sampling constraints noted (single display opportunity per request); no IPS or delayed-feedback correction stated.
- **offline and online evaluation:** Offline ablations on session-wise vs pointwise generation, MoE scale, DPO variants; online A/B (1% traffic, main page): Total Watch Time +1.68%, Average View Duration +6.56% vs multi-stage baseline (abstract also reports 1.6% watch-time increase).
- **reported gains:** First industrial end-to-end generative ranker beating multi-stage cascade online; +1.68% Total Watch Time and +6.56% Average View Duration in online A/B; MoE scaling improves offline metrics; IPA/DPO improves generalization across user preference patterns.
- **applicability note for a two-sided dating recommender:** Reference architecture for collapsing retrieve+rank into one generative session model with preference alignment — applicable if dating feeds move from multi-tower recall + ranker to generating ranked profile slates from interaction histories.
- **applicability note for a two-sided dating recommender:** Watch-time and view-duration rewards do not substitute for bilateral match outcomes, reciprocity, or 7–30 day retention labels; no two-sided or reciprocal structure in objective or evaluation.
- **unverified claims:** none

## 1. Summary

OneRec replaces Kuaishou's cascaded recommender with a single sparse-MoE encoder–decoder that generates session video lists as semantic token sequences. Balanced residual K-Means tokenization, session-wise generation, and IPA (DPO with reward-model-ranked self-hard negatives) address cascade upper-bound limits and pointwise coherence issues. Deployed at 1B parameters with online A/B wins on watch time and view duration.

## Project Relevance

Core **Q8** (migration path): unified generative model replacing CTR-tuned cascade. **Q1** negative: engagement watch-time objective, not LTV. Does not address reciprocity, delayed retention labels, or incrementality.

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Watch time / view duration via generative ranking + DPO. |
| **(2) Credit assignment** | Session-level generative + DPO preference pairs. |
| **(3) Label / horizon; delay / sparsity / censoring** | Session interaction logs; no delayed retention labels. |
| **(4) Short-term vs long-term head fusion** | Single unified generative model replaces cascade stages. |
| **(5) Prediction vs incrementality** | Generative prediction + preference alignment. |
| **(6) Offline / online eval** | Offline ablations; online A/B on watch metrics. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Not specified in source. |
| **(8) CTR → unified long-term migration** | End-to-end generative replacement of multi-stage ranker deployed online. |

## Meta Information

**Authors:** Jiaxin Deng et al.  
**Affiliations:** Kuaishou  
**Venue:** arXiv 2025 (arXiv:2502.18965)  
**Relevance:** Core (D9 unified generative ranking)  
**Priority:** 1
