Date: 2026-08-19 (last updated)
Topic: two-sided market balancing in dating-app recommendation: reciprocal recommendation, exposure allocation under capacity limits, congestion in matching markets

# Methodology Fundamentality Tracking

## Methodology Table

| Method Name | Proposal Paper (Year) | Baseline Mention Count | Derived Variant Count | Independent Measured Performance (Dataset: metric \| source) | Component Count | Simplicity Score (1-5) | Performance Consistency Score (0–5; 0 = Not established) | Fundamentality Composite Score |
|---|---|---:|---:|---|---:|---:|---:|---:|
| Dual-Perspective Graph Neural Network (DPGNN) | Yang et al., *Modeling Two-Way Selection Preference for Person-Job Fit* (2022) | 2 | 0 | Tech candidate/job Recall@5 0.2941/0.3430 (Yang et al. 2022); Technology candidate HR@5 0.4521 as a ReSeq comparator (Zheng et al. 2023); Libimseti CRecall@50 0.3007 and 1,548 pairs as a CRRS comparator (Yang et al. 2024) | 5 | 2 | 0 | 8 |
| Transferable-Utility reciprocal ranking (consolidated MTRS/TU + IPFP/MIPS) | Tomita et al., *Matching Theory-Based Recommender Systems in Online Dating* (2022) | 1 | 1 | Tapple deployment description: quantitative outcomes not specified (Tomita et al. 2022); synthetic n=100: 152.39 expected matches and dating 1,000x1,000: 538.97/386.64 (Tomita et al. 2023); dating 200x200: 102.69/62.47 under log/inverse examination as the TU baseline (Tomita & Yokoyama 2024) | 4 | 3 | 0 | 8 |
| RECON harmonic reciprocal scoring | Pizzato et al., *Recommending People to People* (2013) | 1 | 0 | Commercial dating: S@10 42.20% vs. 23.00% unilateral; R@100 10.80% vs. 5.90%; S@1 with negative preference 37.46% vs. 31.78% (Pizzato et al. 2013); used as a named baseline by Xia et al. (2015), whose exact lift over RECON is not specified | 4 | 3 | 0 | 6 |
| Exposure-fair probabilistic ranking (LP + Birkhoff-von Neumann decomposition) | Singh & Joachims, *Fairness of Exposure in Rankings* (2018) | 0 | 1 | Job example: DTR 1.7483→1.0000 with DCG 3.8193→3.8044; DIR 1.8193→1.0000 with DCG 3.8025 (Singh & Joachims 2018); JME explicitly extends its exposure-fairness formulation (Wu et al. 2022) | 3 | 4 | 0 | 6 |
| Personalized reciprocal weighted-harmonic aggregation (Kleinerman method; Ichimura reproduction) | Kleinerman et al., *Optimally Balancing Receiver and Recommended Users' Importance in Reciprocal Recommender Systems* (2018) | 0 | 1 | Wantedly Visit reproduction: apply nDCG@10 -2.4%, matching-success nDCG@10 -3.3%, unique recommendations@10 +16.8% vs. fixed weights (Ichimura 2026) | 3 | 4 | 0 | 6 |
| Application-limit mean-field congestion control | Arnosti et al., *Managing Congestion in Matching Markets* (2021) | 0 | 0 | Simulated equilibrium: applicant welfare approximately 2× at r=1.4 and 3× at r=1.9; one cap guarantees both sides at least 75% of constrained-efficient maxima | 2 | 5 | 0 | 5 |
| Scarce preference signaling (virtual roses) | Lee & Niederle, *Propose with a Rose?* (2015) | 0 | 0 | Korean dating field experiment: acceptance +3.3 pp (20% relative; IV +4.1 pp); eight vs. two roses increased initiated dates +48% for verified Seoul men and +86% for women | 2 | 5 | 0 | 5 |
| Directional-search action restriction | Kanoria & Saban, *Facilitating the Search for Partners on Matching Platforms* (2021) | 0 | 0 | Synthetic equilibrium: average welfare up to +14.6%; at 2:1 imbalance, long-side utility up to +31%, average welfare up to +10%, short-side loss <8% | 1 | 5 | 0 | 5 |
| Attractiveness-stratified message/reply diagnostic | Rudder, *Your Looks and Your Inbox* (2009) | 0 | 0 | OkCupid: two-thirds of male messages to the top third of women; top women receive nearly 5× typical and 28× low-end messages; top men receive 11× the lowest-rated men; heavily messaged users reply less | 2 | 5 | 0 | 5 |
| Bilateral two-population marketplace experiment | Jin, *Kuaishou Causal Inference and Experimental Design* (2021) | 0 | 0 | Not specified in source. | 2 | 5 | 0 | 5 |
| TinVec | Liu, *Personalized (User) Recommendations at Tinder* (2017) | 0 | 0 | Tinder swipe prediction: AUROC 90%, F1 85% (Liu 2017); baseline lift not specified | 2 | 5 | 0 | 5 |
| Directed PageRank desirability + signed desirability gap | Bruch & Newman, *Aspirational Pursuit of Mates* (2018) | 0 | 0 | Four-city dating logs: men/women target 26%/23% higher desirability; men's upward reply probability never exceeds 21% | 2 | 5 | 0 | 5 |
| Bilateral Occupational-Suitability-aware recommender System (BOSS) | Hu et al., *BOSS* (2023) | 0 | 0 | Technology: AUC 0.8918 ± 0.0021; live Information Technology acceptance rate +6.15% (Hu et al. 2023) | 3 | 4 | 0 | 4 |
| ProML/LiFT model-agnostic fairness post-processing | Logan et al., *A Closer Look at How LinkedIn Integrates Fairness into Its AI Products* (2022) | 0 | 0 | Not specified in source. | 3 | 4 | 0 | 4 |
| Lorenz-efficient concave-welfare reciprocal ranking (LorenzWelfare) | Do et al., *Two-Sided Fairness in Rankings via Lorenz Dominance* (2021) | 0 | 0 | Twitter-13k: bottom-10% cumulative utility 120→280 while total utility 17,000→6,400 at alpha=-5; dominates equality-of-utility near strict equality | 3 | 4 | 0 | 4 |
| Impression Discounting (behavioral decay + density-weighted regression) | Lee et al., *Modeling Impression Discounting in Large-Scale Recommender Systems* (2014) | 0 | 0 | LinkedIn PYMK: offline P@10 +31.3%; live invitation P@10 +13.26% ± 0.2%; regression RMSE 0.1121→0.0188 | 3 | 4 | 0 | 4 |
| Capacity-regularized matrix factorization/ranking (CapMF/CapBPR) | Christakopoulou et al., *Recommendation with Capacity Constraints* (2017) | 0 | 0 | MovieLens100K Cap-BPR: capacity loss 4.51→0.08, pairwise loss 0.12→0.14; Foursquare Cap-GeoBPR: 0.81→0.02 and 0.31→0.28 | 3 | 4 | 0 | 4 |
| DetGreedy representative re-ranking | Geyik et al., *Fairness-Aware Ranking in Search & Recommendation Systems* (2019) | 0 | 0 | LinkedIn Recruiter: representative queries 33%→95%, MinSkew@100 -0.259→-0.011 (p<1e-16), InMails sent/accepted unchanged | 3 | 4 | 0 | 4 |
| Symmetric choice-set restriction + outside-option self-selection | Halaburda et al., *Competing by Restricting Choice* (2018) | 0 | 0 | Analytical rejection probability N/(N+1); simulations: low-outside-option utility peaks near N=2, higher-outside-option utility near N=3 | 3 | 4 | 0 | 4 |
| Belief-sensitive sequential search + like-limit control | Fong, *Effects of Market Size and Competition in Two-Sided Markets* (2024) | 0 | 0 | Live belief experiment: perceived market size +50% yielded -2% matches; perceived competition +50% yielded +3%; structural small-market growth with doubled caps yielded +136.3%/+121.6% matches by side | 3 | 4 | 0 | 4 |
| Matching for Retention (MRet) | Kishimoto et al., *Beyond Match Maximization and Fairness* (2026) | 0 | 0 | Synthetic and major dating-platform data: higher user retention than match-maximization and fairness baselines; quantitative effect not specified | 3 | 4 | 0 | 4 |
| Demand-embedding graph cluster randomization (GCR) | Holtz et al., *Reducing Interference Bias in Online Marketplace Experiments* (2025) | 0 | 0 | Airbnb 2,602,782 listings: booking effect -0.277 clustered vs. -0.345 individual; interaction -0.068 (SE 0.018), implying 19.76% interference bias | 3 | 4 | 0 | 4 |
| Unifying Counterfactual Rankings (UniCoRn) | Nandy et al., *A/B Testing for Recommender Systems in a Two-Sided Marketplace* (2021) | 0 | 0 | LinkedIn live: candidate generation WAU +0.51%, sessions +0.57%; viewee-retention ranker +0.13%/+0.11%; all p<0.001 | 3 | 4 | 0 | 4 |
| Direct-and-Propensity / Direct-Propensity-Robust OPE (DiPS/DPR) | Hayashi et al., *Off-Policy Evaluation and Learning for Matching Markets* (2025) | 0 | 0 | Wantedly 21,736 companies/17,460 job seekers, 1.2% matches: DPR significantly lower MSE across almost all sizes; DiPS/IPS lower selection error than DPR/DR | 3 | 4 | 0 | 4 |
| Shadow Price (SP) marketplace-interference estimator | Bright et al., *Reducing Marketplace Interference Bias Via Shadow Prices* (2022) | 0 | 0 | NYC taxi simulation: standard RCT misses an efficiency gain up to 20% smaller than demand growth; undersupplied supply chain: RCT overstates effect magnitude by more than 2×; SP substantially reduces bias | 3 | 4 | 0 | 4 |
| High-dimensional double-selection causal adjustment | Kazumi, *Analyzing Encounters on Matching Apps* (2022) | 0 | 0 | Tapple: official age verification associated with statistically significant message-approval lifts of +2% for men and approximately +36% for women | 3 | 4 | 0 | 4 |
| Carryover-aware switchback experiment | Jin, *Kuaishou Causal Inference and Experimental Design* (2021) | 0 | 0 | Not specified in source. | 3 | 4 | 0 | 4 |
| Alternating Nash Social Welfare reciprocal allocation (NSW) | Tomita & Yokoyama, *Fair Reciprocal Recommendation in Matching Markets* (2024) | 0 | 0 | Dating 200x200: 90.39 matches and 31/14 envies (log); 59.37 matches and 19/8 envies (inverse) | 4 | 3 | 0 | 3 |
| Causal Reciprocal Recommender System (CRRS) | Yang et al., *Revisiting Reciprocal Recommender Systems* (2024) | 0 | 0 | Libimseti: CRecall@50 0.3387 and 1,743 TP pairs with LightGCN; recruitment: CRecall@50 0.3968 and 8,913 TP pairs with BPRMF | 4 | 3 | 0 | 3 |
| Reciprocal Sequential Recommendation (ReSeq) | Zheng et al., *Reciprocal Sequential Recommendation* (2023) | 0 | 0 | Technology: candidate/recruiter HR@5 0.7597/0.7809; Design: 0.4435/0.3722 (Zheng et al. 2023) | 4 | 3 | 0 | 3 |
| Bipartite interest/attractiveness reciprocal CF (CF1–CF4) | Xia et al., *Reciprocal Recommendation System for Online Dating* (2015) | 0 | 0 | Baihe: higher I-Precision/I-Recall and R-Precision/R-Recall than HCF; exact lifts not specified | 4 | 3 | 0 | 3 |
| Adaptive supplier-fairness policy + IPS evaluation | Mehrotra et al., *Towards a Fair Marketplace* (2018) | 0 | 0 | Spotify: satisfaction 0.709 (+9.0%) Adaptive-I and 0.729 (+12.1%) Adaptive-II vs. relevance-only 0.650 | 4 | 3 | 0 | 3 |
| Joint Multisided Exposure (JME) fairness optimization | Wu et al., *Joint Multisided Exposure Fairness for Recommendation* (2022) | 0 | 0 | MovieLens100K/1M: GG-F significantly improved at alpha=1 (p<0.01); NDCG@50 0.3703→0.3692 / 0.2741→0.2736, degradation not significant | 4 | 3 | 0 | 3 |
| Query Context Embedding (LSTM listwise diversification) | Abdool et al., *Managing Diversity in Airbnb Search* (2020) | 0 | 0 | Airbnb: +1.97% offline MLR, +1.26% offline NDCG; +1.2% online NDCG, +0.44% bookings, +0.61% new-guest bookings | 4 | 3 | 0 | 3 |
| LiJAR cumulative-demand forecasting + score intervention | Borisyuk et al., *LiJAR* (2017) | 0 | 0 | LinkedIn live: underserved applications +6.5%, overserved -8.7%, total +2.3% (not significant), distribution entropy +12% | 4 | 3 | 0 | 3 |
| Collision-aware assortment planning (bucketing + LP + rounding) | Ashlagi et al., *Assortment Planning for Two-Sided Sequential Matching Markets* (2022) | 0 | 0 | Synthetic 100-supplier markets: mean ALG/UB match ratio 0.37–0.47 and minimum at least 0.33 across tested instances | 4 | 3 | 0 | 3 |
| Fixed-effects bilateral preference estimation + Gale-Shapley benchmark | Hitsch et al., *Matching and Sorting in Online Dating* (2010) | 0 | 0 | Boston/San Diego logs: 71%/56% male/female first contacts unrequited; 4.3%/6.4% convert to matches; decentralized achieved-rank gap 4.6%/3.8% of maximum | 4 | 3 | 0 | 3 |
| Hinge reciprocal deep-learning recommendation + bilateral dealbreaker gating | Hinge, *How We Connect Daters* (2025) | 0 | 0 | Not specified in source. | 4 | 3 | 0 | 3 |
| Two-Sided Randomization with improved interference correction (TSRI-2) | Johari et al., *Experimental Design in Two-Sided Platforms* (2022) | 0 | 0 | Simulated 5,000-listing balanced market: normalized absolute bias about 0.08 vs. 0.20–0.22 for CR/LR/TSRN; normalized SE about 0.19 vs. 0.08–0.10 | 4 | 3 | 0 | 3 |
| Simple Multiple Randomization Design (SMRD) | Masoero et al., *Multiple Randomization Designs* (2021) | 0 | 0 | Strategic 200×150 market, 10,000 rerandomizations: correct positive profit sign where single-sided design is negative; buyer-spillover null rejected 99.5% | 4 | 3 | 0 | 3 |
| Tinder dynamic activity-first ranking | Tinder, *Powering Tinder — The Method Behind Our Matching* (2019) | 0 | 0 | Not specified in source. | 5 | 2 | 0 | 2 |
| Thresholded Eligibility Control (TEC) | Sekiya et al., *Designing Recommendation Exposure and Favorite Lists* (2026) | 0 | 0 | Timee simulation: job-finding 57.61%→70.03%, fill 67.42%→82.17%; field: +9.045 matches/prefecture-day (p<0.05), low-exposure tail -6.1 pp | 5 | 2 | 0 | 2 |
| Exposure-Constrained Deferred Acceptance (ECDA) + effective dates | Sekiya et al., *Integrating Predictive Models into Two-Sided Recommendations* (2026) | 0 | 0 | CoupLink simulation: effective dates +7.6%, receiver dating probability +8.7%, raw dates -24.6%; field excluding top 0.1%: effective dates +0.003 (p<0.05), proposer/receiver probability +0.002/+0.005 | 5 | 2 | 0 | 2 |

## How the Scores Were Finalized

Fundamentality composite score = `(baseline mention count × 3) + (derived variant count × 2) + simplicity score + (performance consistency score × 2)`.

- Baseline mention count includes only a method explicitly named as an experimental comparator in another card. It excludes related-work citations and conceptual comparisons. The countable evidence is DPGNN in Zheng et al. (2023) and Yang et al. (2024), TU in Tomita and Yokoyama (2024), and RECON in Xia et al. (2015).
- Derived variant count includes only another paper that explicitly modifies, extends, or reproduces the method: the 2023 scalable TU/IPFP/MIPS continuation of the 2022 MTRS system; Wu et al.'s 2022 JME extension of exposure fairness; and Ichimura's 2026 reproduction of Kleinerman et al.'s personalized aggregation.
- Simplicity follows the template mapping: 1–2 components = 5, 3 = 4, 4 = 3, 5 = 2, and 6+ = 1. Components are coarse deployable blocks described in the cards, not parameter counts.
- Performance consistency is `0` for every row, meaning **Not established**. No method has at least two independent measurements with the same dataset definition, metric, cutoff, treatment, and market setting, so applying the template's standard-deviation bands would manufacture comparability. Reported results remain in the evidence column without being converted into a consistency claim.
- The table is sorted by descending baseline mention count, then by composite score and method name for deterministic ties. Top-10 ties use baseline mentions, variants, then direct usefulness to this survey's industry-first market-balancing layers; the formula itself is unchanged.

## Industry-First Usefulness Map

The score measures cross-paper fundamentality, not product priority. For implementation triage: DPGNN, TU, RECON, and personalized harmonic aggregation are reciprocal-scoring patterns; LiJAR, CapMF/CapBPR, TEC, ECDA, and application limits are capacity-aware patterns; exposure-fair LP, DetGreedy, Lorenz welfare, JME, and collision-aware assortment are constrained reranking/allocation patterns; roses, directional search, choice restriction, and like limits are market-design levers; OkCupid concentration, PageRank desirability gaps, Lorenz/Gini, entropy, coverage, and effective dates are ecosystem metrics; bilateral randomization, switchbacks, TSRI-2, SMRD, GCR, UniCoRn, DiPS/DPR, and shadow prices are evaluation methods for interference or logged policies.

## Top Method Analysis

### Rank 1: Dual-Perspective Graph Neural Network (DPGNN) (Composite Score: 8)

- Why fundamental: It is the corpus's most frequently reused named baseline and cleanly separates outgoing taste from incoming appeal, making it a useful reciprocal-scoring backbone before capacity-aware allocation.
- Representative paper: Chen Yang, Yupeng Hou, Yang Song, Tao Zhang, Ji-Rong Wen, and Wayne Xin Zhao, *Modeling Two-Way Selection Preference for Person-Job Fit*, RecSys 2022.
- Papers using it as a baseline: Bowen Zheng et al., *Reciprocal Sequential Recommendation*, RecSys 2023; Chen Yang et al., *Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method*, KDD 2024.
- Known variants: Not established as direct descendants in the cards; ReSeq and CRRS are successor comparisons, not counted as DPGNN variants.
- Independent measured performance range: Not established. Recall@5, HR@5, and CRecall@50 are not comparable; the evidence column preserves each value separately.

### Rank 2: Transferable-Utility Reciprocal Ranking (MTRS/TU + IPFP/MIPS) (Composite Score: 8)

- Why fundamental: It turns bilateral preferences and market-wide demand pressure into retrieval-compatible market-clearing scores, directly joining reciprocal and capacity-aware scoring.
- Representative paper: Yoji Tomita, Riku Togashi, Yuriko Hashizume, and Naoto Ohsaka, *Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets*, RecSys 2023.
- Papers using it as a baseline: Yoji Tomita and Tomohiko Yokoyama, *Fair Reciprocal Recommendation in Matching Markets*, RecSys 2024.
- Known variants: The 2022 MTRS system description and the 2023 examination-agnostic TU formulation with IPFP and augmented MIPS are consolidated here; the latter is the one counted continuation.
- Independent measured performance range: Not established. Expected-match totals span different market sizes, proactive sides, and examination functions and must not be pooled.

### Rank 3: RECON Harmonic Reciprocal Scoring (Composite Score: 6)

- Why fundamental: It is a simple, directly dating-tested bilateral scorer whose harmonic aggregation suppresses pairs with weak return interest and remains an explicit later baseline.
- Representative paper: Luiz Pizzato, Tomek Rej, Joshua Akehurst, Irena Koprinska, Kalina Yacef, and Judy Kay, *Recommending People to People: The Nature of Reciprocal Recommenders with a Case Study in Online Dating*, User Modeling and User-Adapted Interaction 2013.
- Papers using it as a baseline: Peng Xia et al., *Reciprocal Recommendation System for Online Dating*, ASONAM 2015.
- Known variants: Negative-preference suppression and priority weighting are within-paper configurations, not separately counted paper variants.
- Independent measured performance range: Not established; only the proposal paper reports compatible numeric outcomes, while Xia et al. do not provide an exact lift over RECON in the card.

### Rank 4: Exposure-Fair Probabilistic Ranking (LP + Birkhoff-von Neumann) (Composite Score: 6)

- Why fundamental: It supplies the canonical constrained-reranking primitive for allocating position exposure under explicit fairness constraints, though dating needs reciprocal utility and individual capacity constraints.
- Representative paper: Ashudeep Singh and Thorsten Joachims, *Fairness of Exposure in Rankings*, KDD 2018.
- Papers using it as a baseline: Not established under the strict explicit-comparator rule.
- Known variants: Haolun Wu et al., *Joint Multisided Exposure Fairness for Recommendation*, SIGIR 2022, explicitly extends the exposure-fairness formulation to consumer and producer groups.
- Independent measured performance range: Not established; the proposal's job/news DCG and fairness ratios are not comparable with JME's MovieLens NDCG and GG-F objective.

### Rank 5: Personalized Reciprocal Weighted-Harmonic Aggregation (Composite Score: 6)

- Why fundamental: It is a lightweight way to personalize the sender-versus-recipient trade-off and disperse traffic without requiring a global allocation solver.
- Representative paper: Arik Kleinerman, Ariel Rosenfeld, Francesco Ricci, and Sarit Kraus, *Optimally Balancing Receiver and Recommended Users' Importance in Reciprocal Recommender Systems*, RecSys 2018.
- Papers using it as a baseline: Not established.
- Known variants: Chiaki Ichimura, *An Attempt to Personalize Preference Aggregation in Reciprocal Recommendation*, Wantedly Engineer Blog 2026, reproduces the method with per-user Brent-optimized weights.
- Independent measured performance range: Not established; the corpus contains one independent reproduction, reporting -2.4% apply nDCG@10, -3.3% matching-success nDCG@10, and +16.8% unique recommendations@10.

### Rank 6: Application-Limit Mean-Field Congestion Control (Composite Score: 5)

- Why fundamental: A like/application cap is the simplest explicit market-design lever for protecting receiver screening capacity and reducing stale or wasteful proposals.
- Representative paper: Nick Arnosti, Ramesh Johari, and Yash Kanoria, *Managing Congestion in Matching Markets*, Manufacturing & Service Operations Management 2021.
- Papers using it as a baseline: Not established.
- Known variants: Not established.
- Independent measured performance range: Not established; the card contains one theoretical/numerical study, not independent field replications.

### Rank 7: Scarce Preference Signaling (Virtual Roses) (Composite Score: 5)

- Why fundamental: It is a low-complexity dating-native market-design lever with randomized evidence that scarce signals help capacity-limited recipients prioritize serious proposals.
- Representative paper: Soohyung Lee and Muriel Niederle, *Propose with a Rose? Signaling in Internet Dating Markets*, Experimental Economics 2015.
- Papers using it as a baseline: Not established.
- Known variants: Not established in the cards; Super-Like-style product mappings are inferences, not counted variants.
- Independent measured performance range: Not established; one field experiment reports +3.3 percentage points acceptance (IV +4.1 points) and larger initiated-date gains by treatment group.

### Rank 8: Directional-Search Action Restriction (Composite Score: 5)

- Why fundamental: It shows that choosing which side may initiate can reduce rejection congestion when screening costs or side sizes are asymmetric.
- Representative paper: Yash Kanoria and Daniela Saban, *Facilitating the Search for Partners on Matching Platforms: Restricting Agent Actions*, Management Science 2021.
- Papers using it as a baseline: Not established.
- Known variants: Not established.
- Independent measured performance range: Not established; the evidence is one analytical/numerical equilibrium study rather than independent empirical measurements.

### Rank 9: Attractiveness-Stratified Message/Reply Diagnostic (Composite Score: 5)

- Why fundamental: It provides a minimal ecosystem-health diagnostic for the exact failure mode at issue—attention concentration and declining reply propensity among overloaded recipients.
- Representative paper: Christian Rudder / OkCupid, *Your Looks and Your Inbox*, OkTrends company blog 2009.
- Papers using it as a baseline: Not established.
- Known variants: Not established.
- Independent measured performance range: Not applicable; this is an observational diagnostic, and the card reports concentration ratios rather than intervention performance.

### Rank 10: Bilateral Two-Population Marketplace Experiment (Composite Score: 5)

- Why fundamental: It is the simplest evaluation design in the tracker that explicitly randomizes both interacting populations to expose cross-side spillovers missed by ordinary user-level A/B tests.
- Representative paper: Yaran Jin, *Kuaishou Causal Inference and Experimental Design*, DataFunTalk technical-talk recap 2021.
- Papers using it as a baseline: Not established.
- Known variants: The same source separately describes carryover-aware switchbacks; that is a distinct temporal design and remains a separate tracker row.
- Independent measured performance range: Not established; the source provides no quantitative effect or bias-reduction estimates.

## Cross-Paper Comparability Limitations

- Outcomes are heterogeneous: swipe AUROC/F1, top-k retrieval metrics, expected matches, unique matched pairs, welfare, envy, exposure ratios, entropy, bookings, application acceptance, experiment bias, and retention are not on a common scale.
- Market units differ materially: one-sided suppliers, asymmetric job markets, symmetric dating users, sequential assortments, and centrally optimized marketplaces have different capacity and interference structures.
- Evidence strength ranges from production A/B tests and randomized dating experiments to offline replay, proprietary-log simulations, stylized examples, theory, and consumer-facing product descriptions.
- Dataset sizes, candidate cutoffs, examination functions, market balance, capacity definitions, and time horizons often differ even when metric names look similar.
- Consequently, numeric minima/maxima are reported only when a genuinely comparable range exists. Here none meets that standard; `0` consistency and `Not established` are deliberate conservative judgments, not evidence of inconsistency.
