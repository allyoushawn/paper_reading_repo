# Reciprocal Recommender Systems: Analysis of state-of-art literature, challenges and opportunities towards social recommendation

- **notebook source_id:** `53e7040e`
- **extraction method:** direct PDF read (NotebookLM unavailable)

## Summary
Survey of reciprocal recommender systems (RRS) — recommenders where the recommended "items" are people who must themselves accept the recommendation, requiring mutual (reciprocal) preference for success. Formalizes RRS against item-to-user and nonreciprocal user-to-user RS families, taxonomizes algorithm approaches (content-based, memory-based CF, model-based CF, hybrid, other) and fusion strategies for combining two unilateral preference scores into a reciprocal one (harmonic mean dominant; also arithmetic/geometric mean and the cross-ratio uninorm). Surveys RRS work across online dating (the dominant application), recruitment, online learning, social networks, and emerging domains (skill-sharing, shared economy, mentoring, academia), and analyzes five representative models (RECON, RCF, RWS, LFRR, CCR) in depth. Concludes with a five-perspective research agenda (fusion strategies, emerging applications, recommendation approaches, evaluation/reproducibility, fairness/explainability/ethics). No new empirical results of its own — this is a literature review, not an experimental paper.

## Method
Not a novel algorithm — a systematic survey plus conceptual formalization. Defines RRS formally (Def. 2.3): for two users x, y, a reciprocal recommender combines two unidirectional user-to-user recommenders R_U(x) and R_U(y); the reciprocal preference is p_{x↔y} = φ(p_{x,y}, p_{y,x}) for an aggregation function φ. The harmonic mean, p_{x↔y} = 2/(p_{x,y}^{-1}+p_{y,x}^{-1}), is identified as the dominant fusion choice in the literature because it is pulled toward the *minimum* of its two inputs — closer to the "both sides must be sufficiently interested" requirement — versus the more "optimistic" arithmetic/geometric means, which can reward one strongly one-sided score. Also covers the cross-ratio uninorm as a mixed optimistic/pessimistic/neutral alternative. Distinguishes single-class RRS (homogeneous pool, any user recommendable to any other — social media, same-gender dating) from two-class RRS (disjoint sets, e.g. heterosexual dating, recruiter/candidate).

## Datasets and Baselines
As a survey, it tabulates datasets/methods used across the reviewed literature rather than running its own experiment: RECON's Australian dating-site case study; LFRR's evaluation on Pairs (large Japanese dating site); CCR's evaluation on an online dating site against a random-neighbor baseline (~70% success rate vs baseline); the Speed Dating Experiment (Kaggle); Twitter Friends dataset; HarvardX MOOC person-course data. Notes the field's chronic shortage of public, reciprocity-labeled datasets, largely for privacy reasons.

## Results
No new quantitative results (this is a survey). It reports others' headline numbers as illustrations: a CF+HMM hybrid (CFHMM-HR) raised online-dating success rate from under 50% to 60–70% over its content-based-only predecessor; CCR achieved roughly double (~70%) the success rate of a random-neighbor baseline; LFRR matched RCF's precision/recall/F1 while running in real time on datasets where RCF became computationally intractable; RECON outperformed a nonreciprocal baseline and helped alleviate cold-start in its Australian case study; a probabilistic model (ProCF) reduced computational complexity versus its RCF ancestor and reduced popularity bias.

## Limitations
Authors' own stated gaps (Section 5): the field lags well behind classical item RS in maturity; cold-start/sparsity is worse than in item RS because user–user interaction data is sparser than user–item data; the literature relies almost entirely on offline evaluation, with very few live user studies; RRS success/failure metrics are non-standard and rarely account for asynchronous partial responses (the "Unknown" state, e.g. a request left unread); popularity bias is pervasive and only partially addressed; fairness, explainability, and ethical treatment of RRS are all flagged as under-studied; near-exclusive focus on heterosexual two-class dating and a handful of other domains leaves many plausible RRS domains (house-share, loneliness prevention, travel, group formation, politics/e-administration) unexplored; same-gender/single-class dating RRS is explicitly called out as understudied.

## Heavily Cited Prior Works
- Pizzato et al. 2010, "RECON: A reciprocal recommender for online dating" (RecSys) — foundational CB-RRS using harmonic-mean fusion.
- Pizzato et al. 2013, "Beyond friendship: the art, science and applications of recommending people to people" (RecSys) — earliest comprehensive RRS definition and case studies.
- Neve & Palomares 2019, "Latent factor models and aggregation operators for collaborative filtering in reciprocal recommender systems" (RecSys) — LFRR.
- Xia et al. 2015/2019 — online-dating RRS and WE-Rec (Walrasian-equilibrium fairness-aware RRS).
- Akehurst, Koprinska, Yacef, Pizzato, Rej — explicit-vs-implicit preference studies in online dating.
- Do, Corbett-Davies, Atif, Usunier 2021, "Two-sided fairness for rankings via Lorenz dominance" (NeurIPS) — the paper this survey's fairness discussion foreshadows.
- Kleinermann, Rosenfeld, Kraus 2018, "Optimally balancing receiver and recommended users' importance in reciprocal recommender systems" (RecSys).

## Bibliography Fields
- **title:** Reciprocal Recommender Systems: Analysis of state-of-art literature, challenges and opportunities towards social recommendation
- **authors or organization:** Iván Palomares, Carlos Porcel, Luiz Pizzato, Ido Guy, Enrique Herrera-Viedma
- **year:** 2021 (received Sep 2020, accepted Dec 2020, published online Dec 2020; journal issue Information Fusion 69 (2021) 103–127)
- **venue or type:** Information Fusion (Elsevier journal) — academic survey
- **link:** https://www.ujaen.es/grupos-de-investigacion/asia/sites/investigacion_asia/files/uploads/node_evento/revistas_indexadas/1-s2.0-S1566253520304267-mainext.pdf
- **tier tag:** Tier 3 academic method (survey)
- **what they did (≤80 words):** Surveyed and formally taxonomized the Reciprocal Recommender Systems (RRS) literature: characterized RRS against item-to-user and nonreciprocal user-to-user RS, catalogued algorithm families and preference-fusion strategies, tabulated RRS applications across dating, recruitment, online learning, social networks and emerging domains, analyzed five representative models in depth, and laid out a five-perspective research agenda for the field.
- **mechanism relevant to two-sided balancing (≤50 words):** Formalizes the reciprocal-scoring layer generically (aggregation function φ over two unilateral preference scores, harmonic mean dominant) and surveys popularity-bias-aware techniques (e.g. RWS's importance-weighting of low-popularity users) — useful as a map of the reciprocal-scoring design space, not itself a capacity-allocation mechanism.
- **metrics used, and the reported effect:** Survey reports others' metrics (precision/recall/F1, success rate, DCG-style measures); no unified metric of its own. Catalogs RRS-specific success/failure indicators (Actioned/Not-Actioned × Accepted/Rejected/Unknown Contact).
- **fit for a dating app:** high — reason: this is the field's most comprehensive map of reciprocal-scoring mechanisms, fusion functions, and dating-specific RRS models (RECON, LFRR, CCR, RWS all evaluated on real dating platforms), and its research agenda (fairness, popularity bias, explainability) directly names problems this project must solve, even though the survey proposes no capacity-allocation or ecosystem-metric mechanism itself.
- **confidence that the item is real and described correctly:** high — read directly from the PDF; all figures, citations, and formulas are internally consistent with the known Palomares et al. Information Fusion 2021 paper.

## Project Relevance
Directly addresses Layer 1 (reciprocal scoring) as its core subject: the harmonic-mean-vs-arithmetic/geometric-mean argument (Section 3.2) is exactly the "like-back probability" fusion question the project's Layer 1 needs, and RWS's importance-weighting of low-popularity users is an early, crude analogue of capacity-aware exposure allocation (Layer 2). However, the survey itself does **not** address hard capacity limits, exposure allocation under constraints, or ecosystem-level metrics (Gini, wasted likes, two-sided retention) — its own Section 5 explicitly calls fairness/popularity-bias/ecosystem-level RRS "still very scarcely investigated," confirming this is a gap the project must fill from other sources. Best used as a taxonomy/vocabulary reference and a citation index into the reciprocal-scoring literature, not as a source of a specific transferable mechanism.

## Reverse Citation Map

