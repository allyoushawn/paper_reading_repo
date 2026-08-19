# Discovery Notes — codex-sol Phase 2

Date: 2026-08-18  
Notebook: `two-sided-market-balancing-dating` (`d3071ac8-16ef-4460-8991-7701679974c8`)

## Baseline and local curated-repo scan

- `notebook_list` and `notebook_get` confirmed the required existing notebook and **141 sources** before this run. No notebook was created.
- The local Awesome Deep Learning Papers repository was resolved through the repo registry, was already on `master`, and `git pull origin master` reported `Already up to date.` Its keyword filename scan found the Airbnb KDD 2018 embedding paper and LinkedIn 2025 job-search paper, both already present in NotebookLM; it produced **no new core reciprocal/capacity paper**.
- The shared seed URLs were confirmed as already ingested by matching the shared queue source IDs against the live NotebookLM source list. They were not re-added.

## Required NotebookLM discovery passes

### Pass 1 — paper/topic keywords

- Query: `two-sided market balancing dating-app recommendation reciprocal recommender systems exposure allocation capacity constraints congestion matching markets assortment optimization fairness of exposure marketplace interference`
- `research_start` task ID: `ChAzNzExMTkzYzY4MTkxMGY1EAgaBGEzYTQqA3Vzdw`
- Canonical task ID returned by polling: `2fb9291b-2af4-4b5e-9c50-f2a74aaefe19`
- Final status: `completed`; 67 hits.
- Full-result review: most high-fit hits were duplicates of existing sources (MODE, Counterfactual RRS, Assortment Planning, Dating Heuristic, reciprocal-recsys survey, experimental design, Airbnb cluster randomization). One new high-fit source was imported: **Reducing Marketplace Interference Bias Via Shadow Prices** (hit index 10), source ID `14292df1-f11b-4d0b-b404-db226ca1e99e`.

### Pass 2 — companies, engineering blogs, industry venues, and local languages

- Query: `Tinder Hinge Bumble Badoo OkCupid Match Grindr Pairs Tapple Tantan Momo Soul LinkedIn Indeed ZipRecruiter BOSS Zhipin Upwork Airbnb Uber Lyft DoorDash Etsy Thumbtack Spotify Kuaishou TikTok engineering blog reciprocal recommendation marketplace balancing RecSys industry 2025 2026 KDD applied data science 相互推荐 双边推荐 婚恋推荐 相互推薦 マッチングアプリ 推薦 reciprocal recommender survey 2022 2023 2024 2025 2026`
- `research_start` task ID: `ChBiMzcwODQzYWQ2ZGU2N2RjEAgaBGJiOWYqA3Vzdw`
- Canonical task ID returned by polling: `98d070bb-d85b-4e99-a1f5-f458b807a730`
- Final status: `completed`; 75 hits.
- Full-result review: the strongest high-fit results (Revisiting RRS, GraphMatch, Tinder Elasticsearch, Uber marketplace balance, Airbnb two-sided preferences) were already in the notebook. The pass also returned SEO/consumer explainers, generic platform-strategy pages, and single-sided retrieval work, which were not imported.
- A separate verified Japanese query found a genuinely new industry source, **相互推薦における嗜好の集約をパーソナライズする試み** (Wantedly Engineer Blog, 2026). It was added with `source_add` as source ID `8f872a8a-ca7f-4c9d-ada5-bb124b6b75d7`.
- No third industry pass was required: the final selection is 86.7% Tier 1+2, above the 60% threshold.

## Web query log and named nulls

Queries used in addition to the two NotebookLM passes:

- `site:recsys.acm.org/recsys25 matching marketplace reciprocal recommendation industry`
- `site:recsys.acm.org/recsys26 reciprocal recommendation marketplace industry`
- `site:arxiv.org reciprocal recommender systems survey 2022 OR 2023 OR 2024 OR 2025 OR 2026`
- `site:medium.com/bumble-tech ranking recommendation matching algorithm`
- `相互推荐 双边推荐 婚恋推荐 交友推荐 推荐 生态健康 算法 工程`
- `相互推薦 マッチングアプリ 推薦 双方向 レコメンド エンジニアリング`
- `site:developers.cyberagent.co.jp マッチングアプリ 推薦 相互推薦`
- `site:tech.bumble.com OR site:medium.com/bumble-tech recommendation ranking matching`
- Exact-title searches for selected sources and their free versions, including Spotify fair marketplace, Joint Multisided Exposure Fairness, Thumbtack, Integrating Predictive Models, CyberAgent, BOSS, Hinge, and the Chinese/Japanese sources.

Named null or low-yield results:

- **Bumble Tech:** publication exists, but no ranking/recommendation/matching-mechanics post was found; returned code review and mobile-test automation posts only.
- **Post-2021 reciprocal-recsys survey:** no free, general reciprocal-recommender survey paper newer than Palomares et al. (2021) was found. The 2025 SpringerBriefs book was paywalled; 2024 *Revisiting Reciprocal Recommender Systems* is a method/formulation paper, not a survey.
- **RecSys 2026 matching/industry papers:** the official site had the call, dates, and tutorials, but no public accepted-contributions list or matching-market industry paper at search time. This is logged as a venue null, not evidence that none will appear.
- **Dating-app primary engineering ranking posts:** no new ranking-mechanics post was found for Badoo, Bumble, Match Group outside Tinder/Hinge, Grindr, eHarmony, Zoosk, Tantan, Momo, Soul, Baihe, or Jiayuan. Grindr's available post explicitly describes distance-sorted filtering rather than a recommender. Coffee Meets Bagel yielded infrastructure detail only.
- **Chinese official dating engineering sources:** Tantan, Momo, Soul, Baihe, and Jiayuan returned no official reciprocal-ranking engineering source. Third-party/SEO results were rejected.
- **Japanese search:** not null. CyberAgent/Tapple and Wantedly produced direct engineering sources; Pairs/Eureka was already represented in the notebook.
- **Local Awesome repository:** no new core paper after duplicate removal.
- **Upwork, Hired, Etsy, and Meta/PYMK in the company pass:** no new high-fit capacity-balancing or interference source beyond material already in the notebook. Indeed, DoorDash, Uber, Lyft, Airbnb, and Kuaishou did return industry material, but most was either already present or too adjacent for the 45-item selection.

## Link and metadata verification

- All 45 selected rows were checked against the live NotebookLM source list; **missing source IDs: 0**.
- Direct HTTP checks returned 200 for 43 selected URLs. Two bot-sensitive exceptions were independently verified:
  - **BOSS**: ACM returned HTTP 403 to `curl`; title, authors, year, and abstract were verified on the official KDD 2023 proceedings page, while the full ACM PDF is already successfully indexed as the selected NotebookLM source.
  - **Towards a Fair Marketplace**: the author PDF timed out in `curl`, but the page/PDF was opened through web retrieval and its title, authors, venue, year, and content were verified; the same full paper is indexed in NotebookLM.
- An initially guessed Hinge newsroom path returned 404. NotebookLM source content exposed the canonical `https://hinge.co/how-we-connect-daters`, which then returned HTTP 200; only that corrected URL appears in the queue.
- Metadata was triangulated from primary/free pages, arXiv records, author/institution PDFs, official conference pages, and source text already indexed in NotebookLM. No title or year was inferred from an unverified search snippet alone.

## Paywall and fallback log

- Palomares et al. (2021): Elsevier landing page avoided; selected the free University of Jaén author/institution PDF.
- Fong (2024): INFORMS landing page avoided; selected the free UCLA working-paper version and retained the published 2024 title, noting that the ingested text carries the earlier working title.
- Mehrotra et al. (2018): ACM landing page avoided; selected the author's free PDF.
- LinkedIn Talent Search fairness (2019), Fairness of Exposure (2018), Two-Sided Fairness via Lorenz Dominance (2021), UniCoRn (2021), and the RecSys/KDD reciprocal papers: selected arXiv or author/institution versions where available.
- BOSS (2023): official ACM URL was bot-blocked during direct verification; official KDD proceedings metadata plus the already-ready NotebookLM full-paper source were used. No unverified mirror was selected.
- RECON (2010), Neve and Palomares (2019), and the 2025 SpringerBriefs volume remained paywalled after the documented arXiv/SSRN/Semantic Scholar/author-page fallback history in the shared queue; none was selected.
- No selected item has `nlm:failed:*` status.

## Source additions and duplicates avoided

- Added 2 sources to NotebookLM:
  1. Wantedly Engineer Blog (2026), source `8f872a8a-ca7f-4c9d-ada5-bb124b6b75d7`.
  2. Reducing Marketplace Interference Bias Via Shadow Prices (2022), source `14292df1-f11b-4d0b-b404-db226ca1e99e`.
- Notebook source count: **141 → 143 (delta +2)**.
- Duplicate imports avoided included MODE (multiple URLs), Revisiting RRS (arXiv plus institution PDF), Fair Marketplace (paper plus Spotify listing), Tinder Elasticsearch (duplicate hostnames), Fairness-Aware LinkedIn Talent Search (duplicate PDFs), Counterfactual RRS, GraphMatch, Dating Heuristic, the 2021 reciprocal-recsys survey, and RecSys 2025 OPE.

## Final selection and coverage

- Selected: **45**.
- Tier 1: 24 (53.3%). Tier 2: 15 (33.3%). Tier 3: 6 (13.3%). Tier 1+2: **39/45 (86.7%)**.
- Multi-tag direction coverage: D1 19, D2 7, D3 8, D4 14, D5 10, D6 8, D7 8, D8 7.
- Every direction has selected coverage. D2 and D8 are the thinnest at seven tagged sources each; D8 nevertheless includes both Japanese company engineering work and a Chinese industry experimentation source.
