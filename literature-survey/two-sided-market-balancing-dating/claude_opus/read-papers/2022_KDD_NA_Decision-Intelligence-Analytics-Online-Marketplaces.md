# Paper Analysis: KDD 2022 Workshop on Decision Intelligence and Analytics for Online Marketplaces: Jobs, Ridesharing, Retail, and Beyond

**Source:** Zhiwei (Tony) Qin (Lyft), Liangjie Hong (LinkedIn), Rui Song (NCSU/Amazon), Hongtu Zhu (UNC Chapel Hill), Mohammed Korayem (CareerBuilder), Haiyan Luo (Indeed), Michael I. Jordan (UC Berkeley). ACM SIGKDD 2022 workshop report, DOI 10.1145/3534678.3542895. NotebookLM source_id `8c7171c0-8609-4e5c-879b-b5e6473767b1`
**Date analyzed:** 2026-08-16

---

## 1. Summary

**Title:** KDD 2022 Workshop on Decision Intelligence and Analytics for Online Marketplaces: Jobs, Ridesharing, Retail, and Beyond
**Authors:** Zhiwei (Tony) Qin, Liangjie Hong, Rui Song, Hongtu Zhu, Mohammed Korayem, Haiyan Luo, Michael I. Jordan
**Abstract:** This is a published 3-page ACM workshop report (not a primary research paper) summarizing a dual-track KDD 2022 workshop that brought together 100+ academics and industry practitioners (Lyft, LinkedIn, Amazon, eBay, Indeed, DiDi Chuxing) to discuss data-driven decision-making across online marketplaces. It covers six keynote summaries and lists 10 accepted spotlight papers plus 5 poster abstracts.

**Key contributions (of the workshop as reported):**
- Keynote by Ido Bright (a16z/Stanford-affiliated): a "shadow-price" A/B testing estimator for matching platforms that corrects bias from SUTVA violations caused by marketplace interference, proven to be a correct first-order (fluid-limit) approximation and less biased than standard RCT metrics.
- Keynote by Susan Athey: GAN-fabricated profile experiments on the Kiva microlending marketplace showing photo-based fairness/exposure interventions can boost outcomes for the least-popular listings and reduce inequity without lowering total transaction volume.
- Keynote by Daniel Hewlett (LinkedIn): transfer-learning architecture unifying member/job embeddings across LinkedIn's hiring marketplace search and recommendation systems.
- 10 peer-reviewed spotlight papers spanning ridesharing fairness, sequential recommenders, causal forests, and job search ranking.

**Methodology:** N/A (a report synthesizing others' keynotes and accepted papers, not a unified method).

**Main results:** No unified quantitative results; individual keynote findings are summarized (see Bibliography Fields and Project Relevance below).

---

## 2. Experiment Critique

Not applicable — this is a workshop summary report, not a paper presenting its own experiments. The keynotes it summarizes (Bright's shadow-price estimator; Athey's GAN survey-experiment) each have their own rigor, but only secondhand descriptions are available from this source, not the underlying papers.

---

## 3. Industry Contribution

**Deployability:** The keynotes describe production-adjacent techniques (shadow-price A/B testing at unspecified marketplace companies; LinkedIn's deployed transfer-learning matching system) but this report itself is not a deployable artifact.

**Problems solved:** Cross-domain view of decision intelligence in marketplaces — experimentation under interference, visual/fairness-driven exposure bias, and job-matching transfer learning.

**Engineering cost:** Not specified in source.

---

## 4. Novelty vs. Prior Work

Not applicable in the usual sense — this is a synthesis report; novelty claims belong to the underlying keynote works, which are not separately available in this notebook.

---

## 5. Dataset Availability

**Datasets mentioned:**
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Kiva microlending logs + GAN-fabricated survey profiles (Athey keynote) | — | Not accessible (proprietary/survey) | Used to isolate photo-driven bias in lender choice |
| eBay global inventory, LinkedIn Talent Solutions graph, DiDi Chuxing fleet data, ZipRecruiter/Indeed ad logs | — | Not accessible (industry-internal) | Referenced across keynotes, no public release |

**Offline experiment reproducibility:** Not reproducible — all referenced datasets are proprietary industry telemetry.

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

**Authors:** Zhiwei (Tony) Qin, Liangjie Hong, Rui Song, Hongtu Zhu, Mohammed Korayem, Haiyan Luo, Michael I. Jordan
**Affiliations:** Lyft, LinkedIn, North Carolina State University/Amazon, UNC Chapel Hill, CareerBuilder, Indeed, UC Berkeley
**Venue:** ACM SIGKDD 2022 (workshop report, published in KDD '22 proceedings)
**Year:** 2022
**PDF:** Not fetched directly — analyzed via NotebookLM source
**Relevance:** Related — pointer to specific relevant mechanisms (shadow-price interference-aware testing; GAN-based exposure-fairness intervention) via keynote summaries, not a self-contained method
**Priority:** 2

---

## Bibliography Fields

- **title:** KDD 2022 Workshop on Decision Intelligence and Analytics for Online Marketplaces: Jobs, Ridesharing, Retail, and Beyond
- **authors or organization:** Zhiwei (Tony) Qin (Lyft), Liangjie Hong (LinkedIn), Rui Song (NCSU/Amazon), Hongtu Zhu (UNC), Mohammed Korayem (CareerBuilder), Haiyan Luo (Indeed), Michael I. Jordan (UC Berkeley)
- **year:** 2022
- **venue or type:** ACM SIGKDD 2022 workshop report (3-page ACM proceedings entry)
- **link:** https://doi.org/10.1145/3534678.3542895
- **tier tag:** Tier 1 — Adjacent marketplaces (job/ride/retail), report of a KDD workshop
- **what they did (≤80 words):** Summarized a dual-track KDD 2022 workshop with 100+ attendees from academia and industry (Lyft, LinkedIn, eBay, Indeed, DiDi). Reports six keynotes — most notably a shadow-price-based A/B testing correction for marketplace interference (Bright) and a GAN-driven photo-fairness exposure-redistribution experiment on the Kiva marketplace (Athey) — plus 10 accepted spotlight papers on ridesharing, recommendation, and causal inference in marketplaces.
- **mechanism relevant to two-sided balancing (≤50 words):** Two pointer-level mechanisms: (1) shadow-price A/B estimator correcting SUTVA-violation bias under matching-market interference; (2) counterfactual exposure-redistribution policy (image-based) that boosted under-exposed listings and cut marketplace inequity without lowering total transactions.
- **metrics used, and the reported effect:** No single quantitative headline for the report itself; per-keynote: Bright's shadow-price estimator proven less biased than standard RCT estimator (fluid-limit first-order approximation); Athey's counterfactual policy simulations "boost outcomes of the least popular campaigns and reduce overall inequity without sacrificing the number of transactions" (no numeric effect size given in source).
- **fit for a dating app:** medium — the shadow-price interference-aware A/B testing idea and the exposure-redistribution-without-volume-loss finding are both directly relevant to the project's Layer 4 (interference-aware experimentation) and Layer 2 (exposure redistribution), but this source only summarizes them secondhand; the underlying Bright and Athey papers would need to be sourced directly for implementable detail.
- **confidence that the item is real and described correctly:** high (NotebookLM grounded answer with extensive direct quotes and a real, verifiable ACM DOI; consistent across all three queries).

---

## Project Relevance

This workshop report is useful chiefly as a **pointer to two specific mechanisms worth chasing as primary sources**, rather than as a self-contained technical reference. (1) Ido Bright's shadow-price A/B testing keynote directly targets the project's Layer 4 need (interference-aware experimentation under feedback loops): instead of comparing raw treatment/control value, it compares each group's average shadow price in the matching linear program, which the source states is provably less biased than a standard RCT estimator under marketplace interference — exactly the failure mode the project would hit when testing exposure-allocation changes in a market where the same reply-capacity pool is shared across users. (2) Susan Athey's Kiva GAN-photo-fairness keynote is a directly analogous "photo-driven skewed desirability" study to the dating-app problem: it demonstrates, via counterfactual policy simulation, that redirecting exposure toward under-exposed/less-popular listings can reduce inequity without sacrificing total transaction volume — a proof-of-concept that exposure redistribution need not be a volume-destructive intervention, which is the central worry for any dating-market fairness re-ranker. Both mechanisms are summarized only at a high level here; the survey should independently source Bright's and Athey's underlying papers/working papers if deeper implementation detail is needed. The remainder of the workshop (rideshare fairness, LinkedIn transfer learning, ZipRecruiter ranking) is only generically adjacent.
