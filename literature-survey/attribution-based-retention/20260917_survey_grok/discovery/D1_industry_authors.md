# D1 — Industry author / team discovery (2025-01 through 2026-09)

Discovery agent run: 2026-09-17. Scope: papers and production write-ups on attribution, incrementality, and attribution-adjacent measurement.

**Already in parent (skip as NEW; still listed per team where relevant):**
- *LiDDA: Data Driven Attribution at LinkedIn* (arXiv:2505.09861)
- *Amazon Ads Multi-Touch Attribution* (arXiv:2508.08209)
- *See Beyond a Single View: Multi-Attribution Learning…* / MAL (KDD CIKM 2025; arXiv:2508.15217)
- *MAC: A Conversion Rate Prediction Benchmark…* / MoAE (KDD 2026; arXiv:2603.02184)
- *Click A, Buy B* / CABB (KDD 2025; arXiv:2507.15113)
- *Beyond Last-Click: An Optimal Mechanism for Ad Attribution* / PVM (NeurIPS 2025; arXiv:2511.22918)
- *Statistical Learning from Attribution Sets* (COLT 2026; arXiv:2602.06276)

---

## LinkedIn — Bencina, LiDDA, LinkedIn data-driven attribution, marketing science

**Queries run:**
- `LinkedIn Bencina LiDDA data driven attribution 2025 2026`
- `John Bencina LinkedIn attribution arxiv 2025 2026`
- `site:engineering.linkedin.com attribution data-driven 2025 2026`

**Already in parent:** *LiDDA: Data Driven Attribution at LinkedIn* (John Bencina et al.; arXiv:2505.09861; transformer DDA + MMM calibration; large-scale LinkedIn GTM/LMS deployment).

### NEW candidates

| year | title | authors/org | venue or blog | URL | Q1/Q2 | why relevant | free PDF URL |
|------|-------|-------------|---------------|-----|-------|--------------|--------------|
| 2025 | Buyer Journey Insights with Data-Driven Attribution | John Bencina, Erkut Aykutlug, Flora Chen, Zerui Zhang, Changshuai Wei, Stephanie Sorenson, Shao Tang / LinkedIn GTM AI + LMS | LinkedIn Engineering blog | https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution | Q2 | Production write-up of hybrid MTA+MMM DDA rollout (probabilistic paid-media touchpoints, holdout/MMM calibration); predates/publicizes LiDDA system goals | n/a (blog) |

**Notes:** csauthors.net lists only one 2025 paper for John Bencina (LiDDA). No additional arXiv/venue hits for Bencina or LinkedIn marketing-science attribution in window.

---

## Amazon Ads — Randall Lewis, Florian Zettelmeyer, Brett Gordon, Cristobal Garib, Johannes Hermle; Amazon MTA causal calibration

**Queries run:**
- `Amazon Ads Randall Lewis Florian Zettelmeyer multi-touch attribution causal calibration 2025 2026`
- `site:amazon.science Randall Lewis attribution 2025`
- `site:amazon.science attribution advertising 2025 2026`

**Already in parent:** *Amazon Ads Multi-Touch Attribution* (Randall Lewis, Florian Zettelmeyer, Brett R. Gordon, Cristobal Garib, Johannes Hermle et al.; arXiv:2508.08209; RCT + ML causal calibration models for touchpoint credit).

**nothing new found** for these named authors on Amazon Ads MTA / causal calibration beyond the parent paper and third-party summaries (e.g., sellermetrics.app guide citing the same system).

**Notes:** Amazon Science has 2025 “attribution” papers (supply-chain SCM, multi-agent error attribution) but none authored by Lewis/Zettelmeyer/Gordon/Garib/Hermle on advertising MTA. Randall Lewis author page on amazon.science shows no new ads-MTA publication in window.

---

## Alibaba / Alimama — Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu, Jian Xu, Bo Zheng, Jinqi Wu; MAL, MoAE, MAC

**Queries run:**
- `Alibaba Alimama MAL multi-attribution learning MoAE MAC Sishuo Chen 2025 2026`
- `"Can Large Language Models Identify Meaningful Touchpoints" LOTUS arxiv 2608.28649 venue`

**Already in parent:**
- *See Beyond a Single View: Multi-Attribution Learning…* / MAL (Chen, Chan, Sheng, Zhu, Xu, Zheng et al.; CIKM 2025; arXiv:2508.15217)
- *MAC: A Conversion Rate Prediction Benchmark…* incl. MoAE (Wu, Chen, Chan et al.; KDD 2026; arXiv:2603.02184; PyMAL: https://github.com/alimama-tech/PyMAL)

### NEW candidates

| year | title | authors/org | venue or blog | URL | Q1/Q2 | why relevant | free PDF URL |
|------|-------|-------------|---------------|-----|-------|--------------|--------------|
| 2026 | Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution? (LOTUS) | Jinqi Wu, Sishuo Chen, Zhangming Chan, Yong Bai, Chao Yi, Han Zhu, Shuodian Yu, Lei Zhang, Sheng Chen, Chenghuan Hou, Jian Xu, Chaoyou Fu / Alibaba (Taobao & Tmall) | CIKM 2026 short paper (accepted; arXiv preprint) | https://arxiv.org/abs/2608.28649 | Q1 | LLM-based touchpoint selection for conversion attribution; human-aligned semantic labels as auxiliary CVR training signal; beats in-shop baseline and CABB heuristic on production-scale offline GAUC | https://arxiv.org/pdf/2608.28649 |

**Notes:** MoAE is part of the MAC paper (already in parent), not a separate publication.

---

## Google — Aiyou Chen, Jon Vaver, Mukund Sundararajan, Badih Ghazi; Trimmed Match, TEDDA, Privacy Sandbox, attribution sets 2026

**Queries run:**
- `Google Aiyou Chen Jon Vaver Trimmed Match TEDDA Privacy Sandbox attribution sets 2025 2026`
- `site:arxiv.org attribution sets 2026 Google Chen`
- `site:research.google attribution 2025 2026`
- `Badih Ghazi attribution advertising 2025 2026`
- `Privacy Sandbox attribution reporting 2025 2026 Google blog update`
- `Jon Vaver Mukund Sundararajan attribution 2025 2026 Google`
- `TEDDA Google attribution arxiv 2025`

**Already in parent:** *Statistical Learning from Attribution Sets* (Applebaum, Busa-Fekete, August Y. Chen, Gentile, Koren, Mokhtari; COLT 2026; arXiv:2602.06276) — privacy-limited learning from candidate-click sets motivated by Privacy Sandbox.

**Legacy (out of window, no 2025–2026 update found):**
- Trimmed Match / TMD (Aiyou Chen; AOAS 2021; arXiv:2105.07060) — geo-experiment iROAS, not new in window.
- TEDDA — *A Time To Event Framework For Multi-touch Attribution* (arXiv:2009.08432, 2020).
- Jon Vaver digital-attribution pubs (2016–2021) on research.google; no 2025–2026 ad-attribution paper found.
- Mukund Sundararajan — ML feature attribution (VisxAI etc.), not ad MTA in window.

### NEW candidates

| year | title | authors/org | venue or blog | URL | Q1/Q2 | why relevant | free PDF URL |
|------|-------|-------------|---------------|-----|-------|--------------|--------------|
| 2025 | On the Differential Privacy and Interactivity of Privacy Sandbox Reports | Badih Ghazi, Charlie Harrison, Arpana Hosabettu, Pritish Kamath, Alexander Knop, Ravi Kumar, Ethan Leeman, Pasin Manurangsi, Mariana Raykova, Vikas Sahu, Phillipp Schoppmann / Google | PoPETs 2025 (vol. 2025, issue 3) | https://doi.org/10.56553/popets-2025-0104 | Q2 | Formal DP analysis of Attribution Reporting API + Private Aggregation API under interactive querying — core privacy guardrails for cookieless conversion measurement | https://arxiv.org/abs/2412.16916 |
| 2025 | Update on Plans for Privacy Sandbox Technologies | Anthony Chavez / Google Chrome Privacy Sandbox | Google Privacy Sandbox blog | https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies | Q2 | Production/policy write-up (Oct 17, 2025): retires Attribution Reporting API (Chrome/Android) and related PS APIs; pivots to W3C interoperable Attribution standard — major shift for attribution measurement infrastructure | n/a (blog) |

**Notes:** Summary Reports Optimization for ARA (PETS 2024) predates window. Third-party “Q3 2026 ARA delay” articles (e.g., perfxad.com) conflict with the Oct 2025 retirement announcement; not treated as authoritative. WICG attribution-reporting-api repo marked scheduled for deprecation/archival.

---

## Meta — Robert Moakler, Julian Runge, Xiangyu Zeng; CABB, Robyn, PIE predicted incrementality

**Queries run:**
- `Meta Robert Moakler Julian Runge Robyn PIE predicted incrementality CABB 2025 2026`
- `NBER w35044 PIE predicted incrementality 2026`
- `Xiangyu Zeng CABB Click A Buy B attribution arxiv 2025`
- `Julian Runge Meta attribution 2025 2026 arxiv`
- `Julian Runge Robyn arxiv 2025 packaging media mix modeling`
- `Robert Moakler Julian Runge Meta incremental attribution research 2025 2026`

**Already in parent:** *Click A, Buy B: Rethinking Conversion Attribution in E-Commerce Recommendations* / CABB (Xiangyu Zeng et al.; KDD 2025; arXiv:2507.15113).

### NEW candidates

| year | title | authors/org | venue or blog | URL | Q1/Q2 | why relevant | free PDF URL |
|------|-------|-------------|---------------|-----|-------|--------------|--------------|
| 2026 | Predicted Incrementality by Experimentation (PIE) for Ad Measurement | Brett R. Gordon, Robert Moakler, Florian Zettelmeyer / Meta Ads Research + Northwestern (+ Amazon affiliations for Zettelmeyer/Gordon) | NBER Working Paper 35044 (Apr 2026); MSI working paper; arXiv v2 updated 2026 | https://www.nber.org/papers/w35044 | Q2 | Scales RCT incrementality to non-experimental campaigns via post-determined features; R² 0.88 vs 0.19 for 7-day last-click on 2,226 Meta experiments; documents parallel Meta Incremental Attribution product | https://arxiv.org/html/2304.06828v2 |
| 2025 | Packaging Up Media Mix Modeling: An Introduction to Robyn's Open-Source Approach (v3) | Julian Runge, Igor Skokan, Gufeng Zhou, Koen Pauwels / Meta Marketing Science | arXiv (v3 revised Jan 24, 2025) | https://arxiv.org/abs/2403.14674 | Q2 | Meta open-source MMM package write-up; explicitly frames privacy-driven shift away from deterministic attribution toward probabilistic MMM — adjacent measurement stack used when MTA degrades | https://arxiv.org/pdf/2403.14674 |

**Production (not counted as paper NEW):** Meta Incremental Attribution in Ads Manager (help center rollout; https://en-gb.facebook.com/business/help/644554008179419) — product surface related to PIE-style incrementality optimization.

**Notes:** Julian Runge acknowledged in PIE but not an author. Meta Engineering 2025–2026 blogs (GEM, Adaptive Ranking Model, sequence learning) are ads-ranking, not attribution/incrementality measurement.

---

## Adobe — Rohan Arava, Ritwik Sinha, David Arbour, DNAMTA

**Queries run:**
- `Adobe Rohan Arava Ritwik Sinha DNAMTA attribution 2025 2026`
- `Rohan Arava Adobe attribution 2025 2026 arxiv`
- `David Arbour Adobe attribution arxiv 2025 2026`
- `Ritwik Sinha David Arbour "Attribution IQ" OR attribution 2025 Adobe`
- `"Graphical Point Process" removal effects multi-touch attribution Management Science 2025 Adobe`

**Name note:** No researcher **Rohan Arava** found. Closest match is **Sai Kumar Arava** (Adobe ML manager; DNAMTA / Attribution AI). DNAMTA itself is AdKDD 2018 (arXiv:1809.02230), outside window.

**Already known (outside window):** DNAMTA — *Deep Neural Net with Attention for Multi-channel Multi-touch Attribution* (Sai Kumar Arava et al.; AdKDD 2018).

### NEW candidates

| year | title | authors/org | venue or blog | URL | Q1/Q2 | why relevant | free PDF URL |
|------|-------|-------------|---------------|-----|-------|--------------|--------------|
| 2025 | A Graphical Point Process Framework for Understanding Removal Effects in Multi-Touch Attribution | Jun Tao, Qian Chen, James W. Snyder, Arava Sai Kumar, Amirhossein Meisami, Lingzhou Xue / Adobe Digital Experience + Penn State | Management Science 71(9), Sep 2025 (online Dec 2024) | https://doi.org/10.1287/mnsc.2023.00457 | Q1 | Path-level MTA via graphical point processes and probabilistic removal effects; Adobe Attribution AI / enterprise analytics line | https://arxiv.org/abs/2302.06075 (preprint) |

**Notes:** Ritwik Sinha + David Arbour have NeurIPS 2025 (*Leveraging semantic similarity for experimentation with AI-generated treatments*; https://research.adobe.com/publication/leveraging-semantic-similarity-for-experimentation-with-ai-generated-treatments/) — experimentation/causal inference, not marketing attribution. Attribution IQ (CIKM 2020 demo) is pre-window.

---

## Criteo — Eustache Diemert, Damien Lefortier, attribution bidding

**Queries run:**
- `Criteo Eustache Diemert Damien Lefortier attribution bidding 2025 2026`
- `Eustache Diemert arxiv 2025 attribution bidding Criteo`
- `Eustache Diemert 2025 WISE private advertising attribution Criteo`

**nothing new found** on attribution-aware bidding or MTA from Diemert/Lefortier in 2025–2026.

**Prior work (out of window):** *Attribution Modeling Increases Efficiency of Bidding in Display Advertising* (Diemert, Meynet, Galland, Lefortier; AdKDD/KDD 2017; arXiv:1707.06409). FiPLA (*Fixed Point Label Attribution for Real-Time Bidding*; Bompaire, Désir, Heymann; MSOM 2024) is Criteo-related but not authored by Diemert/Lefortier and outside window.

**Tangential 2025 hit (not attribution bidding):** *CriteoPrivateAd: A Real-World Bidding Dataset to Design Private Advertising Systems* (arXiv:2502.12103) cites the 2017 attribution dataset; Diemert co-authored *Open Research Challenges for Private Advertising Systems Under Local Differential Privacy* (WISE 2024 proc., Springer 2025) — privacy ML, not attribution credit.

---

## Amazon Science / Google Research / Meta Research blogs (2025–2026 attribution)

**Queries run:**
- `site:amazon.science attribution advertising 2025 2026`
- `site:research.google attribution 2025 2026`
- `site:research.facebook.com OR site:engineering.fb.com attribution incrementality 2025 2026 Meta`
- `Privacy Sandbox attribution reporting 2025 2026 Google blog update`

### NEW production / blog candidates

| year | title | authors/org | venue or blog | URL | Q1/Q2 | why relevant | free PDF URL |
|------|-------|-------------|---------------|-----|-------|--------------|--------------|
| 2025 | A first-of-its-kind experiment to measure the impact of out-of-home advertising | Egor Abramov et al. / Amazon | Amazon Science blog | https://www.amazon.science/blog/a-first-of-its-kind-experiment-to-measure-the-impact-of-out-of-home-advertising | Q2 | Causal OOH ad measurement via randomized transit-line placement + DiD + surveys — experimental incrementality outside click-path MTA | n/a (blog) |
| 2025 | Update on Plans for Privacy Sandbox Technologies | Anthony Chavez / Google | Privacy Sandbox blog | https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies | Q2 | See Google row above | n/a (blog) |

**nothing new found** on Meta Research / Engineering blogs specifically documenting incrementality, MTA, or attribution measurement products in 2025–2026 (Engineering posts cover ranking/GEM/sequence models; Incremental Attribution is documented via Business Help Center, not a research blog post).

**Amazon Science:** No Randall Lewis–authored blog post on Amazon Ads MTA in window; supply-chain “attribution” and LLM error-attribution papers are different problem domains.

**Google Research:** No new Jon Vaver / ad-MTA blog post in window beyond Privacy Sandbox policy shift and PoPETs paper above.

---

## Cross-team arXiv hits (not mapped to a single industry row above)

Found via `site:arxiv.org "multi-touch attribution" 2025 2026 Amazon Google Meta` — included for completeness; authors are not on the follow list.

| year | title | authors/org | venue or blog | URL | Q1/Q2 | why relevant | free PDF URL |
|------|-------|-------------|---------------|-----|-------|--------------|--------------|
| 2025 | Causal-driven attribution (CDA): Estimating channel influence without user-level data | Georgios Filippou et al. / Trinity College Dublin | arXiv preprint | https://arxiv.org/abs/2512.21211 | Q1 | Privacy-era channel MTA from aggregated impressions via PCMCI + SCM (cites Amazon MTA 2025) | https://arxiv.org/pdf/2512.21211 |
| 2026 | Integrated Marketing Attribution (IMA): A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM | Meghana R. Bhat et al. / Lowe's | arXiv preprint | https://arxiv.org/abs/2606.16878 | Q2 | MMM-anchored campaign-level attribution without user tracking; cites Google unified measurement framing | https://arxiv.org/pdf/2606.16878 |

---

## URL verification log

| URL | Status |
|-----|--------|
| https://www.nber.org/papers/w35044 | OK (200) |
| https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies | OK (200) |
| https://arxiv.org/abs/2608.28649 | OK |
| https://arxiv.org/pdf/2608.28649 | OK |
| https://doi.org/10.1287/mnsc.2023.00457 | OK |
| https://www.amazon.science/blog/a-first-of-its-kind-experiment-to-measure-the-impact-of-out-of-home-advertising | OK |
| https://www.linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution | OK (found via search; LinkedIn blog) |
