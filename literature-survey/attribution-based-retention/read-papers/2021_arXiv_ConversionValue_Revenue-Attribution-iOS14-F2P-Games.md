# Paper Analysis: Show me the Money: Measuring Marketing Performance in Free-to-Play Games using Apple’s App Tracking Transparency Framework

**Source:** https://arxiv.org/pdf/2102.08458.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Show me the Money: Measuring Marketing Performance in Free-to-Play Games using Apple’s App Tracking Transparency Framework  
**Authors:** Frederick Ayala-Gómez, Ismo Horppu, Erlin Gülbenkoğlu, Vesa Siivola, Balázs Pejó  
**Abstract:**  
After iOS 14.5, users who deny tracking are not mapped one-to-one to campaigns; Apple exposes per-campaign counts of installs by integer conversion value. The paper formalizes mapping those histograms to revenue, derives an error-minimizing attribution function $g$ (given a schema), and back-tests schemas on historical F2P game data with IDFA-based last-click ground truth.

**Key contributions:**
- Formal problem definition for revenue attribution from conversion values.
- Theoretically optimal $g$ for any schema when privacy threshold $p<2$ (Theorem 1) and practical Uniform vs Null-based variants under null buckets.
- Empirical comparison of conversion-value schemas (EV, rolling revenue/purchase count, UD, PV baselines) under simulated threshold $p$.

**Methodology:**  
Build weekly matrices $\hat{X}$ of conversion-value counts per campaign under schema $f$ and privacy rule; compare $g(\hat{U}, \hat{X})$ to last-click campaign revenues; revenue-weighted weekly errors; six-month, 90-day-matured paid-player cohorts.

**Main results:**  
Rolling revenue (RR) / rolling purchase (RI) schemas that separate spenders from non-spenders perform best; example: at $p=2$, D7 RR with Null-based attribution within ~4% of normalized error vs D30 PV+Uniform baseline; high $p$ collapses RR/RI toward EV/UD as values become null.

---

## 2. Experiment Critique

**Design:**  
Historical back-test with 500K+ paying users, 213 campaigns, 7 networks; country-stratified privacy simulation; baselines UD and hypothetical PV; multiple $p \in \{0,2,10,100\}$ and day-window variants.

**Statistical validity:**  
Squared-error objective; normalized reporting vs D30 PV+U; uncertainty quantification not specified in source.

**Online or field experiments if any:**  
Not specified in source (offline back-test only).

**Reproducibility:**  
Python on 64 vCPU / 512 GB noted; proprietary revenue plots/data not released; public code link not specified in source.

**Overall:**  
Credible industry-grounded evaluation for SKAdNetwork-era campaign ROI; conclusions scoped to F2P games with sparse spenders.

---

## 3. Industry Contribution

**Deployability:**  
Actionable guidance for UA teams on schema bits (time vs revenue vs counts) under low vs high privacy thresholds.

**Problems solved:**  
Campaign-level revenue measurement when IDFA is unavailable, using SKAdNetwork postbacks.

**Engineering cost:**  
Not specified in source.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
Formal optimal $g$ plus systematic empirical schema comparison for SKAdNetwork conversion values.

**Prior work comparison:**  
Not specified in source (NotebookLM batch; no independent novelty web search).

**Verification:**  
Not specified in source.

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Global F2P mobile game (unnamed) | Not specified in source | No | Business confidential; six-month historical extract |

**Offline experiment reproducibility:**  
Not specified in source.

---

## 6. Community Reaction

Not searched in this batch (NotebookLM-only ingestion).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Frederick Ayala-Gómez; Ismo Horppu; Erlin Gülbenkoğlu; Vesa Siivola; Balázs Pejó  
**Affiliations:** BANDAI NAMCO Mobile; Zynga; Rovio Entertainment; CrySyS Lab (per title-page footnotes)  
**Venue:** arXiv  
**Year:** 2021  
**PDF:** downloaded (arXiv)  
**Relevance:** Related  
**Priority:** 2

---

## NotebookLM — Project alignment (requirements.md §Project Context)

1. **Per-touchpoint fractional credit:** No — attributes revenue to **campaigns** from aggregate conversion-value counts; last-click is ground truth reference, not multi-touch path credit for supervised per-interaction learning.  
2. **Continuous labels for a generalizing attribution model:** Not specified in source for ML training targets (revenue is used for ROI measurement, not described as labels for a model scoring new interaction types).  
3. **Heterogeneous touch types / self-selection:** Not specified in source.
