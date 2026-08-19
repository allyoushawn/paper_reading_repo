# A Challenge-based Survey of E-recruitment Recommendation Systems

- **notebook source_id:** `801196e0`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
This is a survey of e-recruitment (job/candidate) recommendation research from 2012 onward, organized not by algorithm family (collaborative filtering vs. content-based vs. hybrid, as prior surveys did) but by eight practical **challenges** developers and researchers face: data quality, heterogeneous data/multiple interaction types, cold start, user preferences vs. suitability, interpretability/explainability, specific objectives (multi-stakeholder, one-worker-one-job), bias/fairness, and large scale. The authors crawled dblp with ten keywords, filtered to 99 academic papers (2012–2019, ≥5 citations) plus 24 industry/expert papers, for 123 papers total, and for each challenge catalog the proposed solution approaches in the literature (with figure-tree overviews) and flag open research directions. No new algorithm or empirical result is proposed — the contribution is the taxonomy itself plus a companion website cataloging the 123 papers.

## Method
Not a method paper. Methodology is a literature survey: dblp search across {'job recommender', 'job recommendation', 'job matching', 'e-recruitment', 'e-recruiting', 'online recruitment', 'person-job fit', 'vacancy recommendation', 'candidate recommendation', 'occupation recommendation'} → 515 papers → filtered to papers actually recommending jobs/job seekers (not job types), published 2012+, with ≥5 citations if pre-2019 → 99 papers, plus 24 hand-added industry papers → 123 papers, each tagged by recommendation type (job/job-seeker/reciprocal), method type, and which of the 8 challenges it addresses.

## Datasets and Baselines
Not applicable — this is a survey with no original experiments. It notes that public benchmark data for e-recruitment recommendation is scarce: only two fully public datasets exist (CareerBuilder 2012 dataset on Kaggle; Zhilian dataset from the Chinese platform Zhaopin), plus RecSys Challenge 2016/2017 data (from Xing) that is used in some studies but "not publicly available."

## Results
No empirical results (survey paper). The substantive output is: (1) identification of 8 challenges (data quality; heterogeneous data & multiple interaction types & external data sources; cold start; user preferences as well as suitability; interpretability and explainability; specific objectives; bias and fairness; large scale), each with a figure decomposing the sub-issues and citing the papers addressing each sub-issue (Figs. 1–8); (2) a structured table (Table 1, in the Appendix) tagging all 123 collected papers by recommendation type, method type, and challenges addressed; (3) a list of open/future research directions: the "one worker, one job" (OWOJ) balancing problem, career-path recommendation, domain adaptation, multi-linguality, conversational recommendation, support for specific job-seeker subgroups (e.g., adults with autism, the elderly), and fairness (flagged as understudied specifically for e-recruitment despite growing general RecSys attention).

## Limitations
Authors state explicitly: (1) the 8 challenges were "selected and elaborated ... from our point of view" — other challenges (e.g., feature extraction granularity) could exist and were not covered; (2) they deliberately omitted papers from other reciprocal-recommendation domains (e.g., online dating) "to limit the scope of this survey," despite noting those domains share the same two-sided mutual-choice structure; (3) they note the field suffers from a scarcity of public datasets (only two fully public datasets found), which they suggest limits benchmark comparability and slows progress.

## Heavily Cited Prior Works
- de Ruijt & Bhulai (2021), "Job recommender systems: A review" — prior survey this paper positions itself against (method-centric vs. this paper's challenge-centric framing)
- Gale & Shapley (1962), "College Admissions and the Stability of Marriage" — cited for stable matching as an OWOJ/specific-objectives solution
- Borisyuk, Zhang & Kenthapadi (2017), "LiJAR: A system for job application redistribution towards efficient career marketplace" — cited as a job-redistribution solution under the "specific objectives" (OWOJ) challenge
- Fu et al. — person-job fit model using hierarchical LSTM + Dynamic Multi-Key Value Memory Network for dynamic/multi-interaction-type preferences, cited repeatedly (heterogeneous data, dynamic preferences)
- Zhu et al. — explainability method visualizing high-frequency words per embedding dimension, cited under interpretability/explainability
- Boukari et al. (2020), "Huntalent" (LinkedIn-adjacent large-scale content-based recruitment system via Apache Spark) — cited under large scale
- Geyik et al. — fairness-aware re-ranking framework for job-seeker search results, cited under bias and fairness

## Bibliography Fields
- **title:** A challenge-based survey of e-recruitment recommendation systems
- **authors or organization:** Yoosof Mashayekhi, Nan Li, Bo Kang, Jefrey Lijffijt, Tijl De Bie — IDLAB, Department of Electronics and Information Systems (ELIS), Ghent University, Belgium
- **year:** 2022 (arXiv:2209.05112 first submitted Sept 2022; the read PDF is v2, dated 20 Oct 2023)
- **venue or type:** arXiv preprint (cs.IR); the manifest/filename attribute this to ACM Computing Surveys (CSUR) but no explicit journal banner, volume, or issue is visible on the pages read — venue not independently confirmed from the PDF itself.
- **link:** https://arxiv.org/pdf/2209.05112
- **tier tag:** Tier 3 academic method (survey/taxonomy, no new method or platform data)
- **what they did (≤80 words):** Surveyed 123 e-recruitment recommendation papers (2012–2023) organized around eight practical challenges (data quality, heterogeneity, cold start, preference/suitability, explainability, specific objectives incl. one-worker-one-job and reciprocal recommendation, bias/fairness, scale) rather than by algorithm family, cataloging proposed solutions per challenge with figure-tree overviews and flagging open research directions and dataset scarcity.
- **mechanism relevant to two-sided balancing (≤50 words):** Explicitly names "one worker, one job" (OWOJ) — job seekers/postings compete for scarce slots, so recommending success-unlikely matches wastes capacity — as a core challenge, and catalogs reciprocal recommenders, LiJAR-style job-application redistribution, and stable matching as its solution approaches.
- **metrics used, and the reported effect:** Not applicable — survey paper, no original experiments or metrics.
- **fit for a dating app:** medium — the OWOJ framing and pointers to LiJAR/stable-matching/reciprocal-recommendation solutions are structurally on-target for layers 1–2, but this is a map to primary literature rather than a mechanism paper itself, so it mainly earns its place as a citation index.
- **confidence that the item is real and described correctly:** high — read directly, taxonomy and challenge descriptions are explicit and unambiguous.

## Project Relevance
Serves mainly as a **map to primary sources** rather than a directly usable mechanism. Its "one worker, one job" (OWOJ) challenge is a direct structural analogue to the project's reply-capacity scarcity, and it explicitly names LiJAR (job application redistribution) and stable matching (Gale-Shapley) as OWOJ solutions — both of which are core candidate mechanisms for the project's **layer 2 (capacity-aware exposure allocation)**. Its "bias and fairness" and "specific objectives" (reciprocal recommenders, multi-stakeholder) sections touch **layer 1 (reciprocal scoring)** and **layer 4 (ecosystem metrics)** by pointing to the relevant sub-literatures, but this paper itself does not propose or validate a mechanism — treat it as an index/pointer document, not primary evidence.

## Reverse Citation Map
