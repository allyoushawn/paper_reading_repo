# Queue — two-sided-market-balancing-dating

Shared across workplace runs. **Append only — read this file before writing, never recreate it.**

> **Merge note (claude_opus, 2026-08-16 21:5x).** This file was created by `claude_opus` at 21:21
> with 93 entries, then replaced wholesale at 21:31 by a `cursor-grok` run whose header states it
> was "created ... after notebook ingest already existed" — i.e. it did not read the existing file.
> Both runs' contents are merged below; nothing from either has been deleted. The `cursor-grok`
> snapshot taken before this merge is preserved.
> Each run also keeps a private authoritative copy (`claude_opus/queue-claude_opus.md`) because a
> shared file cannot be relied on under concurrent writers.

Format: Title | tier | direction (D1–D8) | nlm:<source_id or failure>

## To Process (claude_opus run)



### Tier 1 — Dating-platform primary sources

- Powering Tinder® — The Method Behind Our Matching (Tinder company newsroom, 2019) | tier:1 | direction:D1 | nlm:9bdcac0f-65a3-44e8-aaa2-24f0c1bcb3a4
- Personalized (User) Recommendations at Tinder: The TinVec Approach (Steve Liu, MLconf SF 2017) | tier:1 | direction:D1 | nlm:2ff277b6-5d4a-4a88-bb0d-abf7c2e12c03
- Hinge employs new algorithm to find your 'most compatible' match (TechCrunch 2018, re: Hinge's Gale-Shapley-based "Most Compatible") | tier:1 | direction:D1,D5 | nlm:8c15aeab-44c5-42cb-9db5-5f3a11792991
- OkTrends, "Your Looks and Your Inbox" (OkCupid, 2009, mirror) | tier:1 | direction:D6 | nlm:7254c174-e1fa-44e9-9026-b1cab56a1e9b
- "Data Science of Love" (Vaclav Petricek, eHarmony, Strata + QCon 2013) | tier:1 | direction:D1 | nlm:16e0e255-7244-493f-a3fe-2bb5c8f4ba13
- Powering recommendation models using Amazon ElastiCache for Redis at Coffee Meets Bagel | tier:1 | direction:D1 | nlm:934ebdb0-fe31-4828-b42e-9a2bceb2e104
- Tinder's migration to Elasticsearch 8 (Tinder tech blog, 2025) | tier:1 | direction:D1 | nlm:ef5834f7-2122-4ddd-93cb-914c2b4d5edf
- What AI Principles Teach Us About Finding Love (OkCupid tech blog, 2025) | tier:1 | direction:D1,D6 | nlm:0873a0e7-21ef-4ae0-985a-b00cd3a5f676
- Automated Decision Making at Grindr (Grindr blog, 2023 — states distance-sorted filtering, NOT a rec algorithm; useful negative contrast) | tier:1 | direction:D1 | nlm:c60a97fd-d38e-4c59-a1f3-3cf84e8abaf1
- Introducing Smart Photos — For The Most Swipeworthy You | tier:1 | direction:D1 | nlm:7ee84a11-660e-4b2b-bbf1-571830ea4937
- How on-device AI models find your best Tinder profile photo | tier:1 | direction:D1 | nlm:5ce3021f-6ce9-4580-9128-8a4cfabb80c2

### Tier 1 — Adjacent marketplaces (job / ride / home / creator)

- LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace (Borisyuk, Zhang, Kenthapadi, LinkedIn, KDD 2017) | tier:1 | direction:D3,D4 | nlm:11b0d239-3d33-4e8a-a366-5c87b64a3d42
- Modeling Impression Discounting in Large-scale Recommender Systems (Lee, Lakshmanan, Tiwari, Shah, LinkedIn, KDD 2014) | tier:1 | direction:D3 | nlm:41ae2a64-26bd-4645-bdd2-75487b254338
- Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems (Mehrotra, McInerney, Bouchard, Lalmas, Diaz, Spotify, CIKM 2018) [file] | tier:1 | direction:D2,D4 | nlm:069d754f-0604-4a8c-abc4-0407ceba2423
- Recommendations in a Marketplace (Mehrotra & Carterette, Spotify Research, RecSys 2019 tutorial) | tier:1 | direction:D2 | nlm:4ea2fce9-31fa-4249-bd4f-a2cb6b5dbce8
- Real-time Personalization using Embeddings for Search Ranking at Airbnb (Grbovic & Cheng, KDD 2018) [file] | tier:1 | direction:D5 | nlm:aad314c0-211d-46c7-b208-cf3fc48928ba
- Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets (CyberAgent, RecSys 2023) | tier:1 | direction:D1 | nlm:711cc5a5-fa03-4b06-b668-247bd8c34f21
- Fair Reciprocal Recommendation in Matching Markets (CyberAgent + U Tokyo, RecSys 2024) | tier:1 | direction:D1,D2 | nlm:ad4c549e-01e1-403d-aea1-e152f66747a4
- Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method (Chen Yang et al., KDD 2024) | tier:1 | direction:D1 | nlm:c48aa0c3-be96-4d7e-9d69-f80a146256cc
- Modeling Two-Way Selection Preference for Person-Job Fit (Yang, Hou, Song, Zhang, Wen, Zhao; BOSS Zhipin + Renmin U, RecSys 2022) | tier:1 | direction:D1 | nlm:36a35563-0075-4a98-8155-3636a7a99757
- Reciprocal Sequential Recommendation (Zheng et al., RecSys 2023) | tier:1 | direction:D1 | nlm:62c16054-74a2-4417-8c06-feaf957ca164
- BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment (BOSS Zhipin + USTC, KDD 2023; authors incl. Xiao Hu, Yuan Cheng, Zhi Zheng, Yue Wang, Xinxin Chi, Hengshu Zhu) | tier:1 | direction:D1 | nlm:28429a27-6687-4a62-bb67-8d48ed79dc70
- A closer look at how LinkedIn integrates fairness into its AI products | tier:1 | direction:D2 | nlm:406bf239-83ed-4d9c-851f-bbefc3144492
- Building Representative Talent Search at LinkedIn | tier:1 | direction:D2 | nlm:a029e228-8668-426e-84fe-249d0fa9d407
- Building a Large-Scale Recommendation System: People You May Know | tier:1 | direction:D1 | nlm:72b12e20-b22c-44df-8084-499d857af2dc
- Joint Multisided Exposure Fairness for Recommendation (Microsoft) | tier:1 | direction:D2 | nlm:eeb5deb6-cf7d-4b0b-a452-2f18e4e060d1
- Engineering the Right Opportunities for Thumbtack Pros | tier:1 | direction:D3,D4 | nlm:1bdd8568-9257-42f0-9305-512d3a4560f5
- Building a Transformer-Based Category Recommender at Thumbtack | tier:1 | direction:D1 | nlm:b1a14644-792a-4f6a-b8e8-d0db6e825fc6
- SED468 — Thumbtack Marketplace Evolution (Software Engineering Daily podcast) | tier:1 | direction:D2 | nlm:dc89f2b8-f718-42a0-8180-c50eeea57d25
- Personalizing Airbnb Search by Learning from the Guest | tier:1 | direction:D5 | nlm:ec6d0d08-99e6-40c4-8ff4-5a548e7796c5
- Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example | tier:1 | direction:D2 | nlm:254165eb-d1bc-4762-bde2-c94b7ae4a468
- A Better Match for Drivers and Riders: Reinforcement Learning at Lyft | tier:1 | direction:D5 | nlm:b0bf71c0-91b5-4806-aa47-ae062de27e76
- CyberAgent JP blog: reciprocal rec system matching theory (Japanese) | tier:1 | direction:D1,D8 | nlm:3b880c82-a704-47b6-8166-51c0791c11df
- CyberAgent JP blog: matching app encounters analysis (Japanese) | tier:1 | direction:D8 | nlm:ed9a750d-10ab-4384-a4ef-6241dceadde0
- Choosing an algorithmic fairness metric for an online marketplace (YinYin Yu, practitioner piece, arXiv) | tier:1 | direction:D2 | nlm:3c046693-7a3e-41c4-a3bc-b45bcfd66487
- Marketplace Analytics: Balancing Supply, Demand, and Liquidity Metrics | tier:1 | direction:D2 | nlm:b3f30d97-a9ba-4226-a79a-44ee4192910a
- 3 Powerful Features of ZipRecruiter's Search | tier:1 | direction:D1 | nlm:bd467e2e-7916-4df1-8cfe-ed50b6d7188e
- "Beyond A/B Testing": using surrogacy and region splits for marketplace experimentation (industry blog, exact company unattributed in title) | tier:1 | direction:D7 | nlm:4cb86d35-a0bb-4736-b96f-c761660910a7
- Towards a Fair Marketplace… (Spotify Research listing page — same underlying paper as the Mehrotra CIKM 2018 file above; secondary/redundant source) | tier:1 | direction:D2 | nlm:bf792841-3d1c-4d77-881b-acea7346127d
- RecSys 2025 — Accepted Contributions (conference program index, not a paper) | tier:1 | direction:D1 | nlm:bf49347b-e728-459a-8b9f-85ee20db9f6c
- TSMO 2025 — Two-Sided Marketplace Optimization workshop (Google Sites index, not a paper) | tier:1 | direction:D2 | nlm:5676baa4-9255-40ab-aa6f-f92806721dcc
- KDD 2022 Workshop on Decision Intelligence and Analytics for Online Marketplaces (SIGKDD index, not a paper) | tier:1 | direction:D2 | nlm:8c7171c0-8609-4e5c-879b-b5e6473767b1

### Tier 2 — Applied research / field experiments on real matching or dating platforms

- Assortment Planning for Two-Sided Sequential Matching Markets (Ashlagi, Krishnaswamy, Makhijani, Saban, Shiragur, Operations Research 2022) | tier:2 | direction:D5 | nlm:8608cddc-7ce5-4442-a73b-4f882753f031
- Facilitating the Search for Partners on Matching Platforms (Kanoria & Saban, Management Science 2021) | tier:2 | direction:D5 | nlm:8166a680-4ba6-4ab6-ab2b-abde364efb23
- Managing Congestion in Matching Markets (Arnosti, Johari, Kanoria, M&SOM 2021) | tier:2 | direction:D3 | nlm:be32771a-cc6b-45b2-a988-f65302a37b9d
- Competing by Restricting Choice: The Case of Matching Platforms (Halaburda, Piskorski, Yıldırım, Management Science 2018) | tier:2 | direction:D5 | nlm:b3251909-7bd7-40b8-ba1e-664702bc8203
- Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating (Jessica Fong, Marketing Science 2024; preprint titled "Search, Selectivity, and Market Thickness…" was the text ingested) | tier:2 | direction:D5,D6 | nlm:c02339ea-e8c6-4cd3-864c-a4b1ecf133df
- Propose with a Rose? Signaling in Internet Dating Markets (Lee & Niederle, Experimental Economics 2015 — field experiment, Korean dating site) | tier:2 | direction:D5 | nlm:180f76b2-5656-4253-bf5a-175014e2052a
- Matching and Sorting in Online Dating (Hitsch, Hortaçsu, Ariely, American Economic Review 2010) | tier:2 | direction:D6 | nlm:b22c1eb9-5c82-469e-8c26-bc2c84f62c1b
- Aspirational Pursuit of Mates in Online Dating Markets (Bruch & Newman, Science Advances 2018 — desirability via PageRank) | tier:2 | direction:D6 | nlm:6fd7c401-d934-4316-b13d-0fc1fbc39b2c
- Reciprocal Recommendation System for Online Dating (Xia, Liu, Sun, Chen, ASONAM 2015) | tier:2 | direction:D1 | nlm:f3e7044f-0935-451f-840f-1b0baaa35cd4
- Online Dating Recommendations: Matching Markets and Learning Preferences (Tu et al., WWW 2014 Companion) | tier:2 | direction:D1 | nlm:fa4b77b4-a8ff-46e1-bcd6-087b7e38c344
- "Platform Design in Curated Dating Markets" (authors blinded for peer review, submitted to Manufacturing & Service Operations Management; selects profile subsets shown per user per period; proves the integral Dating Heuristic achieves 1−1/e approximation across platform designs and 1/4e with non-sequential matches in a large market; uses real data from an undisclosed dating app under NDA; cites Rios et al. 2023 for the Dating Heuristic) | tier:2 | direction:D4,D5 | nlm:c17bdd53-6317-429b-83df-72b3bc0cec43
- Experimental Design in Two-Sided Platforms: An Analysis of Bias (Johari, Li, Liskovich, Weintraub, Management Science 2022) | tier:2 | direction:D7 | nlm:c2aa9d85-74ed-4a98-8c41-55a7c5642d1b
- Multiple Randomization Designs (Bajari et al., arXiv 2021) | tier:2 | direction:D7 | nlm:ecffd79a-f987-4db0-9423-29db4fc71baf
- Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-experiment on Airbnb (Holtz, F. Lobel, R. Lobel, Liskovich, Aral, Management Science 2025 — 5 authors, corrected from brief's 4) | tier:2 | direction:D7 | nlm:6a17afaa-1e78-46c9-8dde-9a35c52b1b82
- Designing Recommendation Exposure and Favorite Lists: A Field Experiment on a Spot-Work Platform (arXiv) | tier:2 | direction:D4 | nlm:733a9204-805a-4e36-9be7-120f1a3531dd
- Mr. Right or Mr. Best: The Role of Information Under Preference Mismatch in Online Dating | tier:2 | direction:D5,D6 | nlm:c5479a0f-7b8c-40be-a830-212326305de6
- It takes two to tango: a directed two-mode network approach to desirability on a mobile dating app (PMC) | tier:2 | direction:D6 | nlm:09c242a3-9dbf-4ff9-bd55-9c33515a981a

### Tier 3 — Academic methods mapping to a lever, or surveys

- Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation (Palomares, Porcel, Pizzato, Guy, Herrera-Viedma, Information Fusion 2021 — most recent reciprocal-recsys survey found; the arXiv preprint 2007.16120 was withdrawn by the authors in Jan 2021 over an author dispute — do NOT cite that copy; this entry uses the published-version copy) | tier:3 | direction:D1 | nlm:53e7040e-1e6a-46e1-8576-6113e3748507
- Two-sided Fairness in Rankings via Lorenz Dominance (Do, Corbett-Davies, Atif, Usunier, Meta, NeurIPS 2021 — covers the reciprocal case) | tier:3 | direction:D2 | nlm:6d5ea1eb-d81c-4350-98e9-a942e67aecfc
- Fairness of Exposure in Rankings (Singh & Joachims, KDD 2018) | tier:3 | direction:D2 | nlm:51ed95ae-2945-409c-bb05-5761a57d9357
- Recommendation with Capacity Constraints (Christakopoulou, Kawale, Banerjee, CIKM 2017) | tier:3 | direction:D3 | nlm:433bf032-d30d-4b31-98f0-1a7006022991
- Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating (Pizzato, Rej, Akehurst, Koprinska, Yacef, Kay, User Modeling and User-Adapted Interaction 23(5), 2013, DOI 10.1007/s11257-012-9125-0 — brief had no URL, resolved during discovery) | tier:3 | direction:D1 | nlm:fc3355e4-578d-4934-b9c5-949934c7d6d3
- A Challenge-based Survey of E-recruitment Recommendation Systems (Mashayekhi, Li, Kang, Lijffijt, De Bie, ACM Computing Surveys 2022 — blind-spot-#2 find; e-recruitment specific, not general reciprocal recsys, but same two-sided mutual-choice structure) | tier:3 | direction:D1 | nlm:801196e0-1114-4d23-a4f5-e23d6f622f06
- Balanced Neighborhoods for Multi-sided Fairness in Recommendation (PMLR) | tier:3 | direction:D2 | nlm:1dccf951-fbf2-453e-845b-277d30f7c9f9
- Balancing Fairness and High Match Rates in Reciprocal Recommender Systems: A Nash Social Welfare Approach (arXiv) | tier:3 | direction:D1,D2 | nlm:6a44f3f3-e515-418d-abe7-3734c067e731
- MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets (arXiv) | tier:3 | direction:D1 | nlm:706fe50d-ca71-4ce7-b13c-2b09dbdcc978
- A Best-of-Both Approach to Improve Match Predictions and Reciprocal Recommendations for Job Search (arXiv 2409.10992) | tier:3 | direction:D1 | nlm:e44c714b-90b3-4200-b04f-b080de14abd1
- Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching (arXiv) | tier:3 | direction:D6 | nlm:ac33368a-b91f-4d5d-bb04-416786e45ee0
- Parallel and Mini-Batch Stable Matching for Large-Scale Reciprocal Recommender Systems (arXiv) | tier:3 | direction:D1,D5 | nlm:e340a22d-a272-41eb-8ac6-c9c6eca9b599
- Counterfactual Reciprocal Recommender Systems for User-to-User Matching (arXiv) | tier:3 | direction:D1 | nlm:665bad41-0c99-4bf2-a309-0402df4ca828
- Explainable Reciprocal Recommender System for Affiliate-Seller Matching (MDPI) | tier:3 | direction:D1 | nlm:1c575967-a9b1-455b-b600-55b4e8c63b9a
- Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach (arXiv) | tier:3 | direction:D1 | nlm:dc9b9201-8782-4615-8aaa-61a69421d536
- Designing labor market recommender systems (Semantic Scholar) | tier:3 | direction:D1 | nlm:6f04017d-4dbc-4a84-8c27-9535ec633f58
- Fairness in Job Recommendation under Quantity Constraints (The PIKE Group) | tier:3 | direction:D3 | nlm:8c1b6d85-d596-43e5-b100-59d35db770a2
- Salience and Market-aware Skill Extraction for Job Targeting (arXiv) | tier:3 | direction:D1 | nlm:49771075-24a9-454e-b43e-dc50a8a0dc8a
- Creator-Side Recommender System: Challenges, Designs, and Applications (arXiv) | tier:3 | direction:D2 | nlm:e2743fe8-7433-4eac-87f4-6f54d2c8e1b9
- User Fairness, Item Fairness, and Diversity for Rankings in Two-Sided Markets (NSF PAR) | tier:3 | direction:D2 | nlm:722d4cc7-0e2f-491b-9202-f06fe18ce014
- Using Bayesian optimization for balancing metrics in recommendation systems | tier:3 | direction:D2 | nlm:4ade17eb-c333-43ff-8244-79b8a3bcbe91
- Using Recommendations To Balance Demand and Supply in Two-Sided Marketplaces (OpenReview) | tier:3 | direction:D2 | nlm:a979c5f5-1b56-4ab1-a30b-3f03a06a2d31
- Reinforcement Learning for Modeling Marketplace Balance | tier:3 | direction:D2 | nlm:3b294ea0-7a61-494a-ab51-b6aff71c3e48
- Congestion and Information Design in Matching Markets (DII UChile working paper) | tier:3 | direction:D3 | nlm:4c32184b-55e9-40eb-a974-bfa62b146c1e
- Managing Congestion in a Matching Market via Demand Information Disclosure | tier:3 | direction:D3 | nlm:a58bf722-6ff1-450c-815e-0fd370d50c89
- Matching Market Design with Constraints | tier:3 | direction:D5 | nlm:8c073ae4-0c30-498e-86a1-5144bbccd4d8
- Prediction and Congestion in Two-Sided Markets: Economist versus Machine Matchmakers (UCR) | tier:3 | direction:D3 | nlm:1c0f9a09-5e17-4a74-ba49-ad3db5c05989
- A Pigouvian Approach to Congestion in Matching Markets (IZA@LISER Network) | tier:3 | direction:D3 | nlm:f066725b-f69b-4d77-84b4-595cbda7c9b5
- Policy Design for Two-sided Platforms with Participation Dynamics (GitHub/arXiv) | tier:3 | direction:D3 | nlm:e0ef0297-acaa-4d43-80e5-1f8fdb9da14e
- Strategic Behavior in Two-sided Matching Markets with Recommendation-enhanced Preference-formation (NeurIPS/NIPS) | tier:3 | direction:D5 | nlm:fa328baa-5106-4403-933d-d7f9de52c61a
- Interview choice reveals your preference on the market (KAUST Repository) | tier:3 | direction:D5 | nlm:7769d47d-4384-40f0-a420-f908267d6771
- Two-Sided Time-Independent Regret for Matching Markets with Limited Interviews (arXiv) | tier:3 | direction:D5 | nlm:1d391169-5c4c-4583-b61e-6451aa0199f2

### Tier 1 — Adjacent marketplaces

- Managing Diversity in Airbnb Search (Airbnb, KDD 2020) | tier:1 | direction:D2,D4 | nlm:f5e1509e-1c05-4bf8-8cd7-433bb407233c
- Powering Job Search at Scale (LinkedIn, 2025) | tier:1 | direction:D2 | nlm:a4d449b9-deb0-4e06-9ac3-9c4d84b8296d
- DPGNN / 面向人岗匹配的双向选择偏好建模 (BOSS Zhipin, RecSys 2022, Chinese write-up) | tier:1 | direction:D1,D8 | nlm:45b3083a-b955-44d3-bb25-8bf8a6c6220b
- 快手因果推断与实验设计 / Kuaishou Causal Inference and Experimental Design (2021) | tier:1 | direction:D7,D8 | nlm:f21c8433-e1f1-41f6-b5ef-ad5a2075a2d4
- マーケットプレイス型プロダクトが直面する3つの課題 / CrowdWorks marketplace challenges (Qiita, 2018) | tier:1 | direction:D2,D3,D8 | nlm:d8e8fa9c-5528-496b-9b62-fc8a81643fde
- Off-Policy Evaluation and Learning for Matching Markets (Hayashi, Goda, Saito, RecSys 2025) [added by cursor-grok] | tier:1 | direction:D7 | nlm:7e39447e-3e79-44be-a507-70275b62a7c0

### Tier 1 — Dating-platform primary sources

- Matching Theory-based Recommender Systems in Online Dating [added by cursor-grok] | tier:1 | direction:D1,D5 | nlm:9c7ac344-4e9f-48a8-ac9e-88f800877266

## Done (cursor-grok run)

- [cursor-grok/read-papers/2023_RecSys_TU-matching_Fast-Examination-agnostic-Reciprocal.md] | Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets | 2026-08-16 | nlm:711cc5a5-fa03-4b06-b668-247bd8c34f21
- [cursor-grok/read-papers/2017_KDD_LiJAR_Job-Application-Redistribution.md] | LiJAR | 2026-08-16 | nlm:11b0d239-3d33-4e8a-a366-5c87b64a3d42
- [cursor-grok/read-papers/2023_MSOM_NA_Improving-Match-Rates-Dating-Assortment.md] | Rios Saban Zheng M&SOM | 2026-08-16 | nlm:c17bdd53-6317-429b-83df-72b3bc0cec43
- [cursor-grok/read-papers/2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md] | Fair Reciprocal Recommendation in Matching Markets | 2026-08-16 | nlm:ad4c549e-01e1-403d-aea1-e152f66747a4
- [cursor-grok/read-papers/2022_RecSys_MTRS_Matching-Theory-Online-Dating.md] | Matching Theory-based Recommender Systems in Online Dating | 2026-08-16 | nlm:9c7ac344-4e9f-48a8-ac9e-88f800877266
- [cursor-grok/read-papers/2024_MktSci_NA_Market-Size-Competition-Online-Dating.md] | Fong Marketing Science 2024 | 2026-08-16 | nlm:c02339ea-e8c6-4cd3-864c-a4b1ecf133df
- [cursor-grok/read-papers/2025_RecSys_DiPS_OPE-Matching-Markets.md] | Off-Policy Evaluation and Learning for Matching Markets | 2026-08-16 | nlm:7e39447e-3e79-44be-a507-70275b62a7c0
- [cursor-grok/read-papers/2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems.md] | Revisiting Reciprocal Recommender Systems | 2026-08-16 | nlm:c48aa0c3-be96-4d7e-9d69-f80a146256cc
- [cursor-grok/read-papers/2021_MSOM_NA_Managing-Congestion-Matching-Markets.md] | Arnosti Johari Kanoria congestion | 2026-08-16 | nlm:be32771a-cc6b-45b2-a988-f65302a37b9d
- [cursor-grok/read-papers/2025_LyftEng_MMV_Marketplace-Marginal-Values-Interference.md] | Lyft MMV interference | 2026-08-16 | nlm:9fe83587-cd97-4016-9ada-368a68677ee9

Remaining bibliography items (not given individual read-papers) are listed as Done-lite in `cursor-grok/literature-review.md`.

## Skipped (cursor-grok run)

- RECON RecSys 2010 | nlm:failed:paywall — checked arxiv, SSRN, Semantic Scholar, author homepage; no free PDF. Use Pizzato UMUAI 2013.
- Neve & Palomares RecSys 2019 | nlm:failed:paywall — same search order.
- Bumble Tech ranking post | not found (null).
- RecSys 2026 industry track papers | not posted as of 2026-08-16.
- FAIR-MATCH arXiv 2507.01063 | source_add resolved to arXiv homepage.
- arXiv 2201.11331 | mistaken ID added during seed fill; treat as Peripheral unless title confirms matching-theory talk (correct talk is 2208.11384).
- KISSmetrics marketplace analytics | low-quality content marketing.
- Deep-research hit index 0 (NLM generated report) | not a primary source.

## Added 2026-08-17 (cursor-grok continuation) — append only

- Tinder’s migration to Elasticsearch 8 (Sokolov, Hickey, Du, 2025) | tier:1 | direction:D1,D6 | nlm:ef5834f7-2122-4ddd-93cb-914c2b4d5edf
- Large-scale collaborative filtering… with JAX (Jablons, OkCupid Tech Blog, 2021) | tier:1 | direction:D1 | nlm:199f4755-e45b-4d9b-b46c-03c7e011160e
- A Reciprocal Embedding Framework For Modelling Mutual Preferences (Ramanathan et al., AAAI 2021) | tier:1 | direction:D1,D7 | nlm:3da6ec16-bd07-4d28-b23f-e2ccd529327f
- CUPID (Kim et al., arXiv:2410.18087) | tier:1 | direction:D1 | nlm:fa442dc5-e8d7-43ec-b21c-b4f62618f3cd
- GraphMatch (Sacha et al., arXiv:2512.02849) | tier:1 | direction:D2 | nlm:d3bfc710-f2b9-45fd-b8f2-036f98bb3b9b
- LinkSAGE (Liu et al., KDD 2025) | tier:1 | direction:D2 | nlm:3158c20b-fab3-4729-8cd2-849399fe05a0
- Fairness-Aware Ranking… LinkedIn Talent Search (Geyik, Ambler, Kenthapadi, KDD 2019) | tier:1 | direction:D4 | nlm:e893e729-1271-481f-8c74-f94d74c0bf88
- Introducing Smart Photos (Tinder Newsroom, 2016) | tier:1 | direction:D3 | nlm:7ee84a11-660e-4b2b-bbf1-571830ea4937
- The Dating Heuristic (arXiv:2308.02584) | tier:2 | direction:D4,D5 | nlm:2c123934-0fa8-42e1-b0f1-6af4fc0ead28
- Ethical Considerations of AI for Online Dating (Neve, Pairs Engineering, 2023) | tier:1 | direction:D5 | nlm:271f0f1e-a0b9-4b3e-8f71-e592c33c74c0
- 基于双向匹配的陌生人社交… (Maimai essay) | tier:1 | direction:D5,D8 | nlm:a5a378d7-cf61-4c3d-a300-8a9791cfafbd
- A challenge-based survey of e-recruitment recommendation systems (Mashayekhi et al., CSUR 2024) | tier:3 | direction:D1 | nlm:801196e0-1114-4d23-a4f5-e23d6f622f06
- Reciprocal Recommender Systems (Neve, SpringerBriefs 2025) | tier:3 | direction:D1 | nlm:failed:paywall
- Predicting Potential Customer Support Needs… (Airbnb Eng PDF, imported 7ddbec32) | tier:1 | direction:D2 | nlm:827d0f31-c9f1-4639-a342-cfe8f4f696de
- マッチングアプリにおける推薦システム (CyberAgent Speaker Deck, imported 7ddbec32) | tier:1 | direction:D8 | nlm:0b59c0ed-a1c3-44ee-bac8-2dd4cbc23f99

## Skipped (cursor-grok 2026-08-17)

- GetMatches.ai / VIDA Select / DEV.to Bumble “algorithm” posts | SEO, not primary
- ByteByteGo Tinder geosharding recap | third-party
- BOSS Scribd mirror | already have ACM PDF
- InfoQ 陌陌模型化召回 | nearby-feed recall, not dating matching
- Neve SpringerBriefs 2025 PDF | paywall, no free copy
- student.cs LinkedIn KDD 2019 PDF | source_add failed; used arXiv 1905.01989
- Paper-keyword 61-hit research_import from 2026-08-16 | task not recoverable

## Added (cursor-grok 2026-08-17 gap-fill)

- How We Connect Daters (Hinge, 2025) | tier:1 | direction:D1,D5 | nlm:b2ee80ca-cd26-4339-883d-a8ec39570aba
- Evolving Together: How Daters Helped Shape Hinge in 2025 | tier:1 | direction:D1 | nlm:76a4eccc-7629-4f04-93a0-62a4dcece95a
- Graph Fusion in Reciprocal Recommender Systems (Zhang, Wang, Yamasaki, IEEE Access 2023) | tier:2 | direction:D1 | nlm:2383281d-7e6b-4cc0-9856-0c476d92e23c (text extract); nlm:d9e1502a-516d-434f-962f-df59bab7168a (IEEE wall, empty)
- A/B Testing for Recommender Systems in a Two-sided Marketplace (UniCoRn, Nandy et al., NeurIPS 2021) | tier:1 | direction:D7 | nlm:93144d1a-4049-4be7-a854-3e5e7ff5b79d
- Kanzhun IR / CMBI: fairer traffic to more responsive users | tier:1 | direction:D2,D3 | nlm:ad032946-c920-471a-8f79-4f1120ea2ec1 (HKEX); nlm:94e5fef2-b528-499c-a2d2-08f4feb460aa (CMBI); nlm:503e6bd0-4a92-4a5a-907a-cc7c2398f850 (IR)
- Mapping Stakeholder Needs to Multi-Sided Fairness… (Kaya & Bogers, RecSys 2025, Jobindex) | tier:1 | direction:D2 | nlm:bf49347b-e728-459a-8b9f-85ee20db9f6c (program page)

## Skipped (cursor-grok 2026-08-17 gap-fill)

- Bumble Tech ranking post | still null (`site:tech.bumble.com ranking` empty); HLD Handbook / DEV.to not primary
- RecSys 2025 LCM4Rec (Krause & Oosterhuis) | T3 choice model, not matching
- Paper-keyword research_start re-run | NLM MCP Not connected

## Skipped / blocked (cursor-grok 2026-08-17 nlm-cli)

- OpenReview UniCoRn PDF | ingested as Cloudflare wall `nlm:bc2811a7` (arxiv PDF already in notebook)
- IEEE Xplore GFRR DOI | ingested as empty wall `nlm:d9e1502a` (text extract used instead)
- Deep research task `ChBjM2UxZDliYmYxN2JiODI4EAgaBDAxZDIqA3Vzdw` | started via `nlm research start --force --mode deep`; CLI poll/import 400 on RPC `e3bVqc` — not imported. Import from the NotebookLM UI if the task completed.
- 探探 / 陌陌 / Soul ranking engineering posts | still none
- Dating-log OPE | still none (Hayashi eval is Wantedly)

## Added 2026-08-18 (codex-sol Phase 2)

- 相互推薦における嗜好の集約をパーソナライズする試み (Wantedly Engineer Blog, 2026) | tier:1 | direction:D1,D8 | nlm:8f872a8a-ca7f-4c9d-ada5-bb124b6b75d7
- Reducing Marketplace Interference Bias Via Shadow Prices (arXiv, 2022) | tier:2 | direction:D7 | nlm:14292df1-f11b-4d0b-b404-db226ca1e99e
