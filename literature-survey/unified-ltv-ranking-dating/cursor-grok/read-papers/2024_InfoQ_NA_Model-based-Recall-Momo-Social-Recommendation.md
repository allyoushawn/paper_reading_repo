# Paper Analysis: Model-based Recall in Momo Social Recommendation

**Source:** https://www.infoq.cn/article/7s6oqecgk8bmckobj0ud
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** 模型化召回在陌陌社交推荐的应用和探索 (Model-based Recall in Momo Social Recommendation)
- **authors or company:** 吴保鑫 (Wu Baoxin), Momo Technology
- **venue:** InfoQ
- **year:** 2021
- **URL:** https://www.infoq.cn/article/7s6oqecgk8bmckobj0ud
- **source type:** blog
- **direction:** D8
- **problem setting:** Two-sided social recommendation on Momo for Nearby Moments (content-mediated matching) and Nearby People (location-based matching); recall must capture both content consumption and bilateral social matching within a recall → coarse rank → fine rank → re-rank pipeline.
- **objective and label definition:** Recall-stage embedding models trained on scene interaction labels (click, like, comment, greet, follow, reply); losses include Weighted-Hinge-Loss for ANN retrieval and multi-objective user representation learning split by interaction type; online metrics are interaction conversion rate and social matching rate — no retention, LTV, or revenue labels.
- **prediction or incrementality:** Predicts user–item / user–user compatibility embeddings for ANN retrieval; not causal incrementality of exposure on long-term outcomes.
- **model architecture:** Four model-based recall channels: (1) multimodal dynamic content semantics (Bi-LSTM/Transformer text + ResNet image + interactive attention) for I2I; (2) scene preference model with long/short-term Transformer sequence units, User–Item–Owner tri-side matching, multi-task heads per interaction type for U2I and U2U2I; (3) social graph GCN on friendship/chat/blacklist edges with virtual interest-based edges and layer-concatenated node embeddings for social U2U2I; offline training + online ANN (HNSW etc.).
- **credit assignment:** Pointwise / pair-level interaction labels aggregated into embedding training; graph edges weighted by relationship strength; no IPS, counterfactual correction, or user-level delayed outcome attribution.
- **training data and counterfactual handling:** Platform behavior logs (dynamic posts, scene interactions, social relations); batch negatives plus global negatives for preference model; hard negatives from blacklist users for GCN; no counterfactual or delayed-feedback handling described.
- **offline and online evaluation:** Offline model training with ablation on architecture choices; online A/B on interaction conversion rate and social matching rate per recall channel; no unified offline ranking metric (NDCG/AUC) reported for full stack.
- **reported gains:** Scene-preference U2I/U2U2I recall: interaction conversion rate +15%+; content-semantics I2I recall: interaction conversion rate +10%+ (A/B); social-matching GCN recall: social matching rate +10%+ (A/B).
- **applicability note for a two-sided dating recommender:** Direct industry precedent for bilateral social matching recall (GCN social edges, User–Owner item encoding, U2U2I channels) alongside content preference — mirrors dating apps that must rank profiles for reciprocity, not just content similarity.
- **applicability note for a two-sided dating recommender:** Recall-only engagement proxies (interaction conversion, social matching rate) with no retention/revenue objective, delay model, or unified LTV ranking — useful for reciprocal recall design, not for credit assignment or long-horizon label fusion.
- **unverified claims:** Primary InfoQ URL timed out on direct fetch (2026-08-16); quantitative A/B lifts (+15%, +10%, +10% social matching) taken from InfoQ article text retrieved via web mirror of the same URL — significance intervals and metric definitions not stated in source.

## 1. Summary

Momo describes model-based recall for open social recommendation across Nearby Moments and Nearby People. The stack builds four embedding recall channels: multimodal content semantics (I2I), scene interaction preference with long/short-term sequences and multi-task interaction heads (U2I/U2U2I), and GCN social-graph matching recall (U2U2I). Models train offline and serve via ANN retrieval; gains reported on interaction conversion and social matching rates in online A/B tests.

## Project Relevance

Speaks to **Q7** (two-sided/reciprocal markets): explicit social-matching recall channel and User–Owner–Item tri-side matching are closest deployed analogues to dating reciprocity at recall stage. Does not address Q1 (unified LTV objective), Q3 (delayed labels), Q4 (head fusion), Q5 (incrementality), or Q6 (validated long-horizon online eval).

| Dimension | Source extraction |
|-----------|-------------------|
| **(1) Ranking objective** | Interaction conversion and social matching at recall; retention/LTV/revenue not specified. |
| **(2) Credit assignment** | Supervised embedding learning on logged interactions; no counterfactual correction. |
| **(3) Label / horizon; delay / sparsity / censoring** | Real-time scene interactions; no delay or censoring model. |
| **(4) Short-term vs long-term head fusion** | Not specified in source. |
| **(5) Prediction vs incrementality** | Prediction / retrieval scoring only. |
| **(6) Offline / online eval** | Per-channel A/B on conversion and matching rates; no delayed retention metrics. |
| **(7) Reciprocity / congestion / fairness / revenue vs match** | Social matching GCN and bilateral Owner encoding; congestion and revenue trade-offs not specified. |
| **(8) CTR → unified long-term migration** | Not specified in source. |

## Meta Information

**Authors:** 吴保鑫 (Wu Baoxin)  
**Affiliations:** Momo Technology  
**Venue:** InfoQ (2021-03-31)  
**Relevance:** Core (D8 reciprocal recall)  
**Priority:** 2
