# Paper Analysis: Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method

**Source:** `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2408.09748.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method
**Authors:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao (corresponding), Jun Xu, Yang Song, Hengshu Zhu
**Affiliations:** Nanbeige Lab/BOSS Zhipin, Gaoling School of AI at Renmin University of China, UC San Diego, Career Science Lab at BOSS Zhipin
**Venue:** KDD '24 (30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining), Barcelona, Spain, August 2024. Code released at https://github.com/RUCAIBox/CRRS.

**Abstract/framing:** The paper argues that the majority of existing RRS work evaluates each side of a reciprocal recommendation independently using conventional single-sided ranking metrics (Recall, Precision, NDCG), which overlooks that a match requires *both* sides' recommendations to succeed jointly, and that recommending the same pair on both sides is redundant (it should count as one successful outcome, not two). The paper (1) proposes five new evaluation metrics from three perspectives — overall coverage, bilateral stability, balanced ranking; (2) reformulates RRS from a causal perspective as **bilateral treatments** (recommend-A-to-B and recommend-B-to-A as two separate treatment variables) under the potential-outcome framework; (3) proposes a model-agnostic method, **Causal Reciprocal Recommender System (CRRS)**, that estimates the causal effect of each of the four treatment combinations and reranks accordingly.

**Key contribution:** A worked demonstration that traditional metrics (Recall/Precision/NDCG computed per side) cannot distinguish between recommendation strategies that produce very different actual match counts, plus a concrete evaluation-metric and causal-modeling fix.

**Methodology:** RRS is formulated with bilateral treatments $T_A, T_B \in \{0,1\}$ for a user pair $(a_i, b_j)$ — $T_A=1$ means $b_j$ is recommended to $a_i$; $T_B=1$ means $a_i$ is recommended to $b_j$. Under the potential-outcome framework, three predictive functions are learned — $\hat y_{10}, \hat y_{11}, \hat y_{01}$ — estimating the matching probability under each observable treatment combination (the $T_A{=}0,T_B{=}0$ case trivially yields $\hat y_{00}=0$, since neither side is shown the other). Training proceeds in two stages: (1) pretrain a backbone (BPRMF or LightGCN) with real matched data using BPR loss; (2) counterfactually finetune three treatment-specific heads on data partitioned by observed treatment, using a "similar users have similar treatment effects" collaborative-estimation assumption to work around the fundamental unobservability of counterfactual outcomes. Ranking scores are $s_{a_i} = \hat y_{10} + \hat y_{11}$, $s_{b_j} = \hat y_{01} + \hat y_{11}$, refined by a reranking strategy that also accounts for "vacant slot" expectations (the possibility that an unrecommended side introduces a new match opportunity elsewhere).

**Main results:** On two real-world datasets (Recruitment: 32,161/25,665 users, 790,725 interactions, 224,636 matches; Dating [Libimseti.cz]: 6,391/6,516 users, 605,288 interactions, 51,474 matches — mutual rating ≥8 defined as a match), CRRS outperforms MF-based (BPRMF, D-BPRMF, LFRR) and graph-based (LightGCN, D-LightGCN, DPGNN) baselines on the paper's proposed coverage metrics. E.g., on Recruitment, CRRS(BPRMF) achieves CRecall@50 = 0.3968 vs. best baseline LFRR's 0.3550 (statistically significant, paired $t$-test $p<0.05$), with 8,913 true positive pairs vs. LFRR's 7,929; CRRS(LightGCN) achieves CRecall@50 = 0.4670 vs. DPGNN's 0.4555, with 10,490 true positive pairs vs. 10,231. On Dating, CRRS(BPRMF) reaches CRecall@50 = 0.3086 (True Positive Pairs 1,588) vs. LFRR's 0.3045 (1,567); CRRS(LightGCN) reaches CRecall@50 = 0.3387 (1,743) vs. DPGNN's 0.3007 (1,548).

## 2. Experiment Critique

**Design:** Full-ranking evaluation (every candidate ranked, $K=50$) on two real-world, large-scale datasets; 8:1:1 train/val/test split; embedding dimension standardized at 128 across all methods; hyperparameter search over learning rates; early stopping (patience 30). Statistical significance is reported (paired $t$-test, $p<0.05$) for the headline improvements. An ablation study (Table 4) isolates the contribution of finetuning, pre-training, and reranking, and a further analysis (Figure 5) examines where redundant recommendations concentrate in the ranking list. **Online experiments:** none — this is purely an offline evaluation study. **Reproducibility:** code and (for Dating) a public dataset (Libimseti.cz, via konect.cc) are available; the Recruitment dataset is proprietary (from BOSS Zhipin, a real recruitment platform).

**Limitations/negative results stated by authors:** A genuine trade-off is reported and not hidden: on Recruitment, CRRS improves CRecall (0.4670 vs. DPGNN's 0.4555) but at the cost of a *fall* in SRecall — the bilateral-stability metric — from DPGNN's 0.1535 to CRRS's 0.1248, i.e., reducing redundant recommendations to raise overall coverage can reduce the rate of mutual (both-sides) recommendation, which the authors note is "normal when trying to reduce redundant recommendations." This trade-off does *not* appear in the Dating dataset, and the authors explicitly flag they are unsure why ("possibly because there is a significant difference in sparsity between the two datasets ... with even greater sparsity differences on '#Interactions'" — stated as a hypothesis, not a confirmed cause). The ablation study also shows the reranking strategy's benefit is "relatively modest" on the Dating dataset. Separately, Figure 5 shows redundant recommendations concentrate in the top ranking positions, leading the authors to note that "an objective of directly optimizing the discrepancy between both sides' ranking lists may be ineffective" — a stated negative result about a simpler alternative approach.

## 3. Industry Contribution

CRRS is model-agnostic (validated on both MF-based and graph-based backbones) and is positioned as a drop-in causal reranking layer rather than a full architecture replacement, which lowers integration cost. Engineering cost is nontrivial, however: it requires (a) partitioning training data by observed bilateral-treatment combination, (b) three separate treatment-conditioned model heads with a two-stage pretrain/finetune pipeline, and (c) a reranking step that samples candidate users to estimate "vacant slot" expectations at serving time. No latency or serving-cost analysis is reported — this is presented purely as an offline-trainable/offline-evaluable method.

## 4. Novelty vs. Prior Work

The central novelty claim, and the one most load-bearing for the survey, is methodological: prior RRS work (Pizzato et al. 2010's RECON; Neve and Palomares 2019's aggregation-operator survey; Tomita et al. 2022's matching-theory RRS — Paper 1 in this batch; and the broader field surveyed by Palomares et al. 2021) evaluates each side independently with standard ranking metrics, which the authors demonstrate (Figure 2, a worked three-scenario example) is provably insufficient: three distinct top-1 recommendation strategies yield identical Recall/Precision/NDCG (all 0.5) but produce 4, 2, and 3 actual matched pairs respectively — traditional metrics cannot distinguish them, while the paper's CRecall and SRecall do. On the causal-formulation side, the paper draws on the general causal-inference-in-recommendation literature (Rubin 1980's potential-outcome framework; Pearl 2009's causal-inference foundations) and applies it specifically to bilateral (two-sided) treatments, which the authors state is a novel application in the RRS context.

## 5. Dataset Availability

| Dataset | Public? | #Users (A/B) | #Interactions | #Match | Sparsity |
|---|---|---|---|---|---|
| Recruitment | No (proprietary, BOSS Zhipin) | 32,161 / 25,665 | 790,725 | 224,636 | 99.90% |
| Dating (Libimseti.cz) | Yes (via konect.cc) | 6,391 / 6,516 | 605,288 | 51,474 | 98.55% |

Note: the "Dating" dataset is an older rating-based dating site (mutual ratings ≥8 between opposite-sex pairs proxy for a "match"), structurally different from a modern swipe-based app like Tapple or Tinder — no like/dislike swipe action, no chat-unlock event, and no session or time-decay structure is used.

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Value |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method; Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu (Nanbeige Lab/BOSS Zhipin, Renmin University of China, UC San Diego); KDD '24; 2024; https://doi.org/10.1145/3637528.3671734 (arXiv: https://arxiv.org/abs/2408.09748) |
| 2 | Source type | Academic (industry co-authored — BOSS Zhipin) |
| 3 | Direction | D8 |
| 4 | Problem setting | Reciprocal recommendation across two real-world two-sided markets (recruitment and online dating). Both sides receive ranked recommendation lists; a successful outcome (match) requires both sides to be recommended to each other. |
| 5 | Objective and label definition | No retention/revenue objective and no time horizon. The label is a binary, immediately-observed match event (actual mutual selection for Recruitment; mutual rating ≥8 for Dating). Recruitment data spans "two weeks of real logs," but this is the data-collection window, not a label horizon — the match label itself carries no delay. Horizon and delay handling beyond this: Not specified in source. |
| 6 | Prediction or incrementality | Addresses a form of incrementality distinct from the project's needs: CRRS estimates the *causal effect of the recommendation itself* (bilateral treatment $T_A, T_B$) on immediate match probability via a potential-outcome framework — this is causal with respect to whether showing a profile causes a match, not causal with respect to downstream retention or revenue. It does not estimate incrementality over any delayed outcome. |
| 7 | Model architecture | Model-agnostic causal framework layered on MF-based (BPRMF) or graph-based (LightGCN) backbones. Three treatment-conditioned prediction heads estimate potential outcomes $\hat y_{10}, \hat y_{11}, \hat y_{01}$ from shared pretrained user embeddings via a two-stage pretrain/counterfactual-finetune pipeline (BPR loss with negative sampling per treatment partition), followed by a reranking strategy incorporating vacant-slot expectations via an IsMax selection rule. |
| 8 | Credit assignment | The paper's core mechanism: a "vacant slot" reasoning process. When one side lacks a recommendation ($T_A{=}0$), the expected value of what *would* be recommended in that slot, $\bar y(a_i)$, is estimated by sampling candidates from the opposite side and averaging relevance scores from the backbone model; this combines with the direct treatment outcome to form the global match expectation. This is single-round, item-level (one recommendation slot) credit assignment — not delayed-outcome-to-impression attribution in the project's sense. |
| 9 | Training data and counterfactual handling | Real matched interaction logs, partitioned by observed bilateral-treatment combination ($T_{11}, T_{10}, T_{01}$ subsets) for counterfactual finetuning. The paper explicitly names the fundamental problem — "there is only one intervention per sample in RRS. We cannot observe the final results of different treatments for the same pair... this is a counterfactual problem" — and addresses it via a similarity-based collaborative-estimation assumption ("similar users have similar treatment effects under recommendations"), not via randomization or an instrumental variable. |
| 10 | Offline and online evaluation | Offline only. Full-ranking evaluation ($K=50$) with standard metrics (Recall, Precision, NDCG) plus the paper's five proposed metrics (CRecall, CPrecision, SRecall, SPrecision, RNDCG) on the Recruitment and Dating datasets. No online experiment. |
| 11 | Reported gains | On Recruitment, CRecall@50 improves from 0.3550 (LFRR, best baseline) to 0.3968 (CRRS/BPRMF), true positive pairs from 7,929 to 8,913 ($p<0.05$); CRecall@50 improves from 0.4555 (DPGNN) to 0.4670 (CRRS/LightGCN), true positive pairs from 10,231 to 10,490. On Dating (Libimseti.cz), CRecall@50 improves from 0.3045 (LFRR) to 0.3086 (CRRS/BPRMF) and from 0.3007 (DPGNN) to 0.3387 (CRRS/LightGCN). |
| 12 | Applicability to a two-sided dating recommender | The paper's five evaluation metrics — especially CRecall/CPrecision (avoiding double-counting bilateral matches) and SRecall/SPrecision (bilateral/mutual-recommendation rate) — are directly reusable as reciprocal-specific offline metrics for the survey's evaluation plan, since standard ranking metrics provably cannot capture mutual acceptance (Figure 2's worked example). Its causal framing addresses recommendation→match causality, not exposure→retention/revenue causality, so it does not directly answer the project's incrementality question. |
| 13 | Unverified claims | The authors' hypothesis for why the Recruitment coverage/stability trade-off doesn't appear in the Dating dataset ("possibly because there is a significant difference in sparsity between the two datasets") is explicitly labeled by the authors themselves as speculative, not confirmed by further experiments in this paper. |

## Project Relevance

This paper is the survey's clearest source for **Q6** (offline/online evaluation under two-sided interference): it directly argues, with a worked counterexample, that standard single-sided ranking metrics (Recall/Precision/NDCG) cannot capture mutual acceptance in a reciprocal market, and proposes five concrete metrics — Coverage-adjusted Recall/Precision (CRecall/CPrecision), Stability-adjusted Recall/Precision (SRecall/SPrecision), and Reciprocal NDCG (RNDCG, population-size-weighted to handle side-size imbalance/"crowding") — that the survey's evaluation-plan deliverable can adopt directly. It also speaks to **Q5** in a qualified way: it introduces a causal/potential-outcome framing for RRS, but the causal target is recommendation→match, not exposure→retention/revenue, so it is a structural analogy for the project's incrementality question rather than a direct answer. It touches **Q2** via its "vacant slot" credit-assignment mechanism, though again at the single-impression, not delayed-outcome, level. It does not address **Q1, Q3, Q4, Q8** — no retention/revenue objective, no horizon, no short/long-term head fusion, no migration path.

Horizon verdict: none — static snapshot.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `CRRS`._

## Meta Information

- **Authors:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu
- **Affiliations:** Nanbeige Lab/BOSS Zhipin, Gaoling School of Artificial Intelligence (Renmin University of China), University of California San Diego, Career Science Lab/BOSS Zhipin
- **Venue:** KDD '24 (30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- **Year:** 2024
- **Relevance:** Core
- **Priority:** 1
- **Source ID:** `nlm:0e509aae`
