Date: 2026-08-17
Topic: unified LTV ranking for dating
Paper count: 120 (D1=28, D2=16, D3=13, D4=12, D5=7, D6=7, D7=10, D8=22, D9=5). Industry-heavy. Original 90-card synthesis 2026-08-16; 30 continuation cards 2026-08-17.

Workplace: `cursor-grok/`. Cards: `./read-papers/`. Shared brief: `../README.md`.

# Unified retention/revenue ranking for a dating recommender — Literature Review

## Field summary

Industry recommenders almost never train a swipe ranker on raw 30-day retention or weeks-scale revenue. They keep a multi-task stack of **short-horizon event heads** (click, like, dwell, conversion) and move the long-term objective into one of four places: (1) a **value-model / fusion layer** over those heads (Instagram Explore, LinkedIn LiRank, Tencent BatchRL-MTF, Kuaishou xMTF); (2) a **delayed reward** on a session MDP (Kuaishou RLUR / GFN4Retention / Future Impact Decomposition; Google SlateQ and Top-K Off-Policy REINFORCE; Spotify long-term audio Q); (3) a **user-level LTV or return-time head** that is not yet item-attributed (Google ZILN, Kuaishou ODMN, WeChat GRePO-LTV); (4) an **experiment surrogate**, not a training loss (Athey et al. surrogate index; Netflix 14-vs-63 day auto-surrogate; Google proxy-metric selection; Spotify LOPE).

What sources **state**: prediction of retention conditional on exposure is the default; causal incrementality of a single impression is almost never inside the ranker. Reciprocity and congestion are handled in a separate two-sided literature (CyberAgent TU/NSW, Hinge Most Compatible, CUPID, CRRS) that does not use retention/revenue as the ranking objective. No card in this corpus documents a production dating ranker whose training loss is D7/D30 retention or subscription LTV.

**Inference (not in sources):** the dating team’s current CTR/CVR + uplift blend is the Instagram/LinkedIn value-model pattern plus an extra causal score that industry feed rankers do not mix into the same serving formula. Unifying the objective without collapsing that distinction, and without ignoring reciprocity, is the design problem this survey is for.

### Most promising approaches (for this product)

1. **Auxiliary-head LTV fusion:** keep like/match/conversation towers; add delayed retention/revenue heads; replace the post-hoc blend with learned fusion (BatchRL-MTF / xMTF / LiRank / Instagram VM). Treat uplift as evaluation, not as a third serving score.
2. **Retention-ensemble RL with item-level credit:** RLUR-style return-time reward over existing scorers, plus SlateQ/FID decomposition so a delayed user outcome can touch one shown profile.
3. **Reciprocal second stage that cannot be an afterthought:** CyberAgent TU/NSW (or a reverse-like head plus capacity penalty) on top of (1) or (2). No surveyed LTV ranker does this jointly.

### Practical recommendations

Short term (1–3 months): add D7/D30 and 28-day revenue heads as auxiliaries; stop blending uplift into the rank score; stand up a surrogate-index / proxy-metric gate from historical ranking A/Bs; log fusion weights and two-sided like/match outcomes.

Mid term (3–6 months): learned fusion toward a dwell/return proxy (BatchRL-MTF or xMTF); item-level delayed credit (FID or SlateQ Q-head); TU/NSW or inbound-cap rerank; incrementality only in OPE and experiment design (LOPE, UniCoRn, DiPS).

---

## Taxonomy of unified long-term-value ranking approaches

Categories are defined by **where the long-horizon objective sits**, not by venue. Industry adopters are taken from the cards.

| Family | What is unified | Where LTV/retention lives | Prediction vs incrementality (as sources state) | Industry adopters in this corpus |
|--------|-----------------|---------------------------|--------------------------------------------------|----------------------------------|
| T1. Value model / multi-task fusion | Many short heads → one score | Tunable or learned fusion weights; sometimes a dwell/revisit/LTV auxiliary | Prediction. Fusion is not CATE. | Instagram Explore VM; LinkedIn LiRank and dwell MOO; YouTube MMoE; Tencent BatchRL-MTF → UnifiedRL → EnhancedRL; Kuaishou xMTF; Pinterest MTL+calibration blog and PRL-PUTS; Pinterest Save/Revisit/Retain; Twitch delayed-signal MOR; Alibaba video LTV heads / SORT-Gen list rerank; Airbnb MO-LTR distillation; Meituan MTFM |
| T2. Retention-as-RL-reward | Policy over items or over fusion weights | Delayed return time / session return / 60-day stickiness as reward | Policy value, still not impression-level uplift | Kuaishou RLUR, TSCAC, GFN4Retention, FID, AURO, SEC; Google SlateQ, Top-K REINFORCE, URL; Spotify audio long-term Q; Yahoo/Etsy r²Bandit; Alibaba value-aware profit RL |
| T3. Surrogate / proxy layer | Experiment decision, not the ranker | Short-run metrics mapped to long-run ATE or policy value | Incrementality of **policies**, not of one exposure | Athey et al. surrogate index; Netflix 200-test auto-surrogate + TechBlog TC/JIVE recipe + KDD 2024 covariance paper; Google Choosing a Proxy Metric / Pareto Optimal Proxy; Spotify LOPE; Impatient Bandits; DASI; PROXIMA; Proximal Surrogate Index (unobserved confounding); 15-platform workshop |
| T4. User-level LTV / return prediction | User (or user–item) outcome model | Multi-horizon spend, DAU, LT1/LT7/LT30 revisit | Prediction. Online ROI is measured separately. | Google ZILN; Kuaishou ODMN; WeChat GRePO-LTV; Meituan CC-OR-Net; Pinterest PinnerFormer 14–28d; Snap UUM; Kuaishou OCARM; Duolingo / Pinterest notification volume |
| T5. Entire-space funnel MTL | Impression → click → conversion (chain) | Sparse conversion head trained on all impressions | Prediction; ESCM² adds IPS/DR toward a causal CVR estimand | Alibaba ESMM, ESM², HM³, ESDF, DEFUSE; Ant ESCM²; Meituan AITM; Airbnb Journey Ranker |
| T6. Uplift inside ranking | Rank by CATE / IPS-corrected match | Treatment effect of campaign or of bilateral display | Incrementality — but almost never a swipe ranker | Devriendt et al. LTR-for-uplift; AUUC-max targeting; Tencent RERUM / E3IR (incentive budget); ReAlloc multi-channel seller budget; Sony counterfactual reciprocal; Wantedly DiPS matching OPE |
| T7. Delayed-feedback / revenue labels | Right-censored conversion or spend | Attribution windows 1–30d; fake-negative / delay models | Prediction of delayed conversion, not retention uplift | Criteo DFM; Twitter FN loss; Alibaba ESDF/DEFUSE/**DEFER**; FSIW, TS-DL, DLA-DF, many-conversions Poisson (Google); Tencent CBDF; UniROM ad-slate revenue RL |
| T8. Two-sided overlay | Bilateral score or market-clearing | Match/chat quality, not LTV | Prediction of matches; experiments need interference designs | Hinge Most Compatible; Tinder matching blog + geosharded retrieval (infra); CyberAgent TU/NSW and MTRS; CUPID (Azar); CRRS; Momo; LinkedIn Jobs / UniCoRn; Airbnb diversity / guest-preference IV; TSPR coherency-preserving marketplace experiments; ECDA matching-theoretic dating integrator; Grindr (no ranker) |
| T9. Generative / reward-model ranker | Retrieve+rank as one sequence model | Reward model from engagement → long-term utility | Still correlational (Netflix GenRec states this) | Meta HSTU; Kuaishou OneRec; Meituan MTGR; Netflix GenRec |

**Inference:** T1+T5+T8 is the least discontinuous path from today’s like/match/conversation + uplift blend. T2 is the documented “make retention the objective” path, but only on one-sided video. T3 is mandatory evaluation infrastructure either way. T6 should **not** be folded into the serving formula as if conditional retention were causal.

---

## 1. D1 — Long-term value as the ranking objective: value models and fusion (28 papers)

These papers keep short-horizon heads and change **how they are combined**, or they add a delayed auxiliary that is still not a causal uplift.

### Understanding Dwell Time to Improve LinkedIn Feed Ranking (LinkedIn Engineering, 2018)

- Source: LinkedIn Engineering blog, 2018
- Detailed analysis: [2018_Blog_NA_Understanding-Dwell-Time-LinkedIn-Feed.md](./read-papers/2018_Blog_NA_Understanding-Dwell-Time-LinkedIn-Feed.md)

Adds P(skip) from dwell CDFs beside action and downstream/upstream value heads. Online: fewer skips, more clicks/virals and time spent (percentages not stated). Prediction, not incrementality.

### Recommending What Video to Watch Next: A Multitask Ranking System (RecSys 2019)

- Source: RecSys 2019 (YouTube / Google)
- Detailed analysis: [2019_RecSys_MMoE_Recommending-What-Video-Watch-Next.md](./read-papers/2019_RecSys_MMoE_Recommending-What-Video-Watch-Next.md)

MMoE over engagement and satisfaction heads. Live: +0.20–0.45% engagement, +1.22–3.07% satisfaction vs shared-bottom. Pointwise prediction.

### A Pareto-Efficient Algorithm for Multiple Objective Optimization in E-Commerce Recommendation (RecSys 2019)

- Source: RecSys 2019 (Alibaba / Kwai)
- Detailed analysis: [2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Recommendation.md](./read-papers/2019_RecSys_PE-LTR_Pareto-Efficient-Multi-Objective-Recommendation.md)

Scalarized multi-objective LTR; CTR–GMV Pearson r = −0.343. Online percentages not specified in source. Shows engagement vs revenue conflict before any dating success paradox.

### Multitask Mixture of Sequential Experts for User Activity Streams (KDD 2020)

- Source: KDD 2020 (Google)
- Detailed analysis: [2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts.md](./read-papers/2020_KDD_MoSE_Multitask-Mixture-Sequential-Experts.md)

Sequential MoE for next-day activity counts. GMail: +4.8% AUC on quality–cost; ~8% click preservation at 80% resource savings. Not item-level delayed credit.

### Jointly Learning to Recommend and Advertise (WWW/KDD 2020)

- Source: arXiv 2003.00097 (MSU / ByteDance)
- Detailed analysis: [2020_KDD_RAM_Jointly-Learning-Recommend-and-Advertise.md](./read-papers/2020_KDD_RAM_Jointly-Learning-Recommend-and-Advertise.md)

Two-level DQN: session dwell vs ad continuation vs RTB revenue. RAM-l vs DRQN: Rrev +16.42%. Session-level RL, not user LTV.

### Multi-Objective Ranking Optimization for Product Search Using Stochastic Label Aggregation (WWW 2020)

- Source: WWW 2020 (Amazon)
- Detailed analysis: [2020_WWW_NA_Multi-Objective-Ranking-Stochastic-Label-Aggregation.md](./read-papers/2020_WWW_NA_Multi-Objective-Ranking-Stochastic-Label-Aggregation.md)

Stochastic per-query choice between relevance and 6-week/2-month purchase labels. Two-phase stochastic aggregation dominates linear fusion on reported NDCG.

### Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems (KDD 2022)

- Source: KDD 2022 (Tencent)
- Detailed analysis: [2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md](./read-papers/2022_KDD_BatchRL-MTF_Multi-Task-Fusion-Long-Term-Satisfaction.md)

**Primary T1 template.** PLE heads stay; BCQ policy outputs fusion weights; instant reward is a regression-weighted mix of play/like/share/skip toward future app dwell (γ=0.95). Production: **+2.550% app dwell time, +9.651% positive-interaction rate**. Not a direct LTV predictor; not incrementality.

### Scaling the Instagram Explore Recommendations System (Meta Engineering, 2023)

- Source: Meta Engineering blog, 2023
- Detailed analysis: [2023_Blog_NA_Scaling-Instagram-Explore-Recommendations.md](./read-papers/2023_Blog_NA_Scaling-Instagram-Explore-Recommendations.md)

MTML second-stage heads fused by a tunable **value model** into Expected Value. Distillation to first stage. Numeric lifts not specified in source. Closest public cousin of a post-hoc head blend.

### Multitask Ranking System for Immersive Feed and No More Clicks (CIKM 2023)

- Source: CIKM 2023 (Google)
- Detailed analysis: [2023_CIKM_NA_Multitask-Ranking-Immersive-Feed-Short-Video.md](./read-papers/2023_CIKM_NA_Multitask-Ranking-Immersive-Feed-Short-Video.md)

Weighted combination of watch/like/comment/share; trail-bias correction. Live Overall Enjoyment +1.96% from trail debias. Serving-time fusion, not one LTV head.

### Leveraging Dwell Time to Improve Member Experiences on the LinkedIn Feed (LinkedIn Engineering, 2024)

- Source: LinkedIn Engineering blog, 2024
- Detailed analysis: [2024_Blog_NA_Leveraging-Dwell-Time-LinkedIn-Feed.md](./read-papers/2024_Blog_NA_Leveraging-Dwell-Time-LinkedIn-Feed.md)

Auto-normalized long-dwell exceedance vs cluster percentiles, fused in MOO. Statistically significant dwell gains (exact % not in blog). Predictive engagement, not incremental retention.

### LiRank: Industrial Large Scale Ranking Models at LinkedIn (KDD 2024)

- Source: KDD 2024 (LinkedIn)
- Detailed analysis: [2024_KDD_LiRank_Industrial-Large-Scale-Ranking-LinkedIn.md](./read-papers/2024_KDD_LiRank_Industrial-Large-Scale-Ranking-LinkedIn.md)

Multi-task like/comment/share/click/**long dwell**; Jobs application+click; Ads chargeability MTL. Online: **+0.5% Feed sessions, +1.76% qualified applications, +4.3% Ads CTR**; Neural Linear Thompson sampling **+0.06% professionals DAU**. Pointwise prediction; DAU explored, not attributed per post.

### Multi-objective Learning to Rank by Model Distillation (KDD 2024)

- Source: KDD 2024 (Airbnb)
- Detailed analysis: [2024_KDD_MO-LTR-MD_Multi-Objective-Learning-to-Rank-Distillation.md](./read-papers/2024_KDD_MO-LTR-MD_Multi-Objective-Learning-to-Rank-Distillation.md)

Student matches booking hard labels while distilling multi-objective teachers (cancellations, review boosts). Online **+0.37% booking (p=0.02)**; serving-time score boosts hurt NDCG more than soft labels.

### Trinity: Syncretizing Multi-/Long-Tail/Long-Term Interests All in One (KDD 2024)

- Source: KDD 2024 (ByteDance)
- Detailed analysis: [2024_KDD_Trinity_Syncretizing-Long-Tail-Long-Term-Interests.md](./read-papers/2024_KDD_Trinity_Syncretizing-Long-Tail-Long-Term-Interests.md)

Long-term cluster histograms (up to 2500 actions) plus playtime-weighted rerank. Douyin: Watch Time +0.118%, AAD +0.008% (Trinity-M). AAD is a retention **surrogate**, not item-attributed LTV.

### Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals (arXiv 2025)

- Source: arXiv 2608.04455 (Twitch / Prime Video)
- Detailed analysis: [2025_arXiv_NA_Multi-Objective-Ranking-Live-Streaming-Delayed-Signals.md](./read-papers/2025_arXiv_NA_Multi-Objective-Ranking-Live-Streaming-Delayed-Signals.md)

Immediate minutes-play plus **14-day** chat/follow/spend heads. Online Exp.1: DAV +0.09%, D-viewer capped ARPU +0.56%. Closest documented delayed **revenue** head inside a ranker. Still pointwise prediction.

### Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention (arXiv 2025)

- Source: arXiv 2511.18013 (Pinterest)
- Detailed analysis: [2025_arXiv_NA_Save-Revisit-Retain-User-Retention.md](./read-papers/2025_arXiv_NA_Save-Revisit-Retain-User-Retention.md)

MMoE + RP&RV head: save then 1d/7d profile revisit, joined on user+Pin. Online: 7dRevGrid +1.18% volume, active users +0.10%, time spent +0.39%. Item-level **surrogate** attribution, not causal.

### One Model to Rank Them All (EGA-V1 / UniROM) (arXiv 2025)

- Source: arXiv 2505.19755
- Detailed analysis: [2025_arXiv_UniROM_One-Model-to-Rank-Them-All.md](./read-papers/2025_arXiv_UniROM_One-Model-to-Rank-Them-All.md)

Pretrain clicks; RLAF on platform revenue under IC/IR. Online vs MCA: CTR +5.2%, RPM +13.6%. Slate-level **ad revenue**, not user retention. Marginal-contribution rewards are credit assignment for ads, not dating LTV.

### xMTF: A Formula-Free Model for Reinforcement-Learning-Based Multi-Task Fusion (WWW 2025)

- Source: WWW 2025 (Kuaishou)
- Detailed analysis: [2025_arXiv_xMTF_Formula-Free-RL-Multi-Task-Fusion.md](./read-papers/2025_arXiv_xMTF_Formula-Free-RL-Multi-Task-Fusion.md)

Replaces BatchRL-MTF’s fixed log-sum formula with monotonic fusion cells; outer RL on daily watch time, inner SL. Online vs UNEX-RL: **+0.833% daily watch time**, +0.583% play counts. Session MDP; no item-level 30-day credit.

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning (arXiv 2026)

- Source: arXiv 2607.14192 (Pinterest)
- Detailed analysis: [2026_arXiv_NA_Long-Term-Engagement-Downstream-Rewards-Learning.md](./read-papers/2026_arXiv_NA_Long-Term-Engagement-Downstream-Rewards-Learning.md)

**Q8 template:** screen session behaviors by retention correlation; add deeper-session / negative-shallow / adoption heads to existing Pinnability. Homefeed SS +0.24–0.48%; label latency ~3 weeks → ~2 days. Uniform negative thresholds hurt non-core users until segment-tuned.

### A Long-term Value Prediction Framework In Video Ranking (2026)

- Source: DOI 10.1145/3774904.3792830 (Alibaba)
- Detailed analysis: [2026_arXiv_NA_Long-Term-Value-Prediction-Framework-Video-Ranking.md](./read-papers/2026_arXiv_NA_Long-Term-Value-Prediction-Framework-Video-Ranking.md)

PDQ-normalized slide time, attributed slide time, censoring-aware **author day-level LTV**. Online: PDQ +2.49% VV; Author LTV LT3 +0.21%. Delayed-label pipeline; still prediction.

### A Production-Ready RL Framework for Personalized Utility Tuning with Pareto Sweeping (PRL-PUTS) (arXiv 2026)

- Source: arXiv 2605.16344 (Pinterest)
- Detailed analysis: [2026_arXiv_PRL-PUTS_Personalized-Utility-Tuning-Pareto-Sweeping.md](./read-papers/2026_arXiv_PRL-PUTS_Personalized-Utility-Tuning-Pareto-Sweeping.md)

One-step bandit (γ=0) over discrete (Repin, P2P) weight pairs on frozen heads. Online: Repin +0.66%, P2P +0.30%, Successful Sessions +0.13%. Offline–online Pearson up to 0.999. Fusion-layer RL without delayed retention reward.

### Continuation (2026-08-17)

**UnifiedRL / IntegratedRL-MTF** (Tencent, 2024) — [card](./read-papers/2024_arXiv_IntegratedRL-MTF_Offline-RL-Multi-Task-Fusion.md). Direct successor of BatchRL-MTF: offline actor–critic on fusion weights plus a custom exploration strategy. Online vs evolutionary search: **+4.64% valid consumption, +1.74% duration**. **Prediction/policy on fusion, not impression CATE.**

**EnhancedRL** (Tencent, 2024) — [card](./read-papers/2024_arXiv_EnhancedRL_Enhanced-State-RL-Multi-Task-Fusion.md). Same MTF MDP with an enhanced user–item state. Online vs UnifiedRL: **+3.84% valid consumption, +0.58% duration**. Documented **staged MTF migration**: formula fusion → UnifiedRL → EnhancedRL.

**Pinterest MTL + calibration** (Engineering blog, 2020) — [card](./read-papers/2020_Blog_NA_Pinterest-MTL-Calibration-Utility-Home-Feed.md). Per-action heads fused into a calibrated utility; adding a >10s video head shifted video distribution **+40%**. Value-model cousin of Instagram Explore.

**Instagram “Powered by AI” Explore** (ai.meta.com, 2021) — [card](./read-papers/2021_Blog_NA_Powered-by-AI-Instagram-Explore-Value-Model.md). Weighted arithmetic value model over like/save vs negative actions. Numeric lifts **not specified in source**. Complements the 2023 scaling post.

**Netflix long-term member satisfaction** (TechBlog, 2024) — [card](./read-papers/2024_Blog_NA_Recommending-Long-Term-Member-Satisfaction-Netflix.md). Public write-up of the RecSys 2023 reward-innovation talk: retention is the north star but **unsuitable as a training reward**; engineered proxy rewards + delayed-feedback predictors feed a contextual bandit. No % in the blog.

**Alibaba GMV mutual-influence ranking** (IJCAI 2018) — [card](./read-papers/2018_IJCAI_NA_Globally-Optimized-Mutual-Influence-Aware-Ranking.md). Slate purchase probability depends on other items. Offline AUC 0.724→0.774. Within-slate congestion analog; GMV not dating LTV.

**SORT-Gen** (SIGIR 2025, Taobao) — [card](./read-papers/2025_SIGIR_SORT-Gen_Generative-Re-ranking-List-Level-Multi-Objective.md). Generative list rerank of click/order/GMV. vs greedy: **+9.61% click, +8.35% order, +13.67% GMV**. List-level credit, one-sided e-comm.

**MTFM** (Meituan, 2025) — [card](./read-papers/2025_arXiv_MTFM_Alignment-Free-Foundation-Model-Meituan.md). Alignment-free foundation model, MMoE heads, CTR/CTCVR. Backbone, not a delayed retention objective.

---

## 2. D2 — RL and long-horizon credit assignment for retention (16 papers)

### Returning is Believing: Optimizing Long-term User Engagement in Recommender Systems (CIKM 2017)

- Source: CIKM 2017 (UVA / Etsy / Yahoo)
- Detailed analysis: [2017_CIKM_NA_Returning-is-Believing-Long-Term-Engagement.md](./read-papers/2017_CIKM_NA_Returning-is-Believing-Long-Term-Engagement.md)

r²Bandit: click plus expected future clicks from a return-time GLM. Yahoo replay: ~2× CTR vs GLM-UCB; return rate ~1.8×. Early return-time credit, not uplift.

### DRN: A Deep Reinforcement Learning Framework for News Recommendation (WWW 2018)

- Source: WWW 2018 (Penn State / MSRA)
- Detailed analysis: [2018_WWW_DRN_Deep-Reinforcement-Learning-News-Recommendation.md](./read-papers/2018_WWW_DRN_Deep-Reinforcement-Learning-News-Recommendation.md)

DQN reward = click + β·activeness (survival on return intervals). Online CTR 0.0113 for DDQN+U+DBGD. Activeness is a supplementary signal, not an uplift head.

### SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets (IJCAI 2019)

- Source: IJCAI 2019 (Google)
- Detailed analysis: [2019_IJCAI_SlateQ_Reinforcement-Learning-Recommendation-Sets.md](./read-papers/2019_IJCAI_SlateQ_Reinforcement-Learning-Recommendation-Sets.md)

Under single-choice, slate Q = Σ P(i|s,A) Q(s,i); serve v·Q. YouTube LTV capped at N days. Live: ~+0.5% day 1 to >+1.0% day 20 vs myopic. **Q4/Q8:** keep pCTR, add Q-head.

### Top-K Off-Policy Correction for a REINFORCE Recommender System (WSDM 2019)

- Source: WSDM 2019 (Google / YouTube)
- Detailed analysis: [2019_WSDM_NA_Top-K-Off-Policy-Correction-REINFORCE.md](./read-papers/2019_WSDM_NA_Top-K-Off-Policy-Correction-REINFORCE.md)

Trajectory return with top-K IPS. Standard off-policy: no significant ViewTime; top-K K=16 avoids −0.66% ViewTime drop. Credit is sequence-level, not item-level retention.

### Value-aware Recommendation based on Reinforced Profit Maximization (WWW 2019)

- Source: WWW 2019 (Alibaba)
- Detailed analysis: [2019_WWW_NA_Value-Aware-Recommendation-Reinforcement-Profit.md](./read-papers/2019_WWW_NA_Value-Aware-Recommendation-Reinforcement-Profit.md)

Page-level monetized reward; XVR generalizes CVR. Online vs DNN-LTR: **+6.8% GMV**. Predicts conversion×price, not uplift of exposure.

### Neural Interactive Collaborative Filtering (SIGIR 2020)

- Source: SIGIR 2020 (Tsinghua / JD / Baidu)
- Detailed analysis: [2020_SIGIR_NICF_Neural-Interactive-Collaborative-Filtering.md](./read-papers/2020_SIGIR_NICF_Neural-Interactive-Collaborative-Filtering.md)

Q-learning on ratings; curriculum on γ. Precision@40 +4.6–9.4% in simulators. No retention label.

### User Response Models to Improve a REINFORCE Recommender System (WSDM 2021)

- Source: WSDM 2021 (Google)
- Detailed analysis: [2021_WSDM_URL_User-Response-Models-REINFORCE-Recommender.md](./read-papers/2021_WSDM_URL_User-Response-Models-REINFORCE-Recommender.md)

Auxiliary click/dwell heads on Top-K REINFORCE; gated to low-activity users. Live enjoyment **+0.12%** (low-activity +0.26%). **Q8:** auxiliary heads first, no serving change.

### Reinforcing User Retention in a Billion Scale Short Video Recommender System (WWW 2023)

- Source: WWW 2023 (Kuaishou)
- Detailed analysis: [2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale.md](./read-papers/2023_WWW_RLUR_Reinforcing-User-Retention-Billion-Scale.md)

**Primary T2 template.** Actor outputs 8 fusion weights; terminal reward = normalized returning time; immediate + RND critics. Online ≈150 days vs CEM: **+0.450% app open frequency, +0.2% DAU, +0.053% D1, +0.063% D7**. Session-end credit, not per-video 30-day attribution. Prediction/policy, not CATE.

### Two-Stage Constrained Actor-Critic for Short Video Recommendation (WWW 2023)

- Source: WWW 2023 (Kuaishou)
- Detailed analysis: [2023_WWW_TCAC_Two-Stage-Constrained-Actor-Critic.md](./read-papers/2023_WWW_TCAC_Two-Stage-Constrained-Actor-Critic.md)

Maximize WatchTime with KL constraints to sparse like/follow/share policies. Online vs LTR: WatchTime +0.379%, Share +3.376%, **Comment −0.619%**. Documents a real sparse-vs-dense trade-off.

### Optimizing Audio Recommendations for the Long-Term: A Reinforcement Learning Perspective (arXiv 2023)

- Source: arXiv 2302.03561 (Spotify / Columbia)
- Detailed analysis: [2023_arXiv_NA_Optimizing-Audio-Recommendations-Long-Term.md](./read-papers/2023_arXiv_NA_Optimizing-Audio-Recommendations-Long-Term.md)

Q = clickiness × (1 + stickiness). **60-day** stickiness. Banner (impacted users): **+81% 60-day minutes, +32% 60-day active days**; shelf week-8 podcast minutes +1.7%. Keep myopic head; add item-level habit term. Not two-sided.

### Future Impact Decomposition in Request-level Recommendations (KDD 2024)

- Source: KDD 2024 (Kuaishou)
- Detailed analysis: [2024_KDD_FID_Future-Impact-Decomposition-Request-Level.md](./read-papers/2024_KDD_FID_Future-Impact-Decomposition-Request-Level.md)

ItemA2C splits V(s_{t+1}) across slate items. Online vs request A2C: watch time +0.129%, like +1.103%, **DAU +0.028%, retention +0.016%**. Best documented **item-level** future-impact split. Degrades as K grows.

### Modeling User Retention through Generative Flow Networks (KDD 2024)

- Source: KDD 2024 (Kuaishou)
- Detailed analysis: [2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow.md](./read-papers/2024_KDD_GFN4Retention_Modeling-User-Retention-Generative-Flow.md)

Backward flow attributes terminal retention to each step. Authors report beating CEM/DIN/TD3/SAC/RLUR; **exact percentages not specified in source**. Most explicit “retention attribution” language in the corpus.

### AURO: Reinforcement Learning for Adaptive User Retention Optimization (2024)

- Source: DOI 10.1145/3696410.3714956 (NTU / Kuaishou)
- Detailed analysis: [2024_arXiv_AURO_Adaptive-User-Retention-Optimization.md](./read-papers/2024_arXiv_AURO_Adaptive-User-Retention-Optimization.md)

Episode-end return-time reward; state-abstraction for drift. Live vs RLUR: 7d retention +0.138‰, dwell +0.263‰, CTR +3.260‰ (permillage as reported).

### Continuation (2026-08-17)

**Stratified Expert Cloning (SEC)** (Kuaishou / PKU, 2025) — [card](./read-papers/2025_arXiv_NA_Stratified-Expert-Cloning-Retention-Aware.md). Imitate high-retention expert trajectories instead of online RL. Offline return time 1.411 vs GFN 1.496 (−5.7%); online Active Days **+0.098%**. Migration-friendly: clone retention experts from logs rather than train an actor on D7.

**KuaiSim** (2023) — [card](./read-papers/2023_arXiv_KuaiSim_Comprehensive-Simulator-Recommender-Systems.md). Simulator with a next-day return module. Tooling for retention RL, not a production ranker.

**EDT4Rec** (KDD 2024) — [card](./read-papers/2024_arXiv_NA_Maximum-Entropy-Decision-Transformer-Reward-Relabelling.md). Decision Transformer with reward relabeling for click RTG. KuaiRand Recall 31.26 vs CDT4Rec 30.32. Academic sequential RL; click reward, not D7.

---

## 3. D3 — Surrogates and proxy metrics (13 papers)

These papers evaluate **policies**, they do not train the swipe model. They are how you know a unified ranker helped 30-day retention without waiting 30 days every time.

### The Surrogate Index: Combining Short-Term Proxies to Estimate Long-Term Treatment Effects (NBER 2019)

- Source: NBER WP 26463 (Athey, Chetty, Imbens, Kang)
- Detailed analysis: [2019_NBER_NA_The-Surrogate-Index-Short-Term-Proxies.md](./read-papers/2019_NBER_NA_The-Surrogate-Index-Short-Term-Proxies.md)

μ(s,x) = E[Y|S,X]; ATE on index = ATE on Y under surrogacy+comparability. GAIN: 6-quarter index 0.061 vs naive 0.117 vs 36-quarter 0.064. **Incrementality**, not ranking.

### Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay (KDD 2023)

- Source: KDD 2023 (Spotify)
- Detailed analysis: [2023_KDD_NA_Impatient-Bandits-Long-Term-Without-Delay.md](./read-papers/2023_KDD_NA_Impatient-Bandits-Long-Term-Without-Delay.md)

Progressive Bayesian filter on daily traces → 60-day stickiness. 50% of prior variance by day 8; day-two proxy plateaus. Offline simulation only; predictive, not causal uplift.

### Evaluating the Surrogate Index as a Decision-Making Tool Using 200 A/B Tests at Netflix (arXiv 2023)

- Source: arXiv 2311.11922 (Netflix)
- Detailed analysis: [2023_arXiv_NA_Evaluating-Surrogate-Index-200-AB-Tests-Netflix.md](./read-papers/2023_arXiv_NA_Evaluating-Surrogate-Index-200-AB-Tests-Netflix.md)

14-day linear auto-surrogate vs 63-day direct: **~95% decision consistency**, precision 79%, recall 65%, **0 false launches of statistically negative experiences**. Conservative (misses some true positives).

### Pareto Optimal Proxy Metrics (arXiv 2023 / card year 2025)

- Source: arXiv 2307.01000 (Google)
- Detailed analysis: [2023_arXiv_NA_Pareto-Optimal-Proxy-Metrics.md](./read-papers/2023_arXiv_NA_Pareto-Optimal-Proxy-Metrics.md)

Pareto front of sensitivity vs DAU directionality. Composite proxy: 8.5× sensitivity, recall 72% vs 40% for short-term north star. Does not estimate effect size.

### Estimating long-term outcome of algorithms (Spotify Research Blog, 2024)

- Source: Spotify Research blog (LOPE intro)
- Detailed analysis: [2024_Blog_NA_Estimating-Long-Term-Outcome-Algorithms-Spotify.md](./read-papers/2024_Blog_NA_Estimating-Long-Term-Outcome-Algorithms-Spotify.md)

Blog for Saito et al. WWW 2024: long-term reward ≅ surrogate effect + action effect. LOPE vs DR 36% MSE at n=200 (simulation numbers; full table on the WWW card).

### Choosing a Proxy Metric from Past Experiments (KDD 2024)

- Source: KDD 2024 (Google / DeepMind)
- Detailed analysis: [2024_KDD_NA_Choosing-Proxy-Metric-Past-Experiments.md](./read-papers/2024_KDD_NA_Choosing-Proxy-Metric-Past-Experiments.md)

Sharpe-ratio weights over historical TEs; sample-size adaptive. 307 recsys A/Bs: composite proxy quality 0.302 vs best auxiliary 0.258. No live deployment in source.

### Long-term Off-Policy Evaluation and Learning (WWW 2024)

- Source: WWW 2024 (Spotify)
- Detailed analysis: [2024_WWW_NA_Long-Term-Off-Policy-Evaluation-Learning.md](./read-papers/2024_WWW_NA_Long-Term-Off-Policy-Evaluation-Learning.md)

LOPE: week-1 streams/clicks/likes → week-3 streams; robust when surrogacy fails. Real A/B MSE 9.2–15.0% below DR. Horizon in the Spotify test is **21 days**, not a year.

### Estimating the Long-Term Effects of Novel Treatments: The Dynamically Adjusted Surrogate Index (NeurIPS 2021; file dated 2024)

- Source: arXiv 2103.08390 (Microsoft Research)
- Detailed analysis: [2024_arXiv_NA_Dynamically-Adjusted-Surrogate-Index.md](./read-papers/2024_arXiv_NA_Dynamically-Adjusted-Surrogate-Index.md)

Adjusts Y for auto-correlated future treatments before the surrogate map. Unadjusted indices overestimate under serial treatments. Semi-synthetic only.

### PROXIMA: Proxy Metric Validation with Segment-Level Fragility Detection (arXiv 2026)

- Source: arXiv 2604.14352
- Detailed analysis: [2025_arXiv_PROXIMA_Proxy-Metric-Validation-Segment-Fragility.md](./read-papers/2025_arXiv_PROXIMA_Proxy-Metric-Validation-Segment-Fragility.md)

Reliability = correlation + directional accuracy + segment fragility. KuaiRec fragility **68%** vs Criteo 13% despite >96% directional accuracy. Recommendation proxies hide Simpson reversals.

### Evaluating for the Long Term: Learnings from Industry (arXiv 2026)

- Source: arXiv 2608.08043 (15 platforms)
- Detailed analysis: [2026_arXiv_NA_Evaluating-for-the-Long-Term-Industry.md](./read-papers/2026_arXiv_NA_Evaluating-for-the-Long-Term-Industry.md)

Consensus: experiment-learned surrogates beat observational; autosurrogates are hard to beat; sign reversals concentrate in **content quality, hyper-monetization, pricing**. Netflix 95% 2-week vs 2-month; YouTube trashy-video −0.5% watch at 3 weeks, recovery by 3 months; Meta integrity holdout lower activity at 2 years. Directly flags the dating **success paradox / monetization vs match quality** as a sign-reversal class.

### Continuation (2026-08-17)

**Netflix TechBlog: better proxy metrics from past experiments** (2024) — [card](./read-papers/2024_Blog_NA_Improve-Next-Experiment-Proxy-Metrics-Netflix.md). Engineering recipe for the KDD 2024 covariance paper: user-level \(S\)–\(Y\) correlation and OLS on estimated ATEs are both **biased**; use TC or JIVE. Clickbait example is the warning against ranking for likes because likes correlate with retention. No numeric lift in the blog.

**Learning the Covariance of Treatment Effects Across Many Weak Experiments** (KDD 2024, Netflix) — [card](./read-papers/2024_KDD_NA_Learning-Covariance-Treatment-Effects-Weak-Experiments.md). Formal TC/JIVE/LIML estimators. Experiment-level, not item-level.

**Proximal Surrogate Index** (2026) — [card](./read-papers/2026_arXiv_NA_Proximal-Surrogate-Index-Unobserved-Confounding.md). Extends Athey et al. when surrogacy fails under unobserved confounding. Closer to RCT 4-year earnings than naive index (16.43 vs worse naive). Academic; relevant if dating D7 is a leaky surrogate for D30.

---

## 4. D4 — User-level retention/LTV labels (12 papers)

### Notification Volume Control and Optimization System at Pinterest (KDD 2018)

- Source: KDD 2018 (Pinterest)
- Detailed analysis: [2018_KDD_NA_Notification-Volume-Control-Optimization-Pinterest.md](./read-papers/2018_KDD_NA_Notification-Volume-Control-Optimization-Pinterest.md)

Weekly budget from DAU, unsubscribe, week-4 post-unsub activity. Incremental utility p(a|k+1)−p(a|k). Email&Push: volume down, CTR +10–21%, **DAU +3%**. Decouples volume from CTR ranker. User-level, not item-level.

### A Deep Probabilistic Model for Customer Lifetime Value Prediction (2019)

- Source: arXiv 1907.04485 (Google)
- Detailed analysis: [2019_arXiv_ZILN_Deep-Probabilistic-Customer-Lifetime-Value.md](./read-papers/2019_arXiv_ZILN_Deep-Probabilistic-Customer-Lifetime-Value.md)

Zero-inflated lognormal on 1–3 year spend after first purchase. +23.9–48.0% Spearman vs MSE. **The revenue-head loss** for subscriptions + a-la-carte. Customer-level prediction.

### A Sleeping, Recovering Bandit Algorithm for Optimizing Recurring Notifications (KDD 2020)

- Source: KDD 2020 (Duolingo)
- Detailed analysis: [2020_KDD_NA_Sleeping-Recovering-Bandit-Notifications-Duolingo.md](./read-papers/2020_KDD_NA_Sleeping-Recovering-Bandit-Notifications-Duolingo.md)

Reward = lesson within 2 hours; also D1/D7. Online: +0.5% DAU, **+2.0–2.2% new-user D1/D7**. Difference scoring (relative lift), not a supervised LTV ranker.

### Billion-user Customer Lifetime Value Prediction (CIKM 2022)

- Source: CIKM 2022 (Kuaishou)
- Detailed analysis: [2022_CIKM_NA_Billion-User-Customer-Lifetime-Value-Kuaishou.md](./read-papers/2022_CIKM_NA_Billion-User-Customer-Lifetime-Value-Kuaishou.md)

ODMN: ordered ltv_30 ≤ … ≤ ltv_365. Beats ZILN on AMBE; online ROI **+11.9 / +12.8 / +14.7%**. User-level acquisition LTV, not swipe credit.

### PinnerFormer: Sequence Modeling for User Representation at Pinterest (KDD 2022)

- Source: KDD 2022 (Pinterest)
- Detailed analysis: [2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation.md](./read-papers/2022_KDD_PinnerFormer_Sequence-Modeling-User-Representation.md)

Dense all-action loss on positives in a **14–28 day** window. Homefeed +2.5% repins. Future-engagement propensity, not LTV or incrementality.

### Universal User Modeling (UUM) (Snap Engineering, 2025)

- Source: Snap Engineering blog
- Detailed analysis: [2024_Blog_UUM_Universal-User-Modeling-Snapchat.md](./read-papers/2024_Blog_UUM_Universal-User-Modeling-Snapchat.md)

1+ year cross-surface sequences; next-k prediction; embeddings into rankers. Numeric A/B lifts **not specified in source**. Encoder, not an LTV objective.

### CC-OR-Net: A Unified Framework for LTV Prediction through Structural Decoupling (arXiv 2025)

- Source: arXiv 2601.10176 (Meituan)
- Detailed analysis: [2025_arXiv_CC-OR-Net_Unified-LTV-Prediction-Structural-Decoupling.md](./read-papers/2025_arXiv_CC-OR-Net_Unified-LTV-Prediction-Structural-Decoupling.md)

Ordinal buckets + whale precision. Domain 1 Gini 0.803, Spearman 0.761. User-level; no impression credit.

### Mini-Game Lifetime Value Prediction in WeChat (arXiv 2025)

- Source: arXiv 2506.11037 (WeChat)
- Detailed analysis: [2025_arXiv_GRePO-LTV_Mini-Game-Lifetime-Value-WeChat.md](./read-papers/2025_arXiv_GRePO-LTV_Mini-Game-Lifetime-Value-WeChat.md)

Payment over **3/7/30 days** after registration. Online avg LTV/GMV **+8.4%** (3d +9.9%, 7d +7.8%, 30d +7.73%). User–game pair, not slate.

### Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling (arXiv 2026)

- Source: arXiv 2604.25839 (Kuaishou)
- Detailed analysis: [2026_arXiv_OCARM_Distilling-Post-Conversion-User-Retention.md](./read-papers/2026_arXiv_OCARM_Distilling-Post-Conversion-User-Retention.md)

Teacher sees post-conversion onboarding; student predicts LT1/LT7/LT30 without leakage. Online LT30: re-engaged devices **+20.47% / +34.43%** (non-uninstalled / uninstalled). Analog of distilling post-match chat into pre-match ranking. User-level bidding, not item credit.

### Continuation (2026-08-17)

**CLTV embeddings** (WWW 2017, ASOS) — [card](./read-papers/2017_WWW_NA_Customer-Lifetime-Value-Prediction-Using-Embeddings.md). Session-log embeddings improve 12-month CLTV / churn over RF. User-level prediction, not item ranker.

**Cross-domain adaptive CLV** (advertising, 2021/2023) — [card](./read-papers/2021_arXiv_NA_Cross-Domain-Adaptive-Learning-Advertisement-CLV.md). 7-day consumption LTV; AUC +6.8–14.5% vs single-domain. Domain adaptation, not ranking fusion.

**Generative sequential notification optimization** (2025) — [card](./read-papers/2025_arXiv_NA_Generative-Sequential-Notification-Optimization.md). Multi-objective Decision Transformer for notification volume. **+0.72% sessions** vs CQL while sending fewer notes. Same family as Pinterest/Duolingo notify volume, not swipe LTV.

---

## 5. D5 — Multi-task cascades with long-horizon heads (7 papers)

### Entire Space Multi-Task Model (SIGIR 2018)

- Source: SIGIR 2018 (Alibaba)
- Detailed analysis: [2018_SIGIR_ESMM_Entire-Space-Multi-Task-Model.md](./read-papers/2018_SIGIR_ESMM_Entire-Space-Multi-Task-Model.md)

pCTCVR = pCTR × pCVR over all impressions. Public CVR AUC +2.56 abs vs BASE. **Canonical like → match → conversation chain.**

### Entire Space Multi-Task Modeling via Post-Click Behavior Decomposition (SIGIR 2020)

- Source: SIGIR 2020 (Alibaba)
- Detailed analysis: [2020_SIGIR_ESM2_Entire-Space-Post-Click-Behavior-Decomposition.md](./read-papers/2020_SIGIR_ESM2_Entire-Space-Post-Click-Behavior-Decomposition.md)

Decomposes post-click path. Online **+3% CVR vs ESMM**.

### AITM: Modeling Sequential Dependence for Audience Multi-step Conversion (KDD 2021)

- Source: KDD 2021 (Meituan)
- Detailed analysis: [2021_KDD_AITM_Sequential-Dependence-Multi-Step-Conversions.md](./read-papers/2021_KDD_AITM_Sequential-Dependence-Multi-Step-Conversions.md)

Information transfer along funnel steps. Online vs MLP: **+25.0% approval CR, +42.11% activation CR**. Sequential dependence for dating cascade.

### HM³: Hierarchically Modeling Micro and Macro Behaviors (SIGIR 2021)

- Source: SIGIR 2021 (Alibaba)
- Detailed analysis: [2021_SIGIR_HM3_Hierarchically-Modeling-Micro-Macro-Behaviors.md](./read-papers/2021_SIGIR_HM3_Hierarchically-Modeling-Micro-Macro-Behaviors.md)

Micro/macro/purchase graph. Online **+8.27% CVR, +8.32% GMV vs BASE**.

### ESCM²: Entire Space Counterfactual Multi-Task Model (SIGIR 2022)

- Source: SIGIR 2022 (Ant Group)
- Detailed analysis: [2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task.md](./read-papers/2022_SIGIR_ESCM2_Entire-Space-Counterfactual-Multi-Task.md)

IPS/DR regularizers on CVR. Online vs ESMM: **+2.84% orders, +10.85% premium**. Closest D5 paper to a **causal estimand**, still conversion not retention.

### Optimizing Airbnb Search Journey with Multi-task Learning (KDD 2023)

- Source: KDD 2023 (Airbnb)
- Detailed analysis: [2023_KDD_NA_Optimizing-Airbnb-Search-Journey-Multi-Task.md](./read-papers/2023_KDD_NA_Optimizing-Airbnb-Search-Journey-Multi-Task.md)

Chain-rule P(uncancelled booking) plus negative milestones (rejection, cancel). Stays online: **+0.61% uncancelled bookers**. Funnel with explicit negative heads — useful for unmatched/ignored likes.

### Continuation (2026-08-17)

**Multi-IPW / Multi-DR post-click CVR** (WWW 2020, Alibaba) — [card](./read-papers/2020_WWW_NA_Causal-Approaches-Debiasing-Post-Click-CVR-Multi-Task.md). MNAR click→conversion debiasing on ESMM. Ali-CCP Multi-DR CVR AUC 69.29 vs ESMM 68.56. **Causal CVR, not retention CATE.**

---

## 6. D6 — Uplift and incrementality inside ranking (7 papers)

Thin on purpose: industry swipe rankers in this corpus do **not** put CATE in the serving formula.

### Learning to Rank for Uplift Modeling (arXiv 2020)

- Source: arXiv 2002.05897 (VUB)
- Detailed analysis: [2020_arXiv_NA_Learning-to-Rank-for-Uplift-Modeling.md](./read-papers/2020_arXiv_NA_Learning-to-Rank-for-Uplift-Modeling.md)

Listwise LTR on RCT uplift. Hillstrom: ~4% incremental gains at 50% targeted. User-level campaign targeting, not item exposure.

### Rankability-enhanced Revenue Uplift Modeling (RERUM) (arXiv 2024)

- Source: arXiv 2405.15301 (Tencent FiT)
- Detailed analysis: [2024_arXiv_NA_Rankability-Enhanced-Revenue-Uplift-Modeling.md](./read-papers/2024_arXiv_NA_Rankability-Enhanced-Revenue-Uplift-Modeling.md)

ZILN + listwise uplift loss. Online LIFT@2 **+9.20 / +37.24 / +15.43%** across campaigns. Marketing allocation, not a feed ranker.

### Counterfactual Reciprocal Recommender Systems for User-to-User Matching (arXiv 2025)

- Source: arXiv 2508.01867 (Sony)
- Detailed analysis: [2025_arXiv_NA_Counterfactual-Reciprocal-Recommender-User-Matching.md](./read-papers/2025_arXiv_NA_Counterfactual-Reciprocal-Recommender-User-Matching.md)

IPS/SNIPS/DR for mutual acceptance under display bias. NDCG@10 +2.7% Synthetic; Coverage@10 +51%. Corrects **selection bias on pairs**, not retention uplift of showing B to A.

### Off-Policy Evaluation and Learning for Matching Markets (arXiv 2025)

- Source: arXiv 2507.13608 (Wantedly / Cornell)
- Detailed analysis: [2025_arXiv_NA_Off-Policy-Evaluation-Learning-Matching-Markets.md](./read-papers/2025_arXiv_NA_Off-Policy-Evaluation-Learning-Matching-Markets.md)

V(π) = expected mutual matches; DiPS/DPR beat IPS/DR under sparse replies. OPE for two-sided policies, not a training objective for LTV.

### Continuation (2026-08-17)

**AUUC-max treatment targeting** (2020) — [card](./read-papers/2020_arXiv_NA_Treatment-Targeting-AUUC-Maximization.md). Rank by CATE via AUUC with generalization bounds. Campaign targeting, not swipe ranking.

**E3IR cost-effective incentive uplift** (Tencent FiT, 2024) — [card](./read-papers/2024_arXiv_NA_End-to-End-Cost-Effective-Incentive-Uplift.md). Joint uplift + budget. Hillstrom-family AUUC/QINI; marketing incentives.

**ReAlloc multi-channel uplift** (2024/2026) — [card](./read-papers/2024_arXiv_NA_Multi-Channel-Uplift-Policy-Learning.md). Seller/product budget split. Online pay orders **+3.53%**. Marketplace *budget* uplift, not ranking a profile for a viewer.

These three thicken D6 without changing the 90-card conclusion: incrementality in this literature is still **campaign/budget allocation**, not a dating swipe formula.

---

## 7. D7 — Delayed feedback and revenue labels (10 papers)

### Modeling Delayed Feedback in Display Advertising (KDD 2014)

- Source: KDD 2014 (Criteo)
- Detailed analysis: [2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md](./read-papers/2014_KDD_DFM_Modeling-Delayed-Feedback-Display-Advertising.md)

p(x) and delay λ(x); 30-day window; last-click. NLL 0.3960 vs Naive 0.4076; Naive **underpredicts conversions 21%**. Template for subscription labels that arrive after ingest.

### Addressing Delayed Feedback for Continuous Training with Neural Networks in CTR prediction (RecSys 2019)

- Source: RecSys 2019 (Twitter)
- Detailed analysis: [2019_RecSys_NA_Addressing-Delayed-Feedback-Continuous-Training.md](./read-papers/2019_RecSys_NA_Addressing-Delayed-Feedback-Continuous-Training.md)

Fake-negative weighted loss vs DFM/PU. Online **+55% RPMq, +23% monetized CTR**. CTR delay, not retention.

### Delayed Feedback Modeling for the Entire Space Conversion Rate Prediction (AAAI 2021)

- Source: AAAI 2021 (Alibaba)
- Detailed analysis: [2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md](./read-papers/2021_AAAI_ESDF_Delayed-Feedback-Entire-Space-CVR.md)

7-day window; day-slot delay probabilities. Public AUC 0.7811 vs ESMM 0.7679.

### Counterfactual Reward Modification for Streaming Recommendation with Delayed Feedback (SIGIR 2021)

- Source: SIGIR 2021 (Renmin / Tencent)
- Detailed analysis: [2021_SIGIR_NA_Counterfactual-Reward-Modification-Delayed-Feedback.md](./read-papers/2021_SIGIR_NA_Counterfactual-Reward-Modification-Delayed-Feedback.md)

R = λ·click + (1−λ)·w·Y; w corrects censored conversions. ~70% of WeChat coupon conversions delayed past collection day. Unbiased delayed **reward**, not full LTV incrementality.

### Asymptotically Unbiased Estimation for Delayed Feedback Modeling via Label Correction (WWW 2022)

- Source: WWW 2022 (Alibaba)
- Detailed analysis: [2022_WWW_DEFUSE_Asymptotically-Unbiased-Delayed-Feedback.md](./read-papers/2022_WWW_DEFUSE_Asymptotically-Unbiased-Delayed-Feedback.md)

IP/FN/RN/DP types; 1-day Taobao / 30-day Criteo windows. Online **+2.28% CVR**.

### Continuation (2026-08-17)

**DEFER** (KDD 2021, Alibaba) — [card](./read-papers/2021_KDD_DEFER_Delayed-Feedback-Modeling-Real-Negatives.md). Brief seed, previously unverified in this workplace. Duplicate **real negatives** (never-convert within \(w_2\)) so \(q(x)=p(x)\) under continuous training; IS loss with fake-negative classifier. Criteo AUC 0.8394 (RI-AUC 90% of Oracle); online **>6% CVR** in several Alibaba scenarios. Direct recipe for match/reply labels that mature after ingest.

**FSIW** (WWW 2020) — [card](./read-papers/2020_WWW_FSIW_Feedback-Shift-Correction-Delayed-CVR.md). Importance-weighted ERM for delayed CVR. Criteo LR-FSIW LL 0.3928 vs DFM 0.3989.

**TS-DL** (IJCAI 2020, JD) — [card](./read-papers/2020_IJCAI_TS-DL_Attention-Delayed-Feedback-Post-Click.md). Attention + day-slot hazard. RelaImpr vs DIN up to +44.76% on one wait-period split.

**DLA-DF** (SIGIR 2020) — [card](./read-papers/2020_SIGIR_DLA-DF_Dual-Learning-Algorithm-Delayed-Conversions.md). PU+MNAR dual learning. CyberAgent co-author; still conversion prediction.

**Many conversions per click** (Google, 2021) — [card](./read-papers/2021_arXiv_NA_Handling-Many-Conversions-Per-Click-Delayed-Feedback.md). Poisson count/value per click, not first-conversion-only. Log-loss −8.6% vs mature-only. Relevant if a-la-carte revenue can fire more than once per impression.

---

## 8. D8 — Two-sided / reciprocal markets (22 papers)

None of these make retention or subscription LTV the ranking loss. They constrain whatever unified scorer you train.

### Hinge Employs New Algorithm to Find Your “Most Compatible” Match (TechCrunch, 2018)

- Source: TechCrunch; Hinge
- Detailed analysis: [2018_TechCrunch_NA_Hinge-Most-Compatible-Gale-Shapley.md](./read-papers/2018_TechCrunch_NA_Hinge-Most-Compatible-Gale-Shapley.md)

Gale–Shapley on learned like/pass preferences; success proxy = phone-number exchange. Users **8× more likely to go on dates** vs other Hinge recs (company-reported via TechCrunch). Credit/incrementality not specified.

### Learning Hiring Preferences: The AI Behind LinkedIn Jobs (LinkedIn Engineering, 2019)

- Source: LinkedIn Engineering blog
- Detailed analysis: [2019_Blog_NA_Learning-Hiring-Preferences-LinkedIn-Jobs.md](./read-papers/2019_Blog_NA_Learning-Hiring-Preferences-LinkedIn-Jobs.md)

Hirer Message/Archive/Skip → term weights. Offline NDCG@1 +49.61%. Two-sided jobs, real-time, no delay model.

### Powering Tinder — The Method Behind Our Matching (Tinder, 2019)

- Source: Tinder blog
- Detailed analysis: [2019_Blog_NA_Powering-Tinder-Method-Behind-Matching.md](./read-papers/2019_Blog_NA_Powering-Tinder-Method-Behind-Matching.md)

Concurrent activity as primary signal; Likes/Nopes. Gains not specified. Operational, not LTV.

### How Coffee Meets Bagel leverages data and AI for love (CIO Dive, 2019)

- Source: CIO Dive
- Detailed analysis: [2019_CIODive_NA_Coffee-Meets-Bagel-Data-AI-Matching.md](./read-papers/2019_CIODive_NA_Coffee-Meets-Bagel-Data-AI-Matching.md)

Explicitly rejects likes/time-on-app as success; nine blended models; daily batch. No retention/revenue model in source.

### Managing Diversity in Airbnb Search (KDD 2020)

- Source: KDD 2020 (Airbnb)
- Detailed analysis: [2020_KDD_NA_Managing-Diversity-Airbnb-Search.md](./read-papers/2020_KDD_NA_Managing-Diversity-Airbnb-Search.md)

Second-stage diversity vs booking. Query-context LSTM: bookings **+0.44%**, new-guest +0.61%. Congestion cousin on listings, not people.

### Reciprocal Recommender Systems: Analysis of State-of-Art Literature (Information Fusion, 2021)

- Source: arXiv 2007.16120
- Detailed analysis: [2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md](./read-papers/2021_InfoFusion_NA_Reciprocal-Recommender-Systems-Survey.md)

Field survey: p(x↔y)=φ(p(x,y),p(y,x)). Incrementality not discussed.

### A/B Testing for Recommender Systems in a Two-sided Marketplace (NeurIPS 2021)

- Source: arXiv 2106.00762 (LinkedIn UniCoRn)
- Detailed analysis: [2021_NeurIPS_UniCoRn_AB-Testing-Two-Sided-Marketplace.md](./read-papers/2021_NeurIPS_UniCoRn_AB-Testing-Two-Sided-Marketplace.md)

Post-hoc experiment layer for producer-level ATE. Ranking-model experiment: +0.13% WAU. **Q6:** user-split A/Bs are not enough.

### Interference, Bias, and Variance in Two-Sided Marketplace Experimentation (2022)

- Source: arXiv 2104.12222 (Stanford)
- Detailed analysis: [2022_WWW_NA_Interference-Bias-Variance-Two-Sided-Marketplace.md](./read-papers/2022_WWW_NA_Interference-Bias-Variance-Two-Sided-Marketplace.md)

CR relative bias near 0 to ~80% depending on load. 50-50 allocation near variance-optimal. Incrementality of GTE, not a ranker.

### Matching Theory-based Recommender Systems in Online Dating (arXiv 2022)

- Source: arXiv 2208.11384 (CyberAgent MTRS)
- Detailed analysis: [2022_arXiv_NA_Matching-Theory-Recommender-Online-Dating.md](./read-papers/2022_arXiv_NA_Matching-Theory-Recommender-Online-Dating.md)

Choo–Siow TU equilibrium μ with capacity √μ_x,0√μ_y,0. Claims less like-concentration vs fusion; production % not specified.

### Automated Decision Making at Grindr (Grindr, 2023)

- Source: Grindr blog
- Detailed analysis: [2023_Blog_NA_Automated-Decision-Making-Grindr.md](./read-papers/2023_Blog_NA_Automated-Decision-Making-Grindr.md)

**States no ranking model for discovery.** Security/moderation only. Negative control: not all dating apps unify LTV ranking.

### Fast and Examination-agnostic Reciprocal Recommendation in Matching Markets (RecSys 2023)

- Source: RecSys 2023 (CyberAgent)
- Detailed analysis: [2023_RecSys_NA_Fast-Examination-Agnostic-Reciprocal-Recommendation.md](./read-papers/2023_RecSys_NA_Fast-Examination-Agnostic-Reciprocal-Recommendation.md)

TU market-clearing; n=200: 332.91 expected matches vs Naive 219.56; reactive Gini 0.1019 vs 0.3872. Social welfare, not retention.

### Reciprocal Sequential Recommendation (RecSys 2023)

- Source: arXiv 2306.14712
- Detailed analysis: [2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md](./read-papers/2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md)

Bilateral BPR + distillation. Recruitment HR@5 0.4435 vs DPGNN 0.2422. Prediction only.

### Managing Congestion in Two-Sided Platforms: The Case of Online Rentals (arXiv 2023)

- Source: arXiv 2308.14703
- Detailed analysis: [2023_arXiv_NA_Managing-Congestion-Two-Sided-Platforms.md](./read-papers/2023_arXiv_NA_Managing-Congestion-Two-Sided-Platforms.md)

Top 20% of rooms ~100% of requests. Modest mix of random ranking (α<0.1) matches utility with less congestion. Structural, not an ML ranker.

### Model-based Recall in Momo Social Recommendation (InfoQ, 2024)

- Source: InfoQ (Momo)
- Detailed analysis: [2024_InfoQ_NA_Model-based-Recall-Momo-Social-Recommendation.md](./read-papers/2024_InfoQ_NA_Model-based-Recall-Momo-Social-Recommendation.md)

U2I/U2U2I recall: interaction conversion **+15%+**; GCN social matching **+10%+**. Short-horizon matching, not LTV.

### Fair Reciprocal Recommendation in Matching Markets (RecSys 2024)

- Source: RecSys 2024 (CyberAgent)
- Detailed analysis: [2024_RecSys_NA_Fair-Reciprocal-Recommendation-Matching-Markets.md](./read-papers/2024_RecSys_NA_Fair-Reciprocal-Recommendation-Matching-Markets.md)

NSW vs social-welfare ranking under envy-freeness. Real log-examination: NSW 90.39 matches vs SW 111.37; male envy **31 vs 434**. Match-count vs fairness trade-off is measured; retention is not.

### Online Reciprocal Recommendation with Theoretical Performance Guarantees (WWW 2024 / arXiv 1806.01182)

- Source: arXiv 1806.01182
- Detailed analysis: [2024_WWW_NA_Online-Reciprocal-Recommendation-Performance-Guarantees.md](./read-papers/2024_WWW_NA_Online-Reciprocal-Recommendation-Performance-Guarantees.md)

SMILE clusterable matching; Θ(M) matches with theoretical T. Binary preferences; no LTV.

### CUPID: A Real-Time Session-Based Reciprocal Recommendation System (arXiv 2024)

- Source: arXiv 2410.18087 (Hyperconnect Azar)
- Detailed analysis: [2024_arXiv_CUPID_Session-Based-Reciprocal-Recommendation.md](./read-papers/2024_arXiv_CUPID_Session-Based-Reciprocal-Recommendation.md)

Predict log chat duration; **switchback** because of a shared pool. Online chat duration **+6.8% / +5.9%** (warm/cold). Immediate interaction quality, not retention. Switchback is the dating-relevant eval design.

### Revisiting Reciprocal Recommender Systems: Metrics, Formulation, and Method (arXiv 2024)

- Source: arXiv 2408.09748 (CRRS)
- Detailed analysis: [2024_arXiv_NA_Revisiting-Reciprocal-Recommender-Systems.md](./read-papers/2024_arXiv_NA_Revisiting-Reciprocal-Recommender-Systems.md)

Potential outcomes for bilateral assignments; CRecall/SRecall/RNDCG. Dating CRecall@50 0.3387 vs BPRMF 0.2795. Pair-level causal **match**, not delayed retention.

### Continuation (2026-08-17)

**Tinder Geosharded Recommendations Part 1** (Tech Blog, 2019) — [card](./read-papers/2019_Blog_NA_Geosharded-Recommendations-Tinder.md). Match Group primary source beyond the 2019 matching essay. S2 geo-index; **20×** computations vs single ES index. **Low project relevance** for the ranking objective: retrieval infra, no LTV/retention labels. Does show dense-city hot shards (congestion at serve time).

**TSPR** (2025) — [card](./read-papers/2025_arXiv_NA_Two-Sided-Prioritized-Ranking-Marketplace-Experiments.md). Coherency-preserving two-sided experiment design so ranking A/Bs identify a global treatment effect. Eval-layer complement to UniCoRn / CUPID switchback.

**ECDA** (2026) — [card](./read-papers/2026_arXiv_NA_Integrating-Predictive-Models-Two-Sided-Matching.md). Matching-theoretic integrator on top of production GBTs (AUC 0.80–0.92) for a dating-like market (CoupLink). Simulation: fewer total dates but better effective dates / receiver-side probability. **Capacity-aware second stage**, still not D7 LTV.

**Airbnb guest preferences / two-sided marketplace** (2026) — [card](./read-papers/2026_arXiv_NA_Understanding-Guest-Preferences-Two-Sided-Airbnb.md). IV price elasticity when experiments are impractical. Two-sided demand, not a swipe ranker.

---

## 9. D9 — Generative / reward-model rankers (5 papers)

Optional family. They unify retrieve+rank with a learned reward, still correlational.

### Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers (ICML 2024)

- Source: ICML 2024 (Meta HSTU)
- Detailed analysis: [2024_ICML_HSTU_Actions-Speak-Louder-Generative-Recommendations.md](./read-papers/2024_ICML_HSTU_Actions-Speak-Louder-Generative-Recommendations.md)

Generative recommenders; multi-task NE on engagement/consumption. Online 12.4% E-Task win. Next-action prediction, not incrementality.

### MTGR: Industrial-Scale Generative Recommendation Framework in Meituan (arXiv 2025)

- Source: arXiv 2505.18654 (Meituan)
- Detailed analysis: [2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md](./read-papers/2025_arXiv_MTGR_Industrial-Scale-Generative-Recommendation-Meituan.md)

Token-sequence CTR/CTCVR. Online PV_CTR +1.31%, UV_CTCVR +1.22%. No retention objective in the loss.

### OneRec: Unifying Retrieve and Rank with Generative Recommender and Preference Alignment (arXiv 2025)

- Source: arXiv 2502.18965 (Kuaishou)
- Detailed analysis: [2025_arXiv_OneRec_Unifying-Retrieve-Rank-Generative-Recommender.md](./read-papers/2025_arXiv_OneRec_Unifying-Retrieve-Rank-Generative-Recommender.md)

Autoregressive semantic IDs + DPO. Online **+1.68% Total Watch Time, +6.56% Average View Duration**. Session generative targets, not delayed LTV credit.

### OneRec Technical Report (arXiv 2025)

- Source: arXiv 2506.13695 (Kuaishou)
- Detailed analysis: [2025_arXiv_OneRec_Technical-Report-Generative-Recommender.md](./read-papers/2025_arXiv_OneRec_Technical-Report-Generative-Recommender.md)

RSFT on play duration; RL with P-Score reward model. Ablation: up to +5.84% Watch Time, +1.82% App Stay Time. Reward model is T1 fusion inside a generative policy.

### GenRec: An LLM-Backed Recommendation Ranker at Netflix (arXiv 2026)

- Source: arXiv 2608.10257 (Netflix)
- Detailed analysis: [2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker-Netflix.md](./read-papers/2026_arXiv_GenRec_LLM-Backed-Recommendation-Ranker-Netflix.md)

Ranking CE weighted by reward models of how short-term events **correlate** with long-term outcomes. Online **+0.115% short-term engagement, +0.006% long-term core metric**. Source states correlational proxies, not causal incrementality of one title.

---

## Comparison table of all 120 references

Columns: title (short), company/authors, year, source type, direction, objective / label / horizon, prediction vs incrementality, credit assignment, reported gains (short), dating applicability (short). Gains are only those **stated on the card**. “n.s.” = not specified in source.

| Title | Company / authors | Year | Type | Dir | Objective / label / horizon | Pred vs inc | Credit | Gains (short) | Dating applicability |
|-------|-------------------|------|------|-----|-----------------------------|-------------|--------|---------------|----------------------|
| Modeling Delayed Feedback in Display Advertising | Criteo (Chapelle) | 2014 | industry | D7 | pCVR + delay λ; 30d last-click | Pred | Click→conversion ID, last-click | NLL 0.396 vs 0.408; Naive −21% conversions | Sub delay/censoring; not two-sided |
| Returning is Believing | Yahoo/Etsy/UVA | 2017 | academic | D2 | Click + return-time future clicks; horizon T | Pred+bandit | Per-round article; return scales future rounds | ~2× CTR; ~1.8× return vs GLM-UCB | Return-time reward analog; one-sided |
| Understanding Dwell Time (LinkedIn Feed) | LinkedIn | 2018 | blog | D1 | P(skip) + action/downstream/upstream heads | Pred | Pointwise impression | Skip AUC +10%; online time spent ↑ (no %) | Dwell as negative like; no reciprocity |
| Notification Volume Control at Pinterest | Pinterest | 2018 | industry | D4 | Weekly DAU vs unsub vs week-4 post-unsub | Pred; optimizer uses Δp | User-week budget, not item | Email&Push DAU +3%; CTR +10–21% | Re-engagement volume; not swipe LTV |
| Entire Space Multi-Task Model (ESMM) | Alibaba | 2018 | industry | D5 | CTR×CVR entire impression space | Pred | Pointwise funnel | CVR AUC +2.56 abs public | Like→match chain; SSB |
| Hinge Most Compatible (Gale–Shapley) | Hinge / TechCrunch | 2018 | blog | D8 | “Hit it off”; phone-number proxy | n.s. | n.s. | 8× dates vs other recs (reported) | Reciprocal matching; not LTV |
| DRN news RL | PSU / MSRA | 2018 | academic | D2 | Click + β activeness; γ=0.4 | Q-learning | Per-request news | Online CTR 0.0113 best in table | Return survival analog; one-sided |
| LinkedIn Jobs hiring preferences | LinkedIn | 2019 | blog | D8 | Real-time Message/Archive/Skip | Pred | Term-count dot product | NDCG@1 +49.61% offline | Two-sided jobs; no delay |
| Powering Tinder matching | Tinder | 2019 | blog | D8 | Match potential; Likes/Nopes; concurrent activity | n.s. | n.s. | n.s. | Dating ops; not unified LTV |
| Coffee Meets Bagel data/AI | CMB | 2019 | blog | D8 | Offline connection, not likes/time | Pred (blended) | Daily batch n.s. | Control KPI qualitative | Rejects vanity proxies |
| SlateQ | Google | 2019 | industry | D2 | Engagement/watch; YouTube LTV cap N days | Pred Q+pCTR | RTDS consumed-item Q | Live +0.5% d1 to >+1% d20 | One-act-per-slate; add Q-head |
| The Surrogate Index | Athey et al. | 2019 | academic | D3 | Long-run Y from short S; GAIN 36 quarters | **Inc (ATE)** | n/a (estimator) | Index 0.061 vs naive 0.117 vs 0.064 | Eval layer for 90d retention |
| YouTube MMoE watch-next | Google | 2019 | industry | D1 | Engagement + satisfaction heads | Pred | Pointwise | +0.20–0.45% eng; +1.22–3.07% sat | Multi-head fusion template |
| Delayed feedback continuous CTR | Twitter | 2019 | industry | D7 | Click/conv with incomplete labels | Pred | Per-impression delay loss | +3% RCE; online +55% RPMq | Label delay; not retention |
| Pareto-efficient e-comm LTR | Alibaba/Kwai | 2019 | industry | D1 | CTR vs GMV scalarization | Pred | Pointwise | CTR–GMV r=−0.343; % n.s. | Revenue vs engagement conflict |
| Top-K Off-Policy REINFORCE | Google | 2019 | industry | D2 | Discounted trajectory return | Policy | Sequence R_t | K=16 avoids −0.66% ViewTime | Off-policy RL; not two-sided |
| Value-aware profit RL | Alibaba | 2019 | industry | D2 | Page GMV; XVR×price | Pred/policy | Page-level sum | Online GMV +6.8% vs DNN-LTR | Revenue RL; one-sided e-comm |
| ZILN LTV | Google | 2019 | industry | D4 | 1–3y spend, zero-inflated | Pred | User-level | Spearman +24–48% vs MSE | **Revenue head loss** |
| MoSE activity streams | Google | 2020 | industry | D1 | Next-day activity counts | Pred | Sequence last-day | GMail +4.8% AUC tradeoff | User state; not item LTV |
| Managing Diversity Airbnb Search | Airbnb | 2020 | industry | D8 | Booking + diversity surrogates | Pred | Pairwise booked-vs-shown | Bookings +0.44% | Listing congestion analog |
| Sleeping recovering bandit notifications | Duolingo | 2020 | industry | D4 | Lesson in 2h; D1/D7 | Bandit lift | One template → 2h outcome | D1/D7 +2.0–2.2% | Notify retention; not ranking |
| RAM recommend+advertise | ByteDance/MSU | 2020 | academic | D1 | Session dwell vs ad revenue | Policy | Session timestep | Rrev +16.42% vs DRQN | Dual objective; not dating |
| ESM² post-click decomposition | Alibaba | 2020 | industry | D5 | Decomposed post-click CVR | Pred | Pointwise funnel | Online +3% CVR vs ESMM | Richer cascade |
| NICF | Tsinghua/JD | 2020 | academic | D2 | Rating reward; 40 steps | Q | Pointwise TD | P@40 +4.6–9.4% sim | No retention |
| Stochastic label aggregation | Amazon | 2020 | industry | D1 | Relevance vs 6w–2mo purchase | Pred | Query-level coin | NDCG@5 0.493 vs 0.395 | Multi-obj labels |
| Learning to Rank for Uplift | VUB | 2020 | academic | D6 | CATE; AUUC | **Inc** | User RCT | ~4% inc. at 50% targeted | Campaign LTR; not swipe |
| ESDF delayed entire-space CVR | Alibaba | 2021 | industry | D7 | CVR 7d; delay slots | Pred | Click-time features | AUC 0.781 vs ESMM 0.768 | Delay+funnel |
| Reciprocal RS survey | Granada et al. | 2021 | academic | D8 | φ(p_xy, p_yx) | Pred (survey) | n.s. | Synthesized only | Field map |
| AITM multi-step conversion | Meituan | 2021 | industry | D5 | Sequential funnel CRs | Pred | Per-banner steps | Online +25% / +42% CR | Cascade transfer |
| UniCoRn two-sided A/B | LinkedIn | 2021 | industry | D8 | Producer ATE of ranking | **Inc** | Position attention | Ranking +0.13% WAU | Two-sided experiments |
| HM³ micro/macro CVR | Alibaba | 2021 | industry | D5 | Graph CVR | Pred | Impression nodes | Online +8.27% CVR / +8.32% GMV | Funnel graph |
| CBDF delayed reward | Tencent/Renmin | 2021 | industry | D7 | λ click+(1−λ) weighted Y | Unbiased delayed R | Per (ctx,item) | Beats DFM-S on WeChat coupons | Censored conv reward |
| URL auxiliary REINFORCE | Google | 2021 | industry | D2 | RL return + click/dwell aux | Pred aux | Item reward; zeros on non-click | Enjoyment +0.12% | Aux heads first |
| DASI dynamic surrogate | Microsoft Research | 2021 | academic | D3 | M-period Y adj for future T | **Inc** | Customer-period | Unadjusted overestimates (sim) | Overlapping campaigns |
| Billion-user LTV Kuaishou | Kuaishou | 2022 | industry | D4 | ltv 30/90/180/365 | Pred; ROI in A/B | User-level | ROI +11.9–14.7% | Multi-horizon LTV labels |
| BatchRL-MTF | Tencent | 2022 | industry | D1 | Session dwell via fusion weights; γ=0.95 | Policy on fusion | Per-step in session | ADTime +2.55%; UPI +9.65% | **Keep heads, learn blend** |
| PinnerFormer | Pinterest | 2022 | industry | D4 | 14–28d future engagement | Pred | User embedding | Homefeed repins +2.5% | Future-window user tower |
| ESCM² | Ant Group | 2022 | industry | D5 | CVR with IPS/DR | Pred+CRM | Exposure IPS | Orders +2.84%; premium +10.85% | Causal CVR, not retention |
| DEFUSE delayed labels | Alibaba | 2022 | industry | D7 | CVR; 1d/30d windows | Pred | Click-time x; DP inject | Online +2.28% CVR | Censoring types |
| Two-sided experiment interference | Stanford | 2022 | academic | D8 | GTE bookings | **Inc** | Group CR/LR | Bias 0–~80% | Do not user-split blindly |
| MTRS matching theory dating | CyberAgent | 2022 | industry | D8 | Choo–Siow μ; MF likes | Pred equilibrium | Market allocation | Concentration ↓ (no % in source) | Dating TU overlay |
| Instagram Explore scaling | Meta | 2023 | blog | D1 | VM over click/like/see-less | Pred | Per-item EV | n.s. | Value-model cousin |
| Immersive feed MTL | Google | 2023 | industry | D1 | Watch/like/comment/share | Pred | Impression + trail bias | Enjoyment +1.96% trail | Sparse-head co-train |
| Impatient Bandits | Spotify | 2023 | industry | D3 | 60d stickiness from daily z_k | Pred traces | Show-level bandit | 50% var by d8; sim > delayed | Cold-start before LTV matures |
| Airbnb Journey Ranker | Airbnb | 2023 | industry | D5 | Uncancelled book; chain + negatives | Pred | Search-list milestones | Uncancelled bookers +0.61% | Funnel + reject/cancel |
| Fast TU reciprocal rec | CyberAgent | 2023 | academic | D8 | Expected matches μ* | Pred | Market equilibrium | 332.91 vs Naive 219.56 (n=200) | Congestion overlay |
| ReSeq reciprocal sequential | RUCAIBox | 2023 | academic | D8 | Bilateral match BPR | Pred | Pair | HR@5 0.44 vs DPGNN 0.24 | Reciprocal seq; not LTV |
| RLUR | Kuaishou | 2023 | industry | D2 | Min return time; D1/D7 eval | Policy | Session-end; 8 weight actor | +0.45% opens; +0.063% D7 | **Retention as RL objective** |
| TSCAC | Kuaishou | 2023 | industry | D2 | WatchTime s.t. sparse interactions | Policy | Step vector reward | WT +0.379%; Comment −0.619% | Dense vs sparse trade-off |
| Netflix 200-test surrogate | Netflix | 2023 | industry | D3 | 14d auto-surrogate vs 63d | **Inc (TE)** | User-day Y | ~95% decision agree; rec 65% | Ship gate for ranking A/Bs |
| Managing congestion rentals | academic | 2023 | academic | D8 | Utility vs request concentration | Structural CF | n/a | Top 20% rooms ~100% requests | Popularity congestion |
| Spotify long-term audio RL | Spotify | 2023 | industry | D2 | 60d stickiness × clickiness | Q vs incumbent | Item habit state Z | Banner +81% 60d min (impacted) | Keep CTR head; add stickiness |
| Pareto optimal proxy metrics | Google | 2023 | industry | D3 | DAU direction vs sensitivity | **Inc (TE)** | Experiment-level | 8.5× sensitivity; rec 72% vs 40% | Launch-metric weights |
| Grindr automated decisions | Grindr | 2023 | blog | D8 | No discovery ranker | n/a | n/a | n.s. | Negative: not all apps rank |
| LinkedIn long dwell v2 | LinkedIn | 2024 | blog | D1 | Cluster-normalized long dwell + skip | Pred | Request MOO | Positive dwell (no % in text) | Long-dwell head |
| Snap UUM | Snap | 2025 | blog | D4 | Next-k events; 1y history | Pred | User embedding | n.s. | Cross-funnel user tower |
| HSTU generative rec | Meta | 2024 | industry | D9 | Next engagement/consumption | Pred | Autoregressive | 12.4% E-Task online | Sequence backbone |
| Momo model-based recall | Momo | 2024 | blog | D8 | Scene interactions | Pred | Pair/graph | Matching rate +10%+ | Social recall; not LTV |
| FID / ItemA2C | Kuaishou | 2024 | industry | D2 | List reward; 1w online; DAU/retention | Policy | Weighted V(s') per item | Retention +0.016%; WT +0.129% | **Item credit for delayed V** |
| GFN4Retention | Kuaishou | 2024 | industry | D2 | Terminal return frequency + r_t | Policy/flow | Backward flow per step | Beats RLUR (exact % n.s.) | Retention attribution |
| LiRank | LinkedIn | 2024 | industry | D4/D1 | Like/comment/dwell; Jobs apply | Pred | Pointwise | Feed sessions +0.5%; Jobs +1.76% | Aux heads + long dwell + explore |
| MO-LTR distillation | Airbnb | 2024 | industry | D1 | Booking + teacher soft labels | Pred | Listwise search | Booking +0.37% | Distill extra objectives |
| Choosing a Proxy Metric | Google | 2024 | industry | D3 | North-star TE via composite proxy | **Inc** | Experiment portfolio | Quality 0.302 vs aux 0.258 | Weight match/reply/return |
| Trinity long-term interests | ByteDance | 2024 | industry | D1 | Watch>10s; AAD surrogate | Pred | Cluster histograms | WT +0.118%; AAD +0.008% | Long seq; weak credit |
| Fair Reciprocal NSW | CyberAgent | 2024 | academic | D8 | Matches s.t. envy-free | Pred | Market ranking | NSW 90.4 vs SW 111.4 matches | Fairness vs matches |
| LOPE (WWW paper) | Spotify | 2024 | industry | D3 | Week-3 streams from week-1 s | **Inc (OPE)** | Policy value | MSE −9–15% vs DR | Offline long-term policy eval |
| Online reciprocal guarantees | academic/Google | 2024 | academic | D8 | Mutual matches M_T | Pred | Round pairwise | Theory Θ(M); I-SMILE > random | Not LTV |
| AURO | Kuaishou/NTU | 2024 | industry | D2 | Return-time episode reward | Policy | Last-step retention | 7d ret +0.138‰ vs RLUR | Adaptive retention RL |
| CUPID Azar | Hyperconnect | 2024 | industry | D8 | Log chat duration | Pred | Pair | Duration +6.8% warm; switchback | Reciprocal quality; switchback |
| RERUM revenue uplift | Tencent FiT | 2024 | industry | D6 | CATE on revenue; 1mo sales | **Inc** | User RCT | LIFT@2 +9–37% | Marketing, not swipe |
| CRRS reciprocal metrics | academic | 2024 | academic | D8 | Match r_ij; bilateral treatments | Causal pair | Pair potential outcomes | CRecall@50 0.339 vs 0.280 | Bilateral causal match |
| Spotify LOPE blog | Spotify | 2024 | blog | D3 | Same as LOPE WWW | **Inc** | n.s. | 36% MSE vs DR at n=200 (sim) | Same as LOPE |
| CC-OR-Net LTV | Meituan | 2025 | academic | D4 | Nonneg LTV; ordinal buckets | Pred | User-level | Gini 0.803 | Whale revenue; no item credit |
| GRePO-LTV WeChat | WeChat/HKUST | 2025 | industry | D4 | Pay 3/7/30d post-reg | Pred | User–game | LTV/GMV +8.4% | Multi-horizon pay labels |
| MTGR Meituan | Meituan | 2025 | industry | D9 | CTR/CTCVR tokens | Pred | Pointwise | PV_CTR +1.31% | Generative CTR; not LTV |
| Counterfactual reciprocal | Sony | 2025 | academic | D6 | Mutual accept; IPS/DR | Pred debiased | Pair display | NDCG@10 +2.7%; Cov +51% | Display bias, not retention |
| Twitch delayed-signal MOR | Twitch/Prime | 2025 | industry | D1 | SMP/LMP + 14d chat/follow/spend | Pred | Impression; 14d agg | DAV +0.09%; ARPU +0.56% | **Delayed spend head** |
| DiPS matching OPE | Wantedly | 2025 | academic | D6 | Expected mutual matches | OPE | Scout/reply tuples | Lower MSE than IPS/DR | Two-sided OPE |
| Save Revisit Retain | Pinterest | 2025 | industry | D1 | Save→7d revisit | Pred surrogate | Item via Pin+user join | AU +0.10%; time +0.39% | 7d item-level surrogate |
| OneRec technical report | Kuaishou | 2025 | industry | D9 | Play-duration RSFT + P-Score RL | Pred/policy | Generated item in session | WT up to +5.84% (ablation) | Reward-model unification |
| OneRec unify retrieve-rank | Kuaishou | 2025 | industry | D9 | Semantic IDs + DPO | Pred | Session list | WT +1.68%; AVD +6.56% | Later-stage unify |
| PROXIMA | RIT | 2026 | academic | D3 | Proxy reliability + fragility | Decision audit | n/a | KuaiRec fragility 68% | Segment sign-flip audit |
| UniROM / EGA-V1 | ads research | 2025 | industry | D1 | Click pretrain; revenue RLAF | Pred+slate RL | Marginal ad revenue | RPM +13.6% | Ads LTV ≠ dating LTV |
| xMTF | Kuaishou | 2025 | industry | D1 | Daily watch time via MFC fusion | Policy on fusion | Session MDP | Watch +0.833% vs UNEX-RL | Formula-free blend |
| GenRec Netflix | Netflix | 2026 | industry | D9 | Rank CE × long-term reward models | Pred (stated correlational) | Request-level | +0.115% ST; +0.006% LT core | Reward-weighted LTR |
| Evaluating for the Long Term | 15 platforms | 2026 | workshop | D3 | Surrogacy playbook | **Inc** | n/a | Netflix 95%; sign flips in monetization | **Success paradox class** |
| Downstream rewards learning | Pinterest | 2026 | industry | D1 | Retention-correlated session heads | Pred | Session behaviors | SS +0.24–0.48% | Staged aux-head migration |
| Video ranking LTV framework | Alibaba | 2026 | industry | D1 | PDQ / attributed time / author LTV | Pred | Multi-signal attribution | LT3 +0.21%; VV +2.49% PDQ | Delayed LTV heads |
| OCARM post-conversion distill | Kuaishou | 2026 | industry | D4 | LT1/LT7/LT30 revisit | Pred | User bidding | LT30 +11.55% / +22.18% | Distill post-match into rank |
| PRL-PUTS | Pinterest | 2026 | industry | D1 | One-step Repin/P2P weights | Policy γ=0 | Request top-k | SS +0.13%; Repin +0.66% | Learned VM weights |
| UnifiedRL (IntegratedRL-MTF) | Tencent | 2024 | industry | D1 | Session reward via fusion weights | Policy | User-state actor | +4.64% consumption; +1.74% duration vs ES | BatchRL-MTF successor |
| EnhancedRL | Tencent | 2024 | industry | D1 | Same + enhanced user–item state | Policy | Per pair | +3.84% consumption vs UnifiedRL | Next MTF stage |
| Pinterest MTL calibration blog | Pinterest | 2020 | blog | D1 | Utility over action heads | Pred | Impression | Video mix +40% | Value-model cousin |
| Instagram Explore VM (2021) | Meta | 2021 | blog | D1 | Weighted like/save vs negative | Pred | Grid item | n.s. | Same VM as 2023 post |
| Netflix LTV reward blog | Netflix | 2024 | blog | D1 | Proxy reward; delayed-feedback preds | Pred | User–item proxy r | n.s. | RecSys 2023 public write-up |
| GMV mutual-influence ranking | Alibaba | 2018 | industry | D1 | Slate GMV | Pred | Within-slate | AUC 0.724→0.774 | Slate congestion analog |
| SORT-Gen list rerank | Taobao | 2025 | industry | D1 | List click/order/GMV | Pred | List-level | +9.61% click; +13.67% GMV | Generative rerank |
| MTFM | Meituan | 2025 | industry | D1 | CTR/CTCVR foundation | Pred | Exposure | HP CTR GAUC 0.6954 | Backbone not LTV |
| SEC retention cloning | Kuaishou | 2025 | industry | D2 | Clone high-retention trajectories | Policy | Trajectory | Active Days +0.098% | Imitation vs RLUR |
| KuaiSim | academic/Kuaishou | 2023 | academic | D2 | Simulator return module | Sim | Session | L-reward 4.042 ListCVAE | Tooling |
| EDT4Rec | CSIRO/UNSW | 2024 | academic | D2 | Click RTG DT | Policy | Relabeled RTG | Recall 31.26 vs 30.32 | Click RL |
| Netflix proxy-metrics blog | Netflix | 2024 | blog | D3 | TC/JIVE on historical A/Bs | **Inc (TE)** | Experiment | n.s. in blog | Launch-gate recipe |
| Covariance of TEs (KDD 2024) | Netflix | 2024 | industry | D3 | Cov(τ_S, τ_Y) | **Inc** | Experiment | TC/JIVE ≪ OLS bias (sim) | Same as blog |
| Proximal Surrogate Index | academic | 2026 | academic | D3 | Long-run Y under confounding | **Inc** | Unit | Closer to RCT earnings | Leaky D7→D30 |
| CLTV embeddings | ASOS | 2017 | industry | D4 | 12-month net sales / churn | Pred | User | Churn AUC ↑ vs RF | User LTV |
| Cross-domain ad CLV | academic+ads | 2021 | academic | D4 | 7d consumption | Pred | User | AUC +6.8–14.5% | Not ranking |
| Gen. sequential notifications | industry | 2025 | industry | D4 | Multi-obj notify DT | Policy | User episode | Sessions +0.72% | Notify not swipe |
| Multi-IPW/DR CVR | Alibaba | 2020 | industry | D5 | Debiased pCVR | Pred+IPS | Impression | CVR AUC 69.29 vs 68.56 | Causal CVR |
| AUUC-max targeting | LIG | 2020 | academic | D6 | ITE ranking | **Inc** | User RCT | AUUC 0.03065 | Campaign |
| E3IR incentive uplift | Tencent FiT | 2024 | industry | D6 | CATE + budget | **Inc** | User treatment | Best AUUC/QINI on Hillstrom | Marketing |
| ReAlloc multi-channel | industry | 2024 | industry | D6 | Channel budget uplift | **Inc** | Item budget | Orders +3.53% | Not swipe |
| DEFER real negatives | Alibaba | 2021 | industry | D7 | CVR; duplicate RN | Pred | Click-time x | Criteo AUC 0.8394; online >6% CVR | **Seed now confirmed** |
| FSIW | CyberAgent | 2020 | industry | D7 | Delayed CVR IS | Pred | Click x | LL 0.3928 vs DFM 0.3989 | Censoring |
| TS-DL | JD | 2020 | industry | D7 | Hazard delay slots | Pred | Item + history | RelaImpr +5–45% vs DIN | Delay |
| DLA-DF | academic/CyberAgent | 2020 | academic | D7 | PU+MNAR CVR | Pred | Click | Beats DFM (fig.) | Delay |
| Many conversions/click | Google | 2021 | industry | D7 | Poisson count/value | Pred | Last-click | Logloss −8.6% vs mature-only | Multi-fire revenue |
| Tinder geosharding | Tinder | 2019 | blog | D8 | Retrieval capacity | n/a | n/a | 20× computations | Infra only |
| TSPR marketplace experiments | Warwick | 2025 | academic | D8 | Global TE under coherency | **Inc** | Query | MC recovers GTE | Two-sided A/B |
| ECDA dating matching | CoupLink | 2026 | industry | D8 | Capacity-aware dates | Pred | Recommendation | Better receiver-side dates (sim) | Second-stage matcher |
| Airbnb guest preferences | Airbnb | 2026 | industry | D8 | Price elasticity IV | **Inc** | Geo-time | Measurement, not ranker | Two-sided demand |

One hundred twenty rows (90 from 2026-08-16 plus 30 continuation). DASI is the NeurIPS 2021 card (`2024_arXiv_NA_Dynamically-Adjusted-Surrogate-Index.md`). UnifiedRL filename: `2024_arXiv_IntegratedRL-MTF_Offline-RL-Multi-Task-Fusion.md`.

---

## Answers to Q1–Q8

### Q1. How do industry recommenders make retention, LTV, or revenue the training objective?

**What sources state.** They rarely replace CTR heads. They (a) fuse short heads toward a long-term **proxy reward** (Zhang et al., Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems, KDD 2022: dwell-correlated instant reward, +2.55% app dwell; Cao et al., xMTF, WWW 2025: daily watch time +0.833%); (b) put **returning time** on a session policy (Cai et al., Reinforcing User Retention in a Billion Scale Short Video Recommender System, WWW 2023: +0.063% D7 vs CEM); (c) add delayed **task heads** (Twitch Multi-Objective Ranking for Live-Streaming, 14-day spend, ARPU +0.56%; Pinterest Save, Revisit, Retain, 7-day revisit; Alibaba A Long-term Value Prediction Framework In Video Ranking, author LTV LT3 +0.21%); (d) train user-level LTV models used in bidding/targeting, not always in ranking (Wang et al., ZILN, 2019; Kuaishou Billion-user Customer Lifetime Value Prediction, CIKM 2022 ROI +11.9–14.7%; WeChat Mini-Game Lifetime Value Prediction, +8.4% LTV/GMV); (e) weight ranking losses by a **reward model of long-term correlation** (Netflix GenRec, +0.006% long-term core metric). Instagram Explore (Vorotilov & Shugaepov, 2023) still fuses **short** events with a value model; numeric LTV lifts are not in that blog.

**Inference:** “Unified objective” in production means **unified serving score**, not a single 30-day retention BCE on each impression.

### Q2. How do they attribute a user-level delayed outcome to an item-level decision?

**What sources state.** Most do not. Credit stays pointwise on the short event (LiRank; ESMM family; Instagram VM). Session-level: RLUR and GFN4Retention put retention on the **last request** or back-propagate flow through the session (Liu et al., Modeling User Retention through Generative Flow Networks, KDD 2024). Item-level among surveyed industrial RL: Ie et al., SlateQ (IJCAI 2019) under single-choice; Wang et al., Future Impact Decomposition in Request-level Recommendations (KDD 2024) splits V(s') across slate items (retention +0.016%). Pinterest Save, Revisit, Retain joins 7-day revisits to the **saved Pin**. Spotify Optimizing Audio Recommendations for the Long-Term attributes 60-day minutes via item stickiness state. User-level LTV papers (ZILN, ODMN, GRePO-LTV, OCARM) explicitly do **not** map Y to one impression.

### Q3. Which labels and horizons for retention and revenue? Delay, sparsity, censoring?

**What sources state.**

| Outcome | Horizons actually used | Delay/censor handling |
|---------|------------------------|------------------------|
| Return / retention | D1/D7 (RLUR, Duolingo); DAU/WAU (Pinterest notifications); LT1/LT7/LT30 revisit (OCARM); 14d vs 63d daily activity (Netflix surrogate); 60d stickiness (Spotify Impatient Bandits and audio RL) | Normalize return time by predicted baseline (RLUR); progressive traces (Impatient Bandits); distillation without post-conversion leakage (OCARM) |
| Engagement surrogate of retention | 14–28d future actions (PinnerFormer); 7d save-revisit (Pinterest); long dwell percentile (LiRank, LinkedIn blogs) | Cluster-normalized thresholds updated daily (LinkedIn 2024) |
| Revenue / LTV | 1–3 years spend (ZILN); 30/90/180/365 (Kuaishou ODMN); 3/7/30d payment (GRePO-LTV); 14d spend (Twitch); page GMV (Alibaba value-aware RL) | ZILN zeros+heavy tail; ordered multi-horizon; DFM/DEFUSE 1–30d conversion windows |
| Conversion funnel | Impression→click→conversion; 7d (ESDF) or 30d (DFM, DEFUSE Criteo) | Fake-negative (Twitter RecSys 2019); IP/FN/RN/DP (DEFUSE); ~70% delayed past collection day (CBDF WeChat) |

No card defines a dating-specific “successful match ends tenure” label.

### Q4. How do they combine short-term heads with long-term heads?

**What sources state.** Three patterns: (1) **Fixed / tunable fusion** — Instagram VM weights; LinkedIn MOO; Pinterest utility weights (Save/Revisit u_RP&RV = 1.27× u_Repin; PRL-PUTS discrete pairs). (2) **Learned fusion** — BatchRL-MTF log-sum of PLE scores; xMTF monotonic cells; RLUR 8-D weight actor. (3) **One extra head, still fused** — long dwell, revisitation, 14d spend, author LTV, Spotify stickiness multiplier Q = P_w × (1+stickiness). Distillation (Airbnb MO-LTR-MD; UniROM; OCARM) is a fourth pattern: teachers carry extra objectives into one student.

### Q5. Where does uplift sit inside the ranking model?

**What sources state.** Almost nowhere in feed/swipe rankers. Devriendt et al. and RERUM rank **users** for campaigns. ESCM² uses IPS/DR for **CVR estimation**, not retention CATE. Sony Counterfactual Reciprocal and CRRS correct **pair display / bilateral assignment**, not incremental retention. RLUR normalizes return time by a predicted baseline (a bias correction, not a two-model uplift head). Pinterest notification volume uses **incremental utility** of +1 send, decoupled from the CTR ranker.

**Inference:** folding the team’s existing uplift model into the same softmax as like/match/conversation **is not a documented industry pattern**. Industry keeps incrementality in experiment design (D3, UniCoRn, DiPS) or in a separate budgeter.

### Q6. Offline and online evaluation under slow retention and two-sided interference?

**What sources state.** Offline: Conservative-OPE (BatchRL-MTF), NCIS (TSCAC), LOPE (Spotify week-1 → week-3), KuaiSim (FID, GFN, xMTF). Surrogate ship gates: Netflix 14 vs 63 day (~95% agreement); Google proxy quality / Pareto sensitivity; PROXIMA segment fragility (68% on KuaiRec). Online: long A/Bs (RLUR ~150 days; Pinterest Save/Revisit ~2 months). Two-sided: UniCoRn producer ATE; Stanford CR bias 0–~80%; CUPID **switchback** because of a shared matching pool; DiPS/DPR for matching-market OPE. Industry workshop (Evaluating for the Long Term, 2026): sign reversals cluster in quality and hyper-monetization; observational surrogacy often biased (Pandora 21-month ad-load).

### Q7. What is specific to two-sided / reciprocal markets?

**What sources state.** Reciprocal fusion or TU equilibrium (Hinge Most Compatible; CyberAgent MTRS / Fast TU / Fair NSW); congestion (rental paper: top 20% rooms ~100% requests; NSW cuts envy 434→31 at a match-count cost); interference (UniCoRn, Stanford GTE, CUPID switchback); metrics that penalize duplicate bilateral hits (CRRS). Coffee Meets Bagel and the industry workshop both warn that time-on-app / short engagement can oppose connection quality. Grindr states it does not rank discovery. **No D8 paper trains on D7 retention or subscription LTV.**

**Inference:** a unified LTV ranker that ignores inbound-like capacity will recreate the congestion the TU/NSW papers measure, and a retention objective will collide with the success paradox the workshop lists as a sign-reversal class.

### Q8. Documented migration paths from CTR + blend to a unified model?

**What sources state, as staged patterns:**

1. **Auxiliary heads first, serving unchanged** — Chen et al., User Response Models to Improve a REINFORCE Recommender System, WSDM 2021; Pinterest Downstream Rewards (add heads, HyperOPT weights, <5% extra train cost); Pinterest Save/Revisit/Retain (new head on MMoE); LinkedIn P(skip) then long dwell; Pinterest 2020 MTL+calibration blog.
2. **Keep towers, replace the blend** — Instagram VM tuning; **BatchRL-MTF → UnifiedRL → EnhancedRL** (Tencent staged MTF; +4.64% then +3.84% consumption); xMTF / PRL-PUTS / RLUR weight actors; Spotify stickiness multiplier on existing clickiness.
3. **Clone retention experts from logs** — Stratified Expert Cloning (Kuaishou 2025) before or instead of online RLUR.
4. **Distill extra objectives into one student** — Airbnb MO-LTR-MD; OCARM teacher→student; first-stage distillation on Instagram Explore.
5. **Myopic → LTV Q-head** — SlateQ on YouTube (keep pCTR, add Q).
6. **Decouple long-term budgeter from CTR ranker** — Pinterest Notification Volume Control (explicit move off CTR-only).
7. **Generative reward-model last** — OneRec, GenRec, HSTU — after a working multi-head ranker exists.

No source documents “delete the uplift model and put CATE in the ranker.” E3IR / ReAlloc / AUUC-max remain incentive and budget allocators. DEFER is the missing delayed-label seed for continuous retraining.

---

## Open gaps

1. **No production dating ranker with retention/revenue as the training objective.** Hinge, Tinder, CMB, Momo, CUPID, CyberAgent TU/NSW optimize matches, dates, chat duration, or welfare — not D7/D30 or subscription LTV.
2. **Success paradox unlabeled.** Evaluating for the Long Term (2026) flags quality/monetization sign reversals; Coffee Meets Bagel rejects time-on-app; no card proposes a “good match that ends tenure” label or a constraint that protects it.
3. **Prediction vs incrementality is not solved inside ranking.** Conditional D30 given exposure will uprank already-retained power users. Uplift-in-ranker papers are campaign LTR (RERUM, E3IR, ReAlloc, AUUC-max) or pair-IPS (Sony), not swipe CATE.
4. **Item-level credit for 7–30d retention is unsolved at dating cardinality.** FID needs item-wise feedback on a small K; SlateQ assumes single choice; GFN percentages are missing from the card; user-level LTV (ZILN/ODMN) does not credit a profile.
5. **No two-sided retention MDP.** RLUR/TSCAC/xMTF are one-sided video. Reciprocal RL with congestion and delayed bilateral outcomes is absent.
6. **Joint LTV + reciprocity.** TU/NSW and BatchRL-MTF never appear in the same system in this corpus.
7. **Subscription mix.** Twitch 14d spend and WeChat 3/7/30d pay are the only delayed **revenue heads** in a ranking/bidding stack; neither is two-sided or success-paradox-aware.
8. **Two-sided surrogate indices.** Netflix/Google/Spotify surrogates assume SUTVA-ish user splits. CUPID, UniCoRn, and TSPR show that is false for matching pools; nobody published a surrogate index **on match-GTE**.
9. **Low-base-rate delayed labels.** ESMM-style entire-space training is for conversion, not for 30d retention after a rare match. How to train a D30 head on impressions that never matched is unspecified.
10. **GFN4Retention numeric lifts** and several blog % (Instagram VM, Snap UUM, Tinder) are **not specified in source** — do not plan capacity on them.

## References (low relevance for the unified-ranker decision)

Useful as background only: Grindr (no ranker); Tinder geosharding (retrieval infra, 20× compute); NICF simulator Q-learning; Reciprocal RS survey (no LTV); SMILE theory paper; Learning to Rank for Uplift (campaign RCTs); UniROM ad auctions; MTGR CTR-only generative ranker; KuaiSim (simulator).
