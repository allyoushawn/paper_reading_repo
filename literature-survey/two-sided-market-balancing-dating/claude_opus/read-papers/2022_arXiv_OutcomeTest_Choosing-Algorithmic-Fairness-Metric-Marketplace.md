# Paper Analysis: Choosing an Algorithmic Fairness Metric for an Online Marketplace

**Source:** YinYin Yu (LinkedIn), Guillaume Saint-Jacques (Apple), "Choosing an algorithmic fairness metric for an online marketplace: Detecting and quantifying algorithmic bias on LinkedIn," practitioner arXiv paper. NotebookLM source_id `3c046693-7a3e-41c4-a3bc-b45bcfd66487`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Choosing an algorithmic fairness metric for an online marketplace: Detecting and quantifying algorithmic bias on LinkedIn
**Authors:** YinYin Yu (LinkedIn), Guillaume Saint-Jacques (Apple)
**Abstract:**
Derives a group-level algorithmic fairness metric — the "Outcome Test," adapted from Becker's economic theory of taste-based discrimination — that isolates algorithmic bias from human bias and from pre-existing group qualification differences (the "infra-marginality" confound) in two-sided recommendation platforms. Applies it to audit two LinkedIn systems (InstaJob notifications, PYMK connection recommendations) by gender.

**Key contributions:**
- Formalizes "equal opportunity for equally qualified candidates" as the fairness notion, tested via marginal-outcome regressions (comparing realized outcomes of similarly-scored candidates across groups) rather than raw group-average comparisons.
- Proves mathematically, via counterexamples, that two common fairness metrics — Equalized Odds and Precision Parity — both produce false positives and false negatives when groups have different underlying qualification distributions.
- Provides a 2×2 framework distinguishing algorithmic-bias mitigations (score recalibration) from human-bias mitigations (UI/behavioral nudges), and a counterfactual notification-reallocation exercise on real LinkedIn data.

**Methodology:**
Decile-binned marginal-outcome regressions on pointwise classification (InstaJob) and ranking (PYMK) algorithms; counterfactual reallocation of notifications under bias-corrected scores.

**Main results:**
Bias-corrected InstaJob notification allocation increased total realized outcome by ~1% while holding notification volume constant; the paper does not report a corresponding number for PYMK. Absolute values are redacted for privacy throughout.

---

## 2. Experiment Critique

**Design:** Rigorous for a practitioner paper — includes formal proofs (via constructed counterexamples) that alternative fairness metrics fail, plus an empirical audit and counterfactual simulation on real production data.

**Statistical validity:** Decile-binned linear regressions with a score control term; coefficients tested for significance, though exact values are redacted. The marginal-decile approach is explicitly justified as a bias/power trade-off (finer bins have less statistical power).

**Online experiments (if any):** None — this is an offline/observational audit plus counterfactual simulation, not an A/B test.

**Reproducibility:** Not reproducible — proprietary LinkedIn data and redacted numeric results (all y-axis values, percent changes) throughout.

**Overall:** Methodologically the strongest single item read in this batch — clean counterexample-based critique of standard fairness metrics — but its empirical claims cannot be independently verified due to redaction, and it explicitly scopes out anything beyond static point-in-time bias measurement.

---

## 3. Industry Contribution

**Deployability:** Already deployed — the paper states LinkedIn "has operationalized bias detection and its mitigation in all its AI systems."

**Problems solved:** Gender-bias detection/quantification in classification (InstaJob) and ranking (PYMK) recommenders on a real two-sided platform.

**Engineering cost:** Moderate — requires computing per-decile marginal-outcome regressions and maintaining bias-corrected counterfactual scoring pipelines; explicitly does not require retraining or redesigning the underlying model objective.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Deriving a fairness metric from a stated fairness notion (equal opportunity for equally qualified candidates) first, rather than picking among pre-existing metrics without justification — and applying Becker's Outcome Test to ML for the first time in this framing per the authors.

**Prior work comparison:** Builds on Becker (1957) economics of discrimination; Corbett-Davies & Goel (2018) fairness-metric critique; Kleinberg et al. (2016, 2018a, 2018b) on inherent fairness-metric trade-offs and human-decision/ML-prediction interplay.

**Verification:** Plausible and well-grounded in cited economics literature; not independently checked against other algorithmic-fairness surveys here.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| LinkedIn InstaJob production logs | N/A | No — proprietary | Job notification / application / recruiter-attention outcomes |
| LinkedIn PYMK production logs | N/A | No — proprietary | Connection recommendation / acceptance / downstream interaction outcomes |

**Offline experiment reproducibility:** Not reproducible — no data release; all quantitative results redacted for privacy.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** YinYin Yu, Guillaume Saint-Jacques
**Affiliations:** LinkedIn (Yu); Apple (Saint-Jacques, at time of writing)
**Venue:** arXiv preprint (practitioner paper)
**Year:** 2022 (per project context; exact arXiv date not independently re-confirmed against source text)
**PDF:** Not fetched directly — analyzed via NotebookLM source; link not captured in available source metadata
**Relevance:** Related
**Priority:** 1 (per queue tier)

---

## Bibliography Fields

- **title:** Choosing an algorithmic fairness metric for an online marketplace: Detecting and quantifying algorithmic bias on LinkedIn
- **authors or organization:** YinYin Yu (LinkedIn), Guillaume Saint-Jacques (Apple)
- **year:** 2022
- **venue or type:** Practitioner arXiv paper
- **link:** Not captured in NotebookLM source metadata
- **tier tag:** Tier 1 — Adjacent marketplaces (job/ride/home/creator)
- **what they did (≤80 words):** Derives the "Outcome Test," a group-fairness metric based on equal opportunity for equally qualified candidates, that separates algorithmic bias from human bias and from confounding group-level qualification differences. Proves via counterexamples that Equalized Odds and Precision Parity both mislabel fair algorithms as biased (and vice versa) when group qualification distributions differ. Audits two LinkedIn systems (InstaJob, PYMK) by gender and runs a bias-corrected counterfactual notification reallocation.
- **mechanism relevant to two-sided balancing (≤50 words):** None directly — no reciprocal scoring, capacity modeling, or exposure redistribution. Offers a transferable *measurement* lens (decile-binned marginal-outcome fairness testing) and a practical algorithmic-vs-human-bias mitigation framework (score recalibration vs. UI nudges).
- **metrics used, and the reported effect:** Marginal-outcome regression coefficients (significance reported, magnitudes redacted); bias-corrected counterfactual raised total realized InstaJob outcome by ~1% at constant notification volume.
- **fit for a dating app:** medium — the fairness-measurement methodology is a solid, transferable auditing technique for any two-sided platform, but the paper explicitly has no capacity-aware or exposure-redistribution mechanism, so it addresses fairness measurement, not the wasted-likes/capacity problem itself.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answers with direct source quotes and full bibliography across all three queries; source_id validated in every call).

---

## Project Relevance

**Medium project relevance.** NotebookLM's Query 3 explicitly confirms this paper's fairness framework does not model reciprocal/mutual-interest scoring dynamics, capacity or reply-capacity constraints, exposure redistribution away from over-subscribed users, or ecosystem-health metrics like match spread or two-sided retention — it evaluates static, pointwise recommendation fairness at a single point in time and abstracts away feedback loops entirely. Its transferable value to this project is narrower but real: (1) the marginal-outcome / Outcome Test methodology is a rigorous template for auditing whether a capacity-aware reciprocal scorer is fair across genders or other groups once built, and (2) its algorithmic-bias-vs-human-bias 2×2 framework usefully maps onto a dating-market question the project will eventually face — whether observed imbalance (e.g., women receiving fewer good matches) stems from the ranking algorithm itself or from senders' own biased swiping behavior, which would call for different interventions (score recalibration vs. UI/product nudges like signaling messages).
