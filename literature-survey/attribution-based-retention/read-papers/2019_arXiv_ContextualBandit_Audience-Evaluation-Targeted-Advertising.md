# Paper Analysis: Online Evaluation of Audiences for Targeted Advertising via Bandit Experiments

**Source:** https://arxiv.org/pdf/1907.02178.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Online Evaluation of Audiences for Targeted Advertising via Bandit Experiments  
**Authors:** Tong Geng, Xiliang Lin, Harikesh S. Nair  
**Abstract:** **(1) Core problem and key contribution**

*   **Core Problem:** When running digital advertising campaigns, advertisers must match specific creatives to specific Target Audiences (TAs). A major challenge arises when these TAs overlap (e.g., "San Francisco users" and "Male users" contain overlapping segments). Standard industry "split-testing" struggles with this overlap: assigning an overlapping user strictly to one TA arm violates the representativeness of the other TA, while dropping…

**NotebookLM extraction (Query 1 — scope: this source):**

**(1) Core problem and key contribution**

*   **Core Problem:** When running digital advertising campaigns, advertisers must match specific creatives to specific Target Audiences (TAs). A major challenge arises when these TAs overlap (e.g., "San Francisco users" and "Male users" contain overlapping segments). Standard industry "split-testing" struggles with this overlap: assigning an overlapping user strictly to one TA arm violates the representativeness of the other TA, while dropping users to maintain representativeness results in wasted data. Furthermore, typical A/B tests are non-adaptive, meaning they allocate the same amount of costly traffic to poorly performing creatives as they do to winning ones throughout the test.
*   **Key Contribution:** The authors propose an adaptive contextual bandit algorithm that solves the overlap problem by partitioning the overlapping TAs into completely mutually exclusive Disjoint Audiences (DAs). By treating these DAs as the context for a Thompson Sampler, the algorithm adaptively learns the best creative for each non-overlapping sub-population to minimize the advertiser's costs (regret), while simultaneously using probabilistic aggregation to assess the true value of the broader, overlapping TAs. The authors successfully deployed this algorithm as a real-world testing product on JD.com.

**(2) Proposed method or architecture in detail**

*   **Step 1: Disjoint Partitioning:** The system takes the advertiser's $K$ target audiences and splits them into $J$ disjoint sub-populations (DAs) so that every user uniquely maps to only one DA context. 
*   **Step 2: Contextual Thompson Sampler Formulation:** The algorithm treats each DA as a distinct context and each creative as an arm. Because the desired user feedback (clicks) is binary, the algorithm uses a Beta-Bernoulli framework. The probability of a click (CTR) for a specific creative-DA combination is modeled as a Beta distribution, which acts as a conjugate prior to the Bernoulli outcome. 
*   **Step 3: Adaptive Allocation:** As batches of users arrive, the system categorizes each user into their unique DA context, samples parameters from the posterior Beta distributions of all creatives, calculates the expected monetary payoff (minus display costs), and displays the creative with the highest expected payoff. Parameters are updated at the end of each batch using the observed clicks.
*   **Step 4: Probabilistic Aggregation and Stopping Rule:** While the bandit learns at the narrow DA level, the advertiser's goal is to find the best creative for the broader TA level. To bridge this, the algorithm aggregates the posterior distributions of the DAs back up to the TA level using the law of total probability, weighted by the historical population proportion of each DA within the TA. The system continually calculates an estimated "regret" (the expected loss from not picking the best TA-creative combination) and automatically stops the test once the normalized regret for all TAs falls below a strict 1% threshold.

**(3) Datasets used for evaluation and comparison baselines**

*   **Datasets used for evaluation:**
    *   **Simulated Datasets:** The authors generated data for 1,000 multi-batch replications featuring 2 creatives and 2 overlapping TAs (producing 3 DAs) with uniform expected CTR distributions. They explicitly manipulated this data to test how increasing the degree of audience overlap (from 0% to 90%) impacts cross-audience learning and regret.
    *   **Real-World Case Study (JD.com):** The system was evaluated on a live, deployed ad campaign for a large cellphone manufacturer. The campaign featured 2 overlapping TAs and 3 creatives, processing a dataset of 18,499 live users and 631 clicks over a six-hour period.
*   **Comparison baselines:**
    *   **Equal Allocation (EA):** A non-adaptive baseline representing traditional "A/B/n" testing. It evaluates performance at the disjoint DA level but allocates traffic equally among creatives in every batch without adapting to performance feedback.
    *   **Split-Testing (ST):** The standard industry baseline where users are randomized directly into broad TA-arms (ignoring the disjoint DA mapping). Users are only shown a creative if they match the TA definition, meaning overlapping users are either forced into one representative arm or their data is under-utilized.

---

## 2. Experiment Critique

**NotebookLM extraction (Query 2 — scope: this source):**

**(1) Key quantitative results and improvements over baselines**

*   **Higher Accuracy in Finding the Best Combination:** In multi-batch simulations against baselines, the proposed Thompson Sampler (TS) correctly identified the true-best creative-audience combination **85.8% of the time at stopping**, outperforming the Equal Allocation (EA) baseline (77.8%) and the standard industry Split-Testing (ST) baseline (70.8%).
*   **Lower Regret / Cost of Experimentation:** The TS algorithm generated the **smallest amount of expected regret** across all tested methods, progressively decreasing expected regret per impression as batches arrived. ST generated the most regret and required the largest sample sizes because it non-adaptively threw away data from overlapping users.
*   **Real-World Case Study Lift:** In a live 6-hour test deployed on JD.com involving 18,499 users, the algorithm found the best combination with 98.4% posterior probability. A back-of-the-envelope simulation showed that if the non-adaptive EA baseline had been used on that exact same traffic, **the TS generated 52 more clicks (an 8.2% increase in total clicks) than EA**. 

**(2) Limitations, failure modes, or negative results noted by the authors**

*   **Failure at Extreme Audience Overlap:** The authors specifically tested the limits of the algorithm as audience overlap increased (which shrinks payoff differences between audiences). As a negative result, they observed that **when overlap becomes extreme and payoff differences become extremely small, it becomes "increasingly difficult to correctly identify the true-best" combination**, and the confidence (posterior probability) at stopping drops significantly. To fix this in extreme scenarios, the authors note additional stopping conditions may be necessary.
*   **Combinatorial Scalability Limits:** Because the algorithm explicitly breaks target audiences down into disjoint sub-populations, the number of contexts grows combinatorially as the number of target audiences increases. As a limitation, the deployed product **restricts the maximum number of target audiences ($K$) and creatives ($R$) to 5** to keep the required learning parameters manageable.
*   **Long-Term Dependency Assumptions:** The framework assumes that creatives do not induce long-term dependencies (e.g., they do not alter future user arrival rates) and that the auctions are unrelated to each other. 
*   **Unresolved Stopping Rule Debate:** The authors note that the statistical community has an unresolved debate regarding how to properly stop a Thompson Sampler during Bayesian inference, and their chosen stopping rule (based on normalized regret falling below 1%) reflects "practical product-related considerations" rather than resolving this theoretical issue.

**(3) Top 5–7 most heavily cited prior works named in the related work or introduction**

1.  **Scott, S. L. (2015) – *Multi-armed bandit experiments in the online service economy***: Highlighted as one of the closest complementary papers on using bandits to evaluate advertising creatives, and directly utilized by the authors to define their regret estimation and stopping rule formulation.
2.  **Schwartz, Bradlow, and Fader (2017) – *Customer acquisition via display advertising using multi-armed bandit experiments***: Cited alongside Scott (2015) as a primary related work that applies bandit experiments to targeted advertising, though without addressing the specific audience overlap problem.
3.  **Ju et al. (2019) – *A sequential test for selecting the better variant...***: Also cited as a highly relevant complementary paper utilizing bandits for sequential A/B testing of variants.
4.  **Scott, S. L. (2010) – *A modern Bayesian look at the multi-armed bandit***: Cited to support the general finding that the Thompson Sampler achieves superior performance relative to Equal Allocation strategies.
5.  **Russo et al. (2018) – *A tutorial on Thompson sampling***: Cited as the primary theoretical overview for the contextual Thompson Sampler framework utilized in the paper.
6.  **Facebook (2019) and Tencent (2019) Split-Testing Documentation:** Cited directly to define the "audience split-testing" experimental design currently popular in the industry, which serves as the primary real-world baseline the authors aim to improve upon.

---

## 3. Industry Contribution

**Deployability:** Not specified in source beyond what is implied by the empirical setting described in Query 1/2.

**Problems solved:** See Query 1 framing above.

**Engineering cost:** Not specified in source.

---

## 4. Novelty vs. Prior Work

Not specified in source beyond the “prior works” list in Query 2.

---

## 5. Dataset Availability

Not specified in source as a structured dataset table; see Query 1/2 for any named corpora or benchmarks.

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Not specified in source. | | | |

**Offline experiment reproducibility:** Not specified in source.

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

**Authors:** Tong Geng; Xiliang Lin; Harikesh S. Nair  
**Affiliations:** Unknown  
**Venue:** arXiv  
**Year:** 2019  
**PDF:** https://arxiv.org/pdf/1907.02178.pdf  
**Relevance:** Related  
**Priority:** 3

---

## Project Relevance

**Low project relevance.** Based on the provided source, here is the evaluation of the paper against your project framing:

**(A)** No, this paper does not propose or estimate per-touchpoint, per-impression, or per-user incremental credit that could serve as multi-touch attribution (MTA) training labels. 
The granularity of the model's learning and evaluation is at the **aggregate segment level**. While the system assigns individual users to specific "Disjoint Audiences" (DAs) based on their features at the moment of an impression, it does not track users longitudinally or calculate credit for individual touchpoints. Instead, it aggregates all binary outcomes within a batch for a given DA to estimate a segment-wide expected Click-Through Rate (CTR) and payoff.

**(B)** Instead of fractional attribution labels, the system produces an **adaptive traffic allocation policy** and **segment-level performance estimates**. Specifically, it outputs:
*   A contextual policy (via Thompson Sampling) that dictates the probability of displaying a specific creative to a user based on which disjoint segment (DA) they fall into. 
*   Estimates of expected payoff and regret for different creative-audience combinations, ultimately aggregating this data to declare a single "winning" creative for a broader, overlapping Target Audience (TA).
*   **Connection to MTA:** The connection to MTA is virtually nonexistent. This is an A/B testing / experimental design methodology used to optimize creative assignments in isolated, single-step interactions. It explicitly ignores multi-touch journeys.

**(C)** 
*   **Continuous non-purchase conversions:** The methodology as written is incompatible with continuous outcomes like "user days-active". The authors explicitly model the user's action ($y_{irj}$) as a binary variable (e.g., a click, $y \in \{0, 1\}$). Because the feedback is binary, the entire learning architecture relies on a Beta-Bernoulli conjugate prior framework. To handle continuous outcomes, the underlying mathematical framework would need to be rewritten (e.g., using Normal or Gamma distributions).
*   **Selection bias among active users:** The framework is completely unequipped to handle user-level selection bias or accumulating touchpoints. The authors explicitly state that their approach assumes "creatives do not induce long-term dependencies, for instance, that they do not affect future user arrival rates, and that auctions are unrelated to each other". By treating every user arrival as an independent, isolated draw within a batch, it ignores the reality that highly active users on a dating platform will sequentially accumulate multiple overlapping treatments over time.
