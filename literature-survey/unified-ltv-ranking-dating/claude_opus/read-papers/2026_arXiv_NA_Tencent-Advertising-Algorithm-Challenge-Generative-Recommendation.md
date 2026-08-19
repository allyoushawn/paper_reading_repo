# Paper Analysis: The Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2604.04976.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

This is a competition report (Junwei Pan et al., Tencent Inc. / CUHK, arXiv preprint 2604.04976) describing the Tencent Advertising Algorithm Challenge 2025, an "All-Modality Generative Recommendation" competition built on two new large-scale, fully multi-modal advertising-log datasets — TencentGR-1M (~1M users, ~4.78M ads, exposure/click-labeled) and TencentGR-10M (~10.1M users, ~17.5M ads, adding conversion labels: 94.63% exposure, 2.85% click, 2.52% conversion). The task in both rounds is next-item prediction: given a user's chronological ad interaction sequence (impression, click, and in the final round, conversion tokens, each carrying collaborative IDs plus pre-computed multi-modal text/image embeddings), generate/retrieve the next ad the user is most likely to click or convert on, scored offline by HitRate@10/NDCG@10 (preliminary round) or conversion-upweighted w-HitRate@10/w-NDCG@10 (final round, conversions weighted 2.5x clicks). The paper releases a baseline causal-Transformer next-token-prediction model trained with InfoNCE and ANN (Faiss) retrieval, and summarizes the top three teams' and one innovation-award team's architecture choices (per-position action-conditioning, GNN-enriched encoders, RQ-KMeans semantic IDs, and a joint semantic-ID-generation-plus-action-prediction objective), without reporting a comparable leaderboard-score table for any individual model.

## 2. Experiment Critique

Evaluation is entirely offline, on a private, sandboxed, network-isolated test set, ranked purely on next-click/next-conversion retrieval metrics; there is no online experiment (this is a competition leaderboard, not a deployed system study). The paper is largely descriptive of the competition mechanics and the winning teams' design choices rather than a controlled ablation; no statistical significance testing is reported for any comparison. Reproducibility is a stated design goal — code, data, and a baseline implementation are released and a mandatory code-execution/reproducibility check gated advancement to the final round — but the top-team solutions themselves are not released code, only textual design summaries.

## 3. Industry Contribution

The datasets and baseline are released as an industrial-scale, fully multi-modal generative-recommendation benchmark tied to a real advertising pipeline (Tencent Ads), intended to catalyze research into semantic-ID-based generative retrieval/ranking; the paper explicitly frames this as filling a gap in public benchmarks that jointly offer scale, multi-modality, and industrial advertising realism. No production deployment, latency, or serving-cost figures are given — the competition and baseline are research artifacts, not a described production system.

## 4. Novelty vs. Prior Work

Positioned against existing generative-recommendation benchmarks the authors say are single-modality or non-advertising (Amazon Beauty/Toys/Sports, Yelp), and against larger but still limited multi-modal datasets (MIND, KuaiRand/KuaiRec, Tenrec, WWW'25 short-video dataset) that the authors say lack industrial ad creatives or conversion-centric labels. Cites PinRec (Badrinath et al. 2025, outcome-conditioned multi-token generative retrieval) as a direct architectural influence on multiple top-team solutions (action-type conditioning), along with TIGER, LETTER, DAS, MMQ, and OneRec as the broader semantic-ID/generative-recommendation lineage it builds on.

## 5. Dataset Availability

| Dataset | Public? | Size | Notes |
|---|---|---|---|
| TencentGR-1M | Yes, released for the competition (HuggingFace: TAAC2025/TencentGR-1M) | ~1,001,845 users, ~4,783,154 ads | Preliminary round; exposure + click labels only |
| TencentGR-10M | Yes, released for the competition (HuggingFace: TAAC2025/TencentGR-10M) | ~10,139,575 users, ~17,487,676 ads | Final round; exposure + click + conversion labels |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "The Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation," Junwei Pan, Wei Xue, Chao Zhou, Xing Zhou, Lunan Fan, Yanbo Wang, Haoran Xin, Zhiyu Hu, Yaozheng Wang, Fengye Xu, Yurong Yang, Xiaotian Li, Junbang Huo, Wentao Ning, Yuliang Sun, Chengguo Yin, Jun Zhang, Shudong Huang, Lei Xiao, Huan Yu, Irwin King, Haijie Gu, Jie Jiang (Tencent Inc. / CUHK), arXiv preprint, arXiv:2604.04976, https://arxiv.org/abs/2604.04976 |
| 2 | Source type | Industry paper (Tencent Inc., with CUHK co-author) — competition/benchmark report |
| 3 | Direction | D9 |
| 4 | Problem setting | A public modeling competition on two new large-scale, fully multi-modal advertising-log datasets, formulated as generative next-item (next-ad) sequence recommendation: given a user's chronological ad interaction history, predict the next ad the user clicks or converts on. |
| 5 | Objective and label definition | Next-item / next-click-or-conversion prediction over a bounded sequence (≤100 item tokens per user). Preliminary round labels clicks only; final round adds conversions, using "an attribution window consistent with industry standards to account for conversion delay" — the paper does not state the window's numeric length. No retention or multi-day/multi-session horizon is defined; the outcome is the single next logged interaction. |
| 6 | **Prediction or incrementality** | Prediction only — the paper does not address incrementality. |
| 7 | Model architecture | Baseline: causal-Transformer next-token-prediction generative recommender. Per-token multi-field feature fusion (categorical/ID embedding tables plus pre-computed multi-modal text/image embeddings, concatenated and MLP-projected) feeds a causal Transformer; the final-position hidden state is the user embedding, trained with an InfoNCE contrastive loss against sampled negatives (action-type-weighted in the second round to upweight conversions), with Faiss ANN retrieval at inference. |
| 8 | **Credit assignment** | Not applicable / not addressed — this is single-sequence next-item prediction, not a user-level delayed-outcome-to-item-level-decision attribution problem; each training instance already pairs one interaction with its immediately preceding sequence prefix. |
| 9 | Training data and counterfactual handling | De-identified Tencent Ads logs (TencentGR-1M / TencentGR-10M, see Dataset Availability). No counterfactual, off-policy, or exposure-bias correction is described; InfoNCE negatives are sampled uniformly from the global candidate pool, not from logged non-interactions. |
| 10 | Offline and online evaluation | Offline only, on a private sandboxed test set with no network access. Preliminary round: HitRate@10, NDCG@10. Final round: action-type-weighted w-HitRate@10, w-NDCG@10 (conversions weighted 2.5x clicks). No online A/B test is reported or possible in a competition format. |
| 11 | Reported gains | No single winning model's numeric leaderboard score is reported in the paper; it summarizes qualitative design choices of the top three teams and the Technical Innovation Award winner rather than a comparable gains-over-baseline table. |
| 12 | Applicability to a two-sided dating recommender | Low direct applicability — single-sided next-ad-click/conversion prediction with no reciprocity, congestion, retention, or revenue-horizon modeling; its only transferable element is the general multi-modal generative sequence-to-semantic-ID recommendation pattern. |
| 13 | Unverified claims | None beyond standard competition self-description; the paper reports only aggregate leaderboard structure and top-team design summaries, not independently verifiable performance numbers for any single model. |

## Project Relevance

**Low project relevance.** The paper is a competition report on next-ad-click/conversion prediction — a single-impression, short-horizon discriminative-turned-generative task with no retention, revenue-over-weeks, delayed-label, or two-sided/reciprocal-market content anywhere in it. It touches none of the eight research questions directly; its only value to this survey is as a signal that industry effort (Tencent) is currently concentrated on scaling multi-modal generative sequence models for short-horizon ad-click/conversion prediction, not on unifying that objective with retention or LTV.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Junwei Pan, Wei Xue, Chao Zhou, Xing Zhou, Lunan Fan, Yanbo Wang, Haoran Xin, Zhiyu Hu, Yaozheng Wang, Fengye Xu, Yurong Yang, Xiaotian Li, Junbang Huo, Wentao Ning, Yuliang Sun, Chengguo Yin, Jun Zhang, Shudong Huang, Lei Xiao, Huan Yu, Irwin King, Haijie Gu, Jie Jiang
- **Affiliations:** Tencent Inc.; CUHK
- **Venue:** arXiv preprint
- **Year:** 2026 (arXiv:2604.04976; describes the 2025-run challenge)
- **Relevance:** Related
- **Priority:** 3
- **nlm:42cc0f19**
