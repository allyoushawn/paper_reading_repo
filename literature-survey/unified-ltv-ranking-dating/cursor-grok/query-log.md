# Query log — cursor-grok — 2026-08-16

Format: query | result count / note. Nulls: `no results from <source> for <query>`.

## Seed verification searches

- Hinge Most Compatible Gale-Shapley recommender engineering blog | ~5 hits; TechCrunch 2018-07-11 is the primary primary-source-adjacent writeup. no results from Hinge engineering blog for Most Compatible ranking internals
- Bumble Tech blog recommendation ranking data science | blog index exists; no ranking/retention/LTV posts in top results. no results from Bumble Tech for retention OR LTV ranking
- LinkedIn Engineering feed ranking downstream upstream value long dwell | 2 hits (dwell-time posts, 2018 and follow-up)
- Pinterest Engineering multi-objective ranking LTV retention | 1 direct hit (MTL + calibration utility ranking) plus later arXiv 2511.18013, 2605.16344, 2607.14192
- Netflix Reward innovation RecSys 2023 arXiv PDF | title confirmed; no arXiv PDF. ACM paywalled
- Case Study Learning Robust Long-run Surrogate Metrics KDD 2026 | title/authors/venue confirmed; ACM paywalled; no arXiv/SSRN/author PDF
- Instagram Explore value model long-term ranking Meta Engineering | 2 hits: engineering.fb.com 2023-08-09 (already in notebook) and ai.meta.com "Powered by AI"
- 探探 推荐 留存 长期价值 技术博客 | product/PM commentary only. no results from 探探技术 for 用户留存 推荐 强化学习
- Soul App 推荐 留存 长期价值 技术博客 | IPO coverage, no ranking-model paper. no results from Soul 技术博客 for LTV 预估 推荐
- site:eng.snap.com retention ranking recommender long-term value | 1 relevant hit: Universal User Modeling (UUM)
- "Coffee Meets Bagel" recommendation algorithm engineering blog ranking | 2 hits: CIO Dive 2019 (9-model blend); AWS Database Blog (Redis serving). No CMB-owned tech blog with LTV/retention objective
- site:doordash.engineering ranking long-term retention value model | no results from DoorDash Engineering for long-term value ranking
- site:uber.com ranking long-term retention value model | hits on ads Hetero-MMoE, mediation modeling, incentive uplift (marketplace, not dating ranker)

## Chinese keyword searches (this pass)

- 用户留存 推荐 强化学习 | covered by existing Kuaishou RLUR / GFN4Retention / Future Impact sources in notebook
- 长期价值 排序 | covered by BatchRL-MTF, UniROM, GRePO-LTV already in notebook
- 双边市场 推荐 互惠 | covered by CyberAgent + Palomares already in notebook
- 陌陌 推荐 | existing notebook source `模型化召回在陌陌社交推荐的应用和探索`

## NLM source_add 2026-08-16

Added (9):
- LinkedIn dwell time (2 posts)
- Hinge Most Compatible (TechCrunch)
- Snap UUM
- Coffee Meets Bagel (CIO Dive + AWS)
- arXiv 2511.18013 Save/Revisit/Retain
- arXiv 2608.10257 Netflix GenRec
- arXiv 2605.16344 Pinterest PRL-PUTS

Failed or not returned in bulk add:
- Pinterest Medium MTL blog (retrying)
- Meta ai.meta.com Instagram Explore post (retrying)

## NLM quota

- After ~45 cards, `nlm notebook query` and MCP `notebook_query` returned RESOURCE_EXHAUSTED. Remaining cards extracted from arXiv PDFs and live URLs. Do not treat those later cards as NLM-grounded.

## Blog nulls still outstanding for a later pass

- Match Group corporate engineering blog (beyond Tinder 2019)
- Grindr beyond the existing "Automated Decision Making" page (already in notebook)
- Xiaohongshu 长期价值 排序
- Tencent 腾讯技术工程 多任务融合 长期 (paper exists; blog post not separately confirmed)

## Continuation searches 2026-08-17 (cursor-grok)

- Match Group / Tinder engineering beyond 2019 "Powering Tinder" | hit: Tinder Tech Blog Geosharded Recommendations Part 1 (2019-05-14) plus Part 2 architecture and Part 3 consistency. Part 1 carded. no results from Match Group corporate blog for retention OR LTV ranking
- site:medium.com/tinder geosharded recommendations ranking LTV retention | 3 infra posts; no ranking-objective / LTV post
- 小红书 长期价值 排序 推荐 技术博客 | advertiser-LTV explainers and third-party recsys walkthroughs. no results from 小红书技术 for 长期价值 排序
- 腾讯技术工程 多任务融合 长期用户满足 | BatchRL-MTF / UnifiedRL / EnhancedRL papers; 智源 talk recap of the KDD 2022 paper. no results from 腾讯技术工程 blog for a separate MTF post
- Bumble Tech recommendation ranking matching LTV | still moderation / topic-modelling / bitmaps. no results from Bumble Tech for retention OR LTV ranking
- Netflix "Improve your next experiment by learning better proxy metrics from past experiments" | 1 hit; carded (D3 blog companion to KDD 2024)
- Grindr ranking recommender beyond Automated Decision Making | no additional ranking/LTV page. existing Grindr card stands
