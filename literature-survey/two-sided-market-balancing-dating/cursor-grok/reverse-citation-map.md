# Reverse citation / cross-reference map — cursor-grok workplace

Phase 3.7 analog. NotebookLM was disconnected this run (`Not connected` / `-32000`), so this map is from **this workplace’s annotated corpus + `read-papers/` notes**, not from a full-notebook `notebook_query` or from reading every PDF’s related-work section. Do not treat it as a complete citation graph of the shared notebook.

**Relations recorded:** 18 directed “mentions / builds-on” edges among workplace items.

## Scoring lineage (D1)

```
RECON (Pizzato UMUAI 2013 / RecSys 2010)
  → Palomares survey 2021 (taxonomy + aggregation)
  → Kleinerman RecSys 2018 (reply weight α; live dating A/B)
  → Xia ASONAM 2015 (Baihe CF; cited by GFRR)
  → Ramanathan AAAI 2021 (Tapple dual embeddings + recency rerank)
      → Tomita RecSys 2022 talk (TU on Tapple)
      → Tomita RecSys 2023 TU/IPFP+MIPS
          → Tomita RecSys 2024 NSW
          → Tomita RecSys 2026 MODE
          → Kishimoto et al. MRet 2026 (retention-weighted)
  → GFRR IEEE Access 2023 (send/reply GNN; parallel to TU, not cited by TU notes)
  → CUPID 2024 (Azar session-cached duration; social discovery, not dating)
  → Tinder ES8 2025 (2T P(Match) vs P(Like) online)
  → OkCupid JAX 2021 (voter vs votee vectors)
  → Hinge 2025 product posts (DL mutual compatibility; no method citations)
```

## Jobs analog (D2–D4)

```
Lee KDD 2014 impression discounting
  → LiJAR KDD 2017 (forecast + boost/penalize)
      → Geyik KDD 2019 DetGreedy (same Talent/Recruiter stack)
      → LinkSAGE KDD 2025 (Borisyuk coauthor; GNN matching, not redistribution)
      → Kanzhun IR / CMBI 2025 (product: traffic → more responsive users)
Yang RecSys 2022 DPGNN / Hu KDD 2023 BOSS (BOSS Zhipin ranking papers)
Mashayekhi CSUR 2024 (e-recruitment survey; cites LiJAR; omits dating)
Kaya RecSys 2025 (Jobindex; stakeholder fairness interviews, not a ranker)
```

## Assortment / market design (D5)

```
Rios, Saban, Zheng M&SOM 2023 (field assortment; GSB page +40% matches)
  → Dating Heuristic arXiv:2308.02584 (1−1/e; who initiates)
Ashlagi et al. OR 2022 (sequential matching assortment)
Arnosti, Johari, Kanoria M&SOM 2021 (application caps)
Kanoria & Saban MS 2021 (which side searches; Bumble analog)
Halaburda et al. MS 2018 (restrict N)
Fong Marketing Science 2024 (thickness × like limits)
Lee & Niederle 2015 (roses)
```

## Evaluation (D7)

```
Johari, Li, Liskovich, Weintraub MS 2022 (randomize the congested side)
  → Holtz et al. MS 2025 (Airbnb cluster RCT; 19.8% of TATE was interference)
  → Nassiri & Bright Lyft MMV 2025 (user-split × shadow price)
  → Nandy et al. UniCoRn NeurIPS 2021 (producer-side design; LinkedIn edges)
Hayashi, Goda, Saito RecSys 2025 DiPS/DPR (Wantedly jobs OPE; names dating, eval is jobs)
Ramanathan AAAI 2021 location-grouped A/B (dating spillover control, not OPE)
```

## RecSys 2025 program mine (accepted list, live page)

On-target matching paper in the 2025 accepted list: **Hayashi/Goda/Saito OPE** (already in bib). Adjacent, not added as method templates: LCM4Rec (Krause & Oosterhuis; choice/cannibalization); Kaya & Bogers Jobindex multi-sided fairness interviews. Amazon two-stage candidate-generator OPE is retrieval OPE, not matching-market OPE.

## Nulls that affect the map

- No paper in this corpus is a **dating-log OPE**. Hayashi’s abstract mentions dating; the experiment is Wantedly Visit.
- No **Bumble Tech** ranking paper exists to hang on the Kanoria–Saban “short side proposes” node.
- **Hinge 2025** posts do not cite Gale–Shapley; the 2018 TechCrunch piece is press, not a method parent.
