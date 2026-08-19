# Paper Analysis: Experimental Design in Two-Sided Platforms: An Analysis of Bias

**Source:** NotebookLM source `c2aa9d85-74ed-4a98-8c41-55a7c5642d1b` (Management Science 2022)
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Experimental Design in Two-Sided Platforms: An Analysis of Bias
**Authors:** Ramesh Johari, Hannah Li, Inessa Liskovich, Gabriel Y. Weintraub
**Abstract:**
A/B tests on two-sided marketplaces (e.g., a booking/rental platform) violate SUTVA because a treated customer competes with control customers for the same shared, dynamically-replenishing inventory (listings). The paper builds a continuous-time Markov chain model of listing availability with a mean-field (fluid) limit, proves that the bias of customer-side randomization (CR) and listing-side randomization (LR) estimators depends on market balance (demand-to-supply ratio λ/τ), and introduces two-sided randomization (TSR) plus debiased "TSRI" estimators that interpolate between CR and LR and explicitly correct for competition/cannibalization.

**Key contributions:**
- A dynamic-inventory Markov chain / mean-field-limit model of a two-sided platform with formal convergence and steady-state uniqueness proofs.
- Proof that naive CR is unbiased in demand-constrained markets but biased in supply-constrained ones, and vice versa for naive LR — good design depends on market balance.
- Two-sided randomization (TSR): randomize both customers and listings; apply treatment only when a treated customer meets a treated listing.
- TSRI-1 / TSRI-2 estimators that explicitly measure and correct for competition ("cannibalization") between treatment and control, reducing bias substantially over naive CR/LR/TSR at the cost of higher variance.

**Methodology:**
Customers arrive via Poisson process, form a consideration set of available listings, and choose via a multinomial logit discrete-choice model; booked listings become unavailable for an exponentially-distributed occupancy period. The finite-N system provably converges (rate O(1/N)) to a deterministic mean-field fluid limit, whose unique steady state is characterized via a convex optimization problem. TSRI estimators interpolate CR and LR weighted by β = e^(−λ/τ) and subtract a measured cannibalization correction term.

**Main results:**
At balanced market (λ/τ=1): naive CR and LR both ≈22% biased relative to GTE, naive TSR ≈26% biased; TSRI-2 reduces this to ≈7.5–8% bias (at the cost of ~2.5x the standard error of naive LR). At demand-constrained (λ/τ=0.1): naive LR is ~33% biased, CR only ~2%; TSRI-2 <1%. At supply-constrained (λ/τ=10): naive CR is >300% biased, naive LR ~1.7%, TSRI-2 ~2%. Against cluster-randomization (an alternative bias-reduction approach), TSRI-2 stays under 10% bias across all levels of market interconnectedness, while cluster-randomization bias rises to ~30% as the market becomes more interconnected.

---

## 2. Experiment Critique

**Design:**
Rigorous theory-plus-simulation design: formal bias proofs at the two market-balance extremes, then simulation across the full λ/τ range and across four robustness scenarios (customer heterogeneity, listing heterogeneity, heterogeneous treatment effects, varying baseline utility), plus a head-to-head against cluster-randomization under varying "preference ratio" (market interconnectedness).

**Statistical validity:**
Simulations report bootstrapped 95th-percentile confidence intervals; the bias-variance tradeoff across estimators is explicitly quantified (e.g., TSRI-2's ~0.20-of-GTE standard error vs. ~0.08 for naive LR/TSR at balanced market). The paper is candid that its mean-field model shows some discrepancy from finite-system simulation at balance extremes (small λ → high SE from few arrivals; large λ → mean-field approximation degrades as available-listing counts shrink).

**Online experiments (if any):**
Not run as a live platform experiment in this paper — validated via simulation of the fitted Markov-chain/choice model, calibrated to realistic booking probabilities (20% control / 23% treatment).

**Reproducibility:**
Full model, proofs, and estimator formulas are specified; simulation parameters are given explicitly (N=5,000 listings, T=25 periods, 500 runs). No dataset or code release is mentioned — this is a methodology paper, not an applied-data paper.

**Overall:**
Results support the central claim that market balance determines which naive design is safer, and that TSR-based debiased estimators meaningfully reduce bias across the whole balance spectrum at a variance cost. Authors explicitly flag standard-error estimation under interference as an open problem (their own "naive" SEs assume independence, which is technically violated).

---

## 3. Industry Contribution

**Deployability:**
High for platforms already running two-sided A/B infrastructure (e.g., can compute per-cell λ/τ from existing telemetry) — the paper explicitly frames its results as guidance for choosing CR vs. LR vs. TSR based on measured market balance, and TSRI estimators are a purely statistical post-hoc correction requiring no product change.

**Problems solved:**
Directly addresses interference-biased A/B testing in a shared-inventory two-sided marketplace — squarely Layer 4 (ecosystem metrics and experimentation under interference) of this project.

**Engineering cost:**
Moderate: requires instrumenting both customer-side and listing-side treatment assignment (TSR), logging enough state to measure cannibalization for the TSRI correction, and estimating λ/τ per market segment to calibrate the correction weight β.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First to formally characterize how naive CR/LR bias depends on market balance via a dynamic (not static) inventory model with a rigorous mean-field limit, and to propose interference-corrected TSRI estimators that interpolate between CR and LR.

**Prior work comparison:** Closely related to, and cites as independently concurrent, Bajari et al. (2019/2023) "Multiple randomization designs for interference" (a static-model, more general treatment of two-sided randomization) — this is the same underlying idea as source `ecffd79a` (Multiple Randomization Designs) in this batch, developed independently and in a dynamic rather than static setting. Also builds on Holtz et al. (2020) (cluster-randomization on Airbnb — source `6a17afaa` in this batch), Blake & Coey (2014), Fradkin (2015/2019), and Wager & Xu (2019) "Experimenting in equilibrium."

**Verification:** Novelty claims are consistent with the cited literature; the paper is explicit about its overlap with and distinction from Bajari et al. (2019) (dynamic vs. static model) and from Holtz et al. (2020)/cluster-randomization approaches (which this paper directly benchmarks against in Section 8).

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| None — simulated marketplace (N=5,000 listings, T=25 periods, 500 runs) | N/A | N/A | Methodology paper; no real platform dataset used |

**Offline experiment reproducibility:** The simulation setup (parameters, choice model, Markov chain) is fully specified and could be reimplemented, though no code is released.

---

## 6. Community Reaction

Not checked — out of scope for this NotebookLM-sourced batch pass (no web search performed).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Ramesh Johari, Hannah Li, Inessa Liskovich, Gabriel Y. Weintraub
**Affiliations:** Stanford University (Johari, Weintraub); industry affiliations for Li/Liskovich not confirmed in extracted content
**Venue:** Management Science, 2022
**Year:** 2022
**PDF:** Not fetched directly — analyzed via NotebookLM source extraction
**Relevance:** Related
**Priority:** 2

---

## Bibliography Fields

- **title:** Experimental Design in Two-Sided Platforms: An Analysis of Bias
- **authors or organization:** Ramesh Johari, Hannah Li, Inessa Liskovich, Gabriel Y. Weintraub
- **year:** 2022
- **venue or type:** Management Science (academic journal)
- **link:** N/A (accessed via NotebookLM notebook source; not separately fetched)
- **tier tag:** Tier 2 — Applied research / field experiments on real matching or dating platforms

**What they did (80 words max):** Built a dynamic Markov-chain/mean-field model of a two-sided marketplace with shared, replenishing inventory; proved that naive customer-side (CR) and listing-side (LR) A/B test estimators are biased in opposite market-balance regimes; introduced two-sided randomization (TSR) and debiased TSRI estimators that interpolate CR/LR and correct for competition ("cannibalization"), cutting bias substantially (to single-digit % of GTE) versus naive designs, at a variance cost, validated via extensive simulation.

**Mechanism relevant to two-sided balancing (50 words max):** Provides an interference-aware A/B testing methodology for a marketplace where treated units compete for shared, capacity-limited "inventory" — directly analogous to two people competing for a desirable match's finite reply capacity. Its market-balance-dependent bias framework and TSRI correction are the closest thing in this batch to an off-the-shelf experimentation methodology for the project's Layer 4.

**Metrics used, and the reported effect:** Bias as % of GTE across CR/LR/TSR/TSRI-1/TSRI-2 estimators, at three market-balance regimes: demand-constrained (λ/τ=0.1: naive LR ~33% biased vs. TSRI-2 <1%), balanced (λ/τ=1: naive CR/LR ~22%, naive TSR ~26%, TSRI-2 ~7.5–8%), supply-constrained (λ/τ=10: naive CR >300%, naive LR ~1.7%, TSRI-2 ~2%); standard error reported alongside bias to show the bias-variance tradeoff.

**Fit for a dating app:** medium — the marketplace-interference and market-balance-dependent bias framework transfers conceptually, but the paper's "inventory" (a listing becomes unavailable once booked, then replenishes) is a supply-depletion model, not a reply-capacity/reciprocity model; a dating platform's interference is about a person's finite attention/reply budget being shared across many simultaneous suitors, not sequential exclusive booking, so the TSRI correction machinery would need real adaptation, not direct reuse.

**Confidence that the item is real and described correctly:** high — both Query 1 and Query 2 were grounded (`sources_used` matched `c2aa9d85...`), with detailed formulas, named estimators (TSRI-1/TSRI-2), specific figures, and a real bibliography (Bajari et al. 2019, Holtz et al. 2020, Wager & Xu 2019) consistent with the known Johari/Li/Liskovich/Weintraub Management Science 2022 paper. Query 3 (the dedicated project-relevance probe) could not be run — see Project Relevance note below.

---

## Project Relevance

*Note: the dedicated Query 3 project-relevance probe could not be completed — the NotebookLM API returned `RESOURCE_EXHAUSTED` errors on every attempt (5+ retries, including after `refresh_auth`), likely due to concurrent load from other batches sharing this notebook/account. The analysis below synthesizes project relevance from the grounded Query 1/Query 2 content above, not from a fresh NLM answer.*

Medium-to-high relevance as a *methodology template* for the project's Layer 4 (experimentation under interference), with an important structural mismatch to adapt for. What transfers well: (1) the core insight that **naive single-sided randomization is biased in a direction that depends on market balance** — for a dating app, this maps directly to expecting different bias behavior for A/B tests of exposure-allocation changes depending on whether a given demographic/segment is "receiver-constrained" (few desirable profiles relative to demand, analogous to supply-constrained) or "sender-constrained" (analogous to demand-constrained); (2) the **TSR design pattern** (randomize both sides, treat only matched-treatment pairs) is directly reusable for testing a capacity-aware exposure-allocation policy in a dating market, since it isolates the policy's effect from cross-side interference; (3) the explicit **bias-variance tradeoff quantification** is a useful template for how this project should report experimentation results under interference, rather than a single point estimate.

What does not transfer directly: the paper's notion of "interference" is booking-driven inventory depletion (a listing is exclusively occupied once booked, then eventually frees up) — there is no concept of a person's simultaneous, non-exclusive reply-capacity being drawn down by many concurrent likes, nor any fairness/spread metric (the paper's only outcome is the global treatment effect on booking probability). A dating-market adaptation of TSRI would need a reply-capacity-depletion model in place of the inventory-Markov-chain, and would need to extend the estimand beyond global treatment effect to cover match-spread/Gini and two-sided retention, which this paper does not address.
