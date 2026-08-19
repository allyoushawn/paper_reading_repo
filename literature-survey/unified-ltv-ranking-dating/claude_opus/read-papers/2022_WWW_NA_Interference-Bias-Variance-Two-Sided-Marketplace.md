# Paper Analysis: Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms

**Source:** WWW 2022 (arXiv:2104.12222, submitted 2021-04-27), Stanford University. https://arxiv.org/pdf/2104.12222
**Date analyzed:** 2026-08-16

## 1. Summary

Hannah Li, Ramesh Johari, Geng Zhao, and Gabriel Y. Weintraub (Stanford University) address a specific failure of standard A/B testing in two-sided marketplaces (ridesharing, lodging, online matching): treatment and control units compete for the same shared supply or demand, which violates the Stable Unit Treatment Value Assumption (SUTVA) and biases the standard difference-in-means Global Treatment Effect (GTE) estimator. In customer-side randomization (CR), a treatment customer who books a listing mechanically reduces the supply available to control customers; symmetrically, in listing-side randomization (LR), a treatment listing that receives applications reduces effective demand for control listings. Existing bias-reducing alternatives — cluster-randomized or switchback (time-interval) designs — trade this bias for large variance increases and substantial engineering implementation cost, so platforms keep running the simpler, biased CR or LR designs in practice.

The paper's contribution is a tractable static bipartite market model — N listings, M customers, a three-step consideration → application → acceptance booking process — that yields closed-form asymptotic bias and variance for both CR and LR difference-in-means estimators as a function of relative market demand λ = M/N. Its headline results: (1) the CR estimator is asymptotically unbiased as the market becomes demand-constrained (λ→0), while LR remains biased there; the LR estimator is asymptotically unbiased as the market becomes supply-constrained (λ→∞), while CR remains biased there — so market balance alone determines which design is bias-optimal; (2) choosing the bias-optimal experiment type (CR vs. LR) costs little or nothing in variance; (3) the treatment allocation proportion a is a genuine bias-variance lever — variance is minimized near a=0.5, but bias changes monotonically in a for multiplicative interventions, so a more extreme split trades variance for lower bias; (4) despite this, a numerically demonstrated finding is that a 50-50 split is a robust, near-MSE-optimal default in most calibrated scenarios (variance approximation ratio at most 1.004 relative to the variance-optimal split for CR); and (5) sequential "ramp-up" designs are shown to be self-correcting: a small initial allocation limits bias if the true effect is harmful, and can be safely increased if the effect looks positive, which itself further reduces bias.

Methodology: a static model with heterogeneous listing types θ∈Θ and customer types γ∈Γ; consideration probability is scaled as N·p^(N)(γ,θ)→φ(γ,θ) to keep consideration-set sizes bounded as the market grows to infinity; each customer applies to exactly one listing in their consideration set uniformly at random, and each listing accepts exactly one applicant uniformly at random from those who applied. The CR and LR difference-in-means estimators are defined and their large-market limits derived via a queueing-style conversion function F(x)=(1-e^-x)/x, giving explicit application-rate and booking-rate fixed points. Validation is via calibrated large-scale numerical simulation — not real platform data — with homogeneous markets of M≈4.1 million customers and N swept from roughly 66 thousand to 268 million listings (λ from small to large), consideration probabilities calibrated to a 20% global-control / 22% global-treatment booking rate.

## 2. Experiment Critique

**Design.** This is a theoretical paper; its "experiments" are calibrated Monte Carlo / numerical simulations rather than real marketplace data, so conventional experiment-critique concepts (held-out data, real baselines) apply loosely. The simulation design is systematic: it sweeps λ across many orders of magnitude, tests both homogeneous and two-type heterogeneous markets, and separately isolates the effect of the allocation proportion from the effect of experiment type (CR vs. LR) — a clean way to disentangle the two design levers the paper claims matter.

**Statistical validity.** The core claims are proved analytically (Theorem 1: unbiasedness in market extremes; Theorems 2–3: monotonicity of bias in the allocation proportion for multiplicative interventions) under explicit stated assumptions — no listing-side "screening" of applicants, and a multiplicative-lift intervention model for the monotonicity results. Numerical simulation is used to confirm the theorems and characterize magnitudes the theorems do not pin down exactly, e.g., the 1.004 variance-approximation-ratio finding for a 50-50 split.

**Online experiments.** None. The model is static with no live platform deployment or online A/B test reported anywhere in the paper.

**Reproducibility.** Proofs are given in a lengthy appendix; simulation parameters (market sizes, λ sweep range, φ/φ̃ calibration to 20%/22% booking rates) are specified precisely enough to reproduce the reported figures, though no code release is confirmed in the extracted content.

**Overall.** Rigorous as theory, but every quantitative magnitude claim — that interference bias can range from "one-third the size to the same size as the GTE" (cited from prior empirical work), the 1.004 variance ratio, or the roughly 15–80% relative CR bias range in the authors' own calibration — comes from either cited prior empirical studies or the authors' own calibrated simulation, never from a live marketplace experiment. The authors do not claim otherwise.

## 3. Industry Contribution

**Deployability.** High by design: the paper is explicitly written as decision guidance for platforms already running simple, individually randomized CR or LR A/B tests that lack the engineering resources for cluster or switchback designs. The core prescription — pick CR vs. LR based on measured relative demand λ — requires no new randomization infrastructure, only a measurement of market balance layered on top of standard treatment-assignment logic already in place.

**Problems solved.** Gives platforms a principled, closed-form answer to two concrete design questions — "should I randomize the demand side or the supply side" and "what treatment allocation should I use" — replacing ad hoc choices with a decision rule tied to a measurable market statistic (λ).

**Engineering cost.** Minimal incremental cost over an existing CR/LR A/B testing platform: no new randomization unit, no network clustering, no switchback scheduling. The paper's own framing positions cluster and switchback designs as the "expensive" alternative it is trying to help platforms avoid.

## 4. Novelty vs. Prior Work

**Claimed novelty.** The first closed-form, asymptotic characterization of bias and variance for both CR and LR difference-in-means estimators jointly, as a function of both experiment type and treatment allocation proportion, in a tractable large-market bipartite model — prior work either demonstrated interference bias empirically or addressed only one design lever (type or allocation) at a time.

**Prior work.** Imbens and Rubin, *Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction* (Cambridge University Press, 2015) — canonical SUTVA reference. Burdett, Shi, and Wright, "Pricing and matching with frictions," *Journal of Political Economy* 109(5), 2001 — source of the bipartite matching-with-frictions model this paper adopts. Blake and Coey, "Why marketplace experimentation is harder than it seems: The role of test-control interference," *EC* 2014 — first empirical demonstration that marketplace interference bias can be as large as the treatment effect itself. Fradkin, "Search frictions and the design of online marketplaces," *AMMA* 2015 — empirical grounding for search-friction effects. Ugander, Karrer, Backstrom, and Kleinberg, "Graph cluster randomization: Network exposure to multiple universes," *KDD* 2013 — the cluster-randomization alternative this paper positions against. Sneider, Tang, and Tang, "Experiment rigor for switchback experiment analysis" (2019), and Bojinov, Simchi-Levi, and Zhao, "Design and analysis of switchback experiments" (2021) — switchback-testing design references. Johari, Li, Liskovich, and Weintraub, "Experimental design in two-sided platforms: An analysis of bias" (2021) — the authors' own precursor work, in a dynamic rather than static two-sided market setting.

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Calibrated numerical simulation | Synthetic, generated from the paper's own market model | Parameters published; code release not confirmed in extracted content | Homogeneous/heterogeneous markets, M up to ~4.1M customers, N swept 2^16–2^28 listings, booking rates calibrated to 20%/22% control/treatment |

No real marketplace transaction data is used or released.

## 6. Community Reaction

Not assessed in NotebookLM mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms," Hannah Li, Ramesh Johari, Geng Zhao, Gabriel Y. Weintraub (Stanford University), WWW, 2022 (arXiv:2104.12222), https://arxiv.org/pdf/2104.12222 |
| 2 | Source type | Academic |
| 3 | Direction | D8 |
| 4 | Problem setting | Bias and variance of standard A/B-test estimators (customer-side vs. listing-side randomization) under SUTVA-violating competition/interference in a two-sided booking marketplace |
| 5 | Objective and label definition | Not an ML paper — no training objective or label. The estimation target is the Global Treatment Effect (GTE), the expected change in fractional bookings if an intervention were launched platform-wide vs. not at all. Modeled as a static, one-shot booking process (no continuous time); no delay or censoring handling, since the model is static by construction |
| 6 | Prediction or incrementality | Incrementality — the paper's own wording: "the goal is to estimate the effect that an intervention would have on a metric of interest if it were launched to the entire platform... we call this effect the global treatment effect or GTE." This is a causal-effect estimation paper, not a predictive-model paper |
| 7 | Model architecture | Not an ML model — a stylized static bipartite market model (N listings × M customers, three-step consideration→application→acceptance process) with closed-form asymptotic bias/variance expressions for CR and LR difference-in-means estimators |
| 8 | Credit assignment | Group-level, not item- or user-level: the CR and LR estimators compare aggregate booking rates between the entire treatment group and the entire control group (customers for CR, listings for LR); there is no pointwise or slate-level decomposition of a user-level outcome to an individual impression or item |
| 9 | Training data and counterfactual handling | No training data. Randomized unit is either the customer/viewer (Customer-side Randomization, CR) or the listing/candidate (Listing-side Randomization, LR); the paper also references cluster (geographic) and switchback (time-interval) randomization as higher-variance industry alternatives. Bias direction/magnitude: under a positive (upward) multiplicative intervention, both CR and LR estimators are asymptotically positively biased (overestimate the GTE); under a negative intervention, both are negatively biased. CR bias → 0 as the market becomes demand-constrained (λ→0) while LR remains biased there; LR bias → 0 as the market becomes supply-constrained (λ→∞) while CR remains biased there. Prior cited empirical/simulation work puts marketplace interference bias at roughly one-third to the full size of the true GTE; the authors' own calibrated simulation shows CR's relative bias (Bias/GTE) ranging from near 0 up to ~80% depending on λ, while LR's relative bias stays comparatively flat around ~15% |
| 10 | Offline and online evaluation | Offline only — closed-form asymptotic limits plus calibrated numerical simulation, never real platform traffic. No online evaluation is reported anywhere in the paper |
| 11 | Reported gains | Not a "gains" paper in the model-comparison sense; its quantitative deliverable is the bias/variance characterization itself — e.g., a 50-50 allocation split achieves a variance-approximation ratio of at most 1.004 relative to the variance-optimal allocation (CR design, across all tested market-balance and effect-size parameters) |
| 12 | Applicability to a two-sided dating recommender | Directly actionable for the survey's evaluation plan: a dating app can use relative supply/demand of active candidates vs. viewers (λ) to decide whether to randomize on the viewer or candidate side for a ranking-model A/B test, and should expect CR/LR bias to trade off in the directions and rough magnitudes this paper quantifies. Its simplifying assumptions — no reciprocity requirement, no listing "screening," a static one-shot booking process — do not hold for dating apps, where a match requires mutual acceptance, so its formulas are a starting approximation rather than an exact fit |
| 13 | Unverified claims | The claim that choosing the bias-optimal design "has little effect on variance" is demonstrated only in the authors' own calibrated simulations, not on live platform traffic; the paper's own figures for how large interference bias is "in practice" are drawn from citing two prior empirical/simulation studies rather than from this paper's own real-world measurement |

**Platform recommendation (what the paper says to actually do).** (1) Choose experiment type by market balance: run CR in demand-constrained markets (λ→0), run LR in supply-constrained markets (λ→∞); if the choice of experiment type is unavailable (e.g., legal or UX constraints force a single design), this choice-of-type lever still dominates the allocation-proportion lever in reducing error. (2) Use a 50-50 treatment split as a robust, near-MSE-optimal default in most practical regimes; in large markets, where variance is small relative to bias, shift toward a more extreme allocation to reduce bias instead. (3) For risky interventions, use a sequential ramp-up design: a small initial allocation limits harm and estimation bias if the true effect is negative, and can be safely increased if the effect looks positive — the increase itself further reduces bias as the allocation grows.

## Project Relevance

This paper answers the core of the survey's **Q6** for the specific case of a single ranking-model A/B test in a two-sided market: it provides a market-balance-based rule (CR vs. LR, keyed to relative demand λ) for which side to randomize, quantifies the resulting bias direction and rough magnitude, and gives a concrete allocation-proportion recommendation (50-50 as robust default, ramp-up for risky changes). It is the strongest available answer in this batch to "what should a platform actually do" for evaluating a ranking change under two-sided interference, and is directly usable in the executive summary's evaluation-plan deliverable. It does not address **Q1–Q5 or Q8** at all — no ML model, no retention/revenue objective, no delayed label, no item-level credit assignment, no migration path. Its own stated limitation — no reciprocal "screening" by either side, a static one-shot booking process — means it does not capture the reciprocity or congestion-under-mutual-consent structure specific to dating (**Q7**): this is a one-sided-acceptance booking-marketplace model, not a two-sided-consent matching model, so a dating-app application must treat its bias formulas as approximate rather than exact.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Hannah Li, Ramesh Johari, Geng Zhao, Gabriel Y. Weintraub
- **Affiliations:** Stanford University
- **Venue:** WWW 2022 (arXiv:2104.12222, submitted 2021-04-27)
- **Year:** 2022
- **Relevance:** Core
- **Priority:** 1
- **nlm:ca9ef34f-f462-4c3e-b8c3-3bd64b0bedfc**
