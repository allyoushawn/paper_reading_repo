# Paper Analysis: Reducing Marketplace Interference Bias Via Shadow Prices

**Source:** https://arxiv.org/abs/2205.02274  
**Date analyzed:** 2026-08-19

---

## 1. Summary

**Title:** Reducing Marketplace Interference Bias Via Shadow Prices  
**Authors:** Ido Bright, Arthur Delarue, Ilan Lobel  
**Abstract:** Standard randomized experiments in matching marketplaces are biased because treated demand competes with control demand for shared capacity. The paper derives two optimization-aware estimators and shows that an estimator based on linear-program shadow prices can reduce both bias and variance when the platform centrally matches supply and demand.

**Key contributions:**

- Proves that the standard randomized-controlled-trial estimator overstates a sign-consistent global treatment effect in amplitude.
- Introduces Two-LP and Shadow Price estimators for generalized matching and network-flow marketplaces.
- Extends shadow-price correction to secondary metrics through complementary slackness.

**Methodology:** Demand and supply arrive as typed Poisson processes. A bipartite matching or network-flow linear program allocates them subject to demand, supply, flow, and edge-capacity constraints. Two-LP re-solves counterfactual global-control and global-treatment programs; the Shadow Price estimator weights experimental demand differences by optimal dual values from the observed matching program. SP+ combines the standard and shadow-price estimators for some asymmetric designs.

**Main results:** On a New York City taxi simulation, standard randomization misses a true efficiency gain up to 20% smaller than the demand increase, while Shadow Price and Two-LP remove nearly all simulated bias. Under supply-chain undersupply, standard randomization overstates effect magnitude by more than twofold; Shadow Price substantially reduces bias.

## 2. Experiment Critique

**Design:** Theorems cover fluid-limit matching systems and simulations cover spatial ride-hailing contention and network bottlenecks. True global effects are available by construction, enabling direct estimator-bias comparisons.

**Statistical validity:** The taxi study uses 12 settings, 80 sampled markets, and 20 allocations per sample; the supply-chain study averages 1,000 simulations. The source reports estimator distributions and bias comparisons, but it is not a live field experiment.

**Online experiments:** Not specified in source.

**Reproducibility:** The taxi input is public New York City Taxi and Limousine Commission data, and the optimization formulations are explicit. A packaged implementation, seeds, and complete hyperparameters are not specified in source.

**Overall:** Strong theory and controlled simulations support correction in centrally optimized matching systems. Transfer is limited for decentralized choice markets, asymmetric treatment shares, finite samples, and degenerate linear programs.

## 3. Industry Contribution

**Deployability:** Suitable when a platform already performs centralized allocation through a linear program and can retain primal and dual solutions.

**Problems solved:** Interference bias caused by treatment and control units consuming shared marketplace capacity.

**Engineering cost:** Medium to high: production matching must be faithfully represented, dual solutions must be stable, and Two-LP requires extra counterfactual solves. Shadow Price avoids most re-optimization but still depends on an optimization-mediated marketplace.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Use the matching program's dual prices as a first-order, finite-system estimate of the global treatment effect while preserving ordinary user randomization.

**Prior work comparison:** Blake and Coey study test-control interference; Fradkin uses simulation for digital matching platforms; Ugander et al. develop graph-cluster randomization; Holtz et al. apply cluster randomization to marketplaces; Bojinov et al. analyze switchbacks; Johari et al. analyze two-sided randomization.

**Verification:** Limited to works explicitly named in the source-scoped NotebookLM response.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| NYC Taxi and Limousine Commission June 2023 trip records | https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page | Yes | Approximately 10 million origin-destination pairs underpin the ride-hailing simulation. |
| Stylized supply-chain network | Not specified in source | No standalone dataset | Two plants, two retailers, and two five-node warehouse layers. |

**Offline experiment reproducibility:** Partially reproducible from the public taxi data and stated optimization model; code and exact simulation configuration are not supplied in the source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Estimate a treatment's global value from the marginal value of scarce matching constraints instead of comparing the realized totals of treatment and control users who compete with one another.

**Metrics and reported effect:** In simulated high-contention taxi markets, the real efficiency gain is up to 20% below the raw demand increase; Shadow Price and Two-LP remove nearly all simulated bias. In undersupplied supply chains, ordinary randomization overstates effect magnitude by more than twofold.

**Capacity/interference relevance:** Both are explicit: demand, supply, and network capacities constrain allocation, and competition over them creates interference. The model assumes centralized algorithmic matching, unlike mutual user choice in dating.

**Practical mapping:** If a dating marketplace introduces a constrained allocation layer, its dual values could correct experiments on total matches or another linear edge metric. Without such a layer, the paper does not directly provide prices for reply capacity, conversations, match Gini, wasted likes, or two-sided retention.

**Dating fit: Low.** The interference principle matters, but the estimator requires a centralized linear-program matching mechanism absent from ordinary double-opt-in dating.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Ido Bright, Arthur Delarue, Ilan Lobel  
**Affiliations:** Lyft; Georgia Institute of Technology; New York University  
**Venue:** arXiv working paper  
**Year:** 2022 (version 4 dated 2024)  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Reducing Marketplace Interference Bias Via Shadow Prices
- **Authors/organization:** Ido Bright, Arthur Delarue, Ilan Lobel; Lyft, Georgia Tech, NYU
- **Year:** 2022
- **Venue/type:** arXiv working paper
- **Link:** https://arxiv.org/abs/2205.02274
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Modeled demand and supply arrivals in centrally optimized matching and network-flow markets, proved why ordinary randomized experiments overstate global effects under contention, and proposed Two-LP and Shadow Price estimators. Simulations based on New York City taxi trips and a stylized supply chain compare estimator bias and variance against known global effects.
- **Mechanism relevant to two-sided balancing (≤50 words):** Value experimental demand changes by the dual prices of scarce allocation constraints. Marginal values internalize competition for shared capacity that ordinary treatment-control totals ignore.
- **Metrics and reported effect:** Ordinary randomization misses an efficiency gain up to 20% smaller than demand growth and overstates undersupply effects by more than twofold; Shadow Price substantially reduces simulated bias.
- **Dating-app fit:** Low — useful interference logic, but it assumes centralized linear-program allocation rather than decentralized mutual choice.
- **Confidence:** High on source-scoped theory and simulations; medium on dating transfer.
