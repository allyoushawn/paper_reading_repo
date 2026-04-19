Date: 2026-04-12  
Source: https://arxiv.org/pdf/2205.12879  
NLM Source ID: 0bb38cc6-db7a-4197-9cf4-a68b516fb381  
NotebookLM notebook: `proxy-label-learning` (`6fbcf9e6-3833-4660-8b56-67b0b98bf394`)  
Venue: NeurIPS 2022  
Relevance: Core  
Priority: 1

# Paper Analysis: Understanding Programmatic Weak Supervision via Source-aware Influence Function

**Source:** https://arxiv.org/pdf/2205.12879  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Understanding Programmatic Weak Supervision via Source-aware Influence Function

**Authors:** Jieyu Zhang, Haonan Wang, Cheng-Yu Hsieh, Alexander Ratner (University of Washington; UIUC; Snorkel AI)

**Abstract:**  
Standard **influence functions (IF)** attribute test behavior to **whole training points**, but in **programmatic weak supervision (PWS)** labels are **synthesized** from a **label model** over many **(data, LF, class)** contributions. **Source-aware IF** **decomposes** the noise-aware training loss into **(i, j, c)** terms—the effect of LF *j* on class dimension *c* of example *i*—and estimates influence under **reweighting** or **weight-moving** perturbations. Applications: **multi-angle debugging** of mispredictions, **LF mislabeling detection** (+**9–37%** average precision vs. LM/EM/KNN baselines), and **test-loss improvement** by dropping harmful terms (**+13–24%** vs. ordinary IF / group IF in the paper’s framing).

**Key contributions:**
- **Loss decomposition** aligned with PWS probabilistic label construction (unified tensor *W* for MV / identity vs. softmax-style LFs).
- **Reweighting** (additive influences; requires identity aggregation path) vs. **weight-moving** (keeps simplex, aggregation-agnostic).
- **Approximate identity surrogate** for **Dawid–Skene** / **Snorkel MeTaL**-style exponentials via a **least-squares** fit to reproduced soft labels.

**Methodology:**  
13 **classification** datasets from **WRENCH** (Census, IMDb, Yelp, Youtube) plus **Mushroom, Spambase, PhishingWebsites** (tree-induced LFs) and **six DomainNet** domain splits with cross-domain LFs. End model primarily **logistic regression** on BERT/ResNet-18 features; label models **MV, DS, Snorkel**. Baselines: **ERM**, ordinary **IF / RelatIF**, **group IF**, LM/EM/KNN mislabeling scores.

**Main results:**  
Case studies show **same influential point** under ordinary IF can mask **different responsible LFs** across label models; **Spearman 0.71–0.99** between summed source-aware scores and ordinary IF rankings; LF-level influence correlations **~0.675–0.766** averaged (noisy, some cells n.s.).

---

## 2. Experiment Critique

**Design:**  
Strong focus on **interpretability metrics** (AP for LF errors; held-out test loss after pruning). Transductive setup noted for comparability to prior group-IF work.

**Statistical validity:**  
Highlights **significance failures** for some LF influence estimates due to **summation noise**; uses ranking correlation where IF magnitudes are unstable.

**Online experiments (if any):**  
Not specified in source.

**Reproducibility:**  
WRENCH-based codebase; **approximated** DS/Snorkel slightly hurts raw ERM loss vs. originals but **improves best achievable post-IF pruning** in reported figure.

**Overall:**  
Clear **mechanistic** advance for PWS debugging; **theory for IF** largely inherits logistic case; **CNN-scale** end models left to appendix / future work.

---

## 3. Industry Contribution

**Deployability:**  
Tooling mindset: trace bad production behavior to **specific LFs or votes**, not only to rows in *D̂*.

**Problems solved:**  
Operational **PWS triage** when many overlapping rules drive a discriminative student.

**Engineering cost:**  
IF needs **Hessian-vector** machinery; fine-grained decomposition increases bookkeeping vs. vanilla IF.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**  
First **general**, label-model–aware IF that targets **(data, source, class)** primitives vs. **group IF** summing datapoint influences without learnable LM nuance.

**Prior work comparison:**  
**Koh & Liang** IF; **Koh et al.** group influence; **RelatIF**; **Ratner** data programming / Snorkel; **WRENCH** datasets.

**Verification:**  
Empirical gains are **largest** where PWS is messy (DomainNet); behavior aligns with qualitative “who to blame” stories.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| WRENCH subsets | GitHub WRENCH | Yes | Census, IMDb, Yelp, Youtube |
| UCI-style tabular | Open | Yes | Mushroom, Spambase, PhishingWebsites |
| DomainNet | Public | Yes | Six 5-class domain tasks |

**Offline experiment reproducibility:**  
Good via WRENCH; DomainNet LF construction follows cited protocol.

---

## 6. Community Reaction

No significant HN/Reddit thread surfaced in the quick targeted search. **No significant community discussion found** in the scan performed for this batch.

---

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Meta Information

**Authors:** Jieyu Zhang, Haonan Wang, Cheng-Yu Hsieh, Alexander Ratner  
**Affiliations:** University of Washington; University of Illinois Urbana-Champaign; Snorkel AI, Inc.  
**Venue:** NeurIPS 2022  
**Year:** 2022  
**PDF:** downloaded (arXiv)  
**Relevance:** Core  
**Priority:** 1

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
