# Paper Analysis: Assortment Planning for Two-Sided Sequential Matching Markets

**Source:** https://web.stanford.edu/~iashlagi/papers/assortment.pdf  
**Date analyzed:** 2026-08-18

---

## 1. Summary

**Title:** Assortment Planning for Two-Sided Sequential Matching Markets  
**Authors:** Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur  
**Abstract:** A platform choosing personalized partner menus must trade off giving users enough attractive options against collisions when many users choose the same capacity-limited partner. The paper proves this two-stage assortment problem is strongly NP-hard and gives a polynomial-time constant-factor approximation based on supplier bucketing, linear-program relaxations, rounding, and coordinated menu construction.

**Key contributions:**

- A two-stage multinomial-logit model in which customers choose from platform menus and suppliers then choose at most one interested customer.
- Constant-factor approximation algorithms for low-value and high-value supplier regimes and a black-box combination for the general case.
- A menu-construction rule that approximately balances impressions among similar suppliers to reduce collisions.

**Methodology:** Suppliers are bucketed by public attractiveness and outside-option value. In the low-value regime, a linear program assigns bucket-level exposure, a rounding algorithm converts fractional allocations to integers, and a load-balancing step assigns individual suppliers. In the high-value regime, each customer receives one supplier; a concave relaxation allocates customers among suppliers. The general algorithm partitions suppliers by value and combines both regimes.

**Main results:** In simulations with 100 suppliers and 50–150 customers, the algorithm's mean match-count ratio to a relaxed upper bound ranges from 0.37 to 0.47 and never falls below about one third across tested instances. The general theoretical guarantee is at least one half of the smaller low- and high-value approximation factors.

## 2. Experiment Critique

**Design:** The paper combines proofs with synthetic simulations. For each combination of customer count and exponential-distribution parameters, it generates 25 market instances and averages 30 independent choice simulations per instance. The only empirical comparator is a linear-relaxation upper bound; standard greedy or unconstrained recommendation heuristics are not evaluated.

**Statistical validity:** Mean, minimum, and median algorithm-to-upper-bound ratios are reported. Confidence intervals, standard errors, hypothesis tests, and a power analysis are not specified in source.

**Online experiments:** Not specified in source.

**Reproducibility:** Algorithms and generative parameters are described, including `lambda_v, lambda_o in {1, 10}`. Public code, a static dataset, data splits, and a replication package are not specified in source.

**Overall:** Proofs support the hardness and approximation claims, and simulations show stable performance against a deliberately optimistic upper bound. Evidence for heterogeneous, dynamic, real-world dating markets is absent.

## 3. Industry Contribution

**Deployability:** The method is a global assortment-allocation layer. Bucketing and linear optimization are polynomial-time, but a production system would need estimated bilateral choice and outside-option scores plus repeated menu recomputation.

**Problems solved:** Overexposure of popular profiles, conflicting requests, and wasted demand when each recipient can consummate at most one match.

**Engineering cost:** Moderate to high: LP solving, supplier bucketing, integer rounding, balanced menu assignment, and reliable capacity/choice estimates are required.

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** It formulates decentralized two-sided assortment planning with preferences on both sides and supplies an efficient constant-factor approximation.

**Prior work comparison:** van Ryzin and Mahajan (1999) and Talluri and Van Ryzin (2004) study one-sided assortment choice; Rusmevichientong et al. (2010) and Davis et al. (2013) add inventory capacities; Halaburda et al. (2017), Arnosti et al. (2014), and Kanoria and Saban (2020) study limiting choice or congestion; Feldman et al. (2009) and related online-matching work centrally coordinate arrivals. This paper instead sets menus before simultaneous decentralized choices, creating collisions.

**Verification:** Novelty is supported by the source's formal comparison and hardness/approximation results. Independent web verification was not part of this source-scoped batch.

## 5. Dataset Availability

**Datasets mentioned:**

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic two-sided markets | Not applicable | Reconstructable | 100 suppliers; 50–150 customers; exponential attractiveness and outside-option draws. |

**Offline experiment reproducibility:** The distributions and simulation counts are specified, but code and a replication package are not specified in source.

## 6. Community Reaction

Not specified in source.

## Project Relevance

**Exact mechanism:** Allocate personalized profile assortments globally. Similar recipients are bucketed by attractiveness and outside-option value, then exposure is balanced within each bucket so fewer senders collide on the same popular recipient.

**Metrics and reported effect:** Expected matches are the objective. Across synthetic settings, the algorithm attains mean algorithm-to-upper-bound ratios of 0.37–0.47 and at least one third in every tested instance. Conversations, retention, and a direct wasted-like count are not specified in source.

**Capacity/congestion relevance:** Each agent can match at most once. Congestion appears as multiple customers selecting the same supplier; the supplier's match probability `|M_j|/(|M_j|+q_j)` has diminishing marginal returns. The menu rule also bounds how often a supplier is displayed.

**Practical mapping:** Customers map to swiping daters, suppliers to shown profiles, first-stage selections to likes, and second-stage selections to like-backs. A dating implementation needs symmetric roles, heterogeneous pair-specific preferences, asynchronous arrivals, and softer conversation/reply capacities instead of a single-match cap.

**Dating fit: Medium.** The collision mechanism directly addresses wasted likes to popular profiles, but the evaluated model is asymmetric, homogeneous on one side, static, and synthetic.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------------|-----------------|-----------------------------|
| No verified inbound mentions within the 45-source corpus. | — | — |

## Meta Information

**Authors:** Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur  
**Affiliations:** Stanford University; Duke University; Facebook; Stanford Graduate School of Business  
**Venue:** Operations Research (per survey queue/brief; not specified in queried PDF text)  
**Year:** 2022 (per survey queue/brief; not specified in queried PDF text)  
**PDF:** available  
**Relevance:** Core  
**Priority:** 2

## Annotated Bibliography Fields

- **Title:** Assortment Planning for Two-Sided Sequential Matching Markets
- **Authors/organization:** Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur; Stanford University, Duke University, Facebook, Stanford Graduate School of Business
- **Year:** 2022
- **Venue/type:** Operations Research; theoretical and simulation paper
- **Link:** https://web.stanford.edu/~iashlagi/papers/assortment.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Modeled a platform that chooses supplier menus before customers and suppliers make sequential, reciprocal choices. After proving the optimization strongly NP-hard, the authors developed polynomial-time constant-factor algorithms using supplier bucketing, linear-program relaxations, rounding, and balanced menu construction. Synthetic simulations test realized matches against a relaxed upper bound.
- **Mechanism relevant to two-sided balancing (≤50 words):** Allocate menus globally and spread exposure approximately evenly among suppliers with similar attractiveness and outside options. This reduces collisions in which many customers choose one capacity-limited supplier while comparable suppliers receive too little demand.
- **Metrics and reported effect:** Expected matches; mean algorithm-to-upper-bound ratio 0.37–0.47 across tested settings and at least one third in every instance. Conversations, retention, and direct wasted-like effects are not specified.
- **Dating-app fit:** Medium — direct collision-aware assortment allocation, but asymmetric homogeneous-choice assumptions and one-match capacity require substantial adaptation.
- **Confidence:** High on source-scoped model and simulation claims; medium on venue/year metadata because those are supplied by the verified survey queue rather than the queried PDF text.
