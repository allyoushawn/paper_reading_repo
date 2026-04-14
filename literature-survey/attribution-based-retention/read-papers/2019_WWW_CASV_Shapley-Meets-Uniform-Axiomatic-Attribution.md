# Paper Analysis: Shapley Meets Uniform: An Axiomatic Framework for Attribution in Online Advertising

**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3392721  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Shapley Meets Uniform: An Axiomatic Framework for Attribution in Online Advertising  
**Authors:** Not fully listed in the SSRN abstract snippet provided to NotebookLM (check full PDF for author list)  
**Abstract (from source):** Attribution in online advertising requires assessing contributions of individual actions (emails, display, search) to conversion. Common heuristics lack formal justification. The paper proposes an axiomatic framework, shows how standard heuristics fit it and can fail, introduces the **counterfactual adjusted Shapley value (CASV)** to retain desirable Shapley properties while fixing shortcomings in advertising settings, and pairs it with a **Markovian model** of the conversion funnel where ad actions have stage-dependent impact. Under the Markovian model, CASV coincides with an **adjusted unique-uniform** scheme that is efficiently implementable as a correction to naive uniform attribution. Numerical experiments use a large-scale real-world dataset.

**Key contributions:**

- Axiomatic attribution framework for online advertising.
- CASV metric bridging Shapley-style fairness and advertising path structure.
- Markovian journey model; equivalence to adjusted unique-uniform under stated assumptions.

**Methodology:** Formal axioms + Markov funnel model + CASV definition; numerical experiments vs. common metrics/heuristics.

**Main results:** Theoretical equivalence result (CASV ↔ adjusted unique-uniform under Markov model); empirical section referenced but detailed numbers not in abstract-only source.

---

## 2. Experiment Critique

**Design:** Large-scale real dataset referenced; baselines described as “commonly used metrics” and uniform scheme.

**Statistical validity:** Not specified in source (abstract-only).

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Dataset identity not disclosed in provided text.

**Overall:** Strong theoretical positioning; NotebookLM source was abstract-heavy, limiting numeric critique.

---

## 3. Industry Contribution

**Deployability:** High potential — adjusted unique-uniform scheme is framed as computationally tractable vs. full Shapley enumeration.

**Problems solved:** Formal critique and replacement path for unjustified attribution heuristics in funnel advertising.

**Engineering cost:** Moderate — requires Markov model estimation from journey data; simpler than full game-theoretic sampling if assumptions hold.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** First axiomatic packaging of online ad attribution with CASV + Markov funnel equivalence to a corrected uniform scheme.

**Prior work comparison (from reference list in source):** Berman (2018) “Beyond the Last Touch”; Xu/Duan/Whinston path-to-purchase point process; Anderl et al. (2016) Markov customer journey; Kireyev et al. display/search dynamics; Blake et al. paid search experiments; Balseiro et al. exchange/yield papers; Littlechild & Owen (Shapley foundations).

**Verification:** Conceptual positioning is clear; detailed empirical superiority claims need full-text verification.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Large-scale proprietary dataset | Not named in source | Unknown | Referenced for numerical experiments |

**Offline experiment reproducibility:** Not specified in source.

---

## 6. Community Reaction

No significant community discussion found from the abstract-only pass.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** See full WWW 2019 proceedings / SSRN PDF for complete author list  
**Affiliations:** Not specified in source  
**Venue:** WWW (The Web Conference) 2019  
**Year:** 2019  
**PDF:** SSRN landing page (ingested via NotebookLM)  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(A) Per-touchpoint credit vs aggregate lift:** CASV / adjusted unique-uniform targets **contributions of individual advertiser actions** along the funnel — aligned with **fractional per-action credit** rather than pure aggregate lift, though continuous supervised labels are not discussed.

**(B) Continuous engagement / retention outcomes:** Not specified in source (framed around discrete conversion funnel).

**(C) Selection bias:** “Counterfactual adjusted” naming suggests causal intent, but **explicit selection-bias handling** is **not specified in source** in the provided excerpt.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
