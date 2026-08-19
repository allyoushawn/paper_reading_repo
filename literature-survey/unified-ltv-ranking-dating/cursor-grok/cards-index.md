# Compact survey-card index — cursor-grok — 120 references

## D7 | 2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md
- title: Modeling Delayed Feedback in Display Advertising
- url: https://arxiv.org/abs/1406.6035
- objective: Post-click conversion probability \(p(x)\) and conversion delay \(\lambda(x)\); 30-day attribution window; last-click attribution; first conversion per click only.
- pred_vs_inc: Predicts absolute conversion probability; not causal uplift of ad exposure.
- credit: Post-click attribution: conversion within 30 days mapped to clicked impression via shared user/advertiser ID; last-click wins; multiple conversions per click discarded (first kept).
- gains: Overall NLL 0.3960 vs Naive 0.4076 (~3% improvement); recent campaigns NLL 0.4006 vs Shifted 0.4176; Naive underpredicts conversions by 21%; DFM converges to true CVR after 2 days in toy simulation (mean delay 4 days).

## D2 | 2017_CIKM_NA_Returning-is-Believing-Long-Term-Engagement.md
- title: Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems
- url: https://doi.org/10.1145/3132847.3133025
- objective: Immediate reward = click; return time between sessions determines interaction rounds available; optimize total clicks in period T; r²Bandit balances exploration, short-term click exploitation, and long-term return exploitation via expected 
- pred_vs_inc: Contextual bandit scores articles by immediate click probability plus expected future clicks from return-time model (GLM with logit/inverse link); UCB-style exploration on combined score—not uplift es
- credit: Per recommendation round: chosen article affects immediate click and subsequent return interval, which scales future interaction opportunities; finite-horizon expected future reward approximation avoi
- gains: r²Bandit ~2× CTR of GLM-UCB/rGLM-UCB on Yahoo replay; return rate ~1.8× GLM-UCB; naive-r²Bandit reduces average return time 18–25% vs. logged baseline; ~63% users with shorter return than historical average; significantl

## D4 | 2017_WWW_NA_Customer-Lifetime-Value-Prediction-Using-Embeddings.md
- title: Customer Lifetime Value Prediction Using Embeddings
- url: https://arxiv.org/pdf/1703.02596.pdf
- objective: CLTV = net sales minus returns over next 12 months; churn = no order in past year; training labels from disjoint prior-year window (Figure 1); model predicts CLTV percentiles then maps to monetary values via calibration trees.
- pred_vs_inc: Outcome prediction only; no treatment/uplift framing.
- credit: Customer-level annual net spend; features from demographics, purchases, returns, and session logs over prior 12 months—no per-impression attribution.
- gains: Session-log embeddings significantly improve churn AUC over handcrafted-only RF (Figure 8; best hidden dim 32–128); hybrid DNN beats logistic regression on churn but did not exceed RF within affordable compute (Figures 9

## D1 | 2018_Blog_NA_Understanding-Dwell-Time-LinkedIn-Feed.md
- title: Understanding Dwell Time to Improve LinkedIn Feed Ranking
- url: https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time
- objective: Adds P(skip) = P(member dwell time on update < T_skip seconds), a negative engagement label derived from empirical dwell-time CDFs on mobile; existing heads predict P(action), E[downstream clicks/virals | action], and E[upstream value | act
- pred_vs_inc: Predicts probabilities of skip and standard engagement events from logged impressions—not causal incrementality of exposure on retention.
- credit: Pointwise per (member, update) impression labels; skip threshold T_skip estimated where P(action | dwell = T) becomes non-zero via Bayes rule on empirical CDFs; no user-level delayed outcome mapped to
- gains: P(skip) model AUC +10% offline with dwell features; online A/B: large reduction in skipped updates, increased click/viral engagement, and increased time spent on feed (no exact percentage lifts stated in source).

## D1 | 2018_IJCAI_NA_Globally-Optimized-Mutual-Influence-Aware-Ranking.md
- title: Globally Optimized Mutual Influence Aware Ranking in E-Commerce Search
- url: https://doi.org/10.24963/ijcai.2018/518
- objective: Maximize expected GMV = price × purchase probability per item in query result set; binary purchased/not-purchased label within query session (same-day logs); no delayed conversion or retention horizon.
- pred_vs_inc: Prediction only—p(i|c(o,i)) is cross-entropy purchase probability; no counterfactual exposure-effect estimation.
- credit: Within-slate: purchase probability depends on global feature vector encoding relative standing vs co-displayed items and (RNN) items ranked ahead—probability mass redistributed across same result set,
- gains: Offline AUC 0.724→0.747→0.765→0.774 and RIG 0.094→0.119→0.141→0.156 for DNN→miDNN→miRNN→miRNN+attention. Online A/B (Table 2, rerank 50, beam 5): GMV +2.91% (miDNN, +9% latency), +5.03% (miRNN, +58% latency), +5.82% (miR

## D4 | 2018_KDD_NA_Notification-Volume-Control-Optimization-Pinterest.md
- title: Notification Volume Control and Optimization System at Pinterest
- url: https://doi.org/10.1145/3219819.3219906
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D5 | 2018_SIGIR_ESMM_Entire-Space-Multi-Task-Model.md
- title: Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate
- url: https://doi.org/10.1145/3209978.3210024
- objective: pCTR (click label y on all impressions), pCTCVR (joint y∧z label on all impressions), pCVR derived as intermediate; per-impression binary labels from traffic logs; temporal split (first half train, second half test); delay not specified
- pred_vs_inc: Prediction (supervised probability estimation of conversion conditional on click)
- credit: Not specified in source for mapping user-level delayed outcomes to item-level decisions; per-impression pointwise labels only
- gains: Public dataset: CVR AUC 68.56% vs BASE 66.00% (+2.56 abs); CTCVR AUC 65.32% vs 62.07% (+3.25 abs). Product dataset (100%): +2.18% CVR AUC, +2.32% CTCVR AUC vs production baseline

## D8 | 2018_TechCrunch_NA_Hinge-Most-Compatible-Gale-Shapley.md
- title: Hinge Employs New Algorithm to Find Your "Most Compatible" Match
- url: https://techcrunch.com/2018/07/11/hinge-employs-new-algorithm-to-find-your-most-compatible-match-for-you/
- objective: Identify pairs most likely to "hit it off"; preferences learned from historical liking and passing activity; success proxy in market tests = exchange of personal phone numbers; horizon, delay, sparsity, censoring not specified in source.
- pred_vs_inc: Not specified in source.
- credit: Not specified in source.
- gains: Users 8× more likely to go on dates (phone-number exchange proxy) with Most Compatible vs other Hinge recommendations.

## D2 | 2018_WWW_DRN_Deep-Reinforcement-Learning-News-Recommendation.md
- title: DRN: A Deep Reinforcement Learning Framework for News Recommendation
- url: https://doi.org/10.1145/3178876.3185994
- objective: RL reward r_total = r_click + β·r_active (β=0.05); r_active from constant-hazard survival model on user return intervals (S_a=0.32 jump on return, T_0=24h expected return, λ_0=1.2×10⁻⁵ s⁻¹ decay); discount γ=0.4 on future Q-value; minor upd
- pred_vs_inc: Dueling Double DQN estimates Q(s,a) for immediate + discounted future click reward; user activeness is supplementary feedback signal, not separate uplift head.
- credit: Per news-request timestep: state = user (2065-dim across 5 time granularities) + context (32-dim); action = candidate news features (417-dim) + interaction (25-dim); reward on recommended item click +
- gains: Offline best DDQN+U+DBGD CTR 0.1663, nDCG 0.4854 vs. W&D CTR 0.1554; online DDQN+U+DBGD CTR 0.0113, P@5 0.0149, nDCG 0.0492, ILS 0.1216 (best among compared methods); DDQN alone largest offline jump from DN.

## D8 | 2019_Blog_NA_Geosharded-Recommendations-Tinder.md
- title: Geosharded Recommendations Part 1: Sharding Approach
- url: https://medium.com/tinder/geosharded-recommendations-part-1-sharding-approach-d5d54e0ec77a
- objective: Not a ranking objective. Success metric in the post is query/index capacity and P50/P90/P99 latency under production load. No like, match, conversation, retention, or revenue label. Horizon/delay/censoring not specified because there is no 
- pred_vs_inc: Neither. The post is index-sharding infrastructure. Load score used to *balance* shards (unique users, active users, query count, or a mix); not a causal estimator.
- credit: Not specified in source (no user-level outcome mapped to an item-level ranking decision).
- gains: Geosharded search index handles **20×** more computations than the previous single-index setup (production measurement). No match-rate, retention, or revenue lift stated.

## D8 | 2019_Blog_NA_Learning-Hiring-Preferences-LinkedIn-Jobs.md
- title: Learning Hiring Preferences: The AI Behind LinkedIn Jobs
- url: https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs
- objective: Real-time hirer feedback labels (Message, Archive, Skip) aggregated per hiring project, sourcing channel, feedback type, and profile term type; horizon is real-time within session — no delay or censoring model.
- pred_vs_inc: Prediction only — ranks candidates by predicted relevance ("most likely to accept your outreach"); no causal or counterfactual framing.
- credit: Pointwise aggregate-count: hirer feedback tallied by profile term, sourcing channel, and rating into term-weight vector; new candidate score is dot product with their profile terms — no IPS or counter
- gains: NDCG@1 +49.61% relative lift (offline simulation); ~20% better than previous production algorithm (offline simulation); online-learning features occupy 7 of top 10 most important XGBoost features.

## D8 | 2019_Blog_NA_Powering-Tinder-Method-Behind-Matching.md
- title: Powering Tinder® — The Method Behind Our Matching
- url: https://tinder.com/powering-tinder
- objective: Improve match potential and meaningful connections; primary signal is concurrent user activity; labels implied as Likes and Nopes plus profile metadata; horizon, delay, sparsity, censoring not specified in source.
- pred_vs_inc: Not specified in source.
- credit: Not specified in source.
- gains: Not specified in source (operational scale only: 190 countries, 45 languages).

## D8 | 2019_CIODive_NA_Coffee-Meets-Bagel-Data-AI-Matching.md
- title: How Coffee Meets Bagel leverages data and AI for love
- url: https://www.ciodive.com/news/coffee-meets-bagel-dating-technology-ai-data/548395/
- objective: Success = deep meaningful connections moving offline, not time-on-app or like counts; KPIs evolving toward connect/chat on-platform and sharing personal information; explicit rejection of likes/time as success proxies; no retention/LTV mode
- pred_vs_inc: Deep neural network "blended" matcher: nine models score candidates, system converges to final match score; not described as incrementality or causal uplift modeling.
- credit: Not specified in source; batch daily curation rather than per-impression attribution.
- gains: #LadiesChoice helped >50% of female users feel more control (company-reported); average male wanted 17 bagels/day vs average woman wanted four "high quality" bagels (company-reported); no model accuracy or revenue/retent

## D2 | 2019_IJCAI_SlateQ_Reinforcement-Learning-Recommendation-Sets.md
- title: SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets; Eugene Ie, Vihan Jain, Jing Wang, Sanmit Narvekar, Ritesh Agarwal, Rui Wu, Heng-Tze Cheng, Tushar Chandra, Craig 
- url: https://arxiv.org/pdf/1905.12767.pdf
- objective: Reward = degree of engagement (e.g., consumption/watch time); YouTube LTV capped at N days; time-based discounting for sparse homepage visits; simulation γ=1 session budget model. Delay/sparsity/censoring beyond time discount not specified.
- pred_vs_inc: Predicts item-wise Q(s,i) (long-term engagement conditional on click) and v(s,i) pCTR; optimizes slate value—not causal incrementality.
- credit: RTDS: reward/transition depend on consumed item only; auxiliary Q^π(s,i) updated via decomposed SARSA/Q-learning; time-based discounting on YouTube for long gaps between visits.
- gains: Simulation QL-OT-OS: 174.6% avg return (+9.67% vs Random), quality −0.3056 (+48.46% vs Random); SARSA-GS 170.7% vs FSQ 164.2% (+180% greater lift over Random); YouTube live: ~+0.5% day 1 to >+1.0% by day 20 aggregated en

## D3 | 2019_NBER_NA_The-Surrogate-Index-Short-Term-Proxies.md
- title: The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely
- url: https://www.nber.org/system/files/working_papers/w26463/w26463.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D1 | 2019_RecSys_MMoE_Recommending-What-Video-Watch-Next.md
- title: Recommending What Video to Watch Next: A Multitask Ranking System
- url: https://doi.org/10.1145/3298689.3346997
- objective: Engagement objectives (click classification, watch-time regression) and satisfaction objectives (like classification, survey-rating regression); per-impression labels from user logs; online eval uses time spent and survey ratings
- pred_vs_inc: Prediction (multi-task pointwise classification/regression heads)
- credit: Not specified in source for user-level delayed outcomes; per-item pointwise prediction only
- gains: Live YouTube A/B (same model complexity): MMoE 4-expert vs shared-bottom 3.7M mults — +0.20% engagement, +1.22% satisfaction; MMoE 8-expert vs shared-bottom 6.1M — +0.45% engagement, +3.07% satisfaction

## D7 | 2019_RecSys_NA_Addressing-Delayed-Feedback-Continuous-Training.md
- title: Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction
- url: https://arxiv.org/pdf/1907.06558.pdf
- objective: Binary click/conversion labels with incomplete observation at ingestion time. Compares five loss functions: log loss, delayed feedback loss (exponential delay model), positive-unlabeled (PU) loss, fake-negative (FN) weighted loss, FN calibr
- pred_vs_inc: Predicts P(click|impression) under delayed label correction—standard predictive CTR, not causal incrementality of ad exposure on advertiser revenue or user retention.
- credit: Per-impression click label with loss corrections for unobserved positives; time-elapsed and time-to-click features for delay model in delayed-feedback loss. No user-level delayed outcome (retention/re
- gains: +3% RCE offline vs prior SOTA on 668M examples; online +55% RPMq and +23% monetized CTR (FN weighted vs log loss).

## D1 | 2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Recommendation.md
- title: A Pareto-Efficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation
- url: https://doi.org/10.1145/3298689.3346998
- objective: CTR (click NLL) and GMV (price-weighted click/conversion NLL); impression/click/purchase labels from one-week EC-REC logs; online A/B over three days on CTR, IPV, PAY, GMV
- pred_vs_inc: Prediction (scalarized multi-objective supervised LTR)
- credit: Not specified in source for user-level delayed outcomes; pointwise impression-level losses
- gains: One-week platform data shows CTR–GMV trade-off (Pearson r = −0.343, p < 0.01). Offline/online table percentages: Not specified in source (Q2 NLM query failed).

## D2 | 2019_WSDM_NA_Top-K-Off-Policy-Correction-REINFORCE.md
- title: Top-K Off-Policy Correction for a REINFORCE Recommender System
- url: https://doi.org/10.1145/3289600.3290999
- objective: Immediate reward on clicked/watched items; long-term reward R aggregated over 4–10 hour future window; primary online metric ViewTime
- pred_vs_inc: Policy optimization (REINFORCE policy gradient with off-policy importance weighting)
- credit: Trajectory-level discounted return R_t assigned via policy gradient to each action in sequence; not item-level retention decomposition
- gains: Standard off-policy: no significant ViewTime lift but +0.53% videos viewed; top-K (K=16) vs standard (K=1): avoids −0.66% ViewTime drop; K=8 vs K=16: +0.15% ViewTime; raising cap c to e⁵: −0.52% ViewTime

## D2 | 2019_WWW_NA_Value-Aware-Recommendation-Reinforcement-Profit.md
- title: Value-aware Recommendation based on Reinforced Profit Maximization in E-commerce Systems
- url: https://arxiv.org/abs/1902.00851
- objective: Reward = aggregated monetized value of click, add-to-cart, add-to-wishlist, purchase per page; XVR generalizes CVR to arbitrary action types mapped to expected purchase contribution × price; offline train one week / test next week on 49M lo
- pred_vs_inc: RL policy learns ranking-formula exponent coefficients α, β, γ to maximize simulated page-level profit reward; XVR models predict conversion probability of each action type—not uplift over counterfact
- credit: Page-level reward sums monetized values across items and action types on a recommended slate; MDP state = user features + up to 50 candidate item features (CTR, CVR, price) + context (page index, time
- gains: Offline vs. DNN-LTR: +6.0% E[GMV], +7.3% R′_page, +2.5% precision@20, +2.4% recall@20, +0.7% MAP; online vs. DNN-LTR: +6.8% GMV, +0.3% CTR, +0.4% IPV; vs. item-CF: +27.9% GMV, +8.2% CTR, +8.8% IPV; adding cart/wishlist X

## D4 | 2019_arXiv_ZILN_Deep-Probabilistic-Customer-Lifetime-Value.md
- title: A Deep Probabilistic Model for Customer Lifetime Value Prediction
- url: https://arxiv.org/pdf/1907.04485.pdf
- objective: Total customer spend (or donation value) in a fixed horizon (typically 1–3 years) after initial purchase, excluding first-purchase value; mixture of zeros and heavy-tailed positives.
- pred_vs_inc: Predicts absolute future LTV outcome via supervised regression; not causal incrementality.
- credit: Not specified in source (customer-level prediction only).
- gains: DNN-ZILN vs MSE: +23.9% Spearman (linear), +48.0% (DNN); +11.4–28.6% normalized Gini; −60–68.9% decile MAPE; KDD Cup profit $15,498 vs winner $14,712 (+5%).

## D1 | 2020_Blog_NA_Pinterest-MTL-Calibration-Utility-Home-Feed.md
- title: Multi-task Learning and Calibration for Utility-based Home Feed Ranking
- url: https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad
- objective: Per-action binary labels (click, long-click, close-up, repin; later video >10s view, hide); each MTL head predicts calibrated action probability; utility combines calibrated P(action) with tunable weights W(action); no explicit retention/LT
- pred_vs_inc: Predicts per-action probabilities fused into utility score; predictive engagement modeling, not incremental effect of an exposure on long-term retention.
- credit: Per user–Pin impression; multi-head predictions combined via fixed/tunable utility weights at ranking time; no user-level delayed outcome mapped to individual Pin exposures described.
- gains: Video distribution increased by 40% with increased engagement rates after adding calibrated >10s video-view head; qualitative improvements in prediction accuracy, engineering velocity, and business tuning speed; no topli

## D7 | 2020_IJCAI_TS-DL_Attention-Delayed-Feedback-Post-Click.md
- title: An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration
- url: https://doi.org/10.24963/ijcai.2020/487
- objective: Latent eventual conversion \(C\); observed label \(Y\); delay \(D\); elapsed time \(E\); post-click item sequence \(S_e\) within \([0, e_i]\) day slots; training week 2018-09-04 to 09-10, test 2018-09-12 on JingDong ad positions.
- pred_vs_inc: Predicts \(P(C=1|X,H)\) and day-slot hazard \(h(D|X,H,S_E)\)—absolute CVR, not incrementality.
- credit: Candidate item features \(X_i\) and pre-click history \(H_i\); post-click calibration uses \(S_{e_i}\) (items clicked after candidate click through day \(e_i\)) to set time-varying hazard.
- gains: TS-DL RelaImpr vs DIN: WP1 +5.24%, WP2 +44.76%, JD-MP +8.02% AUC; ablation TS-DL/D drops 1.61–19% RelaImpr. JD-MP JS divergence vs DFM: 0.1229/0.0889 test/train (23.9% and 29.8% reduction stated). \(\Delta\)rCVR roughly 

## D1 | 2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts.md
- title: Multitask Mixture of Sequential Experts for User Activity Streams
- url: https://doi.org/10.1145/3394486.3403359
- objective: Per-day (or per-timestep) regression/count targets on sparse user activity variables (e.g., Drive search result clicks in GMail, keypress counts); synthetic sinusoidal multi-task targets for controlled evaluation; no explicit retention/LTV 
- pred_vs_inc: Supervised multi-task prediction of next-timestep activity counts; downstream thresholded decision label for UI feature toggle—not RL on long-term engagement.
- credit: Sequence-level: predict last-day targets from prior 29 days of per-user activity tensor; daily timestep aggregation; no item-level impression credit for delayed user outcome.
- gains: Synthetic: ~10% lower MSE than Sequential Multi-head on both tasks; G Suite: MoSE best among 8 architectures; GMail: +4.8% AUC on quality–cost tradeoff curve; ~8% relative click preservation at 80% resource savings vs. p

## D8 | 2020_KDD_NA_Managing-Diversity-Airbnb-Search.md
- title: Managing Diversity in Airbnb Search
- url: https://arxiv.org/abs/2004.02621
- objective: Base ranker: pairwise cross-entropy on booked vs non-booked listing pairs per query/user (binary relevance); diversity second-stage rankers optimize Mean Listing Relevance (MLR), Hellinger distance to target location/price distributions, or
- pred_vs_inc: Predicts listing booking relevance and diversity-aware re-rank scores; not causal incrementality of slate diversity on long-term guest retention.
- credit: Pairwise booked-vs-shown labels for base model; second-stage models learn from list-level context or distribution targets — no IPS or user-level delayed outcome attribution to a single impression.
- gains: Query-context LSTM second-stage (production): online NDCG +1.2%, overall bookings +0.44%, new-guest bookings +0.61%; location-diversity ranker: new-user bookings +1%, China bookings +3.6%; greedy MLR and price-diversity 

## D4 | 2020_KDD_NA_Sleeping-Recovering-Bandit-Notifications-Duolingo.md
- title: A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications
- url: https://research.duolingo.com/papers/yancey.kdd20.pdf
- objective: Binary reward \(r_t=1\) if user completes a lesson within 2 hours of notification; long-term metrics include DAU, lessons completed, D1/D7 retention.
- pred_vs_inc: Estimates relative template lift (difference scoring) with recency penalty; deployed as bandit policy, not supervised LTV model.
- credit: User-level binary outcome attributed to the single selected notification template within a 2-hour window; user arm history tracks recency.
- gains: Offline +1.9% reward vs random; online +0.5% DAU, +0.4% lessons, +2.0–2.2% new-user D1/D7 retention; holdout +2.5% reward after 5 months.

## D1 | 2020_KDD_RAM_Jointly-Learning-Recommend-and-Advertise.md
- title: Jointly Learning to Recommend and Advertise
- url: https://arxiv.org/abs/2003.00097
- objective: RS reward: session dwell time (minutes) on recommended items — long-horizon engagement proxy with γ=0.95 discount; AS reward: 1 if user continues browsing after ad, 0 if leaves; immediate ad revenue revt(aas) from RTB/GSP bidding; horizon i
- pred_vs_inc: RL policy optimization (two-level DQN) maximizing expected cumulative rewards; not causal incrementality of a single exposure on retention/revenue.
- credit: MDP transition rewards at session timestep: dwell time attributed to rec-list, continuation binary reward to ad decision; discounted sum over session — not per-impression delayed retention attribution
- gains: RAM-l vs DRQN: Rrs 19.61±0.23 min (+3.26% improv. over DRQN baseline row), Ras 9.76±0.09 (+4.16%), Rrev 1.49±0.06 (+16.42%); RAM-n vs RAM-l: Rrev 1.56±0.07 (+4.70%, p=0.001), Rrs 19.49±0.16 (−0.61% vs RAM-l).

## D7 | 2020_SIGIR_DLA-DF_Dual-Learning-Algorithm-Delayed-Conversions.md
- title: Dual Learning Algorithm for Delayed Conversions
- url: https://doi.org/10.1145/3397271.3401282
- objective: Predict true CVR γ(X)=P(Y=1|X); observed label Y_obs = O·Y where O indicates whether true conversion is observed by training time given elapsed time E since click; training periods L ∈ {0.5, 1, 2, 4} days in synthetic eval.
- pred_vs_inc: Prediction only—IPS/ICVR reweighting corrects label-observation bias (PU+MNAR), not causal treatment/incremental exposure effects.
- credit: Single click-to-conversion event level—no multi-item slate or multi-step funnel attribution.
- gains: Normal delay (Figure 1 right): nnDLA-DF lower relative log-loss than DFM and Naive across L=0.5–4 days, largest advantage at short L; exponential delay (Figure 1 center): DFM wins when its exponential assumption holds; n

## D5 | 2020_SIGIR_ESM2_Entire-Space-Post-Click-Behavior-Decomposition.md
- title: Entire Space Multi-Task Modeling via Post-Click Behavior Decomposition for Conversion Rate Prediction
- url: https://doi.org/10.1145/3397271.3401064
- objective: Auxiliary targets CTR, CTAVR (impression→DAction), CTCVR over entire impression space; CVR derived from decomposed sub-paths; per-impression binary labels from user logs; delay not specified
- pred_vs_inc: Prediction (supervised multi-task probability estimation)
- credit: Not specified in source for user-level delayed outcomes; per-impression labels on decomposed funnel steps
- gains: Offline: CVR AUC 0.8486 vs ESMM 0.8398 (+0.0088); CTCVR AUC 0.8371 vs 0.8270 (+0.0101); CTCVR GAUC 0.8051 vs 0.7906 (+0.0145). Online: +3% CVR vs ESMM

## D2 | 2020_SIGIR_NICF_Neural-Interactive-Collaborative-Filtering.md
- title: Neural Interactive Collaborative Filtering
- url: https://doi.org/10.1145/3397271.3401181
- objective: Immediate rating reward per step (ratings ≥4 treated as satisfied in simulation); 40-step interaction horizon; curriculum increases discount γ_e over epochs (η=0.2) from myopic toward longer-horizon Q-learning—no explicit retention or reven
- pred_vs_inc: Q-learning estimates per-item Q-values for next recommendation; delayed "exploration bonus" arises when a later satisfied recommendation is credited to earlier exploratory actions via bootstrapping—no
- credit: Pointwise single-item: each step's TD update uses the recommended item's immediate rating plus bootstrapped max-Q of next state; no slate decomposition.
- gains: Cumulative Precision@40 relative improvement over best baseline: +9.43% MovieLens-1M, +4.59% EachMovie, +6.65% Netflix (cold-start); +7.92% MovieLens-1M and +6.43% Netflix (warm-start taste drift); γ=0 ablation drops >10

## D7 | 2020_WWW_FSIW_Feedback-Shift-Correction-Delayed-CVR.md
- title: A Feedback Shift Correction in Predicting Conversion Rates under Delayed Feedback
- url: https://arxiv.org/abs/2002.02068
- objective: Latent eventual conversion \(C \in \{0,1\}\); observed training label \(Y\); elapsed time \(E\) since click; delay \(D\); correct-label indicator \(S\); 30-day Criteo observation period; campaign-specific observational windows on Dynalyst (
- pred_vs_inc: Predicts absolute \(P(C=1|X)\) via consistent importance-weighted ERM—not incrementality.
- credit: Post-click impression features \(X\) at click time; elapsed time \(e_i\) included as FSIW feature.
- gains: Criteo LR-FSIW: LL 0.3928 vs DFM 0.3989 (1.5% improvement, significant), NLL 28.02 vs 27.33 (2.5%, significant); training ~2.1h vs DFM ~140h. Dynalyst Campaign L FFMIW: NLL 2.304 vs FFM 1.7197 (significant). Online Campa

## D5 | 2020_WWW_NA_Causal-Approaches-Debiasing-Post-Click-CVR-Multi-Task.md
- title: Large-scale Causal Approaches to Debiasing Post-click Conversion Rate Estimation with Multi-task Learning
- url: https://doi.org/10.1145/3366423.3380037
- objective: Binary conversion label r_{u,i} ∈ {0,1} per exposure; conversion observed only if user clicked (o_{u,i}=1); sequential chain exposure→click→conversion with no longer-horizon retention label.
- pred_vs_inc: **Prediction debiasing only**—Multi-IPW/Multi-DR correct MNAR selection into training data via IPW/DR, estimating P(conversion|exposure) over full exposure space; does not estimate incremental causal 
- credit: Pointwise per-(user, item) exposure—no journey-level or delayed backward attribution.
- gains: Ali-CCP (Table 3): Multi-DR CVR AUC 69.29±0.31 / CTCVR AUC 65.43±0.34 vs ESMM 68.56±0.37 / 65.32±0.49. Set D (11.5B exposures): Multi-DR CTCVR AUC 77.23 / GAUC 62.28 vs ESMM CTCVR AUC 76.55 / GAUC 61.76.

## D1 | 2020_WWW_NA_Multi-Objective-Ranking-Stochastic-Label-Aggregation.md
- title: Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation
- url: https://doi.org/10.1145/3366423.3380122
- objective: Per query–product pair: relevance R (human majority vote, graded or binary) and purchase P (purchases ÷ impressions over a fixed 6-week or 2-month window). Stochastic aggregation flips a per-query coin with probability α so all products und
- pred_vs_inc: Predicts ranking scores matching aggregated relevance/purchase orderings; no causal incrementality or exposure-effect framing.
- credit: Query-level label assignment only—one stochastic coin flip per training query applies to every product in that query list; no user/session delayed outcome mapped to a single impression.
- gains: 2phase-stoch dominates 2phase-linear, 1phase-stoch, 1phase-linear, and fusion on all three datasets; on raw data two-phase purchase optimization reaches NDCG@5 0.493 vs 0.395 single-phase; deterministic linear families c

## D6 | 2020_arXiv_NA_Learning-to-Rank-for-Uplift-Modeling.md
- title: Learning to Rank for Uplift Modeling
- url: https://arxiv.org/pdf/2002.05897.pdf
- objective: Individual treatment effect \(U(X)=P(y=1|X,t=1)-P(y=1|X,t=0)\); binary response \(y\) from A/B treatment \(t\in\{0,1\}\); ranking quality measured via uplift/Qini curves and AUUC.
- pred_vs_inc: Estimates CATE-style uplift and optimizes ranking directly via listwise LTR; not observational incrementality of exposure in a recommender.
- credit: User-level RCT tuples \((X,y,t)\); no item-level or delayed outcome credit assignment.
- gains: On Hillstrom, LambdaMART PCG reaches ~4% incremental gains at 50% targeted population where other methods need ~100%; significantly higher AUUC than two-model and uplift RF on Hillstrom and Criteo (student \(t\)-test, \(

## D6 | 2020_arXiv_NA_Treatment-Targeting-AUUC-Maximization.md
- title: Treatment Targeting by AUUC Maximization with Generalization Guarantees
- url: https://arxiv.org/abs/2012.09897
- objective: Binary outcome \(y \in \{0,1\}\); treatment \(g \in \{T,C\}\); ITE \(= E[Y|X,T{=}1] - E[Y|X,T{=}0]\); optimize expected AUUC (joint relative estimator, Def. 1) via bipartite ranking loss decomposition; no delay or censoring in formulation.
- pred_vs_inc: **incrementality** — directly targets Individual Treatment Effect ranking through AUUC lower-bound surrogate, not raw outcome probability.
- credit: Individual-level \((x_i, g_i, y_i)\); no item-level or slate-level delayed-outcome decomposition.
- gains: Hillstrom AUUC-max(\(s_{\mathrm{poly}}\)): 0.03065 (rank 2/9), vs SDR 0.03079, TM 0.03019, PCG 0.03063 (~5,000 params); 23 parameters, 0.17× TM training time. Bound generalization gap ~0.02 avg vs alternatives. Jobs poli

## D7 | 2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md
- title: Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction
- url: https://ojs.aaai.org/index.php/AAAI/article/view/16495
- objective: Post-click CVR over entire impression space; 7-day attribution window (\(T=7\)); labels \(Y\)=click, \(Z\)=observed conversion, \(C\)=latent eventual conversion, \(D\)=delay, \(E\)=elapsed time since click.
- pred_vs_inc: Predicts absolute CTR, CTCVR, CVR, and day-slot delay probabilities; not incrementality.
- credit: Delayed conversion mapped to original clicked user-item interaction feature vector \(X\) captured at click time.
- gains: Public AUC 0.7811 (+4.93% RelaImpr vs ESMM 0.7679); product GAUC 0.6181 (+6.68% RelaImpr vs ESMM 0.6107); +0.82% and +3.16% RelaImpr over DFM on public/product datasets respectively.

## D1 | 2021_Blog_NA_Powered-by-AI-Instagram-Explore-Value-Model.md
- title: Powered by AI: Instagram's Explore Recommender System
- url: https://ai.meta.com/blog/powered-by-ai-instagrams-explore-recommender-system/
- objective: MTML final-pass model predicts positive actions (like, save) and negative actions (e.g., “See Fewer Posts Like This”); value model fuses head probabilities with tunable weights; short-horizon engagement labels—no retention/LTV horizon state
- pred_vs_inc: Predicts per-action probabilities combined via weighted arithmetic value model; predictive engagement scoring, not incremental long-term effect of an exposure.
- credit: Per media item in Explore grid; value model score ranks candidates; diversity heuristic downranks repeated authors/seed accounts deeper in batch; no user-level delayed outcome attribution to individua
- gains: Not specified in source (qualitative claims of personalized discovery at scale; no percentage lifts stated).

## D8 | 2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md
- title: Reciprocal Recommender Systems: Analysis of State-of-Art Literature, Challenges and Opportunities towards Social Recommendation
- url: https://arxiv.org/abs/2007.16120
- objective: Field-wide objective is bilateral mutual compatibility p(x↔y)=φ(p(x,y), p(y,x)); labels from expressions of interest, messages, replies, likes; failure includes ignored contact after N days; no standard horizon or delay/censoring framework 
- pred_vs_inc: Surveyed models predict absolute reciprocal compatibility scores; incrementality not discussed in source.
- credit: Not specified in source for any surveyed model.
- gains: Synthesized benchmarks only: CCR ~70% contact success (2× random baseline); CFHMM-HR 60–70% vs <50% CB-only; RRK +14–17% match prediction vs IBCF; LFRR real-time at Pairs scale matching RCF accuracy; CiteSeer 96% recipro

## D5 | 2021_KDD_AITM_Sequential-Dependence-Multi-Step-Conversions.md
- title: AITM: Modeling the Sequential Dependence for Audience Multi-step Conversion with Multi-task Learning in the Meituan App
- url: https://doi.org/10.1145/3477495.3532030
- objective: 
- pred_vs_inc: Prediction (multi-task supervised conversion probability per funnel step)
- credit: Not specified in source for user-level delayed outcomes; per-banner impression labels with sequential funnel constraints
- gains: Offline approval AUC 0.8534 vs PLE 0.8518 (+0.0142 vs LightGBM); activation AUC 0.8770 vs PLE 0.8731 (+0.0234). Online vs MLP: +25.0% approval CR, +42.11% activation CR

## D7 | 2021_KDD_DEFER_Delayed-Feedback-Modeling-Real-Negatives.md
- title: Real Negatives Matter: Continuous Training with Real Negatives for Delayed Feedback Modeling
- url: https://arxiv.org/abs/2104.14121
- objective: Post-click binary conversion \(y \in \{0,1\}\); sample types: real negative (\(z > w_2\)), fake negative (\(w_1 < z < w_2\)), positive (\(z < w_1\)); duplicated real negatives and positives re-ingested after attribution window closes.
- pred_vs_inc: Predicts absolute CVR \(p(y=1|x)\); importance-sampled loss corrects distribution shift—not incrementality.
- credit: Post-click attribution to clicked impression features \(x\) at click time; last-click 7-day attribution on Taobao-30days.
- gains: Offline DEFER: Criteo AUC 0.8394 (RI-AUC 90.11% vs Oracle), Taobao AUC 0.6483 (RI-AUC 88.00%); beats FNW-RN, ES-DFM, Oracle-close NLL. Online: >6.0% CVR improvement in several scenarios; 8.5% CVR (continuous, Add-to-Cart

## D8 | 2021_NeurIPS_UniCoRn_AB-Testing-Two-Sided-Marketplace.md
- title: A/B Testing for Recommender Systems in a Two-sided Marketplace
- url: https://arxiv.org/pdf/2106.00762
- objective: Not an ML training objective — UniCoRn is a post-hoc experiment-design layer on trained control/treatment scoring models T0/T1; estimation target is producer-level response Y_i aggregated over the experiment window.
- pred_vs_inc: Incrementality — measures average treatment effect (ATE) of ranking changes on producers, not outcome prediction.
- credit: Pointwise item-level: outcomes assigned to rank position R_D(i,I_s) in a consumer session; producer response Y_i aggregates position-based attention across items and sessions.
- gains: Candidate-generation experiment: +0.51% Weekly Active Unique users, +0.57% Sessions (p<0.001); ranking-model experiment: +0.13% WAU, +0.11% Sessions (p<0.001); offline UniCoRn variants outperform OASIS and HaThucEtAl on 

## D5 | 2021_SIGIR_HM3_Hierarchically-Modeling-Micro-Macro-Behaviors.md
- title: HM³: Hierarchically Modeling Micro and Macro Behaviors for Conversion Rate Prediction
- url: https://doi.org/10.1145/3404835.3462973
- objective: Four entire-space auxiliary targets (CTR, D-Mi, D-Ma, CTCVR) plus derived pCVR from six conditional sub-path probabilities; per-impression binary labels on graph nodes; SR logs 2020-09-16 to 09-30
- pred_vs_inc: Prediction (supervised multi-task probability decomposition on behavior graph)
- credit: Not specified in source for user-level delayed outcomes; per-impression labels on micro/macro/purchase nodes
- gains: SR-L CVR AUC: HM³ 0.84891 vs BASE 0.84703 (+0.00188); vs ESMM +0.00166. Online: +8.27% CVR, +8.32% GMV vs BASE (vs ESMM +2.76% CVR, ESM² +4.84%)

## D7 | 2021_SIGIR_NA_Counterfactual-Reward-Modification-Delayed-Feedback.md
- title: Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback
- url: https://doi.org/10.1145/3404835.3462892
- objective: Reward R = λ·click + (1−λ)·conversion, where conversion Y may be unobserved if it occurs after data collection (true conversion V latent). CBDF modifies delayed reward via counterfactual importance sampling: R_mod = λ·C + (1−λ)·w·Y with w =
- pred_vs_inc: Counterfactual importance sampling yields unbiased estimate of expected true delayed reward Pr{V=1|S}—addresses bias from censored conversions, not full causal incrementality of recommendation on user
- credit: Per (context, recommended item) pair; immediate click and delayed conversion combined into scalar reward; importance weights correct downward bias when conversions not yet observed. ~70% of WeChat cou
- gains: CBDF converges faster than unmodified-reward bandits on synthetic data; beats DFM-S, SBUCB, EXP3-B, SBUCB-D on all three datasets (exact metric values vary by dataset; WeChat is production coupon traffic).

## D2 | 2021_WSDM_URL_User-Response-Models-REINFORCE-Recommender.md
- title: User Response Models to Improve a REINFORCE Recommender System; Minmin Chen, Bo Chang, Can Xu, Ed H. Chi (Google); WSDM 2021; https://dl.acm.org/doi/10.1145/3437963.3441764
- url: https://dl.acm.org/doi/10.1145/3437963.3441764
- objective: Main RL: discounted cumulative reward R_t from immediate response r(s,a) (zero for non-interacted items); auxiliary URL: immediate click (BCE) or dwell (Huber). Main window: trailing 6 hours + 4-hour reward buffer; auxiliary: full trajector
- pred_vs_inc: Prediction only — auxiliary tasks predict immediate user response to enrich representations; not incrementality/uplift.
- credit: Item-level pointwise: per-item reward/response logged; non-interacted items zeroed in RL loss; all slate items contribute to click auxiliary loss.
- gains: Live user-enjoyment: +0.12% (95% CI [+0.07%, +0.18%]) URL dwell vs base REINFORCE; +0.26% low-activity vs +0.09% high-activity slice; offline MAP@1 0.061 (combined URL, linear head) vs 0.059 / 0.057; 7-day window baselin

## D4 | 2021_arXiv_NA_Cross-Domain-Adaptive-Learning-Advertisement-CLV.md
- title: Cross-Domain Adaptative Learning for Online Advertisement Customer Lifetime Value Prediction
- url: https://ojs.aaai.org/index.php/AAAI/article/view/25583/25355
- objective: LTV = total consumption over trailing 7 days linked via anonymous ad identifier (e.g., IDFA); ZILN-variant loss (payment-indicator cross-entropy + lognormal NLL on positives); no censoring/survival handling discussed.
- pred_vs_inc: Direct outcome prediction only; domain adaptation aligns distributions, not treatment effects.
- credit: User-level 7-day consumption aggregated by ad identifier; no per-impression or per-exposure decomposition.
- gains: vs single-domain target training: average AUC improvements 6.8–14.5% across eight backbones; vs fine-tuned source expert on Mixed model: +3.2–9.6% AUC and +7.4–24.7% Gini across G1–G5; example DCNv2 on G2: +13.7% AUC (ab

## D7 | 2021_arXiv_NA_Handling-Many-Conversions-Per-Click-Delayed-Feedback.md
- title: Handling many conversions per click in modeling delayed feedback
- url: https://arxiv.org/abs/2101.02284
- objective: Label \(y_p \in [0,\infty)\) = total count or value of post-click events attributed to last click within window \(M\); delayed features \(L_p\) include partial labels in \([t_p, t_p+d_i)\); sub-models \(f_i\) predict thermometer-encoded cum
- pred_vs_inc: Poisson regression predicting expected conversion count per click—absolute expectation, not incrementality.
- credit: Last-click attribution; partial labels and "label so far" feature map immature observations to unbiased completed-label estimate \(y'_{p,t_k}\).
- gains: Poisson log loss improvement vs M3 (mature-only baseline): all data −8.6%; long-delay advertisers −10.16%; new advertisers (<10 days) −1.81%; Oracle upper bound −9.1% / −10.87% / −2.0%. Proposed model closest to neutral 

## D4 | 2022_CIKM_NA_Billion-User-Customer-Lifetime-Value-Kuaishou.md
- title: Billion-user Customer Lifetime Value Prediction: An Industrial-scale Solution from Kuaishou
- url: https://arxiv.org/pdf/2208.13358.pdf
- objective: Active return days (offline) or platform value after 30 days (online A/B) at horizons 30/90/180/365; ordered \(ltv_{30}\le ltv_{90}\le ltv_{180}\le ltv_{365}\).
- pred_vs_inc: Predicts absolute multi-horizon LTV; ROI uplift measured only in online A/B.
- credit: Not specified in source (user-level acquisition prediction).
- gains: ODMN vs ZILN on \(ltv_{30}\): AMBE 0.0423 vs 0.1336; Mutual Gini 0.0125 vs 0.0226; online ROI +11.9%/+12.8%/+14.7%.

## D1 | 2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md
- title: Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems
- url: https://arxiv.org/pdf/2208.06942
- objective: Optimizes long-term user satisfaction within a recommendation session (MDP with discount γ=0.95). Instant reward r(s,a) = weighted sum of immediate feedback metrics (video play time, play integrity, likes, shares, comments, skips); weights 
- pred_vs_inc: Learns a fusion policy (continuous action α) that maximizes cumulative discounted session reward; not a direct LTV predictor—optimizes fusion weights trading instant vs. delayed satisfaction.
- credit: Per recommendation timestep within a session: state = user profile + interaction history (last 500 watched videos); action = fusion weights applied to current candidate ranking; transition and reward 
- gains: Production deployment: +2.550% app dwell time and +9.651% user positive-interaction rate vs. baselines; offline OPE ranks BatchRL-MTF best on stability and returns among RL variants; ablation BatchRL-MTF-Rinteraction mat

## D4 | 2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation.md
- title: PinnerFormer: Sequence Modeling for User Representation at Pinterest
- url: https://arxiv.org/pdf/2205.04507.pdf
- objective: Dense all-action loss: maximize similarity to pins with positive Homefeed engagement (repin, >10s closeup, >10s click) in a 14–28 day future window after embedding time.
- pred_vs_inc: Predicts future engagement propensity via metric learning; not LTV or causal incrementality.
- credit: Not specified in source (no user-level retention→item attribution).
- gains: Recall@10 0.229 vs PinnerSage oracle 0.026–0.046; batch staleness drop 8.3% vs SASRec 13.9%; Homefeed +2.5% repins, +1.3% closeups; Ads +0.5–1.1% gCTR.

## D5 | 2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task.md
- title: ESCM²: Entire Space Counterfactual Multi-Task Model for Post-Click Conversion Rate Estimation
- url: https://doi.org/10.1145/3534678.3539382
- objective: CTR, CVR (counterfactual-regularized), CTCVR over exposure space; binary click/conversion labels; 90-day industrial logs + Ali-CCP; chronological train/val/test split
- pred_vs_inc: Prediction with counterfactual risk minimization (IPS/DR regularizers debias CVR estimation toward causal estimand)
- credit: Not specified in source for user-level delayed outcomes; per (user,item) exposure labels with IPS/DR reweighting from click propensity
- gains: CVR AUC industrial: ESCM²-IPS 0.7730 vs ESMM 0.7547; CTCVR AUC: ESCM²-DR 0.8265 vs ESMM 0.8153. Online: +2.84% orders, +10.85% premium, +5.64% UV-CVR vs ESMM (scenario 1)

## D7 | 2022_WWW_DEFUSE_Asymptotically-Unbiased-Delayed-Feedback.md
- title: Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction
- url: https://doi.org/10.1145/3485447.3511965
- objective: CVR \(p(y=1|x)\) decomposed into immediate positive IP (\(d\le w_o\)) plus delayed positive DP (\(d>w_o\)); attribution window \(w_a\) (1 day Taobao, 30 days Criteo); four sample types: IP, FN, RN, DP.
- pred_vs_inc: Predicts absolute conversion probability; not incrementality of ad exposure.
- credit: Delayed conversion mapped back to original click features \(x\) at \(t_0\); DP duplicated with positive label injected at conversion time.
- gains: Criteo-30d: DEFUSE AUC 0.8408 (RI-AUC 52.33% vs ES-DFM 46.11%); Criteo-1d: Bi-DEFUSE AUC 0.8467 (RI-AUC 96.30%); Taobao: Bi-DEFUSE AUC 0.8080 (RI-AUC 66.33% vs ES-DFM 52.04%); online +2.28% CVR.

## D8 | 2022_WWW_NA_Interference-Bias-Variance-Two-Sided-Marketplace.md
- title: Interference, Bias, and Variance in Two-Sided Marketplace Experimentation: Guidance for Platforms
- url: https://arxiv.org/pdf/2104.12222
- objective: Not an ML paper — estimation target is Global Treatment Effect (GTE), expected change in fractional bookings if intervention launched platform-wide; static one-shot booking process with no delay/censoring.
- pred_vs_inc: Incrementality — causal GTE estimation, not predictive modeling.
- credit: Group-level only — CR/LR estimators compare aggregate booking rates between treatment and control groups; no pointwise or slate-level decomposition.
- gains: Not model-comparison gains; deliverable is bias/variance characterization — 50-50 allocation achieves variance-approximation ratio ≤1.004 relative to variance-optimal allocation (CR design); CR relative bias ranges near 

## D8 | 2022_arXiv_NA_Matching-Theory-Recommender-Online-Dating.md
- title: Matching Theory-based Recommender Systems in Online Dating
- url: https://arxiv.org/pdf/2208.11384.pdf
- objective: Replace φ(p_x,y, p_y,x) reciprocal fusion with Choo–Siow transferable-utility equilibrium matching μ_x,y incorporating capacity terms √μ_x,0 √μ_y,0; unilateral scores p_x,y, p_y,x from matrix factorization on likes/thanks; no explicit reten
- pred_vs_inc: Predicts equilibrium match probabilities μ_x,y (not incremental lift of a recommendation); transfers τ_x,y adjust bilateral utilities; unmatched option modeled explicitly.
- credit: Market-equilibrium allocation across full candidate sets; not per-exposure delayed outcome attribution.
- gains: Not specified in source as quantitative production lifts; claims MTRS mitigates extreme concentration of likes/matches vs off-the-shelf fusion; individual-level matching vs group-identical recommendations in Chen et al. 

## D8 | 2023_Blog_NA_Automated-Decision-Making-Grindr.md
- title: Automated Decision Making at Grindr
- url: https://www.grindr.com/blog/automated-decision-making-and-grindr
- objective: Not applicable — source states no ranking model is used for user discovery.
- pred_vs_inc: Not applicable for ranking; only binary security/moderation classifiers (spam accounts, non-compliant images) with human-in-the-loop override for false positives.
- credit: Not applicable — no ranking or recommendation model to assign outcomes to impressions.
- gains: Not specified in source — no quantitative results reported.

## D1 | 2023_Blog_NA_Scaling-Instagram-Explore-Recommendations.md
- title: Scaling the Instagram Explore Recommendations System
- url: https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/
- objective: Short-horizon engagement events (click, like, see less, etc.) predicted by MTML second-stage ranker; combined via tunable value model (VM) weights into Expected Value score per item—not explicit retention/LTV labels.
- pred_vs_inc: Predicts probabilities of immediate engagement events; VM linearly fuses heads with tunable weights W_click, W_like, W_see_less, etc.
- credit: Per-item expected value from multi-event probabilities at ranking stage; no user-level delayed outcome attribution to individual exposures described.
- gains: Not specified in source (no numeric lift percentages in blog post).

## D1 | 2023_CIKM_NA_Multitask-Ranking-Immersive-Feed-Short-Video.md
- title: Multitask Ranking System for Immersive Feed and No More Clicks: A Case Study of Short-Form Video Recommendation
- url: https://doi.org/10.1145/3583780.3615489
- objective: Multi-task prediction of user behaviors (watches, likes, comments, shares, etc.) from impression logs; sparse tasks (e.g., comments ~1 per 1000 watches) vs. dense watch/engagement tasks; no explicit retention/LTV horizon label—live metrics 
- pred_vs_inc: Supervised multi-task ranking heads predict per-behavior probabilities; final ranking score is a weighted combination of task predictions (multi-objective fusion at serving), not a direct policy for l
- credit: Per-impression / per-video-in-sequence labels from user logs; trail-bias correction attributes position-in-watch-sequence effects; no user-level delayed outcome decomposed to individual slate items be
- gains: Trail debias on all tasks: +1.96% Overall Enjoyment live; disentangle regularization: up to +0.33% Overall Enjoyment; sparse co-training with upweight 50: +0.29% Overall Enjoyment and +3.07% on sparse task metric vs. sep

## D3 | 2023_KDD_NA_Impatient-Bandits-Long-Term-Without-Delay.md
- title: Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay
- url: https://arxiv.org/pdf/2307.09943.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D5 | 2023_KDD_NA_Optimizing-Airbnb-Search-Journey-Multi-Task.md
- title: Optimizing Airbnb Search Journey with Multi-task Learning
- url: https://doi.org/10.1145/3580305.3599881
- objective: Primary: uncancelled booking per search impression (binary NDCG relevance). Auxiliary heads: six sequential positive milestones via chain-rule decomposition P(unc)=P(unc|book)P(book|req)…P(c); negative milestones (rejection, cancellation) v
- pred_vs_inc: Journey Ranker predicts listing scores decomposed into Base (positive funnel), Twiddler (negative milestones), and Combination (context-dependent weighting of negative risks); predicts conversion prob
- credit: Search-impression listwise labels; positive milestones attributed along guest journey chain; negative milestones down-weighted via context-conditioned combination; training mixes booker-only positive 
- gains: Stays offline NDCG +0.48% (±0.05%) vs baseline (+9.2% params). Stays online: +0.61% uncancelled bookers, +0.14% searchers→clickers, +0.48% clickers→uncancelled bookers. Also +2.0% bookers (in-real-life experiences), +9.0

## D8 | 2023_RecSys_NA_Fast-Examination-Agnostic-Reciprocal-Recommendation.md
- title: Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets
- url: https://doi.org/10.1145/3604915.3608774
- objective: Maximize expected total matches (social welfare) via market-clearing TU equilibrium scores μ*_{c,j}; unilateral preferences p_{c,j}, p_{j,c} from matrix factorization; real dating logs subsampled to 200×200 and 1000×1000 with k-core filteri
- pred_vs_inc: Predicts absolute equilibrium match probabilities under global capacity constraints; not incrementality modeling.
- credit: Not specified in source; market-level equilibrium aggregation, not per-exposure delayed-outcome decomposition.
- gains: n=200 synthetic: TU 332.91 expected matches vs Naive 219.56 and Reciprocal 273.86; 1000×1000 male-proactive: TU 538.97 vs Naive 375.82 and Reciprocal 491.12 (SW infeasible); reactive-side Gini 0.1019 (TU) vs 0.3872 (Naiv

## D8 | 2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md
- title: Reciprocal Sequential Recommendation
- url: https://arxiv.org/pdf/2306.14712
- objective: Joint loss L = L_ma + λ·L_mi + μ·L_sd (macro BPR + micro BPR + Margin-MSE self-distillation); positive label is bilateral mutually-agreed interaction (interview-reached pairs in recruitment; matched questioner-answerer in Q&A); sequences tr
- pred_vs_inc: Prediction only — predicts matching-degree score for user pairs; no causal or counterfactual effect of exposure.
- credit: Pointwise per bilateral pair (u_i, v_j); no slate-level, impression-level, or coordinate-based credit assignment.
- gains: Design recruitment HR@5 0.4435 vs. DPGNN 0.2422 and SASRec 0.2033; Technology recruitment HR@5 0.7597 vs. DPGNN 0.4521; AskUbuntu HR@5 0.5259 vs. FMLP-Rec 0.2706; latency 0.2832 ms/batch (with distillation) vs. 8.7105 ms

## D2 | 2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale.md
- title: Reinforcing User Retention in a Billion Scale Short Video Recommender System
- url: https://arxiv.org/abs/2302.03322
- objective: Primary: minimize inter-session returning time (proxy for retention/DAU); delayed session-end reward hours–days later; immediate reward = watch time + interactions per request; D1/D7 retention evaluated online
- pred_vs_inc: Policy optimization (DDPG-style actor–critic RL), not pointwise prediction ranking
- credit: Session-level returning-time reward at last request only (γ=1 within session, γ=0.95 at terminal step); immediate heuristic + RND critics for per-step guidance; normalized retention reward divides tru
- gains: Offline: returning time 1.892 vs CEM 2.036 / TD3 2.009; retention 0.618 vs CEM 0.587 / TD3 0.592. Online (≈150 days): +0.450% app open frequency, +0.2% DAU, +0.053% D1 retention, +0.063% D7 retention vs CEM

## D2 | 2023_WWW_TCAC_Two-Stage-Constrained-Actor-Critic.md
- title: Two-Stage Constrained Actor-Critic for Short Video Recommendation; Qingpeng Cai, Zhenghai Xue, Chi Zhang, Wanqi Xue, Shuchang Liu, Ruohan Zhan, Xueliang Wang, Tianyou Zuo, Wentao Xie, Dong Zheng, et a
- url: https://arxiv.org/pdf/2302.01680.pdf
- objective: Main: long-term cumulative WatchTime r_1; auxiliaries: Click, Like, Comment, Hate, Follow, Share, etc.; horizon = user session; γ≈0.99 offline, 0.95 production; WatchTime dense per view, interactions sparse; hate extremely sparse. Retention
- pred_vs_inc: Policy-value optimization (expected cumulative WatchTime under constraints); not causal incrementality at training time.
- credit: Step-level vector reward r_t(s_t,a_t) at each recommendation; standard Bellman TD credit over session—not explicit user-level delayed outcome → item attribution beyond immediate feedback.
- gains: KuaiRand WatchTime NCIS 13.14 vs BC 12.85 (+2.23%); Like +18.80%, Comment +15.6% vs BC; online vs LTR: WatchTime +0.379%, Share +3.376%, Download +1.733%, Comment −0.619%.

## D2 | 2023_arXiv_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md
- title: KuaiSim: A Comprehensive Simulator for Recommender Systems
- url: https://arxiv.org/abs/2309.12645
- objective: Simulator environment, not a single ranker objective. Cross-session level: return day Y(R) ∈ {1,…,10} days (Geometric(p_ret) with D=10 cap) and binary user-retention ratio; immediate feedback includes click/like/comment/follow/forward/hate;
- pred_vs_inc: Prediction/simulation only—User Retention Module predicts next-day return probability p_ret = personal bias + λ₁·session immediate reward + global bias; no causal incrementality or treatment-effect es
- credit: Session-level only: response retention bias attributes return probability to aggregate session immediate reward, not to individual impressions; no item-level delayed-outcome credit assignment.
- gains: See offline/online eval above; request-level ListCVAE best max L-reward 4.042±0.001; whole-session HAC best total reward 10.1742±0.0634.

## D3 | 2023_arXiv_NA_Evaluating-Surrogate-Index-200-AB-Tests-Netflix.md
- title: Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix
- url: https://arxiv.org/pdf/2311.11922
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D8 | 2023_arXiv_NA_Managing-Congestion-Two-Sided-Platforms.md
- title: Managing Congestion in Two-Sided Platforms: The Case of Online Rentals
- url: https://arxiv.org/pdf/2308.14703.pdf
- objective: Estimated request utility U_is from rank-ordered logit on clicks/requests; click propensity depends on position and E[U|info]; counterfactuals vary ranking mix α∈[0,1] between full personalization and random order; outcomes = click/request 
- pred_vs_inc: Structural discrete-choice estimation (not ML ranker); counterfactual simulation holds search sets fixed and reorders results; assumes search volume invariant to ranking (conservative on horizontal di
- credit: Not applicable — econometric choice model, not learned recommender with delayed feedback.
- gains: Top position captures >15% of all clicks/requests vs ~4% at position 10; top 20% of rooms account for ~100% of requests; status-quo (utility, congestion) lies below efficiency frontier — modest α (<0.1) on random ranking

## D2 | 2023_arXiv_NA_Optimizing-Audio-Recommendations-Long-Term.md
- title: Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective; Lucas Maystre, Daniel Russo, Yu Zhao (Spotify / Columbia); arXiv 2023 (industry-lab); https://arxiv.org/pdf/23
- url: https://arxiv.org/pdf/2302.03561.pdf
- objective: Long-term reward: total listening / engagement with recommended items over months; discovery uses 60-day fixed horizon stickiness (γ=1 over 60 days); daily periods; binary consumption r(c)=1(c>0) in prototypes; retention modeled exogenous w
- pred_vs_inc: Predicts Q_{π0}(s,a) — long-term value of deviating from incumbent on one recommendation slot; counterfactual Q formula; not uplift vs holdout at training level though holdback validates attribution.
- credit: Item-level: Q credits recommendation via (i) change in listen probability and (ii) transition in content-relationship state affecting stickiness; surrogacy Assumption 2 mediates long-term item engagem
- gains: Banner (impacted users): +81% 60-day show minutes, +32% 60-day active days vs control; median minutes +80%+; shelf week-8 overall podcast minutes +1.7%, discovery consumption +6.2%, lasting discovery rate +5.4%.

## D3 | 2023_arXiv_NA_Pareto-Optimal-Proxy-Metrics.md
- title: Pareto Optimal Proxy Metrics
- url: https://arxiv.org/pdf/2307.01000
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D3 | 2024_Blog_NA_Estimating-Long-Term-Outcome-Algorithms-Spotify.md
- title: Estimating long-term outcome of algorithms
- url: https://research.atspotify.com/2024/05/estimating-long-term-outcome-of-algorithms
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D3 | 2024_Blog_NA_Improve-Next-Experiment-Proxy-Metrics-Netflix.md
- title: Improve Your Next Experiment by Learning Better Proxy Metrics From Past Experiments
- url: https://netflixtechblog.com/improve-your-next-experiment-by-learning-better-proxy-metrics-from-past-experiments-64c786c2a3ac
- objective: Proxy vector \(S\) (short-term, e.g. CTR or engagement) vs north-star \(Y\) (retention / long-term revenue). Horizon of \(Y\) is not given as a fixed day count; blog example contrasts click-through with “long-term retention.” Delay handling
- pred_vs_inc: Incrementality of **policies / treatments**, not of a single exposure. Target is covariance of *true* treatment effects \(\mathrm{Cov}(\tau_S, \tau_Y)\), not user-level \(\mathrm{Corr}(S,Y)\) and not 
- credit: Not an item-level ranker. Mapping is experiment → estimated treatment effects on \(S\) and \(Y\). No user-level delayed outcome mapped to one recommended title.
- gains: Not specified in this source (process and estimator description only).

## D1 | 2024_Blog_NA_Leveraging-Dwell-Time-LinkedIn-Feed.md
- title: Leveraging Dwell Time to Improve Member Experiences on the LinkedIn Feed
- url: https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed
- objective: Evolves from P(skip) negative signal to an Auto Normalized Long Dwell binary label: predict whether dwell exceeds the x-th percentile of dwell for the item's top-K attribute cluster (content type, creator type, distribution method, etc.), r
- pred_vs_inc: Predicts skip probability and long-dwell exceedance probabilities fused into a weighted MOO score—predictive engagement modeling, not incremental retention effect of a specific exposure.
- credit: Request/impression-level multi-head predictions combined via tuned MOO hyperparameters; long-dwell labels normalized within categorical clusters updated daily; no attribution of user-level retention t
- gains: Figure 8 shows iteration #4 achieved statistically significant positive improvements on targeted dwell metrics (exact lift percentages not stated in blog text); qualitative gains on sessions, overall time spent, and time

## D1 | 2024_Blog_NA_Recommending-Long-Term-Member-Satisfaction-Netflix.md
- title: Recommending for Long-Term Member Satisfaction at Netflix
- url: https://netflixtechblog.com/recommending-for-long-term-member-satisfaction-at-netflix-ac15cada49ef
- objective: Retention is north star but impractical as direct reward (noisy, low sensitivity, hard to attribute, slow—one signal/account/month); proxy reward r(user, item) engineered from interaction patterns (play, complete, thumb, genre discovery, am
- pred_vs_inc: Bandit policy π(item | user; r) trained on proxy rewards; delayed-feedback prediction models estimate p(final feedback | observed feedback) offline—predictive reward engineering, not stated causal inc
- credit: Proxy reward defined per user–item interaction r(user, item); delayed completion/thumbs-up predicted per training example; attribution across series of bad recommendations acknowledged as hard for ret
- gains: Not specified in source (conceptual framework and process; no percentage improvements reported).

## D4 | 2024_Blog_UUM_Universal-User-Modeling-Snapchat.md
- title: Universal User Modeling (UUM): A Foundation Model for User Understanding at Snapchat
- url: https://eng.snap.com/universal_user_modeling
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D9 | 2024_ICML_HSTU_Actions-Speak-Louder-Generative-Recommendations.md
- title: Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations
- url: https://arxiv.org/pdf/2402.17152.pdf
- objective: Generative Recommenders (GRs) trained in streaming one-pass settings on user action sequences (items + action types + timestamps). Ranking uses multi-task Normalized Entropy (NE) on main engagement task (E-Task) and main consumption task (C
- pred_vs_inc: Predicts next actions / ranks candidates from sequential representations—predictive modeling of engagement intensity and ordering, not causal incrementality of exposure on retention.
- credit: Fully sequential formulation over user action history; targets are next engagement/consumption events in the sequence—implicit credit via autoregressive transduction, not user-level delayed outcome at
- gains: Up to 65.8% NDCG lift on Amazon Books (HSTU-large vs SASRec); 12.4% online E-Task win; 285× more complex GR with higher QPS than DLRM at 1024–16384 candidates via M-FALCON.

## D8 | 2024_InfoQ_NA_Model-based-Recall-Momo-Social-Recommendation.md
- title: 模型化召回在陌陌社交推荐的应用和探索 (Model-based Recall in Momo Social Recommendation)
- url: https://www.infoq.cn/article/7s6oqecgk8bmckobj0ud
- objective: Recall-stage embedding models trained on scene interaction labels (click, like, comment, greet, follow, reply); losses include Weighted-Hinge-Loss for ANN retrieval and multi-objective user representation learning split by interaction type;
- pred_vs_inc: Predicts user–item / user–user compatibility embeddings for ANN retrieval; not causal incrementality of exposure on long-term outcomes.
- credit: Pointwise / pair-level interaction labels aggregated into embedding training; graph edges weighted by relationship strength; no IPS, counterfactual correction, or user-level delayed outcome attributio
- gains: Scene-preference U2I/U2U2I recall: interaction conversion rate +15%+; content-semantics I2I recall: interaction conversion rate +10%+ (A/B); social-matching GCN recall: social matching rate +10%+ (A/B).

## D2 | 2024_KDD_FID_Future-Impact-Decomposition-Request-Level.md
- title: Future Impact Decomposition in Request-level Recommendations; Xiaobei Wang, Shuchang Liu, Xueliang Wang, Qingpeng Cai, Lantao Hu, Han Li, Peng Jiang, Kun Gai, Guangming Xie (Kuaishou Technology / Peki
- url: https://arxiv.org/pdf/2401.16108.pdf
- objective: Maximize expected cumulative discounted list reward E[∑ γ^i R(s_{t+i}, a_{t+i})]; offline click-or-not (1.0 / −0.2); online linear combination of watch time, like, follow, collect, comment; episode depth capped at 20 offline; 1-week online 
- pred_vs_inc: Policy-value / cumulative-reward RL (A2C); predicts V(s) and item-level advantages; not incrementality/uplift modeling.
- credit: Linear list reward R = ∑ r_{t,k}; equal or weighted share of next-state value V(s_{t+1}) assigned per item via w_{t,k}; item-level advantage A(s_t, i_{t,k}, w_{t,k}) drives pointwise policy updates.
- gains: KuaiRand: ItemA2C-M total reward 16.03 vs HAC 12.65 (+27% reward, +20% depth); ML1M: 17.94 vs 17.53 (+2.3% / +1.8%); online vs request-level A2C: watch time +0.129%, like +1.103%, follow +0.300%, collect +0.963%, comment

## D2 | 2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow.md
- title: Modeling User Retention through Generative Flow Networks
- url: https://doi.org/10.1145/3637528.3671531
- objective: End-of-session retention reward R (user return frequency) plus per-step immediate rewards r_t (weighted clicks, watch time, likes, etc.); between-session delayed signal
- pred_vs_inc: Generative flow matching / policy learning (not pointwise CTR prediction)
- credit: Backward probabilistic flow back-propagates terminal retention to each session step (“retention attribution”); immediate rewards enter per-step DB term −α·r_t
- gains: Authors report superiority over CEM, DIN, TD3, SAC, RLUR in offline and live experiments; exact metric percentages: Not specified in source (NLM Q2 failed)

## D1 | 2024_KDD_LiRank_Industrial-Large-Scale-Ranking-LinkedIn.md
- title: LiRank: Industrial Large Scale Ranking Models at LinkedIn
- url: https://arxiv.org/pdf/2402.06859.pdf
- objective: Multi-task pointwise ranking: Feed predicts like, comment, share, vote, click, long dwell per (member, post) pair; Ads CTR uses chargeability-based MTL with three heads; Jobs predict application and click probabilities. Long dwell defined a
- pred_vs_inc: Predicts probabilities of short-horizon engagement events and dwell exceedance; Thompson sampling on last-layer weights explores for long-term DAU gains—not causal incrementality modeling of exposure 
- credit: Pointwise (member, item) labels per impression; no session-level delayed outcome propagation to individual items stated; long dwell and session metrics evaluated at aggregate A/B level.
- gains: +0.5% Feed member sessions; +1.76% qualified job applications (Jobs search/recommendations); +4.3% Ads CTR relative in online A/B; +0.06% professionals DAU from Thompson sampling; Ads quantization +0.9% CTR relative in o

## D1 | 2024_KDD_MO-LTR-MD_Multi-Objective-Learning-to-Rank-Distillation.md
- title: Multi-objective Learning to Rank by Model Distillation
- url: https://doi.org/10.1145/3637528.3671597
- objective: Primary hard label: booked listing = 1, other impressions 0 (listwise softmax CE). Soft labels: weighted sum of frozen per-objective teacher model scores (or prior student model scores in self-distillation). Secondary objectives include can
- pred_vs_inc: Student MLP predicts ranking scores matching primary hard labels while distilling multi-objective teacher score ordering via soft labels—predicts booking propensity under multi-objective regularizatio
- credit: Listwise labels per search impression list; booked listing attributed back to search containing booking; soft labels encode full list ordering from teachers—partial user preference on unbooked items r
- gains: Offline +1.1% NDCG vs MTL baseline; online +0.37% booking (CVR) with p_val=0.02; secondary objectives neutral in A/B; soft-label ad-hoc boost −0.1% NDCG vs −0.5% for serving-time score boost at matched high-rating listin

## D3 | 2024_KDD_NA_Choosing-Proxy-Metric-Past-Experiments.md
- title: Choosing a Proxy Metric from Past Experiments
- url: https://arxiv.org/pdf/2309.07893.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D3 | 2024_KDD_NA_Learning-Covariance-Treatment-Effects-Weak-Experiments.md
- title: Learning the Covariance of Treatment Effects Across Many Weak Experiments
- url: https://doi.org/10.1145/3637528.3672034
- objective: Primary metric \(Y\) (long-term, e.g. retention/revenue) and secondary surrogates \(S\); population estimand is covariance matrix \(\Lambda_K\) of true cross-experiment ATEs on \((Y,S)\) and OLS/TLS slopes \(\theta_1,\theta_{2,\Psi}\) in th
- pred_vs_inc: Under stated structural models (full mediation, INSIDE direct effects, or small-effect NPIV), \(\theta_1\) identifies mediated or natural-indirect components of ATE on \(Y\) — supports unbiased surrog
- credit: Experiment-level only — each historical test contributes one \((\hat\tau_Y,\hat\tau_S)\) point; no within-experiment user-to-item attribution; homoskedastic \(\Omega\) assumed known/estimated across u
- gains: Simulations: TC and LIMLK far less biased than naive OLS on ATE scatterplot under weak effects; with direct effects LIMLK inconsistent, TC remains consistent for \(\beta\); Netflix TC median absolute bias reduction ~63% 

## D1 | 2024_KDD_Trinity_Syncretizing-Long-Tail-Long-Term-Interests.md
- title: Trinity: Syncretizing Multi-/Long-Tail/Long-Term Interests All in One
- url: https://arxiv.org/pdf/2402.02842.pdf
- objective: Retrieval positives: watch >10s, finish, or engagement (upvote/share/follow/comment); re-rank staytime objective with negatives if watched ≤2s and playtime-weighted in-batch softmax (clipped at 5 minutes). Online metrics: Watch Time, Averag
- pred_vs_inc: Retrieval uses statistical cluster histograms and rule-based cluster selection—not direct LTV prediction; re-rank models predict playtime-weighted relevance for candidate pruning.
- credit: Long-term behavior sequence (up to 2500 actions) aggregated into cluster histograms h1/h2; per-cluster counts drive retrieval—not item-level mapping of user retention to a single past exposure.
- gains: Trinity-M: +0.118% Watch Time, +0.008% AAD, +0.046% AAH, +0.153% AT on Douyin; +0.178% Watch Time, +0.018% AAD, +0.078% AAH, +0.038% AT on Douyin Lite. Trinity-LT: +0.069% Watch Time, +0.546% AT on Douyin Lite. Trinity-L

## D8 | 2024_RecSys_NA_Fair-Reciprocal-Recommendation-Matching-Markets.md
- title: Fair Reciprocal Recommendation in Matching Markets
- url: https://doi.org/10.1145/3640457.3688130
- objective: Maximize expected total matches (social welfare) subject to envy-freeness of recommendation opportunity; utility = expected match count per agent; labels from like/dislike and match/sorry interactions; 200×200 dense subsample for ALS prefer
- pred_vs_inc: Predicts absolute expected match outcomes under a position-based ranking policy given offline-estimated asymmetric preference probabilities p₁(i,j), p₂(j,i); not incrementality modeling.
- credit: Not specified in source; ranking policy optimized at market level, not per-exposure delayed-outcome attribution.
- gains: Real data (log examination): NSW 90.39 matches vs SW 111.37 with male envy 31 vs 434 and female envy 14 vs 331; inverse examination: NSW 59.37 matches vs SW 74.95 with male envy 19 vs 330 and female envy 8 vs 254.

## D3 | 2024_WWW_NA_Long-Term-Off-Policy-Evaluation-Learning.md
- title: Long-term Off-Policy Evaluation and Learning
- url: https://arxiv.org/pdf/2404.15691.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D8 | 2024_WWW_NA_Online-Reciprocal-Recommendation-Performance-Guarantees.md
- title: Online Reciprocal Recommendation with Theoretical Performance Guarantees
- url: https://arxiv.org/pdf/1806.01182.pdf
- objective: Maximize number of uncovered mutual matches \(M_T\) within \(T\) rounds; binary pairwise preferences \(\sigma(b,g)\in\{-1,+1\}\); performance vs omniscient matchmaker knowing full \(\sigma\).
- pred_vs_inc: Learns cluster structure from implicit feedback to accelerate match discovery; not LTV/revenue prediction or treatment uplift.
- credit: Round-level pairwise feedback \((b,g)\mapsto\sigma\); matches credited when reciprocating positive edge observed (possibly across rounds). No delayed retention or revenue labels.
- gains: Theorem: under clusterability, SMILE uncovers \(\Theta(M)\) matches in \(T=\omega(n(C_G+C_B)+n^3\log n/M)\) rounds, comparable to omniscient matchmaker when \(M,T\) not too small; empirically I-SMILE dominates random bas

## D2 | 2024_arXiv_AURO_Adaptive-User-Retention-Optimization.md
- title: AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems
- url: https://doi.org/10.1145/3696410.3714956
- objective: Retention reward at episode end: r = λ × user return time (zero at other steps); return time is the gap until the user returns to the platform; optimizes long-horizon accumulated return in MDP sessions—not immediate CTR alone.
- pred_vs_inc: Actor-critic RL policy selects top-k items from candidate pool; state-abstraction module signals environment drift to adapt policy; guarded exploration via performance-based rejection sampling—not exp
- credit: Session-level retention reward assigned to last step of episode; immediate click/like/comment rewards at intermediate steps in live evaluation; sparse delayed return-time signal drives long-horizon cr
- gains: KuaiSim: AURO 1.531±0.058 average return days vs RLUR 1.794±0.070; Day-1 return rate 0.824±0.018 vs RLUR 0.731±0.026; retention reward −0.015±0.000 vs RLUR −0.018±0.000. Live vs RLUR: 7d retention +0.138‰, dwell time +0.

## D8 | 2024_arXiv_CUPID_Session-Based-Reciprocal-Recommendation.md
- title: CUPID: A Real-Time Session-Based Reciprocal Recommendation System for a One-on-One Social Discovery Platform
- url: https://arxiv.org/pdf/2410.18087.pdf
- objective: Maximize overall user satisfaction proxied by total chat duration across pairs; label y_ij = observed chat duration per match history m_i,k = (u_i, u_j, y_ij); training loss is MSE on log-scaled chat durations; no retention/LTV horizon or d
- pred_vs_inc: Predicts expected chat duration ŷ_ij = f(u_i, u_j) for all pairs in matching pool U(t); scores feed business-logic matching algorithms; not incrementality or causal treatment-effect modeling.
- credit: Pair-level regression to realized chat duration; no slate-level, impression-level, or multi-step retention credit assignment.
- gains: Online vs Wide&Deep baseline: average chat duration +6.8% (warm-start), +5.9% (cold-start); long-match ratio +12.6%/+12.9%; latency −79.7% (p90) and −75.9% (p99) vs synchronous session modeling; offline AUROC up to 0.873

## D1 | 2024_arXiv_EnhancedRL_Enhanced-State-RL-Multi-Task-Fusion.md
- title: EnhancedRL: An Enhanced-State Reinforcement Learning Algorithm for Multi-Task Fusion in Recommender Systems
- url: https://arxiv.org/abs/2409.11678
- objective: Maximize session cumulative reward G_t with discount γ; per user–item pair instant reward r(s_{tj}, a_{tj}) = Σ w_i · v_i (watch time, valid consumption >10s, like/share/collect); list reward r(s_t, a_t) = Σ_j r(s_{tj}, a_{tj}); fusion via 
- pred_vs_inc: Offline RL actor–critic with enhanced state (user + item + MTL predictions + context) outputs per user–item fusion weights—policy optimization, not pointwise outcome prediction.
- credit: Per user–item pair state and action; critics aggregate list-item Q-values and rewards for TD update; session-level cumulative reward—item-granular fusion weights vs UnifiedRL’s single user-level actio
- gains: Online vs UnifiedRL: +3.84% user valid consumption, +0.58% user duration time; offline MTF-GAUC 0.8037 vs UnifiedRL 0.7954; fully deployed in large-scale RS.

## D1 | 2024_arXiv_IntegratedRL-MTF_Offline-RL-Multi-Task-Fusion.md
- title: UnifiedRL: A Reinforcement Learning Algorithm Tailored for Multi-Task Fusion in Large-Scale Recommender Systems
- url: https://arxiv.org/abs/2404.17589
- objective: RL maximizes discounted cumulative session reward G_t = Σ γ^i r(s_{t+i}, a_{t+i}); instant reward r(s_t, a_t) = weighted sum over list items of watch time, valid consumption (>10s), like/share/collect, etc.; action a is 10-D fusion weight v
- pred_vs_inc: Offline RL actor–critic learns fusion-weight policy maximizing session cumulative reward—policy optimization over logged exploration data, not pointwise outcome prediction.
- credit: User-level state (profile + behavior sequence + stats); single fusion-weight action per request applied to all candidates via Eq. 1; instant reward summed over full recommendation list l items; sessio
- gains: Online vs ES: +4.64% user valid consumption, +1.74% user duration time; offline MTF-GAUC 0.7953 vs ES 0.7836; deployed in multiple Tencent RSs plus search and ads.

## D3 | 2024_arXiv_NA_Dynamically-Adjusted-Surrogate-Index.md
- title: Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index
- url: https://arxiv.org/pdf/2103.08390.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D6 | 2024_arXiv_NA_End-to-End-Cost-Effective-Incentive-Uplift.md
- title: End-to-End Cost-Effective Incentive Recommendation under Budget Constraint with Uplift Modeling
- url: https://arxiv.org/pdf/2408.11623.pdf
- objective: CATE-style uplifts τ^c_{i,k} (conversion) and τ^r_{i,k} (revenue/cost) vs control k=0; treatments k∈{0,…,K}; budget constraint on sum of cost uplifts; monotonic smooth response curves enforced structurally.
- pred_vs_inc: Incrementality (uplift/CATE) for allocation; end-to-end joint training of uplift heads and differentiable ILP allocation layer.
- credit: User-level treatment assignment (which incentive level per customer); not item-level ranking in a feed.
- gains: Binary Hillstrom-Men/Women: E3IR best on AUUC/QINI/KENDALL/AUCC vs meta-learners, DragonNet, TPM-SL, Direct Rank, DRP (Table 1, e.g., Men KENDALL 0.7033 vs DRP 0.6811). Multi-treatment: Hillstrom MT-AUCC 0.0803 vs DRM 0.

## D2 | 2024_arXiv_NA_Maximum-Entropy-Decision-Transformer-Reward-Relabelling.md
- title: Maximum-Entropy Regularized Decision Transformer with Reward Relabelling for Dynamic Recommendation
- url: https://arxiv.org/abs/2406.00725
- objective: Binary click reward per interaction—ratings above 75% of max scale count as positive; return-to-go (RTG) = sum of future rewards conditions the DT; no multi-day retention or revenue horizon defined.
- pred_vs_inc: Prediction/policy optimization for expected discounted click reward; no causal incrementality or treatment-effect framing.
- credit: RTG relabeling propagates revised return estimates backward across trajectory timesteps using CQL Q-values—credit from other trajectories sharing states, but for click-level reward only, not delayed r
- gains: KuaiRand-1k: EDT4Rec Recall 31.256±0.241% vs CDT4Rec 30.322±0.208%; similar margins on LibraryThing, Book-Crossing, GoodReads, MovieLens-20M, Netflix (Table 1). VirtualTaobao: higher average CTR with tighter variance tha

## D6 | 2024_arXiv_NA_Multi-Channel-Uplift-Policy-Learning.md
- title: Multi-channel Uplift Policy Learning
- url: https://arxiv.org/pdf/2607.28182.pdf
- objective: Maximize expected outcome μ(X,p)=E[Y(p)|X]; decision primitive is local causal reallocation gradient g*(X,p)=Π_T ∇_p μ on budget simplex; not scalar ITE per channel independently.
- pred_vs_inc: Causal uplift / marginal reallocation field; orthogonal teacher (DML-style) for unbiased local gradients; student distills marginal field for support-aware decisions.
- credit: Item-level (seller/product) budget split across channels; not user-feed impression credit.
- gains: Online A/B: pay orders +3.53% [+2.8%, +5.1%], platform income +3.26 pt, profit margin +1.42 pt, total cost −2.47%, GMV −2.64%, marketing ROI unchanged; offline DR lift 0.025 vs baselines; support violations 0.000 vs 0.67

## D6 | 2024_arXiv_NA_Rankability-Enhanced-Revenue-Uplift-Modeling.md
- title: Rankability-enhanced Revenue Uplift Modeling Framework for Online Marketing (RERUM)
- url: https://arxiv.org/pdf/2405.15301.pdf
- objective: CATE \(\tau(x)=E[Y|X=x,T=1]-E[Y|X=x,T=0]\) with continuous revenue response \(Y\); ranking metrics AUUC, AUQC, KRCC, LIFT@30; online LIFT@2 on top-2% ranked users over 1-month sales window.
- pred_vs_inc: Estimates heterogeneous treatment effect on continuous revenue; optimizes uplift ranking via ZILN response heads plus listwise uplift ranking loss—incrementality for campaign targeting, not exposure e
- credit: User-level RCT samples \((x,t,y)\); pairwise/listwise losses align predicted uplift order across treatment and control arms—no per-impression delayed credit.
- gains: Offline: RERUM(DragonNet) improves LIFT@30 by 21.98% on average vs best baseline across three datasets; online LIFT@2 +9.20%, +37.24%, +15.43% across three campaigns (20.61% average), authors report 430M USD AUM gain per

## D8 | 2024_arXiv_NA_Revisiting-Reciprocal-Recommender-Systems.md
- title: Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method
- url: https://arxiv.org/pdf/2408.09748.pdf
- objective: Primary outcome = final match (r_ij ∈ {0,1}); direction label d_ij indicates A→B vs B→A interactions; five holistic metrics — CRecall, CPrecision, SRecall, SPrecision, RNDCG@K — penalize duplicate bilateral hits; K=50; no retention/LTV hori
- pred_vs_inc: Causal reciprocal model estimates potential outcomes ŷ_t for bilateral treatment assignments t ∈ {10, 11, 01} under Rubin framework; ranking scores s_ai = ŷ_10 + ŷ_11, s_bj = ŷ_01 + ŷ_11; reranking us
- credit: Pair-level causal treatment effects across bilateral recommendation assignments; not session-level or long-horizon retention credit.
- gains: Dating CRRS (BPRMF): CRecall@50 0.3387 vs BPRMF 0.2795; True Positive Pairs 1,743 vs 1,439; RNDCG@50 0.0849 vs 0.0660; Recruitment CRRS: CRecall@50 0.4670 vs DPGNN 0.4555 but SRecall 0.1248 vs 0.1535 (coverage–stability 

## D1 | 2025_SIGIR_SORT-Gen_Generative-Re-ranking-List-Level-Multi-Objective.md
- title: A Generative Re-ranking Model for List-level Multi-objective Optimization at Taobao
- url: https://doi.org/10.1145/3726302.3731935
- objective: List-level value maximization \(\alpha V_{click} + \beta V_{conversion} + \gamma V_{GMV}\) with sequential incremental accumulation over positions; training uses ordered regression on real exposed lists — cumulative click/pay counts per sub
- pred_vs_inc: Predicts list-level cumulative click/conversion/GMV values for sub-lists and selects items to maximize weighted multi-objective value — supervised prediction of short-horizon engagement outcomes, not 
- credit: List-level credit — clicks/conversions anywhere in the exposed list contribute to cumulative list-value labels; position-aware ordered regression attributes incremental value across list positions wit
- gains: vs greedy formula baseline: +9.61% CLICK, +8.35% ORDER, +13.67% GMV (Table 1, asterisked); vs FFT Context-aware + fastDPP: +4.13% CLICK, +8.10% GMV; deployed across multiple Taobao App scenarios.

## D4 | 2025_arXiv_CC-OR-Net_Unified-LTV-Prediction-Structural-Decoupling.md
- title: CC-OR-Net: A Unified Framework for LTV Prediction through Structural Decoupling
- url: https://arxiv.org/pdf/2601.10176.pdf
- objective: Non-negative lifetime value \(y\in\mathbb{R}^+\) per user; \(K=4\) ordinal buckets (zero + three quantile splits on positives); trilemma: ranking (Gini, Spearman), regression (NMAE, MAPE, NRMSE), whale precision (AMBE, SVA stratified accura
- pred_vs_inc: Supervised LTV point prediction with architecturally guaranteed ordinal ranking; not causal incrementality of exposure.
- credit: User-level LTV label only; no session/impression or two-sided credit assignment.
- gains: vs baselines on Domain 1: Gini 0.803, Spearman 0.761, SVA 67.01%, whale-bucket AMBE 4.849 (−25.0% vs w/o augmentation); Recall@5000 whales 38.1% vs ExpLTV 36.5%; inference 0.79 ms (100k batch).

## D4 | 2025_arXiv_GRePO-LTV_Mini-Game-Lifetime-Value-WeChat.md
- title: Mini-Game Lifetime Value Prediction in WeChat
- url: https://arxiv.org/abs/2506.11037
- objective: Cumulative payment a user contributes to a specific game over 3-, 7-, or 30-day horizons after registration.
- pred_vs_inc: Predicts absolute multi-horizon payment value per user–game pair; not causal incrementality.
- credit: Delayed payment label assigned to user–game pair \((u_p, i_q)\); not slate/impression-level attribution.
- gains: Avg offline NMAE 0.188 vs best baselines (+14.0% NMAE, +3.6% AUC, +1.6% N-GINI); online avg LTV/GMV +8.4% (3d +9.9%/+9.83%, 7d +7.8%/+7.93%, 30d +7.73%/+7.60%).

## D1 | 2025_arXiv_MTFM_Alignment-Free-Foundation-Model-Meituan.md
- title: MTFM: A Scalable and Alignment-free Foundation Model for Industrial Recommendation in Meituan
- url: https://arxiv.org/abs/2602.11235
- objective: Per-scenario, per-task supervised labels: CTR and CTCVR on HP/PHF; CTR, CTCVR, IMD (30-minute redemption), WRITE (24-hour redemption) on SQS — immediate click/conversion/redemption events, no explicit multi-week retention or LTV horizon in 
- pred_vs_inc: MMoE heads on final T-token embeddings output separate scenario-specific task scores — standard supervised prediction of short-horizon conversion events, not causal incrementality on long-term outcome
- credit: Item/exposure-level labels per candidate T-token after user-level aggregation across scenarios; shared H/R tokens carry cross-scenario behavior — standard logged-label supervision, no delayed user-out
- gains: Offline: MTFM best across scenarios — e.g. HP CTR GAUC 0.6954, CTCVR GAUC 0.6507; SQS CTR GAUC 0.8027. Online: SQS orders +2.98%, CTR +1.89%, UV_CTCVR +2.46%, latency −5ms; PHF orders +1.45%, CTR +1.53%, UV_CTCVR +1.03%,

## D9 | 2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md
- title: MTGR: Industrial-Scale Generative Recommendation Framework in Meituan
- url: https://arxiv.org/pdf/2505.18654.pdf
- objective: Discriminative CTR and CTCVR prediction on user–candidate pairs reorganized as token sequences; labels are click and click-through-conversion events from industrial logs — no explicit retention, LTV, or revenue-per-user objective in trainin
- pred_vs_inc: Predicts per-candidate CTR/CTCVR logits from unified token sequence — supervised ranking, not causal incrementality.
- credit: Standard supervised CTR/CTCVR labels per candidate token after user aggregation; cross features encode user–candidate historical CTR/exposure — pointwise logged labels, no IPS or delayed-outcome user 
- gains: MTGR-large vs DLRM baseline: offline CTR GAUC +0.8956%, CTCVR GAUC +1.4656%; online PV_CTR +1.31%, UV_CTCVR +1.22%; 65× forward FLOPs per sample with training cost unchanged and inference cost −12% vs DLRM; TorchRec thro

## D6 | 2025_arXiv_NA_Counterfactual-Reciprocal-Recommender-User-Matching.md
- title: Counterfactual Reciprocal Recommender Systems for User-to-User Matching
- url: https://arxiv.org/pdf/2508.01867.pdf
- objective: Learn compatibility score \(s(u,v;\Theta)\) predicting mutual acceptance \(R(u,v)\) under a uniform target distribution over pair space \(\mathcal{P}=U\times V\); label \(r(u,v)\) observed only when pair is displayed \(O(u,v)=1\). No time h
- pred_vs_inc: Selection-bias-corrected prediction of mutual acceptance via IPS/SNIPS/DR reweighting; not incremental effect of exposure on retention/revenue.
- credit: Direct pair-level: one displayed pair \((u,v)\) yields one bilateral outcome \(r(u,v)\); no slate-level or delayed user-outcome attribution.
- gains: NDCG@10: +2.7% Synthetic (0.307 vs 0.299 LFRR), +3.5% DBLP (0.475 vs 0.459), +0.9% Epinions; Coverage@10 +51% Synthetic (0.763 vs 0.504); Gini-Exposure −24% Synthetic (0.535 vs 0.708).

## D4 | 2025_arXiv_NA_Generative-Sequential-Notification-Optimization.md
- title: Generative Sequential Notification Optimization via Multi-Objective Decision Transformers
- url: https://arxiv.org/pdf/2509.02458.pdf
- objective: Multi-objective discounted return-to-go over finite-horizon episodes (length T+H) sampled from continuous interaction streams; reward vector includes predicted click/open value, actual inter-state visits, and adaptive volume-penalty fatigue
- pred_vs_inc: Return-conditioned policy learning (offline RL as supervised sequence modeling); not explicit CATE/uplift—uses predicted engagement models as reward components plus realized visit rewards.
- credit: User-level sequential notification decisions; rewards mix candidate-level predicted CTR/open with user visit events between states—not item-level attribution of long-horizon retention to a single feed
- gains: +0.72% user sessions vs multi-objective CQL while reducing notification volume; learned RTG prompts and context length 4 ablations contribute incrementally; production at 100–150K QPS.

## D1 | 2025_arXiv_NA_Multi-Objective-Ranking-Live-Streaming-Delayed-Signals.md
- title: Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals with Segment-Aware Targeting
- url: https://arxiv.org/pdf/2608.04455.pdf
- objective: Multi-task targets: SMP (shallow minutes-play, immediate), LMP (long minutes-play, immediate), chat/follow/spend (14-day delayed window); business metrics DAV (daily active viewers), capped ARPU, LMP, follows.
- pred_vs_inc: Pointwise multi-task probability predictions fused into ranking score; not causal uplift.
- credit: Impression-level labels with 14-day delayed aggregation for sparse targets; 35-day forward eval window; immediate labels for SMP/LMP.
- gains: Online Exp.1: DAV +0.09% (\(p<0.01\)), LMP +0.16%, D-viewer capped ARPU +0.56% (\(p<0.05\)); Exp.2 VST: E-viewer DAV +0.15%, LMP +0.25%; Exp.3 MMoE: DAV +0.08%, follows +0.27%; MMoE cuts delayed-target params 41.9% (26.7

## D6 | 2025_arXiv_NA_Off-Policy-Evaluation-Learning-Matching-Markets.md
- title: Off-Policy Evaluation and Learning for Matching Markets
- url: https://arxiv.org/pdf/2507.13608.pdf
- objective: Policy value \(V(\pi)=\frac{1}{|C|}\sum_c\sum_j \pi(j|c)\,q_s(c,j)\,q_r(c,j)\): expected number of mutual matches. First-stage \(s\): scout sent; second-stage \(r\): reply; terminal match \(m=s\cdot r\).
- pred_vs_inc: Estimates expected match outcomes under a target policy via OPE; predicts conditional q-functions, not causal uplift of exposure.
- credit: Logged bandit tuples \((j_c,s_c,r_c)\) map first/second-stage rewards to company context \(c\) (date, interaction rank, company ID) and job seeker \(j\) (date, seeker ID).
- gains: DiPS/DPR achieve significantly lower MSE than IPS/DR across synthetic configurations; DPR lowest MSE on Wantedly at all sample sizes; DiPS-PG/DPR-PG highest policy values under sparse rewards and large action spaces.

## D1 | 2025_arXiv_NA_Save-Revisit-Retain-User-Retention.md
- title: Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems
- url: https://arxiv.org/pdf/2511.18013.pdf
- objective: Adds merged revisitation head RP&RV predicting save-then-revisit: same-day revisitation impression (1dRevImpre), same-day revisitation grid-click (1dRevGrid), and 7-day revisitation grid-click (7dRevGrid) within 0–6 days after repin; fused 
- pred_vs_inc: Predicts probability of joint repin-and-revisit outcomes from exposure logs—surrogate attribution links save on Related Pins to later profile revisit by user ID + Pin ID, not causal incrementality of 
- credit: Surrogate attribution: revisitation credited only to the saved Pin when user revisits that Pin on own profile within 7 days (same-day or cross-day rules); cross-surface join on user ID and Pin ID with
- gains: Offline: revisitation head NDCG@3 +40.15%, Hits@3(repin) +0.59%, Hits@3(revisit) +0.65%; online: 7dRevGrid +1.18% volume / +1.42% propensity, repin +0.94% / +0.64%, active users +0.10% volume / +0.08% propensity, session

## D2 | 2025_arXiv_NA_Stratified-Expert-Cloning-Retention-Aware.md
- title: Stratified Expert Cloning for Retention-Aware Recommendation at Scale
- url: https://arxiv.org/abs/2504.05628
- objective: Maximize expected long-term retention \(E_u[R_u \mid \pi]\) measured by active days in a window (online: 7-day Active Days) or return time / engagement in offline KuaiSim; expert users stratified by retention score (active days/month or LTV
- pred_vs_inc: Behavior cloning from high-retention expert trajectories — learns policies that mimic expert actions given user state, indirectly optimizing retention without explicit reward-modeling or uplift estima
- credit: Trajectory-level imitation — retention outcome attributed implicitly through expert demonstration labels rather than per-action delayed reward backprop; adaptive selection maps current user state to n
- gains: Offline Return Time 1.411 vs GFN 1.496 (−5.7%); online cumulative Active Days +0.098% (Kuaishou) and +0.122% (Kuaishou Lite), each >200k additional DAU; valid interest clusters +1.31% / +1.14%.

## D8 | 2025_arXiv_NA_Two-Sided-Prioritized-Ranking-Marketplace-Experiments.md
- title: Two-Sided Prioritized Ranking: A Coherency-Preserving Design for Marketplace Experiments
- url: https://arxiv.org/pdf/2502.09806.pdf
- objective: Estimand is global lift Φ — proportional change in query-level outcomes when all items are treated vs. all untreated; outcomes y_{q,i} are clicks, bookings, or revenue aggregated per query; not a recommender ranking objective.
- pred_vs_inc: Causal experimental-design framework; uses recommender relevance scores only to break ties within priority tiers, not to optimize ranking quality.
- credit: Not applicable — paper designs experiments to estimate global treatment effects under within-list interference (limited attention + unit-demand substitution), not per-impression delayed outcome attrib
- gains: Monte Carlo evidence that TSPR identifies global treatment effect under coherency constraints where user-level and naive item-level designs fail; semi-synthetic Expedia calibration.

## D9 | 2025_arXiv_OneRec_Technical-Report-Generative-Recommender.md
- title: OneRec Technical Report
- url: https://arxiv.org/pdf/2506.13695.pdf
- objective: Pre-training: next-token prediction (LNTP) on tokenized video semantic IDs from multi-scale user behavior (short, positive-feedback, lifelong compressed histories). Post-training: RSFT filters bottom 50% sessions by play duration; RL aligns
- pred_vs_inc: Predicts generative item distributions and optimizes policy rewards from a learned preference model—not causal incrementality of a single exposure on retention/revenue.
- credit: Session-level generative outputs scored by reward model on (user, generated item) pairs; RSFT drops low-duration sessions; RL samples 512 items per user with per-item P-Score rewards—credit at generat
- gains: 10× FLOPs vs prior ranker; 5.2×/2.6× MFU vs original ranking model; online App Stay Time and LT7 lifts; RL with vtr reward: up to +5.84% Watch Time, +1.82% App Stay Time (pass@128, group 2048 ablation).

## D9 | 2025_arXiv_OneRec_Unifying-Retrieve-Rank-Generative-Recommender.md
- title: OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment
- url: https://arxiv.org/pdf/2502.18965
- objective: Session training: autoregressive next semantic-token prediction on user history (likes, follows, shares, effective watches) and session target lists tokenized via multi-level balanced residual K-Means on aligned multimodal embeddings; IPA s
- pred_vs_inc: Generates session item lists via autoregressive semantic IDs; DPO aligns to reward-model preferences — predictive generative ranking, not causal incrementality of exposure on retention.
- credit: Session-level generative targets and DPO on chosen vs rejected full session responses from beam search; reward model provides per-user preference scores for hard-negative mining — not user-level delay
- gains: First industrial end-to-end generative ranker beating multi-stage cascade online; +1.68% Total Watch Time and +6.56% Average View Duration in online A/B; MoE scaling improves offline metrics; IPA/DPO improves generalizat

## D3 | 2025_arXiv_PROXIMA_Proxy-Metric-Validation-Segment-Fragility.md
- title: PROXIMA: Proxy Metric Validation with Segment-Level Fragility Detection for Online Controlled Experiments
- url: https://arxiv.org/pdf/2604.14352.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D1 | 2025_arXiv_UniROM_One-Model-to-Rank-Them-All.md
- title: One Model to Rank Them All: Unifying Online Advertising with End-to-End Learning (EGA-V1 / UniROM)
- url: https://arxiv.org/pdf/2505.19755.pdf
- objective: Pretrain on binary click labels ζ^clk ∈ {0,1} for K exposed + N_s=2995 popularity-sampled unexposed ads per request; post-train with RLAF maximizing platform revenue (bid × permutation-aware pCTR) under IC/IR payment constraints—no retentio
- pred_vs_inc: Predicts permutation-aware pCTR and generates ad allocations maximizing expected revenue—prediction and slate-level revenue attribution via marginal contribution rewards, not user-level incremental re
- credit: Slate/sequence-level: RL reward r_yi = marginal revenue contribution of ad y_i in generated sequence Y vs best sequence excluding it; supervised labels are per-ad clicks within request and session—not
- gains: Offline vs FS-LTR: Recall@50 +20.4%, AUC +1.48%, eCTR +8.3%, eRPM +11.4%, Ψ 9.1%→2.3%; online vs MCA: CTR +5.2%, RPM +13.6%, ROI +3.1%, response time +2.2% (~5 ms) despite scoring ~100× more candidates.

## D1 | 2025_arXiv_xMTF_Formula-Free-RL-Multi-Task-Fusion.md
- title: xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion in Recommender Systems
- url: https://arxiv.org/pdf/2504.05669.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D9 | 2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker-Netflix.md
- title: GenRec: An LLM-Backed Recommendation Ranker at Netflix
- url: https://arxiv.org/pdf/2608.10257.pdf
- objective: Phase 2 post-training combines (1) catalog-aware ranking cross-entropy on high-quality engagement labels (duration thresholds, thumbs-up, content-type-specific denoising) and (2) language modeling on verbalized histories. Explicit goal: max
- pred_vs_inc: Predicts item ranking scores and weights training by reward-model estimates of long-term value—correlational proxies, not stated causal incrementality of a single exposure on retention/revenue.
- credit: Request-level ranking loss weighted by reward models derived from engagement events; reward models estimate how strongly short-term events correlate with long-term outcomes—no explicit item-level dela
- gains: +1.6% offline MRR relative with ~40× less Phase-2 data; online +0.115% short-term engagement, +0.006% long-term core metric (both significant at Netflix scale).

## D3 | 2026_arXiv_NA_Evaluating-for-the-Long-Term-Industry.md
- title: Evaluating for the Long Term: Learnings from Industry
- url: https://arxiv.org/pdf/2608.08043.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D8 | 2026_arXiv_NA_Integrating-Predictive-Models-Two-Sided-Matching.md
- title: Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach
- url: https://arxiv.org/pdf/2602.19689.pdf
- objective: Integrator maps ML predictions (proposer login, proposer like, receiver login, receiver relike) into many-to-many recommendations; primary evaluation metrics are average dates, **effective dates** (congestion-discounted matches), and dating
- pred_vs_inc: Uses production gradient-boosted tree classifiers (AUC 0.80–0.92) to predict behavioral probabilities; integrators combine predictions into matchings — not causal incrementality of a recommendation on
- credit: Recommendation-level matching under capacity constraints; no delayed retention or revenue attribution to individual impressions.
- gains: Simulation: ECDA improves effective dates and receiver-side dating probability despite fewer total dates. Field DID (excluding top 0.1% receiver-days): statistically significant positive effects on average effective date

## D1 | 2026_arXiv_NA_Long-Term-Engagement-Downstream-Rewards-Learning.md
- title: Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning
- url: https://arxiv.org/pdf/2607.14192.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D1 | 2026_arXiv_NA_Long-Term-Value-Prediction-Framework-Video-Ranking.md
- title: A Long-term Value Prediction Framework In Video Ranking
- url: https://doi.org/10.1145/3774904.3792830
- objective: Ranking-stage LTV heads augmenting immediate engagement: PDQ-normalized slide time; multi-dimensional attributed slide time (contextual/behavioral/content signals); author-centric day-level LTV targets (censoring-aware, N-day delayed labels
- pred_vs_inc: Task-augmentation heads (PDQ, attribution module, author LTV) added to existing ranker predict LTV components; hybrid/Tweedie losses with noise filtering—predicts long-horizon engagement value, not ex
- credit: Multi-dimensional attribution learns continuous strengths across contextual, behavioral, content, author, co-occurrence signals; explicit noise filtering in hybrid loss; author LTV uses censoring-awar
- gains: Offline PDQ: XAUC 0.6378 vs baseline 0.6252 (+0.0126); MSE 0.0946 vs 4.9847. Attribution: XAUC +0.0118, MSE −0.8755. Online vs MSE baseline: PDQ +2.49% VV (baseline already +4% VV); Author LTV LT3 +0.21%, QA VV +4.03%; a

## D3 | 2026_arXiv_NA_Proximal-Surrogate-Index-Unobserved-Confounding.md
- title: The Proximal Surrogate Index: Long-Term Treatment Effects under Unobserved Confounding
- url: https://arxiv.org/abs/2601.17712
- objective: Primary outcome \(Y\) (e.g. year-4 weekly earnings, weeks employed); surrogates \(S\) (years 2–3 earnings/employment); proxies \(W\) (outcome-aligned, both samples) and \(Z\) (surrogate-aligned, observational only); experimental ATE on \(Y\
- pred_vs_inc: Identifies and estimates causal ATE on long-term \(Y\) via proximal surrogate index \(h_0(W,S,X)\) and multiply robust DML estimators — causal effect estimation, not predictive ranking of retention co
- credit: Unit-level causal estimand — no item-level or slate-level credit assignment; surrogates \(S\) mediate \(A \to Y\) under no-direct-effect assumption; proxies adjust for \(U\) confounding \(S\)–\(Y\) an
- gains: Proximal estimator closer to RCT benchmark than naive surrogate index for 4-year earnings (16.43 vs 7.05–7.30) and weeks employed (3.50 vs 0.80–0.84); larger standard errors than naive methods.

## D8 | 2026_arXiv_NA_Understanding-Guest-Preferences-Two-Sided-Airbnb.md
- title: Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example
- url: https://arxiv.org/pdf/2607.00280.pdf
- objective: Guest demand modeled via logit choice; price elasticity of demand estimated from host-set prices; segment-level heterogeneity in price sensitivity derived from how guest mix shifts with price; labels are booking/conversion shares by guest s
- pred_vs_inc: Causal price elasticity via supply-based instrumental variables isolating supply-driven price variation conditional on demand; observational estimates calibrated ("haircut") against pricing experiment
- credit: Geo-time panel attribution of guest-mix changes to price movements; not impression-level delayed retention credit assignment.
- gains: Enables ongoing guest price-sensitivity measurement where experiments are impractical; segment heterogeneity insights inform host pricing tools and guest personalization (e.g., affordable-listing marketing for price-sens

## D4 | 2026_arXiv_OCARM_Distilling-Post-Conversion-User-Retention.md
- title: Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling
- url: https://arxiv.org/pdf/2604.25839.pdf
- objective: 
- pred_vs_inc: 
- credit: 
- gains: 

## D1 | 2026_arXiv_PRL-PUTS_Personalized-Utility-Tuning-Pareto-Sweeping.md
- title: A Production-Ready RL Framework for Personalized Utility Tuning with Pareto Sweeping in Pinterest Recommender Systems (PRL-PUTS)
- url: https://arxiv.org/pdf/2605.16344.pdf
- objective: One-step contextual bandit (γ=0): agent selects discrete (Repin weight, P2P-impression weight) pairs applied to fixed ranker head scores; rewards are clipped binary request-level counts r^repin = min(n^repin,1), r^p2p = min(n^p2p,1) on top-
- pred_vs_inc: Learns Q^repin(s,a) and Q^p2p(s,a) expected immediate request rewards under chosen utility weights—policy selects weights to maximize engagement, not causal incremental effect of exposure on long-term
- credit: Request-level reward from engagement on the served top-k list; credit assigned to the chosen utility-weight action for that request, not to individual item exposures over a delayed retention window.
- gains: Global P2P-leaning policy (α=0.24): online Repin +0.66%, P2P +0.30%, Successful Sessions +0.13%; matched static average weights: Repin −0.24%, P2P +0.07%, SS +0.02% vs PRL-PUTS +0.12%/+0.21%/+0.11%; offline–online Pearso
