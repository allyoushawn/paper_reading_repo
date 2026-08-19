# Phase 4 Conflict Check

Date: 2026-08-19  
Scope: every quantitative or foundational cross-paper claim retained in `../literature-review.md` was checked against the named own card(s). NotebookLM conflicts were re-queried with source-scoped follow-ups in `phase4-conflict-nlm-quant.md` and `phase4-conflict-nlm-baselines.md`.

## Quantitative claim checks

| Retained claim | Card evidence checked | Resolution |
|---|---|---|
| RECON S@10 42.20% versus 23.00% unilateral | `2013_UMUAI_RECON_Recommending-People-To-People.md`, main results and bibliography fields | Exact match; retained. |
| LiJAR underserved +6.5%, overserved -8.7%, entropy +12% | `2017_KDD_LiJAR_Job-Application-Redistribution.md`, main results and live experiment | Exact match; retained. Total applications +2.3% is explicitly nonsignificant and is not used as a gain claim. |
| Virtual rose acceptance +3.3 percentage points | `2015_ExpEcon_VirtualRose_Propose-With-A-Rose.md`, main results; source-scoped conflict query | Exact match; retained. NLM Q6/Q7's 7.8-point reading was a middle-recipient subgroup coefficient, not the overall effect, and was excluded. |
| TU synthetic expected matches 152.39 versus reciprocal 129.82; dating 538.97/386.64 versus 491.12/360.05 | `2023_RecSys_TU_Fast-Examination-Agnostic-Reciprocal.md`, main results and bibliography fields | Exact match; retained with market-size and proactive-side context. |
| Fairness of Exposure job DTR 1.7483→1.0000 with DCG 3.8193→3.8044 | `2018_KDD_NA_Fairness-of-Exposure-Rankings.md`, main results | Exact match; retained as an offline job example, not a dating effect. |
| JME GG-F improves at p<0.01 with MovieLens100K NDCG@50 0.3703→0.3692 | `2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md`, main results | Exact match; retained; relevance degradation is explicitly nonsignificant. |
| NSW 90.39 matches and 31/14 envies versus SW 111.37 and 434/331 | `2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md`, main results and bibliography fields | Exact card match; retained. Narrow NLM follow-up confirms Gini is not reported, so all NLM-only NSW Gini values were excluded. |
| OkCupid 66% of male messages target the top 33% of women | `2009_OkTrends_NA_Your-Looks-and-Your-Inbox.md`, bibliography fields | Exact match; retained as observational concentration evidence. |
| Hitsch et al. 71%/56% unrequited contacts and 4.3%/6.4% match conversion | `2010_AER_GaleShapley_Matching-and-Sorting-Online-Dating.md`, main results and bibliography fields | Exact match; retained with side ordering. |
| Airbnb GCR overall interference bias 19.76% | `2025_MgmtSci_GCR_Reducing-Interference-Bias-Airbnb.md`, main results; source-scoped conflict query | Exact match; retained. NLM-only 12.05%/28.65% tightness subgroups were excluded because their difference is not statistically significant and the card does not carry them. |
| ECDA simulation effective dates +7.6%, receiver probability +8.7%, raw dates -24.6%; field ex-top-0.1% +0.003 effective dates, +0.002/+0.005 side probabilities | `2026_arXiv_ECDA_Predictive-Models-Two-Sided-Recommendations.md`, bibliography fields; source-scoped conflict query | Card values retained. NLM-only raw table cells and +0.334 receiver-likes coefficient were excluded from the synthesis. |
| TEC field +9.045 matches per prefecture-day | `2026_arXiv_TEC_Recommendation-Exposure-Favorite-Lists.md`, bibliography fields; source-scoped conflict query | Exact match; retained only in the card and read-first rationale. The nonsignificant -40.458 favorites coefficient was not promoted as an effect. |
| Tier mix 24/15/6 and 39/45 = 86.7%; D1–D8 counts | `queue-codex-sol.md` and `discovery-notes.md` | Exact match; retained. |

## Foundational and baseline checks

| Claim | Evidence checked | Resolution |
|---|---|---|
| DPGNN is a direct baseline in ReSeq and CRRS | `2023_RecSys_ReSeq_Reciprocal-Sequential-Recommendation.md` and `2024_KDD_CRRS_Revisiting-Reciprocal-Recommender-Systems.md` experimental-design/results sections | Confirmed; two uses retained. |
| TU is a direct baseline in Fair Reciprocal Recommendation | `2024_RecSys_NSW_Fair-Reciprocal-Recommendation.md` experimental design | Confirmed; retained. |
| RECON is a direct baseline in Xia et al. 2015 | `2015_ASONAM_RRS_Reciprocal-Recommendation-Online-Dating.md` experimental design | Confirmed; retained; exact lift over RECON remains Not specified. |
| JME extends exposure-fairness formulations | `2022_SIGIR_JME_Joint-Multisided-Exposure-Fairness.md` prior-work comparison | Confirmed as an extension, not counted as a direct baseline. |
| Wantedly reproduces Kleinerman et al.'s personalized harmonic aggregation | `2026_Wantedly_PersonalizedAggregation_Personalizing-Preference-Aggregation.md` abstract and prior-work comparison | Confirmed as a reproduction, not counted as a direct baseline. |

The narrow NotebookLM baseline follow-up independently confirms four using-paper cases: DPGNN in two papers, TU in one, and RECON in one. This resolves Query 5's earlier omission of TU and RECON.

## Excluded conflicts

- NLM-only claims for MODE, Tu et al. 2014, Economist versus Machine, and other sources outside the selected 45 were not used in the bibliography synthesis.
- Hinge's “double-digit match increase” appears only in another workplace's shared requirements summary; the own Hinge card reports no quantitative effect, so the claim was excluded.
- Tapple's cited Gini shift is explicitly secondhand and remains labeled as such only inside its card.
- NLM Query 1–3 method and dataset lists include notebook sources outside the selected corpus; they were treated as discovery context, not evidence for 45-card claims.

## Result

**PASS.** All retained quantitative and foundational cross-paper claims are supported by the named own cards. Conflicting or unsupported NotebookLM-only claims were either corrected through source-scoped follow-up or excluded.
