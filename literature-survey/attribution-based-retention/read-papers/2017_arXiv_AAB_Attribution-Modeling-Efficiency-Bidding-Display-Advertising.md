# Paper Analysis: Attribution Modeling Increases Efficiency of Bidding in Display Advertising

**Source:** https://arxiv.org/pdf/1707.06409.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Attribution Modeling Increases Efficiency of Bidding in Display Advertising  
**Authors:** Eustache Diemert, Julien Meynet, Pierre Galland, Damien Lefortier (Criteo)  
**Abstract:** Argues standard expected-value bidding ignores evolving **attribution** of conversions to prior clicks; proposes an exponential-decay model for attributed-conversion probability after a click and embeds its **marginal** contribution in bids; introduces attribution-aware expected utility (AEU) for offline evaluation.

**Key contributions:**
- Attribution probability model \(P(A=1\mid S=1,X,\Delta)=e^{-\lambda(x)\delta}\) with MLE for \(\lambda\).
- Attribution-aware bidder: scales CPA×\(P(A_{\mathrm{ALL}}=1\mid x)\) by \((1-e^{-\lambda(x)\delta_c})\) for marginal attribution of an additional click opportunity.
- AEU metric reweights displays by learned attribution to avoid last-click bias in offline policy comparison.

**Methodology:** Criteo click–conversion logs with attribution flags; logistic-style calibration; online A/B via multiplicative bid shaper \(A(1-Be^{-\lambda\delta})\); baselines LCB/FCB.

**Main results:** Offline UA at \(\beta=1000\): AB vs LCB **+12.32%**; online **+5.5% OEC**, improved advertiser ROI, lower user exposure, short-term platform revenue negative (expected underspend vs reference).

---

## 2. Experiment Critique

**Design:** Strong industry-scale offline replay + production A/B; honest trade-off on revenue.

**Statistical validity:** AEU can favor bidder matching the same attribution model (overfitting risk noted); \(\lambda\) often global across advertisers for stability.

**Online experiments (if any):** Yes — multi-setting Criteo A/B with bootstrap significance.

**Reproducibility:** Dataset announced for release in paper era; engineering replication needs internal attribution logs.

**Overall:** Practical bridge from **path-level marginal attribution** to **bid control**; not a new path-Shapley estimator but a deployment pattern.

---

## 3. Industry Contribution

**Deployability:** High — multiplier form on existing bidder.

**Problems solved:** Post-click overbidding under last-touch-trained EVB; aligns spend with marginal attributed value.

**Engineering cost:** Low–moderate — one decay parameter plus calibration loop.

---

## 4. Novelty vs. Prior Work

Builds on lift-based bidding (Xu et al. 2016), expected utility (Chapelle 2015), and MTA literature (Shao & Li; Dalessandro et al.); positions against naive last-touch training labels for conversion models.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Criteo production sample (30 days) | research.criteo.com (historical announcement) | Conditional | Displays/clicks/conversions/attribution |

**Offline experiment reproducibility:** Partial — schema described; competitive bids partially unobserved (lost auctions) as noted.

---

## 6. Community Reaction

Not specified in source.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Eustache Diemert; Julien Meynet; Pierre Galland; Damien Lefortier  
**Affiliations:** Criteo  
**Venue:** arXiv (stat.ML)  
**Year:** 2017  
**PDF:** https://arxiv.org/pdf/1707.06409.pdf  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(A)** Produces **marginal attributed conversion probability** per incremental click opportunity for **bidding**, and illustrates multi-click fractional schemes (\(A_{\mathrm{AM}}\)); **not specified in source** as labels for a separate supervised retention model.

**(B)** Outcomes modeled as **Bernoulli** conversion/attribution events; **continuous engagement outcomes are not specified in source.**

**(C)** Selection bias in offline replay from **unobserved lost auctions** is noted; user activity enters features \(x\) but **no dedicated endogeneity treatment for “more touches because more active”** beyond standard modeling.
