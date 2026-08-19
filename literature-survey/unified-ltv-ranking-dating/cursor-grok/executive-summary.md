Date: 2026-08-17

# Unified LTV ranking for a dating recommender — Executive Summary

Workplace: `cursor-grok/`. Corpus: **120 cards** (90 from 2026-08-16 plus 30 continuation). Full comparison table, D1–D9 notes, and Q1–Q8 answers: [`literature-review.md`](./literature-review.md). Method composites: [`method-tracker.md`](./method-tracker.md).

**Decision in one paragraph.** Do not replace like/match/conversation heads with a single “predicted D30” score, and do not fold the existing uplift model into that same serving formula. Industry systems that actually moved off CTR-only ranking (Tencent BatchRL-MTF; Kuaishou RLUR / xMTF; LinkedIn LiRank; Instagram Explore; Spotify long-term audio Q) **keep short-horizon heads** and change fusion or add a delayed head/reward. Incrementality lives in the **evaluation layer** (Athey et al. surrogate index; Netflix 14-vs-63 day auto-surrogate; Spotify LOPE), not inside the softmax. Reciprocity and congestion are a **second stage** (CyberAgent TU/NSW; CUPID switchback), not a later fairness patch.

## Key questions (from Project Context)

- How to make retention/revenue the ranking objective without discarding CTR/CVR heads or pretending conditional retention is causal.
- How to label delayed D7–D30 retention and weeks-scale subscription revenue.
- How to evaluate under two-sided interference and the success paradox.

## Main findings

1. **“Unified” in production means one serving score, not one label.** Zhang, Liu, Dai, et al., Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction in Recommender Systems (KDD 2022, Tencent) and Cao, Zhang, Chen, Zhan, Wang, xMTF (WWW 2025, Kuaishou) still run MTL heads; the policy only learns fusion. Tencent’s follow-ons UnifiedRL (2024; +4.64% valid consumption vs evolutionary search) and EnhancedRL (2024; +3.84% vs UnifiedRL) are a **documented staged MTF path**. Cai, Liu, Wang, et al., Reinforcing User Retention in a Billion Scale Short Video Recommender System (WWW 2023) optimizes return time by outputting **eight weights over existing scorers**; Stratified Expert Cloning (Kuaishou 2025) clones high-retention trajectories instead (+0.098% Active Days).
2. **Predicted retention ≠ effect of showing B to A.** No swipe-ranker card trains CATE of an impression on D30. Uplift papers in this corpus target campaigns (Devriendt et al., Learning to Rank for Uplift Modeling; Tencent RERUM) or pair-display bias (Sony Counterfactual Reciprocal Recommender Systems). ESCM² (Wang et al., SIGIR 2022) is IPS/DR for **CVR**, not retention.
3. **Item-level credit for delayed user outcomes is rare.** Default is pointwise short events (LiRank; ESMM). Exceptions: Ie et al., SlateQ (IJCAI 2019); Wang et al., Future Impact Decomposition (KDD 2024); Liu et al., GFN4Retention (KDD 2024; **exact % not specified in source**); Pinterest Save, Revisit, Retain (7-day Pin join).
4. **Two-sided LTV ranking is undocumented.** Hinge Most Compatible, CyberAgent TU/NSW, and CUPID optimize matches or chat duration. Evaluating for the Long Term (Sigerson et al., 2026) lists quality and hyper-monetization as the **sign-reversal** class — the success paradox belongs there, and no dating card labels it.

---

## Deliverable 1 — Full table pointer and highest-leverage slice

All 90 rows (title, company, year, type, D1–D9, labels/horizon, prediction vs incrementality, credit, gains, dating note) are in [`literature-review.md` § Comparison table](./literature-review.md). Do not treat the slice below as the corpus.

| Paper | Co. | Year | Why it is leverage for this migration | Stated result (card) |
|-------|-----|------|----------------------------------------|----------------------|
| Multi-Task Fusion via RL for Long-Term User Satisfaction (BatchRL-MTF) | Tencent | 2022 | Keep heads; learn the blend | +2.55% app dwell; +9.65% positive interactions |
| xMTF formula-free fusion | Kuaishou | 2025 | Same, without a fixed formula | +0.833% daily watch time vs UNEX-RL |
| Reinforcing User Retention (RLUR) | Kuaishou | 2023 | Return time as the RL objective | +0.45% opens; +0.063% D7 vs CEM (~150d) |
| Future Impact Decomposition (FID) | Kuaishou | 2024 | Item-level split of future V | Retention +0.016%; watch +0.129% vs request A2C |
| SlateQ | Google | 2019 | Keep pCTR; add item Q | YouTube +0.5% d1 → >+1% d20 vs myopic |
| LiRank + LinkedIn long dwell | LinkedIn | 2024 | Aux heads + long-dwell + light DAU explore | +0.5% Feed sessions; TS +0.06% DAU |
| Instagram Explore value model | Meta | 2023 | Documented VM over event heads | Numeric lifts **not specified in source** |
| Scaling delayed spend heads (Twitch MOR) | Twitch | 2025 | 14-day spend/follow in the ranker | DAV +0.09%; capped ARPU +0.56% |
| ZILN LTV loss | Google | 2019 | Zero-inflated revenue head | Spearman +24–48% vs MSE |
| Choosing a Proxy Metric / Netflix 200-test surrogate | Google / Netflix | 2024 / 2023 | Ship on 14d without waiting 63d | Netflix ~95% decision agreement; recall 65% |
| Long-term Off-Policy Evaluation (LOPE) | Spotify | 2024 | Offline long-term policy value when surrogacy fails | MSE 9–15% below DR on 3-week tests |
| Fair Reciprocal / TU matching | CyberAgent | 2023–24 | Congestion in the score | TU 333 vs Naive 220 matches (n=200); NSW envy 31 vs 434 |
| Counterfactual Reciprocal / DiPS OPE | Sony / Wantedly | 2025 | Selection bias and two-sided OPE | NDCG@10 +2.7%; DiPS < IPS MSE |
| Evaluating for the Long Term | 15 platforms | 2026 | Monetization/quality sign reversals | Netflix 95%; YouTube trashy-video recovers by 3 months |
| Impatient Bandits | Spotify | 2023 | Act before 60d labels mature | 50% of prior variance by day 8 (sim; no live A/B) |

---

## Deliverable 2 — Taxonomy and industry adopters

| Family | Long-horizon object | Adopters in this corpus |
|--------|---------------------|-------------------------|
| T1 Value-model / learned fusion | Weights over short heads; optional delayed aux | Instagram Explore; LinkedIn LiRank/dwell; YouTube MMoE; Tencent BatchRL-MTF → UnifiedRL → EnhancedRL; Kuaishou xMTF; Pinterest MTL blog / PRL-PUTS / Save/Revisit; Twitch 14d spend; Alibaba video LTV / SORT-Gen; Airbnb distillation |
| T2 Retention-as-RL-reward | Return time / session return / 60d stickiness | Kuaishou RLUR, TSCAC, GFN4Retention, FID, AURO; Google SlateQ, Top-K REINFORCE, URL; Spotify audio Q; Yahoo r²Bandit |
| T3 Surrogate / proxy **eval** | Short TE → long TE or policy value | Athey et al.; Netflix auto-surrogate; Google proxy/Pareto; Spotify LOPE; Impatient Bandits; DASI; PROXIMA; 15-platform workshop |
| T4 User-level LTV/return model | Multi-horizon spend or LT1/7/30 | ZILN; Kuaishou ODMN; WeChat GRePO-LTV; Meituan CC-OR-Net; PinnerFormer; Snap UUM; OCARM; Duolingo / Pinterest notify volume |
| T5 Entire-space funnel MTL | Impression→click→conversion | ESMM, ESM², HM³, ESDF, DEFUSE, ESCM², AITM, Airbnb Journey Ranker |
| T6 Uplift-in-ranking (thin) | CATE or IPS pair | LTR-for-uplift; RERUM; Sony counterfactual reciprocal; DiPS |
| T7 Delayed conversion/revenue labels | 1–30d windows, ZILN, fake-negatives | Criteo DFM; Twitter FN; Alibaba ESDF/DEFUSE; Tencent CBDF |
| T8 Two-sided overlay | Matches/chat/welfare, **not LTV** | Hinge; Tinder blog; CyberAgent TU/NSW/MTRS; CUPID; CRRS; Momo; LinkedIn UniCoRn; Airbnb diversity |
| T9 Generative reward ranker | Reward model × sequence | Meta HSTU; Kuaishou OneRec; Meituan MTGR; Netflix GenRec |

---

## Deliverable 3 — Three candidate architectures for this dating case (ranked)

Recommended bias matches the cards: keep like/match/conversation as auxiliaries; add delayed retention/revenue; treat incrementality separately; put reciprocity/congestion in the serving path, not as an afterthought.

### Rank 1 — Auxiliary-Head LTV Fusion (AH-LTV)

**Objective.** Serve `score(A,B) = Fuse(p_like, p_match, p_conv, p_{D7}, p_{D30}, E[rev_{28d}], p_{likeback})`, then a **capacity-aware rerank** (TU/NSW or inbound-like cap). Fuse is learned (BatchRL-MTF / xMTF / PRL-PUTS), not the current post-hoc blend.

**Labels and horizons.** Keep current like / match / conversation. Add: binary return D7 and D30 (RLUR online metrics; OCARM LT1/LT7/LT30); 28-day ZILN on subscription + a-la-carte (Wang et al. ZILN; WeChat GRePO 3/7/30d); optional 7-day “deep conversation / return-to-thread” surrogate (Pinterest Save, Revisit, Retain). Reverse-like as an ESMM/AITM-style funnel head, not as a post-multiply hack only.

**How it absorbs today’s stack.** Towers stay. The uplift blend **leaves serving**. Uplift scores become (i) an OPE feature or (ii) a holdout estimator, following Q5 evidence that CATE is not in production swipe formulas.

**Data needed.** Impression logs with delayed joins; user-level D7/D30; 28d revenue; bilateral like/match; logged fusion weights if you train BatchRL-MTF; inbound-like counts for the second stage.

**Main risk.** Fuse will optimize **predicted** retention (active users look good). Without the TU/NSW stage, congestion worsens. Without a success-paradox constraint, a “good match that churns” can be down-ranked. **Inference:** mitigate with a match-quality / conversation-depth constraint (TSCAC-style KL to a sparse match head) and with incrementality only in eval (Deliverable 6).

### Rank 2 — Retention-Ensemble RL (RE-RL)

**Objective.** Session (or day) MDP: terminal reward = normalized return time or D7 (Cai et al., RLUR); immediate reward = like/match/conversation (RLUR dual critics; TSCAC constraints). Action = fusion weights or item Q (SlateQ / FID).

**Labels and horizons.** Same delayed labels as Rank 1, but assigned as **rewards** (session-end in RLUR; item-weighted V(s') in FID; 60-day stickiness in Maystre, Russo, Zhao, Optimizing Audio Recommendations for the Long-Term).

**How it absorbs today’s stack.** Rank 1 towers freeze; the actor only mixes them (RLUR’s 8-D weights). Uplift stays out of the actor. Add TU/NSW after the policy’s top-K.

**Data needed.** Request-level trajectories; item-wise feedback on the shown slate (FID’s requirement); off-policy logs with propensity for Top-K REINFORCE / BatchRL-MTF BCQ.

**Main risk.** No card trains a **two-sided** retention MDP. Credit at session-end (RLUR) will smear a delayed D30 across many profiles unless FID/SlateQ is in place. Online Comment dropped under TSCAC (−0.619%) — sparse match/conversation can lose to dense time-on-app.

### Rank 3 — Unified Reward Ranker (URR)

**Objective.** One expected-value head: a reward model maps short events → long-term member utility (Netflix GenRec; Kuaishou OneRec P-Score; Instagram VM as the shallow version).

**Labels and horizons.** Reward-model training on correlational long-term outcomes (GenRec **states** correlation, not causality): +0.115% short-term, **+0.006%** long-term core at Netflix scale.

**How it absorbs today’s stack.** Distill like/match/conversation teachers into one student (Airbnb MO-LTR-MD +0.37% booking) or replace the cascade later (OneRec +1.68% watch time). Uplift still not inside the reward unless you collect RCTs.

**Data needed.** Stable reward-model labels; huge sequence logs (HSTU/OneRec). Reciprocity is not in these stacks.

**Main risk.** Highest discontinuity, weakest two-sided story, easiest place to hide the success paradox inside a black-box reward. Defer until Rank 1 is in production and surrogates are calibrated.

---

## Deliverable 4 — Staged migration (CTR/CVR + uplift blend → unified model)

| Stage | Change | Measure (offline) | Measure (online) |
|-------|--------|-------------------|------------------|
| 0. Freeze blend | Log today’s mix weights, uplift score, two-sided likes; do not ship a new objective | Calibration of like/match/conversation; uplift AUUC on **holdout experiments**, not on logged Y\|exposure | Baseline D7/D30, sub 28d, match Gini, inbound-like Gini, wasted likes |
| 1. Auxiliary delayed heads | Add D7/D30, ZILN 28d, reverse-like, optional 7d deep-thread (Pinterest Save/Revisit; LinkedIn long dwell; Twitch 14d spend). Serving still uses old blend | Head AUC/GAUC; delayed-label coverage; DFM/DEFUSE-style censoring bias | Guardrail A/B: matches, conversations, D7 **must not collapse**; segment fragility (PROXIMA) |
| 2. Drop uplift from serving | Rank = Fuse(short + delayed heads) with **fixed** weights (Instagram VM / LiRank MOO). Uplift → dashboard + LOPE only | Correlation of new score vs old blend; LOPE week-1 → D21/D30 | 14-day surrogate index vs 63-day holdout (Netflix recipe); two-sided design (UniCoRn / switchback as CUPID) |
| 3. Learn fusion | BatchRL-MTF or xMTF or PRL-PUTS on a dwell/return proxy; TSCAC-style constraint so conversation/match cannot be zeroed | Conservative-OPE / NCIS; constraint slacks | App-open / D7 / 28d revenue; conversation rate (TSCAC showed a Comment drop) |
| 4. Item credit + congestion | FID or SlateQ Q-head on the shown slate; TU/NSW or inbound cap as second stage | Item-level attribution sanity (does V split concentrate on already-popular B?) | Match Gini, envy, unused likes, **both-sides** D7 |
| 5. Only then consider URR | Distill Rank 1+4 into one reward model (GenRec/OneRec pattern) | Reward-model vs 63d north star (surrogacy tests) | Long-run holdout; monetization vs match-quality **sign-reversal** watch (workshop) |

What to **stop** measuring as a north star: impression CTR, raw time-on-app, predicted D30 among people who would have retained anyway.

---

## Deliverable 5 — Label and horizon recommendations (with evidence)

**Retention (ranking heads).**

- Train **D7 binary return** as the dense delayed head (RLUR reports D1/D7 online; OCARM trains LT1/LT7, ships LT30; Duolingo D1/D7 +2.0–2.2% on notifications).
- Train **D30** as a slower head or as the surrogate-index target, not as the only loss (Netflix uses 63-day daily activity as long; Impatient Bandits 60-day stickiness; Kuaishou ODMN ordered 30/90/180/365 for user LTV).
- Add a **7-day item-attributed surrogate** (save/return-to-profile in Jiang et al., Save, Revisit, Retain: 7dRevGrid +1.18%, active users +0.10%) mapped to “return to this match’s thread,” **Inference:** not stated for dating; the join pattern is.
- Handle delay with DFM/DEFUSE/**DEFER**/fake-negative machinery for labels that arrive after ingest (Chapelle KDD 2014; Twitter RecSys 2019; Gu et al., Real Negatives Matter, KDD 2021; DEFUSE WWW 2022). RLUR’s return-time **normalization by predicted baseline** is the bias correction to copy, not a CATE head.

**Revenue.**

- **28-day** ZILN on subscription + a-la-carte (ZILN 1–3y is too slow for ranker iteration; WeChat GRePO uses 3/7/30d and reports +8.4% LTV/GMV; Twitch uses 14d spend, ARPU +0.56%).
- Keep a slower 90d user-level LTV (ODMN) for **budgeting and eval**, not for per-impression BCE.
- Do not use GMV-style page profit (Alibaba Value-aware Recommendation, +6.8% GMV) as the dating north star: it ignores the success paradox.

**Success paradox (no source gives a dating label).** **Inference:** add a constrained “relationship-quality” head (conversation depth, reported date, or Hinge-style phone exchange) and treat retention-up + quality-down as a **failed** launch class, matching Evaluating for the Long Term on quality/monetization reversals (YouTube trashy-video −0.5% watch at 3 weeks, recovery by 3 months; Meta integrity holdout worse at 2 years).

---

## Deliverable 6 — Evaluation plan

**Offline.** (1) Per-head AUC/GAUC on like/match/conversation/D7/D30/rev. (2) Entire-space CTCVR-style metrics on match and conversation (ESMM). (3) Conservative-OPE or LOPE for the fusion policy (BatchRL-MTF Conservative-OPEstimator; Saito et al., Long-term Off-Policy Evaluation and Learning: week-1 streams/clicks/likes → week-3 streams, 9–15% MSE vs DR). (4) DiPS/DPR if the policy is a matching-market allocation (Hayashi et al. / Wantedly Off-Policy Evaluation and Learning for Matching Markets). (5) Never use predicted D30 among treated users as a causal metric.

**Surrogate validation.** Fit a surrogate index (Athey, Chetty, Imbens, Kang, The Surrogate Index, 2019) from historical ranking A/Bs: 14-day match/reply/D7 → 30/63-day retention and 28d revenue. Netflix Evaluating the Surrogate Index… Using 200 A/B Tests: 14 vs 63 day **~95% decision consistency**, precision 79%, recall 65%, **zero** false launches of statistically negative experiences — plan for missed true positives. Do **not** validate the surrogate by correlating user-level likes with D30 (Bibaut, Chou, Ejdemyr, Kallus, Netflix TechBlog 2024: that slope can have the wrong sign). Use TC/JIVE on historical ranking experiments (Learning the Covariance of Treatment Effects Across Many Weak Experiments, KDD 2024). Google Choosing a Proxy Metric from Past Experiments (KDD 2024) and Pareto Optimal Proxy Metrics for weights. PROXIMA for **segment** sign flips (68% fragility on KuaiRec). Re-fit when treatments are auto-correlated (DASI, Microsoft Research) or when surrogacy is confounded (Proximal Surrogate Index, 2026). Prefer **experiment-learned** surrogates over observational fits (Evaluating for the Long Term, 2026; Pandora ad-load observational methods often wrong-signed).

**Online under two-sided interference.** Do not ship Rank 1–4 on a naive viewer-split A/B. Use UniCoRn (LinkedIn, NeurIPS 2021) for producer-side ATE; expect cluster-randomized bias 0–~80% depending on load (Johari et al., Interference, Bias, and Variance in Two-Sided Marketplace Experimentation). CUPID used **switchback** because of a shared pool. TSPR (Two-Sided Prioritized Ranking, 2025) is a coherency-preserving alternative when you must keep a ranking A/B. Run a 14-day surrogate gate and a 60-day holdout. Watch match Gini, unused likes, both-sides D7, and monetization-vs-quality jointly (workshop sign-reversal class).

---

## Deliverable 7 — Open questions, gaps, top-10 reading order

**Open / gaps.** No production dating ranker with D7/D30 or subscription as the **training** loss. Success paradox unlabeled. Impression-level retention CATE absent. FID/SlateQ item credit untested at dating slate size and bilateral feedback. No two-sided retention MDP. TU/NSW never combined with BatchRL-MTF in this corpus. No surrogate index on **match GTE**. GFN4Retention and Instagram VM numeric lifts **not specified in source**.

**Top-10 reading order** (for the dating ranking team, not citation count):

1. Zhang et al., Multi-Task Fusion via Reinforcement Learning for Long-Term User Satisfaction, KDD 2022 (BatchRL-MTF).
2. Cai et al., Reinforcing User Retention in a Billion Scale Short Video Recommender System, WWW 2023 (RLUR).
3. Cao et al., xMTF, WWW 2025.
4. Borisyuk et al., LiRank, KDD 2024, plus LinkedIn dwell blogs.
5. Vorotilov & Shugaepov, Scaling the Instagram Explore Recommendations System, 2023.
6. Wang et al., Future Impact Decomposition, KDD 2024, and Ie et al., SlateQ, IJCAI 2019.
7. Athey et al., The Surrogate Index, 2019; Zhang et al., Netflix 200 A/B tests, 2023; Tripuraneni et al., Choosing a Proxy Metric, KDD 2024.
8. Saito et al., Long-term Off-Policy Evaluation and Learning, WWW 2024; Sigerson et al., Evaluating for the Long Term, 2026.
9. Tomita et al., Fast Examination-agnostic Reciprocal Recommendation, RecSys 2023; Tomita & Yokoyama, Fair Reciprocal Recommendation, RecSys 2024.
10. Wang et al., ZILN, 2019; Twitch Multi-Objective Ranking for Live-Streaming (14d spend); Pinterest Save, Revisit, Retain.

---

## Most Fundamental Methods (from method-tracker composites)

Counts are **estimated from this 120-card corpus**, not global citations. Composite = 3×baseline + 2×derived + simplicity + 2×consistency. Continuation cards add DEFER as a DFM descendant and UnifiedRL/EnhancedRL as BatchRL-MTF descendants; they do not dethrone ESMM / Surrogate Index / DFM at the top of the table.

1. **ESMM** (composite 36): Ma, Zhao, Huang, Wang, Hu, Zhu, Gai, Entire Space Multi-Task Model, SIGIR 2018. The like→match→conversation identity trained on all impressions; D5 is descendants.
2. **Surrogate Index** (31): Athey, Chetty, Imbens, Kang, The Surrogate Index, NBER 2019. The eval object for delayed north stars; D3 is descendants.
3. **Delayed Feedback Model** (27): Chapelle, Modeling Delayed Feedback in Display Advertising, KDD 2014. Right-censoring for subscription labels.
4. **MMoE** (26): Zhao, Hong, Wei, et al., Recommending What Video to Watch Next, RecSys 2019. Default multi-head ranker.
5. **ZILN** (25): Wang et al., A Deep Probabilistic Model for Customer Lifetime Value Prediction, 2019. Default zero-inflated revenue loss.

BatchRL-MTF (16), RLUR (21), SlateQ (19), and TU/NSW (17) score lower because few later cards re-run them as baselines. They are still the **system templates** for AH-LTV / RE-RL (see method-tracker “project-critical” table).

---

## Implications for the dating recommender

The current system is already T1 (CTR/CVR heads) plus an extra T6 score. The documented migration is **T1 → T1+delayed heads → learned fusion (T2 on weights) → T8 rerank**, with T3 as the launch process. That is AH-LTV then RE-RL, not a jump to OneRec.

Reciprocity cannot wait for stage 5: CyberAgent TU/NSW and the rental congestion paper show personalization without capacity concentrates demand; a retention-trained ranker will do the same to high-LTV profiles. CUPID and UniCoRn are the experiment designs for that second stage.

Uplift should remain the team’s honesty check — LOPE, holdout CATE, UniCoRn — not a third term in the ranking formula. Sources that put incrementality **inside** ranking are campaign targeters, not dating feed rankers.

## Next steps

- [ ] Stage 0–1: delayed D7/D30 + ZILN 28d heads; log two-sided outcomes; remove uplift from serving.
- [ ] Fit a 14-day surrogate index on historical ranking A/Bs (Netflix/Google recipe); add PROXIMA segment audit.
- [ ] Stage 3–4: BatchRL-MTF or xMTF fusion; FID/SlateQ credit; TU/NSW or inbound cap.
- [ ] Explicit success-paradox guardrail in the launch rubric (workshop quality/monetization class).

## Search scope

- Survey dates: 2026-08-16 (90 cards) and 2026-08-17 continuation (30 cards; **120 total**). Directions D1–D9 as in `../requirements.md`.
- Mix: D1=28, D2=16, D3=13, D4=12 (57.5% core), D5=7, D6=7, D7=10, D8=22, D9=5. Industry + blog ≥60% (typed fields ~89%).
- Continuation filled: DEFER seed; Netflix proxy-metrics blog; Tinder geosharding (infra, low relevance); Tencent UnifiedRL/EnhancedRL staged MTF; remaining brief blog nulls logged.
