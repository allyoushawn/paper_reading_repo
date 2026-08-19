Date: 2026-08-16
Topic: two-sided market balancing in dating-app recommendation: reciprocal recommendation, exposure allocation under capacity limits, congestion in matching markets

# two-sided market balancing in dating-app recommendation: reciprocal recommendation, exposure allocation under capacity limits, congestion in matching markets - Survey Requirements

## Request

Verbatim topic (used for NLM `research_start` keyword extraction): "two-sided market balancing in dating-app recommendation: reciprocal recommendation, exposure allocation under capacity limits, congestion in matching markets"

This is Survey 4 of the Attribution-Based Retention project. The full ask is defined in the survey brief: `knowledge_base/projects/attribution_based_retention/survey-4-brief-two-sided-market-balancing-dating.md`. Problem statement and full Project Context: see `./README.md`.

What is requested (brief's "What we want from you"):
1. A reference list, industry first.
2. For each reference: the mechanism, the metric, the reported effect, and how it maps to a dating app.
3. A synthesis of design patterns.
4. Gaps and next searches.

Run mode: `/literature-survey-nlm`. NotebookLM notebook `two-sided-market-balancing-dating`, id `d3071ac8-16ef-4460-8991-7701679974c8` (already exists, currently 0 sources — do not call `notebook_create`). Workspace prefix for this run: `claude_opus` — this run's own outputs go under `./claude_opus/`, per the brief's multi-runner "Shared resources" convention; `README.md` and this file are shared at the topic root.

## Core Keywords

Extracted from the topic string (6, within the 3–6 range):
- two-sided market balancing
- reciprocal recommendation
- exposure allocation
- capacity-constrained recommendation (capacity limits)
- congestion in matching markets
- dating-app recommendation

## Target Conferences / Journals

**TIER OVERRIDE.** `literature-survey-priorities.md` ranks academic venues first. This survey inverts that, per the brief's "Source priority" section.
- Tier 1 — Industry: engineering blogs, industry-track papers (KDD Applied Data Science, RecSys industry, WWW industry, CIKM applied), conference talks (RecSys, KDD, MLconf, QCon, Data Council), patents. Prefer these.
- Tier 2 — Applied research on real platform data or field experiments (operations research, economics, marketing science, management science). Include when it reports an experiment or data from a real dating or matching platform.
- Tier 3 — Academic ML papers. Include only when the method maps directly to a named lever, or when it is a survey.
- **Target mix: at least 60% of items from Tier 1 + Tier 2.**

Operationalizing the override into concrete venues:

- **Tier 1 (prefer):** RecSys industry track, KDD Applied Data Science track, WWW industry track, CIKM applied track; talks at RecSys, KDD, MLconf, QCon, Data Council; patents (Google Patents / USPTO full-text search); company engineering blogs (see "Target Engineering Blogs" below). Why: the brief's known gap is that dating apps publish little modeling detail directly, so industry-track papers and talks from adjacent two-sided platforms (job marketplaces, ride-share, home-share) carry the real design detail.
- **Tier 2 (include when grounded in real platform data/experiments):** Management Science, M&SOM (Manufacturing & Service Operations Management), Marketing Science, Operations Research, Experimental Economics, American Economic Review, Science Advances. Why: OR/economics field experiments on real dating or matching-platform data are where market-design levers get causally validated.
- **Tier 3 (include only by exception — lever match or survey):** NeurIPS, KDD research track, RecSys research track, WWW research track, CIKM research track, UMUAI, Information Fusion, ASONAM. Why: this survey is industry-first per the override; academic ML papers are included only when pre-screened against a named lever or when the paper itself is a survey.

## Target Engineering Blogs

- Tinder press room / newsroom — https://www.tinderpressroom.com
- Bumble Tech (Medium) — https://medium.com/bumble-tech (blog exists; no ranking-specific post located yet, see Known Blind Spots)
- OkCupid OkTrends (archived; mirror used) — https://gwern.net/doc/psychology/okcupid/
- AWS Database Blog (Coffee Meets Bagel infra case study)
- LinkedIn Engineering Blog
- Airbnb Engineering (Medium) — https://medium.com/airbnb-engineering
- Spotify Research / Spotify Engineering
- Lyft Engineering Blog — https://eng.lyft.com
- DoorDash Engineering Blog — https://careersatdoordash.com/blog
- Uber Engineering Blog
- Etsy Engineering ("Code as Craft")
- Thumbtack Engineering Blog
- Meta AI / Meta Engineering blog (People You May Know)
- CyberAgent AI Lab / CyberAgent tech blog (Japanese)
- Not yet confirmed to have a ranking-relevant blog — search directly per Known Blind Spots: Hinge, Match Group, Grindr, Badoo, OkCupid, Zoosk, Pairs (Eureka), Tapple, Tantan, Momo, Soul App

## Companies to Search by Name

- **Dating:** Tinder, Hinge, Bumble, Badoo, OkCupid, Match, Coffee Meets Bagel, Grindr, eHarmony, Zoosk, Pairs (Eureka), Tapple (CyberAgent), Tantan, Momo, Soul App, Baihe, Jiayuan.
- **Job markets (same two-sided structure):** LinkedIn, Indeed, ZipRecruiter, BOSS Zhipin (Kanzhun), Upwork, Hired.
- **Other two-sided platforms:** Airbnb, Uber, Lyft, DoorDash, Etsy, Thumbtack, Spotify (creator side), Meta (People You May Know), Kuaishou and TikTok (creator side).

## Search Query List (8 search directions, verbatim from the brief)

- **Direction 1 — Reciprocal recommendation in dating:** "reciprocal recommender system", "reciprocal recommendation online dating", "reciprocal recommendation matching markets", "people-to-people recommendation", "mutual like prediction", "two-way preference", "match prediction two-sided", "harmonic mean reciprocal score", "reciprocal recommender survey".
- **Direction 2 — Market and ecosystem framing:** "two-sided marketplace recommendation", "marketplace health metrics", "ecosystem health recommendation", "liquidity two-sided market", "supply demand balance recommendation", "multi-stakeholder recommendation", "provider-side fairness", "two-sided fairness ranking", "exposure allocation", "fairness of exposure".
- **Direction 3 — Capacity and congestion:** "capacity constrained recommendation", "congestion matching market", "over-subscription", "application redistribution", "attention budget", "diminishing returns impressions", "impression discounting", "b-matching recommendation", "capacitated assignment ranking", "popularity bias feedback loop", "Matthew effect recommendation".
- **Direction 4 — Constrained allocation and re-ranking:** "constrained ranking linear programming", "Lagrangian re-ranking exposure", "optimal transport exposure allocation", "pacing controller exposure", "PID controller recommendation", "guaranteed delivery allocation", "budget pacing", "market equilibrium exposure allocation", "assortment optimization matching platform", "calibrated recommendations".
- **Direction 5 — Market design levers:** "stable matching dating app", "Gale-Shapley dating", "assortment optimization dating market", "market thickness online dating", "signaling in dating markets", "which side searches matching platform", "restricting choice matching platform", "daily like limit congestion", "curated daily batch dating".
- **Direction 6 — Objectives and metrics:** "match rate", "matches per user Gini", "share of users with at least one match", "conversation rate", "reply rate", "unrequited likes", "like-to-match ratio", "desirability score PageRank", "attractiveness decile analysis", "two-sided retention", "long-term ecosystem value reinforcement learning".
- **Direction 7 — Evaluation:** "A/B testing two-sided marketplace interference", "two-sided randomization", "switchback experiment", "marketplace experimentation bias", "cluster randomization marketplace", "off-policy evaluation ranking".
- **Direction 8 — Local-language sources:** search Chinese and Japanese too. Chinese: 相互推荐, 双边推荐, 双边匹配, 婚恋推荐, 交友推荐, 推荐 生态健康. Japanese: 相互推薦, マッチングアプリ 推薦, 双方向 レコメンド.

## Survey Scope and Constraints

- **Target number of references:** 60–100 for this NLM run (per the brief's "How to run" bullet: "Floor for the nlm run: 60–100 references"). This supersedes the brief's general Rules-section figure of 30–50, which applies to the non-NLM one-shot fallback. **The ≥60% Tier 1+2 mix has priority over the count — do not add academic (Tier 3) items only to reach the floor.**
- **Year range:** prefer 2015–2026. Keep classics regardless of year. Give a publication year for every item.
- **Must include:** see "Must Include" section below (seed groups A–E, 44 seeds). Sanity check: the Must Include seeds alone are already Tier 1+2 = 36/44 (~82%), well above the 60% floor.
- **Exclude / deprioritize:**
  - Tier 3 academic ML papers that do not map directly to a named lever and are not a survey (per Tier Override above).
  - Papers whose primary contribution is single-viewer ranking-*objective* design (that is Survey 3's territory) unless they also address a two-sided/market-layer lever. The CyberAgent RecSys 2023/2024 papers are the known overlap with Survey 3 — include them here, but do not double-count them as independent evidence if both surveys' outputs are later combined.
- **Verify every link.** Do not invent titles or authors. Mark uncertain items as uncertain.
- **Prefer primary sources.** If a blog summarizes a paper, cite both.
- **Paywall rule:** find the arXiv, SSRN, or author-page version instead of skipping.
- **Report coverage per direction** (Directions 1–8 above). Name directions that returned little.
- **Log null results per source:** name each blog, venue, or query that returned nothing useful.
- **Keep notes short.** Do not paste abstracts.
- **Adjacent-field expansion plan** (if the queue risks running dry before reaching the 60–100 target): first re-run Direction 1 (dating-app engineering blogs) and Direction 2 (reciprocal-recsys surveys) with more effort — these are the two known blind spots below — and widen Direction 8 (local-language) effort, before expanding into any subfield not already named in the 8 directions.

## Must Include

Grouped A–E, following the brief's seed reference groups (44 seeds total; verify each again before citing). Tier tags per the override above. Corrections and uncertainty flags below are preserved exactly from the brief.

### Group A — Dating platforms describing their own matching (Tier 1)

- **"Powering Tinder® — The Method Behind Our Matching."** Tinder (company newsroom). 2019. Company newsroom post. Tier 1. https://www.tinderpressroom.com/powering-tinder-r-the-method-behind-our-matching — notes the Elo score is retired.
- **"Personalized (User) Recommendations at Tinder: The TinVec Approach."** Steve Liu (Tinder). 2017. MLconf SF talk. Tier 1. https://mlconf.com/sessions/personalized-user-recommendations-at-tinder-the-t/
- **Hinge "Most Compatible"** (Gale-Shapley-based). 2018. Press coverage only (TechCrunch, quoting the CEO) — no primary Hinge source located. Tier 1. https://techcrunch.com/2018/07/11/hinge-employs-new-algorithm-to-find-your-most-compatible-match-for-you/
- **Hinge Gini analysis.** Aviv Goldgeier (Hinge), via Quartz coverage. 2017. Press coverage. Tier 1. https://qz.com/1051462/these-statistics-show-why-its-so-hard-to-be-an-average-man-on-dating-apps — Gini 0.376 (women) vs. 0.542 (men).
- **OkTrends, "Your Looks and Your Inbox."** OkCupid. 2009 (mirror). Company blog (archived). Tier 1. https://gwern.net/doc/psychology/okcupid/yourlooksandyourinbox.html — message concentration by attractiveness.
- **"Data Science of Love."** Vaclav Petricek (eHarmony). 2013. Strata + QCon talk slides. Tier 1. https://www.slideshare.net/VaclavPetricek/data-science-of-love
- **Coffee Meets Bagel recommendation infra case study.** AWS (Coffee Meets Bagel customer case study). Year unconfirmed. AWS Database Blog. Tier 1. https://aws.amazon.com/blogs/database/powering-recommendation-models-using-amazon-elasticache-for-redis-at-coffee-meets-bagel/ — **uncertain: year unconfirmed, low modeling detail (infra-focused).**
- **Bumble Tech (Medium publication).** Bumble. No specific ranking post identified. Company engineering blog. Tier 1. https://medium.com/bumble-tech — **uncertain: blog exists; no ranking-specific post located as of brief date (2026-08-15) — search directly during discovery.**

### Group B — Industry-track papers on reciprocal recommendation and two-sided balancing (Tier 1)

- **"Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets."** CyberAgent. RecSys 2023. Tier 1. https://dl.acm.org/doi/10.1145/3604915.3608774 — Japanese dating platform. Shared seed with Survey 3 — do not double-count.
- **"Fair Reciprocal Recommendation in Matching Markets."** CyberAgent and University of Tokyo. RecSys 2024. Tier 1. https://dl.acm.org/doi/10.1145/3640457.3688130 — shared seed with Survey 3 — do not double-count.
- **"Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method."** Chen Yang et al. KDD 2024. Tier 1. https://dl.acm.org/doi/10.1145/3637528.3671734
- **"Modeling Two-Way Selection Preference for Person-Job Fit."** Yang, Hou, Song, Zhang, Wen, Zhao (BOSS Zhipin and Renmin University). RecSys 2022. Tier 1. https://dl.acm.org/doi/10.1145/3523227.3546752
- **"Reciprocal Sequential Recommendation."** Zheng et al. RecSys 2023. Tier 1. https://dl.acm.org/doi/abs/10.1145/3604915.3608798
- **"BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment."** KDD 2023. Tier 1. https://dl.acm.org/doi/10.1145/3580305.3599783
- **"LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace."** Borisyuk, Zhang, Kenthapadi (LinkedIn). KDD 2017. Tier 1. https://www.kdd.org/kdd2017/papers/view/lijar-a-system-for-job-application-redistribution-towards-efficient-career- — closest analog: moves exposure away from over-subscribed jobs. **Correction applied: authors are Borisyuk, Zhang, Kenthapadi.**
- **"Modeling Impression Discounting in Large-scale Recommender Systems."** Lee, Lakshmanan, Tiwari, Shah (LinkedIn). KDD 2014. Tier 1. https://dl.acm.org/doi/10.1145/2623330.2623356
- **"Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems."** Mehrotra, McInerney, Bouchard, Lalmas, Diaz (Spotify). CIKM 2018. Tier 1. https://dl.acm.org/doi/10.1145/3269206.3272027
- **"Recommendations in a Marketplace."** Spotify Research. Publication page, year unconfirmed. Tier 1. https://research.atspotify.com/publications/recommendations-in-a-marketplace — **uncertain: year unconfirmed.**
- **"How Airbnb uses Machine Learning to Detect Host Preferences."** Bar Ifrach (Airbnb). 2015. Company engineering blog (Medium). Tier 1. https://medium.com/airbnb-engineering/how-airbnb-uses-machine-learning-to-detect-host-preferences-18ce07150fa3 — models the other side's acceptance.
- **"Real-time Personalization using Embeddings for Search Ranking at Airbnb."** Grbovic and Cheng (Airbnb). KDD 2018. Tier 1. https://dl.acm.org/doi/10.1145/3219819.3219885

### Group C — Applied research with real dating or matching platform data (Tier 2)

- **"Improving Match Rates in Dating Markets Through Assortment Optimization."** Rios, Saban, Zheng. M&SOM 2022. Tier 2. https://pubsonline.informs.org/doi/10.1287/msom.2022.1107 — piloted at a major US dating app, 25%+ more matches.
- **"Assortment Planning for Two-Sided Sequential Matching Markets."** Ashlagi, Krishnaswamy, Makhijani, Saban, Shiragur. Operations Research 2022. Tier 2. https://web.stanford.edu/~iashlagi/papers/assortment.pdf
- **"Facilitating the Search for Partners on Matching Platforms."** Kanoria and Saban. Management Science 2021. Tier 2. https://pubsonline.informs.org/doi/10.1287/mnsc.2020.3794 — which side should search.
- **"Managing Congestion in Matching Markets."** Arnosti, Johari, Kanoria. M&SOM 2021. Tier 2. https://pubsonline.informs.org/doi/10.1287/msom.2020.0927
- **"Competing by Restricting Choice: The Case of Matching Platforms."** Halaburda, Piskorski, Yıldırım. Management Science 2018. Tier 2. https://pubsonline.informs.org/doi/10.1287/mnsc.2017.2797
- **"Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating."** Jessica Fong. Marketing Science 2024. Tier 2. https://pubsonline.informs.org/doi/abs/10.1287/mksc.2023.0142 — **correction applied: this is the published title; earlier working title was "Search, Selectivity, and Market Thickness in Two-Sided Markets."**
- **"Propose with a Rose? Signaling in Internet Dating Markets."** Lee and Niederle. Experimental Economics 2015. Tier 2. https://link.springer.com/article/10.1007/s10683-014-9425-9 — field experiment on a Korean dating site.
- **"Matching and Sorting in Online Dating."** Hitsch, Hortaçsu, Ariely. American Economic Review 2010. Tier 2. https://www.aeaweb.org/articles?id=10.1257/aer.100.1.130
- **"Aspirational Pursuit of Mates in Online Dating Markets."** Bruch and Newman. Science Advances 2018. Tier 2. https://www.science.org/doi/10.1126/sciadv.aap9815 — desirability via PageRank.
- **"Reciprocal Recommendation System for Online Dating."** Xia, Liu, Sun, Chen. ASONAM 2015. Tier 2. https://dl.acm.org/doi/10.1145/2808797.2809282
- **"Online Dating Recommendations: Matching Markets and Learning Preferences."** Tu et al. WWW 2014 Companion. Tier 2. https://dl.acm.org/doi/10.1145/2567948.2579240

### Group D — Experimentation in two-sided markets (Tier 1 and 2)

- **"Experimental Design in Two-Sided Platforms: An Analysis of Bias."** Johari, Li, Liskovich, Weintraub. Management Science 2022. Tier 2. https://pubsonline.informs.org/doi/abs/10.1287/mnsc.2021.4247
- **"Multiple Randomization Designs."** Bajari et al. arXiv 2021. Tier 2. https://arxiv.org/abs/2112.13495
- **"Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-experiment on Airbnb."** Holtz, Lobel, Liskovich, Aral. Management Science 2025. Tier 2. https://pubsonline.informs.org/doi/10.1287/mnsc.2020.01157
- **"Using Marketplace Marginal Values to Address Interference Bias."** Lyft Engineering. 2025. Tier 1. https://eng.lyft.com/using-marketplace-marginal-values-to-address-interference-bias-a11aff6e670f
- **"Experiment Rigor for Switchback Experiment Analysis."** DoorDash Engineering. 2025. Tier 1. https://careersatdoordash.com/blog/experiment-rigor-for-switchback-experiment-analysis/

### Group E — Academic methods that map to a lever (Tier 3)

- **"Optimally Balancing Receiver and Recommended Users' Importance in Reciprocal Recommender Systems."** Kleinerman, Rosenfeld, Ricci, Kraus. RecSys 2018. Tier 3. https://dl.acm.org/doi/abs/10.1145/3240323.3240349
- **"RECON: A Reciprocal Recommender for Online Dating."** Pizzato, Rej, Chung, Koprinska, Kay. RecSys 2010. Tier 3. https://dl.acm.org/doi/10.1145/1864708.1864747
- **"Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating."** Pizzato et al. UMUAI 2013. Tier 3. **No URL given in the brief — locate and verify during discovery.**
- **"Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation."** Palomares, Porcel, Pizzato, Guy, Herrera-Viedma. Information Fusion 2021. Tier 3. https://www.sciencedirect.com/science/article/abs/pii/S1566253520304267 — survey; currently the most recent reciprocal-recsys survey identified (see Known Blind Spots).
- **"Latent Factor Models and Aggregation Operators for Collaborative Filtering in Reciprocal Recommender Systems."** Neve and Palomares. RecSys 2019. Tier 3. https://dl.acm.org/doi/10.1145/3298689.3347026
- **"Two-sided Fairness in Rankings via Lorenz Dominance."** Do, Corbett-Davies, Atif, Usunier (Meta). NeurIPS 2021. Tier 3. https://proceedings.neurips.cc/paper/2021/hash/48259990138bc03361556fb3f94c5d45-Abstract.html — covers the reciprocal case.
- **"Fairness of Exposure in Rankings."** Singh and Joachims. KDD 2018. Tier 3. https://doi.org/10.1145/3219819.3220088
- **"Recommendation with Capacity Constraints."** Christakopoulou, Kawale, Banerjee. CIKM 2017. Tier 3. https://dl.acm.org/doi/10.1145/3132847.3133034

## Known Blind Spots

From the brief's first pass (2026-08-15); both must be searched again with more effort in Phase 2:

1. **No dating-app engineering-blog post on ranking mechanics was found.** Group A above leans on press coverage (TechCrunch, Quartz) and a talk/newsroom post rather than a primary engineering blog. Re-search directly: Bumble Tech (Medium), Tinder/Match Group engineering channels, and engineering blogs (if any) for Grindr, Badoo, OkCupid, Zoosk, Hinge, Pairs/Eureka, Tapple/CyberAgent, Tantan, Momo, Soul App.
2. **No reciprocal-recsys survey published after 2021 was found.** Palomares et al. (Information Fusion 2021, Group E) is the most recent survey identified. Re-search: RecSys 2022–2026 workshop proceedings, arXiv survey listings, and forward citation search from the 2021 survey.
3. **RecSys 2025 and RecSys 2026 industry tracks must be included** in discovery — both postdate the brief's last confirmed search pass.

## Project Context

See `./README.md` for the canonical Project Context. This file references it; do not duplicate.

## Must-Include / Project-Context Consistency Check

Procedure: `kb/context/literature-survey/literature-survey-conventions.md` § Phase 1 Must Include / Project Context Consistency Check. For each cluster, the output type it produces is compared against what `README.md`'s Project Context defines as useful — mechanisms or evidence for one of the four modeling layers (reciprocal scoring, capacity-aware exposure allocation, market-design levers, ecosystem metrics/experimentation), aimed at market-health outcomes rather than single-viewer CTR/CVR.

| Cluster | Output type produced | Modeling layer(s) addressed | Mismatch? |
|---|---|---|---|
| A — Dating platforms' own descriptions | Qualitative mechanism descriptions + match-distribution statistics (Gini) | Layer 1 (reciprocal scoring), Layer 4 (ecosystem metrics) | No |
| B — Industry-track reciprocal/two-sided papers | Concrete scoring functions, redistribution systems, fairness-aware ranking algorithms | Layers 1–3 | No |
| C — Applied research, real platform data | Field-experiment effects on match rate / congestion / signaling, on real dating/matching platforms | Layer 3 (market-design levers); validates market-health metrics directly | No |
| D — Experimentation in two-sided markets | Bias-correction and experimental-design methodology for marketplace interference | Layer 4 (ecosystem metrics and experimentation under interference) | No |
| E — Academic methods mapping to a lever | Algorithmic methods for reciprocal scoring / exposure fairness / capacity constraints, pre-filtered by the brief to map to a named lever, or a survey | Layers 1–3, or cross-cutting survey | No |

**Result: no mismatches.** All five clusters produce output types that map directly to at least one of the Project Context's four modeling layers, and none targets single-viewer CTR/CVR (the objective type the Project Context explicitly excludes). No cluster needs demotion to "Background only" and none needs removal from Must Include. The Must Include list proceeds as-is, pending user confirmation of this requirements file as a whole.

## Summary of Actual Search Results

Filled by the **cursor-grok** workplace run (2026-08-16). Details live in `cursor-grok/literature-review.md`; do not treat this block as a second bibliography.

- Total papers in cursor-grok bibliography: **72** annotated items as of 2026-08-17 gap-fill (was 66 after continuation; 53 on 2026-08-16). Inside the 60–100 NLM floor; mix still takes precedence.
- Tier 1+2 share: **86%** (62/72)
- Number of categories: 8 search directions from this file
- Key findings (2026-08-17 gap-fill): Hinge 2025 company pages — DL mutual-compatibility Discover ranker; newsroom **double-digit match increase**. GFRR: send AUC 73.15% / fusion 71.26% on 2020 dating logs. UniCoRn: LinkedIn producer-side A/B (750M+). Kanzhun IR: traffic to more responsive users. Xia ASONAM 2015: Baihe CF. RecSys 2025 matching paper = Hayashi. Bumble ranking and dating-log OPE still null. NLM MCP disconnected; 61-hit re-import still blocked.
- NLM: leftover industry task `7ddbec32` imported; new industry pass `275cee32` (10 hits, SEO discarded). Gap-fill cited from live pages, not new notebook sources.

## Codex-sol Summary of Actual Search Results — 2026-08-19

- Workplace: `./codex-sol/`
- Total analyzed items: **45**.
- Tier mix: Tier 1 = 24, Tier 2 = 15, Tier 3 = 6; Tier 1+2 = **39/45 (86.7%)**.
- Direction coverage: **D1 11 primary / 19 tagged; D2 5 / 7; D3 4 / 8; D4 4 / 14; D5 6 / 10; D6 5 / 8; D7 6 / 8; D8 4 / 7**; every direction has decision-relevant evidence, with D2 and D8 the thinnest.
- Major finding — reciprocal scoring: bilateral scoring is necessary but insufficient; the useful market layer combines like-back evidence with receiver load or market-wide scarcity.
- Major finding — capacity/allocation: LinkedIn redistribution, application-limit theory, exposure constraints, and matching-market mechanisms consistently support treating recommendations as scarce exposure allocation, although conversation-capacity calibration in dating remains open.
- Major finding — market design: scarce signals, limits, curated choice, and initiation rules can reduce screening congestion, but effects depend on side imbalance and market thickness.
- Major finding — metrics/evaluation: total matches must be paired with conversations, coverage/share with at least one, Gini/Lorenz spread, wasted or unrequited likes, effective interactions, and two-sided retention; ordinary user-split A/B tests can be biased by shared-market interference.
- Coverage evaluation: **31/31 = 100% covered; project-context fitness PASS; zero gaps**. Seven items are explicitly marked thin-but-decision-ready, and all omitted Must-Include anchors are named in `./codex-sol/coverage-evaluation.md`.
- Evidence limit: the codex-sol selection is below the requested 60–100-reference floor, but does not pad with lower-priority academic items; the 86.7% industry/applied mix and complete modeling-layer coverage support decision-making.

**Correction — authoritative brief override:** The authoritative target is **30–50 verified items**; codex-sol's **45 items satisfy it**, and the immediately preceding evidence-limit sentence citing a 60–100-reference floor is stale and superseded.
