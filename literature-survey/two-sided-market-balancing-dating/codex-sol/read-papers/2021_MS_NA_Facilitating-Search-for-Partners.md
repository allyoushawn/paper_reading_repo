# Paper Analysis: Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions

**Source:** https://web.stanford.edu/~dsaban/facilitating-search.pdf  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions  
**Authors:** Yash Kanoria, Daniela Saban  
**Abstract:** In dynamic matching markets, agents incur screening costs to learn pair-specific value, and unrestricted proposal behavior creates rejection externalities and congestion. The paper models stationary equilibria with arrivals and departures and shows that restricting which side proposes or screens, or hiding quality tiers, can improve average and lower-tier welfare.

**Key contributions:**

- A continuous-time strategic search model with idiosyncratic values, screening costs, arrivals, and exogenous departures.
- Analysis of directional search, one-sided screening, centralized matching, and hidden quality information.
- Conditions under which restricting action raises average welfare or creates a Pareto improvement.

**Methodology:** Workers and employers arrive stochastically, receive Poisson opportunities, pay to screen a candidate's pair-specific value, and use equilibrium acceptance thresholds. The paper characterizes evolutionarily stable stationary equilibria and compares unrestricted search with policies that block one side from proposing or screening and conceal vertical-quality tiers.

**Main results:** When worker screening costs are twice employer costs, employer-only proposing improves average welfare by up to 14.6%. When workers arrive twice as fast as employers, blocking worker proposals increases worker utility by up to 31% and average welfare by up to 10%, while employer utility falls by less than 8%.

## 2. Experiment Critique

**Design:** The evidence is analytical and numerical, not empirical. Counterfactuals cover unequal screening costs, a two-to-one long/short-side imbalance, and vertically differentiated worker types.

**Statistical validity:** Equilibrium and limiting claims are supported by proofs. Standard errors, confidence intervals, hypothesis tests, and field data are not specified in source.

**Online experiments:** Not specified in source.

**Reproducibility:** Model equations, assumptions, and proofs are supplied. Code, data, and a replication package are not specified in source.

**Overall:** The source identifies a credible congestion externality and conditions for welfare gains, but results depend on strong assumptions: independent uniform values, common departure rate, fixed lifetime strategies, instantaneous responses, no transfers, and often a vanishing departure-rate limit.

## 3. Industry Contribution

**Deployability:** Directional initiation and hidden quality tiers are simple product rules; choosing the correct proposing side requires estimating market imbalance and side-specific screening costs.

**Problems solved:** Rejection-driven wasted effort, congestion from inactive selective recipients, and welfare loss for long-side or lower-tier users.

**Engineering cost:** Low for global messaging/proposal rules; higher for segment-specific controls, causal calibration, monitoring strategic behavior, and interference-aware testing.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Shows in a dynamic strategic-search model that restricting agent actions can mitigate rejection externalities and the inspection paradox.

**Prior work comparison:** Gale and Shapley (1962) omit search costs; Rochet and Tirole (2003) model cross-side participation but not partner search; Pissarides (2000) uses random meetings; Fradkin (2015) and Horton (2015) document marketplace frictions empirically; Halaburda, Piskorski, and Yildirim (2016) study restricting choice in a static game; Weintraub et al. (2008) provide a mean-field equilibrium foundation.

**Verification:** The queried source supports the model and comparisons. Venue/year use the verified survey queue because the PDF text identifies a 2017 working-paper date.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic equilibrium settings | Not applicable | Reconstructable | Uniform pair values and explicit arrival/screening parameters. |
| Airbnb, Upwork, TaskRabbit evidence | Prior works | Not specified | Motivation only, not evaluation data. |

**Offline experiment reproducibility:** Requires implementing the equilibrium calculations; code is not specified in source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Restrict which side can initiate, disable screening on one or both sides, or hide vertical-quality tiers. Directional search moves initiation to the side with lower screening cost or scarcer supply, reducing rejection externalities imposed on the other side.

**Metrics and reported effect:** Average and side-specific welfare are reported. With 2x worker screening cost, directional search raises average welfare up to 14.6%. With a 2:1 long-side imbalance, it raises long-side utility up to 31% and average welfare up to 10%, while short-side utility declines less than 8%. Match, conversation, retention, and wasted-action counts are not specified.

**Capacity/congestion relevance:** Congestion is a queue of selective "reacher" agents who remain active but reject lower-tier proposals, wasting proposers' screening effort. Hard inbox, reply, or swipe caps are not modeled.

**Practical mapping:** Proposals map to likes or first messages and screening to profile evaluation. A dating product can constrain which side initiates or conceal popularity signals. Calibration must accommodate bilateral initiating, delayed replies, correlated preferences, and finite conversation capacity.

**Dating fit: High.** Dating is an explicit application, and directional initiation directly targets rejection congestion; however, evidence is theoretical and the policy can reduce welfare when imbalance is small or parameters fall outside the beneficial region.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2022_OR_NA_Assortment-Two-Sided-Sequential-Matching.md](./2022_OR_NA_Assortment-Two-Sided-Sequential-Matching.md) | Novelty vs. Prior Work — Comparison | Cites Kanoria and Saban as limiting-choice/congestion prior work versus this assortment formulation. |
| [2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md](./2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md) | Novelty vs. Prior Work — Background | Cites Kanoria and Saban (2021) on action restrictions. |
| [2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md](./2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md) | Novelty vs. Prior Work — Background | Cites Kanoria and Saban (2021) as restricting decentralized actions. |

## Meta Information

**Authors:** Yash Kanoria, Daniela Saban  
**Affiliations:** Columbia Business School; Stanford Graduate School of Business  
**Venue:** Management Science (per survey queue/brief; queried PDF identifies a 2017 working-paper version)  
**Year:** 2021 (publication year per survey queue/brief)  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions
- **Authors/organization:** Yash Kanoria, Daniela Saban; Columbia Business School and Stanford Graduate School of Business
- **Year:** 2021
- **Venue/type:** Management Science; theoretical matching-market paper
- **Link:** https://web.stanford.edu/~dsaban/facilitating-search.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Built a dynamic matching model with arrivals, departures, strategic thresholds, and costly discovery of pair-specific value. They compare unrestricted search with directional proposals, one-sided or disabled screening, and hidden quality tiers, proving and numerically illustrating when restricting actions improves side-specific and average welfare.
- **Mechanism relevant to two-sided balancing (≤50 words):** Force the short side or lower-screening-cost side to initiate so the congested long side can screen rather than send mostly rejected proposals. Hiding quality tiers can prevent selective recipients from remaining active while ignoring lower-tier users.
- **Metrics and reported effect:** Up to +14.6% average welfare with asymmetric screening cost; with a 2:1 imbalance, up to +31% long-side utility and +10% average welfare, with <8% short-side loss. Direct match and retention effects are not specified.
- **Dating-app fit:** High — directional initiation and hidden popularity are concrete dating-market levers, though theory predicts parameter-dependent backfire risk.
- **Confidence:** High on the source-scoped model/results; medium on publication metadata because the queried PDF is a 2017 working version while the queue records Management Science 2021.
