# Seed gap check and null results (cursor-grok, 2026-08-16)

Notebook already had 119 sources at run start (claude_opus ingest). cursor-grok verified seeds, added missing free URLs, and logged nulls. Shared `requirements.md` / `README.md` not rewritten.

## Seed coverage vs notebook (44 Must Include)

### Present (free URL already ingested)
A: Tinder newsroom 2019; TinVec MLconf 2017 PDF; Hinge TechCrunch 2018; Quartz Gini 2017; OkCupid OkTrends 2009; eHarmony slides; CMB AWS case study.
B: CyberAgent RecSys 2023 arXiv 2306.09060; Fair Reciprocal RecSys 2024 arXiv 2409.00720; Revisiting RRS KDD 2024 arXiv 2408.09748; DPGNN RecSys 2022 arXiv 2208.08612; ReSeq RecSys 2023 arXiv 2306.14712; BOSS KDD 2023 ACM PDF; LiJAR Stanford PDF; Impression discounting KDD 2014 gersteinlab PDF; Spotify CIKM 2018 + marketplace page; Airbnb host-preferences; Airbnb KDD 2018 PDF.
C: Rios dating_alf.pdf; Ashlagi assortment.pdf; Kanoria facilitating-search.pdf; Arnosti congestion.pdf; Halaburda PlatStrat PDF; Fong UCLA working paper; Lee-Niederle rose PDF; Hitsch matching PDF; Bruch-Newman arXiv 1808.04840; Xia arXiv 1501.06247 (assumed; verify in bib); Tu arXiv 1401.8042 (assumed; verify in bib).
D: Johari arXiv 2002.05670; Bajari arXiv 2112.13495; Holtz Columbia PDF; Lyft MMV 2025; DoorDash switchback 2025.
E: Palomares survey PDF; Pizzato UMUAI Dropbox PDF; Do et al. arXiv 2110.15781; Singh-Joachims arXiv 1802.07281; Christakopoulou CIKM 2017 author PDF.

### Added this run
- Kleinerman RecSys 2018 author PDF (`u.cs.biu.ac.il/~sarit/...`)
- Hayashi/Goda/Saito RecSys 2025 OPE matching markets arXiv 2507.13608
- Tomita MODE RecSys 2026 arXiv 2608.01731 (notebook already had an earlier MODE HTML)
- Tomita RecSys 2022 industry talk arXiv 2208.11384 (added after first bulk; 2201.11331 was a mistaken ID)
- Jiayuan/Tencent Cloud 2018 reciprocal-recsys debate
- Wantedly RecSys 2025 company post

### Failed / paywall / not found
- **Bumble Tech ranking post:** Medium publication exists; no ranking/matching engineering post located. Third-party “algorithm explained” posts are speculation — not cited. Job posting mentions “marketplace health” but is not a primary source. **Null.**
- **RECON RecSys 2010:** ACM paywalled. Checked arXiv, SSRN, Semantic Scholar OA, author `.edu.au` pages. No stable free PDF. Cite via Palomares 2021 + Pizzato UMUAI 2013 which restates RECON. **nlm:failed:paywall**
- **Neve & Palomares RecSys 2019:** ACM paywalled. No arXiv/SSRN/author PDF found. Harmonic-mean aggregation restated in later papers. **nlm:failed:paywall**
- **FAIR-MATCH arXiv 2507.01063:** `source_add` of pdf URL resolved to arXiv homepage, not the paper. Treat as uncertain / skip unless HTML ingest succeeds.
- **RecSys 2026 industry track papers:** conference is 2026-09-27–10-02; CFP is live; industry papers not posted as of 2026-08-16. MODE (research track) is the RecSys 2026 hit. **Null for industry track.**

## Blind-spot re-search

1. Dating-app engineering ranking posts: OkCupid tech blog (JAX CF; AI principles) and Eureka (Pairs) ethics post exist; Tinder newsroom + MLconf; Grindr ADM transparency page. Still no Tinder/Hinge/Bumble *engineering* ranking post with model detail.
2. Reciprocal-recsys *survey* after 2021: none found. Closest: Yang et al. KDD 2024 “Revisiting Reciprocal Recommender Systems” (metrics/formulation/method paper, not a survey). Palomares et al. 2021 remains the last dedicated survey.
3. RecSys 2025: Wantedly “Off-Policy Evaluation and Learning for Matching Markets” (full paper). RecSys 2026: CyberAgent MODE.

## Awesome recsys repo Step 0
Filename glob for reciprocal / LiJAR / marketplace / matching / exposure / capacity returned 0 files. Repo is CTR/ranking-heavy; two-sided matching is outside its folder taxonomy. Recorded as **null from local-awesome-repo**.
