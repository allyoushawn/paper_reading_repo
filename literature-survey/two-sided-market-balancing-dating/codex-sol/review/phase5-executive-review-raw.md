# Phase 5 CLI Review Raw Transcript

- Transport: Cursor CLI fallback after Codex CLI gpt-5.6-sol/high returned a usage-limit error
- Cursor model: gpt-5.6-sol-high
- Mode: ask (read-only)
- Exit code: 0

## 1. PROOF OF READING

| Input basename | Specific fact |
|---|---|
| `literature-review.md` | The bibliography contains 45 references, with Tier 1+2 comprising 39/45 (86.7%); final heading: `## D8 — Chinese and Japanese sources (4)`; final substantive statement: “Confidence is High on source identity and described methods; low on effect magnitude because no quantitative evidence is reported.” |
| `method-tracker.md` | Every method receives performance-consistency score 0 because no two measurements share a comparable dataset, metric, cutoff, treatment, and market setting; final heading: `## Cross-Paper Comparability Limitations`; final substantive statement: “Consequently, numeric minima/maxima are reported only when a genuinely comparable range exists. Here none meets that standard; `0` consistency and `Not established` are deliberate conservative judgments, not evidence of inconsistency.” |
| `README.md` | Each impression is framed as consuming both viewer attention and the shown person’s reply capacity. |
| `requirements.md` | The NLM run requests 60–100 references, while prioritizing the ≥60% Tier 1+2 mix over merely reaching the count. |
| `discovery-notes.md` | NotebookLM grew from 141 to 143 sources through one Wantedly source and one shadow-price source. |
| `2009_OkTrends_NA_Your-Looks-and-Your-Inbox.md` | Two-thirds of male messages went to the top third of women, but the observational post provides no uncertainty estimates. |
| `2010_AER_GaleShapley_Matching-and-Sorting-Online-Dating.md` | Male/female first contacts were unrequited 71%/56% of the time and converted to matches at 4.3%/6.4%. |
| `2013_UMUAI_RECON_Recommending-People-To-People.md` | RECON achieved S@10 of 42.20% versus 23.00% for unilateral recommendation on proprietary dating logs. |
| `2014_KDD_ImpressionDiscounting_Modeling-Impression-Discounting.md` | The LinkedIn PYMK dataset contained 1.08 billion impressions, and live invitation P@10 rose 13.26% ± 0.2%. |
| `2015_ASONAM_RRS_Reciprocal-Recommendation-Online-Dating.md` | Baihe reply rates were 9.5% male-to-female and 17.9% female-to-male, but exact reciprocal-ranking lifts were not tabulated. |
| `2015_ExpEcon_VirtualRose_Propose-With-A-Rose.md` | A randomized 613-user experiment estimated a 3.3-point acceptance increase from attaching a rose. |
| `2017_CIKM_CapMF_Recommendation-Capacity-Constraints.md` | Its capacities are synthetic because the four public datasets contain no ground-truth item capacity. |
| `2017_KDD_LiJAR_Job-Application-Redistribution.md` | LiJAR shifted applications +6.5% toward underserved jobs and −8.7% from overserved jobs while total applications changed by a nonsignificant +2.3%. |
| `2017_MLconf_TinVec_Personalized-User-Recommendations-Tinder.md` | TinVec reported 90% AUROC and 85% F1 but no baseline comparison or mutual-match evaluation. |
| `2018_CIKM_Adaptive-Fairness_Fair-Marketplace-Counterfactual-Evaluation.md` | Adaptive-II estimated satisfaction of 0.729 versus 0.650 for relevance-only using propensity-weighted randomized Spotify logs. |
| `2018_KDD_NA_Fairness-of-Exposure-Rankings.md` | In a six-person job example, disparate-treatment ratio reached 1.0000 while DCG fell from 3.8193 to 3.8044. |
| `2018_MgmtSci_ChoiceRestriction_Competing-By-Restricting-Choice.md` | The theoretical rejection probability is `N/(N+1)` when each user sees `N` candidates. |
| `2018_SciAdv_PageRank_Aspirational-Pursuit-of-Mates.md` | PageRank used damping 0.85, and men and women contacted users 26% and 23% higher in desirability. |
| `2019_KDD_DetGreedy_Fairness-Aware-Ranking-Talent-Search.md` | A three-week LinkedIn test raised representative queries from 33% to 95% without significant InMail changes. |
| `2019_Tinder_NA_Powering-Tinder-Matching.md` | Tinder identifies recent and simultaneous activity as its most important disclosed ranking factor but reports no effect size. |
| `2020_KDD_Query-Context-Embedding_Managing-Diversity-Airbnb-Search.md` | Its LSTM reranker raised bookings 0.44%, whereas some simpler diversification treatments produced harmful online results. |
| `2021_DataFunTalk_BilateralSwitchback_Kuaishou-Causal-Experiment-Design.md` | It describes bilateral randomization and carryover-aware switchbacks but supplies no sample sizes or quantitative outcomes. |
| `2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md` | Its nearly 70% CCR success and 14–17% RRK gains are secondary reports requiring verification in the original studies. |
| `2021_MSOM_ApplicationLimits_Managing-Congestion-Matching-Markets.md` | A single application cap theoretically guarantees each side at least 75% of its constrained-efficient welfare maximum. |
| `2021_MS_NA_Facilitating-Search-for-Partners.md` | Under a 2:1 imbalance, directional search raises modeled long-side utility up to 31% but can reduce short-side utility. |
| `2021_NeurIPS_LorenzWelfare_Two-Sided-Fairness-Lorenz-Dominance.md` | Raising bottom-decile utility from 120 to 280 reduced total utility from 17,000 to 6,400. |
| `2021_NeurIPS_UniCoRn_AB-Testing-Two-Sided-Marketplace.md` | LinkedIn ran UniCoRn on a 40% viewer-side traffic ramp and reported all disclosed online effects at p<0.001. |
| `2021_arXiv_SMRD_Multiple-Randomization-Designs.md` | In simulation, single-sided estimation produced the wrong profit-effect sign while SMRD recovered the positive effect. |
| `2022_CyberAgent_DoubleSelection_Analyzing-Encounters-Matching-Apps.md` | Tapple reported recommendation recall of 0.9 for men and 0.2 for women. |
| `2022_CyberAgent_MTRS_Matching-Theory-Reciprocal-Recommendation.md` | The blog reports no quantitative evaluation of CyberAgent’s own scalable matching approximation. |
| `2022_LinkedIn_LiFT-Platform_LinkedIn-Integrates-Fairness-AI.md` | LinkedIn’s workflow separates disparity analysis, mitigation training, post-score correction, and online validation, but reports no outcomes. |
| `2022_MgmtSci_TSRI_Experimental-Design-Two-Sided-Platforms.md` | TSRI-2 lowered simulated normalized bias to about 0.08 but raised normalized standard error to about 0.19. |
| `2022_OR_NA_Assortment-Two-Sided-Sequential-Matching.md` | Simulations used 100 suppliers and achieved 0.37–0.47 of a relaxed match-count upper bound. |
| `2022_RecSys_DPGNN_Two-Way-Selection-Person-Job.md` | DPGNN improved most reported metrics but lost to LGCNBERT on two Design-candidate ranking metrics. |
| `2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md` | At fairness weight one, GG-F improved significantly while MovieLens NDCG@50 declined by 0.0011 and 0.0005. |
| `2022_arXiv_MTRS_Matching-Theory-Online-Dating.md` | The Tapple system targets over seven million registered users but discloses no quantitative outcome or latency result. |
| `2022_arXiv_SP_Marketplace-Interference-Shadow-Prices.md` | Its strongest results are simulations of centrally optimized taxi and supply-chain markets, not decentralized reciprocal choice. |
| `2023_KDD_BOSS_Bilateral-Occupational-Suitability.md` | A live recruitment test reported 6.15% higher acceptance, but traffic allocation and uncertainty were undisclosed. |
| `2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md` | Distillation reduced reported prediction latency from roughly 8.7 ms to 0.28 ms per batch. |
| `2023_RecSys_TU_Fast-Examination-Agnostic-Reciprocal.md` | Under absolute popularity concentration, TU collapsed to 91.28 expected matches while the social-welfare comparator reached 117.30. |
| `2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems.md` | Libimseti “matches” are mutual ratings of at least eight rather than observed conversations or dates. |
| `2024_MarketingScience_SequentialSearch_Effects-Market-Size-Competition.md` | The randomized effects concern displayed market-size beliefs; the +136.3%/+121.6% cap results are structural counterfactuals. |
| `2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md` | On a 200×200 dating sample, NSW reduced envy sharply but produced 90.39 rather than 111.37 expected matches. |
| `2025_Hinge_DeepRecSys_How-We-Connect-Daters.md` | Hinge describes bilateral dealbreakers and mutual-interest prediction but provides no quantitative result or page publication date. |
| `2025_MgmtSci_GCR_Reducing-Interference-Bias-Airbnb.md` | A five-day, 2.6-million-listing meta-experiment estimated 19.76% interference bias for one pricing treatment. |
| `2025_RecSys_DiPS-DPR_Off-Policy-Evaluation-Matching-Markets.md` | DPR had lower MSE, but DiPS and IPS had lower policy-selection error—a consequential estimator-ranking reversal. |
| `2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md` | Only abstract-level evidence is available: no retention horizon, magnitude, sample size, or significance result is given. |
| `2026_Wantedly_PersonalizedAggregation_Personalizing-Preference-Aggregation.md` | Personalized harmonic aggregation increased unique recommendations 16.8% while reducing both reported nDCG measures. |
| `2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md` | Its strongest field effects require excluding the most congested 0.1%, and messaging remained unchanged. |
| `2026_arXiv_TEC_Recommendation-Exposure-Favorite-Lists.md` | The field design uses only one treated and one control prefecture, limiting uncertainty estimation despite a +9.045 matches/prefecture-day estimate. |

## 2. DECISION-MAKER SYNTHESIS

1. Require bilateral success evidence before allocating exposure because unilateral relevance sends traffic toward users unlikely to reciprocate—*Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating* (2013).
2. Budget exposure against recipient-side expected likes or downstream interactions, while treating the available two-region field evidence as provisional—*Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach* (2026).
3. Use market-wide demand adjustments when independent reciprocal scores concentrate opportunity, recognizing that current dating evidence is offline and model-based—*Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets* (2023).
4. Test scarce priority signals as recipient-attention aids because randomized dating evidence shows higher acceptance without proving retention gains—*Propose with a Rose? Signaling in Internet Dating Markets* (2015).
5. Treat like limits and perceived market thickness as coupled market-state levers, separating randomized belief effects from structural cap simulations—*Effects of Market Size and Competition in Two-Sided Markets: Evidence from Online Dating* (2024).
6. Measure distinct reciprocal successes and vacant-slot opportunity rather than counting two independent top-k hits—*Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method* (2024).
7. Assign interacting substitutes together when testing market-wide changes because individual randomization can materially distort effects—*Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization: Evidence from a Pricing Meta-Experiment on Airbnb* (2025).

## 3. TOP FIVE METHODS CHECK

| Rank | Tracker’s exact method | Composite |
|---:|---|---:|
| 1 | Dual-Perspective Graph Neural Network (DPGNN) | 8 |
| 2 | Transferable-Utility reciprocal ranking (consolidated MTRS/TU + IPFP/MIPS) | 8 |
| 3 | RECON harmonic reciprocal scoring | 6 |
| 4 | Exposure-fair probabilistic ranking (LP + Birkhoff-von Neumann decomposition) | 6 |
| 5 | Personalized reciprocal weighted-harmonic aggregation (Kleinerman method; Ichimura reproduction) | 6 |

This ranking is structurally uncertain, not evidence-robust: every performance-consistency score is zero, reuse counts are tiny, incompatible outcomes cannot be pooled, simplicity materially affects scores, and tie-breaking partly invokes survey usefulness outside the formula.

It should be presented as a lineage/fundamentality audit—not as a product-priority ranking or evidence that DPGNN is superior to lower-ranked capacity and evaluation methods.

## 4. RECOMMENDATIONS

- Reciprocal scoring: require side-specific calibration and report the full view→like→like-back→conversation funnel rather than unilateral top-k accuracy.
- Capacity allocation: define operational capacity first—reply bandwidth, concurrent conversations, or expected productive interactions—and track demand relative to that capacity by recipient and market segment.
- Allocation policy: set exposure budgets or pacing against current capacity with a relevance guardrail, and audit both overdelivery and underdelivery.
- Market-design levers: separately test scarce signals, like limits, curated batches, filter gating, and initiation rules; effects are likely conditional on imbalance, screening costs, and market thickness.
- Metrics: jointly monitor total matches, conversations, share of users with ≥1 match/conversation, Gini/Lorenz distribution, entropy/coverage, unrequited or wasted likes, effective interactions, and retention on both sides.
- Evaluation: select two-sided randomization, competitive-neighborhood clustering, or regional/time switchbacks according to where spillovers occur; use reciprocal OPE for screening policies, not as a replacement for live interference-aware tests.
- Decision process: predeclare throughput–distribution–retention trade-offs and examine effects by side, popularity/load bucket, geography, activity, and new-versus-established user status.

## 5. EVIDENCE LIMITS AND CORRECTIONS

- The 60–100-reference NLM floor is unmet: this output selects 45; the separate cursor-grok run’s 72 items does not make this bibliography complete.
- Tier 1 is an industry-priority label, not an evidence-strength rating; company explainers without experiments must not be described as stronger evidence than randomized or peer-reviewed Tier 2 work.
- OkCupid’s 66% concentration, declining replies, and PageRank desirability patterns are observational; they do not causally show that redistribution raises matches, conversations, or retention.
- RECON’s 42.20% versus 23.00% is proprietary offline success-at-k evidence, not a live causal lift.
- LiJAR’s +6.5%/−8.7% redistribution and +12% entropy are job-market A/B outcomes; total applications rose a nonsignificant 2.3%, and dating matches are unsupported.
- The rose experiment causally supports acceptance by approximately 3.3 points, but its 48%/86% initiated-date quantities are subgroup treatment comparisons and do not establish conversation quality, welfare, or retention.
- Fong’s −2%/+3% belief effects are randomized, whereas −12.2%/−17.7% and +136.3%/+121.6% are structural counterfactuals, not experimentally observed cap effects.
- TU’s expected-match and Gini quantities are probability-model outputs on dense subsets, not realized production outcomes; the method also fails under one extreme concentration setting.
- NSW’s match/envy frontier is an offline 200×200 k-core result and does not show that lower envy improves retention.
- CRRS’s 1,743 “pairs” use mutual Libimseti ratings as a match proxy and provide no conversation or capacity evidence.
- ECDA’s field quantities—+0.003 effective dates, +0.002 proposer probability, and +0.005 receiver probability—are conditional on trimming the top 0.1%, come from only two regions, and accompany zero messaging lift.
- TEC’s +9.045 matches/prefecture-day comes from one treated and one control prefecture; several favorite, subscriber, and fill outcomes were null.
- Airbnb’s 19.76% interference estimate is specific to one short pricing meta-experiment and cannot be quoted as the expected bias in dating.
- Tapple’s 2%/36% age-verification effects use observational double-selection, while the Gini 0.75→0.60 result is secondhand; neither should be presented as a causal balancing result.
- CyberAgent MTRS, Tinder, Hinge, LinkedIn LiFT, and Kuaishou disclose mechanisms but no quantitative effectiveness evidence.
- MRet’s claimed retention improvement has no magnitude, horizon, uncertainty, protocol, or named baseline values and should not support a quantified recommendation.
- “Nonsignificant NDCG degradation” in JME is not evidence of equivalence or zero utility cost.
- Bibliographic citations should disclose that Fong, Halaburda et al., Kanoria–Saban, and some Operations Research/M&SOM links are earlier working versions whose displayed title, author name, venue, or year differs from the cited publication.
- Remove workflow artifacts such as “To run experiments…” from the final reader-facing bibliography.

## 6. COVERAGE CHECK

- Request outputs: the reference list, per-reference fields, synthesis, gaps, next searches, design matrix, and read-first list exist; a distinct one-page executive summary is absent, and the bibliography is below the requested NLM count.
- Core Keywords: all six appear substantively, but hard capacity-constrained dating evidence is thin and “dating-app recommendation” frequently relies on job, music, lodging, or spot-work transfer.
- Must-Include A: absent as selected cards are Hinge “Most Compatible,” Hinge’s Gini analysis, eHarmony’s “Data Science of Love,” the Coffee Meets Bagel infrastructure case, and Bumble Tech; Bumble is at least documented as a null.
- Must-Include B: absent are “Recommendations in a Marketplace,” “How Airbnb uses Machine Learning to Detect Host Preferences,” and “Real-time Personalization using Embeddings for Search Ranking at Airbnb.”
- Must-Include C: absent are “Improving Match Rates in Dating Markets Through Assortment Optimization”—notably the seed claiming 25%+ more matches—and “Online Dating Recommendations: Matching Markets and Learning Preferences.”
- Must-Include D: absent are Lyft’s “Using Marketplace Marginal Values to Address Interference Bias” and DoorDash’s “Experiment Rigor for Switchback Experiment Analysis.”
- Must-Include E: absent as direct cards are “Optimally Balancing Receiver and Recommended Users’ Importance in Reciprocal Recommender Systems,” “RECON: A Reciprocal Recommender for Online Dating,” and “Latent Factor Models and Aggregation Operators for Collaborative Filtering in Reciprocal Recommender Systems”; Kleinerman is represented only indirectly.
- D1: strong reciprocal-method coverage, but little live dating evidence beyond qualitative production descriptions.
- D2: thin—only five primary entries and mostly exposure fairness rather than empirically calibrated market health.
- D3: thin—four primary entries, with no validated reply/conversation-capacity measure.
- D4: thin—four primary entries and little direct dating field evidence.
- D5: broad theory plus one strong signaling experiment, but most caps, menu restrictions, and initiation policies lack direct causal deployment evidence.
- D6: match distribution is covered, while conversations, wasted likes, share with ≥1 match, and two-sided retention are sparse.
- D7: strong adjacent-market methodology, but no validated interference design for a symmetric dating market.
- D8: Japanese industry coverage is useful; official Chinese dating-ranking engineering evidence is absent, and Kuaishou is an adjacent experimentation source.
- Project Context: all four layers are represented, but no study jointly estimates like-back probability conditioned on actual receiver capacity, allocates exposure, and measures conversations plus two-sided retention under interference.

