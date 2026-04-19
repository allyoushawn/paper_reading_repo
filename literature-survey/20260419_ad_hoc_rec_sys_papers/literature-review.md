# Literature Review — Recsys Industry Trend & Future Planning (3 Surveys)

**Date:** 2026-04-19  
**Corpus size:** 3 surveys (fixed scope, no crawling)  
**Lens:** ML engineer in production recsys evaluating industry trend & 1–3 year planning  
**Source:** Cross-source NotebookLM synthesis (notebook `5194ee31`) + per-paper analyses  

---

## 1. The Three Surveys at a Glance

| Survey | Year | Scope | Stance toward generative recsys |
|--------|------|-------|---------------------------------|
| Zhao & Liu — Survey of Retrieval Algorithms in Ad and Content Recommendation | 2024 | Retrieval algorithms (ad targeting + organic content): targeting taxonomies, classical filters, two-tower deep retrieval, extensions | Pre-generative — LLMs framed as offline augmentation (synthetic data, keyword expansion), not end-to-end generative serving |
| Pan et al. — A Survey on Sequential Recommendation | 2024/2025 | Sequential recommendation across ID-only, side-info, multimodal, generative semantic IDs, LLM-powered, ultra-long, data-augmented SR | Emerging in research — strong coverage of generative/LLM SR with explicit failure modes; industrial evidence emphasized for *discriminative* ultra-long lines (e.g., Kuaishou), not for generative SR |
| Kuaishou-RecModel — Generative Recommendation Tri-Decoupled | 2025 | Generative recsys via tokenization × architecture × optimization; industrial deployment narrative | Production-oriented — argues generative stacks (SID, decoder-only, RL alignment) are an industrial direction with named systems and MFU framing |

Together, these surveys triangulate the stack you care about: [Survey 1] grounds **retrieval** and the two-tower mental model that still dominates organic recall; [Survey 2] maps **sequential** modeling where much of “what to compare offline” lives (SASRec, BERT4Rec, TIGER, P5) and states the **small-candidate ranking** deployment default; [Survey 3] supplies the strongest **generative-industry** narrative (tokenization, scaling, named lines) but carries affiliation-heavy rhetoric. No single survey covers the full cascade (e.g., re-ranking depth), so conclusions below are explicitly scoped.

---

## 2. Dominant Methodological Approaches (Q1)

Cross-source synthesis clusters the field into four dominant approaches and maps them to cascade stages.

**1. Classical retrieval & representation learning (two-tower, inverted index, CF/CBF/hybrid).**  
Independent user/item encoders with similarity-based top‑N retrieval (organic), plus inverted-index and targeting levers for ads. **Most central in [Survey 1]**; assumed as the upstream candidate generator in [Survey 2]’s industrial discussion. **Cascade:** retrieval / recall.

**2. Sequential & attention-based modeling (Transformers, ultra-long “retrieve-then-attend”).**  
Causal and bidirectional Transformers (e.g., SASRec, BERT4Rec) for next-item prediction; for very long histories, **retrieval of top‑k behaviors followed by attention** on a short sub-sequence. **Most central in [Survey 2]**. **Cascade:** pre-ranking / ranking on **small candidate sets** (as [Survey 2] emphasizes).

**3. Generative recommendation via semantic tokenization (RQ-VAE / SID, NTP, encoder–decoder and decoder-only).**  
Items as token sequences; **semantic IDs** from residual quantization; training often **next-token prediction**; shift toward **decoder-only** stacks at large parameter counts. **Most central in [Survey 3]**; [Survey 2] treats the same SID family as a research thread with invalid-token risks. **Cascade:** reframes recall/rank as generation (depending on design); may still sit beside or inside cascades in practice.

**4. RL-based preference alignment (DPO, GRPO, hybrid rewards).**  
Beyond imitation of clicks, alignment to multi-objective platform goals. **Central in [Survey 3]**; largely absent as a primary topic in [Survey 1]; [Survey 2] discusses LLM/generative limitations more than RL alignment detail.

---

## 3. Foundational Anchors (Q4) and the Composite Top Methods

NotebookLM’s cross-source “anchor” list aligns with the **Top Method Analysis** in `method-tracker.md` (composite scores computed over this 3-paper corpus).

**From Q4 (foundational across sources):**  
- **Inverted index** — fast ad/user matching; structural prerequisite for large-scale ad retrieval ([Survey 1]).  
- **Matrix factorization → two-tower** — classical collaborative scoring extended to deep feature-rich towers ([Survey 1]).  
- **Two-tower** — default organic retrieval architecture and baseline for multi-/three-tower extensions ([Survey 1]).  
- **SASRec** — “most popular” uni-directional Transformer SR baseline; Table 5 anchor ([Survey 2]).  
- **BERT4Rec** — bidirectional Transformer baseline ([Survey 2]).  
- **HSTU** — sparse-ID generative sequence model framing; basis for MTGR-style lines in the GR literature ([Survey 3]).  
- **TIGER** — generative retrieval with semantic IDs; frequent baseline in generative SR discussions ([Survey 2], [Survey 3]).  
- **RQ-VAE** — dominant residual quantization path for SID construction ([Survey 2], [Survey 3]).

**Woven with `method-tracker.md` composite leaders:**

| Method (tracker) | Role in this synthesis |
|------------------|-------------------------|
| **HSTU** (+5) | Industrial narrative for sparse-ID generative sequence modeling and follow-on frameworks (e.g., MTGR cited in [Survey 3]). |
| **OneRec / One-series** (+5) | End-to-end generative story, MFU comparisons vs. cascaded systems in [Survey 3]. |
| **RQ-VAE / SID** (+5) | Shared engineering object between [Survey 2] (generative SR) and [Survey 3] (tokenizer axis). |
| **TIGER** (+5) | Bridge from “generative SR row in Table 5” ([Survey 2]) to generative retrieval survey depth ([Survey 3]). |
| **SASRec** (+4) | Canonical Transformer-ID baseline for offline comparisons. |
| **BERT4Rec** (+4) | Standard bi-directional alternative in the same comparison set. |
| **P5** (+4) | LLM-prompted multi-task baseline in [Survey 2]; “early text-based” generative framing in [Survey 3]. |
| **SIM** (+4) | Retrieve-then-attend template for ultra-long behavior ([Survey 2]). |
| **Two-tower** (+2) | Retrieval-stage default in [Survey 1]; implicit upstream to SR stacks. |

**Named industrial systems (as cited in corpus):** TWIN / TWIN-V2 at Kuaishou ([Survey 2]); HSTU, MTGR, OneRec / OneSearch / OneLoc, Kuaiformer, EGA-V2, etc., in [Survey 3]’s application narrative — treat as **paper-attributed** unless your org has independent verification.

---

## 4. Evaluation Practice & Industrial Scale Evidence (Q2)

**Datasets and benchmarks**  
The only survey that **lists** a broad set of public dataset names is Liwei Pan et al., *A Survey on Sequential Recommendation* (arXiv:2412.12770): e.g., MIND, H-M, Bili, Art of the Mix, LastFM, **Amazon 2023**, MicroLens, MovieLens, Steam, Yelp, Goodreads, Douban (multi-modal availability varies). **Table 5** in that survey quotes **HR@10 / NDCG@10** on Amazon subdomains (Office, Game, Toy) for representative models. [Survey 1] and [Survey 3] do not provide a comparable unified dataset table in this corpus.

**Shared metrics across themes**  
HR/NDCG for ranking quality ([Survey 2]); engagement and revenue family metrics (DAU/MAU, clicks, retention, CPC, CVR, GMV) discussed at concept level ([Survey 1], [Survey 3]).

**Industrial deployments and scale numbers (named in any source)**  
- **Illustrative platforms:** Netflix, Spotify ([Survey 1]); e-commerce and streaming/social examples ([Survey 2]).  
- **Kuaishou:** TWIN / TWIN-V2 for ultra-long CTR ([Survey 2]); Kuaiformer, OneRec / OneSearch / OneLoc lines ([Survey 3]).  
- **Meituan:** MTGR ([Survey 3]); context-based fast recommendation for Waimai cited from literature ([Survey 2] references).  
- **Catalog / pipeline scale (qualitative):** “tens of millions” of items; cascade **millions → thousands → dozens** ([Survey 3]); sparse-ID vocabulary “hundreds of millions” of tokens ([Survey 3]).  
- **MFU (from [Survey 3] narrative):** cascaded discriminative systems **4.6% / 11.2%** train/infer vs. **OneRec 23.7% / 28.8%** train/infer; LLMs **>40%** MFU cited for contrast.  
- **Ultra-long sequence:** **>1000** interactions as “ultra-long” in [Survey 2].  
- **DAU / latency:** named as important; **no platform-specific DAU counts or ms SLA numbers** in this corpus.  

**Honesty:** Cross-survey **A/B test lift percentages** for generative recsys are **not** tabulated here; [Survey 1] discusses A/B **methodology** pitfalls (traffic stealing, ghost experimentation) without generative lift numbers. [Survey 3] references “commercial success” and reward design examples (e.g., GMV-related signals in scenario-specific systems) at narrative level — not a substitute for your org’s experimentation standards.

---

## 5. Cross-Source Baseline Map (Q5)

| Method | [Survey 1] | [Survey 2] | [Survey 3] |
|--------|------------|------------|------------|
| **SASRec / BERT4Rec** | Not in empirical Table 5; Transformers discussed as costly in towers | Primary **pure-ID baselines** in Table 5; SASRec “most popular” | Framed as **sparse-ID** lineage vs. SID/generative stacks (tokenizer evolution narrative) |
| **TIGER** | Omitted | Generative SR **baseline** in quoted table | **Foundational** generative-retrieval + SID story; many follow-ons |
| **P5** | Omitted | LLM-powered SR **baseline** in table | Early **encoder-decoder / T5-style** prompt unification; contrasted with SID efficiency story |
| **SpecGR** | Omitted | Generative SR baseline | Cited in RQ-VAE / quantization usage |
| **DIN / DCN** | Omitted | Omitted | **Discriminative anchors** for “embedding & MLP” critique |

**Conflict note:** NLM’s Q5 summary states that [Survey 1] “omits” named baselines such as SASRec/TIGER. The per-paper analysis is more precise: [Survey 1] does **not** run a multi-model benchmark table, but it still treats **two-tower / MF** as the central pedagogical anchor. **Trusting the per-paper analysis** — omission of SASRec is **non-appearance in SR benchmarks**, not a claim that sequential baselines are irrelevant to industry.

**Signal:** Where [Survey 2] uses a method as a **neutral offline baseline**, [Survey 3] may recast the same method as **legacy tokenizer paradigm** (sparse ID) or as **pioneer** (TIGER). That mismatch is exactly the “field boundary” signal: **same artifact, different lifecycle label**.

---

## 6. Open Problems & Gaps (Q3)

**In 2+ sources (explicitly):**  
- **Cold start / sparsity** — persistent across retrieval, SR, and GR tokenization stories ([Survey 1]–[Survey 3]).  
- **Compute / long sequences** — quadratic attention, latency, memory; ultra-long sequence noise ([Survey 1]–[Survey 3]).  
- **Data quality & bias** — noise, exposure/position bias; debiasing for generative training ([Survey 2], [Survey 3]).  
- **Privacy / ethics** — profiling and centralized data risks ([Survey 1], [Survey 2] cloud–edge / federated angle).  
- **Interpretability & reasoning** — explainable SR and personalized CoT at scale under latency ([Survey 2], [Survey 3]).

**Thematic buckets (including single-source but high-impact):**  
- **Scaling & ops:** streaming training, algorithm–system co-design, MoE/GQA latency ([Survey 3]).  
- **SID / tokenizer:** collision, objective inconsistency across tokenizer vs. generative stages, prefix dependency in decoding ([Survey 3]); invalid semantic IDs in generation ([Survey 2]).  
- **Evaluation:** A/B pitfalls specific to two-sided markets ([Survey 1]); lack of unified industrial GR benchmark in surveys ([Survey 2], [Survey 3]).  
- **Frontier SR:** open-domain dynamics, continuous drift, “SR for good” ([Survey 2]).  
- **From recommendation to generation:** generative *content* (e.g., video) with sparse feedback — adjacent to classical item recommendation ([Survey 3]).

---

## 7. Industry-Trend Synthesis: Generative Recsys Production Maturity (Q6)

This section answers the north-star question using Q6, Phase 3.7 cross-references, and each paper’s **Project Relevance**.

### What’s already production at scale (named deployments)

- **Discriminative / cascade-heavy stacks** remain the default framing in [Survey 1] and the deployment picture for **ultra-long sequence** work at **Kuaishou (TWIN / TWIN-V2)** in [Survey 2] — these are **not** “generative recsys” in the SID/NTP sense but are **production-grade sequential** modeling at scale.  
- **Generative recommendation (GR) as defined in [Survey 3]:** the tri-decoupled survey claims **industrial applications** for lines such as **HSTU**, **MTGR**, **OneRec / OneSearch / OneLoc**, **Kuaiformer**, and scenario-specific systems (e.g., **EGA-V2** in ads), with **MFU** and parameter-scaling discourse. Treat these as **strong signals in one survey’s citation graph**, not as a global census of all companies.

### What’s emerging-but-real (active industrial work, not yet ubiquitous)

- **SID + generative retrieval / ranking** as an engineering direction: RQ-VAE/ResKmeans, collision handling, joint tokenizer–model training — [Survey 3] positions this as convergent; [Survey 2] documents **offline** competitiveness and **failure modes**.  
- **RL alignment (DPO / GRPO families)** for multi-objective platform goals — central in [Survey 3], rare as primary evidence in the other two.  
- **LLMs as augmenters** (synthetic data, keywords, embeddings) — [Survey 1] and [Survey 2] align on **offline / auxiliary** use before high-QPS generative serving.

### What’s still research-only (in this corpus’s evidence bar)

- **Default production replacement** of full cascades by a single generative model everywhere — [Survey 2] consistently describes SR on **small candidates** and two-stage long-history designs; [Survey 3] argues end-to-end directionally.  
- **Direct LLM item-list generation at strict latency** with robust catalog grounding — failure modes (hallucinated items, invalid IDs) highlighted in [Survey 2].  
- **Diffusion-first SR/GR** — cost and feedback sparsity remain concerns ([Survey 2], [Survey 3]).

### Realistic 1–3 year production trajectory (calibrated)

| Horizon | What the three surveys support together |
|---------|------------------------------------------|
| **0–12 mo** | **Invest** in SID quality, generative *modules* (e.g., retrieval or rank-stage pilots), and RL alignment literacy if your stack touches list-wise objectives; **keep** cascades — [Survey 2] and [Survey 1] remain aligned with staged serving. |
| **1–3 yr** | **Selective adoption** possible where (i) tokenizer–catalog grounding is solved for your inventory, (ii) MFU / serving economics justify unified stacks — per [Survey 3]’s narrative; **independent A/B and risk review** still required — [Survey 1]’s experimentation pitfalls and [Survey 2]’s generative failure modes still apply. |

**Decision-oriented summary:** If your job is **operating a discriminative cascade**, the corpus supports **study SID + decoder-only GR** and **pilot-grade adoption** where orgs already publish lines (per [Survey 3]), while **waiting** on declaring generative recsys **universal production default** — [Survey 2]’s evidence base remains **offline** for generative SR rows; [Survey 1] barely addresses generative serving.

---

## 8. Tension Points: Cascade vs. Unified Generative (Q7)

Synthesizing Q7 with **contradiction** rows from each per-paper reverse citation map.

| Tension | Discriminative-cascade side | Unified-generative side | Engineer takeaway |
|---------|----------------------------|-------------------------|-------------------|
| **Pipeline shape** | Multi-stage recall → rank is necessary for latency and modularity; two-tower scales via decoupled towers ([Survey 1]); SR often on **small candidates** ([Survey 2]) | Multi-stage cascades accumulate error and objective misalignment; end-to-end generative removes stage-wise loss ([Survey 3]) | **Hybrid era:** cascades remain operationally dominant; generative **stages** may replace *parts* first. |
| **Hardware efficiency** | Attention **in towers** is a bottleneck; prefer lean retrieval ([Survey 1]) | Fragmented discriminative ops → low **MFU**; unified generative kernels improve MFU ([Survey 3]) | Compare **whole-path** cost (indexing, ANN, rerankers) vs. generative serving — MFU is one slice. |
| **Item representation** | Sparse IDs + embeddings learn strong CF signals ([Survey 2] Table 5; [Survey 3] admits sparse-ID advantages) | Embedding tables dominate parameters; **SIDs** compress and add semantics ([Survey 3]) | **SID vs sparse ID** is a tokenizer trade — watch **collisions** ([Survey 3]) and **invalid tokens** ([Survey 2]). |
| **Objectives** | Pointwise / pairwise discriminative training, per-stage metrics | NTP + full-sequence modeling; **RL alignment** to platform objectives ([Survey 3]) | If you need multi-objective alignment, RL literacy matters — but reward design is still open ([Survey 3]). |

**Conflict note:** NLM attributes **HSTU** to “Meta” in Q6/Q7-style summaries; your tri-decoupled survey cites HSTU with industrial framing — verify **exact product mapping** in primary sources before internal communication.

---

## 9. What This Synthesis Cannot Tell You (Honesty Section)

- **Three papers** → no coverage guarantee for re-ranking-only methods, auction theory for ads, or full multi-objective ads stacks.  
- **Publication & affiliation skew:** [Survey 3] is Kuaishou-adjacent; [Survey 2] East Asia / global citation mix; [Survey 1] academic + American Express — not a neutral industry panel.  
- **No apples-to-apples benchmark** across the three surveys; Table 5 is **SR-only** and quoted from primaries.  
- **Generative production claims** need **primary papers / internal pilots** to validate for *your* surfaces — especially **A/B lift**, **latency**, and **catalog** constraints.  
- **Adjacent content-generation systems** (e.g., large video models named in [Survey 3]) are not classical item recommendation but influence “supply” narratives.

---

## Source Catalog

| # | File | Citation |
|---|------|----------|
| 1 | [./read-papers/2024_arXiv_NA_Survey-of-Retrieval-Algorithms-Ad-Content-Recommendation.md](./read-papers/2024_arXiv_NA_Survey-of-Retrieval-Algorithms-Ad-Content-Recommendation.md) | Yu Zhao, Fang Liu. "A Survey of Retrieval Algorithms in Ad and Content Recommendation Systems." arXiv:2407.01712, July 2024. |
| 2 | [./read-papers/2024_arXiv_NA_Survey-on-Sequential-Recommendation.md](./read-papers/2024_arXiv_NA_Survey-on-Sequential-Recommendation.md) | Liwei Pan et al. "A Survey on Sequential Recommendation." arXiv:2412.12770, December 2024 (v2 March 2025). |
| 3 | [./read-papers/2025_Preprints_TriDecoupled_Survey-of-Generative-Recommendation-Tri-Decoupled-Perspective.md](./read-papers/2025_Preprints_TriDecoupled_Survey-of-Generative-Recommendation-Tri-Decoupled-Perspective.md) | Kuaishou-RecModel et al. "A Survey of Generative Recommendation from a Tri-Decoupled Perspective: Tokenization, Architecture, and Optimization." Preprints 202512.0203 v1, December 2025. |
