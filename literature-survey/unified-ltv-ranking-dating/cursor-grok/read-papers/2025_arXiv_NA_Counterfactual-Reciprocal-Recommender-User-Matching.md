# Paper Analysis: Counterfactual Reciprocal Recommender Systems for User-to-User Matching

**Source:** https://arxiv.org/pdf/2508.01867.pdf
**Date analyzed:** 2026-08-16
**Workplace:** cursor-grok

## Survey Card

- **title:** Counterfactual Reciprocal Recommender Systems for User-to-User Matching
- **authors or company:** Kazuki Kawamura, Takuma Udagawa, Kei Tateno (Sony Group Corporation)
- **venue:** TSMO '25 (KDD 2025 Workshop)
- **year:** 2025
- **URL:** https://arxiv.org/pdf/2508.01867.pdf
- **source type:** industry paper
- **direction:** D6
- **problem setting:** Bilateral user-to-user matching (dating, gaming, talent); logged pairs over-represent popular users due to historical exposure policy, creating feedback loops that skew learning and fairness.
- **objective and label definition:** Learn compatibility score \(s(u,v;\Theta)\) predicting mutual acceptance \(R(u,v)\) under a uniform target distribution over pair space \(\mathcal{P}=U\times V\); label \(r(u,v)\) observed only when pair is displayed \(O(u,v)=1\). No time horizon or delay model.
- **prediction or incrementality:** Selection-bias-corrected prediction of mutual acceptance via IPS/SNIPS/DR reweighting; not incremental effect of exposure on retention/revenue.
- **model architecture:** Generic compatibility scorer \(s(u,v;\Theta)\) (LFRR latent-factor baseline) plus pair-level propensity model \(\theta(u,v)=\sigma(g(\phi(u),\psi(v);\beta))\); optional neural outcome model \(\hat{r}(u,v)\) for DR variant.
- **credit assignment:** Direct pair-level: one displayed pair \((u,v)\) yields one bilateral outcome \(r(u,v)\); no slate-level or delayed user-outcome attribution.
- **training data and counterfactual handling:** SNIPS objective with pair-level IPS weights \(w_i=1/\theta(u_i,v_i)\) (truncated at ceiling \(c\)); doubly robust augmentation; joint propensity learning (Algorithm 1) re-estimates \(\beta\) as logging policy evolves.
- **offline and online evaluation:** Offline on Synthetic (5K users, ~50K pairs), DBLP-CoAuthor (10K authors), Epinions-Trust (5K users); NDCG@10, MRR, Coverage@10, Gini-Exposure; 10 seeds, paired t-tests. No online evaluation reported.
- **reported gains:** NDCG@10: +2.7% Synthetic (0.307 vs 0.299 LFRR), +3.5% DBLP (0.475 vs 0.459), +0.9% Epinions; Coverage@10 +51% Synthetic (0.763 vs 0.504); Gini-Exposure −24% Synthetic (0.535 vs 0.708).
- **applicability note for a two-sided dating recommender:** Direct template for debiasing pair-level match scores under popularity/exposure feedback loops before Gale–Shapley or capacity-constrained allocation.
  SNIPS/DR corrects who gets seen, not delayed retention credit assignment—combine with delayed-label or OPE methods for long-horizon ranking evaluation.
- **unverified claims:** Fairness-growth feedback loop (debiasing expands active supplier base) validated only on Synthetic; authors flag need for case-by-case production validation.

## 1. Summary

CFRR applies counterfactual IPS/SNIPS/DR to reciprocal (user-to-user) matching, where bilateral acceptance, pair-level propensities, and downstream stable-matching allocation differ from standard item recommendation. The framework estimates pair display propensities \(\theta(u,v)\), reweights logged mutual-acceptance outcomes via self-normalized IPS to stabilize extreme weights, and adds truncation plus doubly robust augmentation for misspecified propensities. Debiased scores feed top-k recommendation, maximum-weight bipartite matching, or Gale–Shapley. Experiments on synthetic and two real-world reciprocal networks show simultaneous ranking accuracy and fairness gains.

## 2. Experiment Critique

Strengths: three datasets with distinct bias mechanisms, rigorous 10-seed statistical testing, ablations on SNIPS vs IPS and DR under propensity misspecification. Weaknesses: no dating-platform or live A/B data despite dating being the headline use case; random negative sampling on DBLP/Epinions may not reflect true non-interaction; positivity assumption infeasible at full pair-space scale (authors acknowledge pruning to viable candidates); no delay/retention horizon.

## 3. Industry Contribution

Production-relevant pair-level debiasing loop: propensity model on exposure logs, weighted compatibility training, optional joint propensity re-estimation as policy evolves. DR variant adds ~20% training overhead; SNIPS adds 5–10%. Designed to integrate with existing RRS scorers and downstream matching allocators.

## 4. Novelty vs. Prior Work

First unified IPS/SNIPS/DR framework for bilateral matching with pair-level propensities. Builds on Swaminathan & Joachims (2015) SNIPS, Schnabel et al. (2016) IPS for recommendation, StableDR (Li et al. 2022), DICE (Zheng et al. 2021), LFRR (Neve & Palomares 2019). Downstream connection to Gale–Shapley (1962).

## 5. Dataset Availability

- **Synthetic:** 5K users, 16D latent factors, ~50K logged pairs; generation details in supplementary material.
- **DBLP-CoAuthor:** https://snap.stanford.edu/data/com-DBLP.html
- **Epinions-Trust:** https://snap.stanford.edu/data/soc-Epinions1.html

## 6. Community Reaction

No significant community discussion found.

## Project Relevance

### (1) Ranking objective: retention / LTV / revenue vs CTR
Mutual acceptance / compatibility under uniform target distribution. Retention, LTV, revenue, CTR: Not specified in source.

### (2) Credit assignment: user-level delayed outcome → item-level decision
Not specified in source. Pair-level bilateral outcome observed when pair is displayed.

### (3) Label and horizon definitions; delay, sparsity, censoring
Label: mutual acceptance \(r(u,v)\) when pair displayed. Horizon, delay, censoring: Not specified in source. Sparsity: SNIPS stabilizes extreme IPS weights from rare pair propensities.

### (4) Short vs long-term head fusion
Not specified in source. Single compatibility scoring function \(s(u,v;\Theta)\).

### (5) Prediction vs incrementality
Predicts mutual acceptability \(R(u,v)\); uses causal reweighting to correct exposure bias, not uplift of exposure on downstream outcomes.

### (6) Offline and online evaluation
Offline: Synthetic, DBLP, Epinions; NDCG@10, MRR, Coverage@10, Gini-Exposure. Online: Not specified in source.

### (7) Reciprocity, congestion, fairness, revenue vs match quality
Reciprocity: core setting (bilateral feedback). Congestion: debiased scores feed max-weight matching under capacity constraints or Gale–Shapley. Fairness: Coverage@10 and Gini-Exposure metrics; downstream fairness constraints noted. Revenue vs match quality: Not specified in source.

### (8) Migration path from CTR-like model toward unified long-term model
Not specified in source.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

## Meta Information

**Authors:** Kazuki Kawamura, Takuma Udagawa, Kei Tateno
**Affiliations:** Sony Group Corporation
**Venue:** TSMO '25 (KDD 2025 Workshop)
**Year:** 2025
**PDF:** https://arxiv.org/pdf/2508.01867.pdf
**Relevance:** Core
**Priority:** 1
