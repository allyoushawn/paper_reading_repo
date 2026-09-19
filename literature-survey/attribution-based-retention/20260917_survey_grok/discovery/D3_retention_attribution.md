# D3 — Q2 Discovery: Attribution-Based Retention (Per-Touch Credit)

**Discovery date:** 2026-09-17  
**Agent:** grok discovery pass (D3)  
**Q2 definition:** Does the method assign **per-interaction credit** for delayed retention / days-active / N-day return to a **specific in-app action or exposure** (MTA-style), vs merely **optimizing a ranking/RL policy** for retention?

**Classification key**
| Label | Meaning |
|-------|---------|
| **TRUE (MTA-style)** | Publishes per-touch credit of retention/active-days to individual actions/exposures; causal or explicit multi-touch decomposition |
| **PARTIAL** | Item/action-level retention scores or surrogate linkage, but no identified causal MTA / confounding acknowledged |
| **NOT attribution** | RL, bandit, LTR, or surrogate-reward **policy optimization**; no per-exposure retention credit table |

---

## Executive summary

Published **strict** per-touch retention attribution (identified causal credit of N-day active to one swipe/match/rec item amid many exposures) was **not found** in industry or dating-specific literature. The closest production-adjacent hits are **partial**: Pinterest save→revisit linkage, Tencent WeChat KanYiKan **IURO** UI retention scores per historical item, and Kuaishou **FID** item-wise future-impact decomposition. The bulk of “retention” literature is **RL / ranking optimization** (RLUR, GFN4Retention, AURO, LRF, etc.) — near-misses, not attribution.

**Count (this discovery pass):** **3 partial per-touch retention-credit hits** (RevisitMTL, IURO, FID) + **1 touchpoint-incrementality hit** (Netflix message holdback, notification not in-app item) vs **~18 RL/ranking retention-optimization near-misses** logged below.

---

## A. Partial per-interaction retention credit (closest Q2 hits)

### A1. Save, Revisit, Retain (RevisitMTL)

| Field | Value |
|-------|-------|
| **Classification** | **PARTIAL** — deterministic surrogate attribution: save on Pin *i* → profile revisitation within 0–7 days; not full-path MTA, confounders acknowledged |
| **Company / dataset** | Pinterest Inc.; Related Pins / Search, 500M+ users; 24M-user online A/B |
| **Outcome** | Active users (+0.10% A/B); same-day / 1-day / 7-day profile revisitation labels |
| **URL** | https://arxiv.org/abs/2511.18013 |

Explicitly frames “accurate attribution” of which exposure triggered revisit; uses save→revisit event pipeline as surrogate for causal effect of saving on return. Credits **specific saved Pins**, not all retention paths (notifications, direct open, etc.).

---

### A2. Interpretable User Retention Modeling (IURO)

| Field | Value |
|-------|-------|
| **Classification** | **PARTIAL** — per **user–item interaction** UI retention score via CMIL/RMIL; identifies sparse “Aha items”; not causal MTA |
| **Company / dataset** | Tencent WeChat “KanYiKan” (看一看); ZhihuRec offline + production A/B on WeChat recommendation |
| **Outcome** | N-day user return (retention rate); online A/B reported retention lift (exact % in paper Table 3) |
| **URL** | https://doi.org/10.1145/3604915.3608818 |

UI scorer assigns a retention score to **each historical user–item interaction**; attention aggregates to find influential items. Combined with online CTR at serving — interpretability-focused, not Shapley/removal-effect attribution.

Follow-on: *Rethinking User Retention Modeling in Recommendation* (TOIS 2026) — https://doi.org/10.1145/3790098

---

### A3. Future Impact Decomposition (FID / ItemA2C)

| Field | Value |
|-------|-------|
| **Classification** | **PARTIAL** — RL item-wise future-impact decomposition (reward-based + adversarial re-weighting); trajectory credit not causal identification |
| **Company / dataset** | Kuaishou Technology; KuaiRand, MovieLens-1M; Kuaishou online |
| **Outcome** | User retention = probability of return **next week** (+0.016% online); DAU +0.028% |
| **URL** | https://arxiv.org/abs/2401.16108 |

Authors: Xiaobei Wang, Shuchang Liu, Qingpeng Cai, Peng Jiang, Kun Gai, et al. Decomposes request-level future value to **per-item** contributions within list — closest Kuaishou mechanism to item-level delayed credit, but still policy-learning not published attribution tables.

Code: https://github.com/wangxiaobei565/itemdecomposition

---

### A4. Netflix message-level holdback (touchpoint incrementality)

| Field | Value |
|-------|-------|
| **Classification** | **PARTIAL (touchpoint, not in-app item)** — always-on 2% message holdback measures **incremental downstream viewing** per notification/message |
| **Company / dataset** | Netflix; production messaging system |
| **Outcome** | Incremental content viewing (not strictly N-day DAU); contrasts open/click vs incremental watch |
| **URL** | https://medium.com/notificationsblog/incrementality-focused-messaging-measurement-all-the-time-everywhere-94ef0c229368 |

Per-**message** causal incrementality via randomized withholding — MTA-analog for **notifications**, not per-feed-item or swipe retention credit.

---

## B. Dating-platform hits (highest value; mostly NOT per-touch attribution)

### B1. Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching (MRet)

| Field | Value |
|-------|-------|
| **Classification** | **NOT attribution** — pair-level retention-curve LTR; joint retention gain of viewer + recommended user |
| **Company / dataset** | Undisclosed major online dating platform + synthetic two-sided data |
| **Outcome** | User retention (ecosystem-level); higher retention vs match-max / fairness baselines in sim + real data |
| **URL** | https://arxiv.org/abs/2602.15752 |

No per-swipe/match/conversation credit for N-day active.

---

### B2. So, Who Likes You? Evidence from a Randomized Field Experiment

| Field | Value |
|-------|-------|
| **Classification** | **NOT attribution** — RCT on WLY feature; causal effect on messages/matches, not retention days-active credit |
| **Company / dataset** | Major North American dating platform (unnamed; often inferred Hinge-class) |
| **Outcome** | +7.4% messages (women), +14.4% / +11.5% matches; engagement not N-day retention decomposition |
| **URL** | https://doi.org/10.1287/mnsc.2022.4576 |

---

### B3. The Secret to Finding a Match: Field Experiment on Choice Capacity

| Field | Value |
|-------|-------|
| **Classification** | **NOT attribution** — RCT on choice capacity → engagement/matching |
| **Company / dataset** | Online dating platform (collaborator unnamed) |
| **Outcome** | Engagement and matching outcomes by gender/capacity arm |
| **URL** | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3517018 |

---

### B4. Positive Customer Churn: An Application to Online Dating

| Field | Value |
|-------|-------|
| **Classification** | **NOT attribution** — cause-specific **survival/hazard** model; reciprocal interactions → positive churn (success exit), not per-touch credit |
| **Company / dataset** | German online dating panel (1,369 respondents) |
| **Outcome** | Positive vs negative churn hazards; reciprocal messages increase positive churn (β=1.012) |
| **URL** | https://doi.org/10.1177/1094670518795054 |

Survival framing adjacent to Q2 but does **not** assign retention credit to individual likes/swipes.

---

### B5. Improving Match Rates in Dating Markets Through Assortment Optimization

| Field | Value |
|-------|-------|
| **Classification** | **NOT attribution** — dynamic assortment + causal effect of **past matches on like behavior**; optimizes matches not retention credit |
| **Company / dataset** | Major US online dating company (industry partner) |
| **Outcome** | +27% matches in field experiments; past-match count negatively affects likes |
| **URL** | https://doi.org/10.1287/msom.2022.1107 |

---

### B6. Love Unshackled: Mobile App Adoption in Online Dating

| Field | Value |
|-------|-------|
| **Classification** | **NOT attribution** — PSM + DiD on mobile adoption → engagement/matches |
| **Company / dataset** | Large online dating site |
| **Outcome** | More profile views, messages, matches after app adoption |
| **URL** | https://doi.org/10.25300/misq/2019/14289 |

---

### B7. Does Premium Subscription Pay Off? (Online Dating)

| Field | Value |
|-------|-------|
| **Classification** | **NOT attribution** — PSM + DiD on premium → funnel stages |
| **Company / dataset** | Online dating platform panel |
| **Outcome** | More visits, messages, matches post-premium; not retention credit per action |
| **URL** | https://aisel.aisnet.org/icis2018/submissions/retention/1347/ |

---

## C. Kuaishou author cluster (Qingpeng Cai, Shuchang Liu, Kun Gai, Peng Jiang)

| Paper | Class | Company / dataset | Outcome | URL |
|-------|-------|-------------------|---------|-----|
| **RLUR** — Reinforcing User Retention in a Billion Scale Short Video RS (WWW 2023) | **NOT attribution** | Kuaishou production; billion-scale logs | Next-day retention, DAU; fully deployed | https://arxiv.org/abs/2302.01724 |
| **GFN4Retention** — Modeling User Retention through GFN (KDD 2024) | **NOT attribution** (flow back-prop is trajectory credit) | Kuaishou + KuaiRand; production A/B | Cross-session return time / retention reward | https://arxiv.org/abs/2406.06043 |
| **AURO** — Adaptive User Retention Optimization (WWW 2025) | **NOT attribution** | Kuaishou live short-video (~25M DAU) + MovieLens + simulator | Retention / return-time RL under non-stationarity | https://arxiv.org/abs/2310.03984 |
| **SEC** — Stratified Expert Cloning for Retention-Aware Rec (CIKM 2025) | **NOT attribution** | Kuaishou & Kuaishou Lite 200M+ DAU | Active-days via imitation from high-retention strata | https://arxiv.org/html/2504.05628v2 |
| **FID** — Future Impact Decomposition (KDD 2024) | **PARTIAL** | Kuaishou online | Week-ahead return prob +0.016% | https://arxiv.org/abs/2401.16108 |
| **OCARM** — Distilling Post-Conversion Content for User Retention (arXiv 2026) | **NOT attribution** | Kuaishou RTB re-engagement | LT1/LT7/LT30 prediction at bid level | https://arxiv.org/abs/2604.25839 |

RLUR abstract explicitly states retention is “hard to decompose … to each item or a list of items” — motivation for RL, not MTA.

---

## D. Other industry / platform hits

### D1. Long-term engagement & delayed feedback (NOT per-touch attribution)

| Paper / source | Class | Company | Outcome | URL |
|----------------|-------|---------|---------|-----|
| Surrogate for Long-Term User Experience (KDD 2022) | **NOT attribution** | Google (large industrial rec platform) | 5-month visiting frequency via RL surrogate rewards | https://doi.org/10.1145/3534678.3539073 |
| Learned Ranking Function (RecSys 2024) | **NOT attribution** | YouTube | Long-term user satisfaction on watches; on-policy slate RL | https://arxiv.org/abs/2408.06512 |
| SlateQ / RL for Slate-based RS (Google, 2019) | **NOT attribution** (item Q under choice assumptions) | YouTube live experiment | User engagement / LTV decomposition | https://research.google/pubs/reinforcement-learning-for-slate-based-recommender-systems-a-tractable-decomposition-and-practical-methodology/ |
| Impatient Bandits (JMLR 2025) | **NOT attribution** | Spotify (podcast rec; hundreds of millions users) | 2-month repeat engagement; progressive feedback bandit | https://arxiv.org/abs/2501.07761 |
| Incremental Recommendation via Causal Models (arXiv 2026) | **NOT retention attribution** | Spotify production A/B | Incremental stream consumption; −7% impressions | https://arxiv.org/abs/2608.26804 |
| Long-run User Value Optimization (Meta, arXiv 2022) | **NOT attribution** | Facebook Feed ranking | Long-run user value via creator HTE + holdout | https://arxiv.org/abs/2204.11421 |
| News Feed ranking (Meta engineering blog) | **NOT attribution** | Meta | Long-term value; weighted engagement signals | https://engineering.fb.com/2021/01/26/ml-applications/news-feed-ranking/ |
| TTGL — Universal Graph Learning (KDD 2025) | **NOT attribution** | TikTok / ByteDance | 7-day retention +0.35% | https://doi.org/10.1145/3711896.3737269 |
| Downstream Rewards Learning (arXiv 2026) | **NOT attribution** | Pinterest | Long-term engagement via proxy downstream rewards | https://arxiv.org/html/2607.14192v1 |
| DCEO — Direct Causal Effect Optimization (arXiv 2026) | **NOT retention** (GMV) | Alibaba Taobao search | 4-day GMV +0.36%; item-level proxy via causal effect | https://arxiv.org/abs/2608.25635 |
| Sleeping, Recovering Bandit for Notifications (KDD 2020) | **NOT attribution** | Duolingo | DAU +0.5%, D1/D7 recurring retention +2% | https://doi.org/10.1145/3394486.3403351 |
| Duolingo Growth Model (blog) | **NOT attribution** | Duolingo | Markov transition rates (NURR, CURR) → DAU | https://blog.duolingo.com/growth-model-duolingo/ |

---

### D2. Treatment-level uplift / incrementality (retention-adjacent, not per in-app action)

| Paper | Class | Company | Outcome | URL |
|-------|-------|---------|---------|-----|
| Uplift Modeling with Delayed Feedback — CFR-DF (AAAI 2026) | **NOT per-touch** | ByteDance Douyin | Push-frequency uplift; 1B+ user 14-day A/B; activation & switch-close | https://doi.org/10.1609/aaai.v40i19.38686 |
| Leveraging Causal Inference — Mental Health App (ACM 2023) | **PARTIAL (module-level)** | Wysa (app) + RCT | Module-level IV causal effect on well-being **and retention** | https://doi.org/10.1145/3565472.3592967 |

---

### D3. Survival / days-active modeling (NOT per-touch credit)

| Paper | Class | Notes | URL |
|-------|-------|-------|-----|
| Assessing User Retention of a Mobile App: Survival Analysis | **NOT attribution** | Kaplan–Meier / Cox on app uninstall; active vs passive data modes | https://pmc.ncbi.nlm.nih.gov/articles/PMC7728530/ |
| A/B-Test of Retention and Monetization Using the Cox Model | **NOT attribution** | Game analytics; session/churn rates | https://doi.org/10.1609/aiide.v13i1.12941 |
| Learning from Delayed Outcomes via Proxies (ICML 2019) | **NOT retention attribution** | GitHub + marketplace; delayed outcome proxies | https://arxiv.org/abs/1807.09387 |

---

### D4. Offline retention policy learning (academic, no production deployment cited)

| Paper | Class | Dataset | URL |
|-------|-------|---------|-----|
| DT4Rec — User Retention-oriented Recommendation with Decision Transformer (WWW 2023) | **NOT attribution** | IQiYi, MovieLens-1M | https://arxiv.org/abs/2303.06347 |

---

## E. Snap / Tencent / ByteDance — retention-attribution specific

| Source | Retention-attribution finding |
|--------|----------------------------|
| **Snap** (SnapLGR, UUM, eng.snap.com blogs) | RecSys / retrieval papers optimize view time, deep sessions — **no per-item retention credit** published. SnapLGR A/B: view time +0.37%, deep sessions +0.18% — https://arxiv.org/html/2607.28895 |
| **Tencent** | **IURO** (WeChat KanYiKan) is the only Tencent hit with per-interaction retention scores (Section A2). No published swipe/match retention MTA. |
| **ByteDance / TikTok** | **TTGL** (+0.35% 7-day retention) and **CFR-DF** (push-frequency uplift on Douyin) — optimization/uplift, not in-app action credit. **Monolith** is infra (online training), not retention attribution — https://arxiv.org/abs/2209.07663 |

---

## F. Explicit misses — Match Group / Tinder / Hinge / Bumble tech blogs

Searches conducted 2026-09-17 across company engineering domains, `mtch.com`, product blogs, and keyword queries (`retention attribution`, `match`, `swipe`, `recommendation`).

| Source queried | Result |
|----------------|--------|
| `engineering.tinder.com`, `tech.tinder.com` | **No results** — no public engineering blog post on retention attribution, per-swipe credit, or MTA-style match→days-active |
| `hinge.co` (How We Connect, careers, help) | **No technical publication** — product/algorithm descriptions only; no retention credit methodology |
| Hinge / Match Group PDFs & news (`mtch.com`, IR) | **No attribution paper** — business metrics (Sparks, MAU) and AI prompt-quality features only |
| `bumble.com/the-buzz`, `team.bumble.com` | **No engineering retention attribution** — Best Bees compatibility, Private Detector open-source, Tech Academy |
| Match Group engineering R&D venue | **No peer-reviewed or blog MTA-for-retention** found |

**Dating verdict:** Published **per-touch retention attribution for swipes/likes/matches/conversations was not found** from Match Group properties. Closest dating work optimizes **matches** (MSOM 2022) or **ecosystem retention** (MRet ICLR 2026), or studies **engagement/churn hazards** without action-level credit (Positive Customer Churn).

---

## G. Query log (representative searches)

| Query cluster | Notable finding |
|---------------|-----------------|
| retention attribution / engagement attribution / credit assignment long-term | Mostly MMP/ad MTA guides; not in-app rec retention |
| RLUR / GFN4Retention / Qingpeng Cai / Kun Gai | Kuaishou RL retention optimization cluster (Section C) |
| dating app match like swipe retention causal | RCT + survival papers (Section B); no MTA |
| session attribution / which item caused user to return | GA4/deep-link session docs; not rec retention MTA |
| RecSys delayed feedback long-term reward LTV ranking | SlateQ, LRF, Impatient Bandits, Wang surrogate |
| Netflix / YouTube / Facebook long-term value delayed feedback | LRF, Meta long-run value, Netflix message holdback |
| Duolingo / Snap / Spotify / Pinterest retention | Bandit notifications, SnapLGR engagement, Spotify incremental/causal rec, Pinterest RevisitMTL + downstream rewards |
| survival attribution app events | Generic survival analysis; not per-touch credit |
| site:engineering.tinder.com retention | **Empty** |
| site:mtch.com engineering retention | IR/news only |

---

## H. Q2 verdict (D3)

1. **Strict Q2 (identified per-touch causal credit of N-day active to one in-app action):** **Not found** in industry or dating literature searched.
2. **Best partial hits:** Pinterest **RevisitMTL** (save→7d revisit), Tencent **IURO** (UI retention score per historical item), Kuaishou **FID** (item future-impact decomposition).
3. **Dating:** Multiple causal/survival papers on matches/engagement/churn; **zero** published swipe→days-active attribution systems from Tinder/Hinge/Bumble/Match Group.
4. **Dominant pattern:** Retention-aware **RL / LTR / bandit / surrogate reward** (RLUR, GFN4Retention, AURO, LRF, Wang 2022, Duolingo KDD 2020) — optimizes policy, does not publish per-exposure retention credit.
5. **Adjacent incrementality:** Netflix message holdback and Douyin CFR-DF measure **treatment/message-level** incremental effects, not recommender item MTA for retention.

---

*End D3 discovery.*
