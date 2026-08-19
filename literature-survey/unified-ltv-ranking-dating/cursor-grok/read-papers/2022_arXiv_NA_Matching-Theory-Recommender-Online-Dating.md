# Paper Analysis: Matching Theory-based Recommender Systems in Online Dating

**Source:** https://arxiv.org/pdf/2208.11384.pdf  
**Date analyzed:** 2026-08-16  
**Workplace:** cursor-grok

## Survey Card

- **title:** Matching Theory-based Recommender Systems in Online Dating
- **authors or company:** Yoji Tomita, Riku Togashi, Daisuke Moriwaki (CyberAgent, Inc.)
- **venue:** RecSys 2022 (arXiv preprint)
- **year:** 2022
- **URL:** https://arxiv.org/pdf/2208.11384.pdf
- **source type:** industry paper
- **direction:** D8
- **problem setting:** Reciprocal online dating on tapple (7M+ registered users): men/women like or nope candidates; matches require mutual "thank"; popular users receive excessive likes creating capacity bottlenecks that standard fusion rankers ignore.
- **objective and label definition:** Replace φ(p_x,y, p_y,x) reciprocal fusion with Choo–Siow transferable-utility equilibrium matching μ_x,y incorporating capacity terms √μ_x,0 √μ_y,0; unilateral scores p_x,y, p_y,x from matrix factorization on likes/thanks; no explicit retention or revenue label in source.
- **prediction or incrementality:** Predicts equilibrium match probabilities μ_x,y (not incremental lift of a recommendation); transfers τ_x,y adjust bilateral utilities; unmatched option modeled explicitly.
- **model architecture:** MF unilateral preference estimation → TU equilibrium via iterative proportional fitting (IPFP) closed-form updates on μ_x,0, μ_y,0; reciprocal score p̃_x↔y = exp((p_x,y + p_y,x)/2); scalability approximations via LSH/ANN for neighbor sums.
- **credit assignment:** Market-equilibrium allocation across full candidate sets; not per-exposure delayed outcome attribution.
- **training data and counterfactual handling:** tapple production MF on unilateral historical feedback; full |X|×|Y| score matrix and IPFP iterations; LSH/ANN approximations for million-scale deployment; offline experimentation design discussed but detailed online lift numbers not reported in this preprint.
- **offline and online evaluation:** Complexity analysis O(|X||Y|(d+T)) vs iALS; comparison to Chen et al. (2021) group-level OLS approach preserving individual MF preferences; online experimentation and SUTVA concerns flagged as future work; no A/B metrics in source.
- **reported gains:** Not specified in source as quantitative production lifts; claims MTRS mitigates extreme concentration of likes/matches vs off-the-shelf fusion; individual-level matching vs group-identical recommendations in Chen et al. baseline.
- **applicability note for a two-sided dating recommender:** TU matching with explicit unmatched/outside options is a principled congestion-aware layer atop reciprocal MF scores when star users are overwhelmed.
- **applicability note for a two-sided dating recommender:** Full equilibrium computation remains costly at dating scale; source discusses approximations but does not report end-to-end latency, retention impact, or calibrated online match-rate deltas.
- **unverified claims:** none
