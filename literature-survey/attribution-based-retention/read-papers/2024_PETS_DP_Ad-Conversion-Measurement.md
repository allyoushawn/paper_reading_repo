# Paper Analysis: Differentially Private Ad Conversion Measurement

**Source:** https://arxiv.org/pdf/2403.15224.pdf  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Differentially Private Ad Conversion Measurement  
**Authors:** John Delaney, Badih Ghazi, Charlie Harrison, Christina Ilvento, Ravi Kumar, Pasin Manurangsi, Martin Pál, Karthik Prabhakar, Mariana Raykova  
**Abstract:**  
Defines an end-to-end central-DP model for ad conversion measurement: an attribution rule maps each user’s impression sequence plus conversion to fractional weights on $(i,c)$ pairs; a curator applies contribution bounds (pre- or post-attribution), then Laplace noise scaled by $C_0 \cdot r \cdot \Delta(f)/\varepsilon$. The paper classifies which combinations of attribution rule, adjacency (privacy unit), and enforcement point are **operationally valid** ($\ell_1$ change $O(r)$ independent of publisher/advertiser counts).

**Key contributions:**
- Definition of $C_0$-valid configurations tying attribution sensitivity to DP noise scale.
- Complete classification (Table 5 in paper) for common rules: LTA, FTA, uniform, exponential decay, U-shaped, etc., across adjacencies.
- Key structural facts: pre-attribution enforcement always $C_0=1$ for all rules/adjacencies; post-attribution + user×publisher always invalid; uniform/EXP/U-shaped can be invalid under impression adjacency while LTA/FTA may be 2-valid.

**Methodology:**  
Formal attributed datasets as weighted $(i,c)$ multisets; lemmas/theorems with explicit adversarial constructions for impossibility results.

**Main results:**  
Representative constants: pre-attribution $C_0=1$ universally (Theorem 5); post-attribution user / user×advertiser / conversion adjacencies $C_0=1$ (Theorems 4,6,7); impression+post: FTA and LTA 2-valid (Theorems 2,8); uniform multi-touch invalid (Theorem 9); exponential decay invalid (Corollary 1); U-shaped invalid (Theorem 10); user×publisher×advertiser: only FTA 2-valid (Theorem 11), LTA invalid (Theorem 3).

---

## 2. Experiment Critique

**Design:**  
Pure theory + proof sketches; illustrative adversarial datasets to show unbounded sensitivity growth.

**Statistical validity:**  
Central $\varepsilon$-DP via Laplace mechanism; sensitivity bounds $C_0 \cdot r$; discussion of approximate-DP extensions noted as possible.

**Online or field experiments if any:**  
Not specified in source (paper cites external empirical ARA evaluations but runs none here).

**Reproducibility:**  
Proofs in appendix; no code/data release specified in source.

**Overall:**  
Tight formal classification; directly actionable for API privacy-unit and enforcement-point choices.

---

## 3. Industry Contribution

**Deployability:**  
High for browser/platform architects (Chrome ARA, Safari PCM, SKAdNetwork, IPA, etc.) choosing valid DP configurations.

**Problems solved:**  
Explains when naive post-attribution bounding fails (e.g., user×publisher with LTA) and when multi-touch rules break DP sensitivity bounds.

**Engineering cost:**  
Conceptual; implementing valid scopes may require restricting rules or moving enforcement pre-attribution.

---

## 4. Novelty vs Prior Work

**Paper's claimed novelty:**  
First end-to-end formal DP framework linking attribution-rule algebra to measurement-system DP.

**Prior work comparison:**  
Positions relative to empirical ARA papers [13],[6] cited in text as complementary.

**Verification:**  
Not specified in source (NotebookLM batch; no independent novelty web search).

---

## 5. Dataset Availability

**Datasets mentioned:**  
| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| — | — | — | Theoretical paper |

**Offline experiment reproducibility:**  
Proofs only.

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

**Authors:** John Delaney; Badih Ghazi; Charlie Harrison; Christina Ilvento; Ravi Kumar; Pasin Manurangsi; Martin Pál; Karthik Prabhakar; Mariana Raykova  
**Affiliations:** Google (multiple regions, per author block)  
**Venue:** Proceedings on Privacy Enhancing Technologies (PoPETs) 2024(2)  
**Year:** 2024  
**PDF:** downloaded (arXiv / open access venue)  
**Relevance:** Related  
**Priority:** 3

---

## NotebookLM — Project alignment (requirements.md §Project Context)

1. **Per-touchpoint fractional credit:** Yes as **mathematical definition** of rules (uniform, decay, etc.) producing $[0,1]$ weights on impressions along a path — but the paper’s goal is **DP validity of measurement pipelines**, not producing denoised per-touch training labels for a supervised retention model.  
2. **Continuous outcomes as supervised training labels:** Not specified in source.  
3. **Heterogeneous touch types / self-selection:** Impression metadata includes click vs view in examples; user self-selection into more interactions not specified in source.
