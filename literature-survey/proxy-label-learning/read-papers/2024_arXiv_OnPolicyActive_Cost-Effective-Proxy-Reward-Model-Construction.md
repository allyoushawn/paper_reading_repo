# Paper Analysis: Cost-Effective Proxy Reward Model Construction with On-Policy and Active Learning

**Source:** https://arxiv.org/pdf/2407.02119  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Cost-Effective Proxy Reward Model Construction with On-Policy and Active Learning  
**Authors:** Yifang Chen, Shuohang Wang, Ziyi Zhang, Hiteshi Sharma, Nikos Karampatziakis, Donghan Yu, Kevin Jamieson, Simon Shaolei Du, Yelong Shen  
**Abstract:** RLHF pipelines are bottlenecked by preference labeling costs. The paper studies building a weak evaluation model (proxy reward oracle) under very small expert-query budgets, using on-policy generations to avoid seed distribution shift/bias and active learning (coreset-style selection) to query the most informative (prompt, response, criterion) tuples. The trained proxy is used to label many more preference pairs for downstream DPO training.

**Key contributions:**
- On-policy expert querying for EFT construction to mitigate OOD and reward imbalance issues versus seed-only training signals.
- Active learning variants (`coresetEFT`, `coresetIFT`) based on k-center / greedy coreset ideas applied to embeddings from the policy model.
- Empirical demonstration that a small expert-labeled set can support labeling ~9× more DPO pairs than queried, with reported gains on instruction/knowledge benchmarks under ~1.7K-query budgets.

**Methodology:**  
Pipeline: SFT seed → policy generates many responses on unlabeled prompts → select a small subset for expert scoring → train `M_eval` → pseudo-label remaining pool → form DPO pairs (high vs low scored per prompt) → train `M_2` with DPO. Evaluates against random on-policy selection, off-policy adaptations, and SPIN-style self-play baselines under small-seed constraints.

**Main results:**  
Example headline claim: with ~1.7K queries, DPO on Llama-2 7B with ~15K proxy-labeled pairs improves >1% average on AlpacaEval2 and MMLU (5-shot) vs initial SFT, while direct expert labeling without proxy training yields <0.1% improvement under the same budget (per paper text summarized by NLM).

---

## 2. Experiment Critique

**Design:**  
The setting intentionally stresses extreme data scarcity (≈3K seed SFT; small query budgets). This is good for isolating oracle-construction effects but limits absolute performance claims.

**Statistical validity:**  
Paper reports averaging across multiple seeds with total variance decomposition in places; NLM excerpts include `√tv` style reporting for some tables.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
Depends on GPT-judge templates, subsampling of Super-NaturalInstructions prompts, and training details for `M_eval`; some details deferred to appendices in the PDF.

**Overall:**  
Clear, practically motivated contribution orthogonal to “better DPO loss” research: it targets *where to spend expert budget* when building proxy judges.

---

## 3. Industry Contribution

**Deployability:**  
Highly relevant when teams can generate many candidate responses cheaply but can only afford limited strong-model/human judgments. The method is compatible with DPO-family training and could compose with external RM resources (authors note some external-RM settings are out of scope).

**Problems solved:**  
Constructing scalable proxy supervision for preference learning—directly parallel to proxy-label workflows in ranking (cheap impressions, expensive human relevance).

**Engineering cost:**  
Adds embedding extraction + coreset selection + an extra training stage for the evaluator; still likely cheaper than fully expert-labeling large preference sets.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First focused study of cost-effective proxy oracle construction under tiny budgets, combining on-policy querying with active selection; contrasts with self-rewarding LM (Yuan et al.) emphasis and settings.

**Prior work comparison:**  
Positions against offline PairRM-style oracles requiring large preference corpora, and against SPIN-like methods that avoid expert queries but need large clean seeds.

**Verification:**  
arXiv:2407.02119; Microsoft + UW authorship. Not specified in source whether peer-reviewed venue version exists.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| OpenAssistant oasst1 (subset) | public | Yes | seed SFT / seed prompts lineage |
| Super-NaturalInstructions (prompt pool) | public | Yes | unlabeled prompts for generation |
| AlpacaEval2 / MMLU / BBH | public | Yes | downstream evaluation suites |

**Offline experiment reproducibility:**  
Feasible in principle with released artifacts, but judge templates and exact subsampling matter.

---

## 6. Community Reaction

No significant community discussion found in this NotebookLM-derived pass.

**Relevance to proxy label learning:** Core. The evaluator is explicitly a proxy labeler for preferences, trained from sparse trusted labels and used to propagate supervision.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Yifang Chen, Shuohang Wang, Ziyi Zhang, Hiteshi Sharma, Nikos Karampatziakis, Donghan Yu, Kevin Jamieson, Simon Shaolei Du, Yelong Shen  
**Affiliations:** University of Washington; Microsoft Corporation (per PDF header in source)  
**Venue:** arXiv (2407.02119)  
**Year:** 2024  
**PDF:** available at https://arxiv.org/pdf/2407.02119  
**Relevance:** Core  
**Priority:** 2  
**NLM Source ID:** e4e78b35-1a30-4b6d-91a7-bc0d9f866ec2

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
