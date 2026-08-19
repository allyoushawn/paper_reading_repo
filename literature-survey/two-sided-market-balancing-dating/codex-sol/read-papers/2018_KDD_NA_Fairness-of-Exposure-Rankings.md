# Paper Analysis: Fairness of Exposure in Rankings

**Source:** https://arxiv.org/abs/1802.07281  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Fairness of Exposure in Rankings  
**Authors:** Ashudeep Singh, Thorsten Joachims  
**Abstract:** Relevance-only ranking can turn small score differences into winner-take-all exposure. The paper represents a randomized ranking as a doubly stochastic matrix and maximizes expected ranking utility subject to linear demographic-parity, disparate-treatment, or disparate-impact constraints, then samples deterministic rankings through Birkhoff-von Neumann decomposition.

**Key contributions:**

- Defines expected item exposure from rank-position bias.
- Expresses multiple group-fairness concepts as linear constraints on probabilistic rankings.
- Supplies a polynomial-time LP and decomposition pipeline for serving fair rankings in expectation.

**Methodology:** Optimize `u^T P v`, where `u` is relevance, `v` is position exposure, and `P` is a doubly stochastic ranking matrix. Linear constraints equalize group exposure, make exposure proportional to group utility, or make expected clicks proportional to group utility. Decompose `P` into a mixture of permutation matrices and sample a deterministic ranking.

**Main results:** In a six-person job example, disparate-treatment ratio falls 1.7483→1.0000 while DCG falls 3.8193→3.8044; disparate-impact ratio falls 1.8193→1.0000 with DCG 3.8025. On a 25-article news subset, DTR falls 1.0859→1.0000 with DCG 5.2027→5.1983, and DIR falls 1.5211→1.0000 with DCG 5.1461.

## 2. Experiment Critique

**Design:** Evaluation uses a stylized six-candidate job ranking and a processed subset of the Yow news dataset. The comparator is the unconstrained Probability Ranking Principle ranking.

**Statistical validity:** Exact DCG and fairness ratios are reported, and the optimization guarantees constraint satisfaction in expectation. Confidence intervals, standard errors, significance tests, repeated trials, and power analysis are not specified in source.

**Online experiments:** Not specified in source.

**Reproducibility:** The LP, exact stylized utilities, news preprocessing, and a third-party Birkhoff decomposition repository are provided. A complete official code/replication package is not specified in source.

**Overall:** The examples validate exact constraint satisfaction and expose the cost of fairness, but they are small offline settings with no reciprocal choice, recipient capacity, or live behavioral response.

## 3. Industry Contribution

**Deployability:** The method is a constrained reranking layer that samples deterministic rankings from an optimized distribution. Per-query `N x N` linear programs can be expensive for large candidate sets.

**Problems solved:** Winner-take-all exposure, group underexposure, and utility-fairness trade-offs.

**Engineering cost:** Relevance and position-bias estimation, LP infrastructure, fairness-policy specification, decomposition/sampling, and exposure auditing.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** A flexible exposure-allocation formulation that maximizes expected utility under linear group or individual fairness constraints.

**Prior work comparison:** Robertson (1977) establishes relevance-only ranking; Dwork et al. (2012) formalize individual fairness; Zehlike et al. (2017) enforce binary top-k representation; Biega et al. (2018) amortize individual attention; Celis et al. (2017) constrain sensitive attributes; Hardt et al. (2016) formalize equality of opportunity. This paper directly links position exposure, relevance, and impact within one probabilistic-ranking LP.

**Verification:** The source supports its mathematical comparisons and evaluation. Independent web novelty verification was not part of this source-scoped batch.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Stylized job seekers | Not applicable | Yes | Six candidates and utilities are fully stated. |
| Yow news dataset | Link not specified in source | Public | Evaluation uses 25 articles from two feeds. |

**Offline experiment reproducibility:** The mathematical inputs and preprocessing are largely specified; a complete paper-specific repository is absent.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Optimize a probabilistic ranking under linear constraints on average exposure or expected impact, then decompose and sample deterministic rankings so constraints hold in expectation.

**Metrics and reported effect:** In the job example, DTR 1.7483→1.0000 and DIR 1.8193→1.0000 for DCG reductions of 0.0149 and 0.0168. In news, DTR 1.0859→1.0000 with DCG loss 0.0044; DIR 1.5211→1.0000 with loss 0.0566. Match, conversation, wasted-like, and retention outcomes are not specified.

**Capacity/congestion relevance:** Exposure is scarce through rank-position bias, but hard reply limits, individual congestion, oversubscription, and diminishing returns are not modeled.

**Practical mapping:** Dater attention maps to position exposure and recipient quality/compatibility to relevance. A dating version must use reciprocal utility and add per-profile capacity or marginal-value constraints instead of only group-level exposure ratios.

**Dating fit: Low.** It is a useful allocation primitive, but the source treats ranked entities as passive and does not model double opt-in or recipient queues.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| [2018_CIKM_Adaptive-Fairness_Fair-Marketplace-Counterfactual-Evaluation.md](./2018_CIKM_Adaptive-Fairness_Fair-Marketplace-Counterfactual-Evaluation.md) | Novelty vs. Prior Work — Extension | States the marketplace paper builds on Singh and Joachims' *Fairness of Exposure in Rankings*. |
| [2019_KDD_DetGreedy_Fairness-Aware-Ranking-Talent-Search.md](./2019_KDD_DetGreedy_Fairness-Aware-Ranking-Talent-Search.md) | Novelty vs. Prior Work — Comparison | Contrasts Singh and Joachims' large-LP exposure optimization with this paper's production-latency emphasis. |
| [2021_NeurIPS_LorenzWelfare_Two-Sided-Fairness-Lorenz-Dominance.md](./2021_NeurIPS_LorenzWelfare_Two-Sided-Fairness-Lorenz-Dominance.md) | Novelty vs. Prior Work — Comparison | Explicitly compares against Singh and Joachims' fairness-of-exposure ranking. |
| [2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md](./2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md) | Novelty vs. Prior Work — Extension | States the paper extends Singh and Joachims' exposure fairness. |

## Meta Information

**Authors:** Ashudeep Singh, Thorsten Joachims  
**Affiliations:** Cornell University  
**Venue:** KDD 2018  
**Year:** 2018  
**PDF:** available via arXiv  
**Relevance:** Core  
**Priority:** 3

## Annotated Bibliography Fields

- **Title:** Fairness of Exposure in Rankings
- **Authors/organization:** Ashudeep Singh, Thorsten Joachims; Cornell University
- **Year:** 2018
- **Venue/type:** KDD 2018; academic conference paper
- **Link:** https://arxiv.org/abs/1802.07281
- **Tier tag:** Tier 3
- **What they did (≤80 words):** Formulated rankings as doubly stochastic exposure-allocation matrices, maximized expected utility subject to demographic-parity, disparate-treatment, or disparate-impact constraints, and used Birkhoff-von Neumann decomposition to sample deterministic rankings. Offline job and news examples quantify exact fairness ratios and DCG cost.
- **Mechanism relevant to two-sided balancing (≤50 words):** Treat position exposure as a scarce allocatable resource. Solve a linear program that maximizes relevance while enforcing exposure or expected-impact ratios, then sample rankings from the optimized distribution. Recipient-level capacity and reciprocal response must be added for dating.
- **Metrics and reported effect:** Job DTR 1.7483→1.0000 with DCG 3.8193→3.8044; job DIR 1.8193→1.0000 with DCG 3.8025. News DTR and DIR reach 1.0000 with small-to-moderate DCG costs.
- **Dating-app fit:** Low — exposure allocation transfers, but reciprocity and capacity are absent.
- **Confidence:** High — peer-reviewed primary source with explicit formulation and exact offline results.
