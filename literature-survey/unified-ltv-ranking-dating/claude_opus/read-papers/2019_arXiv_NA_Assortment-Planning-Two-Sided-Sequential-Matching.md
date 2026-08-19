# Paper Analysis: Assortment Planning for Two-Sided Sequential Matching Markets

**Source:** arXiv:1907.04485v3 (2020-07-28 revision of a 2019 preprint), Stanford University / Duke University / Facebook. Later published as Ashlagi, Krishnaswamy, Makhijani, Saban, and Shiragur, "Assortment planning for two-sided sequential matching markets," Operations Research, 70(6):2784–2803, 2022 (per that paper's own citation in a bibliography read directly for this batch — not independently verified against the published version). `/Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/1907.04485.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Itai Ashlagi and Daniela Saban (Stanford), Anilesh K. Krishnaswamy (Duke), Rahul Makhijani (Facebook), and Kirankumar Shiragur (Stanford) study a stylized static, two-round matching market — proactive **customers** choose from a platform-constructed **menu** (assortment) of **suppliers** via a multinomial-logit (MNL) choice model, and each chosen supplier then reactively picks at most one of the customers who selected her, also via an MNL-style choice over her outside option. A match requires this mutual sequence of choices. The platform's only lever is the *menu* — the unordered set of suppliers shown to each customer — not their order or position; the model has no ranking or exposure-decay effect within a menu at all. The paper's central trade-off is that larger menus increase each customer's chance of finding an acceptable supplier but also increase **collisions** (multiple customers choosing the same supplier, of whom she can accept only one), which can reduce the total number of matches. The platform's problem — choosing a menu profile to maximize the expected number of matches — is proven strongly NP-hard (via reduction from 3-partition). The authors' main contribution is an efficient, polynomial-time algorithm with a **constant-factor approximation guarantee** to the optimal expected number of matches, built by separately solving two regimes (low-value suppliers, where the outside option is ex-ante at least as good as any single supplier, requiring an LP relaxation over suppliers "bucketed" by similar attractiveness and outside-option scores, plus a rounding step; and high-value suppliers, where a single-supplier menu per customer already suffices) and combining the two regime-specific algorithms in a black-box fashion. Suppliers are heterogeneous (public attractiveness score v_j and outside-option score q_j, both assumed known to the platform); customers are treated as ex-ante identical from the platform's perspective, reflecting settings — the authors give Airbnb as the running example — where the platform has rich information about supplier quality but little to no information about individual customer preferences. Sections 6 (simulation on randomly generated instances) and 7 (conclusion/open questions) were not read for this card, consistent with this paper's Related/Priority-3 depth allocation in this batch; no real-world dataset is used in the pages read.

## 2. Experiment Critique

Not covered in the pages read (Priority 3/Related depth allocation) — Section 6's simulation results were not extracted.

## 3. Industry Contribution

Not covered in the pages read (Priority 3/Related depth allocation).

## 4. Novelty vs. Prior Work

Not covered in the pages read beyond the related-work summary captured in the Reference Card and Project Relevance below (Priority 3/Related depth allocation).

## 5. Dataset Availability

| Dataset | Type | Public? | Notes |
|---|---|---|---|
| Randomly generated synthetic instances (Section 6) | Synthetic | N/A | Not detailed in the pages read for this card (Priority 3 depth; Section 6 not extracted) |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Assortment Planning for Two-Sided Sequential Matching Markets," Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur (Stanford University, Duke University, Facebook), arXiv, 2019 (arXiv:1907.04485; later Operations Research 70(6):2784–2803, 2022 per cross-reference), https://arxiv.org/abs/1907.04485 |
| 2 | Source type | Academic |
| 3 | Direction | D8 |
| 4 | Problem setting | A platform must choose, for each customer, a menu (assortment) of suppliers to show; customers choose at most one supplier from their menu via MNL, and each chosen supplier then chooses at most one of the customers who selected her; the platform's problem is to construct menu profiles maximizing the expected total number of matches, trading off larger menus (more customer choice) against more collisions (wasted customer attention on suppliers who can only accept one applicant) |
| 5 | Objective and label definition | No learned training objective or label — a combinatorial-optimization objective (expected number of matches under known MNL choice-model parameters). Supplier attractiveness scores v_j and outside-option scores q_j are assumed known primitives to the platform, not learned from data within this paper. Single static round (customer chooses, then supplier chooses, within one match cycle); no time horizon, no delay or censoring |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. Even "prediction" is not really at issue here: supplier scores v_j and outside-option values q_j are assumed known inputs to the platform, not estimated or predicted within this paper |
| 7 | Model architecture | Not a learned model — a combinatorial menu-construction algorithm. Two regime-specific constant-factor approximation algorithms (low-value suppliers: LP relaxation over a 2-D bucketing of suppliers by (attractiveness, outside-option) plus a rounding/menu-construction step; high-value suppliers: a combinatorial-optimization-based single-supplier-menu construction), combined in black-box fashion for the general case (Theorem 3.4, overall ratio ½·min{α_L, α_H}) |
| 8 | Credit assignment | Item-level (customer-supplier pair): a match is a mutual-choice event between one customer and one supplier, but choice probabilities are coupled across the whole menu (MNL denominator over all suppliers in a customer's menu) and across all customers who share a supplier in their respective menus (a supplier's reactive choice depends on the full set of customers who selected her). No user-level delayed outcome; single-round, pair-level credit only |
| 9 | Training data and counterfactual handling | No training data and no counterfactual estimation — supplier and outside-option scores are assumed known model inputs, not estimated from observational data within this paper |
| 10 | Offline and online evaluation | Offline theoretical (approximation-ratio proofs, NP-hardness reduction) plus offline synthetic simulation (Section 6, not detailed in the pages read for this card). No real-world data and no online evaluation reported |
| 11 | Reported gains | Not applicable in the pages read — no baseline-comparison numbers were extracted (Section 6 simulation results not read); the paper's headline "gain" is the existence of a polynomial-time algorithm with a proven constant-factor approximation ratio to the NP-hard optimum (Theorem 3.1), not an empirical percentage improvement |
| 12 | Applicability to a two-sided dating recommender | Provides the sharpest formal statement in the batch of the choice-vs-collision (congestion) trade-off in a two-sided market, but its lever is an unordered assortment/menu with no position effects, so it does not speak to how a ranking-only platform should order candidates — only to which candidates to include. No real-world validation; purely theoretical/simulated in the sections read |
| 13 | Unverified claims | No real-world validation is presented in the pages read (Section 6 offline simulation results and Section 7 conclusion were not read, per this paper's Related/Priority-3 depth allocation); the paper's practical relevance rests on Theorem 3.1's constant-factor approximation guarantee, whose actual numerical constant is not stated in the introduction/overview sections read and could in principle be loose in practice — a known general limitation of LP-relaxation/bucketing approximation algorithms, not something addressed in the pages read |

## Project Relevance

This paper speaks to **Q7** (congestion for a shared limited resource in a two-sided market) with the batch's most explicitly game-theoretic formalization of collisions — the precise mechanism by which showing "too many options" to too many customers wastes supplier attention rather than growing matches — and it is directly cross-referenced by both Paper 1 (Su, Bayoumi, and Joachims, WWW 2022, which cites it as related assortment-planning work sharing a simplifying exhaustive-evaluation assumption) and Paper 2 (Calsamiglia et al., 2023, which cites its Operations Research version as related theoretical work on the choice-vs-matching trade-off) elsewhere in this batch, confirming its position as a foundational reference for the congestion literature this survey is trying to cover. It does **not** address **Q1–Q6 or Q8**: there is no learned objective, no prediction task at all (scores are assumed known), no delayed or user-level outcome, no incrementality treatment, no offline/online evaluation on real data (in the pages read), and no migration path from an existing production system. Its central limitation for this project is structural rather than empirical: the platform's lever here is an unordered menu (which suppliers to include), not an ordered ranking (what order to show them in) — the project's actual and only lever — so while the paper's trade-off (more choice vs. more collision) is conceptually the same tension the project faces under congestion, its algorithmic machinery (bucketing suppliers, LP relaxation over menu *membership*) does not transfer directly to a ranking-only setting without first re-deriving an analogous trade-off for rank position rather than menu inclusion.

Horizon verdict: none — static one-shot (two-stage within a single match round: customer chooses, then supplier chooses; no repeated interaction over time, no retention or revenue horizon).
Lever verdict: the assortment/menu — which suppliers to include, not their order — is the platform's lever; the model has no within-menu position or ranking effect. A ranking-only platform can only approximate this by truncating its ranked list to a menu size, which is a coarser, less directly usable form of the paper's actual lever.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Itai Ashlagi, Anilesh K. Krishnaswamy, Rahul Makhijani, Daniela Saban, Kirankumar Shiragur
- **Affiliations:** Stanford University (Ashlagi, Saban, Shiragur); Duke University (Krishnaswamy); Facebook (Makhijani)
- **Venue:** arXiv preprint (arXiv:1907.04485v3, revised 2020-07-28); later Operations Research 70(6):2784–2803, 2022, per cross-reference in another paper's bibliography
- **Year:** 2019 (preprint); 2022 (journal, per cross-reference)
- **Relevance:** Related
- **Priority:** 3
- **nlm:6b37f1b1**
