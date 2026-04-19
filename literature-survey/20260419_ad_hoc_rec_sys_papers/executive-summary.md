# Executive Summary — Recsys Industry Trend & Future Planning

**Date:** 2026-04-19  
**Audience:** Single ML engineer in production recsys (classical cascade today, evaluating generative recsys for the next 1–3 years).  
**Source corpus:** 3 surveys — see Source Catalog at bottom.

---

## TL;DR (read this first)

Classical stacks you already run—two-tower embedding retrieval with ANN top‑K, inverted-index ad targeting, and sequential models on **small candidate sets**—remain the defensible production default in Yu Zhao, Fang Liu. "A Survey of Retrieval Algorithms in Ad and Content Recommendation Systems." arXiv:2407.01712, July 2024. and Liwei Pan et al. "A Survey on Sequential Recommendation." arXiv:2412.12770, December 2024 (v2 March 2025). [Survey 2] explicitly normalizes industrial SR around retrieve-then-attend patterns (SIM-style) for ultra-long behavior and ranking on dozens to thousands of items, not open-ended generation at full catalog scale. Kuaishou-RecModel et al. "A Survey of Generative Recommendation from a Tri-Decoupled Perspective: Tokenization, Architecture, and Optimization." Preprints 202512.0203 v1, December 2025. [Survey 3] documents **named** generative lines (HSTU, MTGR, OneRec / OneSearch / OneLoc, Kuaiformer, EGA-V2) with MFU narratives—credible as *signals that some large shops ship GR-shaped modules*, not as proof that generative recsys is now the median platform default. A three-survey slice cannot support a confident calendar forecast for “when most of the industry flips”; treat any year-bound prediction as scenario planning gated by tokenizer quality, latency, and your own A/B bar. For 1–3 year learning ROI, prioritize **semantic-ID tokenization (RQ-VAE family)**, **retrieve-then-attend / ultra-long sequence design**, and **whole-path cost modeling** (MFU is one lens); keep **LLM-as-ranker** and **diffusion-first SR** as watch-list items unless you have a concrete surface hypothesis. The three surveys **agree** on cold start, attention cost, bias, and the need for staged serving evidence; they **tension** on whether cascades are legacy to be subsumed or the modular backbone you should keep investing in.

---

## 1. Direct Answers to the Four Questions

### 1.1 Classical retrieval/sequential — what's still SOTA, what's legacy?

**Still production-SOTA (per corpus):**

1. **Two-tower (dual-tower) deep retrieval + ANN top‑K** for organic feeds remains the central scalable decomposition in [Survey 1]; [Survey 2] assumes embedding-based recall as the upstream reality for SR stacks. One sentence: decoupled user/item encoders with approximate nearest-neighbor serving are still the reference architecture for recall at tens of millions of items.

2. **Inverted-index and classical targeting filters in ads** stay structurally central for fast user–ad matching alongside learned towers in [Survey 1]. One sentence: heuristic and index-first matching are not “deprecated ML”—they are load-bearing for latency and inventory structure in ad retrieval.

3. **Transformer ID sequence models (SASRec, BERT4Rec)** remain the canonical offline baselines and industrial comparators for sequential ranking on candidate lists in [Survey 2]. One sentence: if your offline grid does not include these, you are not speaking the same language as the SR survey’s evidence tables.

4. **SIM-style retrieve-then-attend** (GSU/ESU, two-stage long histories) is the industrial pattern called out for **ultra-long** behavior (including TWIN / TWIN-V2 at Kuaishou in [Survey 2]). One sentence: before you pay quadratic attention over thousands of events, the surveys converge on *selecting* a short attendable sub-sequence.

5. **Multi-tower / three-tower extensions** over plain two-tower are framed as active improvements in [Survey 1] where multiple objectives or modalities need separate encoders. One sentence: “more towers” is still an incremental SOTA path inside discriminative retrieval.

**Aging or higher-risk (per corpus, not “forbidden”):**

1. **Treating attention-heavy towers as “free” at retrieval QPS** is flagged as a scale bottleneck in [Survey 1]; the mitigation story shifts toward co-design and sparser stacks in [Survey 3]. Legacy mindset: “just add self-attention everywhere in recall.”

2. **End-to-end LLM item-list generation at strict production latency** is consistently graded as early / failure-prone (invalid semantic IDs, hallucinated items) in [Survey 2]. Legacy is not “LLMs exist”—it is assuming they can replace grounded rankers without catalog controls.

3. **Pure offline claims for generative SR rows** without serving constraints: [Survey 2] keeps generative baselines in benchmark tables while warning on deployment defaults; treating offline HR@10 alone as “production SOTA” for generative stacks is the aging interpretation.

### 1.2 Realistic generative recsys production timeline

**Generative recsys at production today**—in the narrow sense of semantic-ID tokenization, decoder-heavy stacks, and RL-style alignment narratives—is **not “zero”** in this corpus: [Survey 3] names multiple **paper-attributed** industrial lines (HSTU, MTGR, OneRec / OneSearch / OneLoc, Kuaiformer, EGA-V2) and cites MFU comparisons (e.g., cascaded discriminative **4.6% / 11.2%** train/infer MFU vs. OneRec **23.7% / 28.8%** in the survey’s cited narrative). Alongside that, [Survey 2] documents **discriminative** ultra-long industrial modeling (TWIN / TWIN-V2) that is production-grade but **not** SID/NTP generative recsys in the [Survey 3] sense. So the honest headline is: **some large platforms likely ship GR-flavored components today**, but the corpus does **not** enumerate deployments across Netflix-scale, mid-market, and long-tail apps, and it does **not** give cross-company A/B lift tables for generative stacks.

**Likely broadening** to “majority of large platforms run generative-first cascades” is **not** statistically justified here. [Survey 3]’s mechanism story (misaligned cascade objectives, parameter-heavy embeddings, MFU upside) supports **selective** stage replacement; [Survey 1] and [Survey 2] counter with modular latency, invalid-token risk, and the millions→thousands→dozens funnel. Actionable **planning** (not forecasting): pilot generative modules where tokenizer–catalog grounding is tractable; keep cascades as default; require internal latency and A/B evidence. Post-**December 2025** evidence is outside this synthesis window.

### 1.3 Where to invest 1–3 yr learning effort

Ordered, opinionated list for a cascade engineer:

1. **Semantic ID tokenization (RQ-VAE / ResKmeans family, collision handling, joint tokenizer–generator training).** *Why:* [Survey 2] and [Survey 3] treat SID as the shared engineering object between “generative SR research” and “industrial GR tokenizer axis.” *First step:* reproduce RQ-VAE item codes on a public catalog subset and measure collision rate vs. downstream NTP loss.

2. **Ultra-long sequence systems (SIM / retrieve-then-attend, two-stage GSU+ESU patterns).** *Why:* [Survey 2] centers these for >1000-event histories and cites Kuaishou industrial lines—directly relevant to pre-ranking/ranking in your cascade. *First step:* implement GSU top‑k + local attention on a session dataset and compare to full-sequence baseline under a fixed CPU/GPU budget.

3. **Whole-path cost & MFU literacy (train + infer, not single-kernel bragging).** *Why:* [Survey 3] uses MFU as a comparative narrative; [Survey 1] warns about attention-in-tower costs at recall. *First step:* build a spreadsheet model: ANN + rerankers + feature logging vs. a hypothetical generative ranker serving curve.

4. **RL alignment primitives (DPO / GRPO families) tied to multi-objective rewards.** *Why:* [Survey 3] makes preference alignment a first-class optimization axis; the other surveys barely teach reward design. *First step:* run a toy offline preference optimization on a list-wise proxy before touching production objectives.

5. **Two-tower + multi-tower deepening (if your recall layer is shallow).** *Why:* [Survey 1] still positions this as the organic-feed workhorse; improvements are incremental but deployable. *First step:* audit tower feature parity, negative sampling, and ANN parameters against published best practices in the retrieval survey.

6. **Deprioritize (unless you have a sharp hypothesis):** **prompt-first LLM rankers (P5-style)** and **diffusion-first recommendation**—both surveys flag cost, latency, or sparsity issues; keep on the horizon, not the core quarterly plan ([Survey 2], [Survey 3]).

### 1.4 Where do the three surveys agree, disagree, or leave gaps?

Drawing from `literature-review.md` Section 8 (tension table) and Phase 3.7 contradiction rows in the per-paper reverse citation maps.

- **Agreements (3 of 3 sources):** Cold start and sparsity remain hard ([Survey 1]–[Survey 3]); compute and long-sequence cost are first-class risks; data bias and exposure effects matter for training; privacy/ethics and centralized profiling show up across surveys; “LLMs as **offline** augmenters” (synthetic data, keywords, embeddings) is a safer default than high-QPS generative rankers ([Survey 1], [Survey 2]).

- **Disagreements / tension points:** **Pipeline shape**—cascades as necessary modular stages ([Survey 1], [Survey 2] small-candidate ranking) vs. cascades as error-accumulating legacy to be subsumed by unified generative models ([Survey 3]). **Hardware narrative**—lean retrieval vs. MFU-unified generative kernels. **Item interface**—sparse IDs + large embedding tables vs. semantic token compression; same methods get labeled “baseline” in [Survey 2] Table 5 and “tokenizer evolution” in [Survey 3].

- **Gaps (no source covers adequately):** Deep **re-ranking**-only methods and diversity constraints; **ad auction** integration and bid optimization; **multi-objective ads** beyond high-level mentions; **on-device** / federated deployment; **platform-specific latency SLAs** and DAU-scale numbers; apples-to-apples **cross-survey benchmarks** (Table 5 is SR-only in [Survey 2]).

---

## 2. Most Fundamental Methods (top 5 from the method tracker)

Order follows the composite leaders in `method-tracker.md` **Top Method Analysis** (rewritten for your planning lens).

**1. HSTU** — *Family:* generative architecture / sparse-ID sequence modeling. For a production engineer, HSTU matters because [Survey 3] uses it as a bridge narrative between classical ID-sequence ranking and generative stacks that still speak “industrial scale.” It is the conceptual hook for whether your org should experiment with **sparse-ID generative rankers** before jumping to full SID decoders. **First touch:** read the primary HSTU paper cited in [Survey 3], then trace how your current ranking stage could accept a generative head without rewriting recall.

**2. OneRec / One-series** — *Family:* end-to-end generative stacks. This line encodes the strongest “unified model vs. fragmented cascade” argument in [Survey 3], including MFU comparisons against cascaded discriminative systems in the survey text. **First touch:** draft a one-page **risk register** (catalog coverage, invalid tokens, rollback) and pair it with the MFU numbers as *hypotheses to validate*, not conclusions.

**3. RQ-VAE (semantic ID quantization)** — *Family:* generative tokenization. SID construction is the shared bottleneck between generative SR research in [Survey 2] and tokenizer-axis engineering in [Survey 3]; tokenizer mistakes become generation mistakes. **First touch:** implement RQ-VAE codes for your item taxonomy subset; measure prefix collisions and out-of-vocabulary behavior under catalog updates.

**4. TIGER** — *Family:* generative retrieval with semantic IDs. TIGER is the concrete pattern for “retrieval as generation” experiments, appearing as a generative baseline row in [Survey 2] and as foundational lineage in [Survey 3]. **First touch:** run a toy **generative recall** task (generate top‑k token sequences) beside your two-tower ANN recall and compare latency–quality curves on the same candidate pool.

**5. SASRec** — *Family:* sequential ID Transformer baseline. Still the most common uni-directional SR reference in [Survey 2]; any proposal that cannot beat SASRec on standard slices is not ready for internal advocacy. **First touch:** reproduce SASRec on Amazon-style public splits using the survey’s quoted metric setup as a sanity baseline.

---

## 3. Recommendations (the actionable section)

> **Decision 1: [Keep] two-tower / ANN organic retrieval as default recall**  
> *Why now:* [Survey 1] still centers this decomposition; [Survey 2] assumes embedding recall upstream of SR ranking.  
> *First action:* Run a quarterly audit of tower freshness, negative sampling, and ANN recall@k vs. business guardrails.  
> *Cost / risk:* Low engineering cost; risk if wrong is mild— you solidify a known-good stage.

> **Decision 2: [Pilot] SIM-style long-history module adjacent to ranking**  
> *Why now:* [Survey 2] documents industrial ultra-long patterns and failure modes you can copy structurally without adopting generative serving.  
> *First action:* Prototype GSU top‑k + local attention on your longest available user histories with a fixed latency budget.  
> *Cost / risk:* Medium engineering cost; risk is mis-tuned GSU washing out signal if k or features are wrong.

> **Decision 3: [Study] RQ-VAE / semantic ID stack on a sandbox catalog**  
> *Why now:* [Survey 2] and [Survey 3] converge on SID as the generative interface; collisions and invalid tokens are cited risks.  
> *First action:* Build SID indices for a non-production catalog mirror; run NTP training on historical sequences.  
> *Cost / risk:* Medium learning + infra cost; risk is investing tokenizer effort while ranking objectives stay pointwise—pair with a clear success metric.

> **Decision 4: [Watch] end-to-end OneRec-style unified stacks**  
> *Why now:* [Survey 3] positions OneRec / OneSearch / OneLoc with MFU and deployment narrative, but [Survey 2] keeps generative evidence largely offline.  
> *First action:* Track primary papers and **any** public postmortems; do not commit headcount until internal pilot metrics exist.  
> *Cost / risk:* Low burn if “watch”; high risk if you adopt on narrative alone—wrong stack bet burns org trust.

> **Decision 5: [Deprioritize] prompt-first LLM ranker (P5-class) for default serving**  
> *Why now:* [Survey 2] includes P5 in baselines but flags generative/LLM limitations; [Survey 3] contrasts early text-based unification with SID efficiency.  
> *First action:* Restrict P5-style ideas to offline enrichment or developer tooling this quarter.  
> *Cost / risk:* Saves latency and hallucination risk; “risk if wrong” is opportunity cost if you *had* a rare surface where prompts win—revisit with evidence.

> **Decision 6: [Adopt] RL alignment literacy at reading-group depth**  
> *Why now:* [Survey 3] elevates DPO/GRPO-style alignment for platform objectives; other surveys barely teach it.  
> *First action:* Two-session reading group on list-wise rewards + offline preference optimization toy.  
> *Cost / risk:* Low direct engineering cost; risk is over-applying RL without reward hygiene—keep it educational until objectives are crisp.

> **Decision 7: [Read next] primary sources outside this corpus**  
> *Why now:* Surveys disagree on lifecycle labels for the same method; tie-breakers live in primaries and your metrics (`literature-review.md` §5).  
> *First action:* Pick **one** generative line (e.g., TIGER or OneRec) and read its canonical paper + any system card.  
> *Cost / risk:* Time cost only; reduces survey-induced certainty bias.

> **Decision 8: [Wait] declaring generative recsys the universal replacement for your cascade**  
> *Why now:* [Survey 2]’s deployment default remains small-candidate discriminative ranking; [Survey 1] never argues generative recall dominance.  
> *First action:* Explicitly document “no org-wide rewrite” until tokenizer + latency + A/B gates clear.  
> *Cost / risk:* Opportunity cost if competitors move faster—but **waiting with pilots running** is different from freezing learning.

---

## 4. Honest Caveats

- **Three-source corpus** — not a full literature scan. The gaps listed in §1.4 are the highest-value follow-ups (ranking-only depth, auctions, on-device, fairness).
- **Author-affiliation skew** — [Survey 3] is Kuaishou-adjacent; expect bullish deployment storytelling for lines tied to that ecosystem. Triangulate with primaries and third-party evidence.
- **Publication-window bias** — coverage is essentially Jul 2024 through Dec 2025; anything newer is invisible here.
- **Surveys ≠ benchmarks** — when [Survey 2] Table 5 and [Survey 3]’s industrial narrative disagree on “what wins,” your A/B harness and offline replay are the tiebreaker.

---

## Source Catalog

| Short form | Full citation |
|------------|---------------|
| Survey 1 | Yu Zhao, Fang Liu. "A Survey of Retrieval Algorithms in Ad and Content Recommendation Systems." arXiv:2407.01712, July 2024. |
| Survey 2 | Liwei Pan et al. "A Survey on Sequential Recommendation." arXiv:2412.12770, December 2024 (v2 March 2025). |
| Survey 3 | Kuaishou-RecModel et al. "A Survey of Generative Recommendation from a Tri-Decoupled Perspective: Tokenization, Architecture, and Optimization." Preprints 202512.0203 v1, December 2025. |

## Sanity check

NotebookLM’s cross-source `notebook_query` answer claims a **“massive transition”** to **decoder-only** models that **“completely eliminat[e] multi-stage pipelines,”** which is **stronger** than §1.2 here, where [Survey 2] keeps **cascaded** small-candidate SR and [Survey 1] keeps two-tower + indexing. The NLM line **over-weights [Survey 3]** vs. [Survey 1]/[Survey 2]. **Trust** this brief and `literature-review.md` §7–§8 (hybrid era, pilots, Phase 3.7 pipeline contradictions). Treat NLM’s paragraph as **[Survey 3]’s thesis compressed**, not an industry census.
