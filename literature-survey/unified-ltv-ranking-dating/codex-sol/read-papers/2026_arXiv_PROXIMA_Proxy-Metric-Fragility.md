# Paper Analysis: PROXIMA

**Source:** https://arxiv.org/abs/2604.14352  
**Date analyzed:** 2026-08-18  
**Extraction mode:** NotebookLM indexed source content fallback (generative query throttling)

## 1. Summary

**Title:** PROXIMA: Proxy Metric Validation with Segment-Level Fragility Detection for Online Controlled Experiments  
**Authors:** Avinash Amudala  
**Abstract:** PROXIMA audits whether a fast experimental proxy gives the same ship/no-ship direction as a slow long-term outcome and detects segments where that relationship reverses.  
**Methodology:** A composite reliability score combines normalized cross-experiment effect correlation, directional accuracy, and one minus segment-level sign-flip fragility. A decision simulator reports oracle agreement, false decisions, and regret.  
**Main results:** Across 80 simulated experiments, early engagement scores 0.80 on Criteo and 0.62 on KuaiRec and averages 98.4% oracle decision agreement. Fragility is 13% in advertising versus 68% in recommendation, while directional accuracy exceeds 96% in both.

## 2. Experiment Critique

**Design:** Fifty simulated Criteo uplift experiments and thirty simulated KuaiRec experiments, segment analyses, baseline comparisons, weight sensitivity, and 1,000-resample bootstrap intervals.  
**Statistical validity:** Multiple reliability dimensions and bootstrapping are strengths. However, both corpora are partitioned into simulated experiments rather than independent treatments; segment sign flips lack multiple-testing correction and weights are heuristic.  
**Online experiments:** No; controlled experiments are simulated from public datasets.  
**Reproducibility:** Code and scripts are public at https://github.com/Avinash-Amudala/PROXIMA/.  
**Overall:** Practical proxy-governance diagnostic, but evidence does not yet show prospective launch performance on a real experiment corpus.

## 3. Industry Contribution

**Deployability:** Lightweight processing (about five minutes for 13.9M Criteo rows on a 16-core laptop) and dashboard/API workflow suit experimentation platforms.  
**Problems solved:** Aggregate-correlation blind spots, Simpson-style segment reversals, and unsafe reliance on fast engagement metrics.  
**Engineering cost:** Historical experiment-effect store, stable segment definitions, long-term outcomes, bootstrap/decision simulation, and periodic revalidation.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Direct proxy reliability auditing and segment fragility detection rather than constructing or predicting an optimal surrogate endpoint.  
**Prior work comparison:** Complements surrogate indices, proxy portfolio selection, CATE discovery, and heterogeneous-impact monitoring.  
**Verification:** Indexed source only.

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---|---|---|---|
| Criteo Uplift | https://ailab.criteo.com/criteo-uplift-prediction-dataset/ | Yes | 13,979,592 observations. |
| KuaiRec | Not specified in source. | Yes | 7,176 users, 1,411,327 interactions. |
| PROXIMA code | https://github.com/Avinash-Amudala/PROXIMA/ | Yes | Reproduction scripts. |

**Offline experiment reproducibility:** High for the paper's simulated evaluation.

## 6. Community Reaction

Not specified in source.

## Survey Card Fields

**Source type:** Academic paper  
**Direction:** D3  
**Problem setting:** Validating early proxy metrics for launch decisions when true retention or lifetime revenue matures slowly and effects vary by segment.  
**Objective and label definition:** Reliability combines correlation of proxy/long-term ATEs, agreement of effect signs, and segment sign-flip rate; oracle decision uses long-term ATE direction.  
**Prediction or incrementality:** Experiment-level causal treatment-effect diagnostic, not individual prediction.  
**Model architecture:** Deterministic composite scorer, fragility detector, bootstrap inference, and counterfactual ship/no-ship simulator.  
**Credit assignment:** Treatment effects are computed separately for proxy and long-term outcomes per experiment and segment; no user-level temporal attribution.  
**Training data and counterfactual handling:** Randomized/simulated treatment-control comparisons; no learned model is required.  
**Offline and online evaluation:** Two public datasets and 80 simulated experiments; no live validation.  
**Reported gains:** 98.4% average oracle agreement; composite reliability 0.80 Criteo and 0.62 KuaiRec; fragility 13% vs 68%.  
**Unverified claims:** Real experiment-corpus performance, recommended score thresholds, segmentation robustness, temporal drift, and causal sufficiency of proxies remain unverified.

## Project Relevance

**Source-stated facts:** Recommendation proxies can retain high global direction accuracy while reversing in 68% of segment checks, and the method recommends segment guardrails plus repeated validation against the true long-term outcome.

**Survey inference:** Before using likes, matches, replies, session time, or short retention as dating-LTV objectives, build a historical treatment-effect matrix and audit direction by tenure, gender/orientation, activity, subscription, geography, and candidate-load segments. PROXIMA validates a proxy but does not construct the unified LTV label.

**Applicability note:** Directly useful as a gate for dating proxy and north-star metric selection.  
Use alongside surrogate construction and real long-horizon holdouts.

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

## Meta Information

**Authors:** Avinash Amudala  
**Affiliations:** Rochester Institute of Technology  
**Venue:** arXiv  
**Year:** 2026  
**PDF:** Available  
**Relevance:** Core measurement reference  
**Priority:** 1
