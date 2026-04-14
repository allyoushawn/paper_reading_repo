# Paper Analysis: Bayesian Modeling of Marketing Attribution

**Source:** https://arxiv.org/pdf/2205.15965.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Bayesian Modeling of Marketing Attribution  
**Authors:** Ritwik Sinha, David Arbour, Aahlad Manas Puli (Adobe Research / NYU)  
**Abstract:** Proposes a likelihood-based Bayesian attribution model for multi-channel journeys that encodes direct channel effects, exponential decay of ad influence over time, synergistic interactions between channels, and customer heterogeneity via random effects. Posteriors are fit with MCMC (Stan) and yield uncertainty for ad effects and half-lives.

**Key contributions:**
- Unified likelihood model with interpretable parameters (baseline μ, random effect b_i, channel magnitudes β_a, decays λ_a, interaction γ).
- Bayesian posteriors as “usable error bounds” for attribution-relevant parameters.
- Evaluation on synthetic recovery experiments and a down-sampled Adobe Analytics travel/experience dataset.

**Methodology:** Models purchase probability at each interaction time using a link g (logit on real data; identity in one simulation) with multiplicative decay of past exposures and an interaction term; attributes channels by summing per-customer differences in predicted sale probability with vs. without a channel.

**Main results:** MCMC posteriors on simulation concentrate within ~0.02 width on β, λ (<4% error). Real-data posteriors show fast decay for some channels; largest attributed orders to Travel Agents, Other Owned sites, then Search Ads (per paper figures).

---

## 2. Experiment Critique

**Design:** Synthetic 10k journeys / 5 channels plus real stratified sample (5k customers, ≤5 touches, 70:30 balance). Abstract mentions “alternatives in simulations” but named baselines and head-to-head metrics are not specified in the excerpted text.

**Statistical validity:** Strong parameter recovery narrative on synthetic data; real-data application is illustrative. Identifiability: when β≈0, λ posteriors can become flat (expected given multiplicative structure).

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Stan-based; proprietary-scale raw logs not public; simulation recipe described.

**Overall:** Solid interpretable Bayesian path model for touch timing and interactions; channel-level attribution sums are explicit; per-touch fractional export as training labels is not spelled out as a productized pipeline.

---

## 3. Industry Contribution

**Deployability:** Moderate—MCMC at journey scale needs engineering; Adobe Analytics context suggests product adjacency.

**Problems solved:** Replaces purely rule-based credit with decay + interaction + heterogeneity in one likelihood.

**Engineering cost:** Stan tuning, scaling to billions of events, and cross-device stitching (noted as future work).

---

## 4. Novelty vs. Prior Work

Positions against rule-based MTA, Markov MTA cardinality limits, and large-scale DNN MTA that omits decay/heterogeneity estimates; cites Yadagiri et al. WISE 2015 for credit-assignment stage; references Shao & Li KDD 2011, Dalessandro et al. 2012, Shapley-based lines, Ren et al. DARNN.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic journeys | Described in paper | Partial | 10k paths, known parameters |
| Adobe Analytics travel sample | Proprietary | No | Down-sampled 5k customers |

---

## 6. Community Reaction

Not specified in source.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Ritwik Sinha, David Arbour, Aahlad Manas Puli  
**Affiliations:** Adobe Research; NYU  
**Venue:** arXiv (stat.AP)  
**Year:** 2022  
**PDF:** https://arxiv.org/pdf/2205.15965.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(a) Per-touchpoint fractional credit for supervised labels:** The paper defines channel attribution as summed differences in conversion probability with vs. without a channel across customers; per-event fractional labels for arbitrary downstream models are not specified in source.

**(b) Continuous outcomes (e.g., days-active):** Link function can be non-logit; simulation uses identity link for continuous y, so extension is structurally supported though dating/retention is not discussed.

**(c) Selection / heterogeneity:** Customer heterogeneity via random effects b_i; explicit selection-bias discussion for active users not specified in source.

**(d) Incrementality vs correlation:** Attribution constructed from counterfactual removal of channel influence in the fitted probability model (incremental flavor at model level), not RCT-grounded incrementality.
