# Paper Analysis: Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction

**Source:** https://ojs.aaai.org/index.php/AAAI/article/view/25583/25355  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction  
**Authors:** Hongzu Su; Zhekai Du; Jingjing Li; Lei Zhu; Ke Lu  
**Abstract:** CDAF transfers LTV signal from a data-rich advertising platform to a sparse target platform by Wasserstein-aligning user representations while dual predictors retain target-specific structure.  
**Methodology:** Pretrain source LTV model, fine-tune target encoder, minimize cross-domain Wasserstein discrepancy, and optimize invariant/specific dual predictors.  
**Main results:** Across five Tencent Games datasets and eight backbones, CDAF consistently improves AUC/Gini; on G2 it raises DCNv2 AUC from 0.633 to 0.720 (+13.7%).

## 2. Experiment Critique

**Design:** Five three-month historical domains; DNN/WDL/DCN/DeepFM/FibiNet/GateNet/DCNv2/mixed backbones; ablations.  
**Statistical validity:** Significant improvements are stated; no online A/B.  
**Online experiments:** None specified.  
**Reproducibility:** Code link is provided; data proprietary.  
**Overall:** Good transfer-learning evidence for scarce LTV labels, but AUC/Gini do not validate monetary calibration or ranking impact.

## 3. Industry Contribution

**Deployability:** Compatible with many backbones; production lift not shown.  
**Problems solved:** Sparse target-domain consumption and source-target distribution gap.  
**Engineering cost:** Source/target data governance, dual predictors, domain-alignment training.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First supervised domain-adaptive LTV framework.  
**Prior work comparison:** Deep LTV prediction and domain adaptation.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Five Tencent Games ad datasets | Not specified in source. | No | Three-month historical consumption. |

**Offline experiment reproducibility:** Code available at https://github.com/TL-UESTC/CDAF; data unavailable.

## 6. Community Reaction

Not specified.

## Survey Card Fields

**Source type:** Industry paper  
**Direction:** D4  
**Problem setting:** Data-sparse ad-platform user LTV prediction using another domain.  
**Objective and label definition:** Potential customer consumption/profit over a period; three months of data, but exact label horizon, delay, zero handling, and censoring Not specified.  
**Prediction or incrementality:** Prediction, not incremental effect.  
**Model architecture:** Cross-domain encoder alignment with Wasserstein distance and dual predictors.  
**Credit assignment:** User-level LTV only; no item/exposure attribution.  
**Training data and counterfactual handling:** Observational source/target consumption; no propensity correction.  
**Offline and online evaluation:** Offline AUC/Gini only.  
**Reported gains:** Up to 13.7% AUC improvement cited on G2/DCNv2.  
**Unverified claims:** Monetary error/calibration and deployment lift absent.

## Project Relevance

**Source-stated facts:** Cross-domain transfer can make a sparse LTV head viable in a new/low-data domain while limiting distribution-shift harm.

**Survey inference:** Dating revenue is sparse by segment/market, so transfer across geographies or products may help. It does not connect a shown profile to revenue, estimate uplift, or model reciprocity, congestion, interference, and positive churn.

**Applicability note:** Useful support for cold-starting sparse dating revenue heads across markets.  
Not a unified ranking or causal credit-assignment solution.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Hongzu Su et al.  
**Affiliations:** UESTC; Tencent internship context  
**Venue:** AAAI  
**Year:** 2023  
**PDF:** Available  
**Relevance:** Core  
**Priority:** 1
