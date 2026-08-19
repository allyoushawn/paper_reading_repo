# two-sided market balancing — Methodology Fundamentality Tracking

Filled from NotebookLM per-source extracts plus publisher-verified field-experiment numbers. Not a 200-paper Phase 3.5 close-out.

## Methodology Table

| Method | Source (strongest) | Baseline mention count (this run) | Derived variant count | Independent measured performance | Components (simplicity) | Dating fit |
|---|---|---|---|---|---|---|
| Reciprocal aggregation (harmonic / C±) | Pizzato et al., UMUAI 2013 (RECON) | 6 (Palomares, Kleinerman, CRRS, ReSeq, DPGNN, CyberAgent blogs) | 3 (LFRR, RWS, CRRS vacant-slot) | Top-10 success 42.2% vs 23.0% non-reciprocal on AU dating site | 2 (content prefs + harmonic) | High |
| Personalized reply weight (RWS) | Kleinerman et al., RecSys 2018 | 1 | 0 | Live dating app: replies 99→322; recommends less popular users | 3 (CF + AdaBoost reply + per-user α) | High |
| TU / Choo–Siow + IPFP (+ MIPS) | Tomita et al., RecSys 2023; RecSys 2022 Tapple talk | 4 (Fair NSW, MODE, MRet, JP blogs) | 2 (NSW, MODE) | Real JP dating data; scales where SW fails; synthetic n=100: 152 vs 106 Naive matches | 2 (IPFP equilibrium + vectorized score) | High |
| Nash social welfare / envy-free exposure | Tomita & Yokoyama, RecSys 2024 | 2 | 1 (2026 NSW arXiv variant in notebook) | Dating logs: male envy 736→31 vs TU; matches 90 vs 103 | 2 (Frank–Wolfe NSW + ranking) | High |
| MODE (mutually optimal direct effects) | Tomita, RecSys 2026 | 0 | 1 (builds on TU) | Dating logs, 1000×1000: >10% matches vs Naive/Reciprocal/TU | 2 (iterative deterministic lists) | High |
| LiJAR forecast + boost/penalize | Borisyuk, Zhang, Kenthapadi, KDD 2017 | 2 | 0 | +12% application entropy; −8.7% over-served apps; +6.5% engagement underserved | 3 (forecast, thresholds, score multiplier) | High analog |
| Impression discounting | Lee et al., KDD 2014 | 1 | 0 | PYMK online: up to +13.26% invitation rate | 2 (decay × rank score) | High analog |
| Assortment / Dating Heuristic | Rios, Saban, Zheng, M&SOM 2023 | 1 | 1 (Ashlagi sequential assortment) | Field: ≥27% more matches vs partner algorithm | 3 (preference model, match-stock, MIP/heuristic) | High |
| Like / application limits | Arnosti, Johari, Kanoria, M&SOM 2021; Fong 2024 | 3 | 0 | Theory: Pareto ≥3/4 of opt welfare; Fong: +25% members can cut matches 12–17% unless like limit rises | 1 (cap) | High |
| Which-side-searches restriction | Kanoria & Saban, MS 2021 | 2 | 0 | Asymmetric markets: block long side from proposing | 1 (who can initiate) | High |
| Scarce signaling (roses) | Lee & Niederle, Exp. Econ. 2015 | 1 | 0 | Rose +3.3pp accept (~+20% rel.); 8 vs 2 roses: +44–48% dates (men) | 1 (token) | High |
| Fairness-of-exposure LP | Singh & Joachims, KDD 2018 | 2 | 1 (Do Lorenz) | Job-seeker sim: DTR 1.75→1.00, DCG 3.82→3.80 | 2 (LP + Birkhoff) | Medium |
| Lorenz / two-sided welfare | Do et al., NeurIPS 2021 | 1 | 0 | Higgs reciprocal: worst-off 10% utility more than doubles vs linear welfare | 2 (Frank–Wolfe + concave W) | High (reciprocal section) |
| CRRS causal + vacant-slot rerank | Yang et al., KDD 2024 | 1 | 0 | Dating CRecall@50 0.339 vs 0.301 DPGNN | 3 (causal RRS, metrics, rerank) | High |
| Matching-market OPE (DiPS/DPR) | Hayashi, Goda, Saito, RecSys 2025 | 0 | 0 | Wantedly A/B logs: lower MSE than IPS/DR at 1.2% match sparsity | 3 (DM + IPS + intermediate labels) | High analog |
| Two-tower P(Match) vs P(Like) | Sokolov, Hickey, Du, Tinder Tech Blog 2025 | 0 | 0 | +6.5% match rate and +22% match volume vs +3.8% SRR for P(Like) | 2 (two-tower retrieve + ES plugin score) | High |
| Dual directed embeddings + recency rerank | Ramanathan et al., AAAI 2021 (Tapple) | 1 (later TU papers) | 1 (TU/IPFP line) | +16.9% match recall vs match-only RS; conversion +60% after rerank | 3 (two directed models, fusion, online rerank) | High |
| Session-cached reciprocal duration | CUPID, Kim et al. 2024 (Azar) | 0 | 0 | Chat duration +6.8%; long-match +12.6%; p90 −79.7% | 3 (async session, dual projection, two-phase train) | Medium-high |
| DetGreedy representative rerank | Geyik, Ambler, Kenthapadi, KDD 2019 | 1 (LinkedIn fairness blog) | 0 | ~3× searches with representative gender mix; business metrics flat | 2 (target mix + DetGreedy) | Medium |
| MMV / shadow-price ATE correction | Nassiri & Bright, Lyft Eng 2025 | 0 | 0 | 10% of launch decisions flip vs naive user-split; ~45% smaller magnitude when congested | 2 (hourly dispatch duals + CUPED) | Medium (match-based, not swipe-choice) |
| Two-sided / cluster randomization | Johari et al., MS 2022; Holtz et al., MS 2025 | 2 | 1 (Bajari MRD) | Holtz Airbnb: 19.8% of naive TATE was interference | 2 (design + cluster embeddings) | High |
| UniCoRn producer-side design | Nandy et al., NeurIPS 2021 (LinkedIn) | 0 | 0 | Edge recs: cand-gen +0.51% WAU / +0.57% sessions; rank +0.13% WAU / +0.11% sessions (p<0.001) | 2 (α-mix counterfactual ranks) | High analog |
| GFRR send/reply GNN | Zhang, Wang, Yamasaki, IEEE Access 2023 | 1 (Xia) | 0 | Dating logs: send AUC 73.15% (+3.20pp), fusion 71.26% (+4.35pp) | 3 (bipartite GNN, two heads, fusion) | High scoring |
| MRet retention-weighted matching | Kishimoto et al., arXiv:2602.15752 | 0 | 0 | Authors claim higher retention vs match-max / fairness baselines on dating data (preprint; numbers not independently re-read) | 2 (retention curves + LTR) | High |

## How to Compute the Fundamentality Composite Score

Not computed formally (sample is a 72-item industry survey, not 200-paper tracker). Rank by (a) dating-platform evidence, (b) reuse as a baseline by later matching papers, (c) implementability in a ranking stack.

## Top Method Analysis

1. **TU / Choo–Siow reciprocal ranking** — only production-shaped method that jointly encodes mutual preference *and* capacity, with a Tapple deployment trail (RecSys 2022 talk → RecSys 2023 paper → RecSys 2024 NSW → RecSys 2026 MODE).
2. **LiJAR-style redistribution** — closest non-dating production analog for “too many likes on the head, too few on the tail.”
3. **Assortment with match-stock dynamics** — only large dating *field* lift we have (≥27% matches).
4. **RECON-style reciprocal aggregation** — still the scoring primitive everything else sits on; 42% vs 23% success is the classic number.
5. **Interference-aware evaluation (Johari / MMV / DiPS)** — without this, patterns 1–4 cannot be A/B'd honestly on a two-sided product.
