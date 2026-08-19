# Paper Analysis: Assortment Planning for Two-Sided Sequential Matching Markets

**Source:** Itai Ashlagi (Stanford), Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban (Stanford GSB), Kirankumar Shiragur. Operations Research, 2022. NotebookLM source_id `8608cddc-7ce5-4442-a73b-4f882753f031`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** Assortment Planning for Two-Sided Sequential Matching Markets
**Authors:** Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur
**Abstract:**
Two-sided matching platforms (labor, dating, accommodation) recommend menus of potential partners and must trade off showing customers more suppliers (raising the chance of a match) against "collisions" — multiple customers converging on the same supplier, who can match with at most one, wasting the others' capacity/effort. The paper introduces a stylized two-stage sequential-choice model (customers choose from a platform-curated menu via MNL; suppliers then choose among the customers who selected them, also via MNL) and proves the platform's menu-optimization problem is strongly NP-hard, then gives a polynomial-time constant-factor approximation algorithm.

**Key contributions:**
- Proof that the two-sided sequential assortment problem is strongly NP-hard (reduction from three-partition).
- A constant-factor approximation algorithm built by solving two regimes separately (high-value suppliers: each customer sees one supplier; low-value suppliers: two-dimensional bucketing of suppliers by attractiveness and outside-option value, LP relaxation, rounding, and menu construction) and combining them.
- The menu-construction step explicitly balances exposure: it shows each supplier in a bucket to approximately the same number of customers, which the paper states is designed to minimize "collisions" (over-subscription).
- The paper's own text explicitly cites dating apps as a motivating example of platforms that "assign attractiveness scores to their users and make display decisions based primarily on these scores."

**Methodology:** Two-stage sequential discrete-choice model (MNL on both sides) with a capacity constraint (each supplier matches at most once); NP-hardness proof; LP-relaxation + bucketing + rounding algorithm with provable approximation guarantees.

**Main results:** Simulation on markets with 100 suppliers, m ∈ {50,...,150} customers: the algorithm consistently captures ≥1/3 (at least 33%) of the linear-programming upper bound on expected matches across 25 random instances × 30 simulation runs per parameter combination, robust to alternative outside-option distributions.

---

## 2. Experiment Critique

**Design:** Purely theoretical/simulation paper — no real-world A/B test. Synthetic markets generated with supplier attractiveness `v_j = 1/(1+z_j)` and outside-option `q_j = 1+w_j`, both exponential draws, swept across `(m, λ_v, λ_o)`. Robustness checked against alternative outside-option distributions.

**Statistical validity:** Not an inferential-statistics paper; reports algorithm-vs-upper-bound ratios (mean/min/median across 25 instances × 30 simulation runs) rather than significance tests — appropriate for a theoretical approximation-algorithm paper.

**Online experiments (if any):** None — no production deployment or A/B test reported.

**Reproducibility:** Full model, LP formulation, and both algorithms (rounding, menu construction) are given in closed form; synthetic data generation process is fully specified, so the simulations are reproducible from the paper alone.

**Overall:** Strong for what it is — a rigorous theory/algorithms paper with formal approximation guarantees, validated by matching simulation results. Its "capacity constraint = matches once" and "collision avoidance via balanced exposure" claims are well supported by both the proofs and the simulation ratios.

---

## 3. Industry Contribution

**Deployability:** The bucketing + LP-relaxation + rounding pipeline is described as intentionally resembling how marketplaces already implement assortment decisions in practice — practical to implement (the authors flag this as a design goal, not just a theoretical curiosity).

**Problems solved:** Exactly the project's core "wasted likes from over-subscription" problem — the paper frames its objective as maximizing expected total matches while controlling supplier-side congestion from simultaneous customer-side interest.

**Engineering cost:** Moderate — requires periodic (or online) LP solves over supplier buckets plus a rounding/menu-construction pass; the bucketing approach (grouping by two continuous scores into discrete buckets) is a standard, implementable clustering step.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First constant-factor approximation algorithm for the two-sided sequential assortment problem with heterogeneous, capacity-constrained (match-once) suppliers, extending single-sided assortment-optimization literature (van Ryzin & Mahajan 1999; Talluri & Van Ryzin 2004) to a genuinely bilateral, capacity-limited setting.

**Prior work comparison (top cited works per source):**
1. van Ryzin & Mahajan (1999), "On the relationship between inventory costs and variety benefits in retail assortments" — foundational MNL assortment optimization.
2. Talluri & Van Ryzin (2004), "Revenue management under a general discrete choice model of consumer behavior."
3. Kanoria & Saban (2020), "Facilitating the search for partners on matching platforms" — directly related search-restriction literature (also in this notebook, see companion analysis).
4. Halaburda, Piskorski & Yıldırım (2017), "Competing by restricting choice: The case of matching platforms."
5. Arnosti, Johari & Kanoria (2014), "Managing congestion in decentralized matching markets."
6. Immorlica & Mahdian (2005), "Marriage, honesty, and stability."
7. Kojima & Pathak (2009), "Incentives and stability in large two-sided matching markets."

**Verification:** Novelty claim is credible — the paper explicitly distinguishes itself from prior choice-restriction literature (Kanoria & Saban, Arnosti et al., Halaburda et al.) by allowing the platform to select an explicit *assortment* as the design lever (not just binary restriction of who may propose), and by allowing full agent heterogeneity rather than ex-ante homogeneous agents.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Synthetic simulated markets (100 suppliers, m∈{50..150} customers) | — | N/A (generated, not external) | Fully specified generative process (exponential draws for v_j, q_j); reproducible from paper text |

**Offline experiment reproducibility:** Fully reproducible — no external data dependency, generative process given explicitly.

---

## 6. Community Reaction

Not assessed for this source (out of scope for Phase 3 batch processing).

---

## Papers That Mention This Paper (Reverse Citation Map)

*Automatically filled in during Phase 3.7 of literature-survey. Leave blank when first created.*

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**Authors:** Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur
**Affiliations:** Stanford University / Stanford GSB (per author list; Makhijani affiliation not confirmed from source excerpts)
**Venue:** Operations Research, 2022
**Year:** 2022
**PDF:** Not fetched directly — analyzed via NotebookLM source
**Relevance:** Core — theoretical foundation for capacity-aware exposure allocation, explicitly motivated by dating-app-style attractiveness-score display decisions
**Priority:** 1

---

## Bibliography Fields

- **title:** Assortment Planning for Two-Sided Sequential Matching Markets
- **authors or organization:** Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur
- **year:** 2022
- **venue or type:** Operations Research (journal)
- **link:** Not directly retrieved from source (Operations Research 2022; also circulated as a working paper)
- **tier tag:** Tier 2 — Applied research on real matching/dating-style platforms
- **what they did (≤80 words):** Modeled two-sided matching platforms as a sequential MNL choice game (customers choose from a curated menu, then suppliers choose among interested customers, capacity-limited to one match each), proved menu optimization is strongly NP-hard, and designed a polynomial-time constant-factor approximation algorithm using two-dimensional bucketing of suppliers, an LP relaxation, and a rounding/menu-construction procedure that balances how often each supplier is shown.
- **mechanism relevant to two-sided balancing (≤50 words):** Menu-construction algorithm caps and balances each supplier's exposure count based on attractiveness and outside-option value, provably minimizing "collisions" (simultaneous over-subscription) while retaining a constant-factor guarantee on total expected matches versus the unconstrained optimum.
- **metrics used, and the reported effect:** Ratio of algorithm's expected matches to LP-relaxation upper bound; algorithm consistently achieves ≥1/3 (≥33%) of the upper bound across simulated markets (100 suppliers, 50–150 customers, 25 instances × 30 runs each), degrading gracefully (~0.40–0.47 ratio) as market size grows.
- **fit for a dating app:** high — the paper explicitly names dating apps as the motivating example for attractiveness-score-based display decisions, and its exposure-balancing mechanism (cap supplier exposure inversely to desirability, directly bounding over-subscription) is a near-direct algorithmic template for redistributing likes away from over-subscribed profiles toward reply-capacity-matched exposure.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with extensive direct quotes, full equations, simulation table, and a citation list matching a real, known Operations Research paper; source_id validated in all three queries; the "for dating apps" phrase is a verbatim quote from the paper itself).

---

## Project Relevance

This is one of the strongest direct theoretical matches found in the survey for the project's Layer 2 (capacity-aware exposure allocation). The paper's own motivating language explicitly targets dating apps' practice of "assign[ing] attractiveness scores to their users and mak[ing] display decisions based primarily on these scores" — the exact mechanism the project needs to redesign. Its core insight — that a capacity-limited supplier (mapping directly onto a dating-app user's finite reply capacity) suffers "collisions" when over-shown, wasting the excess likes/matches of everyone else who selected them — is structurally identical to the project's "wasted likes on over-subscribed users" framing. The menu-construction algorithm's property that each supplier's exposure count is provably bounded as a function of their attractiveness and outside-option value (`c_{k,j} ≤ 2 + q_{k2}/2w_{k1}`) is directly implementable as a capacity-aware exposure cap: highly desirable, highly selective users get *throttled* exposure (they'll convert almost any impression into interest, so showing them less still fills their capacity), while less desirable or less selective users get *boosted* exposure to compensate for lower conversion odds — this is nearly the reciprocal of LiJAR's boost/penalize logic (see companion analysis `2017_KDD_LiJAR...md`) but derived from first principles with a provable approximation guarantee rather than empirical tuning. Two caveats for adaptation: (1) the model treats customers (initiators) as ex-ante homogeneous, which does not capture personalized/mutual reciprocal affinity beyond a single desirability score — the project's reciprocal-scoring layer (Layer 1) would need to sit upstream of this mechanism to first estimate `v_j` and `q_j` per viewer-pair rather than using a single public score; (2) the paper's static, simultaneous-choice batch model (explicitly compared to "swiping once a day") maps well onto daily curated-batch designs but not to continuous real-time swipe feeds without further adaptation.
