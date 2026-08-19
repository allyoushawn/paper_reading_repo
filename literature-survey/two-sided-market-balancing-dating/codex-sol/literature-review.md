Date: 2026-08-19
Topic: two-sided market balancing in dating-app recommendation: reciprocal recommendation, exposure allocation under capacity limits, congestion in matching markets
Paper count: 45

# Two-Sided Market Balancing in Dating-App Recommendation — Literature Review

## Synthesis

The evidence supports a layered market system rather than a single replacement ranker: estimate bilateral interest, discount or budget scarce recipient capacity, allocate exposure under explicit constraints, and evaluate the whole market under interference. The strongest direct dating evidence comes from reciprocal scoring and matching-theoretic systems, while the strongest production capacity controls come from adjacent job and spot-work markets. Effects are not directly comparable because outcomes range from expected matches and acceptance to entropy, welfare, exposure, and retention.

### Design patterns

1. **Score both directions before allocating exposure.** *Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating* raises S@10 from 23.00% unilateral to 42.20% with harmonic bilateral scoring; *Modeling Two-Way Selection Preference for Person-Job Fit* and *BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment* extend the pattern with separate active/passive representations and funnel stages.
2. **Represent overload as a recipient-specific state, not just popularity.** *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace* forecasts demand and shifts applications +6.5% toward underserved jobs and -8.7% from overserved jobs while raising entropy 12%; *Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach* budgets expected inbound likes or effective dates.
3. **Use market-clearing discounts when individual scores create superstar congestion.** *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets* combines mutual preference with transferable-utility outside-option factors and improves expected matches over reciprocal and unilateral comparators while reducing concentration.
4. **Constrain the slate globally when local scores cannot enforce spread.** *Fairness of Exposure in Rankings*, *Joint Multisided Exposure Fairness for Recommendation*, and *Fair Reciprocal Recommendation in Matching Markets* optimize stochastic exposure matrices; the last reduces envy sharply but sacrifices match volume.
5. **Treat product rules as market-design instruments.** *Managing Congestion in Matching Markets* supports application caps; *Propose with a Rose? Signaling in Internet Dating Markets* reports a +3.3 percentage-point acceptance effect; *Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions* and *Competing by Restricting Choice* show when directional search or curated menus reduce rejection competition.
6. **Optimize downstream mutual outcomes, not likes alone.** *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method* reranks vacant or redundant slots for distinct matched pairs; *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching* instead values marginal two-sided retention, though its indexed source gives no numeric lift.
7. **Measure distribution and causal spillovers alongside throughput.** Entropy, Gini/Lorenz curves, coverage, unrequited-contact rates, effective dates, and side-specific retention reveal whether matches are concentrated; UniCoRn, two-sided randomization, cluster randomization, multiple randomization, shadow prices, and matching-market OPE address different interference or logging problems.

## Design-pattern matrix

### reciprocal scoring

| Pattern | *Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating* | *Modeling Two-Way Selection Preference for Person-Job Fit* | *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets* | *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method* |
|---|---|---|---|---|
| reciprocal scoring | Harmonic aggregation suppresses pairs with weak reverse preference; S@10 is 42.20% versus 23.00% unilateral. | Separate active and passive graph roles learn outgoing taste and incoming appeal before combining directions. | Transferable-utility outside-option factors add market-wide demand pressure to bilateral preference. | Bilateral causal outcomes and vacant-slot reranking target distinct matched pairs rather than two independent clicks. |

### capacity-aware scoring

| Pattern | *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace* | *Matching Theory-Based Recommender Systems in Online Dating* | *Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach* | *Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform* |
|---|---|---|---|---|
| capacity-aware scoring | Forecast end-of-horizon demand, relevance-gate boosts, and exponentially throttle overdelivery. | Equilibrium unmatched-probability factors discount capacity-saturated dating users; source reports no outcome magnitude. | Receiver budgets cap expected inbound likes or dates and score congestion-adjusted effective dates. | Stateful eligibility uses vacancy/capacity and past exposure to suppress popular capacity-poor options. |

### constrained re-ranking

| Pattern | *Fairness of Exposure in Rankings* | *Joint Multisided Exposure Fairness for Recommendation* | *Fair Reciprocal Recommendation in Matching Markets* | *Two-Sided Fairness in Rankings via Lorenz Dominance* |
|---|---|---|---|---|
| constrained re-ranking | Linear-programmed stochastic rankings enforce exposure or impact ratios with small job-example DCG cost. | Joint consumer–producer exposure objectives improve GG-F with nonsignificant NDCG loss. | Alternating Nash-social-welfare optimization reduces two-sided envy while trading off expected matches. | Concave welfare redirects exposure toward worse-off users while retaining generalized-Lorenz efficiency. |

### market-design lever

| Pattern | *Managing Congestion in Matching Markets* | *Propose with a Rose? Signaling in Internet Dating Markets* | *Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions* | *Competing by Restricting Choice: The Case of Matching Platforms* |
|---|---|---|---|---|
| market-design lever | Application caps protect recipient screening capacity and can benefit both sides in the mean-field model. | Scarce roses prioritize serious proposals; acceptance rises 3.3 percentage points. | Assign initiation to the side with the appropriate scarcity and screening-cost position to reduce rejected search. | Smaller curated menus lower same-side competition and rejection, but live match effects are not specified. |

### ecosystem metrics

| Pattern | *Your Looks and Your Inbox* | *Matching and Sorting in Online Dating* | *LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace* | *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method* |
|---|---|---|---|---|
| ecosystem metrics | Attractiveness-stratified message share and reply rate expose receiver overload and diminishing reciprocal value. | Unrequited-contact and contact-to-match conversion quantify wasted proposals by side. | Demand-bucket counts and application entropy measure redistribution without hiding total-volume loss. | CRecall/CPrecision and distinct true-positive pairs measure reciprocal outcomes across the whole recommendation set. |

### evaluation method

| Pattern | *Experimental Design in Two-Sided Platforms: An Analysis of Bias* | *A/B Testing for Recommender Systems in a Two-Sided Marketplace* | *Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization* | *Off-Policy Evaluation and Learning for Matching Markets* | *Reducing Marketplace Interference Bias Via Shadow Prices* |
|---|---|---|---|---|---|
| evaluation method | Two-sided randomization and bias corrections use cross-cells to estimate cannibalization. | UniCoRn preserves producer treatment assignments while merging counterfactual ranks in shared feeds. | Demand-embedding clusters keep close substitutes in one treatment cell; Airbnb measured 19.76% interference bias. | DiPS/DPR decompose request and response to stabilize sparse reciprocal OPE, but do not model interference. | Dual prices value contention for shared capacity and reduce simulated RCT bias in centrally allocated markets. |

## Foundational methods and direct baselines

The strict card-based baseline audit identifies only three recurring direct-comparator chains: DPGNN is a named comparator in *Reciprocal Sequential Recommendation* and *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method*; transferable-utility ranking is a comparator in *Fair Reciprocal Recommendation in Matching Markets*; and RECON is a comparator in *Reciprocal Recommendation System for Online Dating*. Explicit extensions or reproductions are also limited: *Joint Multisided Exposure Fairness for Recommendation* extends exposure-fairness formulations, and *An Attempt to Personalize Preference Aggregation in Reciprocal Recommendation* reproduces personalized weighted-harmonic aggregation. Other “foundational” labels in NotebookLM Query 4 are treated as synthesis or citation influence, not baseline counts.

## Read-first: top 10 by expected design value

1. **Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach** — the closest end-to-end dating implementation of reciprocal funnel prediction, receiver budgets, effective-date scoring, and field evaluation.
2. **LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace** — the clearest production blueprint for forecasting overdelivery and redistributing exposure with a relevance floor.
3. **Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets** — a scalable market-clearing reciprocal scorer with dating data and explicit match and concentration evidence.
4. **Managing Congestion in Matching Markets** — the cleanest mechanism for why unrestricted likes overload recipients and when caps improve both sides.
5. **Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method** — supplies market-level reciprocal metrics and reranking for distinct matches rather than unilateral accuracy.
6. **A/B Testing for Recommender Systems in a Two-Sided Marketplace** — a deployed producer-side experimental design that measures receiver-retention ranking without inconsistent shared feeds.
7. **Fair Reciprocal Recommendation in Matching Markets** — quantifies the match-volume versus two-sided-envy frontier on dating data.
8. **Propose with a Rose? Signaling in Internet Dating Markets** — dating-native randomized evidence for a scarce signal that helps recipients prioritize.
9. **Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating** — field and structural evidence that perceived thickness and like caps change selectivity and matches by side.
10. **Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb** — direct meta-experimental evidence that ordinary marketplace A/B estimates can be materially biased.

## Gaps and open questions

- No selected field study jointly estimates like-back probability, individual reply or conversation capacity, exposure allocation, and two-sided retention in one dating system.
- Capacity is variously a hard budget, forecasted demand target, vacancy, or equilibrium outside option; calibration to actual reply or conversation capacity remains unresolved.
- Most dating papers report offline matches, expected matches, or short-run acceptance, while conversation quality, delayed replies, sender trust, and two-sided retention are rarely measured together.
- Fairness, congestion reduction, and total match quality often trade off, but the corpus does not establish a portable operating point across market imbalance and activity regimes.
- Logged-policy OPE handles sparse two-stage rewards, whereas interference-aware designs handle cross-user spillovers; a validated method combining both for reciprocal dating is absent.
- Symmetric dating markets are poorly represented in causal marketplace experimentation compared with listings, jobs, and centrally allocated supply.

### Exactly the next 5 searches

1. dating app receiver reply capacity conversation capacity reciprocal ranking field experiment
2. forward citations “Reciprocal Recommender Systems” 2021 RecSys 2022 2023 2024 2025 2026 survey
3. Tapple Pairs Tinder Hinge Bumble Match engineering congestion exposure allocation like limits reciprocal recommendation
4. symmetric matching market experiment interference cluster randomization switchback dating
5. two-sided retention effective dates conversation quality capacity-constrained reciprocal recommendation

## Coverage, tier mix, and discovery nulls

| Direction | Primary-group entries | Multi-tag coverage | Assessment |
|---|---:|---:|---|
| D1 reciprocal recommendation | 11 | 19 | Strongest area; includes dating, recruitment, surveys, and local-language work. |
| D2 market and ecosystem framing | 5 | 7 | Covered, but thinner and often fairness rather than hard capacity. |
| D3 capacity and congestion | 4 | 8 | Small but high-value set spanning forecasts, caps, and capacity penalties. |
| D4 constrained allocation and re-ranking | 4 | 14 | Broad via cross-tags; direct dating field evidence remains limited. |
| D5 market-design levers | 6 | 10 | Strong dating and theory mix: caps, signaling, menu size, initiation side. |
| D6 objectives and ecosystem metrics | 5 | 8 | Good diagnostics; direct two-sided retention magnitude is sparse. |
| D7 evaluation | 6 | 8 | Strong adjacent-market evidence; symmetric dating interference remains open. |
| D8 Chinese and Japanese | 4 | 7 | Japanese industry evidence is useful; official Chinese dating engineering evidence is thin. |

Tier mix is **Tier 1 = 24, Tier 2 = 15, Tier 3 = 6**, so Tier 1+2 is **39/45 (86.7%)**, above the 60% target.

Named null or low-yield results from discovery: Bumble Tech had no ranking or mechanics post; no general reciprocal-recommender survey newer than Palomares et al. (2021) was found; RecSys 2026 had no public accepted-contributions list at search time; no new primary ranking-mechanics post was found for Badoo, Bumble, Match Group outside Tinder and Hinge, Grindr, eHarmony, Zoosk, Tantan, Momo, Soul, Baihe, or Jiayuan; official Chinese dating engineering searches for Tantan, Momo, Soul, Baihe, and Jiayuan were null; the local Awesome repository yielded no new core paper after deduplication; and Upwork, Hired, Etsy, and Meta/PYMK yielded no new high-fit source beyond already indexed material.

## Limitations and confidence

Confidence is highest for primary papers and production or field experiments with explicit numbers, moderate for theoretical transfers from jobs, spot work, music, travel, or ride-hailing, and lowest for consumer-facing explainers or secondhand effects. Proprietary datasets, heterogeneous metrics, different capacity definitions, and market interference prevent pooled effect sizes. Several sources provide mechanisms without quantitative outcomes; those entries say Not specified rather than treating absence as a null. NotebookLM outputs cover 143 notebook sources and therefore include material outside this selected 45-card bibliography; every cross-paper claim retained here is constrained to the own-card evidence below.

## Annotated bibliography (45 references; each card linked exactly once)


## D1 — Reciprocal recommendation in dating (11)

### [Powering Tinder® — The Method Behind Our Matching](./read-papers/2019_Tinder_NA_Powering-Tinder-Matching.md)

**Full title:** Powering Tinder® — The Method Behind Our Matching  
**Authors/org:** Tinder  
**Year:** 2019  
**Venue/type:** Tinder Newsroom; company product explainer  
**Verified link:** https://www.tinderpressroom.com/powering-tinder-r-the-method-behind-our-matching  
**Tier:** 1  
**What they did:** Tinder publicly described its post-Elo profile-ordering signals: simultaneous activity, proximity, eligibility preferences, declared interests, anonymized photo similarity, and Like/Nope feedback. It frames the system around timely matches and conversations but does not disclose architecture or evaluation.  
**Two-sided mechanism:** Simultaneous activity and reverse photo-similarity targeting make exposure more likely to reach a currently available, plausibly interested counterpart; no explicit reciprocal probability or capacity constraint is given.  
**Metrics and reported effect:** Not specified in source.  
**Dating fit:** Low — direct product relevance, but no capacity allocation or measured market-health effect.  
**Confidence real/correct:** High — primary Tinder source; claims are limited to what the page explicitly discloses.

### [Personalized (User) Recommendations at Tinder: The TinVec Approach](./read-papers/2017_MLconf_TinVec_Personalized-User-Recommendations-Tinder.md)

**Full title:** Personalized (User) Recommendations at Tinder: The TinVec Approach  
**Authors/org:** Steve Liu, Tinder  
**Year:** 2017  
**Venue/type:** MLconf San Francisco; industry conference talk  
**Verified link:** https://mlconf.com/sessions/personalized-user-recommendations-at-tinder-the-t/  
**Tier:** 1  
**What they did:** TinVec adapts Skip-gram Word2Vec to co-swipes. It embeds profiles liked in similar contexts near one another, averages the embeddings of profiles a member liked into a taste vector, and retrieves nearby candidates.  
**Two-sided mechanism:** The source learns only the viewer-to-shown-user direction. It can supply one directional preference representation, but does not estimate like-back probability or allocate exposure by receiver capacity.  
**Metrics and reported effect:** Offline swipe prediction: 90% AUROC and 85% F1; no baseline lift reported.  
**Dating fit:** Medium — useful Layer-1 representation, but unilateral and capacity-blind.  
**Confidence real/correct:** High — primary MLconf page and ingested talk slides; missing evaluation details are explicitly marked.

### [Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets](./read-papers/2023_RecSys_TU_Fast-Examination-Agnostic-Reciprocal.md)

**Full title:** Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets  
**Authors/org:** Yoji Tomita, Riku Togashi, Yuriko Hashizume, Naoto Ohsaka; CyberAgent  
**Year:** 2023  
**Venue/type:** RecSys 2023; conference paper  
**Verified link:** https://arxiv.org/abs/2306.09060  
**Tier:** 1  
**What they did:** They derive a reciprocal ranker from stochastic transferable-utility matching, solve equilibrium outside-option factors with IPFP, and encode the resulting market-balanced score as an augmented Two-Tower dot product for MIPS serving.  
**Two-sided mechanism:** Bilateral preference is combined with market-clearing outside-option factors. High demand reduces a user's equilibrium scaling factor, redistributing recommendation opportunity while keeping retrieval efficient.  
**Metrics and reported effect:** Synthetic n=100: 152.39 expected matches vs. 129.82 reciprocal and 106.45 unilateral; Gini 0.3416/0.1019. Dating 1,000x1,000: 538.97/386.64 vs. reciprocal 491.12/360.05.  
**Dating fit:** High — directly targets reciprocal congestion and exposure spread with real dating data.  
**Confidence real/correct:** High — primary paper and venue record; numerical claims come from source-scoped NotebookLM extraction.

### [Fair Reciprocal Recommendation in Matching Markets](./read-papers/2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md)

**Full title:** Fair Reciprocal Recommendation in Matching Markets  
**Authors/org:** Yoji Tomita (CyberAgent), Tomohiko Yokoyama (The University of Tokyo)  
**Year:** 2024  
**Venue/type:** RecSys 2024; conference paper  
**Verified link:** https://arxiv.org/abs/2409.00720  
**Tier:** 1  
**What they did:** They define two-sided envy-freeness over recommendation opportunity and optimize probabilistic rankings using alternating Nash-social-welfare maximization. The method sacrifices some match volume to nearly eliminate envy on both sides.  
**Two-sided mechanism:** Joint like probabilities determine match utility; doubly stochastic exposure matrices are optimized on both sides, and a multiplicative welfare objective shifts opportunity away from concentrated popular profiles.  
**Metrics and reported effect:** Dating/log setting: NSW 90.39 expected matches and 31/14 envies; SW 111.37 matches and 434/331 envies. Dating/inverse: NSW 59.37 and 19/8; SW 74.95 and 330/254.  
**Dating fit:** High — directly addresses reciprocal exposure concentration and fairness on real dating data.  
**Confidence real/correct:** High — primary paper, official venue record, and public implementation repository.

### [Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method](./read-papers/2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems.md)

**Full title:** Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method  
**Authors/org:** Chen Yang, Sunhao Dai, Yupeng Hou, Wayne Xin Zhao, Jun Xu, Yang Song, Hengshu Zhu; Renmin University of China and BOSS Zhipin  
**Year:** 2024  
**Venue/type:** KDD 2024; conference paper  
**Verified link:** https://arxiv.org/abs/2408.09748  
**Tier:** 1  
**What they did:** They add five holistic reciprocal metrics, formulate two-sided recommendations as bilateral causal treatments, and train CRRS with treatment-specific outcome models plus vacant-slot reranking to maximize distinct matches.  
**Two-sided mechanism:** CRRS compares one-sided and bilateral exposure outcomes and redirects redundant recommendation slots to alternatives with higher total expected match value.  
**Metrics and reported effect:** Dating CRRS-LightGCN: CRecall@50 0.3387, CPrecision@50 0.0075, 1,743 pairs; DPGNN: 0.3007, 0.0067, 1,548. Recruitment CRRS-BPRMF: 0.3968 and 8,913 vs. LFRR 0.3530 and 7,929.  
**Dating fit:** High — targets unique reciprocal outcomes and scarce exposure slots, though not hard reply capacity.  
**Confidence real/correct:** High — primary paper, KDD metadata, author code/data link, and source-scoped evidence.

---

*To run experiments on Libimseti, use the experiment-runner workflow with the dataset URL above.*

### [Modeling Two-Way Selection Preference for Person-Job Fit](./read-papers/2022_RecSys_DPGNN_Two-Way-Selection-Person-Job.md)

**Title:** Modeling Two-Way Selection Preference for Person-Job Fit  
**Authors/org:** Chen Yang, Yupeng Hou, Yang Song, Tao Zhang, Ji-Rong Wen, Wayne Xin Zhao; Renmin University of China and BOSS Zhipin  
**Year:** 2022  
**Venue/type:** RecSys 2022; conference paper  
**Verified link:** https://arxiv.org/abs/2208.08612  
**Tier:** 1  
**What they did:** DPGNN splits every candidate and job into active and passive graph nodes, propagates mutual and unilateral interactions separately, combines two directional scores, and trains with a bilateral quadruple loss plus contrastive alignment. It is evaluated on three large recruitment domains against ten baselines.  
**Mechanism:** Separate outgoing taste from incoming appeal, learn from one-way likes as well as matches, then combine both directions into one reciprocal score.  
**Metrics/effect:** Average lift over LGCNBERT: 7.12% Tech, 4.81% Sales, 7.73% Design. Tech candidate/job Recall@5: 0.2941/0.3430 vs. 0.2685/0.3187.  
**Dating fit + reason:** Medium — directly useful for like-back scoring, but it has no capacity, congestion, exposure-spread, conversation, or retention objective.  
**Confidence:** High — primary paper and source-scoped evidence; proprietary datasets limit independent reproduction.

### [Reciprocal Sequential Recommendation](./read-papers/2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md)

**Title:** Reciprocal Sequential Recommendation  
**Authors/org:** Bowen Zheng, Yupeng Hou, Wayne Xin Zhao, Yang Song, Hengshu Zhu; Renmin University of China and BOSS Zhipin  
**Year:** 2023  
**Venue/type:** RecSys 2023; conference paper  
**Verified link:** https://arxiv.org/abs/2306.14712  
**Tier:** 1  
**What they did:** ReSeq aligns active and passive embedding spaces, encodes chronological bilateral histories with specialized Transformer masks, matches histories through time-sensitive co-attention, and distills the expensive micro model into a dot-product macro scorer. Five real datasets test accuracy and latency.  
**Mechanism:** Model preference drift in both directions, learn fine-grained sequence compatibility offline, and serve a distilled bilateral score at retrieval latency.  
**Metrics/effect:** Technology HR@5 reaches 0.7597 candidate-side and 0.7809 recruiter-side; macro latency is about 0.28 ms/batch versus about 8.7 ms for micro matching.  
**Dating fit + reason:** Medium — strong dynamic reciprocal scorer, but no inbox capacity, congestion cooling, exposure allocation, or retention outcome.  
**Confidence:** High — primary paper, public code, and source-scoped evidence; live dating transfer is untested.

### [BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment](./read-papers/2023_KDD_BOSS_Bilateral-Occupational-Suitability.md)

**Title:** BOSS: A Bilateral Occupational-Suitability-Aware Recommender System for Online Recruitment  
**Authors/org:** Xiao Hu, Yuan Cheng, Zhi Zheng, Yue Wang, Xinxin Chi, Hengshu Zhu; BOSS Zhipin and University of Science and Technology of China  
**Year:** 2023  
**Venue/type:** KDD 2023; conference paper  
**Verified link:** https://www.kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html  
**Tier:** 1  
**What they did:** BOSS uses separate job-seeker and recruiter expert groups, explicit feature interactions, task-specific gates, and an entire-space conditional chain for click, apply, review, and accept. Five large platform datasets and a live experiment evaluate the system.  
**Mechanism:** Separate sender and receiver experts, then optimize the full view-to-mutual-accept funnel rather than a shallow unilateral action.  
**Metrics/effect:** Technology AUC 0.8918 ± 0.0021 versus PLE 0.8875 ± 0.0030; live Information Technology acceptance rate improves 6.15% over control.  
**Dating fit + reason:** Medium — maps directly to view/like/review/like-back, but does not model reply capacity, congestion, spread, or retention.  
**Confidence:** High — primary paper and source-scoped evidence; online test details are limited.

### [Reciprocal Recommendation System for Online Dating](./read-papers/2015_ASONAM_RRS_Reciprocal-Recommendation-Online-Dating.md)

**Title:** Reciprocal Recommendation System for Online Dating  
**Authors/org:** Peng Xia, Benyuan Liu, Yizhou Sun, Cindy Chen; University of Massachusetts Lowell and Northeastern University  
**Year:** 2015  
**Venue/type:** ASONAM 2015; conference paper  
**Verified link:** https://arxiv.org/abs/1501.06247  
**Tier:** 2  
**What they did:** The authors project directed Baihe communication into same-side interest and attractiveness graphs, define Jaccard similarities, estimate both directional compatibilities, and combine them harmonically. Four collaborative variants are tested against RECON and HCF on 200,000-user dating logs.  
**Mechanism:** Infer outgoing taste and incoming appeal separately from behavioral overlap; harmonic aggregation penalizes pairs with weak return interest.  
**Metrics/effect:** CF1–CF4 outperform HCF on interest and reciprocal precision/recall; exact lifts are not specified. Reply rates are 9.5% male-to-female and 17.9% female-to-male.  
**Dating fit + reason:** Medium — directly validated on dating behavior, but it observes overload without modeling capacity or redistributing exposure.  
**Confidence:** High — primary paper and source-scoped evidence; exact plotted effects are not numerically reported.

### [Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating](./read-papers/2013_UMUAI_RECON_Recommending-People-To-People.md)

**Title:** Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating  
**Authors/org:** Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, Judy Kay; University of Sydney  
**Year:** 2013  
**Venue/type:** User Modeling and User-Adapted Interaction; journal paper  
**Verified link:** https://www.dropbox.com/s/cb93kjvlolh1n7q/2012_UMUAI_Pizzato_etal_UMUAI.pdf?dl=1  
**Tier:** 3  
**What they did:** The paper defines reciprocal-recommender roles and outcomes, evaluates RECON's harmonic bilateral scoring on commercial dating logs, compares implicit with stated preferences, adds negative-preference suppression, and studies activity, popularity, reply overload, and recommendation spread.  
**Mechanism:** Combine both directional compatibilities harmonically, learn from implicit positive and negative actions, and monitor whether recommendations collapse onto popular users.  
**Metrics/effect:** RECON S@10 42.20% vs. 23.00% unilateral and 17.3% search; S@1 with negative preference 37.46% vs. 31.78%; reply success falls to 11.31% at 50+ EOIs.  
**Dating fit + reason:** High — direct dating evidence links reciprocal scoring to rejection, overload, and spread, although no hard capacity optimization or retention test is provided.  
**Confidence:** High — primary manuscript and source-scoped evidence; platform and dataset are proprietary.

### [Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation](./read-papers/2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md)

- **Title:** Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation
- **Authors/organization:** Iván Palomares, James Neve, Carlos Porcel, Luiz Pizzato, Ido Guy, Enrique Herrera-Viedma; University of Granada, University of Bristol, Commonwealth Bank of Australia AI Labs, eBay Research
- **Year:** 2021
- **Venue/type:** Information Fusion; journal survey
- **Link:** https://www.ujaen.es/grupos-de-investigacion/asia/sites/investigacion_asia/files/uploads/node_evento/revistas_indexadas/1-s2.0-S1566253520304267-mainext.pdf
- **Tier tag:** Tier 3
- **What they did (≤80 words):** Formalized reciprocal recommendation as fusion of two directional preference estimates; organized algorithms, fusion operators, metrics, datasets, and application areas; reviewed representative dating, recruitment, learning, and social-network systems; and identified research gaps in fairness, explainability, data sparsity, evaluation, and emerging applications.
- **Mechanism relevant to two-sided balancing (≤50 words):** Combine both sides' predicted preferences with mutuality-sensitive operators, then use popularity-aware weighting or stochastic/stable matching to avoid repeatedly recommending overloaded popular users while neglecting the long tail.
- **Metrics and reported effect:** Success/failure rate, reciprocal rank, precision, recall, AUC. CCR: nearly 70% success, about 2× random-neighbor baseline; RRK: 14–17% improvement over IBCF/CSVD. Market-health metrics requested by this project are otherwise not specified.
- **Dating-app fit:** High — directly surveys reciprocal dating recommendation and popularity-load balancing, though not hard capacity allocation.
- **Confidence:** High — peer-reviewed survey; quantitative claims remain secondary reports of cited studies.


## D2 — Market and ecosystem framing (5)

### [Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems](./read-papers/2018_CIKM_Adaptive-Fairness_Fair-Marketplace-Counterfactual-Evaluation.md)

- **Title:** Towards a Fair Marketplace: Counterfactual Evaluation of the Trade-off between Relevance, Fairness & Satisfaction in Recommendation Systems
- **Authors/organization:** Rishabh Mehrotra, James McInerney, Hugues Bouchard, Mounia Lalmas, Fernando Diaz; Spotify Research / Microsoft Research
- **Year:** 2018
- **Venue/type:** CIKM; conference paper
- **Link:** https://rishabhmehrotra.com/papers/CIKM2018-marketplace-mehrotra.pdf
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Defined a supplier popularity-bin fairness objective, proposed global and user-adaptive policies that trade relevance against fair exposure, and evaluated them offline with inverse-propensity scoring on randomized Spotify production logs.
- **Mechanism relevant to two-sided balancing (≤50 words):** Use diminishing returns across supplier-popularity bins, plus a viewer-specific fairness affinity, to redirect some impressions from superstar suppliers toward the long tail while protecting consumer satisfaction.
- **Metrics and reported effect:** Satisfaction proxy = tracks listened to. Adaptive-I: 0.709, +9.0%; Adaptive-II: 0.729, +12.1% versus relevance-only 0.650. Fairness-only: 0.420, 35% below relevance-only. Dating market-health effects not specified.
- **Dating-app fit:** Medium — strong exposure-control and offline-evaluation pattern, but no reciprocity or capacity.
- **Confidence:** High — peer-reviewed industry paper with production randomized logs; transfer to dating is inferential.

### [Joint Multisided Exposure Fairness for Recommendation](./read-papers/2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md)

- **Title:** Joint Multisided Exposure Fairness for Recommendation
- **Authors/organization:** Haolun Wu, Bhaskar Mitra, Chen Ma, Fernando Diaz, Xue Liu; McGill, Microsoft, City University of Hong Kong, Google
- **Year:** 2022
- **Venue/type:** SIGIR; conference paper
- **Link:** https://www.microsoft.com/en-us/research/uploads/prod/2022/04/sigir2022-jme-fairness.pdf
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Defined six exposure-fairness metrics over individual and group consumers and producers, analyzed their disparity–relevance trade-offs, and trained a stochastic matrix-factorization ranker with Gumbel reparameterization and smooth ranks to jointly optimize relevance and group-to-group exposure fairness.
- **Mechanism relevant to two-sided balancing (≤50 words):** Optimize expected exposure between viewer groups and shown-user groups rather than checking only one side. A weighted GG-F term redistributes ranked attention while II/IG/GI/AI/AG metrics localize which side and aggregation level drives imbalance.
- **Metrics and reported effect:** GG-F significantly improves at α=1 (p<0.01) with nonsignificant NDCG degradation; NDCG@50 changes by -0.0011 on MovieLens100K and -0.0005 on MovieLens1M.
- **Dating-app fit:** Medium — excellent joint exposure measurement, but no reciprocity or capacity.
- **Confidence:** High — peer-reviewed paper with public code and datasets.

*To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.*

### [A Closer Look at How LinkedIn Integrates Fairness into Its AI Products](./read-papers/2022_LinkedIn_LiFT-Platform_LinkedIn-Integrates-Fairness-AI.md)

- **Title:** A Closer Look at How LinkedIn Integrates Fairness into Its AI Products
- **Authors/organization:** Heloise Logan, Preetam Nandy, Kinjal Basu, Sakshi Jain; LinkedIn
- **Year:** 2022
- **Venue/type:** LinkedIn Engineering Blog; engineering post
- **Link:** https://www.linkedin.com/blog/engineering/fairness/a-closer-look-at-how-linkedin-integrates-fairness-into-its-ai-pr
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Described a model-agnostic fairness platform in LinkedIn's ProML infrastructure: an analyzer measures group disparities, a mitigation trainer uses LiFT algorithms to learn score corrections, and a post-processing layer applies them before an online A/B validation loop.
- **Mechanism relevant to two-sided balancing (≤50 words):** Centralize two-sided cohort audits and post-score mitigation so viewer, candidate, or joint group attributes can influence ranking without modifying each base model.
- **Metrics and reported effect:** Not specified in source.
- **Dating-app fit:** Low — operationally transferable, but no reciprocal, capacity, congestion, or market-health evidence.
- **Confidence:** High that the architecture is accurately described; low confidence about effectiveness because no quantitative results are disclosed.

### [Managing Diversity in Airbnb Search](./read-papers/2020_KDD_Query-Context-Embedding_Managing-Diversity-Airbnb-Search.md)

- **Title:** Managing Diversity in Airbnb Search
- **Authors/organization:** Mustafa Abdool et al.; Airbnb
- **Year:** 2020
- **Venue/type:** KDD Applied Data Science; conference paper
- **Link:** https://arxiv.org/abs/2004.02621
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Compared heuristic, distribution-matching, contextual-feature, and listwise neural approaches to diversify Airbnb search. Their final LSTM encodes top-result context into a query embedding and re-ranks candidates, improving both offline diversity/relevance and online bookings.
- **Mechanism relevant to two-sided balancing (≤50 words):** Re-rank the whole slate, not each candidate independently. Position-aware diversity, target-distribution losses, or a learned context embedding can prevent repeated exposure of one candidate type and adapt diversification to the viewer and current candidate pool.
- **Metrics and reported effect:** LSTM: +1.97% MLR, +1.26% offline NDCG, +1.2% online NDCG, +0.44% bookings, +0.61% new-guest bookings. Direct dating market-health effects not specified.
- **Dating-app fit:** Medium — strong listwise diversification evidence, but no reciprocity or capacity.
- **Confidence:** High — peer-reviewed Airbnb industry paper with reported production A/B outcomes.

### [Two-Sided Fairness in Rankings via Lorenz Dominance](./read-papers/2021_NeurIPS_LorenzWelfare_Two-Sided-Fairness-Lorenz-Dominance.md)

- **Title:** Two-Sided Fairness in Rankings via Lorenz Dominance
- **Authors/organization:** Virginie Do, Sam Corbett-Davies, Jamal Atif, Nicolas Usunier; Facebook AI and LAMSADE
- **Year:** 2021
- **Venue/type:** NeurIPS 2021; conference paper
- **Link:** https://arxiv.org/abs/2110.15781
- **Tier tag:** Tier 3
- **What they did (≤80 words):** Defined fair rankings as generalized-Lorenz-efficient utility profiles, optimized parameterized concave welfare functions, extended the formulation to reciprocal recommendation, and used Frank-Wolfe inference to make global stochastic reranking tractable. Experiments compare user/item trade-offs on music, movie, follow, and trust networks.
- **Mechanism relevant to two-sided balancing (≤50 words):** Reciprocal utility combines both recommendation directions; concave welfare gives larger marginal value to an exposure or predicted match for a worse-off user, redirecting scarce ranking positions away from already well-served users while preserving Pareto efficiency.
- **Metrics and reported effect:** Twitter-13k: bottom-10% cumulative utility 120→280 at `alpha=-5`, with total utility 17,000→6,400. Quality-weighted and equal-exposure baselines yield dominated curves for `beta>=0.1`; Gini and Lorenz-curve slices quantify distribution.
- **Dating-app fit:** High — directly models reciprocal predicted-match utility and broad outcome distribution, but not hard reply capacity or online dynamics.
- **Confidence:** High — peer-reviewed primary paper with proofs, public datasets, and source-scoped quantitative evidence.


## D3 — Capacity and congestion (4)

### [LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace](./read-papers/2017_KDD_LiJAR_Job-Application-Redistribution.md)

- **Title:** LiJAR: A System for Job Application Redistribution towards Efficient Career Marketplace
- **Authors/organization:** Fedor Borisyuk, Liang Zhang, Krishnaram Kenthapadi; LinkedIn
- **Year:** 2017
- **Venue/type:** KDD 2017 Applied Data Science; conference paper
- **Link:** http://theory.stanford.edu/~kngk/papers/LiJAR-SystemForJobApplicationRedistribution-KDD2017.pdf
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Built and deployed a cumulative-demand forecasting and reranking system for LinkedIn Jobs. It combines dynamic CTR estimation, future-impression forecasting, confidence intervals, relevance-gated boosting, and exponential penalization to move applications from jobs projected to be oversubscribed toward relevant jobs projected to remain underserved.
- **Mechanism relevant to two-sided balancing (≤50 words):** Forecast each recipient's end-of-horizon demand and intervene early: boost under-capacity recipients above a relevance floor and exponentially throttle recipients projected beyond capacity, reallocating attention without replacing the base relevance model.
- **Metrics and reported effect:** Full LiJAR: underserved applications +6.5%, overserved applications -8.7%, total applications +2.3% (not significant), distribution entropy +12%; forecast RMSE -7.5% versus IMP-WEEKLY.
- **Dating-app fit:** Medium — production-proven capacity-aware exposure redistribution, but unilateral and not match- or conversation-aware.
- **Confidence:** High — primary KDD paper describing a deployed LinkedIn system and live A/B results.

### [Modeling Impression Discounting in Large-Scale Recommender Systems](./read-papers/2014_KDD_ImpressionDiscounting_Modeling-Impression-Discounting.md)

- **Title:** Modeling Impression Discounting in Large-Scale Recommender Systems
- **Authors/organization:** Pei Lee, Laks V. S. Lakshmanan, Mitul Tiwari, Sam Shah; University of British Columbia and LinkedIn
- **Year:** 2014
- **Venue/type:** KDD 2014; conference paper
- **Link:** http://archive.gersteinlab.org/meetings/s/2014/08.28/kdd2014-i0kdd-meeting-materials/docs/p1837.pdf
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Analyzed repeated non-converting impressions at LinkedIn and Tencent, learned parametric decay functions from impression count, recency, position, and user frequency, and applied the result as a model-agnostic score multiplier. Density-based pruning and weighted regression stabilize curve fitting on highly skewed billion-scale logs.
- **Mechanism relevant to two-sided balancing (≤50 words):** Repeatedly ignored user-item pairs receive a smaller score, freeing scarce ranking positions for fresh or under-exposed alternatives. The mechanism budgets viewer attention but does not account for the shown user's capacity.
- **Metrics and reported effect:** PYMK offline P@10 +31.3%; live invitation P@10 +13.26% ± 0.2%; density-weighted fit RMSE 0.1121→0.0188. Match, conversation, distribution, and retention effects are not specified.
- **Dating-app fit:** Low — useful anti-staleness component, but no reciprocity or recipient-load model.
- **Confidence:** High — primary KDD industry paper with large offline datasets and a live production test.

### [Managing Congestion in Matching Markets](./read-papers/2021_MSOM_ApplicationLimits_Managing-Congestion-Matching-Markets.md)

- **Title:** Managing Congestion in Matching Markets
- **Authors/organization:** Nick Arnosti, Ramesh Johari, Yash Kanoria; Stanford University and Columbia Business School
- **Year:** 2021
- **Venue/type:** Manufacturing & Service Operations Management; theoretical/applied-research paper
- **Link:** http://www.columbia.edu/~yk2577/congestion.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Built an asynchronous stochastic matching model with application costs, recipient screening costs, compatibility, and changing availability; derived a large-market mean-field equilibrium; and compared unregulated applications, platform limits, and added application friction. They prove that low-cost over-application can eliminate recipient welfare and that caps can benefit both sides.
- **Mechanism relevant to two-sided balancing (≤50 words):** Limit applications/likes before recipient screening queues become congested. The cap raises applicant availability, reduces stale screening work, and avoids the applicant-surplus loss caused by fees or deliberately tedious application flows.
- **Metrics and reported effect:** At `r=1.4`, applicant welfare approximately doubles; at `r=1.9`, it triples. A single cap guarantees both sides at least 75% of their constrained-efficient maxima. Live match, conversation, and retention effects are not specified.
- **Dating-app fit:** Medium — direct like-limit rationale and capacity externality, but asymmetric matching and no personalized reciprocal scoring.
- **Confidence:** High on the theoretical claims; medium on direct dating transfer because evidence is simulation/proof rather than a dating field experiment.

### [Recommendation with Capacity Constraints](./read-papers/2017_CIKM_CapMF_Recommendation-Capacity-Constraints.md)

- **Title:** Recommendation with Capacity Constraints
- **Authors/organization:** Konstantina Christakopoulou, Jaya Kawale, Arindam Banerjee; University of Minnesota and Netflix
- **Year:** 2017
- **Venue/type:** CIKM 2017; conference paper
- **Link:** https://arindam.cs.illinois.edu/papers/17/rec-capacity-cikm17.pdf
- **Tier tag:** Tier 3
- **What they did (≤80 words):** Extended PMF, BPR, GeoMF, and GeoBPR with a differentiable penalty on propensity-weighted expected usage above item-specific capacity. Compared joint training with unconstrained models, capacity-only objectives, and a post-processing assignment that recommends each item only to its top-capacity users on four public datasets.
- **Mechanism relevant to two-sided balancing (≤50 words):** Estimate total expected demand for every candidate and penalize overload inside the ranking objective, or allocate each candidate only to the highest-value users up to capacity. This redirects recommendations away from saturated items.
- **Metrics and reported effect:** MovieLens Cap-BPR: Capacity Loss 4.51→0.08, pairwise loss 0.12→0.14. Foursquare Cap-GeoBPR: 0.81→0.02, pairwise loss 0.31→0.28. Match and retention metrics are not specified.
- **Dating-app fit:** Low — explicit capacity is valuable, but static passive items and no reciprocal acceptance limit direct applicability.
- **Confidence:** High — primary peer-reviewed paper with public benchmark data and detailed quantitative tables; real capacity validity remains untested.


## D4 — Constrained allocation and re-ranking (4)

### [Assortment Planning for Two-Sided Sequential Matching Markets](./read-papers/2022_OR_NA_Assortment-Two-Sided-Sequential-Matching.md)

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

### [Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform](./read-papers/2026_arXiv_TEC_Recommendation-Exposure-Favorite-Lists.md)

- **Title:** Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform
- **Authors/organization:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Yuki Fujii, Shunsuke Ozeki, Shunya Noda; The University of Tokyo and Timee
- **Year:** 2026
- **Venue/type:** arXiv; preprint and production field experiment
- **Link:** https://arxiv.org/abs/2606.17397
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Designed Thresholded Eligibility Control, a parallel exposure controller that updates job-template allocation from posted and unfilled capacity and past recommendations. Calibrated simulations compare Greedy and quota policies; a one-month prefecture-level production rollout on Timee measures matches, favorite stocks, fill rates, and exposure distribution.
- **Mechanism relevant to two-sided balancing (≤50 words):** Convert capacity and vacancy into stateful exposure scores, cap any one recipient's dominance, and expose a recipient only when its eligibility threshold exceeds a randomized slot timing. This redirects impressions from popular but capacity-poor options toward underserved options with usable capacity.
- **Metrics and reported effect:** Simulation job-finding 57.61%→70.03% and fill rate 67.42%→82.17%. Field effect: +9.045 matches per prefecture-day and -6.1 points in the low-exposure tail; several favorite/subscriber/fill outcomes are null.
- **Dating-app fit:** Medium — direct capacity-aware exposure and interference-aware evidence, but FCFS one-sided hiring must become reciprocal matching.
- **Confidence:** High — exact source-scoped preprint and production-study evidence, with design limitations disclosed.

### [Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search](./read-papers/2019_KDD_DetGreedy_Fairness-Aware-Ranking-Talent-Search.md)

- **Title:** Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search
- **Authors/organization:** Sahin Cem Geyik, Stuart Ambler, Krishnaram Kenthapadi; LinkedIn
- **Year:** 2019
- **Venue/type:** KDD 2019 Applied Data Science; industry conference paper
- **Link:** https://arxiv.org/abs/1905.01989
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Defined skew and feasibility metrics for ranked representation and four deterministic post-processing algorithms that enforce a target categorical distribution while preserving model utility. Synthetic tests cover up to ten groups; a three-week LinkedIn Recruiter A/B test evaluates representative queries and recruiter messaging at global scale.
- **Mechanism relevant to two-sided balancing (≤50 words):** Re-rank each result prefix against minimum and maximum group counts. If a group would be underrepresented, select its highest-scoring remaining candidate; otherwise select the best eligible candidate. This gives a production-ready constrained-ranking primitive, though not individual capacity control.
- **Metrics and reported effect:** Representative queries 33%→95%; MinSkew@100 -0.259→-0.011 (`p<1e-16`); InMails sent/accepted unchanged within ±1% (`p>0.5`). Match and retention effects are not specified.
- **Dating-app fit:** Low — scalable constrained reranking transfers, but the objective is unilateral group representation rather than reciprocal, capacity-aware outcomes.
- **Confidence:** High — peer-reviewed industry paper with source-scoped production A/B evidence.

### [Fairness of Exposure in Rankings](./read-papers/2018_KDD_NA_Fairness-of-Exposure-Rankings.md)

- **Title:** Fairness of Exposure in Rankings
- **Authors/organization:** Ashudeep Singh, Thorsten Joachims; Cornell University
- **Year:** 2018
- **Venue/type:** KDD 2018; academic conference paper
- **Link:** https://arxiv.org/abs/1802.07281
- **Tier tag:** Tier 3
- **What they did (≤80 words):** Formulated rankings as doubly stochastic exposure-allocation matrices, maximized expected utility subject to demographic-parity, disparate-treatment, or disparate-impact constraints, and used Birkhoff-von Neumann decomposition to sample deterministic rankings. Offline job and news examples quantify exact fairness ratios and DCG cost.
- **Mechanism relevant to two-sided balancing (≤50 words):** Treat position exposure as a scarce allocatable resource. Solve a linear program that maximizes relevance while enforcing exposure or expected-impact ratios, then sample rankings from the optimized distribution. Recipient-level capacity and reciprocal response must be added for dating.
- **Metrics and reported effect:** Job DTR 1.7483→1.0000 with DCG 3.8193→3.8044; job DIR 1.8193→1.0000 with DCG 3.8025. News DTR and DIR reach 1.0000 with small-to-moderate DCG costs.
- **Dating-app fit:** Low — exposure allocation transfers, but reciprocity and capacity are absent.
- **Confidence:** High — peer-reviewed primary source with explicit formulation and exact offline results.


## D5 — Market-design levers (6)

### [Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions](./read-papers/2021_MS_NA_Facilitating-Search-for-Partners.md)

- **Title:** Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions
- **Authors/organization:** Yash Kanoria, Daniela Saban; Columbia Business School and Stanford Graduate School of Business
- **Year:** 2021
- **Venue/type:** Management Science; theoretical matching-market paper
- **Link:** https://web.stanford.edu/~dsaban/facilitating-search.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Built a dynamic matching model with arrivals, departures, strategic thresholds, and costly discovery of pair-specific value. They compare unrestricted search with directional proposals, one-sided or disabled screening, and hidden quality tiers, proving and numerically illustrating when restricting actions improves side-specific and average welfare.
- **Mechanism relevant to two-sided balancing (≤50 words):** Force the short side or lower-screening-cost side to initiate so the congested long side can screen rather than send mostly rejected proposals. Hiding quality tiers can prevent selective recipients from remaining active while ignoring lower-tier users.
- **Metrics and reported effect:** Up to +14.6% average welfare with asymmetric screening cost; with a 2:1 imbalance, up to +31% long-side utility and +10% average welfare, with <8% short-side loss. Direct match and retention effects are not specified.
- **Dating-app fit:** High — directional initiation and hidden popularity are concrete dating-market levers, though theory predicts parameter-dependent backfire risk.
- **Confidence:** High on the source-scoped model/results; medium on publication metadata because the queried PDF is a 2017 working version while the queue records Management Science 2021.

### [Competing by Restricting Choice: The Case of Matching Platforms](./read-papers/2018_MgmtSci_ChoiceRestriction_Competing-By-Restricting-Choice.md)

- **Title:** Competing by Restricting Choice: The Case of Matching Platforms
- **Authors/organization:** Hanna Halaburda, Mikołaj Jan Piskorski, Pınar Yıldırım; Bank of Canada/NYU, IMD, Wharton
- **Year:** 2018
- **Venue/type:** Management Science; analytical matching-platform paper
- **Link:** https://questromworld.bu.edu/platformstrategy/wp-content/uploads/sites/49/2017/06/PlatStrat_2017_paper_46-1.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Built a two-stage reciprocal dating model in which each user sees `N` candidates and can make one offer. The authors derive how more choice improves conditional match quality but increases rejection through same-side competition, then characterize user self-selection and platform competition. Numerical simulations test robustness when preferences contain vertical correlation.
- **Mechanism relevant to two-sided balancing (≤50 words):** Restrict candidate menus on both sides so each target has fewer competing offers. This lowers rejection and can attract motivated users, creating a curated submarket with higher match probability despite less choice.
- **Metrics and reported effect:** Rejection probability `N/(N+1)`; simulated expected utility peaks at small menu sizes for low-outside-option users. eHarmony's price was about 25% above Match.com's. Real match, conversation, and retention effects are not specified.
- **Dating-app fit:** High — a daily batch or swipe-stack cap directly implements the model's market-design lever, but causal product evidence is absent.
- **Confidence:** High on source-scoped theory; medium-high on venue/year because the queried file is a 2017 working version of the 2018 publication.

### [Propose with a Rose? Signaling in Internet Dating Markets](./read-papers/2015_ExpEcon_VirtualRose_Propose-With-A-Rose.md)

- **Title:** Propose with a Rose? Signaling in Internet Dating Markets
- **Authors/organization:** Soohyung Lee, Muriel Niederle
- **Year:** 2015
- **Venue/type:** Experimental Economics; randomized dating-platform field experiment
- **Link:** https://web.stanford.edu/~niederle/Lee.Niederle.Rose.ExpEcon.2015.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Randomized 613 users on a South Korean dating platform to receive two or eight scarce virtual roses. Users attached roses to proposals, and recipients saw the signal before accepting. Recipient-fixed-effect and instrumental-variable analyses estimate causal acceptance effects, while treatment-level outcomes test whether signaling expands matches or merely reallocates them.
- **Mechanism relevant to two-sided balancing (≤50 words):** A scarce priority signal communicates serious interest and attainability, helping capacity-limited recipients allocate evaluation effort. It coordinates decentralized proposals without centrally changing exposure.
- **Metrics and reported effect:** Rose acceptance +3.3 percentage points (20% relative; IV +4.1). Eight versus two roses raised total initiated dates 48% for verified Seoul men and 86% for women. Conversations and retention were not measured.
- **Dating-app fit:** High — the intervention and outcome funnel directly match limited likes, mutual acceptance, and Super-Like-style signaling.
- **Confidence:** High — source-scoped randomized field evidence and bibliographic metadata are explicit.

### [Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating](./read-papers/2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md)

- **Title:** Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating
- **Authors/organization:** Jessica Fong; earlier working version names Jessica Yu, Stanford Graduate School of Business
- **Year:** 2024
- **Venue/type:** Marketing Science; randomized field experiment and structural model
- **Link:** https://www.anderson.ucla.edu/sites/default/files/documents/areas/fac/marketing/Seminars/Fall%202018/SEARCH,%20SELECTIVITY,%20AND%20MARKET%20THICKNESS%20IN%20TWO%20SIDED%20MARKETS.pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Randomized displayed local male and female counts to causally estimate how perceived candidate supply and competition alter swiping selectivity. The author combines the experiment with historical swipe logs in a dynamic search model with finite like quotas, then simulates two-sided market growth, one-sided gender gating, and like-cap changes in small and large markets.
- **Mechanism relevant to two-sided balancing (≤50 words):** Treat market-size beliefs and like limits as coupled controls. A larger pool can induce over-selectivity and fewer matches; relaxing a scarce like quota can offset this, with sharply different effects by side and market size.
- **Metrics and reported effect:** Perceived market size +50%: matches -2%; perceived competition +50%: +3%. Small-market two-sided growth: -12.2% male and -17.7% female matches; with doubled caps: +136.3% and +121.6%.
- **Dating-app fit:** High — directly estimates strategic swiping and like-cap effects on a live reciprocal dating app.
- **Confidence:** High on source-scoped methods/results; medium-high on publication metadata because the linked PDF is a 2018 version with an earlier title and author surname.

### [Matching Theory-Based Recommender Systems in Online Dating](./read-papers/2022_arXiv_MTRS_Matching-Theory-Online-Dating.md)

- **Title:** Matching Theory-Based Recommender Systems in Online Dating
- **Authors/organization:** Yoji Tomita, Riku Togashi, Daisuke Moriwaki; CyberAgent
- **Year:** 2022
- **Venue/type:** arXiv technical preprint; production-system description
- **Link:** https://arxiv.org/abs/2208.11384
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Combined directional matrix-factorization preferences with a transferable-utility matching equilibrium. The final score multiplies reciprocal affinity by user-specific unmatched-probability terms that discount capacity-saturated users. Iterative proportional fitting solves those terms, while locality-sensitive hashing and approximate nearest-neighbor search reduce all-pairs computation for deployment on Tapple's seven-million-user platform.
- **Mechanism relevant to two-sided balancing (≤50 words):** Apply an equilibrium capacity discount to mutual-preference scores so overloaded superstar profiles lose rank and users with unused matching capacity gain exposure.
- **Metrics and reported effect:** No quantitative match, concentration, conversation, wasted-like, retention, latency, or A/B-test result is specified in source.
- **Dating-app fit:** High — personalized capacity-aware reciprocal scoring was designed for a large Japanese dating app, but it lacks reported validation.
- **Confidence:** High on architecture and metadata; medium on practical effect because no quantitative evaluation is reported.

### [Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach](./read-papers/2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md)

- **Title:** Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach
- **Authors/organization:** Kazuki Sekiya, Suguru Otani, Yuki Komatsu, Sachio Ohkawa, Shunya Noda
- **Year:** 2026
- **Venue/type:** arXiv technical preprint; production simulation and regional field experiment
- **Link:** https://arxiv.org/abs/2602.19689
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Predicted the full login-like-login-relike funnel, defined congestion-adjusted effective dates, and allocated recommendation probabilities with receiver budgets for expected likes or dates. They prove ECDA becomes a greedy scan under date-rate sorting, compare it with one-sided and deferred-acceptance baselines, and run a regional CoupLink difference-in-differences rollout.
- **Mechanism relevant to two-sided balancing (≤50 words):** Cap expected inbound likes or dates, not just recommendation counts, and optimize effective dates so already overloaded receivers are discounted. This spreads exposure toward users who can still convert a match into interaction.
- **Metrics and reported effect:** Simulation: effective dates +7.6%, receiver probability +8.7%, raw dates -24.6%. Field excluding top 0.1%: effective dates +0.003, proposer probability +0.002, receiver probability +0.005; messaging unchanged.
- **Dating-app fit:** High — direct production implementation and field evidence on a reciprocal dating platform.
- **Confidence:** High on source-scoped methods and reported effects; medium-high on causal precision because only two rollout regions support the difference-in-differences design.


## D6 — Objectives and ecosystem metrics (5)

### [Your Looks and Your Inbox](./read-papers/2009_OkTrends_NA_Your-Looks-and-Your-Inbox.md)

**Citation:** Christian Rudder / OkCupid. 2009. *Your Looks and Your Inbox*. OkTrends company blog. https://gwern.net/doc/psychology/okcupid/yourlooksandyourinbox.html. **Tier 1.**  
**What they did (≤80 words):** Analyzed OkCupid photo ratings, message volumes, and reply patterns to quantify how perceived attractiveness shapes user attention. The post compares gender-specific rating curves with actual messaging and reports inbox-volume multiples across attractiveness strata.  
**Two-sided mechanism (≤50 words):** A market-health diagnostic for demand concentration and receiver congestion: segment attention and reply propensity by recipient attractiveness to reveal where additional messages have diminishing reciprocal value.  
**Metrics and reported effect:** Message share, inbox-volume ratios, and reply rates; 66% of male messages target the top 33% of women, while heavily messaged users reply less.  
**Dating-app fit:** **Medium** — strong direct evidence, no intervention.  
**Confidence:** **High** that the item and reported figures match the indexed primary source; causal interpretation is low confidence.

### [Aspirational Pursuit of Mates in Online Dating Markets](./read-papers/2018_SciAdv_PageRank_Aspirational-Pursuit-of-Mates.md)

**Citation:** Elizabeth E. Bruch and M. E. J. Newman. 2018. *Aspirational Pursuit of Mates in Online Dating Markets*. Science Advances / arXiv. https://arxiv.org/abs/1808.04840. **Tier 2.**  
**What they did (≤80 words):** Built directed message networks for active heterosexual daters in New York, Boston, Chicago, and Seattle; estimated PageRank desirability; and modeled how signed desirability gaps relate to message strategy and replies.  
**Two-sided mechanism (≤50 words):** Reflected desirability and signed gap measurement distinguish attainable reciprocal demand from raw popularity, revealing where aspirational outreach overloads high-demand receivers and yields low returns.  
**Metrics and reported effect:** Desirability rank, gap, reply probability, word count, and positivity; users reach ~25% upward, and men's upward reply rate never exceeds 21%.  
**Dating-app fit:** **Medium** — directly relevant measurement, not allocation.  
**Confidence:** **High** for source identity, methods, and reported figures.

### [Matching and Sorting in Online Dating](./read-papers/2010_AER_GaleShapley_Matching-and-Sorting-Online-Dating.md)

**Citation:** Günter J. Hitsch, Ali Hortaçsu, and Dan Ariely. 2010. *Matching and Sorting in Online Dating*. American Economic Review 100(1). https://people.duke.edu/~dandan/webfiles/PapersUpside/Matching%20and%20Sorting%20Dating.pdf. **Tier 2.**  
**What they did (≤80 words):** Estimated mate preferences from a 2003 dating-site clickstream, tested strategic selectivity, simulated Gale-Shapley matches, and compared observed online sorting and reweighted offline marriage patterns with stable-matching predictions.  
**Two-sided mechanism (≤50 words):** Uses estimated preferences and deferred acceptance to benchmark platform-wide sorting and achieved partner ranks; the correction for predicted reply probability tests whether rejection risk changes proposals.  
**Metrics and reported effect:** Reply, contact-to-match conversion, match-rank distance, and attribute correlation; 71%/56% of male/female contacts are unrequited and 4.3%/6.4% become matches.  
**Dating-app fit:** **Medium** — rigorous market benchmark, not modern capacity control.  
**Confidence:** **High** for source identity and reported study results.

### [How We Connect Daters](./read-papers/2025_Hinge_DeepRecSys_How-We-Connect-Daters.md)

**Citation:** Hinge Inc. 2025. *How We Connect Daters*. Company product explainer. https://hinge.co/how-we-connect-daters. **Tier 1.**  
**What they did (≤80 words):** Described Hinge's deep-learning recommendation system, which combines stated preferences and app activity to estimate mutual interest. The page also explains bilateral dealbreakers, behavioral feedback, and why unlimited restrictive filters are not universally available.  
**Two-sided mechanism (≤50 words):** Reciprocal scoring predicts both directions of interest; mutual hard constraints remove incompatible pairs; gating dealbreakers preserves market thickness by limiting universal over-filtering.  
**Metrics and reported effect:** Not specified in source; only a qualitative claim that unlimited dealbreakers would shrink dating pools.  
**Dating-app fit:** **High** — direct production description.  
**Confidence:** **High** for described mechanisms; **medium** for 2025 dating because the page lacks a publication timestamp.

### [Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching](./read-papers/2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md)

**Citation:** Ren Kishimoto et al. 2026. *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching*. ICLR 2026 / arXiv. https://arxiv.org/abs/2602.15752. **Tier 3.**  
**What they did (≤80 words):** Formulated retention-maximizing two-sided recommendation and proposed MRet, a dynamic learning-to-rank method that learns personalized retention curves from profiles and interactions and allocates matching opportunities using the expected retention gains of both participants.  
**Two-sided mechanism (≤50 words):** Joint marginal-retention scoring accounts for diminishing value across both sides and redirects limited matching opportunities toward pairs with the largest ecosystem retention benefit.  
**Metrics and reported effect:** User retention on synthetic and real dating-platform data; MRet is reported to improve retention over match-maximization and fairness baselines, with no quantitative effect specified.  
**Dating-app fit:** **High** — directly aligned with two-sided retention.  
**Confidence:** **High** for bibliographic metadata and abstract claims; **low** for empirical magnitude because the indexed source gives no numbers.


## D7 — Evaluation under marketplace interference (6)

### [Experimental Design in Two-Sided Platforms: An Analysis of Bias](./read-papers/2022_MgmtSci_TSRI_Experimental-Design-Two-Sided-Platforms.md)

- **Title:** Experimental Design in Two-Sided Platforms: An Analysis of Bias
- **Authors/organization:** Ramesh Johari, Hannah Li, Inessa Liskovich, Gabriel Y. Weintraub
- **Year:** 2022
- **Venue/type:** Management Science; theoretical and simulation study
- **Link:** https://arxiv.org/abs/2002.05670
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Modeled a dynamic two-sided marketplace with customer arrivals, finite listing inventory, consideration, choice, and replenishment. The authors derive a mean-field benchmark, show that the least-biased randomization side depends on market balance, and propose two-sided randomization with correction terms that estimate and subtract cannibalization between experimental cells.
- **Mechanism relevant to two-sided balancing (≤50 words):** Randomize viewers and shown users independently, use untreated cross-cells to measure competition spillovers, and weight corrections by supply-demand balance. This targets interference bias rather than changing allocation itself.
- **Metrics and reported effect:** At balanced demand, TSRI-2 reduces normalized absolute bias to about 8% of the global treatment effect versus about 20–22% for the main alternatives, with higher normalized standard error (about 0.19).
- **Dating-app fit:** Medium — dual-side randomization is valuable, but binary inventory and unilateral booking omit reciprocal liking and reply queues.
- **Confidence:** High on source-scoped theory and simulations; medium on direct dating transfer.

### [Multiple Randomization Designs: Estimation and Inference with Interference](./read-papers/2021_arXiv_SMRD_Multiple-Randomization-Designs.md)

- **Title:** Multiple Randomization Designs: Estimation and Inference with Interference
- **Authors/organization:** Lorenzo Masoero, Suhas Vijaykumar, Thomas S. Richardson, James McQueen, Ido Rosen, Brian Burdick, Pat Bajari, Guido Imbens
- **Year:** 2021 (later revision indexed)
- **Venue/type:** arXiv preprint; design-based causal-inference theory and simulation
- **Link:** https://arxiv.org/abs/2112.13495
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Independently randomized two marketplace populations, partitioned pairwise interactions into four eligibility cells, and derived estimators for aggregate, direct, buyer-spillover, and seller-spillover effects. The paper supplies exact finite-sample variance expressions, conservative covariance bounds, and a finite-population central limit theorem, then validates them in strategic-market and Gaussian simulations.
- **Mechanism relevant to two-sided balancing (≤50 words):** Use untreated pair cells with one treated neighbor side to isolate sender- and receiver-mediated spillovers. This reveals effects that ordinary one-sided experiments absorb into bias.
- **Metrics and reported effect:** A single-sided profit estimator gives the wrong sign in simulation; SMRD recovers the positive effect. A conservative test detects a buyer spillover in 99.5% of 10,000 rerandomizations.
- **Dating-app fit:** Medium — experimental cells transfer, but reciprocal matches, congestion, and reply capacity are absent.
- **Confidence:** High on the source-scoped design and simulations; direct marketplace validity remains untested.

### [Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization](./read-papers/2025_MgmtSci_GCR_Reducing-Interference-Bias-Airbnb.md)

- **Title:** Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb
- **Authors/organization:** David Holtz, Felipe Lobel, Ruben Lobel, Inessa Liskovich, Sinan Aral
- **Year:** 2025
- **Venue/type:** Management Science; marketplace field meta-experiment
- **Link:** https://business.columbia.edu/sites/default/files-efs/citation_file_upload/holtz-et-al-2024-reducing-interference-bias-in-online-marketplace-experiments-using-cluster-randomization-evidence-from%20(2).pdf
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Embedded Airbnb listings from search-session co-views, recursively clustered close substitutes, and ran an experiment over experimental designs. Clusters were assigned either to ordinary listing-level randomization or to cluster-level randomization, enabling a direct estimate of how much a guest-fee experiment's measured booking effect was distorted by competitive spillovers.
- **Mechanism relevant to two-sided balancing (≤50 words):** Put profiles competing for the same viewers in one assignment cluster so treatment does not leak through substitution across experimental cells. Compare cluster- and individual-level estimates to quantify residual interference.
- **Metrics and reported effect:** Individual versus cluster estimates were -0.345 and -0.277 bookings per listing; the -0.068 interaction (SE 0.018) implies 19.76% interference bias.
- **Dating-app fit:** Medium — co-view competition transfers, but reciprocal choice and reply capacity are unmodeled.
- **Confidence:** High — peer-reviewed, source-scoped platform meta-experiment; proprietary scaling limits replication.

### [A/B Testing for Recommender Systems in a Two-Sided Marketplace](./read-papers/2021_NeurIPS_UniCoRn_AB-Testing-Two-Sided-Marketplace.md)

- **Title:** A/B Testing for Recommender Systems in a Two-Sided Marketplace
- **Authors/organization:** Preetam Nandy, Divya Venugopalan, Chun Lo, Shaunak Chatterjee; LinkedIn
- **Year:** 2021
- **Venue/type:** NeurIPS; industry recommender experimentation paper
- **Link:** https://arxiv.org/abs/2106.00762
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Assigned producers to control or treatment ranking models and developed UniCoRn to merge their conflicting counterfactual ranks into one viewer feed. A sampling parameter trades experimental fidelity against rescoring cost. Simulations compare rank and treatment-effect error; LinkedIn deployed the design for candidate-generation and viewee-retention experiments.
- **Mechanism relevant to two-sided balancing (≤50 words):** Preserve one model assignment per shown user while blending profile-specific counterfactual ranks into shared feeds. This enables producer-side measurement without a static interaction graph and supports receiver-retention or capacity-aware ranking tests.
- **Metrics and reported effect:** Candidate generation: weekly active unique users +0.51%, sessions +0.57%. Viewee-retention ranking: +0.13% and +0.11%. All p<0.001; no significant latency increase.
- **Dating-app fit:** High — producer exposure and receiver return are direct analogs, though mutual matches are not measured.
- **Confidence:** High — peer-reviewed industry work with significant live results; duration and absolute traffic are undisclosed.

### [Off-Policy Evaluation and Learning for Matching Markets](./read-papers/2025_RecSys_DiPS-DPR_Off-Policy-Evaluation-Matching-Markets.md)

- **Title:** Off-Policy Evaluation and Learning for Matching Markets
- **Authors/organization:** Yudai Hayashi, Shuhei Goda, Yuta Saito; Wantedly, independent, Cornell
- **Year:** 2025
- **Venue/type:** RecSys; reciprocal-matching OPE/OPL research
- **Link:** https://arxiv.org/abs/2507.13608
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Modeled a reciprocal match as an outbound request followed by a conditional response, then proposed DiPS and DPR estimators that combine logged propensities with the denser first-stage label and modeled reply probability. Policy-gradient versions optimize recommendations offline. Synthetic tests and Wantedly job-matching logs compare direct, IPS, and doubly robust baselines.
- **Mechanism relevant to two-sided balancing (≤50 words):** Evaluate reciprocal policies through separate like and like-back stages, using propensity weighting only on the denser first action and regression for receiver response. This stabilizes sparse match evaluation but does not model capacity or interference.
- **Metrics and reported effect:** On 21,736 companies and 17,460 job seekers with 1.2% matches, DPR has the lowest MSE; DiPS and IPS have lower policy-selection error than DPR and DR.
- **Dating-app fit:** High — the two-stage reward exactly matches like and like-back, though market-health effects require live interference-aware tests.
- **Confidence:** High — primary RecSys paper with industrial logs; proprietary data and no public code limit replication.

### [Reducing Marketplace Interference Bias Via Shadow Prices](./read-papers/2022_arXiv_SP_Marketplace-Interference-Shadow-Prices.md)

- **Title:** Reducing Marketplace Interference Bias Via Shadow Prices
- **Authors/organization:** Ido Bright, Arthur Delarue, Ilan Lobel; Lyft, Georgia Tech, NYU
- **Year:** 2022
- **Venue/type:** arXiv working paper
- **Link:** https://arxiv.org/abs/2205.02274
- **Tier tag:** Tier 2
- **What they did (≤80 words):** Modeled demand and supply arrivals in centrally optimized matching and network-flow markets, proved why ordinary randomized experiments overstate global effects under contention, and proposed Two-LP and Shadow Price estimators. Simulations based on New York City taxi trips and a stylized supply chain compare estimator bias and variance against known global effects.
- **Mechanism relevant to two-sided balancing (≤50 words):** Value experimental demand changes by the dual prices of scarce allocation constraints. Marginal values internalize competition for shared capacity that ordinary treatment-control totals ignore.
- **Metrics and reported effect:** Ordinary randomization misses an efficiency gain up to 20% smaller than demand growth and overstates undersupply effects by more than twofold; Shadow Price substantially reduces simulated bias.
- **Dating-app fit:** Low — useful interference logic, but it assumes centralized linear-program allocation rather than decentralized mutual choice.
- **Confidence:** High on source-scoped theory and simulations; medium on dating transfer.


## D8 — Chinese and Japanese sources (4)

### [皆が幸せになるマッチングプラットフォームを目指して。「マッチング理論に基づく相互推薦システム」](./read-papers/2022_CyberAgent_MTRS_Matching-Theory-Reciprocal-Recommendation.md)

- **Title:** 皆が幸せになるマッチングプラットフォームを目指して。「マッチング理論に基づく相互推薦システム」 (*Toward a Matching Platform Where Everyone Can Be Happy: “A Reciprocal Recommendation System Based on Matching Theory”*)
- **Authors/organization:** Yoji Tomita; CyberAgent AI Lab
- **Year:** 2022
- **Venue/type:** CyberAgent Developers Blog; industry technical article
- **Link:** https://developers.cyberagent.co.jp/blog/archives/39706/
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Explained why ordinary reciprocal-score averaging overloads popular dating users, then described a Choo-Siow transferable-utility framework that combines bilateral preference predictions with capacity-aware market clearing. The associated CyberAgent research approximates iterative matching updates so the method can scale toward Tapple's active user population.
- **Mechanism relevant to two-sided balancing (≤50 words):** Use endogenous matching prices to discount capacity-saturated superstars and redistribute recommendations toward mutually compatible users who can still engage.
- **Metrics and reported effect:** Cited work improves median matches, Gini, and exposure coverage but slightly lowers total matches; no exact effects or CyberAgent-system results are specified.
- **Dating-app fit:** High — directly targets mutual-like recommendation under finite chat capacity.
- **Confidence:** High on source identity and mechanism; medium on effects because evidence is secondhand and nonnumeric.

### [マッチングアプリにおける出会いを分析する](./read-papers/2022_CyberAgent_DoubleSelection_Analyzing-Encounters-Matching-Apps.md)

- **Title:** マッチングアプリにおける出会いを分析する (*Analyzing Encounters on Matching Apps*)
- **Authors/organization:** 數見 (Kazumi); Tapple / CyberAgent
- **Year:** 2022
- **Venue/type:** CyberAgent Developers Blog; industry conference recap
- **Link:** https://developers.cyberagent.co.jp/blog/archives/35119/
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Analyzed production Tapple behavior to estimate age-verification effects, expose a large gender gap in recommendation recall, and diagnose superstar exposure concentration. The post describes bidirectional collaborative filtering and double-selection causal adjustment, then proposes multimodal features, frequency caps, and transferable-utility reranking.
- **Mechanism relevant to two-sided balancing (≤50 words):** Measure recall and message conversion separately by side, then constrain or price repeated superstar exposure so compatible, less-saturated users receive more opportunities.
- **Metrics and reported effect:** Recall is 0.9 for men and 0.2 for women; verification lifts message approval 2% and about 36%; cited TU evidence lowers exposure Gini from about 0.75 to 0.60.
- **Dating-app fit:** High — production dating evidence directly covers reciprocal scoring, conversation entry, and exposure concentration.
- **Confidence:** High on blog-reported Tapple metrics; medium on causal generalization and secondhand Gini evidence.

### [相互推薦における嗜好の集約をパーソナライズする試み](./read-papers/2026_Wantedly_PersonalizedAggregation_Personalizing-Preference-Aggregation.md)

- **Title:** 相互推薦における嗜好の集約をパーソナライズする試み (*An Attempt to Personalize Preference Aggregation in Reciprocal Recommendation*)
- **Authors/organization:** Chiaki Ichimura; Wantedly
- **Year:** 2026
- **Venue/type:** Wantedly Engineer Blog; industry technical article
- **Link:** https://www.wantedly.com/companies/wantedly/post_articles/1036056
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Combined outbound apply and recipient match predictions with a user-specific weighted harmonic mean. For users with prior successes, bounded Brent search selects the weight that raises historical successful interactions. An offline comparison against fixed weights measures logged ranking quality and recommendation diversity.
- **Mechanism relevant to two-sided balancing (≤50 words):** Personalize the sender-versus-recipient score trade-off so users do not all rank the same popular recipients, dispersing exposure toward candidates with a better chance of reciprocating.
- **Metrics and reported effect:** Apply nDCG@10 -2.4%, matching-success nDCG@10 -3.3%, unique recommendations@10 +16.8% versus fixed weights.
- **Dating-app fit:** High — reciprocal reply scoring and popular-recipient dispersion transfer directly, though cold start remains.
- **Confidence:** High on source identity, formula, and offline results; medium on online effect because exposure bias is unresolved.

### [快手因果推断与实验设计](./read-papers/2021_DataFunTalk_BilateralSwitchback_Kuaishou-Causal-Experiment-Design.md)

- **Title:** 快手因果推断与实验设计 (*Kuaishou Causal Inference and Experimental Design*)
- **Authors/organization:** Yaran Jin, Kuaishou; edited by Yifang Zhao, Baidu
- **Year:** 2021
- **Venue/type:** DataFunTalk technical-talk recap; BAAI Hub mirror
- **Link:** https://hub.baai.ac.cn/view/9770
- **Tier tag:** Tier 1
- **What they did (≤80 words):** Summarized Kuaishou's causal toolkit for product and recommendation evaluation, including modified difference-in-differences, synthetic control, double machine learning, causal forests, uplift learners, causal graphs, bilateral randomization, and switchback experiments. Live-streaming examples illustrate when cross-side or temporal spillovers make ordinary user-level A/B tests invalid.
- **Mechanism relevant to two-sided balancing (≤50 words):** Randomize both marketplace populations to measure cross-side spillovers, or rotate a market-wide policy across time slices when interacting users contaminate one another's assignments.
- **Metrics and reported effect:** Not specified in source.
- **Dating-app fit:** Medium — interference-aware designs transfer, but capacity, reciprocal matches, and dating outcomes are absent.
- **Confidence:** High on source identity and described methods; low on effect magnitude because no quantitative evidence is reported.


