# Paper Analysis: Amazon Ads Multi-Touch Attribution

**Source:** https://arxiv.org/pdf/2508.08209.pdf
**Date analyzed:** 2026-04-12

---

## 1. Summary
**Title:** Amazon Ads Multi-Touch Attribution
**Authors:** Randall Lewis, Florian Zettelmeyer, Brett R. Gordon, Cristobal Garib, Johannes Hermle, Mike Perry, Henrique Romero, German Schnaidt
**Abstract:** Amazon's new MTA solution allows advertisers to measure how each touchpoint across the marketing funnel contributes to a conversion. It combines randomized controlled trials (RCTs) and machine learning (ML) models to allocate credit for Amazon conversions across Amazon Ads touchpoints in proportion to their likely contribution to shopping decisions. ML models trained purely on observational data can yield precise predictions but may produce biased estimates of ad effects. RCTs yield unbiased ad effects but can be noisy. The MTA methodology combines experiments, ML models, and Amazon's shopping signals to inform attribution credit allocation.

**Key contributions:**
- Bridges the gap between unbiased RCTs (noisy, campaign-level) and precise ML models (biased, touchpoint-level) via Causal Calibration Models
- Introduces a three-system architecture: Ground Truth System (RCT database + calibration), Attribution System (ensemble of rule-based + deep learning models), and Decision System (optimization)
- Mechanically disaggregates campaign-level calibrated predictions down to individual touchpoint MTA credits
- Maintains a database of hundreds of thousands of RCTs across Amazon's ad products

**Methodology:** The framework trains a Causal Calibration Model that regresses RCT campaign treatment effects against outputs of an ensemble of attribution models (Last-Touch Attribution + Model-Driven Attribution via deep learning). Calibration weights (e.g., β=0.6 for LTA, α=0.4 for MDA) are learned to predict RCT ground truth. These weights are then disaggregated from campaign-level back to touchpoint-level to produce "MTA credits" — fractional, causally-backed attribution scores per interaction.

**Main results:** The paper is primarily a methodological overview rather than a benchmark paper. Key quantitative motivations: a 2023 Meta study showed purely observational ML models produce 488%–948% errors in ad effect estimates. The Causal Calibration Model corrects for this by anchoring ML predictions to RCT ground truth. Illustrative example shows ensemble weights (0.6 LTA + 0.4 MDA) producing MTA shares that differ from both LTA and MDA alone.

---

## 2. Experiment Critique
The paper presents a system description rather than a controlled empirical study. No traditional benchmark table with percentage improvements over baselines is provided. The core validation relies on hundreds of thousands of proprietary Amazon RCTs, making the approach non-reproducible externally. The cited Meta study (Gordon et al. 2023) demonstrating 488%–948% errors in observational models provides strong motivation for the hybrid approach. The Causal Calibration Model's out-of-sample prediction accuracy on held-out RCTs is mentioned as a validation step but specific metrics are not reported. Statistical validity is strong in principle (RCT ground truth), but external reproducibility is limited by proprietary data and infrastructure.

---

## 3. Industry Contribution
Highly deployable — this is a production system at Amazon scale. It represents a practical engineering solution to the long-standing industry problem of reconciling causal measurement (RCTs) with scalable prediction (ML). The key insight — using RCTs to calibrate rather than replace ML models — is immediately applicable to any organization that runs experiments. Engineering cost is high (requires maintaining a massive RCT database and multi-model ensemble), but the framework is conceptually transferable to smaller scales.

---

## 4. Novelty vs. Prior Work
The paper builds directly on:
1. **Gordon, Moakler, Zettelmeyer (2023)** — "Close Enough?" proving observational ML fails at ad measurement (488%–948% error)
2. **Gordon, Moakler, Zettelmeyer (2025)** — Predicted Incrementality by Experimentation (PIE), the foundational framework extended by Amazon MTA
3. **IAB (2024)** — IAB/MRC Retail Media Measurement Guidelines recommending RCTs for incrementality

The reference list is unusually short (3 works), suggesting this is an industry white paper rather than an academic contribution.

---

## 5. Dataset Availability
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Amazon RCT Database | N/A | No | Proprietary; hundreds of thousands of RCTs |
| Event History Logs | N/A | No | Proprietary; bid requests, traffic, retail, ASIN catalogs |

---

## 6. Community Reaction
No significant community discussion found.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information
**Authors:** Randall Lewis, Florian Zettelmeyer, Brett R. Gordon, Cristobal Garib, Johannes Hermle, Mike Perry, Henrique Romero, German Schnaidt
**Affiliations:** Amazon, Northwestern University, NBER
**Venue:** arXiv
**Year:** 2025
**PDF:** https://arxiv.org/pdf/2508.08209.pdf
**Relevance:** Core
**Priority:** 1

---

## Project Relevance
**(A) Does it produce per-touchpoint or per-interaction credit suitable as continuous training labels, or mainly aggregate lift?**
- The framework explicitly produces per-touchpoint fractional credit. It uses a Causal Calibration Model to disaggregate campaign-level predictions down to the touchpoint level, generating specific "MTA credits" that represent the predicted incremental effect of each individual touchpoint on the outcome.

**(B) Applicability to non-purchase, continuous engagement / retention outcomes?**
- Not specified in source. The paper exclusively discusses modeling discrete "conversions," "sales," and "purchases."

**(C) Handling selection bias when high-activity users get more touchpoints?**
- The specific mechanism of high-activity users organically receiving more touchpoints is not specified in source. However, the framework handles overarching selection and observational bias by running massive-scale RCTs to establish unbiased causal ground truth. Randomization balances all underlying consumer characteristics (like latent intent) across groups. The system then uses these RCTs to train a Causal Calibration Model, which mathematically corrects the biases in observational ML models by forcing them to predict the unbiased RCT outcomes.
