
# Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method

**Source:** https://arxiv.org/pdf/2408.09748.pdf | **NLM source id:** 54ce1645-9722-4202-9da0-c5145e6ed871 | **Year / venue:** KDD 2024 (arXiv 2408.09748) | **Authors / affiliation:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao*, Jun Xu, Yang Song, Hengshu Zhu — Nanbeige Lab/BOSS Zhipin; Gaoling School of AI, Renmin University of China; UC San Diego; Career Science Lab, BOSS Zhipin (*corresponding) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Reciprocal recommender systems (RRS — recruitment, dating, social) traditionally evaluate each side independently with standard single-sided ranking metrics (Recall/Precision/NDCG), which ignores that both sides' recommendations are coupled and creates redundant recommendations (recommending A to B on both sides when one direction would have sufficed). The paper (a) introduces five holistic metrics — Coverage-adjusted Recall/Precision (CRecall/CPrecision), Stability-adjusted Recall/Precision (SRecall/SPrecision), and Reciprocal NDCG (RNDCG) — and (b) formulates RRS causally under Rubin's potential-outcome framework. **Unit of credit:** per user-pair, bilateral treatment assignment (T_A, T_B) ∈ {10,11,01,00} — whether user pair (aᵢ,bⱼ) is recommended on side A, side B, both, or neither. **Outcome attributed:** successful bilateral match (mutual conversion). **Bias handling:** the four treatment arms isolate independent vs. combined causal effects of one-sided vs. two-sided recommendation; collaborative causal estimation (similar users have similar treatment effects) approximates the fundamentally unobservable counterfactual (only one treatment arm is ever logged per pair); a two-stage CRRS training (BPR pre-training + counterfactual fine-tuning) plus a **vacant-slot reranking strategy** (IsMax) accounts for the opportunity cost of an alternative candidate when one side of a pair isn't recommended, maximizing total non-redundant matches.

## 2. Evidence
- **Datasets:** Recruitment (BOSS Zhipin) — 32,161 candidates, 25,665 recruiters, 790,725 interactions, 224,636 matches, 99.90% sparsity. **Dating (Libimseti)** — 6,391 female / 6,516 male users, 605,288 interactions, 51,474 matches (mutual rating ≥8), 98.55% sparsity.
- **Baselines:** BPRMF, D-BPRMF, LFRR, LightGCN, D-LightGCN, DPGNN (full-ranking top-50 evaluation).
- **Recruitment @K=50:** CRRS(LightGCN) best — CRecall 0.4670 (vs. DPGNN 0.4555), CPrecision 0.0073, 10,490 true-positive matches (vs. DPGNN 10,231).
- **Dating @K=50:** CRRS(LightGCN) best on every metric — CRecall 0.3387 (vs. DPGNN 0.3007), SRecall 0.1221, RNDCG 0.0849, 1,743 true-positive matches (vs. DPGNN 1,548).
- Code/data released at github.com/RUCAIBox/CRRS.

## 3. Limitations
- Coverage-vs-stability trade-off on recruitment: raising CRecall (0.4670 vs. 0.4555) came with a drop in SRecall (0.1248 vs. 0.1535) — reducing redundancy structurally conflicts with bilateral-exposure stability.
- CRRS does not always win on conventional single-sided metrics, since its objective prioritizes total non-redundant matches over single-list ranking accuracy.
- Counterfactual unobservability is fundamental: only one treatment combination is ever logged per pair, so the collaborative estimate is an approximation, not ground truth.
- Vacant-slot matching-expectation estimates rely on sampling a subset of the opposite side rather than exact full-graph enumeration.

## 4. Prior works named
- Rubin (1980) — potential-outcome framework underlying the causal bilateral-treatment formulation.
- Rendle et al. (2009), **BPRMF** — Bayesian Personalized Ranking backbone/pre-training loss.
- He et al. (2020), **LightGCN** — GNN backbone architecture.
- Su, Bayoumi & Joachims (2022) — matching-markets recommendation evaluation and bilateral crowding/imbalance.
- Yang et al. (2022), **DPGNN** — dual-perspective graph baseline for two-way selection preference.

## 5. Project Relevance
- **Answers:** Q2 (models a dating-platform recommendation causally, though the outcome is match, not N7 retention).
- **Attributes retention to individual interactions?** No — attributes bilateral match probability to a recommendation-treatment pair, not retention/active-days to swipe-level interactions over time.
- **Transferable components:** bilateral potential-outcome treatment formulation (distinguishing one-sided vs. mutual exposure) directly maps onto distinguishing a one-sided swipe from a mutual match; the vacant-slot IsMax reranking (opportunity cost of showing candidate B vs. an alternative) is directly relevant to ranking-time incremental-value scoring; redundant-exposure filtering.
- **Required changes:** re-anchor the potential outcome from a single match event to a recurring daily N7 retention indicator; extend the binary bilateral treatment (T_A,T_B) to a full heterogeneous, temporally-ordered interaction sequence (swipe→like→match→message) rather than a single recommendation decision; move from pairwise static scoring to per-swipe sequence-level credit across rolling windows.
- **On last-touch:** does not discuss last-touch/last-click directly; instead critiques single-sided, independent evaluation (the structural analogue of ignoring the other side's touch) for double-counting and for missing that bilateral recommendations jointly cause a match.
- **Transfer rating:** adaptable — the causal bilateral-treatment and vacant-slot-opportunity-cost ideas transfer to ranking-time incremental value estimation, but the paper targets one-shot match probability, not multi-touch fractional retention credit over a swipe sequence.
