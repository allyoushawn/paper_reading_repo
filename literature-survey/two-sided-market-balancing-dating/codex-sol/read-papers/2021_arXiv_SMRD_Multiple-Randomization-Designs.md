# Paper Analysis: Multiple Randomization Designs: Estimation and Inference with Interference

**Source:** https://arxiv.org/abs/2112.13495  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Multiple Randomization Designs: Estimation and Inference with Interference  
**Authors:** Lorenzo Masoero, Suhas Vijaykumar, Thomas S. Richardson, James McQueen, Ido Rosen, Brian Burdick, Pat Bajari, Guido Imbens  
**Abstract:** Single-sided experiments can miss strategic spillovers in markets with interacting populations. The paper formalizes simple multiple randomization designs at the buyer-seller tuple level, derives finite-sample estimators and conservative inference, and shows how the design separates direct, buyer-side, and seller-side effects.

**Key contributions:**

- Formalizes design-based estimation for independently randomized market sides under local interference.
- Derives finite-sample variances, conservative covariance bounds, and a finite-population central limit theorem.
- Demonstrates that single-sided designs can estimate the wrong sign while multiple randomization detects spillovers.

**Methodology:** Buyers and sellers are independently assigned treatment eligibility. Pairwise interactions fall into four cells: control-control, buyer-eligible only, seller-eligible only, and jointly treated. Contrasts among cell means estimate aggregate treatment, side-specific spillovers, and direct treatment effects under a local-interference approximation.

**Main results:** In a 200-by-150 strategic-market simulation over 10,000 rerandomizations, the single-sided estimator reports a negative profit effect despite a positive true effect. A conservative studentized test detects buyer spillovers in 99.5% of runs. Null simulations produce approximately uniform p-values.

## 2. Experiment Critique

**Design:** The four-cell design directly identifies separate side-specific spillovers under its stated local-interference restriction. Strategic and Gaussian simulations test estimation and inference, but no live marketplace experiment is reported.

**Statistical validity:** The paper provides exact design-based variance formulas, an upper-bound variance estimator, and a finite-population central limit theorem. Covariances between assignment-type estimators cannot be unbiasedly identified, making joint inference deliberately conservative.

**Online experiments:** None specified in source. Simulations use 10,000 rerandomization or Monte Carlo trials.

**Reproducibility:** Python code is provided at https://github.com/lorenzomasoero/MultipleRandomizationDesigns.

**Overall:** The theory supports valid conservative inference under local interference. Precision loss, untestable interference structure, sparsity, and heavy-tailed outcomes are important limitations.

## 3. Industry Contribution

**Deployability:** Feasible when treatment can be activated at a pairwise interaction and both market sides have stable identifiers.

**Problems solved:** Separating direct effects from buyer- and seller-mediated spillovers that single-sided A/B tests confound.

**Engineering cost:** Moderate: two eligibility assignments, four-cell interaction logging, and custom variance calculations.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A finite-sample, design-based estimation and inference framework for multiple randomization in marketplaces.

**Prior work comparison:** Neyman (1923) and Fisher establish randomized design; Bajari et al. conceptualize marketplace multiple randomization; Johari et al. (2022) analyze two-sided-platform bias; Hudgens and Halloran (2008) study interference; Li and Ding (2017) and Shi and Ding (2022) provide finite-population central-limit and Berry–Esseen foundations.

**Verification:** Comparison is based only on the source-scoped related work.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Strategic two-sided market simulation | GitHub repository above | Yes, code | 200 advertisers, 150 creators, 10,000 rerandomizations. |
| Additive Gaussian simulation | GitHub repository above | Yes, code | 200 by 150 units, 10,000 runs. |

**Offline experiment reproducibility:** Simulation code is public; there is no real-platform dataset in the source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Independently randomize each dating side and compare four pair-level eligibility cells. Control interactions with treated neighbors expose sender- and receiver-mediated spillovers even though the pair itself is untreated.

**Metrics and reported effect:** The strategic simulation uses platform profit. The single-sided baseline estimates the wrong sign, while SMRD recovers a positive effect; the conservative spillover test rejects a false null 99.5% of the time.

**Capacity/congestion relevance:** Interference from strategic effort is modeled. Reply capacity, inbox congestion, oversubscription, and feedback loops are not specified in source.

**Practical mapping:** The design is useful for like- or ranking-treatment effects that can be gated by pair eligibility. Its local-interference assumption and pairwise activation must be validated for feed-wide ranking changes.

**Dating fit: Medium.** The two-population experiment design maps well, but neither reciprocal match formation nor attention capacity is modeled.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Lorenzo Masoero, Suhas Vijaykumar, Thomas S. Richardson, James McQueen, Ido Rosen, Brian Burdick, Pat Bajari, Guido Imbens  
**Affiliations:** Amazon; Stanford University; University of Washington  
**Venue:** arXiv preprint  
**Year:** 2021 (indexed source is a later revision)  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Multiple Randomization Designs: Estimation and Inference with Interference
- **Authors/organization:** Lorenzo Masoero, Suhas Vijaykumar, Thomas S. Richardson, James McQueen, Ido Rosen, Brian Burdick, Pat Bajari, Guido Imbens
- **Year:** 2021 (later revision indexed)
- **Venue/type:** arXiv preprint; design-based causal-inference theory and simulation
- **Link:** https://arxiv.org/abs/2112.13495
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Independently randomized two marketplace populations, partitioned pairwise interactions into four eligibility cells, and derived estimators for aggregate, direct, buyer-spillover, and seller-spillover effects. The paper supplies exact finite-sample variance expressions, conservative covariance bounds, and a finite-population central limit theorem, then validates them in strategic-market and Gaussian simulations.
- **Mechanism relevant to two-sided balancing (≤50 words):** Use untreated pair cells with one treated neighbor side to isolate sender- and receiver-mediated spillovers. This reveals effects that ordinary one-sided experiments absorb into bias.
- **Metrics and reported effect:** A single-sided profit estimator gives the wrong sign in simulation; SMRD recovers the positive effect. A conservative test detects a buyer spillover in 99.5% of 10,000 rerandomizations.
- **Dating-app fit:** Medium — experimental cells transfer, but reciprocal matches, congestion, and reply capacity are absent.
- **Confidence:** High on the source-scoped design and simulations; direct marketplace validity remains untested.
