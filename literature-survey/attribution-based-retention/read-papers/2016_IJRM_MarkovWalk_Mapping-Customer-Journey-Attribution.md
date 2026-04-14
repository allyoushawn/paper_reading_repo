# Paper Analysis: Mapping the customer journey: Lessons learned from graph-based online attribution modeling

**Source:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2343077  
**Date analyzed:** 2026-04-12

---

## 1. Summary

**Title:** Mapping the customer journey: Lessons learned from graph-based online attribution modeling  
**Authors:** Eva Anderl, Ingo Becker, Florian von Wangenheim, Jan Hendrik Schumann (as listed in SSRN metadata)  
**Abstract (from source):** Advertisers reach customers through many online channels; customers often touch multiple channels along their journey. Evaluating each channel’s contribution to marketing success and how channels interact remains difficult. The authors introduce a graph-based attribution framework that treats customer paths as first- and higher-order Markov walks, applies it to four large customer-level datasets (each with at least seven online channels), and contrasts results with heuristics such as last-click attribution. They report carryover (idiosyncratic channel preferences) and spillover (within- and cross-category interaction effects).

**Key contributions:**

- Graph-based attribution framework capturing sequential journeys via Markov walks (first- and higher-order).
- Empirical generalizations across four industry datasets with rich multichannel structure.
- Evidence that Markov-walk credit differs substantially from last-click and refines prior single-dataset findings.

**Methodology:** Customer journeys modeled as Markov processes on a graph of channel transitions; attribution derived from transition structure (details limited in abstract-only source).

**Main results:** Substantial divergence from last-click; identification of carryover and spillover patterns across channel categories.

---

## 2. Experiment Critique

**Design:** Four large customer-level datasets, ≥7 channels each; comparison to last-click and industry heuristics.

**Statistical validity:** Not specified in source (full paper not in NotebookLM excerpt).

**Online experiments (if any):** Not specified in source.

**Reproducibility:** Industry datasets not publicly identified in the provided text; reproduction likely partial at best.

**Overall:** The NotebookLM source was effectively abstract/metadata; quantitative tables, full Markov specification, and limitations sections were not available for deep critique.

---

## 3. Industry Contribution

**Deployability:** Markov-chain MTA is a standard interpretable family; graph formulation fits reporting to marketing stakeholders.

**Problems solved:** Multi-channel credit with explicit sequential structure vs. single-touch heuristics.

**Engineering cost:** Moderate — transition graph estimation and higher-order Markov extensions add pipeline complexity vs. rules-based MTA.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:** Generalizable cross-industry insights from graph/Markov attribution vs. fragmented single-dataset studies.

**Prior work comparison:** References include clickstream path modeling (Montgomery et al.), mutually exciting point processes for paths (Xu et al.), multichannel effectiveness papers (de Haan et al.; Kireyev et al.), and multichannel CRM surveys (Neslin & Shankar).

**Verification:** Claims align with the Markov-MTA literature stream; full empirical magnitudes could not be verified from the abstract-only source.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| Four proprietary industry datasets | Not specified in source | Unknown | Described only at high level |

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

**Authors:** Eva Anderl, Ingo Becker, Florian von Wangenheim, Jan Hendrik Schumann  
**Affiliations:** Not fully specified in source  
**Venue:** International Journal of Research in Marketing (IJRM), 2016  
**Year:** 2016  
**PDF:** SSRN landing page (ingested via NotebookLM); Elsevier DOI version was previously paywalled in survey notes  
**Relevance:** Core  
**Priority:** 1

---

## Project Relevance

**(A) Per-touchpoint credit vs aggregate lift:** The framework evaluates how each channel contributes vs. last click, implying channel-level (touch-class) credit rather than a single aggregate lift number; suitability as **dense per-interaction** supervised labels is **not specified in source**.

**(B) Continuous engagement / retention outcomes:** Not specified in source (focus on generic “marketing success”).

**(C) Selection bias:** Not specified in source; Markov modeling describes association structure along observed paths rather than explicit causal deconfounding.

---

*[If datasets are accessible: To run experiments on these datasets, use the experiment-runner skill with the dataset URL or info above.]*
