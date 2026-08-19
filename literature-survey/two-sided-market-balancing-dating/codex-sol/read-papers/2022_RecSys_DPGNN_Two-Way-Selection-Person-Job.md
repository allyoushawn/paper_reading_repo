# Paper Analysis: Modeling Two-Way Selection Preference for Person-Job Fit

**Source:** https://arxiv.org/abs/2208.08612  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Modeling Two-Way Selection Preference for Person-Job Fit  
**Authors:** Chen Yang, Yupeng Hou, Yang Song, Tao Zhang, Ji-Rong Wen, Wayne Xin Zhao  
**Abstract:** Person-job fit is bilateral: candidate interest and employer interest are distinct, and unilateral actions are failed matches. DPGNN represents every candidate and job with separate active-taste and passive-appeal nodes, learns from directed interactions, and ranks pairs by a combined two-way score.

**Key contributions:**
- Introduces an explicit two-way formulation for person-job fit.
- Builds a dual-perspective interaction graph covering mutual and unilateral actions.
- Combines hybrid graph propagation, a quadruple ranking loss, and dual-perspective contrastive learning.

**Methodology:** DPGNN initializes active/passive nodes from ID embeddings and BERT text, propagates matched and unilateral edges with different weights, scores both directions by dot product, averages the two scores, and jointly optimizes a quadruple loss plus InfoNCE alignment.

**Main results:** Against the best hybrid baseline LGCNBERT, average relative improvements are 7.12% on Tech, 4.81% on Sales, and 7.73% on Design. Tech candidate/job Recall@5 rises from 0.2685/0.3187 to 0.2941/0.3430.

---

## 2. Experiment Critique

**Design:** Three real recruitment domains cover 106 days and compare DPGNN with ten collaborative, content, and hybrid baselines. Chronological splits use 84 training, 11 validation, and 11 test days; ablations remove the dual graph, quadruple loss, or contrastive loss.

**Statistical validity:** A paired t-test at 0.01 is reported. DPGNN does not dominate every metric: on Design candidates, LGCNBERT has higher NDCG@5 (0.2498 vs. 0.2478) and MRR@5 (0.2637 vs. 0.2584).

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Code is available at https://github.com/RUCAIBox/DPGNN. Hyperparameter ranges and temporal splits are reported; random seeds are not specified.

**Overall:** Evidence supports improved bilateral offline ranking, especially on the passive/job side. It does not demonstrate more matches, fairer match spread, conversation gains, or retention.

---

## 3. Industry Contribution

**Deployability:** Dot-product scoring is retrieval-friendly, but four representations per pair, BERT initialization, graph propagation, and contrastive training add pipeline cost.

**Problems solved:** Separates outgoing taste from incoming appeal and learns from unilateral rejection signals instead of collapsing all non-matches together.

**Engineering cost:** Requires directional action labels, graph refreshes, text embeddings, negative sampling on both sides, and production handling of profile sparsity.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First explicit dual-perspective graph model of two-way selection preference for person-job fit.

**Prior work comparison:** LightGCN supplies lightweight propagation; BPR supplies pairwise ranking; Zhu et al. and Qin et al. represent text-based person-job fit; Malinowski et al. provide early bilateral matching; LFRR provides reciprocal latent factors.

**Verification:** The primary arXiv paper identifies RecSys 2022 metadata, authors, method, code, and experiments.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Tech recruitment logs | Not specified in source | No | 56,634 candidates, 48,090 jobs, 925,193 matches. |
| Sales recruitment logs | Not specified in source | No | 15,854 candidates, 12,772 jobs, 145,066 matches. |
| Design recruitment logs | Not specified in source | No | 12,290 candidates, 9,143 jobs, 166,270 matches. |

**Offline experiment reproducibility:** Code is public, but the proprietary platform datasets are not linked in the source.

---

## 6. Community Reaction

No significant community discussion found.

---

## Project Relevance

**Mechanism:** Maintain separate active-taste and passive-appeal embeddings for every dater. Encode one-way likes and mutual matches as different graph evidence, estimate both directional affinities, and use the bilateral score for retrieval or ranking.

**Metric/effect:** Offline top-5 ranking improves across three recruitment domains; Tech candidate/job Recall@5 reaches 0.2941/0.3430 versus 0.2685/0.3187 for LGCNBERT. Match volume, conversation rate, match spread, wasted likes, and retention are not specified.

**Capacity/congestion:** Not specified in source. DPGNN models reciprocal preference, not inbox capacity, congestion, exposure concentration, marketplace feedback, or interference.

**Dating mapping:** Candidate/job active nodes map to outgoing dater taste; passive nodes map to profile appeal. Applications and recruiter outreach map to directional likes; interviews map to mutual matches. Dating has symmetric human roles, shorter text, and tighter concurrent-conversation capacity than recruitment.

**Dating fit: Medium.** Strong Layer-1 reciprocal scorer, but it needs a separate capacity-aware allocator and ecosystem evaluation.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2023_KDD_BOSS_Bilateral-Occupational-Suitability.md](./2023_KDD_BOSS_Bilateral-Occupational-Suitability.md) | Novelty vs. Prior Work — Background | Says DPGNN motivates two-way preference. |
| [2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md](./2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md) | Experiment Critique / Main results — Direct baseline | Reports Technology HR@5 against DPGNN as a quantitative comparator. |
| [2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems.md](./2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems.md) | Experiment Critique / Main results — Direct baseline | Uses DPGNN as a dating-data quantitative comparator. |

---

## Meta Information

**Authors:** Chen Yang, Yupeng Hou, Yang Song, Tao Zhang, Ji-Rong Wen, Wayne Xin Zhao  
**Affiliations:** Renmin University of China; BOSS Zhipin; Beijing Academy of Artificial Intelligence  
**Venue:** RecSys 2022  
**Year:** 2022  
**PDF:** available via arXiv  
**Relevance:** Core  
**Priority:** 1

---

## Annotated Bibliography Fields

**Title:** Modeling Two-Way Selection Preference for Person-Job Fit  
**Authors/org:** Chen Yang, Yupeng Hou, Yang Song, Tao Zhang, Ji-Rong Wen, Wayne Xin Zhao; Renmin University of China and BOSS Zhipin  
**Year:** 2022  
**Venue/type:** RecSys 2022; conference paper  
**Verified link:** https://arxiv.org/abs/2208.08612  
**Tier:** 1  
**What they did:** DPGNN splits every candidate and job into active and passive graph nodes, propagates mutual and unilateral interactions separately, combines two directional scores, and trains with a bilateral quadruple loss plus contrastive alignment. It is evaluated on three large recruitment domains against ten baselines.  
**Mechanism:** Separate outgoing taste from incoming appeal, learn from one-way likes as well as matches, then combine both directions into one reciprocal score.  
**Metrics/effect:** Average lift over LGCNBERT: 7.12% Tech, 4.81% Sales, 7.73% Design. Tech candidate/job Recall@5: 0.2941/0.3430 vs. 0.2685/0.3187.  
**Dating fit + reason:** Medium — directly useful for like-back scoring, but it has no capacity, congestion, exposure-spread, conversation, or retention objective.  
**Confidence:** High — primary paper and source-scoped evidence; proprietary datasets limit independent reproduction.
