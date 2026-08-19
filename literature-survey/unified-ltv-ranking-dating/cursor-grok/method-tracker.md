Date: 2026-08-16 (last updated 2026-08-17 continuation)
Topic: unified retention/revenue ranking for a dating recommender

# unified-ltv-ranking-dating — Methodology Fundamentality Tracking

Workplace: `cursor-grok`. Corpus: **120 cards**. **Baseline-mention and derived-variant counts are estimated from this corpus only**, not global citation counts. A “baseline mention” is counted when another card in this workplace used the method as an experimental comparison (not merely a Related Work citation). A “derived variant” is counted when a later card in this corpus is an explicit extension, replacement, or named descendant.

Composite score = (baseline mention × 3) + (derived variant × 2) + simplicity + (consistency × 2).

Simplicity: 5 = 1–2 core components, 4 = 3, 3 = 4, 2 = 5, 1 = 6+. Consistency: higher when independent cards report the same directional win (not a numeric stddev, which this corpus does not support).

## Methodology Table

| Method Name | Proposal Paper (Year) | Baseline Mention Count | Derived Variant Count | Independent Measured Performance (Dataset: metric \| source) | Component Count | Simplicity Score (1-5) | Performance Consistency Score (1-5) | Fundamentality Composite Score |
|---------|----------------|-------------------|----------------|--------------------------------------|-------------|-----------------|----------------------|----------------|
| ESMM (entire-space CTR×CVR) | Ma et al., Entire Space Multi-Task Model, SIGIR 2018 (Alibaba) | 6 | 4 | Taobao public: CVR AUC 68.56 vs BASE 66.00; CTCVR AUC 65.32 vs 62.07 (ESMM card). Later cards beat ESMM on industrial CVR/CTCVR (ESM2, ESCM2, ESDF, DEFUSE, HM3). | 3 | 4 | 5 | 36 |
| Surrogate Index | Athey, Chetty, Imbens, Kang, The Surrogate Index, NBER 2019 (rev. 2024) | 5 | 4 | GAIN job training: 6-quarter index 0.061 vs naive 0.117 vs 36-quarter benchmark 0.064 (Surrogate Index card). Netflix 14d auto-surrogate ~95% decision-consistent with 63d (Zhang et al.). | 3 | 4 | 4 | 31 |
| Delayed Feedback Model (DFM) | Chapelle, Modeling Delayed Feedback in Display Advertising, KDD 2014 (Criteo) | 4 | 4 | Criteo-style NLL 0.3960 vs Naive 0.4076; Naive underpredicts conversions by 21% (DFM card). ESDF/DEFUSE/DEFER report further AUC lifts over DFM/ES-DFM. | 3 | 4 | 4 | 29 |
| MMoE | Zhao, Hong, Wei, et al., Recommending What Video to Watch Next, RecSys 2019 (YouTube/Google) | 4 | 2 | Live YouTube: MMoE 4-expert +0.20% engagement / +1.22% satisfaction vs shared-bottom; 8-expert +0.45% / +3.07% (MMoE card). Reused as MTL backbone (Twitch delayed-signal ranking; Pinterest Save/Revisit/Retain). | 3 | 4 | 4 | 26 |
| ZILN | Wang, Liu, et al., A Deep Probabilistic Model for Customer Lifetime Value Prediction, 2019 (Google) | 4 | 2 | DNN-ZILN vs MSE: +23.9% Spearman (linear) / +48.0% (DNN); KDD Cup profit $15,498 vs winner $14,712 (ZILN card). Kuaishou ODMN beats ZILN on ltv_30 AMBE 0.0423 vs 0.1336. | 2 | 5 | 4 | 25 |
| RLUR (retention actor–critic) | Cai, Liu, Wang, et al., Reinforcing User Retention in a Billion Scale Short Video Recommender System, WWW 2023 (Kuaishou) | 3 | 2 | Online ≈150d vs CEM: +0.450% app open frequency, +0.2% DAU, +0.053% D1, +0.063% D7 (RLUR card). AURO and GFN4Retention report beating RLUR offline/live; exact GFN percentages not specified in that card. | 5 | 2 | 4 | 21 |
| Top-K Off-Policy REINFORCE | Chen, Beutel, Covington, et al., Top-K Off-Policy Correction for a REINFORCE Recommender System, WSDM 2019 (Google/YouTube) | 2 | 2 | Top-K (K=16) avoids −0.66% ViewTime drop of standard off-policy; K=8 vs K=16 +0.15% ViewTime (Top-K card). URL (WSDM 2021) bolts auxiliary click/dwell heads: +0.12% live enjoyment. | 3 | 4 | 3 | 20 |
| SlateQ | Ie, Jain, Wang, et al., SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets, IJCAI 2019 (Google) | 2 | 1 | YouTube live vs myopic: ~+0.5% day 1 to >+1.0% by day 20 aggregated engagement (SlateQ card). FID uses SlateQ as offline baseline and beats it on KuaiRand. | 4 | 3 | 4 | 19 |
| BatchRL-MTF | Zhang, Liu, Dai, et al., Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction, KDD 2022 (Tencent) | 1 | 4 | Production: +2.550% app dwell time, +9.651% positive-interaction rate (BatchRL-MTF card). UnifiedRL +4.64% consumption vs ES; EnhancedRL +3.84% vs UnifiedRL; xMTF +0.833% daily watch time vs UNEX-RL. | 4 | 3 | 4 | 20 |
| AITM | Xi, Chen, Yan, et al., Modeling the Sequential Dependence among Audience Multi-step Conversions, KDD 2021 (Meituan) | 1 | 1 | Offline approval AUC 0.8534 vs PLE 0.8518; online vs MLP +25.0% approval CR, +42.11% activation CR (AITM card). Airbnb Journey Ranker is a related chain-rule funnel, not a named AITM fork. | 4 | 3 | 3 | 14 |
| ESCM² (IPS/DR entire-space) | Wang, Chang, Liu, et al., ESCM²: Entire Space Counterfactual Multi-Task Model, SIGIR 2022 (Ant Group) | 1 | 0 | Industrial CVR AUC ESCM²-IPS 0.7730 vs ESMM 0.7547; online +2.84% orders, +10.85% premium vs ESMM (ESCM2 card). | 4 | 3 | 4 | 14 |
| Impatient Bandits | McDonald, Maystre, Lalmas, Russo, Ciosek, Impatient Bandits, KDD 2023 (Spotify) | 1 | 0 | 50% of prior variance explained by 8 days of traces; 95% by one month; progressive bandit beats Delayed and Day-two proxy in 180-round simulation (Impatient Bandits card). No online A/B in source. | 3 | 4 | 3 | 13 |
| Instagram / LinkedIn value-model fusion | Vorotilov & Shugaepov, Scaling the Instagram Explore Recommendations System, Meta Eng Blog 2023; Borisyuk et al., LiRank, KDD 2024 | 1 | 1 | Instagram: no numeric lifts in blog. LiRank: +0.5% Feed member sessions; +1.76% qualified job applications; +4.3% Ads CTR; Thompson sampling +0.06% professionals DAU (LiRank card). Pinterest PRL-PUTS is a learned-weight variant of the same VM idea. | 3 | 4 | 3 | 13 |
| GFN4Retention | Liu, Liu, Yang, et al., Modeling User Retention through Generative Flow Networks, KDD 2024 (Kuaishou) | 0 | 0 | Card states superiority over CEM, DIN, TD3, SAC, RLUR offline and live; **exact percentages not specified in source** (NLM Q2 failed). | 5 | 2 | 2 | 6 |
| Future Impact Decomposition (ItemA2C / FID) | Wang, Liu, Wang, et al., Future Impact Decomposition in Request-level Recommendations, KDD 2024 (Kuaishou) | 0 | 0 | Online vs request-level A2C: watch time +0.129%, like +1.103%; DAU +0.028%, retention +0.016% (FID card). | 4 | 3 | 3 | 9 |
| TU / Fair Reciprocal (NSW) | Tomita et al., Fast and Examination-agnostic Reciprocal Recommendation, RecSys 2023; Tomita & Yokoyama, Fair Reciprocal Recommendation in Matching Markets, RecSys 2024 (CyberAgent) | 1 | 1 | n=200 synthetic: TU 332.91 expected matches vs Naive 219.56; real NSW 90.39 matches vs SW 111.37 with male envy 31 vs 434 (TU / NSW cards). CRRS is a related causal-reciprocal formulation, not a TU fork. | 3 | 4 | 4 | 17 |
| Counterfactual Reciprocal (IPS/DR matching) | Sony Group, Counterfactual Reciprocal Recommender Systems for User-to-User Matching, arXiv 2025 | 0 | 0 | NDCG@10 +2.7% Synthetic vs LFRR; Coverage@10 +51% Synthetic (Counterfactual Reciprocal card). | 3 | 4 | 3 | 10 |
| LOPE (long-term OPE) | Saito, Abdollahpouri, Anderton, Carterette, Lalmas, Long-term Off-Policy Evaluation and Learning, WWW 2024 (Spotify) | 0 | 0 | Synthetic: 36% MSE reduction vs DR at n=200; 71% vs LCI at n=1000. Spotify 3-week tests: 9.2–15.0% MSE reduction vs DR (LOPE card). | 3 | 4 | 4 | 12 |
| Proxy-metric selection (Sharpe / Pareto) | Tripuraneni et al., Choosing a Proxy Metric from Past Experiments, KDD 2024 (Google); Zito et al., Pareto Optimal Proxy Metrics, arXiv 2023 (Google) | 1 | 1 | Choosing Proxy: composite proxy quality 0.302 vs best auxiliary 0.258. Pareto: 8.5× relative sensitivity vs short-term north star; recall 72% vs 40% (those cards). | 3 | 4 | 4 | 17 |
| TSCAC | Cai et al., Two-Stage Constrained Actor-Critic for Short Video Recommendation, WWW 2023 (Kuaishou) | 1 | 0 | Online vs LTR: WatchTime +0.379%, Share +3.376%; Comment −0.619% (TSCAC card). xMTF uses TSCAC-2 as best formula baseline offline. | 4 | 3 | 3 | 12 |
| xMTF | Cao, Zhang, Chen, Zhan, Wang, xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion, WWW 2025 (Kuaishou) | 0 | 0 | KuaiRand watch time 1279.7 vs TSCAC-2 1194.7; online +0.833% daily watch time vs UNEX-RL (xMTF card). | 4 | 3 | 3 | 9 |
| OneRec / generative reward ranker | Kuaishou OneRec papers 2025; Zhai et al., HSTU, ICML 2024 (Meta); Netflix GenRec 2026 | 0 | 2 | OneRec unify: +1.68% Total Watch Time, +6.56% Average View Duration. GenRec: +0.115% short-term engagement, +0.006% long-term core metric (those cards). | 6 | 1 | 3 | 9 |

## How counts were estimated

- **ESMM (6 / 4):** experimental baseline in Entire Space Multi-Task Modeling via Post-Click Behavior Decomposition (SIGIR 2020), ESCM² (SIGIR 2022), Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction (AAAI 2021), Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction (WWW 2022), HM³ (SIGIR 2021), and AITM (KDD 2021, via PLE/ESMM-family MTL). Derived: ESM², ESCM², ESDF, HM³.
- **Surrogate Index (5 / 4):** experimental or decision-layer use in Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix (2023), Long-term Off-Policy Evaluation and Learning (WWW 2024; LCI baseline), Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index (NeurIPS 2021), PROXIMA (2026), Evaluating for the Long Term: Learnings from Industry (2026). Derived: Netflix auto-surrogate, DASI, LOPE surrogate+action split, Impatient Bandits progressive filter (methodologically downstream).
- **DFM (4 / 4):** baseline in ESDF, DEFUSE, Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback (SIGIR 2021), Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction (RecSys 2019). Derived: ESDF, DEFUSE, CBDF, **DEFER** (KDD 2021 real-negative duplication; previously unverified seed).
- **MMoE (4 / 2):** backbone or baseline in Multi-Objective Ranking for Live-Streaming (Twitch/Prime Video), Save, Revisit, Retain (Pinterest), MoSE (KDD 2020), LiRank grouping-strategy MTL. Derived: MoSE, Pinterest RP&RV head on MMoE.
- **ZILN (4 / 2):** baseline in Billion-user Customer Lifetime Value Prediction (CIKM 2022), Rankability-enhanced Revenue Uplift Modeling (RERUM), CC-OR-Net, Mini-Game Lifetime Value Prediction in WeChat (GRePO-LTV). Derived: ODMN (Kuaishou), RERUM ZILN response heads.
- **RLUR (3 / 3):** baseline in GFN4Retention, AURO, and (as cited industrial retention RL) xMTF / OCARM. Derived: AURO, GFN4Retention, **SEC** (stratified expert cloning of high-retention trajectories).
- **BatchRL-MTF (1 / 4):** experimental baseline in xMTF. Derived: xMTF (formula-free MFC), PRL-PUTS (one-step utility-weight bandit), **UnifiedRL / IntegratedRL-MTF**, **EnhancedRL**.

Low baseline counts for GFN4Retention, FID, OneRec, and xMTF mean they are **new industrial methods in this corpus**, not that they are weak. Do not treat a composite of 6–9 as a quality ranking.

## Top Method Analysis (Phase 3.5)

### Rank 1: ESMM (Composite Score: 36)

- Why fundamental: simplest entire-space identity for a sparse downstream conversion trained over all impressions; every later funnel paper in D5 starts from it.
- Representative paper: Ma, Zhao, Huang, Wang, Hu, Zhu, Gai, Entire Space Multi-Task Model: An Effective Approach for Estimating Post-Click Conversion Rate, SIGIR 2018.
- Which papers used this method as a baseline: ESM², ESCM², ESDF, DEFUSE, HM³, AITM (MTL family).
- Known variants: ESM² (post-click decomposition), ESCM² (IPS/DR), ESDF (delay slots), HM³ (micro/macro graph).
- Independent measured performance range: CVR AUC lifts of about +2 to +4 points over BASE/ESMM across Alibaba/Ant industrial sets (N ≈ 5 papers).

### Rank 2: Surrogate Index (Composite Score: 31)

- Why fundamental: the statistical object that lets a 7–14 day experiment stand in for a 30–90 day retention/revenue north star; D3 is almost entirely descendants of this paper.
- Representative paper: Athey, Chetty, Imbens, Kang, The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects More Rapidly and Precisely, NBER Working Paper 26463, 2019 (rev. 2024).
- Which papers used this method as a baseline: Netflix 200-test evaluation, LOPE (LCI), DASI, PROXIMA, industry workshop synthesis.
- Known variants: linear auto-surrogate (Netflix), dynamically adjusted index (Microsoft), LOPE surrogate+action decomposition, Impatient Bandits progressive traces.
- Independent measured performance range: GAIN employment ATE recovered at 6 quarters (0.061 vs benchmark 0.064); Netflix 14-vs-63 day decision consistency ~95% (precision 79%, recall 65%).

### Rank 3: Delayed Feedback Model (Composite Score: 27)

- Why fundamental: first widely reused parametric delay model for conversions that arrive after training ingest; dating subscription labels have the same right-censoring shape.
- Representative paper: Chapelle, Modeling Delayed Feedback in Display Advertising, KDD 2014.
- Which papers used this method as a baseline: ESDF, DEFUSE, CBDF, Twitter RecSys 2019 delayed-feedback study.
- Known variants: ESDF, DEFUSE / Bi-DEFUSE, fake-negative weighted loss (Twitter).
- Independent measured performance range: ~3% NLL vs Naive (DFM); later entire-space delay models report +2–7% relative AUC vs ESMM/ES-DFM.

### Rank 4: MMoE (Composite Score: 26)

- Why fundamental: default industrial pattern for keeping many short-horizon heads in one ranker; dating like/match/conversation heads are this pattern.
- Representative paper: Zhao, Hong, Wei, et al., Recommending What Video to Watch Next: A Multitask Ranking System, RecSys 2019 (YouTube).
- Which papers used this method as a baseline / backbone: Twitch delayed-signal ranking, Pinterest Save/Revisit/Retain, MoSE, LiRank.
- Known variants: MoSE (sequential experts), grouping-strategy MTL in LiRank.
- Independent measured performance range: YouTube live +0.20–0.45% engagement; Pinterest revisitation head online +0.10% active users / +0.39% time spent.

### Rank 5: ZILN (Composite Score: 25)

- Why fundamental: default loss for zero-inflated, heavy-tailed spend; dating subscription + a-la-carte revenue is this distribution.
- Representative paper: Wang, Liu, et al., A Deep Probabilistic Model for Customer Lifetime Value Prediction, 2019 (Google).
- Which papers used this method as a baseline: Kuaishou billion-user LTV, RERUM, CC-OR-Net, GRePO-LTV.
- Known variants: ODMN multi-horizon LTV (Kuaishou), ZILN heads inside RERUM uplift ranking.
- Independent measured performance range: large Spearman/Gini lifts vs MSE (ZILN card); ODMN then beats ZILN on ordered 30/90/180/365 horizons; WeChat GRePO-LTV online LTV/GMV +8.4%.

### Project-critical methods with low composite (not in global top 5)

These are the migration templates for this dating ranker. Their composites are low because the corpus contains few later papers that re-run them as baselines.

| Method | Composite | Why it still leads the architecture ranking |
|--------|-----------|-----------------------------------------------|
| BatchRL-MTF / xMTF | 16 / 9 | Only production pattern that **keeps MTL heads and learns fusion toward a long-term session reward**. |
| RLUR | 21 | Only production pattern that puts **delayed return time** on the ranking policy with D1/D7 online reads. |
| SlateQ / FID | 19 / 9 | Only tractable **item-level** credit assignment for slate/request MDPs. |
| TU / NSW reciprocal | 17 | Only production-adjacent pattern that puts **congestion and envy** into the score, not a post-hoc diversity tweak. |
| Instagram Explore value model / LiRank | 13 | Current-state cousin of the team’s CTR/CVR blend; documented fusion + distillation + (LiRank) long-dwell head. |

## Implications for scoring this survey

Do not pick a unified dating architecture by composite alone. ESMM, MMoE, DFM, and ZILN are the **label and head primitives**. BatchRL-MTF, RLUR, SlateQ/FID, and TU/NSW are the **system templates**. The Surrogate Index family is the **evaluation layer**, not a ranker.
