# Paper Analysis: Capturing Delayed Feedback via Elapsed-Time Sampling

**Source:** https://ojs.aaai.org/index.php/AAAI/article/view/16587  
**Source ID:** adf6d4a9-2fef-4bed-a95e-da11d5b00a5e  
**Date analyzed:** 2026-08-18  
**Model identifier:** codex-sol  
**Evidence mode:** NotebookLM indexed-content fallback after source-scoped query plateau.

---

## 1. Summary

**Abstract:** ES-DFM samples an elapsed waiting time, models the observed-versus-true conversion distribution, duplicates later positives, and importance-weights loss to balance fresh training data against label accuracy.

**Main results:** Criteo AUC/PR-AUC/NLL was 0.8402/0.6393/0.3924 versus vanilla 0.8376/0.6288/0.4047. Taobao was 0.8895/0.6762/0.1112 versus vanilla 0.8842/0.6645/0.1141; improvements over best baselines were significant at p≤0.05.

---

## 2. Experiment Critique

**Design:** Realistic train-on-hour t/test-on-hour t+1 protocol, oracle ceiling, multiple delayed baselines, elapsed-time sensitivity, and corruption robustness.

**Statistical validity:** t-test significance is reported; run counts/dispersion are not visible in extracted content.

**Online experiments:** The source mentions an online evaluation section, but complete production-effect numbers were not present in extracted evidence; treated here as offline streaming evidence.

**Reproducibility:** Criteo is public and supplementary details are at the cited GitHub path; Taobao is private.

**Overall:** Good evidence for optimizing the freshness/accuracy tradeoff.

---

## 3. Industry Contribution

**Deployability:** A waiting/sampling policy plus importance-weighted CVR head fits streaming pipelines.

**Project relevance:** Core for choosing when 7–30-day retention or payment labels enter training; personalized elapsed time could depend on member lifecycle or product type.

**Most important mismatch:** Delay is treated as ordinary eventual conversion, not reciprocal, censored by success, causal, or marketplace-interfering.

---

## 4. Novelty vs. Prior Work

**Claimed novelty:** Explicitly makes observation delay an active sampled policy and derives corresponding unbiased importance weights.

**Verification:** Source-grounded only.

---

## 5. Dataset Availability

| Dataset | Accessible | Notes |
|---------|------------|-------|
| Criteo conversion logs | Yes | Public. |
| Taobao | No | Private industrial data. |
| Supplement | Yes | GitHub path stated in source. |

---

## 6. Community Reaction

No significant discussion assessed.

---

## Papers That Mention This Paper (Reverse Citation Map)

No explicit in-corpus mention found.

---

## Meta Information

**Affiliations:** Alibaba / academic collaborators  
**Venue:** AAAI  
**Year:** 2021  
**Relevance:** Core  
**Priority:** 1  
**Direction:** D7 — delayed feedback / censored labels
