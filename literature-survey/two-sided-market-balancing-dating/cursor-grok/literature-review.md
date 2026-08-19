# Two-sided market balancing for dating-app recommendation — Literature Review

**Run:** cursor-grok, 2026-08-16 first pass + 2026-08-17 continuation + **2026-08-17 gap-fill**. **North star:** `../README.md` Project Context. **Rules:** industry-first (Tier 1+2 ≥60%); 60–100 items, mix wins over count; CyberAgent RecSys 2023/2024 shared with Survey 3.

**Coverage (this workplace's bibliography: 72 annotated items).** Direction 1: strong (Tinder ES8, OkCupid JAX, Tapple AAAI 2021, Hinge 2025 mutual-compat DL, GFRR send/reply GNN, Xia/Baihe). Direction 2: Kanzhun IR “fairer traffic” + Jobindex RecSys 2025 fairness interviews. Direction 3–5: unchanged-strong. Direction 7: UniCoRn producer-side A/B added; dating-log OPE still missing. Direction 8: Xia/Baihe is the Chinese *dating-site data* card; 探探/陌陌/Soul ranking posts still null. Mix still wins.

**Tier mix:** 62 of 72 are Tier 1 or 2 (**86%**). Ten are Tier 3.

**NLM caveat:** several `source_ids` returned no body. Quartz Gini, Lyft MMV, DoorDash switchback, OkCupid JAX, Eureka, and Rios's *published* field number are cited from live publisher/engineering pages. Rios ingested PDF (`c17bdd53`) is a different manuscript — "Platform Design in Curated Dating Markets" — not *Improving Match Rates…* (M&SOM 25(4) 2023). GSB journal page reports **40% more matches** vs the partner algorithm; INFORMS/earlier abstracts said 25%+. Treat 40% as the journal-page figure, not as an NLM extract of the ingested PDF.

**2026-08-17 discovery:** imported leftover industry task `7ddbec32` (Airbnb two-sided ranking PDF + CyberAgent Speaker Deck) and a second industry pass `275cee32` (10 hits; imported Tinder Elastic talk, LinkSAGE, Kanzhun HKEX filing, Columbia congestion PDF). SEO “Hinge/Bumble algorithm explained” hits were **not** imported. Paper-keyword 61-hit `research_import` from 2026-08-16 is still gone (task not recoverable).

**2026-08-17 gap-fill:** Live pages first (MCP was disconnected). **NLM CLI follow-up (same day):** `nlm` auth valid; notebook now **165 sources**. Added Hinge 2025 pages, UniCoRn PDF, Kanzhun IR/CMBI, GFRR text extract. Queried RecSys 2025 list, Kanzhun trio, Hinge, UniCoRn+GFRR — bodies confirmed. Deep `research start` task `ChBjM2UxZDliYmYxN2JiODI4EAgaBDAxZDIqA3Vzdw` launched; CLI `research status`/`import` 400 on poll RPC `e3bVqc` so hits were **not** imported here. Reverse-citation map: `reverse-citation-map.md`.

---

## Annotated bibliography by search direction

Each item: title / authors / year / venue / link / tier · what they did · mechanism · metrics & effect · dating fit · confidence.

### Direction 1 — Reciprocal recommendation in dating

**Powering Tinder — The Method Behind Our Matching.** Tinder Newsroom. 2019. Company post. Tier 1. https://www.tinderpressroom.com/powering-tinder-r-the-method-behind-our-matching  
Did: Official statement that Elo is retired; ranking uses activity, distance, interests, visual similarity, mutual swipe patterns.  
Mechanism: Dynamic activity matching rather than a static desirability score.  
Metrics: Product stats (1.6B+ swipes/day) — no ranking A/B.  
Fit: **High** — primary Tinder ranking disclosure. Confidence: **High**.

**Personalized (User) Recommendations at Tinder: The TinVec Approach.** Steve Liu. 2017. MLconf SF. Tier 1. https://mlconf.com/sessions/personalized-user-recommendations-at-tinder-the-t/  
Did: Word2Vec-style embeddings from co-swipe sequences; recommend nearby vectors.  
Mechanism: Behavioral latent space, not demographics.  
Metrics: Slides claim AUC 90%, F1 85% for swipe direction.  
Fit: **Medium** — viewer-side CF, not capacity-aware. Confidence: **High** (slides in notebook).

**Tinder’s migration to Elasticsearch 8.** Sokolov, Hickey, Du. 2025. Tinder Tech Blog. Tier 1. https://medium.com/tinder/tinders-migration-to-elasticsearch-8-1999748ed7f4  
Did: Recs clusters (90%+ of recs from one ES cluster) moved to ES8; custom Java scoring plugin; geo-sharding; unlocked kNN vector search. Explicitly flags “sender-receiver ecosystem (swiper and swipee)” KPI risk of ranking changes.  
Mechanism: Two-tower retrieval/scoring for **P(Match)** vs **P(Like)** as separate experiments — the production statement of match-health vs swipe-CTR.  
Metrics: 2T P(Match): **+6.5% match rate**, **+22% match volume**. 2T P(Like): **+3.8% swipe-right rate**. p99 latency −12–56%.  
Fit: **High** — first Tinder *engineering* ranking post with online match vs like lifts. Confidence: **High** (live post; NLM extract).

**Large-scale collaborative filtering to predict who on OkCupid will like you, with JAX.** Zachary Jablons. 2021. OkCupid Tech Blog. Tier 1. https://tech.okcupid.com/large-scale-collaborative-filtering-to-predict-who-on-okcupid-will-like-you-with-jax-88ac8a934044  
Did: SVD-style CF on millions of voters × votees, hundreds of millions of votes/week; JAX training ~3 hours for a week of sitewide data.  
Mechanism: **Two vectors per user** (voter vs votee) because like is directed and `dot(A,B) ≠ dot(B,A)`. This is inbound-likeability, not viewer CTR.  
Metrics: “Improvement on baseline”; no public A/B %.  
Fit: **High** scoring primitive; **low** on capacity. Confidence: **High** (live post; NLM body miss, cited from page).

**Hinge “Most Compatible” (Gale–Shapley).** Sarah Perez / TechCrunch quoting CEO. 2018. Press. Tier 1. https://techcrunch.com/2018/07/11/hinge-employs-new-algorithm-to-find-your-most-compatible-match-for-you/  
Did: Daily “Most Compatible” slot via stable matching.  
Mechanism: Gale–Shapley / stable-roommate on like/pass prefs.  
Metrics: Press: 8× more likely to exchange numbers in early tests.  
Fit: **High** — market-design ranking, not CTR. Confidence: **Medium** (press only). Superseded as *the* Hinge ranking source by the 2025 product posts below.

**How We Connect Daters / 2025 product evolution.** Hinge. 2025. Company posts. Tier 1. https://hinge.co/how-we-connect-daters · https://hinge.co/newsroom/hinge-2025-product-evolution  
Did: 2025 Discover ranker is a deep-learning recsys for who you like **and** who is likely to like you. Dealbreakers are two-sided. Paid unlimited dealbreakers withheld because they shrink everyone’s pools.  
Mechanism: Mutual-compatibility ranking + two-sided filters; like-volume warning (“if you send too many likes, we can’t tell”). No architecture published.  
Metrics: Newsroom: **double-digit increase in matches overall** from the mutual-compatibility rollout. No A/B protocol. Match Note survey: ~2/3 of 2,000+ testers.  
Fit: **High** product statement; **low** method detail. Confidence: **High** (NLM bodies `b2ee80ca`, `76a4eccc`). This closes the “Hinge ranking post” gap at the company-page layer, not the engineering-blog layer.

**Matching Theory-based Recommender Systems in Online Dating.** Tomita, Togashi, Moriwaki (CyberAgent). 2022. RecSys industry talk. Tier 1. https://arxiv.org/abs/2208.11384  
Did: Deploy TU matching (Choo–Siow) on Tapple (~7M users) to replace capacity-blind fusion.  
Mechanism: Reciprocal score with transfer τ; IPFP + LSH/ANNS.  
Metrics: Qualitative: cuts like/match concentration; no public A/B %.  
Fit: **High**. Confidence: **High**.

**A Reciprocal Embedding Framework for Modelling Mutual Preferences.** Ramanathan, Shinada, Shimatani, Yamaguchi, Tanaka, Iizuka, Palaniappan (SBX + Tapple). 2021. AAAI / IAAI. Tier 1. https://cdn.aaai.org/ojs/17807/17807-13-21301-1-2-20210518.pdf  
Did: Production RRS on Tapple (then ~5M users, 200M matches): learn men→women and women→men embeddings separately, fuse for mutual like; two-stage retrieve + online rerank; region-specific models; precompute to KV store.  
Mechanism: Directed unidirectional prefs + aggregation; men send more likes than women receive (asymmetric activity). Online rerank blends relevance with recency so likes land on people who can reply.  
Metrics: Offline vs match-only RS: average recall **+16.9% matches**, **+26.74% likes**. Candidate-gen raised engagement but not conversion; after online rerank, conversion **up to +60%**. Sub-100 ms serve.  
Fit: **High** — Tapple production before the TU papers. Confidence: **High** (AAAI PDF).

**Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets.** Tomita, Togashi, Hashizume, Ohsaka. 2023. RecSys. Tier 1. https://arxiv.org/abs/2306.09060  
Did: Examination-agnostic TU ranker; vectorized for MIPS. Japanese dating logs + synthetic.  
Mechanism: IPFP outside options concatenated into (2d+2)-d features; popularity offset in score.  
Metrics: More matches than Naive/Reciprocal; works at sizes where SW dies; Gini improves.  
Fit: **High**. Survey 3 overlap — do not double-count. Confidence: **High**.

**Fair Reciprocal Recommendation in Matching Markets.** Tomita, Yokoyama. 2024. RecSys. Tier 1. https://arxiv.org/abs/2409.00720  
Did: Envy-freeness of recommendation opportunity; alternating NSW via Frank–Wolfe.  
Mechanism: Product of expected utilities → pull exposure off stars.  
Metrics: Dating data: envy 736→31 (men) vs TU; matches 90 vs 103.  
Fit: **High**. Survey 3 overlap. Confidence: **High**.

**MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations.** Tomita. 2026. RecSys. Tier 1. https://arxiv.org/abs/2608.01731  
Did: Mutual optimality of each user's list given others' lists; iterative deterministic ranker.  
Mechanism: Direct-effect equilibrium so congestion control does not dump bad recs on individuals.  
Metrics: 1000×1000 dating logs: >10% matches vs Naive/Reciprocal/TU.  
Fit: **High**. Confidence: **High**.

**Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method.** Yang, Dai, Hou, Zhao, Xu, Song, Zhu. 2024. KDD. Tier 1. https://arxiv.org/abs/2408.09748  
Did: Five bilateral metrics; causal RRS; vacant-slot rerank. Recruitment + dating.  
Mechanism: Recommendations as bilateral treatments; drop redundant dual exposures.  
Metrics: Dating CRecall@50 0.339 vs 0.301 DPGNN.  
Fit: **High**. Confidence: **High**.

**Modeling Two-Way Selection Preference for Person-Job Fit.** Yang, Hou, Song, Zhang, Wen, Zhao (BOSS Zhipin / RUC). 2022. RecSys. Tier 1. https://arxiv.org/abs/2208.08612  
Did: DPGNN dual nodes (select vs be-selected) + contrastive loss.  
Mechanism: Directed two-way preference, not undirected match.  
Metrics: +4.8–7.7% vs CF/content baselines on three job datasets.  
Fit: **Medium-high** (jobs; scoring pattern transfers). Confidence: **High**.

**Reciprocal Sequential Recommendation (ReSeq).** Zheng, Hou, Zhao, Song, Zhu. 2023. RecSys. Tier 1. https://arxiv.org/abs/2306.14712  
Did: Co-attention over both sides' sequences + self-distillation for serving.  
Mechanism: Dynamic two-way prefs, not static profiles.  
Metrics: Five datasets, dating + recruitment (paper; not re-extracted this run).  
Fit: **Medium-high**. Confidence: **Medium** (PDF in notebook; NLM batch skipped body).

**BOSS: Bilateral Occupational-Suitability-Aware Recommender.** Hu, Cheng, Zheng, Wang, Chi, Zhu. 2023. KDD. Tier 1. https://dl.acm.org/doi/10.1145/3580305.3599783  
Did: MoE over Click→Apply→Review→Accept; product of directional probs.  
Mechanism: Sequential two-sided funnel.  
Metrics: Online A/B on BOSS Zhipin: **+6.15% acceptance**.  
Fit: **Medium** (job funnel ≈ like→match→chat). Confidence: **High**.

**Optimally Balancing Receiver and Recommended Users' Importance.** Kleinerman, Rosenfeld, Ricci, Kraus. 2018. RecSys. Tier 3. https://u.cs.biu.ac.il/~sarit/data/articles/recsys18a-sub1173.pdf  
Did: RWS = CF interest × AdaBoost reply, per-user α via Brent. Live dating app Doovdevan (n=398).  
Mechanism: Personalized weight on reply probability.  
Metrics: Replies 99→322; recommends less popular users.  
Fit: **High**. Confidence: **High**.

**Recommending People to People (RECON case study).** Pizzato, Rej, Akehurst, Koprinska, Yacef, Kay. 2013. UMUAI. Tier 3. Dropbox author PDF in notebook.  
Did: Defines RRS; RECON harmonic mean + negative prefs. AU dating site, 1.4M messages.  
Mechanism: Harmonic mean of two preference vectors; subtract dislikes.  
Metrics: Top-10 success **42.2% vs 23.0%**.  
Fit: **High**. Confidence: **High**. RECON RecSys 2010 PDF: paywall, no free copy found.

**Reciprocal Recommendation System for Online Dating.** Xia, Liu, Sun, Chen. 2015. ASONAM. Tier 2. https://arxiv.org/abs/1501.06247  
Did: Baihe.com (China): 60M registered; 200k sampled (Nov 2011; 139k M / 61k F). Reciprocal score from content prefs + interest similarity (shared recipients) + attractiveness similarity (shared senders).  
Mechanism: CF vs content; heterosexual send/reply graph.  
Metrics: CF beats content and beats RECON/HCF on precision and recall (paper figures; no single headline %). Men optimize own interest and ignore inbound attractiveness; women do both.  
Fit: **High** as Chinese dating-*site data*; not a 探探 engineering post. Confidence: **High** (arXiv).

**Graph Fusion in Reciprocal Recommender Systems (GFRR).** Zhang, Wang (UTokyo / CyberAgent), Yamasaki. 2023. IEEE Access. Tier 2. https://doi.org/10.1109/ACCESS.2023.3239785  
Did: GNN on send vs reply edges; fusion for reciprocal prediction. 2020 logs from a collaborating dating service (JP). Mean match rate **<10%**.  
Mechanism: Separate send/reply heads + negative-sample mining; not capacity-aware.  
Metrics: Send AUC **73.15%** (+3.20 pp), reply **68.95%** (+1.74 pp), fusion **71.26%** (+4.35 pp) vs feature-interaction baselines. Offline only.  
Fit: **High** scoring (same send/reply split as Tinder/Hayashi). Confidence: **High** (IEEE Access HTML; NLM extract `2383281d` confirms AUCs; year/<10% from IEEE page, not the truncated extract).

**Reciprocal Recommender Systems: Survey.** Palomares, Porcel, Pizzato, Guy, Herrera-Viedma, Neve. 2021. Information Fusion. Tier 3. Author-copy PDF.  
Did: Last dedicated RRS survey found (2022–2026 search: none). Taxonomy + aggregation operators.  
Mechanism: Harmonic/geometric vs arithmetic; pessimistic ops fight stars.  
Metrics: Restates RECON +83% relative success.  
Fit: **High** as map, not as lever. Confidence: **High**. Last *dedicated* RRS journal survey; see Neve 2025 book and Mashayekhi 2024 CSUR (jobs) below.

**Reciprocal Recommender Systems (SpringerBriefs).** James Neve (Eureka / Pairs). 2025. Book. Tier 3. https://link.springer.com/book/10.1007/978-3-031-85103-2  
Did: Monograph from theory through matching-theory algorithms; author ships RRS at Pairs. Paywalled; no free PDF located this run.  
Mechanism: Matching-theory chapter is the post-2021 map the 2021 Palomares survey does not contain.  
Metrics: None (textbook).  
Fit: **High** as map. Confidence: **High** that the book exists; **low** on unreadable chapters.

**A Challenge-based Survey of E-recruitment Recommendation Systems.** Mashayekhi, Li, Kang, Lijffijt, De Bie. 2024. ACM Computing Surveys 56(10). Tier 3. https://arxiv.org/abs/2209.05112  
Did: Challenge-based (not algorithm-taxonomy) survey of job recsys; treats e-recruitment as reciprocal; cites LiJAR as job redistribution. Explicitly omits dating RRS to bound scope.  
Mechanism: Maps congestion, two-sided prefs, and redistribution in the job analog.  
Fit: **Medium** (jobs, not dating). Confidence: **High**.

**CUPID: A Real-Time Session-Based Reciprocal Recommendation System for a One-on-One Social Discovery Platform.** Kim, Kim, Kim, Yi, Ha, Lee, Lee, Yeom, Chang, Lee (Hyperconnect / Azar). 2024. arXiv:2410.18087. Tier 1. https://arxiv.org/abs/2410.18087  
Did: Production reciprocal matcher for Azar video chat: async session embeddings + two-phase training so pair scoring stays low-latency.  
Mechanism: Predict chat duration (mutual satisfaction proxy) via projected dual embeddings; avoids over-scoring similar users with a plain dot product.  
Metrics: Online: chat duration **+6.8%** (all), long-match ratio **+12.6%**, short-match **−2.4%**. p90 latency 236→48 ms (**−79.7%**).  
Fit: **Medium-high** (social discovery, not dating; same reciprocal latency problem). Confidence: **High** (NLM extract of PDF).

**Latent Factor Models… in RRS (LFRR).** Neve & Palomares. 2019. RecSys. Tier 3. ACM paywall. **nlm:failed:paywall.** Harmonic vs arithmetic aggregation is the lever; cited via Palomares 2021.

**皆が幸せになるマッチングプラットフォームを目指して / マッチングアプリにおける出会いを分析する.** CyberAgent Developers Blog. ~2022. Tier 1.  
Did: Tapple CF RRS; exposure inequality; TU matching approximation.  
Mechanism: Choo–Siow capacities in production narrative.  
Metrics: Recommendation Gini **~0.75**.  
Fit: **High**. Confidence: **High**.

---

### Direction 2 — Market / ecosystem framing

**Towards a Fair Marketplace.** Mehrotra, McInerney, Bouchard, Lalmas, Diaz (Spotify). 2018. CIKM. Tier 1. https://research.atspotify.com/publications/towards-a-fair-marketplace-counterfactual-evaluation-of-the-trade-off-between-relevance-fairness-satisfaction-in-recommendation-systems  
Did: IPS counterfactual tradeoff relevance / supplier fairness / satisfaction.  
Mechanism: Adaptive policies: send long-tail to high-tolerance users.  
Metrics: Global fairness shift −35% satisfaction; adaptive: fairness −15–17%, satisfaction **+9–21%**.  
Fit: **Medium** (creator side ≈ profile side). Confidence: **High**.

**Recommendations in a Marketplace.** Spotify Research. Publication page. Tier 1. https://research.atspotify.com/publications/recommendations-in-a-marketplace  
Did: Framing page for marketplace recs. Year unconfirmed.  
Fit: **Low-medium** (index, not a method). Confidence: **Medium**.

**How LinkedIn integrates fairness into its AI products.** Logan, Nandy, Basu, Jain. 2022. LinkedIn Eng. Tier 1.  
Did: LiFT + post-processing score transform on ProML.  
Mechanism: Pluggable rerank, not retraining.  
Metrics: Architecture only, no %.  
Fit: **Medium**. Confidence: **High**.

**Kanzhun / BOSS Zhipin traffic allocation (IR + CMBI + HKEX).** 2025. IR deck + CMBI + HKEX PDF. Tier 1. https://ir.zhipin.com/static-files/1946b353-b002-4517-9ab6-2c90e9743bb0 · https://hk-official.cmbi.info/upload/adaf574f-72fb-4317-855b-b4bb68635ec2.pdf  
Did: Recommendation-based feeds vs search; “fairer traffic distribution.” NLM: model “drive[s] more traffic to users who are more responsive.” Mutual consent to exchange resume/contact.  
Mechanism: Product-level redistribution + reply-weighting. Nanbeige is a vertical LLM for search/coaching, **not** the ranker. **No scoring formula.**  
Metrics: 2023: **4.8B** messages/month, **1.5B** mutual achievements. 88% SMEs; 66% of enterprise users are bosses. No ranking A/B %.  
Fit: **High analog**. Confidence: **High** on those sentences (NLM `ad032946`, `94e5fef2`, `503e6bd0`).

**Mapping Stakeholder Needs to Multi-Sided Fairness in Candidate Recommendation for Algorithmic Hiring.** Kaya (Jobindex), Bogers. 2025. RecSys. Tier 1. https://recsys.acm.org/recsys25/accepted-contributions/  
Did: 40 stakeholder interviews; map conflicting fairness definitions onto metric categories for CV→recruiter recs.  
Mechanism: None (qualitative).  
Metrics: None.  
Fit: **Medium** (jobs; multi-stakeholder warning). Confidence: **High** (RecSys 2025 program abstract). The only other RecSys 2025 matching-market paper is Hayashi OPE (already in D7).

**How Airbnb uses ML to Detect Host Preferences.** Bar Ifrach. 2015. Airbnb Eng. Tier 1. https://medium.com/airbnb-engineering/how-airbnb-uses-machine-learning-to-detect-host-preferences-18ce07150fa3  
Did: Model the *other side's* accept, not just guest click.  
Mechanism: Two-sided intent.  
Metrics: Not extracted this run (NLM miss).  
Fit: **High** as scoring idea. Confidence: **Medium** (URL verified; body not in NLM extract).

**Real-time Personalization using Embeddings… at Airbnb.** Grbovic & Cheng. 2018. KDD. Tier 1.  
Did: Listing embeddings for search.  
Mechanism: Guest-side personalization; weak capacity story.  
Fit: **Low** for balancing. Confidence: **High** (PDF in notebook).

**Building a Large-Scale Recommendation System: People You May Know.** LinkedIn (classic). Tier 1.  
Did: PYMK at scale; companion to impression discounting.  
Fit: **Medium**. Confidence: **Medium**.

**GraphMatch: Fusing Language and Graph Representations in a Dynamic Two-Sided Work Marketplace.** Sacha, Jafri, Terzolo, Sinha, Rabinovich (Upwork). 2025. arXiv:2512.02849. Tier 1. https://arxiv.org/abs/2512.02849  
Did: Production-scale two-sided retrieval on Upwork (~9M nodes, 62M edges): text encoders + GNN, task-homogeneous client vs freelancer batches, contrastive loss on interviews/hires.  
Mechanism: Mutual-interest events as the alignment signal; side-separated batches so one side does not drown the other.  
Metrics: NDCG@10 freelancer→job **24.2%** vs TextMatch-large 22.4%; job→freelancer **12.4%** vs 11.4%. Serve <70 ms/embedding.  
Fit: **Medium** (jobs; two-sided training recipe transfers). Confidence: **High**.

**LinkSAGE: Optimizing Job Matching Using Graph Neural Networks.** Liu, Wei, Hou, Shen, He, Shen, Chen, Borisyuk, Hewlett, Wu, Veeraraghavan, Tsun, Jiang, Zhang (LinkedIn). 2025. KDD. Tier 1. https://arxiv.org/abs/2402.13430  
Did: Heterogeneous job-marketplace GNN encoder decoupled from existing DNNs; nearline serve. LiJAR coauthor Borisyuk is on this paper — graph layer on top of the redistribution stack.  
Mechanism: Member–job–recruiter graph for matching, not viewer CTR.  
Metrics: JYMBII A/B: qualified applications **+2.2%**, QA rate **+0.3%**; opportunistic seekers QA **+3.2%**, urgent **+2.6%**; Premium survival (free→paid) **+2.2%** in a later graph-edge test.  
Fit: **Medium** (jobs). Confidence: **High** (arXiv HTML).

**Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search.** Geyik, Ambler, Kenthapadi. 2019. KDD. Tier 1. https://arxiv.org/abs/1905.01989  
Did: DetGreedy post-processing so top-k gender mix matches the qualified set; deployed to 100% of LinkedIn Recruiter.  
Mechanism: Constrained re-ranking to a target exposure distribution — the protected-attribute analog of inbound-like caps.  
Metrics: Searches with representative results ~3× (paper: >95% of searches feasible vs prior); business metrics flat.  
Fit: **Medium** (attribute fairness ≠ desirability congestion, but the rerank slot is the same). Confidence: **High**.

---

### Direction 3 — Capacity and congestion

**LiJAR: Job Application Redistribution.** Borisyuk, Zhang, Kenthapadi. 2017. KDD. Tier 1. http://theory.stanford.edu/~kngk/papers/LiJAR-SystemForJobApplicationRedistribution-KDD2017.pdf  
Did: Forecast applications at expiry; boost under-served, exponentially penalize over-served.  
Mechanism: Min/max application bands as capacity.  
Metrics: Entropy **+12%**; over-served apps **−8.7%**; underserved engagement **+6.5%**; total apps **+2.3%**.  
Fit: **High** analog (likes ≡ applications). Confidence: **High**.

**Modeling Impression Discounting in Large-scale Recsys.** Lee, Lakshmanan, Tiwari, Shah. 2014. KDD. Tier 1.  
Did: Decay ignored PYMK impressions.  
Mechanism: Score × d(impressions, no-action).  
Metrics: Offline invitation +31%; online **+13%**.  
Fit: **High** (repeat-seen profiles). Confidence: **High**.

**Managing Congestion in Matching Markets.** Arnosti, Johari, Kanoria. 2021. M&SOM. Tier 2. http://www.columbia.edu/~yk2577/congestion.pdf  
Did: Cheap applications → screening collapse; employers' welfare → 0.  
Mechanism: Application limits / costs restore efficiency.  
Metrics: Limits can give both sides ≥3/4 of constrained-efficient welfare.  
Fit: **High** (daily like caps). Confidence: **High**.

**Aspirational Pursuit of Mates in Online Dating Markets.** Bruch & Newman. 2018. Science Advances. Tier 2. https://arxiv.org/abs/1808.04840  
Did: PageRank desirability on messaging graphs, four US cities.  
Mechanism: Everyone aims ~25% “up”; reply falls with gap.  
Metrics: 25% desirability gap; longer messages up-hierarchy.  
Fit: **High** (describes the skew). Confidence: **High**.

**Your Looks and Your Inbox.** Rudder / OkCupid OkTrends. 2009. Tier 1. https://gwern.net/doc/psychology/okcupid/yourlooksandyourinbox.html  
Did: Attractiveness vs inbox volume.  
Mechanism: Documents congestion, does not fix it.  
Metrics: Men send 2/3 of messages to top 1/3 of women; top women 5× typical, 28× bottom.  
Fit: **High**. Confidence: **High**.

**Hinge Gini (Goldgeier via Quartz).** 2017. Press. Tier 1. https://qz.com/1051462/these-statistics-show-why-its-so-hard-to-be-an-average-man-on-dating-apps  
Did: Like-distribution Gini by gender.  
Metrics: **0.376 women vs 0.542 men**.  
Fit: **High** (ecosystem KPI). Confidence: **High** on the article; NLM returned no body for this source_id.

**Managing Congestion… via Demand Information Disclosure.** Huang, Burtch, Chen, Huang. ISRE / related. Tier 2. Notebook source present.  
Did: Show inbound volume + “busy” framing.  
Mechanism: Information, not rerank.  
Metrics: NLM: deters likes to stars (see design-pattern query).  
Fit: **High** if UI-legal. Confidence: **Medium**.

**Recommendation with Capacity Constraints.** Christakopoulou, Kawale, Banerjee. 2017. CIKM. Tier 3. Author PDF.  
Did: Capacity loss in PMF/BPR/GeoMF.  
Metrics: Cap-BPR capacity loss 4.51→0.08 on ML-100K.  
Fit: **Medium** (items ≠ people). Confidence: **High**.

**It takes two to tango (desirability on a mobile dating app).** PMC paper in notebook. Tier 2.  
Did: Two-mode network desirability.  
Fit: **Medium**. Confidence: **Medium**.

**Introducing Smart Photos — For The Most Swipeworthy You.** Tinder Newsroom. 2016. Tier 1. https://www.tinderpressroom.com (Smart Photos post; nlm:7ee84a11)  
Did: Rotate first photo, learn which image gets right-swipes, personalize order to the viewer.  
Mechanism: **Anti-pattern for balancing** — raises inbound likes on already-shown people (viewer-appeal), which the congestion literature says overloads stars.  
Metrics: Testing: **up to +12% matches**.  
Fit: **High** as a warning, not a template. Confidence: **High**.

---

### Direction 4 — Constrained allocation / rerank

**Improving Match Rates in Dating Markets Through Assortment Optimization.** Rios, Saban, Zheng. M&SOM 25(4) 2023 (online 2022). Tier 2. https://pubsonline.informs.org/doi/10.1287/msom.2022.1107 · SSRN 3698751 · ingested `dating_alf.pdf`  
Did: Daily profile sets; like-probability falls after recent matches; heuristics + **two field experiments** at a major US dating company.  
Mechanism: Assortment timing given two-sided likes and match stock.  
Metrics: GSB journal page for M&SOM 25(4): algorithm can yield **40% more matches** vs partner (simulations + field). Earlier INFORMS/brief wording was 25%+. Ingested `dating_alf.pdf` (`c17bdd53`) is **not this paper** — NLM title is "Platform Design in Curated Dating Markets".  
Fit: **High**. Confidence: **High** that the published article exists; **medium** on which % is the field-test headline (cite GSB 40%, do not treat the ingested PDF as C1).

**Assortment Planning for Two-Sided Sequential Matching Markets.** Ashlagi, Krishnaswamy, Makhijani, Saban, Shiragur. 2022. Operations Research. Tier 2. https://web.stanford.edu/~iashlagi/papers/assortment.pdf  
Did: Menus to customers; suppliers match at most once; LP rounding.  
Metrics: NP-hard; ≥1/3 of LP bound in sims.  
Fit: **Medium-high**. Confidence: **High**.

**Fairness of Exposure in Rankings.** Singh & Joachims. 2018. KDD. Tier 3. https://arxiv.org/abs/1802.07281  
Did: LP exposure constraints + Birkhoff decomposition.  
Metrics: DTR 1.75→1.00, DCG almost unchanged (job sim).  
Fit: **Medium**. Confidence: **High**.

**Two-sided Fairness via Lorenz Dominance.** Do, Corbett-Davies, Atif, Usunier (Meta). 2021. NeurIPS. Tier 3. https://arxiv.org/abs/2110.15781  
Did: Concave welfare both sides; explicit reciprocal extension.  
Metrics: Higgs: worst-off 10% utility more than doubles.  
Fit: **High** (reciprocal section). Confidence: **High**.

**Integrating Predictive Models into Two-Sided Recommendations (ECDA).** Sekiya, Otani, Komatsu, Ohkawa, Noda. 2026. arXiv in notebook. Tier 2/3.  
Did: Constrain expected likes/dates, not displays; deferred acceptance.  
Mechanism: Exposure-constrained DA on predicted funnel.  
Fit: **High** if production-shaped. Confidence: **Medium** (NLM pattern query; not independently re-read).

**No Stakeholder Left Behind (regret-aware two-sided rerank).** ResearchGate PDF in notebook. Tier 3.  
Fit: **Medium**. Confidence: **Low-medium**.

**The Dating Heuristic: A Provably Strong Matching Algorithm for Dating Platforms.** (Follow-on to Rios et al.) 2023. arXiv:2308.02584. Tier 2. https://arxiv.org/pdf/2308.02584  
Did: Worst-case analysis of daily-assortment algorithms under one- vs two-directional search and sequential vs simultaneous likes. Greedy/perfect matching can be arbitrarily bad; Dating Heuristic (Rios et al. 2023) gets **1−1/e** for all those designs.  
Mechanism: Submodular assortment with match backlog; one-directional design should let the side with smaller expected backlog per impression initiate.  
Metrics: Theory + partner-data simulations; one-directional can still get ≥ half the two-directional matches.  
Fit: **High** (ties assortment to who-searches). Confidence: **High** (PDF).

---

### Direction 5 — Market-design levers

**Facilitating the Search for Partners on Matching Platforms.** Kanoria & Saban. 2021. Management Science. Tier 2. https://web.stanford.edu/~dsaban/facilitating-search.pdf  
Did: Who should be allowed to search/propose.  
Mechanism: In imbalance, block the long/less-selective side.  
Metrics: Worker welfare up, employer welfare almost flat (theory).  
Fit: **High** (Bumble-like). Confidence: **High**.

**Competing by Restricting Choice.** Halaburda, Piskorski, Yıldırım. 2018. Management Science. Tier 2.  
Did: Why a small daily set can beat a large catalog.  
Mechanism: Same-side congestion from large N.  
Metrics: Explains eHarmony price premium vs Match.  
Fit: **High** (CMB/Hinge daily batch). Confidence: **High**.

**Effects of Market Size and Competition… Evidence from Online Dating** (working title: Search, Selectivity, and Market Thickness). Fong. 2024. Marketing Science. Tier 2. UCLA working-paper PDF in notebook.  
Did: Field experiment manipulating believed thickness + structural model.  
Mechanism: Beliefs → selectivity; like limits interact with size.  
Metrics: +50% believed size: −3% like on low-quality, +2.8% on high-quality. +25% members: **−12% / −17% matches** in small markets; doubling like limit reverses.  
Fit: **High**. Confidence: **High**.

**Propose with a Rose? Signaling in Internet Dating Markets.** Lee & Niederle. 2015. Experimental Economics. Tier 2. Stanford PDF.  
Did: RCT of scarce virtual roses on a Korean dating site.  
Mechanism: Costly-looking cheap talk with a cap.  
Metrics: Rose **+3.3pp accept (~+20% rel.)**; 8 vs 2 roses: +44–48% dates (men), +86% (women); 30% of roses wasted on top group.  
Fit: **High** (Super Like analog). Confidence: **High**.

**Matching and Sorting in Online Dating.** Hitsch, Hortaçsu, Ariely. 2010. AER. Tier 2.  
Did: Structural prefs + Gale–Shapley efficiency.  
Metrics: Age corr 0.70; decentralized within 3.8–4.6% of first-choice planner.  
Fit: **Medium** (sorting, not congestion ops). Confidence: **High**.

**Coffee Meets Bagel × ElastiCache.** Pyrathon & O'Steen. 2019. AWS. Tier 1.  
Did: Daily queue infra, 100 latent features, Bloom seen-filter.  
Mechanism: Product is a **restricted daily batch**; post is infra.  
Metrics: 1.5M users/day, 2–4ms reads.  
Fit: **Low** for modeling (brief flag). Confidence: **High**.

**Automated Decision Making at Grindr.** Wiley & Quisel. Grindr. Tier 1. https://www.grindr.com/blog (ADM page in notebook)  
Did: **No ranking of matches**; distance + filters + light randomness.  
Mechanism: User-driven marketplace as an alternative to recs.  
Fit: **Medium** (product counterexample). Confidence: **High**.

**Tantan matching strategy (CEO Wang Yu at TechCrunch Hangzhou).** TechNode. 2018. Tier 1. https://technode.com/2018/07/05/tantans-matching-strategy-you-can-be-matched-but-possibly-not-with-your-soul-mate/  
Did: CEO: greedy individual matching ≠ community optimum; platform has a “God’s-eye-view.”  
Mechanism: Rhetoric for ecosystem vs greedy CF.  
Fit: **Medium**. Confidence: **Medium** (`source_add` of this URL failed this run).

**争议：婚恋网站的推荐系统…** 吴金龙 (世纪佳缘) vs 黄鑫. 2018. 腾讯云. Tier 1. https://cloud.tencent.com/developer/article/1142668  
Did: Jiayuan recsys as product/pay conversion; commentator pushes reciprocal metrics (coverage, send motivation, read-pay).  
Mechanism: Reciprocal rec as KPI design, not a model.  
Fit: **Medium**. Confidence: **High**.

**Ethical Considerations of AI for Online Dating.** James Neve. 2023. Pairs Engineering (Eureka). Tier 1. https://medium.com/eureka-engineering/ethical-considerations-of-ai-for-online-dating-41d9c3b4345c  
Did: Pairs AI lead: recs must raise P(like-back), not just P(like). Popularity bias wastes likes on stars who already have thousands. Cites Kleinerman 2018. No model details (deliberate).  
Mechanism: Product ethics = reciprocal + anti-star as constraints, not afterthoughts.  
Metrics: None.  
Fit: **High** (dating-app eng statement of the problem). Confidence: **High** (live post).

**基于双向匹配的陌生人社交业务、策略及算法思考.** (Maimai essay on two-way stranger matching.) ~2023. 脉脉. Tier 1. https://maimai.cn/article/detail?fid=1542265757&efid=k0ypdX75--KrtTL_r1IxAA  
Did: Product levers for Tinder/Tantan/Momo/Soul-like apps: drip (“reservoir”) matches instead of dumping 100 at open; LBS vs looks; fast vs slow matching; hide the match from the short side until the long side sends first message.  
Mechanism: **Pacing inbound attention** and **who speaks first** — market-design, not a ranker.  
Metrics: Qualitative (“head/mid get much higher match rates”).  
Fit: **High** levers, **low** on identified production A/B. Confidence: **Medium** (essay, not a named-company paper).

---

### Direction 6 — Objectives and metrics

Covered in-line above: OkCupid concentration; Hinge Gini 0.376/0.542; Tapple Gini ~0.75; CRRS CRecall/SRecall/RNDCG; MRet retention objective (Kishimoto et al., arXiv:2602.15752, ICLR'26-labeled preprint — **High** fit, **Medium** confidence on unpublished numbers); Kleinerman less-popular recommendations as an implicit anti-congestion metric.

**Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching.** Kishimoto, Takehi, Tanaka, Nomura, Togashi, Tomita, Saito. 2026. arXiv:2602.15752. Tier 2/3.  
Did: MRet — allocate matches where retention curves say they pay.  
Fit: **High** (Survey 3 adjacent). Confidence: **Medium**.

---

### Direction 7 — Evaluation under interference

**Experimental Design in Two-Sided Platforms.** Johari, Li, Liskovich, Weintraub. 2022. Management Science. Tier 2. https://arxiv.org/abs/2002.05670  
Did: Mean-field interference; customer vs listing vs two-sided randomization.  
Mechanism: Randomize the *congested* side; TSR + cannibalization correction.  
Metrics: Demand-constrained: listing-side bias 1.7% of GTE (sim).  
Fit: **High**. Confidence: **High**.

**A/B Testing for Recommender Systems in a Two-sided Marketplace (UniCoRn).** Nandy, Venugopalan, Lo, Chatterjee (LinkedIn). 2021. NeurIPS. Tier 1. https://arxiv.org/abs/2106.00762  
Did: Producer-side experiment design when producer outcomes depend on consumer treatment. Mixes treatment/control producer lists in each viewer session; α trades accuracy vs cost.  
Mechanism: Unifying Counterfactual Rankings; deployed with **α=0** (no extra scoring latency). Ranking arm boosts candidates predicted to **visit if they get a request** (viewee retention).  
Metrics: 750M+ members; billions of edges/day; 40% viewer traffic. Candidate-gen: **+0.51% WAU**, **+0.57% sessions**. Ranking: **+0.13% WAU**, **+0.11% sessions**. p<0.001. No dating.  
Fit: **High analog** (inbound-like = producer). Confidence: **High** (NLM `93144d1a`). **Not** dating-log OPE.

**Multiple Randomization Designs.** Bajari et al. 2021. arXiv:2112.13495. Tier 2.  
Did: Buyer×seller tuple randomization and spillover estimators.  
Fit: **High**. Confidence: **Medium** (NLM mixed a 2025 Masoero et al. writeup with this PDF).

**Reducing Interference Bias… Cluster Randomization (Airbnb).** Holtz, Lobel, Liskovich, Aral. 2025. Management Science. Tier 2.  
Did: Meta-experiment, 2.6M listings; clusters from search co-view embeddings.  
Metrics: **19.76%** of naive TATE was interference.  
Fit: **Medium-high** (substitutes ≈ similar profiles). Confidence: **High**.

**Using Marketplace Marginal Values to Address Interference Bias.** Nassiri & Bright. 2025. Lyft Engineering. Tier 1. https://eng.lyft.com/using-marketplace-marginal-values-to-address-interference-bias-a11aff6e670f  
Did: User-split ATE corrected by hourly dispatch duals (shadow prices). 90% of Lyft tests are user-split.  
Mechanism: MMV = resource contention; matches Bright et al. 2024 theory.  
Metrics: vs time-split: closer after MMV; **10% of launch decisions would flip**; congested cases **~45% smaller** effect.  
Fit: **Medium** (match-based dispatch, not swipe choice — still the right *bias* lesson). Confidence: **High** (live page; NLM miss).

**Experiment Rigor for Switchback Experiment Analysis.** DoorDash Engineering. 2025. Tier 1. https://careersatdoordash.com/blog/experiment-rigor-for-switchback-experiment-analysis/  
Did: Switchback analysis rigor under network effects.  
Fit: **Medium**. Confidence: **Medium** (URL verified; fetch timeout / NLM miss). Related DoorDash posts in notebook: supply-demand ML, dispatch optimization.

**Off-Policy Evaluation and Learning for Matching Markets.** Hayashi, Goda, Saito. 2025. RecSys. Tier 1. https://arxiv.org/abs/2507.13608  
Did: DiPS/DPR using first-stage scout + sparse match; Wantedly Visit A/B logs (21.7k companies, 17.5k seekers, 1.2% sparsity).  
Metrics: Lower MSE than IPS/DR; tracks online A/B.  
Fit: **High**. Confidence: **High**.

**Location-grouped A/B (Tapple).** Ramanathan et al., AAAI 2021 (card in Direction 1).  
Did: Prefers prefecture-level models and same-location assignment so likes between treated and control users do not leak.  
Fit: **High**. Confidence: **High**.

---

### Direction 8 — Chinese / Japanese sources

Japanese: CyberAgent/Tapple line now includes **AAAI 2021 production RRS** (Ramanathan et al.) before the RecSys 2022–2026 matching-theory papers; GFRR (IEEE Access 2023) is a send/reply GNN on 2020 JP dating logs (Wang @ CyberAgent); Eureka/Pairs ethics post (Neve 2023); Wantedly RecSys 2025 OPE.  
Chinese: Xia et al. ASONAM 2015 on **Baihe.com** (CF > content; 200k sample); 世纪佳缘 2018 debate; Tantan TechNode 2018; **Maimai two-way matching essay**; Kanzhun IR (jobs, fairer traffic). **Still null:** Tantan/Momo/Soul *ranking* engineering post with model detail. InfoQ Momo recall is nearby-feed — not added. 知乎 `p/654446985` still unextracted.

**Bumble Tech ranking post:** **Null** (re-confirmed 2026-08-17 gap-fill). `site:tech.bumble.com ranking` returned no hits. Job posts mention retrieval/ranking/marketplace health; closest *published* Tech work is bitmap-index search and CLIP/image captioning, not a matching ranker. HLD Handbook / DEV.to “Bumble algorithm” pages are not primary — not cited.

**RecSys 2025 accepted list** (mined from live program; `nlm:bf49347b` not re-queried): matching-market paper = Hayashi/Goda/Saito OPE. Adjacent: Kaya/Bogers Jobindex fairness interviews (added); LCM4Rec choice/cannibalization (not added — T3, not a matching ranker).

**RecSys 2026 industry track papers:** **Null as of 2026-08-17** (conference 2026-09-27). MODE is research-track.

---

## Design-pattern matrix

Rows = levers. Cells = one line. Empty = not that paper's contribution.

| | Reciprocal scoring | Capacity-aware scoring | Constrained re-ranking | Market-design lever | Ecosystem metrics | Evaluation method |
|---|---|---|---|---|---|---|
| Pizzato UMUAI 2013 | Harmonic + C± | | | | Success/failure @n | Offline dating logs |
| Kleinerman RecSys 2018 | Per-user reply weight α | Down-ranks stars as side effect | | | Popularity of recs | Live dating A/B |
| Tomita RecSys 2022 talk | τ-adjusted reciprocal | Choo–Siow capacity | IPFP+ANNS serve | | Concentration of likes | Deployment narrative |
| Tomita RecSys 2023 TU | | IPFP outside option in score | MIPS rank | | Match count, Gini | Dating logs |
| Tomita RecSys 2024 NSW | | | Envy-free NSW lists | | Envy count vs matches | Dating logs |
| Tomita RecSys 2026 MODE | | Direct-effect equilibrium | Iterative deterministic lists | | Matches vs TU | Dating logs |
| Yang KDD 2024 CRRS | Causal bilateral score | | Vacant-slot rerank | | CRecall, RNDCG | Dating+jobs |
| LiJAR KDD 2017 | | Forecast vs min/max apps | Boost/penalize | | Entropy of applications | LinkedIn online |
| Lee KDD 2014 | | | Impression decay | | Invitation rate | PYMK A/B |
| Rios M&SOM 2023 | | Match-stock in like model | Daily assortment | | Matches +40% GSB page / 25%+ earlier abstracts | Two field tests |
| Arnosti M&SOM 2021 | | | | Application cap | Two-sided welfare | Theory |
| Kanoria–Saban MS 2021 | | | | Who may search | Selectivity, welfare | Theory (+Bumble analog) |
| Halaburda MS 2018 | | | | Restrict N | Accept rate, fees | eHarmony vs Match |
| Fong MS 2024 | | | | Like limit × thickness | Matches −12/−17% if grown blindly | Dating RCT |
| Lee–Niederle 2015 | | | | Scarce roses | +20% accept | Dating RCT |
| Mehrotra CIKM 2018 | | | Adaptive fair routing | | Supplier fairness vs satisfaction | IPS off-policy |
| Johari MS 2022 | | | | | GTE bias | Two-sided randomization |
| Holtz MS 2025 | | | | | 19.8% TATE was interference | Cluster RCT |
| Lyft MMV 2025 | | Shadow price of congestion | | | Launch-decision flips 10% | User-split correction |
| Hayashi RecSys 2025 | Two-stage like→match | | | | OPE MSE | Wantedly A/B logs |
| OkCupid 2009 / Hinge Gini | | | | | Inbox skew; Gini 0.38/0.54 | Observational |
| Grindr ADM | | | | No ranking | User-driven | Transparency page |
| MRet 2026 | Retention-weighted | | LTR allocation | | Two-sided retention | Dating preprint |
| Tinder ES8 2025 | 2T P(Match) vs P(Like) | | kNN retrieve | | Match rate vs SRR | Online A/B |
| OkCupid JAX 2021 | Voter vs votee vectors | | | | Like prediction | Offline SVD |
| Ramanathan AAAI 2021 | Dual-direction embed + fuse | Recency in rerank | Two-stage + online rerank | Region models | Conversion +60% after rerank | Location-grouped A/B |
| CUPID 2024 | Dual projected chat-duration | | Async session cache | | Long-match +12.6% | Azar production |
| GraphMatch 2025 | Side-separated batches | | | | NDCG@10 both directions | Upwork |
| LinkSAGE 2025 | GNN member–job graph | | Nearline encoder | | QA +2.2% / opp. +3.2% | LinkedIn A/B |
| Geyik KDD 2019 | | | DetGreedy gender mix | | 3× representative searches | Recruiter 100% |
| Tinder Smart Photos | | | | Viewer-appeal photos | Matches +12% | Anti-pattern |
| Neve Pairs 2023 | Reciprocal rec as ethics | | | Don't dump stars | None | Eng post |
| Maimai essay | | | | Reservoir + who speaks first | Qualitative skew | Product |
| Dating Heuristic 2023 | | Match backlog in assortment | DH 1−1/e | Who initiates | Sims on partner data | Theory+data |
| Hinge 2025 posts | DL mutual compatibility | | | Two-sided dealbreakers; like-volume warning | Double-digit matches (newsroom) | Product, no A/B protocol |
| GFRR 2023 | Send vs reply GNN + fusion | | | | Send AUC 73.15 / fusion 71.26 | Offline dating logs |
| Xia ASONAM 2015 | Interest + attractiveness CF | | | | CF > RECON/HCF (P/R) | Baihe logs |
| UniCoRn 2021 | | | | | Producer-side design inaccuracy | LinkedIn edge A/B |
| Kanzhun IR 2025 | | Traffic → responsive users | | Fairer distribution (IR) | None public | Product |

---

## Reverse citation / cross-reference map

See `reverse-citation-map.md` for the lineage diagram. Short version: RECON → Palomares → Kleinerman / Xia → Ramanathan 2021 → TU 2022/23 → NSW 2024 → MODE 2026; GFRR is a parallel GNN send/reply line; LiJAR → Geyik / LinkSAGE / Kanzhun IR (jobs); Rios → Dating Heuristic; Johari → Holtz / Lyft MMV / UniCoRn (eval). RecSys 2025 matching paper is Hayashi. Phase 3.7 was not run via NLM (MCP down).

---

## Gaps and next five searches

1. **Bumble / Match ranking engineering posts** — Hinge 2025 company pages now exist (mutual-compat DL; double-digit matches). Still no Hinge *engineering* post with architecture. Bumble Tech ranking still null (re-confirmed). Re-search RecSys 2026 industry talks after 2026-09-27.
2. **Inbound-like pacing in production** — Maimai essay describes a match reservoir; Kanzhun IR says “traffic to more responsive users” with no model. Still no PID / guaranteed-delivery / LiJAR-style *like* forecaster on a dating app.
3. **Chinese dating recsys (探探 / 陌陌 / Soul)** — Xia/Baihe 2015 is academic CF on a Chinese site, not a Tantan ranking blog. Still no 探探/陌陌/Soul ranking post with model detail.
4. **Dedicated RRS survey after Palomares 2021** — none. Substitutes: Neve 2025 SpringerBriefs (paywalled); Mashayekhi 2024 CSUR (jobs).
5. **Two-sided OPE on dating logs** — Wantedly DiPS is jobs (Hayashi names dating in the abstract). Ramanathan is location A/B, not OPE. UniCoRn is LinkedIn producer-side A/B. Need a Tapple/Pairs/Hinge DiPS writeup.

Paper-keyword 61-hit re-import still blocked (NLM disconnect this session). Do not pad T3 to replace it.

## Read-first (expected value for our design)

1. Tomita et al., RecSys 2023 — TU matching on a dating platform, production-shaped.  
2. Sokolov, Hickey, Du, Tinder Tech Blog 2025 — **P(Match) vs P(Like)** online: +6.5% match rate / +22% match volume vs +3.8% SRR.  
3. Hinge 2025 company posts — mutual-compatibility DL; double-digit match lift; like-budget + dealbreaker ecosystem.  
4. Ramanathan et al., AAAI 2021 — Tapple production RRS; conversion +60% only after recency rerank.  
5. Borisyuk et al., KDD 2017 LiJAR — redistribution template (Kanzhun IR is the Chinese product sentence).  
6. Rios, Saban, Zheng, M&SOM 2023 — dating field assortment (GSB page: 40% more matches; ingested PDF is a different paper).  
7. Tomita & Yokoyama, RecSys 2024 — envy vs match-count tradeoff.  
8. Fong, Marketing Science 2024 — like limits × market size.  
9. Hayashi, Goda, Saito, RecSys 2025 — matching-market OPE (jobs logs).  
10. Johari et al., MS 2022 / UniCoRn NeurIPS 2021 / Ramanathan location A/B / Lyft MMV 2025 — do not A/B this like a feed.

Per-paper notes: `read-papers/` (read-first plus 2026-08-17 additions and this gap-fill). Citation map: `reverse-citation-map.md`.

## Null results (log)

- Bumble Tech ranking post: still none (2026-08-17 gap-fill; `site:tech.bumble.com ranking` empty). SEO/HLD Handbook pages discarded.  
- RECON RecSys 2010 and Neve RecSys 2019: ACM paywall, no free PDF.  
- RecSys 2026 industry track: not posted as of 2026-08-17.  
- Awesome recsys repo: 0 relevant PDFs (2026-08-16).  
- Dedicated RRS *journal survey* after Palomares 2021: none. Neve 2025 is a book; Mashayekhi 2024 is e-recruitment CSUR.  
- 探探 / 陌陌 / Soul ranking engineering posts with model detail: none. Xia 2015 is Baihe academic CF. InfoQ Momo is nearby-feed recall.  
- Hinge *engineering* ranking post: none. 2025 company pages exist (this run).  
- Paper-keyword 61-hit `research_import` from 2026-08-16: still unrecoverable. Re-run `research_start` this session: NLM MCP not connected.  
- LinkedIn KDD 2019 student.cs PDF URL: `source_add` failed; used arXiv 1905.01989 instead.  
- Neve SpringerBriefs 2025: no free PDF.  
- SSRN Rios 3698751 HTML: not ingested this run (cite GSB journal page).  
- Dating-log OPE: none. Hayashi eval is Wantedly.  
- NotebookLM this gap-fill: `notebook_get` / `research_start` / `source_add` all `Not connected`. Cards cited from live pages/PDFs.  
- RecSys 2025 LCM4Rec: not added (T3 choice model; not matching).
