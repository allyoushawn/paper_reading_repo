# Paper Analysis: Incrementality Bidding & Attribution

**Source:** https://arxiv.org/pdf/2208.12809.pdf
**Date analyzed:** 2026-04-12

---

## 1. Summary
**Title:** Incrementality Bidding & Attribution
**Authors:** Randall Lewis, Jeffrey Wong
**Abstract:** The causal effect of showing an ad to a potential customer versus not — "incrementality" — is the fundamental question of advertising effectiveness. In digital advertising, three major pieces are central: ad buying/bidding/pricing, attribution, and experimentation. The authors propose a methodology unifying these into a computationally viable model of both bidding and attribution spanning randomization, training, cross-validation, scoring, and conversion attribution. The method is a regularized instrumental variable (IV) model of heterogeneous treatment effects in a continuous-time panel with the Hausman Causal Correction (HCC).

**Key contributions:**
- Unified framework connecting ad bidding, attribution, and experimentation via causal econometrics
- Regularized IV model of heterogeneous treatment effects in continuous time
- Hausman Causal Correction (HCC): L2 penalization bridging correlational ML models and unbiased causal IV estimators, with cross-validated λ
- Continuous-time ad stock modeling using exponential/gamma decay to avoid batch-aggregation bias
- Ghost Bid Stock instrumental variables for bid-level randomization to resolve selection bias
- Computationally tractable continuous-time training via down-sampling negatives with "double negatives" bias correction
- Bayesian Bootstrap for standard errors, cross-validation, and Thompson sampling exploration

**Methodology:** The core model is y_i(t) = α(t) + β x_i(t) + ε_i(t) in continuous time, where x_i(t) is ad stock modeled via exponential/gamma decay PDFs. Selection bias is handled via instrumental variables from randomized experiments — either user-level or bid-level randomization. "Ghost bid stock" features (predicted counterfactual ad stock) serve as IVs. The HCC starts with a correlational model (e.g., Ridge regression), then estimates a causal correction penalized toward the correlational model's predictions. Cross-validation on λ_HCC trades off bias and variance. Computational tractability achieved by collecting all positive conversions, sampling random negatives, and appending "double negatives" to remove sampling bias.

**Main results:** In simulation (N=4,000 to N=400,000): OLS severely overestimates effects (1.82 vs true 1.32), 2SLS is unbiased but noisy (1.31), HCC efficiently bridges both (1.37 at small N → converges to 2SLS at large N). Down-sampling negatives at 10:1 ratio sacrifices at most 10% of available precision. The framework is designed for >10B auctions/day and >1B users/month.

---

## 2. Experiment Critique
The paper uses synthetic simulation studies rather than real-world benchmarks. While the HCC consistency demonstration across sample sizes (4K/43K/400K) is theoretically convincing, no named real dataset is evaluated. The continuous-time modeling motivation is strong — the authors demonstrate how batch-aggregated models (hourly/daily) introduce endogeneity bias through targeting feedback loops operating at millisecond timescales. The down-sampling procedure with double negatives is mathematically rigorous. Key limitation: the linear model constraint (nonlinear incremental value computation is shown to be "quite challenging") may limit flexibility. The framework's statistical power depends heavily on randomization infrastructure (ghost bids require bid-level experiments), which many organizations may not have.

---

## 3. Industry Contribution
Extremely high industry contribution — designed for Netflix-scale production deployment. The framework directly converts causal attribution scores into bid values, closing the loop between measurement and optimization. The HCC concept of "causally correcting" an incumbent correlational model rather than replacing it is pragmatically brilliant — allows incremental adoption without full system overhaul. Engineering requirements are demanding: continuous-time feature engineering, bid-level randomization infrastructure, and real-time scoring at 10ms latency. The surrogate metrics idea (using upper-funnel outcomes with HCC correction toward lower-funnel) is directly applicable to engagement/retention settings.

---

## 4. Novelty vs. Prior Work
1. **Johnson, Lewis, and Nubbemeyer (2017)** — "Ghost Ads" / "Predicted Ghost Ads" — foundational mechanism for ghost bid stock IVs
2. **Lewis and Rao (2015)** — "The Unfavorable Economics of Measuring the Returns to Advertising" — severe noise in ad measurement experiments
3. **Johnson and Lewis (2015)** — Cost Per Incremental Action (CPIA) pricing model; incrementality bidding as generalization of CPM/CPC/CPA
4. **Lewis and Wong (2018)** — "Econometric Bandits" — companion paper with full HCC treatment and Bayesian bootstrap
5. **Johnson, Lewis, and Reiley (2015/2016)** — statistically significant ad effects and baseline IV model forms
6. **Blake, Nosko, and Tadelis (2014)** — eBay massive misallocation via correlational metrics
7. **Athey et al. (2016)** — surrogate/proxy outcomes for improving statistical power

---

## 5. Dataset Availability
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| HCC Simulation | N/A | No | Synthetic; N=4K/43K/400K |
| Production constraints | N/A | No | >10B auctions/day, >1B users/month (engineering environment, not evaluated dataset) |

---

## 6. Community Reaction
No significant community discussion found.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information
**Authors:** Randall Lewis, Jeffrey Wong
**Affiliations:** Netflix
**Venue:** arXiv (working paper)
**Year:** 2018 (first draft 2017)
**PDF:** https://arxiv.org/pdf/2208.12809.pdf
**Relevance:** Core
**Priority:** 1

---

## Project Relevance
**(A) Does it produce per-touchpoint or per-interaction credit suitable as continuous training labels, or mainly aggregate lift?**
- Produces per-touchpoint fractional credit. The framework computes an "incrementality share" (s_ij) and an expected "incremental value" (Δy_ij) for every single impression j shown to user i. These values directly represent the fractional credit of a conversion caused by that specific touchpoint, making them highly suitable as granular training labels.

**(B) Applicability to non-purchase, continuous engagement / retention outcomes?**
- Not specified in source (mainly models discrete events). The model allows for non-purchase "surrogate" metrics like website visits. However, the core mathematics assume outcomes are discrete "conversion" events arriving at "specific moments in time — a set of measure zero." The framework does not specify how to directly apply its continuous-time ad-stock integrals to continuously accumulating engagement metrics like "user-days-active."

**(C) Handling selection bias when high-activity users get more touchpoints?**
- Explicitly addresses "activity bias" (where users organically make themselves eligible for more ads) as a severe source of endogeneity. Uses Ghost Bids / Predicted Ghost Ads as instrumental variables from randomized bid-level experiments to isolate true causal lift from natural activity levels. The HCC mathematically penalizes correlational ML models (which overvalue high-activity correlation) toward the unbiased causal IV estimates. Continuous-time modeling prevents "covariate shift" and reverse-causality biases from targeting feedback loops.
