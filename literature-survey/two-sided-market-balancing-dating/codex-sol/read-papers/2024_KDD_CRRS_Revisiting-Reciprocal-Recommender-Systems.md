# Paper Analysis: Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method

**Source:** https://arxiv.org/abs/2408.09748  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method  
**Authors:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu  
**Abstract:** The paper argues that separately scored top-K metrics double-count redundant bilateral recommendations and miss population imbalance. It introduces coverage-, stability-, and balance-aware metrics, then formulates recommendation direction as bilateral causal treatments and reranks with vacant-slot alternatives to maximize unique matches.

**Key contributions:**
- Proposes CRecall/CPrecision, SRecall/SPrecision, and RNDCG for holistic reciprocal evaluation.
- Models one-sided and bilateral exposure as treatment assignments with separate potential outcomes.
- Introduces model-agnostic CRRS pretraining, treatment-specific fine-tuning, and vacant-slot reranking.

**Methodology:** For each pair, CRRS estimates potential match outcomes under treatments 10, 11, and 01 with separate BPRMF or LightGCN backbones. Models are pretrained on match labels and fine-tuned on treatment-specific data. Reranking compares bilateral recommendation with one-sided recommendations plus the expected match value of filling the released slot with another user.

**Main results:** On Libimseti dating data, CRRS-LightGCN reaches CRecall@50 0.3387, CPrecision@50 0.0075, and 1,743 true-positive pairs versus DPGNN at 0.3007, 0.0067, and 1,548. On recruitment data, CRRS-BPRMF reaches CRecall@50 0.3968 and 8,913 pairs versus LFRR at 0.3530 and 7,929.

---

## 2. Experiment Critique

**Design:** Two real datasets cover recruitment and dating, with 5-core filtering and 8:1:1 splits. Baselines span BPRMF, LightGCN, independent two-sided variants, LFRR, and DPGNN; ablations remove pretraining, causal fine-tuning, or reranking.

**Statistical validity:** Exact offline metrics are reported, but confidence intervals, significance tests, repeated seeds, and propensity-identification diagnostics are not specified. Libimseti uses mutual ratings at least 8 as a match proxy rather than observed app conversations.

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Code and data are linked by the authors. Recruitment logs may have access constraints, while Libimseti is public; preprocessing details and model backbones are documented.

**Overall:** Results support higher unique-match coverage and the contribution of pretraining/reranking. The method has an explicit coverage-stability trade-off and does not dominate on every single-sided metric.

---

## 3. Industry Contribution

**Deployability:** Model-agnostic heads can reuse familiar MF or graph backbones, but maintaining three treatment models plus sampled vacant-slot estimates increases training and serving complexity.

**Problems solved:** Redundant bilateral exposure, metric double-counting, crowding in top ranks, and unbalanced market populations.

**Engineering cost:** Requires reliable directional treatment labels, counterfactual fine-tuning, three outcome models, and reranking with sampled alternative candidates.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A unified reciprocal evaluation suite plus a causal bilateral-treatment formulation and reranker that optimizes unique match coverage.

**Prior work comparison:** Su et al. (2022) motivate total matched pairs; Rubin (1980) grounds potential outcomes; Pizzato et al. (2010) is an early dating RRS; Yang et al. (2022) provide DPGNN and recruitment data; He et al. (2020) provide LightGCN; Rendle et al. (2009) provide BPR; Gale and Shapley (1962) ground matching theory.

**Verification:** The arXiv record, KDD 2024 metadata, and author repository verify the title, authors, venue, code, and dataset claim.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Recruitment logs | Author repository | Partially | 32,161 candidates, 25,665 recruiters, 790,725 interactions, 224,636 matches; two weeks. |
| Libimseti dating | http://konect.cc/networks/libimseti/ | Yes | 6,391/6,516 users, 605,288 interactions, 51,474 mutual-rating matches after filtering. |

**Offline experiment reproducibility:** Relatively strong for Libimseti and the released code; exact recruitment-data access should be checked.

---

## 6. Community Reaction

The paper has public technical summaries and indexed implementations, but no substantial independent reproduction or controversy was found.

---

## Project Relevance

**Exact mechanism:** Treat showing each side as a separate intervention, estimate match outcomes for one-sided and bilateral exposure, and choose between them while accounting for the match value of any newly vacant slot. This reduces duplicate recommendations that do not add unique matched pairs.

**Metrics and reported effect:** CRecall/CPrecision measure unique match coverage, SRecall/SPrecision measure mutual recommendation stability, RNDCG balances side sizes, and true-positive pairs count distinct successes. Dating CRRS-LightGCN improves CRecall@50 from 0.3007 to 0.3387 and pairs from 1,548 to 1,743 versus DPGNN.

**Capacity/congestion relevance:** It explicitly reallocates scarce list slots and documents redundant recommendations concentrated at ranks 1-15. It does not impose hard reply capacity or model message queues; RNDCG addresses side-size imbalance rather than individual popularity inequality. Interference is not modeled.

**Practical mapping:** A dating system can compare the marginal match value of showing a pair bilaterally against using one of those impressions for another pair. Conditioning that vacant-slot value on inbox load would be an additional capacity extension, not part of the paper.

**Dating fit: High.** The method directly optimizes distinct reciprocal outcomes and provides metrics that expose duplicate or imbalanced recommendation behavior.

**Not specified in source:** hard capacity limits; reply-delay congestion; conversation outcomes; match Gini; wasted-like rate; two-sided retention; online A/B tests; marketplace-interference correction.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

---

## Meta Information

**Authors:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu  
**Affiliations:** Renmin University of China; BOSS Zhipin / Kanzhun  
**Venue:** KDD 2024  
**Year:** 2024  
**PDF:** available via arXiv  
**Relevance:** Core  
**Priority:** 1

---

## Annotated Bibliography Fields

**Full title:** Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method  
**Authors/org:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu; Renmin University of China and BOSS Zhipin  
**Year:** 2024  
**Venue/type:** KDD 2024; conference paper  
**Verified link:** https://arxiv.org/abs/2408.09748  
**Tier:** 1  
**What they did:** They add five holistic reciprocal metrics, formulate two-sided recommendations as bilateral causal treatments, and train CRRS with treatment-specific outcome models plus vacant-slot reranking to maximize distinct matches.  
**Two-sided mechanism:** CRRS compares one-sided and bilateral exposure outcomes and redirects redundant recommendation slots to alternatives with higher total expected match value.  
**Metrics and reported effect:** Dating CRRS-LightGCN: CRecall@50 0.3387, CPrecision@50 0.0075, 1,743 pairs; DPGNN: 0.3007, 0.0067, 1,548. Recruitment CRRS-BPRMF: 0.3968 and 8,913 vs. LFRR 0.3530 and 7,929.  
**Dating fit:** High — targets unique reciprocal outcomes and scarce exposure slots, though not hard reply capacity.  
**Confidence real/correct:** High — primary paper, KDD metadata, author code/data link, and source-scoped evidence.

---

*To run experiments on Libimseti, use the experiment-runner workflow with the dataset URL above.*
