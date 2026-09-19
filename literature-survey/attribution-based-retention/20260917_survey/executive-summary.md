Date: 2026-09-17

# Attribution-based Retention — Executive Summary

## Key Questions

Questions this literature survey is trying to answer:

- **Q1.** What is the latest attribution-based approach in the industry? Scope: production or industry-authored attribution systems dated 2025-01 to 2026-09, plus the newest work from the teams and authors behind the classic papers in the parent survey.
- **Q2.** Has anyone in industry published attribution-based retention — that is, attributing user retention, engagement, or days-active to individual in-app interactions (recommendations, matches, messages, notifications, swipes)? No date limit for Q2. Academic work counts if it names a production dataset or deployment.

## Main Findings

### Direct answer to Q1

The 2025–2026 industry frontier shares one pattern: observational attribution scores, where they are used at all, are not the objective; decisions are trained or calibrated on incremental outcomes, and an experiment or an identification layer anchors the observational model. The 2025 anchors are `"Lewis et al., Amazon Ads Multi-Touch Attribution, arXiv 2025"` (an ensemble of observational attribution models calibrated to randomized-holdout lift) and `"Bencina et al., LiDDA: Data Driven Attribution at LinkedIn, arXiv 2025"` (attention-based data-driven attribution aligned to IPW-weighted experiment attribution and MMM shares). The 2026 exemplars extend that pattern. `"Li et al., Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising, ADKDD 2026"` anchors daily channel-level attribution to sparse incrementality experiments and reduces calibration error by 91.38% (channel-day level, not per touch). `"Wei et al., From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation, arXiv 2026"` trains a touch-sequence Transformer with DragonNet propensity heads and constrained allocation on user-level CATE and reports +7.20% LTV (p = 0.041). `"He et al., CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization in E-commerce Uplift Modeling, KDD 2026"` enforces conservation across cannibalizing treatments. `"Fumagalli et al., A Large Scale Heterogeneous Treatment Effect Estimation Framework and Its Applications of Users' Journey at Snap, arXiv 2025"` fits CATE on intention-to-treat experiment logs. `"Liu et al., ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization, ICLR 2026"` gives per-touch counterfactual deletion credit with front-door identification at 400M DAU. Two landscape items are not calibrated touch credit: `"Wu et al., Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?, CIKM 2026"` (LLM touchpoint selection, no causal correction) and `"Bhat et al., Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM, arXiv 2026"` (campaign-day credit anchored to MMM priors, no user-level tracking). Last-touch survives only as an operational label to be corrected (Li et al.) or as one auxiliary label view among several (Alibaba multi-attribution learning).

### Direct answer to Q2

Yes, in part. Direct per-interaction retention credit with production evidence exists at three platforms. `"WeChat/Tencent and Northeastern University authors, Interpretable User Retention Modeling in Recommendation, RecSys 2023"` scores every historical item with attention-based retention scores and improved next-day retention by 0.76% online. `"City University of Hong Kong, Kuaishou, and Nanyang Technological University authors, Modeling User Retention through Generative Flow Networks, KDD 2024"` propagates the terminal retention reward to each recommendation step by detailed balance (+0.015% next-day retention overall, +0.069% on low-activity users; a second-stage deployment showed +0.002%, not significant). `"Zhang, Improving Instagram Notification Management with Machine Learning and Causal Inference, Meta Engineering 2022"` learns per-notification incremental activeness from a 50% randomized send/drop holdout and is deployed.

Partial credit, with production evidence: `"Pinterest authors, Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning, RecSys 2026"` predicts a proxy downstream value per impression with user-prevalence normalization (deployed; no explicit offline multi-touch credit); `"Bakhshi et al., Retentive Relevance: Capturing Long-Term User Value in Recommendation Systems, arXiv 2025"` (Meta) attaches a survey-based per-item retention proxy (+0.030% sessions per user); `"McDonald et al., Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay, KDD 2023"` (Spotify) credits each item with predicted 60-day activity from progressive feedback (offline). The closest structural analogue is `"Liu et al., ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization, ICLR 2026"`, which credits a later in-app action (a creator upload) to individual consumed touchpoints by counterfactual deletion — the same shape as swipe → N7, with a different outcome.

Retention-aware ranking objectives are more common and are not attribution. `"Kishimoto et al., Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching, ICLR 2026"` (offline, on imputed dating-platform logs) and `"Ute et al., Not All Matches Are Equally Valuable: An Online Experiment of Retention-Focused Recommendation in a Job-Matching Platform, RecSys in HR 2026"` (online; churn odds ratio 0.957, not statistically significant) rerank for retention without attributing observed retention to past matches.

Negative evidence. The D3 web search found no per-interaction retention-credit publication from any named dating company (Tinder, Hinge, Match, Bumble, Grindr, Coffee Meets Bagel, Tantan/Momo, Badoo, Happn, The League), from any named gaming company (Roblox, Zynga, King, Supercell, EA, Riot), or from Snap, LinkedIn, or ByteDance/TikTok beyond the known Kuaishou/ByteDance retention-RL lineage. The same search missed Tencent's IURO, which the OpenAlex/arXiv harvest found, so the negative result is a statement about company engineering blogs, not about the whole literature. The dating-platform evidence is academic work on unnamed platforms (MRet by Hanjuku-kaso; MODE and the Nash-social-welfare paper by CyberAgent).

## Most Fundamental Methods

1. Front-door deletion MTA (Composite Score 9): explicit counterfactual touch credit plus identification under latent confounding. Proposed in `"Liu et al., ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization, ICLR 2026"`.
2. IURO attention credit (Composite Score 8): direct item-level retention scores with contrastive “aha item” selection and online retention gains. Proposed in `"WeChat/Tencent and Northeastern University authors, Interpretable User Retention Modeling in Recommendation, RecSys 2023"`.
3. Downstream Rewards (Composite Score 7): scalable per-impression downstream value with user-prevalence debiasing. Proposed in `"Pinterest authors, Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning, RecSys 2026"`.
4. Multi-dimensional LTV attribution (Composite Score 8): position-debiased item weights and delayed multi-day co-training. Proposed in `"Chen et al., A Long-term Value Prediction Framework in Video Ranking, WWW 2026"`.
5. Detailed-balance retention flow (Composite Score 8): terminal retention flows backward through non-last actions. Proposed in `"City University of Hong Kong, Kuaishou, and Nanyang Technological University authors, Modeling User Retention through Generative Flow Networks, KDD 2024"`.

Composite scores tie at 8 for eight further methods; the top-5 cut breaks ties by closeness to the Q2 problem (per-interaction retention credit), not by composite uniqueness. IURO and Downstream Rewards score 8 and 7 after the bias-device rescoring in method-tracker.md.

## Approach Comparison

| Approach | Pros | Cons | Related paper |
|---|---|---|---|
| Removal effect | Interpretable per-swipe score; easy to audit | A predictive model’s deletion effect is not automatically causal | `"Liu et al., ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization, ICLR 2026"` |
| Attention/instance credit | Direct per-item retention labels; production evidence | Attention can preserve confounding | `"WeChat/Tencent and Northeastern University authors, Interpretable User Retention Modeling in Recommendation, RecSys 2023"` |
| Downstream proxy reward | Dense, inexpensive labels; handles delayed funnels | Proxy gaming and incomplete causal identification | `"Pinterest authors, Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning, RecSys 2026"` |
| Uplift/CATE | Targets incremental outcomes and organic baselines | Requires overlap or randomized logs | `"Zhang, Improving Instagram Notification Management with Machine Learning and Causal Inference, Meta Engineering 2022"` |
| Flow/RL credit | Models long sequences and non-last actions | High complexity and unstable off-policy estimation | `"City University of Hong Kong, Kuaishou, and Nanyang Technological University authors, Modeling User Retention through Generative Flow Networks, KDD 2024"` |
| Retention-curve ranking | Low-cost, domain-specific shape prior | Forward allocation, not observed-outcome attribution | `"Kishimoto et al., Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching, ICLR 2026"` |

## Recommendations

Replace last-touch through three phases. Keep the binary rolling N7 target. In v1 the label is a predictive deletion residual, not an incremental effect; only v2 and v3 estimate incremental effects.

### v1 — Interpretable debiased removal effects

- Sources: `"Liu et al., ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization, ICLR 2026"` (deletion mechanic; note its outcome is upload, not N7); `"Dey et al., Sequential Multimodal Evidence Optimization for Product Media Ranking in E-Commerce, CIKM 2026"` (leave-one-out masking credit); `"WeChat/Tencent and Northeastern University authors, Interpretable User Retention Modeling in Recommendation, RecSys 2023"` (instance-scoring architecture); `"He et al., CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization in E-commerce Uplift Modeling, KDD 2026"` (conservation constraint); `"Pinterest authors, Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning, RecSys 2026"` (user-prevalence normalization); `"Zhang, Improving Instagram Notification Management with Machine Learning and Causal Inference, Meta Engineering 2022"` and `"Fumagalli et al., A Large Scale Heterogeneous Treatment Effect Estimation Framework and Its Applications of Users' Journey at Snap, arXiv 2025"` (randomized-holdout template); and `"Kishimoto et al., Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching, ICLR 2026"` as a feature prior only.
- Credit for swipe \(j\):  
  \[
  c_j=\hat P(Y_{N7}=1\mid H)-\hat P(Y_{N7}=1\mid H\setminus\{e_j\})
  \]
  where \(H\) is the time-ordered history available at the reference-day cutoff. c_j is a predictive deletion residual from a model of P(Y_N7 | H); it is not an incremental probability, and no cited paper estimates this exact contrast on N7. Preserve signed credit; report a normalized positive view \(c_j^+=\max(c_j,0)/(\sum_k\max(c_k,0)+\epsilon)\) only for explanation.
- Selection-bias device: subtract each user’s historical swipe/action prevalence when creating downstream features, following Downstream Rewards; stratify by baseline activity; include exposure propensity and position.
- Recurring outcome and heterogeneous touches: create one example per user-reference-day, with day-7 activity as the outcome. Link like, match, and message descendants to their originating swipe; represent each event with type, time gap, position, and counterpart state. Use MRet’s diminishing marginal match value as a regularizing feature, not as causal proof.
- Validation anchor: a small randomized candidate-exposure or score-perturbation holdout, evaluated on aggregate N7 lift and calibration.
- Cost: low to medium.
- Main risks: (1) the residual reflects user motivation and activity rather than causal impact; (2) leave-one-out residuals need not sum to the user-level outcome (non-conservation), so add a conservation constraint as in CanniUplift; (3) two-sided interference — one recommendation changes both users' opportunities (`"Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method, KDD 2024"` models this as a bilateral treatment); (4) the downstream ranker can fit user propensity instead of swipe quality; (5) a match used as a later feature leaks the ranking policy across the cutoff.
- Lead note (not from the surveyed literature): a mutual like requires the counterpart's decision, which the swiper does not control; conditional on candidate attractiveness, the match outcome is a partly random event that can serve as a natural experiment for the incremental value of a match, in the spirit of the Wantedly/MRet retention curves. Treat this as a candidate instrument to test, not an established device.

### v2 — Experiment-calibrated causal sequence attribution with survival

- Sources: `"Wei et al., From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation, arXiv 2026"`; `"Li et al., Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising, ADKDD 2026"`; `"Chen et al., A Long-term Value Prediction Framework in Video Ranking, WWW 2026"`.
- Credit for swipe \(j\):  
  \[
  \tau_j=\hat E[Y_{N7}\mid do(E_j=1),H_{-j}]
       -\hat E[Y_{N7}\mid do(E_j=0),H_{-j}]
  \]
  estimated by a sequence encoder with treated, control, and propensity heads. Calibrate cohort totals so \(\sum_j\tau_j\) matches randomized lift, analogous to ETDC’s experiment-to-observational correction.
- Selection-bias device: randomized exposure logs, DragonNet-style propensity sufficiency and targeted regularization, randomized snapshot dates, and overlap diagnostics.
- Recurring outcome and heterogeneous touches: jointly predict the binary N7 label and a discrete-time hazard \(h_d=P(T=d\mid T\ge d,H)\). Use typed swipe→like→match→message paths and rolling reference dates; prevent later events from leaking across the cutoff.
- Validation anchor: forward-in-time randomized readouts by activity cohort, position, and event path; compare summed predicted lift with observed N7 lift.
- Cost: medium to high.
- Main risk: insufficient overlap for profiles rarely withheld or shown, plus interference because one recommendation changes both users’ opportunities.

### v3 — Front-door and flow-based heterogeneous credit

- Sources: `"Liu et al., ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization, ICLR 2026"` and `"City University of Hong Kong, Kuaishou, and Nanyang Technological University authors, Modeling User Retention through Generative Flow Networks, KDD 2024"`.
- Credit for swipe \(j\), using mediator \(M_j\) such as match or substantive conversation:
  \[
  c_j^{FD}=\sum_m\!\left[P(m\mid do(E_j=1),H)-P(m\mid do(E_j=0),H)\right]
  \sum_{e'}E[Y_{N7}\mid m,E_j=e',H]P(E_j=e'\mid H)
  \]
  A flow model may then distribute the calibrated terminal value across the full typed trajectory.
- Selection-bias device: adversarial proxy-mediator learning, IPW for observed exposure factors, contrastive overlap restriction, and experiment-calibrated terminal rewards.
- Recurring outcome and heterogeneous touches: model each event type as a state transition; allow a match or message to mediate multiple earlier swipes while enforcing conservation so a retained day is not multiply counted.
- Validation anchor: randomized profile exposure plus mediator interventions where feasible; compare front-door and direct experimental estimates on eligible cohorts.
- Cost: high.
- Main risk: the front-door assumptions may fail if match/conversation mediators share unblocked causes with retention.

### Against the 2026-06-13 plan

Keep the core direction, but revise its identification and staging.

- Keep binary N7 as the production target.
- Keep v1 removal effects, but add user-prevalence normalization, position/exposure features, signed credits, and an experimental calibration holdout. Plain removal from a correlational model is not enough.
- Keep the deep v2 and survival head, but require treated/control/propensity heads and randomized snapshot construction before calling its output incremental.
- Add v3 as an optional front-door/flow layer after v2 is calibrated. The evidence does not justify beginning with GFN or front-door complexity.
- Do not ship MRet’s match-count curve as the attribution model. `"Kishimoto et al., Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching, ICLR 2026"` supports it as a reward-shape prior, while its card explicitly identifies it as a ranking policy.

### Why not keep last-touch

The strongest evidence is consistent across domains:

- `"Wei et al., From Prediction to Incrementality: Causal Optimization for Large-Scale Targeting and Recommendation, arXiv 2026"` explicitly randomizes snapshot dates to avoid last-touch leakage.
- `"Li et al., Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising, ADKDD 2026"` shows raw attribution can overstate causal lift and reduces calibration error by 91.38%.
- `"WeChat/Tencent and Northeastern University authors, Interpretable User Retention Modeling in Recommendation, RecSys 2023"` reports AUC 0.5838 for uniform historical credit versus 0.8445 for the full attention-based method on the public ZhihuRec split (0.6732 versus 0.7301 on the WeChat industry split), demonstrating strongly non-uniform retention value.
- `"Konitzer, Media Measurement and the Assisted Own Goal: Attribution, Marketing-Mix Models, and Individual-Level Incrementality, arXiv 2026"` shows, in a controlled simulation of off-platform observability (τ = 0.75, φ = 0), that last-touch credits a platform with only 25% of the conversions it caused; the failure mode is unobserved downstream outcomes, which maps to swipes whose retention effect arrives through later matches and conversations.
- `"Liu et al., ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization, ICLR 2026"` attributes value through counterfactual deletion rather than recency.

Last-touch therefore fails both distribution and identification: it ignores earlier causal paths and rewards activity that would have occurred anyway.

## Evaluation Protocol Without Per-interaction Ground Truth

### Offline estimators

- Precondition: an independent exposure holdout (assignment independent of the attributor) and a placebo-touch fixture (credit assigned to a never-shown profile or to a post-cutoff swipe must be ≈ 0) must exist before AUUC, Qini, or ranker N7 lift is read as causal; without them, deletion labels from P(Y_N7 | H) and a ranker trained on them can look strong while only tracking user activity.
- Train and evaluate on forward time splits with rolling reference dates.
- On randomized traffic, report AUUC, Qini, uplift calibration, and treated/control Brier or log loss.
- For ranking-policy evaluation, use doubly robust and self-normalized IPS estimators where propensities have support.
- Test conservation: per-swipe credits must reconcile with user-level predicted N7 lift and experiment-level aggregate lift.
- Run deletion and insertion sanity checks; specify negative controls (a never-shown profile, a post-cutoff swipe, and an outcome the swipe cannot affect); and placebo timestamps.
- Slice by baseline activity, swipe volume, gender/side of market, position, match count, and cold-start status.
- Compare v1 removal, v2 CATE, last-touch, equal split, and recency-decay labels under the same downstream ranker.

### Online metrics and holdout design

- Primary metric: binary N7 retention and cumulative active days over the same population.
- Secondary metrics: time to next active day, sessions per user, meaningful matches, replied conversations, and successful-conversation rate.
- Guardrails: reports/blocks, unmatches, candidate-side retention, exposure concentration, latency, and overall swipe/match volume.
- Randomize at a level that limits reciprocal spillovers: stable bipartite clusters or user-market cells, not individual impressions alone.
- Maintain an always-on deterministic holdout for candidate exposure or rank perturbation. Log assignment, exposure, swipe, like, match, message, and day-level activity separately.
- Use a longer frozen holdout to detect adaptation and novelty effects; do not recycle the calibration cohort into model training.

### Calibration loop

1. Estimate granular credits from production logs.
2. Aggregate credits to experiment cells and compare them with observed N7 lift.
3. Fit a monotone calibration layer by activity cohort, event type, position, and lookback.
4. Reject or mark unresolved cells with poor overlap or unstable confidence intervals (the certify / reject / unresolved partition follows `"Privacy-Robust Incrementality Measurement for Advertising Systems under Signal Loss, arXiv 2026"`).
5. Retrain the downstream ranking model on calibrated credits.
6. Re-run the randomized holdout and monitor whether predicted aggregate lift, realized N7 lift, and two-sided guardrails remain aligned.

## Next Steps

- [ ] Implement v1 removal-effect labels with user-prevalence normalization and typed event lineage.
- [ ] Design a reciprocal-market-safe randomized exposure holdout.
- [ ] Establish last-touch, equal-split, recency-decay, and removal-effect baselines under one ranker.
- [ ] Add causal propensity heads and the discrete-time survival target only after v1 calibration succeeds.
- [ ] Gate v3 on empirical evidence that observed-covariate adjustment remains biased.

## Search Scope

- Survey period: no limit for Q2; January 2025 through September 2026 for Q1.
- Total cards: 50.
- Major venues: ICLR, KDD, WWW, RecSys, CIKM, AAAI, Review of Economic Studies, and industry engineering publications.
- Search focus: causal attribution, retention-aware recommendation, per-interaction credit, uplift, long-term value, reciprocal matching, notifications, surrogate outcomes, and privacy-era incrementality.

FILES READ: 17 of 17
