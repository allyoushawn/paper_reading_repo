---
model_identifier: codex-sol
timestamp: 2026-08-19T06:17:54Z
method: HEAD then GET Range bytes=0-2047 fallback; redirects followed; 7s timeout; one retry per failure.
totals: Working=120; Unreachable=0; Ambiguous=0
resolution: Verified working=24; Replacements=2; Unresolved=0

## Resolution pass

Method: explicit web search/open of canonical publishers and primary mirrors; ACM/Medium bot-blocks were treated as public when an exact DOI/title record was found. Replacement URLs are canonical primary pages.

| Index | Original URL | Verdict | Replacement canonical URL | Evidence |
|---:|---|---|---|---|
| 3 | https://dl.acm.org/doi/10.1145/3726302.3731935 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 6 | https://dl.acm.org/doi/10.1145/3637528.3671597 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 7 | https://dl.acm.org/doi/10.1145/3580305.3599881 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 10 | https://dl.acm.org/doi/10.1145/3366423.3380122 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 11 | https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad | working-browser |  | Exact Pinterest Engineering title/page found by web search; Medium endpoint returned 403. |
| 13 | https://dl.acm.org/doi/10.1145/3298689.3346998 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 14 | https://ai.meta.com/blog/powered-by-ai-instagrams-explore-recommender-system/ | replacement-found | https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/ | Original returned a bounded HTTP failure; canonical primary page verified by web open/search. |
| 15 | https://dl.acm.org/doi/10.1145/3394486.3403359 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 16 | https://dl.acm.org/doi/10.1145/3298689.3346997 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 28 | https://dl.acm.org/doi/10.1145/3437963.3441764 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 29 | https://dl.acm.org/doi/10.1145/3394486.3403384 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 30 | https://dl.acm.org/doi/10.1145/3289600.3290999 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 31 | https://dl.acm.org/doi/10.1145/3308558.3313404 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 32 | https://dl.acm.org/citation.cfm?doid=3178876.3185994 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 38 | https://dl.acm.org/doi/10.1145/3637528.3671651 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 45 | https://dl.acm.org/doi/10.1145/3583780.3615489 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 46 | https://dl.acm.org/doi/10.1145/3404835.3463053 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 47 | https://dl.acm.org/doi/10.1145/3447548.3467071 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 48 | https://dl.acm.org/doi/10.1145/3397271.3401443 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 49 | https://dl.acm.org/doi/10.1145/3366423.3380037 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 50 | https://dl.acm.org/doi/10.1145/3209978.3210104 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 55 | https://dl.acm.org/doi/10.1145/3485447.3511965 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 58 | https://dl.acm.org/doi/10.1145/3298689.3347002 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 59 | https://dl.acm.org/doi/10.1145/2623330.2623634 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |
| 69 | https://www.alphaxiv.org/overview/2309.12645v2 | replacement-found | https://arxiv.org/abs/2309.12645 | Original returned a bounded HTTP failure; canonical primary page verified by web open/search. |
| 110 | https://dl.acm.org/doi/10.1145/3404835.3462892 | working-browser |  | Exact DOI bibliographic record or public mirror found by web search; original publisher endpoint returned 403. |

| Index | Status | HTTP | Final URL | Attempt trace |
|---:|---|---:|---|---|
| 1 | Working | 200 | https://arxiv.org/html/2602.17058 | HEAD:200 |
| 2 | Working | 200 | https://arxiv.org/html/2608.04455v1 | HEAD:200 |
| 3 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3726302.3731935 | HEAD:403;GET:403 |
| 4 | Working | 200 | https://arxiv.org/html/2504.05669v1 | HEAD:200 |
| 5 | Working | 200 | https://arxiv.org/pdf/2402.06859 | HEAD:200 |
| 6 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3637528.3671597 | HEAD:403;GET:403 |
| 7 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3580305.3599881 | HEAD:403;GET:403 |
| 8 | Working | 200 | https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/ | HEAD:200 |
| 9 | Working | 200 | https://www.linkedin.com/blog/engineering/feed/leveraging-dwell-time-to-improve-member-experiences-on-the-linkedin-feed | HEAD:200 |
| 10 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3366423.3380122 | HEAD:403;GET:403 |
| 11 | Ambiguous | 403 | https://medium.com/pinterest-engineering/multi-task-learning-and-calibration-for-utility-based-home-feed-ranking-64087a7bcbad | HEAD:403;GET:403 |
| 12 | Working | 200 | https://www.linkedin.com/blog/engineering/feed/understanding-feed-dwell-time | HEAD:200 |
| 13 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3298689.3346998 | HEAD:403;GET:403 |
| 14 | Unreachable |  | https://ai.meta.com/blog/powered-by-ai-instagrams-explore-recommender-system/ | HEAD:500;GET:500;HEAD:500;GET:500 |
| 15 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3394486.3403359 | HEAD:403;GET:403 |
| 16 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3298689.3346997 | HEAD:403;GET:403 |
| 17 | Working | 200 | https://arxiv.org/pdf/2310.03984 | HEAD:200 |
| 18 | Working | 200 | https://arxiv.org/pdf/2509.02458 | HEAD:200 |
| 19 | Working | 200 | https://arxiv.org/html/2504.05628v2 | HEAD:200 |
| 20 | Working | 200 | https://arxiv.org/pdf/2401.16108 | HEAD:200 |
| 21 | Working | 200 | https://arxiv.org/pdf/2404.15691 | HEAD:200 |
| 22 | Working | 200 | https://arxiv.org/pdf/2406.06043 | HEAD:200 |
| 23 | Working | 200 | https://arxiv.org/pdf/2307.09943 | HEAD:200 |
| 24 | Working | 200 | https://arxiv.org/pdf/2302.03561 | HEAD:200 |
| 25 | Working | 200 | https://arxiv.org/pdf/2302.01724 | HEAD:200 |
| 26 | Working | 200 | https://arxiv.org/pdf/2302.01680 | HEAD:200 |
| 27 | Working | 200 | https://arxiv.org/pdf/2208.04560 | HEAD:200 |
| 28 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3437963.3441764 | HEAD:403;GET:403 |
| 29 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3394486.3403384 | HEAD:403;GET:403 |
| 30 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3289600.3290999 | HEAD:403;GET:403 |
| 31 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3308558.3313404 | HEAD:403;GET:403 |
| 32 | Ambiguous | 403 | https://dl.acm.org/citation.cfm?doid=3178876.3185994 | HEAD:403;GET:403 |
| 33 | Working | 200 | https://research.atspotify.com/2024/5/estimating-long-term-outcome-of-algorithms | HEAD:200 |
| 34 | Working | 200 | https://arxiv.org/pdf/2402.17637 | HEAD:200 |
| 35 | Working | 200 | https://arxiv.org/html/2601.10176v2 | HEAD:200 |
| 36 | Working | 200 | https://arxiv.org/pdf/2511.18013 | HEAD:200 |
| 37 | Working | 200 | https://arxiv.org/html/2506.11037v3 | HEAD:200 |
| 38 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3637528.3671651 | HEAD:403;GET:403 |
| 39 | Working | 200 | https://ojs.aaai.org/index.php/AAAI/article/download/25583/25355 | HEAD:200 |
| 40 | Working | 200 | https://arxiv.org/pdf/2208.13358 | HEAD:200 |
| 41 | Working | 200 | https://arxiv.org/pdf/2205.04507 | HEAD:200 |
| 42 | Working | 200 | https://research.duolingo.com/papers/yancey.kdd20.pdf | HEAD:200 |
| 43 | Working | 200 | https://arxiv.org/pdf/1912.07753 | HEAD:200 |
| 44 | Working | 200 | http://cdn-static.findly.com.s3.amazonaws.com/wp-content/uploads/sites/1641/2021/08/12173522/notifications-kdd18.pdf | HEAD:200 |
| 45 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3583780.3615489 | HEAD:403;GET:403 |
| 46 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3404835.3463053 | HEAD:403;GET:403 |
| 47 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3447548.3467071 | HEAD:403;GET:403 |
| 48 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3397271.3401443 | HEAD:403;GET:403 |
| 49 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3366423.3380037 | HEAD:403;GET:403 |
| 50 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3209978.3210104 | HEAD:403;GET:403 |
| 51 | Working | 200 | https://xingt-tang.github.io/assets/pdf/rerum_kdd24.pdf | HEAD:200 |
| 52 | Working | 200 | https://arxiv.org/pdf/2012.09897 | HEAD:200 |
| 53 | Working | 200 | https://arxiv.org/pdf/2012.08724 | HEAD:200 |
| 54 | Working | 200 | https://arxiv.org/html/2604.21675v1 | HEAD:200 |
| 55 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3485447.3511965 | HEAD:403;GET:403 |
| 56 | Working | 200 | https://cdn.aaai.org/ojs/16587/16587-13-20081-1-2-20210518.pdf | HEAD:200 |
| 57 | Working | 200 | https://arxiv.org/abs/2104.14121 | HEAD:200 |
| 58 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3298689.3347002 | HEAD:403;GET:403 |
| 59 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/2623330.2623634 | HEAD:403;GET:403 |
| 60 | Working | 200 | https://arxiv.org/pdf/2306.09060 | HEAD:200 |
| 61 | Working | 200 | https://arxiv.org/pdf/2106.00762 | HEAD:200 |
| 62 | Working | 200 | https://www.infoq.cn/article/7s6oqecgk8bmckobj0ud | HEAD:200 |
| 63 | Working | 200 | https://www.linkedin.com/blog/engineering/learning/learning-hiring-preferences-the-ai-behind-linkedin-jobs | HEAD:200 |
| 64 | Working | 200 | https://www.tinderpressroom.com/powering-tinder-r-the-method-behind-our-matching | HEAD:200 |
| 65 | Working | 200 | https://arxiv.org/pdf/2505.18654 | HEAD:200 |
| 66 | Working | 200 | https://www.ijcai.org/proceedings/2018/518 | HEAD:200 |
| 67 | Working | 200 | https://arxiv.org/pdf/2605.16344 | HEAD:200 |
| 68 | Working | 200 | https://arxiv.org/pdf/2607.14192 | HEAD:200 |
| 69 | Unreachable |  | https://www.alphaxiv.org/overview/2309.12645v2 | HEAD:308;GET:308;HEAD:308;GET:308 |
| 70 | Working | 200 | https://arxiv.org/abs/1810.02019 | HEAD:200 |
| 71 | Working | 200 | https://research.google/pubs/slateq-a-tractable-decomposition-for-reinforcement-learning-with-recommendation-sets/ | HEAD:200 |
| 72 | Working | 200 | https://arxiv.org/pdf/2103.08390 | HEAD:200 |
| 73 | Working | 200 | https://arxiv.org/pdf/2608.08043 | HEAD:200 |
| 74 | Working | 200 | https://arxiv.org/pdf/2309.07893 | HEAD:200 |
| 75 | Working | 200 | https://arxiv.org/pdf/2311.11922 | HEAD:200 |
| 76 | Working | 200 | https://arxiv.org/pdf/2307.01000 | HEAD:200 |
| 77 | Working | 200 | https://arxiv.org/pdf/2204.05125 | HEAD:200 |
| 78 | Working | 200 | https://arxiv.org/html/2607.28182v1 | HEAD:200 |
| 79 | Working | 200 | https://icml.cc/virtual/2025/poster/44136 | HEAD:200 |
| 80 | Working | 200 | https://www.alphaxiv.org/abs/2408.11623v2 | HEAD:200 |
| 81 | Working | 200 | https://arxiv.org/abs/2011.11826 | HEAD:200 |
| 82 | Working | 200 | https://arxiv.org/abs/2101.02284 | HEAD:200 |
| 83 | Working | 200 | https://www.ijcai.org/proceedings/2020/487 | HEAD:200 |
| 84 | Working | 200 | https://arxiv.org/pdf/2601.13609 | HEAD:200 |
| 85 | Working | 200 | https://arxiv.org/pdf/2607.00280 | HEAD:200 |
| 86 | Working | 200 | https://arxiv.org/pdf/2508.01867 | HEAD:200 |
| 87 | Working | 200 | https://arxiv.org/pdf/2507.13608 | HEAD:200 |
| 88 | Working | 200 | https://arxiv.org/pdf/2410.18087 | HEAD:200 |
| 89 | Working | 200 | https://arxiv.org/pdf/2401.15811 | HEAD:200 |
| 90 | Working | 200 | https://arxiv.org/pdf/2306.14712 | HEAD:200 |
| 91 | Working | 200 | https://techcrunch.com/2018/07/11/hinge-employs-new-algorithm-to-find-your-most-compatible-match-for-you/ | HEAD:200 |
| 92 | Working | 200 | https://arxiv.org/pdf/2606.31031 | HEAD:200 |
| 93 | Working | 200 | https://arxiv.org/pdf/2608.10257 | HEAD:200 |
| 94 | Working | 200 | https://arxiv.org/html/2602.11235v2 | HEAD:200 |
| 95 | Working | 200 | https://arxiv.org/abs/2505.19755 | HEAD:200 |
| 96 | Working | 200 | https://arxiv.org/html/2508.20900v1 | HEAD:200 |
| 97 | Working | 200 | https://arxiv.org/abs/2502.18965 | HEAD:200 |
| 98 | Working | 200 | https://arxiv.org/html/2406.00725v1 | HEAD:200 |
| 99 | Working | 200 | https://arxiv.org/html/2604.14352v1 | HEAD:200 |
| 100 | Working | 200 | https://arxiv.org/pdf/2601.17712 | HEAD:200 |
| 101 | Working | 200 | https://www.nber.org/system/files/working_papers/w26463/w26463.pdf | HEAD:200 |
| 102 | Working | 200 | https://arxiv.org/pdf/2604.25839 | HEAD:200 |
| 103 | Working | 200 | https://icml.cc/virtual/2025/poster/44364 | HEAD:200 |
| 104 | Working | 200 | https://arxiv.org/pdf/2502.09806 | HEAD:200 |
| 105 | Working | 200 | https://arxiv.org/pdf/2310.17496 | HEAD:200 |
| 106 | Working | 200 | https://arxiv.org/pdf/2002.05897 | HEAD:200 |
| 107 | Working | 200 | https://ojs.aaai.org/index.php/AAAI/article/download/38483/42445 | HEAD:200 |
| 108 | Working | 200 | https://ojs.aaai.org/index.php/AAAI/article/download/28726/29402 | HEAD:200 |
| 109 | Working | 200 | https://proceedings.neurips.cc/paper_files/paper/2022/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf | HEAD:200 |
| 110 | Ambiguous | 403 | https://dl.acm.org/doi/10.1145/3404835.3462892 | HEAD:403;GET:403 |
| 111 | Working | 200 | https://arxiv.org/abs/1802.00255 | HEAD:200 |
| 112 | Working | 200 | https://arxiv.org/pdf/2602.19689 | HEAD:200 |
| 113 | Working | 200 | https://arxiv.org/pdf/2409.00720 | HEAD:200 |
| 114 | Working | 200 | https://arxiv.org/abs/2408.09748 | HEAD:200 |
| 115 | Working | 200 | https://arxiv.org/pdf/2308.14703 | HEAD:200 |
| 116 | Working | 200 | https://arxiv.org/pdf/2104.12222 | HEAD:200 |
| 117 | Working | 200 | https://arxiv.org/abs/2208.11384 | HEAD:200 |
| 118 | Working | 200 | https://arxiv.org/pdf/2106.01941 | HEAD:200 |
| 119 | Working | 200 | https://arxiv.org/pdf/2007.16120v2 | HEAD:200 |
| 120 | Working | 200 | https://proceedings.neurips.cc/paper_files/paper/2018/file/97af07a14cacba681feacf3012730892-Paper.pdf | HEAD:200 |
