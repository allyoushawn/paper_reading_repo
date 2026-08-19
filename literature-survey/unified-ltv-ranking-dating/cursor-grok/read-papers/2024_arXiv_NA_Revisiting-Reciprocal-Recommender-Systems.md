# Paper Analysis: Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method

**Source:** https://arxiv.org/pdf/2408.09748.pdf  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method
- **authors or company:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu (RUC; BOSS Zhipin; UCSD)
- **venue:** KDD 2024
- **year:** 2024
- **URL:** https://arxiv.org/pdf/2408.09748.pdf
- **source type:** academic/industry
- **direction:** D8
- **problem setting:** Two-sided reciprocal recommendation (recruitment, online dating) where independent per-side Recall/NDCG double-count redundant bilateral recommendations and miss system-level match coverage; bilateral treatments jointly determine match outcomes.
- **objective and label definition:** Primary outcome = final match (r_ij ∈ {0,1}); direction label d_ij indicates A→B vs B→A interactions; five holistic metrics — CRecall, CPrecision, SRecall, SPrecision, RNDCG@K — penalize duplicate bilateral hits; K=50; no retention/LTV horizon in source.
- **prediction or incrementality:** Causal reciprocal model estimates potential outcomes ŷ_t for bilateral treatment assignments t ∈ {10, 11, 01} under Rubin framework; ranking scores s_ai = ŷ_10 + ŷ_11, s_bj = ŷ_01 + ŷ_11; reranking uses vacant-slot expectations ȳ(a_i), ȳ(b_j) via IsMax over strategy set.
- **model architecture:** Model-agnostic: three treatment-specific backbones (e.g., BPRMF, LightGCN) sharing pretrained embeddings; two-stage BPR pretrain then counterfactual finetune per treatment dataset D_11, D_10, D_01; vacant-slot reranking maximizes global match expectation.
- **credit assignment:** Pair-level causal treatment effects across bilateral recommendation assignments; not session-level or long-horizon retention credit.
- **training data and counterfactual handling:** Recruitment (32,161 candidates × 25,665 recruiters; 224,636 matches) and Libimseti dating (6,391 × 6,516; 51,474 matches, mutual rating ≥8); 5-core filter; 8:1:1 split; offline assumes one-sided positive exposure suffices for match; no IPS/propensity correction.
- **offline and online evaluation:** Full-ranking offline only @K=50; paired t-test p<0.05 on improvements; no live online A/B reported.
- **reported gains:** Dating CRRS (BPRMF): CRecall@50 0.3387 vs BPRMF 0.2795; True Positive Pairs 1,743 vs 1,439; RNDCG@50 0.0849 vs 0.0660; Recruitment CRRS: CRecall@50 0.4670 vs DPGNN 0.4555 but SRecall 0.1248 vs 0.1535 (coverage–stability trade-off).
- **applicability note for a two-sided dating recommender:** CRecall/CPrecision and bilateral-treatment CRRS framing directly address swipe/match systems where both sides receive ranked lists and redundant mutual exposure should not count twice.
- **applicability note for a two-sided dating recommender:** Libimseti static ratings ≠ production swipe logs with congestion, capacity, and retention; offline one-sided-match assumption and no online validation limit deployability evidence for LTV-oriented rankers.
- **unverified claims:** none
