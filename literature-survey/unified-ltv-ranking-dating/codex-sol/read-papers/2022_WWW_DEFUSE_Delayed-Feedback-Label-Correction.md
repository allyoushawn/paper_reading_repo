# Paper Analysis: Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction

**Source:** https://doi.org/10.1145/3485447.3511965  
**Source ID:** d16aaef1-3541-47de-9542-b6cb80a8e3f4  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Authors:** Yu Chen; Jiaqi Jin; Hui Zhao; Pengjie Wang; Guojun Liu; Jian Xu; Bo Zheng  
**Abstract:** DEFUSE separates immediate positives, fake negatives, real negatives, and delayed positives. A two-step procedure estimates fake-negative probability then applies type-specific importance weights; Bi-DEFUSE jointly models unbiased immediate positives and biased delayed conversions.

**Main results:** On Criteo-30d/1d and 5.2B-row Taobao streams, DEFUSE/Bi-DEFUSE improved the strongest baseline’s RI-AUC by 6.22%, 2.13%, and 15.31%. Taobao AUC rose to 0.8080 (66.33% RI-AUC) versus ES-DFM 0.8066.

---

## 2. Experiment Critique

**Design:** Hourly train-next-hour simulation, two attribution windows, public/industrial data, eight baselines, five runs, pipeline combinations, and ablations.

**Statistical validity:** Average results over five runs are reported, but dispersion/significance values are absent from the displayed table.

**Online experiments:** None; “online” is replayed streaming evaluation.

**Reproducibility:** Code: https://github.com/ychen216/DEFUSE.git; Criteo is public, Taobao is proprietary.

**Overall:** Strong controlled evidence for fine-grained label correction; online revenue/retention impact is unverified.

---

## 3. Industry Contribution

**Deployability:** Compatible with several sample-duplication pipelines.

**Project relevance:** Core for 7–30-day dating retention/payment labels: today’s non-retainer may be a fake negative, and late positives should be reincorporated without double-counting.

**Most important mismatch:** Assumes conversion attribution eventually resolves and does not model reciprocal actions, interference, causal uplift, or successful-exit censoring.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** Four-type importance correction plus bi-distribution use of immediate/delayed positives.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Criteo conversion logs | Yes | 60 days; 30-day/1-day variants. |
| Taobao streaming logs | No | 382M users, 5.2B samples. |
| Code | Yes | Official GitHub. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Venue:** The Web Conference  
**Year:** 2022  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D7 — delayed feedback / censored labels
