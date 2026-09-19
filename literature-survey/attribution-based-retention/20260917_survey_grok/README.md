# 20260917_survey_grok — Follow-up survey: latest industry attribution, and attribution-based retention

Date: 2026-09-17
Lead: Cursor Grok 4.6 (independent of `../20260917_survey/`)
Parent survey: `../` (attribution-based-retention, Run 1–2, April 2026, 62 papers)
NotebookLM notebook (shared with parent survey; all new sources go here): `6a3b8a8e-6f2f-4efe-99eb-283983fc95d9`
Related notebooks: `unified-ltv-ranking-dating` (`67046a44-7490-4fe5-b54a-3f39ef37fdd3`), `two-sided-market-balancing-dating` (`d3071ac8-16ef-4460-8991-7701679974c8`)

## Questions this run must answer

- **Q1.** What is the latest attribution-based approach in the industry? Scope: production or industry-authored attribution systems dated 2025-01 to 2026-09, plus the newest work from the teams and authors behind the classic papers in the parent survey.
- **Q2.** Has anyone in industry published attribution-based retention — that is, attributing user retention, engagement, or days-active to individual in-app interactions (recommendations, matches, messages, notifications, swipes)? No date limit for Q2. Academic work counts if it names a production dataset or deployment.
- **Deliverable.** A recommendation that replaces the current last-touch approach (see Project Context).

## Project Context

**Product.** A dating platform. Users swipe on profiles. A mutual like is a match. Matches lead to conversations.

**Goal.** Attribute a user's retention to particular swipes the user made, so that the platform learns which swipes (and, later, which recommended profiles) keep users coming back. Attribution scores become training labels for a ranking model that predicts, per candidate profile, the incremental retention value of showing it.

**Current production approach (the baseline to beat).** Last-touch attribution. The N7 retention label of a user (active on day 7 after the reference day) is assigned to the most recent swipes the user made before that. Known weaknesses: it ignores earlier swipes, ignores match and conversation outcomes that occur later, credits swipes that would have happened anyway (selection bias — engaged users swipe more), and gives no fractional credit.

**Decisions already made (KB, 2026-06-13).** Retention target is binary next-7-day retention over multi-type events (likes, matches, conversations). Two-tier plan: v1 = interpretable removal-effect attributor; v2 = calibrated deep data-driven attribution with a survival head. This run must confirm or revise that plan against what industry now does.

**What "useful" means for a paper in this run.**

- It produces per-interaction (per-touch) credit, or a per-action incremental value, not only an aggregate lift.
- It handles a binary or time-to-event outcome that recurs (days active), not only one purchase.
- It handles selection bias: engaged users get more interactions naturally.
- It is deployed, or evaluated on production data, at a consumer platform.
- It is from 2025–2026, or it is from a team the parent survey identified as authoritative.

**Analogies to map.** Ad touchpoint → swipe or match. Conversion → N7 retention (recurring). Attribution window → lookback window per interaction type. Channel → interaction type (like, match, conversation, notification).

## Follow list — teams and authors behind the classic papers

The parent survey's `read-papers/` gives these teams. Discovery agents must check each one for 2025–2026 output and log the result, including "nothing new".

| Group | Names to follow | Classic paper in parent survey |
|---|---|---|
| LinkedIn | Bencina et al., LinkedIn marketing science | LiDDA (2025) |
| Amazon Ads | Randall Lewis, Florian Zettelmeyer, Brett Gordon, Cristobal Garib, Johannes Hermle | Causal calibration MTA (2025) |
| Alibaba / Alimama | Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu, Jian Xu, Bo Zheng, Jinqi Wu | MAL (CIKM 2025), MoAE (2026) |
| Google | Aiyou Chen, Nicolas Remy, Marco Longfils, Dinah Shender, Jing Wang, Stephanie Sapp, Jon Vaver, Mukund Sundararajan, Badih Ghazi, Ravi Kumar, Lorne Applebaum, Claudio Gentile | Trimmed Match, TEDDA, UDDA, ARA, attribution sets |
| Meta | Brett Gordon, Robert Moakler, Xiangyu Zeng, Julian Runge | PIE, CABB (KDD 2025), Robyn |
| Adobe | Rohan Arava, Ritwik Sinha, David Arbour | DNAMTA, Bayesian MAR |
| Criteo | Eustache Diemert, Damien Lefortier | Attribution-aware bidding |
| JD.com / Stanford | Ruihuan Du, Harikesh Nair | JDMTA incremental Shapley |
| eBay / USC | Dongdong Yang, Kevin Dyer | DeepMTA |
| Netflix | Causal inference and experimentation team | Causal inference survey |
| DoorDash | Ezra Berger, Jared Bauman | Switchback incrementality |
| Thumbtack | Sang Su Lee, Vijay Raghavan | Panel DML |
| SJTU / UCL | Weinan Zhang, Kan Ren, Jun Wang, Yong Yu | DARNN, bidding machine |
| ICT / CAS | Di Yao, Chang Gong, Jingping Bi | CausalMTA, CausalMMM |
| U Michigan / BJTU | Jiaming Tang, Liping Jing | DCRMTA |
| TCS Research / IIT | Sachin Kumar, Balaraman Ravindran | CAMTA |
| Stanford / Berkeley | Susan Athey, Stefan Wager, Xinkun Nie | Causal forest, R-learner |
| NYU | Foster Provost, Brian Dalessandro, Claudia Perlich | Causally motivated attribution |
| Renmin / PKU | Yixuan An, Zihe Wang | PVM beyond last-click |
| Kuaishou | Qingpeng Cai, Shuchang Liu, Kun Gai, Peng Jiang | RLUR, GFN4Retention (retention RL, from Survey 3) |
| Tencent, ByteDance/TikTok, Snap, Spotify, Pinterest, Duolingo, Match Group/Tinder/Hinge, Bumble | Any published retention or engagement attribution | (none in parent survey — gap) |

## Folder layout

- `README.md` — this file.
- `requirements.md` — this run's search strategy (also mirrored into parent `../requirements.md` § Run 3 Grok).
- `notebooklm-state.md` — this run's notebook id.
- `discovery/` — one candidate table per discovery agent.
- `queue.md` — deduplicated candidate list with status and NotebookLM source id.
- `read-papers/` — one card per processed paper (NotebookLM-extracted). Do not re-process parent `../read-papers/`.
- `review/` — raw Codex and Cursor outputs.
- `survey.md` — the answer to Q1 and Q2, and the recommendation.
- `log.md` — dated run log.
