
Date: 2026-09-18

# Attribution-based Retention — Executive Summary

## Key Questions

- **Q1. What is the latest attribution-based approach in the industry? Scope: production or industry-authored attribution systems dated 2025-01 to 2026-09, plus the newest work from the teams and authors behind the classic papers in the parent survey.**
- **Q2. Has anyone in industry published attribution-based retention — that is, attributing user retention, engagement, or days-active to individual in-app interactions (recommendations, matches, messages, notifications, swipes)? No date limit for Q2. Academic work counts if it names a production dataset or deployment.**

## Main Findings

### Direct answer to Q1

The latest carded industry work divides into four approaches. Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 offers the strongest causal per-touch mechanism: front-door identification, proxy mediation, IPW, and deletion scores. Wu et al., *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*, CIKM 2026 uses LLM semantic reasoning to select conversion touchpoints but lacks causal calibration. Bhat et al., *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM*, arXiv 2026 replaces user tracking with aggregate MMM-anchored campaign attribution. Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 remains the best production hybrid: sequence-wide fractional credit calibrated against holdout experiments and MMM. RecSys 2026 adds Zhang and Gao, *A Causal Transformer Multi-Touch Attribution with Dual Debiasing and Explainable Visualization for Advertising Recommendation* (short paper, G41 stub): the program lists conversion-credit MTA with dual debiasing, but there is no public PDF, so it does not displace ALM-MTA on mechanism. For dating N7, the best direction is therefore ALM-MTA-style removal scoring plus LinkedIn-style experimental calibration—not LLM selection alone, and not an unread advertising transformer.

### Direct answer to Q2

No card meets the strict TRUE standard: identified causal/MTA decomposition of retention or days-active to individual in-app interactions. Discovery logged that Match Group, Tinder, Hinge, and Bumble published no swipe-to-days-active attribution (D3 §F). Related notebooks `unified-ltv-ranking-dating` and `two-sided-market-balancing-dating` over-classified GFN4Retention and MRet as TRUE; this run's cards classify both NOT (policy/LTR, no reusable retention-credit table). The RecSys 2026 addendum is uniformly NOT: MODE is reciprocal match ranking on CyberAgent dating logs, not N7 credit; PROMISE process rewards are SID-token scores; STEPS optimizes Douyin User Active Days as a policy, not a credit table. The closest PARTIAL hits remain Jiang et al., *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*, AAAI 2026 (save→revisit surrogate), Ding et al., *Interpretable User Retention Modeling in Recommendation*, RecSys 2023, and Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026 (per-item retention scores without identified causal MTA). Wang et al., *Future Impact Decomposition in Request-level Recommendations*, KDD 2024 is PARTIAL under the D3 rubric because it publishes item-wise delayed-value scores, even though those scores sit inside RL rather than a causal MTA table. Netflix, *Incrementality-Focused Messaging Measurement*, industry blog 2023 is PARTIAL for randomized message-level downstream viewing, but its card is a failed-ingestion stub. RLUR, GFN4Retention, AURO, SEC, MRet, bandits, ranking methods, and all RecSys 2026 extracted cards are NOT attribution unless they emit reusable per-interaction retention credit; the cards show that they do not.

| G | Classification | Paper and reason |
|---|---|---|
| G1 | NOT | Wu et al., *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*, CIKM 2026 — per-touch purchase conversion, not retention. |
| G2 | NOT | Bhat et al., *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM*, arXiv 2026 — daily campaign credit, not user interactions. |
| G3 | NOT | Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 — marketing conversion credit, not retention. |
| G4 | PARTIAL | Wang et al., *Future Impact Decomposition in Request-level Recommendations*, KDD 2024 — item-wise delayed-value scores exist, but they are RL advantages without identified causal MTA. |
| G5 | PARTIAL | Jiang et al., *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*, AAAI 2026 — item save/revisit surrogate without causal MTA. |
| G6 | NOT | Kishimoto et al., *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching*, ICLR 2026 — retention-aware LTR, no observed-touch decomposition. |
| G7 | NOT | Cai et al., *Reinforcing User Retention in a Billion Scale Short Video Recommender System*, WWW 2023 — request-level RL policy. |
| G8 | NOT | Liu et al., *Modeling User Retention through Generative Flow Networks*, KDD 2024 — flow policy, not reusable item credit; this corrects related-notebook over-classification. |
| G9 | NOT | Xue et al., *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems*, WWW 2025 — continuous-action policy. |
| G10 | NOT | Lin et al., *Stratified Expert Cloning for Retention-Aware Recommendation at Scale*, CIKM 2025 — imitation policy that bypasses credit assignment. |
| G11 | NOT | Ma et al., *Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling*, arXiv 2026 — user-level prediction for bidding. |
| G12 | NOT | Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 — TRUE-style mechanism, wrong outcome: upload. |
| G13 | PARTIAL | Ding et al., *Interpretable User Retention Modeling in Recommendation*, RecSys 2023 — item retention scores, no causal identification. |
| G14 | PARTIAL | Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026 — item retention scores, no causal identification. |
| G15 | NOT | Zhang et al., *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking*, KDD 2025 — evaluation device for booking. |
| G16 | NOT | Zhang et al., *Impatient Bandits: Optimizing for the Long-Term Without Delay*, JMLR 2026 — item-arm posterior used by a bandit, not historical MTA. |
| G17 | NOT | Zhao et al., *User Retention-oriented Recommendation with Decision Transformer*, WWW 2023 — offline RL policy. |
| G18 | NOT | Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026 — incremental stream targeting, not retention-path attribution. |
| G19 | NOT | Wu et al., *Learned Ranking Function: From Short-term Behavior Predictions to Long-term User Satisfaction*, RecSys 2024 — candidate ranking score. |
| G20 | NOT | Lada et al., *Long-run User Value Optimization in Recommender Systems through Content Creation Modeling*, arXiv 2022 — producer-level treatment effect. |
| G21 | NOT | Wang et al., *Surrogate for Long-Term User Experience in Recommender Systems*, KDD 2022 — RL reward surrogate. |
| G22 | NOT | Authors not reported in the card, *Sequential Recommendation for Optimizing Both Immediate Feedback and Long-term Retention*, arXiv 2024 — Decision Transformer policy. |
| G23 | NOT | Wang et al., *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning*, arXiv 2026 — predictive reward heads for ranking. |
| G24 | NOT | Zhang et al., *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search*, arXiv 2026 — proxy-policy optimization for GMV. |
| G25 | NOT | Yancey and Settles, *A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications*, KDD 2020 — notification-arm bandit. |
| G26 | PARTIAL | Netflix, *Incrementality-Focused Messaging Measurement*, industry blog 2023 — causal message touchpoint, downstream viewing outcome; stub evidence. |
| G27 | NOT | Netflix, *A Human-Augmenting Agentic Workflow for Causal Inference*, Netflix Technology Blog 2026 — treatment-level tooling, not credit assignment. |
| G28 | NOT | Guo et al., *PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations*, RecSys 2026 — SID-path process rewards, not historical retention credit. |
| G29 | NOT | Kozaki et al., *Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders*, RecSys 2026 — last-item diagnosis, no credit table. |
| G30 | NOT | Zhang et al., *A Self-Triggered Agentic Push Recommendation System*, RecSys 2026 — Douyin UAD policy, not per-touch credit. |
| G31 | NOT | Wang et al., *UniShare: A Unified Framework for Joint Video and Receiver Recommendation in Social Sharing*, RecSys 2026 — share/receiver ranking. |
| G32 | NOT | Tomita, *MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets*, RecSys 2026 — expected-match lists on dating logs, not N7 MTA. |
| G33 | NOT | Islam, Vasilaky, and Zheleva, *A Control Function Framework for Mitigating Position Bias in Learning to Rank Systems*, RecSys 2026 — click ULTR. |
| G34 | NOT | Min et al., *Towards Reliable Social A/B Testing: Spillover-Contained Clustering with Robust Post-Experiment Analysis*, RecSys 2026 — cluster LT-7 ATE, not per-touch credit. |
| G35 | NOT | Parajuli, Vaez Barenji, and Ekstrand, *On the Convergent Validity of Offline Evaluation Designs for Recommender Systems*, RecSys 2026 — evaluation validity. |
| G36 | NOT | Ding et al., *Zero-Observation User Reactivation with Gap-Driven Dimensional Gating*, RecSys 2026 — next-item reactivation. |
| G37 | NOT | Gu et al., *Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals with Segment-Aware Targeting*, RecSys 2026 — Twitch multi-task ranker. |
| G38 | NOT | Knyazev et al., *Generalized position-based model: Rethinking position weights in ranking off-policy evaluation*, RecSys 2026 — OPE position weights; landing-page ingest. |
| G39 | NOT | Kalagarla et al., *TSMOO: Solving multi-objective experimentation with constrained Thompson sampling*, RecSys 2026 — multi-objective experiment allocation. |
| G40 | NOT | Xia et al., *Alignment + Accuracy: The Cascade Reward Representation for Preranking*, RecSys 2026 — prerank alignment, save-rate policy. |
| G41 | NOT | Zhang and Gao, *A Causal Transformer Multi-Touch Attribution with Dual Debiasing and Explainable Visualization for Advertising Recommendation*, RecSys 2026 — paywalled conversion-MTA stub. |

## Most Fundamental Methods

1. **Front-door removal MTA (score 9).** Direct touch-level removal labels plus explicit confounding machinery. Proposed in Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026.
2. **Experiment-calibrated Transformer DDA (score 8).** Fractional sequence credit anchored to experimental evidence. Proposed in Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025.
3. **Save–revisit surrogate attribution (score 7).** Closest deployed action-to-return linkage. Proposed in Jiang et al., *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*, AAAI 2026.
4. **BCMIL item-retention scoring (score 7).** Directly converts a delayed user label into item scores. Proposed in Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026.
5. **Always-on holdback plus Deep Twin targeting (score 7).** Separates recommended and organic response to expose always-takers. Proposed in Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026.

## Approach Comparison

| Approach | Pros | Cons | Related paper |
|---|---|---|---|
| Front-door removal MTA | Explicit per-touch score; models unobserved confounding | Strong mediator assumptions; no N7 evidence | Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 |
| Calibrated deep DDA | Scalable fractional labels; experiment anchor | Attention is not causal touch effect | Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 |
| Item-retention MIL | Directly serves per-item labels | Selection bias remains | Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026 |
| Save–revisit surrogate | Concrete action-to-return chain | Covers only one pathway | Jiang et al., *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems*, AAAI 2026 |
| Holdback incremental targeting | Strong defense against organic affinity | Expensive; mismatched windows complicate CATE | Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026 |
| RL/LTR retention optimization | Can improve platform outcomes directly | Does not generate auditable attribution labels | Cai et al., *Reinforcing User Retention in a Billion Scale Short Video Recommender System*, WWW 2023 |

## Recommendations

### v1 — Interpretable removal-score attributor

- **Sources and estimator.** Keep the removal architecture from Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 and the item-scoring interface from Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026. For swipe \(j\), emit  
  \[
  c^{(1)}_{u,d,j}=\hat p(Y_{u,d}=1\mid X,T)-\hat p(Y_{u,d}=1\mid X,T\setminus\{j\}).
  \]
  Treat the match and conversation spawned by \(j\) as timestamped downstream mediator tokens linked to that swipe; also report direct-only and total-path deletions. Call \(c^{(1)}\) a **removal score**, not incremental lift.
- **Bias, recurrence, validation, cost, risk.** Fit exposure propensities and overlap diagnostics, then apply IPW as adapted from Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026. Build one row per user/reference-day with \(Y_{u,d}=1\) when active on day \(d+7\), use time-based splits, and cluster uncertainty by user. Validate rank-ordered score buckets against randomized candidate-eligibility or deck-level holdbacks, following the holdback logic of Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026. **Cost: medium. Main risk:** deletion sensitivity remains observational and may reward markers of engagement rather than causes.

### v2 — Calibrated deep DDA with a discrete-time survival head

- **Sources and estimator.** Keep the planned survival head, but calibrate it using Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025. For swipe \(j\), estimate  
  \[
  c^{(2)}_{u,d,j}=\operatorname{Cal}_{z}\!\left[\hat P(N7=1\mid X,T)-\hat P(N7=1\mid X,T\setminus\{j\})\right],
  \]
  where \(\hat P(N7=1)=1-\prod_{k=1}^{7}(1-\hat h_k)\), and \(\operatorname{Cal}_{z}\) is learned within randomized exposure strata. Encode swipe, match, and conversation as typed tokens; linked match/conversation tokens remain in the total-path deletion for their originating swipe.
- **Bias, recurrence, validation, cost, risk.** Use separate recommended and organic-response heads inspired by Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026, and calibrate aggregate predicted credit to experimental N7 lift as in Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025. Train hazards on rolling user-days so repeated binary outcomes are first-class observations rather than duplicate conversions. **Cost: high. Main risk:** good aggregate calibration can coexist with wrong individual-touch allocation.

### v3 — Experiment-anchored causal per-swipe labels

- **Sources and estimator.** Add a third phase based on persistent randomized eligibility/holdback cells, adapting Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026 and the message-withholding design described—but not quantitatively verified—in Netflix, *Incrementality-Focused Messaging Measurement*, industry blog 2023. For an eligible swipe opportunity \(j\), compute the doubly robust pseudo-outcome  
  \[
  c^{(3)}_j=\hat m_1(X)-\hat m_0(X)+
  \frac{A_j(Y-\hat m_1(X))}{e_j(X)}
  -\frac{(1-A_j)(Y-\hat m_0(X))}{1-e_j(X)}.
  \]
  \(A_j\) records whether the profile was shown; match and conversation are mediators used for pathway analysis, not pre-treatment controls.
- **Bias, recurrence, validation, cost, risk.** Randomized \(e_j\) supplies the selection-bias defense; user-day N7 remains the outcome, with repeated observations clustered by user. Validate calibration, AUUC/Qini, and ranking lift against untouched experimental cells, drawing on the propensity-stratified evaluation of Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026. **Cost: high. Main risk:** interference and two-sided spillovers violate single-user treatment assumptions.

### Against the 2026-06-13 plan

- **Keep binary N7.** The closest per-item retention templates still use a short binary horizon (Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026: next-3-day retention). The longest alternative in these cards is a 60-day progressive active-day trace (Zhang et al., *Impatient Bandits: Optimizing for the Long-Term Without Delay*, JMLR 2026), which is a bandit arm posterior rather than per-touch credit. RecSys 2026 does not change this: Zhang et al., *A Self-Triggered Agentic Push Recommendation System*, RecSys 2026 optimize User Active Days as a policy, and Min et al., *Towards Reliable Social A/B Testing: Spillover-Contained Clustering with Robust Post-Experiment Analysis*, RecSys 2026 report LT-7 as a cluster ATE. Neither estimates per-touch credit on binary N7 itself.
- **Keep v1, but rename and constrain it.** Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 supports removal-effect labels, but no card validates that contrast on binary N7. Therefore v1 scores must not be marketed as incremental.
- **Keep v2, but make calibration mandatory.** Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 shows why sequence credit needs experimental or macro calibration; Ding et al., *Rethinking User Retention Modeling in Recommendation*, TOIS 2026 supports the per-item retention head.
- **Change the plan by adding v3.** Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026 shows that organic affinity can dominate naïve recommendation credit. Persistent randomized exposure cells are necessary before claiming per-swipe incremental N7. Min et al., *Towards Reliable Social A/B Testing: Spillover-Contained Clustering with Robust Post-Experiment Analysis*, RecSys 2026 further shows user-level A/B understates LT-7 when social spillover is uncontained (CBR +0.133% vs UBR +0.049%); dating match/conversation graphs need the same interference defense.

### Why not keep last-touch

- Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025 documents that last-touch overvalues bottom-of-funnel events and ignores earlier journey stages—the same failure produced when the latest swipe receives all N7 credit.
- Ding et al., *Interpretable User Retention Modeling in Recommendation*, RecSys 2023 finds sparse influential “aha items” across interaction histories, which contradicts the assumption that only the final item matters.
- Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026 shows that high-affinity users may act organically; last-touch systematically credits exposures received by these always-takers.
- Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026 demonstrates a feasible alternative that distributes sequence credit through per-touch deletion scores rather than assigning 100% to the last event.
- Kozaki et al., *Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders*, RecSys 2026 shows residual connections collapsing contextual mixing from 0.72–0.96 to 0.11–0.39, a structural reason sequential models copy last-touch.

### Evaluation without per-interaction ground truth

- **Randomized anchors:** maintain candidate-eligibility, deck, or notification holdbacks and compare predicted credit sums with observed N7 lift, following Vlontzos et al., *Incremental Recommendation via Causal Models*, arXiv 2026.
- **Propensity-stratified ranking tests:** measure whether high-credit buckets show monotonically higher experimental lift and report AUUC/Qini, following Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026.
- **Aggregate calibration:** require predicted credit totals by interaction type and cohort to match randomized lift within uncertainty, following Bencina et al., *Buyer Journey Insights with Data-Driven Attribution*, LinkedIn Engineering 2025.
- **Placebo and deletion tests:** future touches must receive zero credit, pre-period activity must not move, and removing high-score touches must reduce predicted N7 more than removing matched low-score touches, using the deletion structure of Liu et al., *ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization*, arXiv 2026.
- **Policy validation:** train the downstream ranker on attribution labels and require improvement in randomized N7—not merely offline AUC—while checking match, conversation, and ecosystem-side effects, motivated by Kishimoto et al., *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching*, ICLR 2026.

## Next Steps

- [ ] Instrument swipe / match / conversation as typed touchpoints with a shared user-day N7 label.
- [ ] Ship v1 removal scores with propensity diagnostics; do not train production rankers on them until holdback buckets move N7.
- [ ] Add persistent candidate-eligibility holdbacks before claiming incremental per-swipe N7.
- [ ] Re-ingest Zhang and Gao RecSys 2026 Causal Transformer MTA when a PDF appears; do not treat the program blurb as a mechanism.
- [ ] For two-sided experiments, prefer spillover-contained cluster randomization over naïve user A/B.

## Search Scope

- Survey period: Q1 industry systems 2025-01 to 2026-09; Q2 no date limit
- Total papers this run: 41 cards (25 original NLM + 2 Netflix stubs + 13 RecSys 2026 NLM extracts + 1 paywall stub). G23 counted in the original 25; RecSys 2026 listing noted, not re-extracted.
- Major venues: KDD, WWW, CIKM, RecSys 2026 addendum, ICLR, AAAI, TOIS, JMLR, LinkedIn Engineering, Amazon Science landing pages
- Search keywords: multi-touch attribution, data-driven attribution, retention attribution, incremental value of a recommendation/notification/swipe, last-touch vs removal-effect vs experiment-calibrated DDA; RecSys 2026 official program screen
