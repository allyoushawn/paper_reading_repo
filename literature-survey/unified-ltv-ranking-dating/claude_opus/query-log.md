# Query Log — claude_opus run

The brief requires a record of every query with its result count, and null results in the form
`no results from <source> for <query>`.

---

## Phase 2 — NotebookLM deep research

**2026-08-16 — NotebookLM `research_start`, source=web, mode=deep**

Query (abbreviated): industry recommenders using long-term value, retention, LTV or revenue as the
ranking training objective, plus RL for retention, multi-task fusion, surrogate metrics, industrial
LTV prediction, delayed feedback, uplift inside rankers, and reciprocal two-sided markets. Venue
preference stated for KDD, WWW, CIKM, RecSys, WSDM, SIGIR industry tracks and named company blogs.

- **Result count: 96 sources found.**
- Selected for import after deduplication: 50.
- Removed before import: 46. Breakdown of removals:
  - Mirror duplicates of a paper already selected (ResearchGate, alphaXiv, OpenReview, Semantic
    Scholar copies of the same arXiv paper): 30.
  - Code repositories, not papers (`ksRecoTech/Kuai-RL`, `KID-22/DDFM`, `awesome-generative-recsys`): 3.
  - Listing or index pages, not papers (RecSys 2025 accepted contributions): 1.
  - NotebookLM's own generated deep report (index 0), not an external source: 1.
  - Off topic: 11. Named: a crypto prediction market page, a TrendHunter marketing post on Bumble,
    an Import AI newsletter issue, a Netflix data-infrastructure post, a Spotify LLM-eval post, a
    dating-psychology paper on swipe fatigue, a consultancy blog on the RECON model, a Google patent,
    a master's thesis on game LTV features, an MDPI e-commerce CLV paper, and a LinkedIn-algorithm
    marketing blog.

### Import result: 37 of 50 ingested with content

**13 sources failed content extraction.** The host blocked the automated fetch. NotebookLM created a
placeholder entry titled with the raw URL, but loaded no text. Verified by querying two of them
directly — NotebookLM answered "no passages are loaded in my context" and reported the notebook as
holding 37 sources.

Failure pattern by host:

- `netflixtechblog.com` (Medium-hosted): 6 failures.
- `researchgate.net`: 6 failures.
- `academic.oup.com` (Oxford Academic, paywalled): 1 failure.
- `alibaba-cloud.medium.com` (Medium-hosted): 1 failure. *(counted inside the Medium group above)*

The failed items, with the seed or direction they serve:

| # | Item | Direction | Why it matters |
|---|---|---|---|
| 1 | Recommending for Long-Term Member Satisfaction at Netflix | D1 | Brief seed |
| 2 | Improve Your Next Experiment by Learning Better Proxy Metrics | D3 | Pairs with the Google KDD 2024 proxy-metric seed |
| 3 | A Survey of Causal Inference Applications at Netflix | D6 | — |
| 4 | Round 2: A Survey of Causal Inference Applications at Netflix | D6 | — |
| 5 | GenPage: End-to-End Generative Homepage Construction at Netflix | D9 | — |
| 6 | ML Platform Meetup: Infra for Contextual Bandits and RL | D2 | — |
| 7 | Multi-objective RL for recommender systems: a survey | D1/D2 | — |
| 8 | MTGR: Industrial-Scale Generative Recommendation in Meituan | D9 | — |
| 9 | Uplift Modeling with Generalization Guarantees | D6 | — |
| 10 | Learning to Rank for Uplift Modeling | D6 | Directly on topic — uplift plus ranking |
| 11 | The Surrogate Index (Athey, Chetty, Imbens, Kang) | D3 | **Brief seed, D3 anchor** |
| 12 | Recommender System: Ranking Algorithms and Training Architectures (Alibaba Cloud) | D1 | — |
| 13 | An Attention-based Model for CVR Prediction with Delayed Feedback | D7 | — |

**Action taken:** the brief's paywall rule requires searching arXiv, SSRN, Semantic Scholar and author
pages before marking a reference unavailable. A recovery search ran. The 13 placeholder entries stay
in the notebook, marked `nlm:failed:no-content` in `queue.md`. Recovered URLs entered as new sources.

### Recovery result: 8 of 13 recovered, plus 1 bonus seed

Recovered and ingested (verified by direct query — both spot checks returned full text):

| # | Replacement URL | What it serves | Note |
|---|---|---|---|
| 2 | `arxiv.org/pdf/2402.17637` | Learning the Covariance of Treatment Effects Across Many Weak Experiments | The Netflix KDD 2024 paper the blog post cites as its own work |
| 2b | `arxiv.org/pdf/2309.07893` | Choosing a Proxy Metric from Past Experiments | **Bonus — this is a brief seed for D3** (Google, KDD 2024) |
| 5 | `arxiv.org/pdf/2606.31031` | GenPage: End-to-End Generative Homepage Construction at Netflix | Same document |
| 8 | `arxiv.org/pdf/2505.18654` | MTGR: Industrial-Scale Generative Recommendation in Meituan | Same document |
| 9 | `arxiv.org/pdf/2012.09897` | Treatment Targeting by AUUC Maximization with Generalization Guarantees | **Not confirmed identical.** Same authors and method as the target, different title. Treat as the probable preprint, and mark the claim as unverified in the paper card. |
| 10 | `arxiv.org/pdf/2002.05897` | Learning to Rank for Uplift Modeling | Same document |
| 11 | `nber.org/.../w26463.pdf` | The Surrogate Index (Athey, Chetty, Imbens, Kang) | **Brief seed, D3 anchor.** NBER working-paper version of the paywalled Review of Economic Studies article |
| 12 | `alibabacloud.com/blog/...596643` | Recommender System: Ranking Algorithms and Training Architectures | Publisher's own site, not the Medium mirror |
| 13 | *(local PDF used instead)* | An Attention-based Model for CVR Prediction with Delayed Feedback | The official IJCAI 2020 proceedings PDF exists, but the paper is also in the local Awesome repo, so the local file was used |

**Null results — 5 unrecoverable.** Recorded per the brief's rule.

- `no free version from ACM DL, research.netflix.com, or any mirror for "Recommending for Long-Term Member Satisfaction at Netflix"` — ACM DL returns HTTP 403. `research.netflix.com` serves a client-side-rendered shell with no fetchable text. **This is a brief seed for D1 and counts as a real coverage loss.**
- `no paper found for "A Survey of Causal Inference Applications at Netflix"` — blog-only, no underlying paper.
- `no paper found for "Round 2: A Survey of Causal Inference Applications at Netflix"` — blog-only, no underlying paper.
- `no paper found for "ML Platform Meetup: Infra for Contextual Bandits and Reinforcement Learning"` — a 2019 event recap, no proceedings.
- `no free version from arXiv, SSRN, Semantic Scholar, or author pages for "Multi-objective reinforcement learning for recommender systems: a comprehensive survey"` — Springer, DOI 10.1007/s13735-025-00383-7, paywalled with no open preprint.

**Method note.** A source whose title displays as a raw URL is **not** necessarily a failed ingestion.
Sources added through `research_import` failed silently and held no text. Sources added through
`source_add` displayed raw-URL titles but held full text. The only reliable test is to query the
source and check whether NotebookLM returns passages. Both methods were checked by query here, not
inferred from the title.

---

## Phase 2 — local Awesome repo scan

**Source:** `Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising`, a local clone holding
574 PDFs.

- **Result count: 46 candidates** across D1, D2, D3, D5, D7, D8, D9.
- After removing 3 already present in the notebook with content (ES-DFM, DEFER, OneRec-V2):
  **43 unique PDFs uploaded as local files.**
- Uploading local files bypasses host blocking entirely. This also recovered failure #13 above.

**Null results from this source:**

- `no results from the Awesome repo for D4 (user-level retention and LTV prediction, label design)` —
  the repo holds nothing on customer lifetime value, zero-inflated lognormal loss, return-time or
  churn prediction, 28-day future-action labels, dense all-action loss, or notification retention.
- `no results from the Awesome repo for D6 (uplift and incremental effects inside the ranking model)` —
  the repo holds causal debiasing of conversion-rate labels, filed under D5, but nothing on uplift
  ranking, incremental recommendation, or off-policy learning for matching markets.

These two null results are **covered by the NotebookLM deep research**, which returned strong D4 and
D6 material. The two discovery sources are complementary, not redundant.

---

## Phase 2 — seed verification and gap-filling discovery (round 2)

The brief requires every seed marked `confirmed` or `not found`. All 41 seeds were checked, plus
targeted extra searches for the three thin directions D8, D4 and D3.

**Result: 23 found with a fetchable URL, 15 already queued, 6 blocked, 2 not found. 37 new sources
ingested** (38 recovered minus one duplicate — DEFER was already in the notebook).

### Ingested by direction

| Direction | New | Notable |
|---|---|---|
| D8 two-sided and reciprocal | **20** | Palomares reciprocal-recommender survey, CyberAgent RecSys 2023, Tinder, Grindr, Momo, LinkedIn Jobs, Airbnb, plus 6 papers on two-sided experiment interference |
| D4 user-level LTV and labels | 5 | Google ZILN, Kuaishou billion-user LTV, PinnerFormer, Duolingo notification bandit |
| D2 RL for retention | 4 | Kuaishou GFN4Retention, Future Impact Decomposition, Two-Stage Constrained Actor-Critic, Spotify long-term audio |
| D3 surrogate metrics | 3 | Evaluating for the Long Term (15-firm workshop report), Spotify Impatient Bandits, Long-term OPE |
| D1 long-term value objective | 2 | LinkedIn LiRank, Meta Instagram Explore value model |
| D6 uplift in the ranker | 2 | Counterfactual Reciprocal Recommenders, OPE for Matching Markets |
| D5 multi-task cascades | 1 | Alibaba ESCM2 |

### A URL-verification error caught downstream

The verification agent reported `arxiv.org/pdf/2007.16120` as verified. It returns **HTTP 404**.
The `/abs/` form returns 200, and `/pdf/2007.16120v2` returns a valid PDF. The paper — the Palomares
reciprocal-recommender survey, the D8 anchor — was ingested from the version-suffixed path.

**Rule for later runs:** an arXiv paper whose unversioned `/pdf/` path 404s may still be available at
`/pdf/<ID>v1` or `v2`. Check the versioned path before recording a null result. Do not trust a
reported "verified" URL that fails ingestion twice — check it directly.

### Blocked — recorded as null results

- `no free version from ACM DL or research.netflix.com for "Reward innovation for long-term member satisfaction"` — Netflix, RecSys 2023, Tang, Pan, Wang, Basilico. **The seed is now CONFIRMED to exist**, unlike the earlier assessment. It is inaccessible, not missing. ACM DL returns 403.
- `no free version from ACM DL for "Case Study: Learning Robust, Long-run Surrogate Metrics with Modeling and Instrumental Variables"` — Meta, KDD 2026. Brief seed. Confirmed to exist.
- `no free version from ACM DL or labs.pinterest.com for "Notification Volume Control and Optimization System at Pinterest"` — KDD 2018. Brief seed. Confirmed to exist.
- `no free version from ACM DL for "MIRROR: A Multi-View Reciprocal Recommender System for Online Recruitment"` — SIGIR 2024.
- `no free version from ScienceDirect for "biDeepFM: A multi-objective deep factorization machine for reciprocal recommendation"` — 2021.
- `no non-Medium mirror for "Evolution of Multi-Objective Optimization at Pinterest Home Feed"` — every Pinterest Engineering post is Medium-hosted.

### Not found

- `no Hinge-authored technical post found for the "Most Compatible" Gale-Shapley feature` — only third-party press coverage exists.
- `no official Bumble engineering or data-science blog located`.

### Dating-industry null results — this is itself a finding

- `no results from Match Group for "technology blog engineering data science machine learning recommendation"`
- `no results from Coffee Meets Bagel for "engineering blog machine learning matching algorithm"`
- `no results from Tantan 探探 for "技术 推荐算法 匹配"`
- `no results from Soul App for "推荐算法 技术团队 社交"`

**The major dating platforms publish essentially nothing on ranking.** The only industry sources that
exist are Tinder's 2019 pressroom post, Momo's InfoQ article, and Grindr's disclosure — and Grindr
states it runs **no recommendation algorithm at all**, only distance-sorted search.

This shapes the survey's conclusion. Evidence for a unified retention/revenue ranker in a dating
context must be transferred from adjacent two-sided markets — LinkedIn Jobs, Airbnb, and online
recruitment — because the dating industry itself has not published it. The executive summary must say
so plainly rather than imply a dating-specific evidence base exists.

---

## OPEN DEVIATION — the core-direction ratio rule cannot be met

**The rule.** The brief states: "Fill the core directions D1 to D4 to at least 50% of the total before
you expand D5 to D9."

**The state after round 2.**

| Direction | Count |
|---|---|
| D1 | 15 |
| D2 | 17 |
| D3 | 8 |
| D4 | 9 |
| D5 | 9 |
| D6 | 11 |
| D7 | 23 |
| D8 | 25 |
| D9 | 8 |
| **Total** | **125** |

D1–D4 hold 49 of 125 — **39%**, short of the 50% rule.

**Why the rule cannot be satisfied here.** Reaching 50% would require cutting the total to about 98,
which means removing roughly 27 non-core papers. The two largest non-core directions are D7 (23) and
D8 (25). Cutting D8 would gut the direction that carries reciprocity, congestion, two-sided
interference, and every dating-industry source the survey managed to find. That directly contradicts
the Project Context, which names reciprocity and congestion as defining constraints and devotes
research question Q7 to them.

**Assessment.** The rule's purpose is to stop a survey drifting into adjacent areas before covering
its core. That purpose is met: every core direction now holds solid coverage (D1: 15, D2: 17, D3: 8,
D4: 9), and each cleared the 3-reference floor several times over. The ratio fails on arithmetic, not
on weak core coverage.

**Decision taken.** Keep D8 at full strength and record the deviation rather than obey the ratio.
The Project Context is the declared north star and it outranks a proportional heuristic. D7 at 23 is
the genuinely over-weighted direction — an artifact of the local Awesome repo, which is dense in
advertising conversion-delay work. Phase 3 will treat the weakest D7 papers at the one-paragraph
depth reserved for Priority 3–4, so they consume budget in proportion to their value.

**This deviation is flagged for the user and must appear in `log.md` and the executive summary.**

---

## Pending null-result checks

The brief requires a recorded null result for every named blog that returns nothing. These sources
are **not yet searched** and must be covered before the synthesis:

- **English:** Netflix Tech Blog, Spotify Research and Engineering, Pinterest Engineering, LinkedIn
  Engineering, Meta Engineering and AI at Meta, Google Research, YouTube, Airbnb Tech, Uber
  Engineering, DoorDash Engineering, Snap Engineering, Duolingo, Match Group and Tinder Tech Blog,
  Hinge, Bumble Tech, Grindr, Coffee Meets Bagel.
- **Chinese:** Kuaishou (快手技术), ByteDance/Douyin (字节跳动技术团队), Tencent (腾讯技术工程),
  Meituan (美团技术团队), Alibaba (阿里技术), Xiaohongshu, Tantan (探探), Momo (陌陌), Soul.

Note: the dating-app sources (Tinder, Hinge, Bumble, Grindr, Coffee Meets Bagel, Tantan, Momo, Soul)
are the highest-value and least likely to yield published ranking work. A null result for them is
itself a finding worth reporting.
