# Method Tracker — Recsys Industry Trend & Future Planning

This tracker records methods named across the three surveys, who proposes vs. who treats them as baselines, and a fundamentality composite.

| Method | First Named In | Family | Mentioned As Baseline (count) | Variants Derived (count) | Components | Hyperparams | Notes | Fundamentality Composite |
|--------|----------------|--------|-------------------------------|--------------------------|-----------|-------------|-------|-------------------------|
| HSTU | 3 | generative-arch | 3 | 2 | n/a | n/a | Sparse-ID sequence modeling for ranking; industrial deployment narrative in GR survey (MTGR lineage). | +5 |
| OneRec / One-series | 3 | generative-arch | 3 | 3 | n/a | n/a | End-to-end generative; MFU narrative vs cascades; named lines OneRec / OneSearch / OneLoc in GR survey. | +5 |
| RQ-VAE (semantic ID quantization) | 3 | generative-tokenizer | 3 | many (3+) | 4 | 4 | Dominant SID construction path in GR survey; ties LC-Rec / TIGER-class lines in corpus. | +5 |
| SASRec | 2 | sequential-id | 3 | many (3+) | 4 | 5 | Called “most popular” SR model; Table 5 baseline; Transformer-ID anchor across SR survey. | +4 |
| Two-Tower (dual-tower) retrieval | 1 | retrieval | 3 | many (3+) | 3 | 3 | Survey’s central organic-retrieval architecture; matrix-factorization extension; multi-/three-tower follow-ons. | +2 |
| BERT4Rec | 2 | sequential-id | 2 | many (3+) | 4 | 5 | Bi-directional Transformer SR; Table 5 baseline. | +4 |
| Collaborative filtering / CBF / hybrid | 1 | retrieval | 2 | many (3+) | n/a | n/a | Classical organic retrieval families alongside deep retrieval. | +2 |
| DIN | 3 | retrieval | 2 | many (3+) | 3 | 4 | Discriminative behavior-modeling anchor in GR survey background. | +2 |
| Inverted index (ad targeting) | 1 | retrieval | 2 | n/a | 2 | n/a | Efficient matching vs. user profiles in ad systems. | 0 |
| LC-Rec | 3 | generative-tokenizer | 2 | n/a | n/a | n/a | SID + collaborative/language semantics alignment example in GR survey. | 0 |
| Multi-task / three-tower extensions | 1 | retrieval | 2 | 2 | 4 | 4 | Described as improvements over plain two-tower. | 0 |
| P5 | 2 | sequential-llm | 2 | n/a | 6+ | 5+ | LLM-prompted multi-task SR; Table 5; GR survey discriminative/LLM anchor alongside DIN/DCN. | +4 |
| SIM | 2 | sequential-id | 2 | many (3+) | 3 | 4 | GSU/ESU long-sequence retrieval-attention pattern; SIM/ETA/QIN-style thread in SR survey. | +4 |
| TIGER | 2 | generative-tokenizer | 2 | many (3+) | 5 | 5 | Generative retrieval w/ semantic IDs; Table 5 generative row; GR survey cites TIGER lineage + follow-ups. | +5 |
| TWIN / TWIN-V2 | 2 | sequential-id | 2 | 2 | n/a | n/a | Cited industrial ultra-long CTR modeling at Kuaishou; composite 0 — thin cross-survey baseline/perf evidence in corpus. | 0 |
| UniSRec / multi-modal SR | 2 | sequential-id | 2 | n/a | 5+ | 5+ | Multi-modal vs pure-ID comparisons in quoted table; SR survey notes hyperparameter/collapse sensitivity — complex vs simple +1. | −1 |
| DCN | 3 | retrieval | 1 | 2 | 3 | 3 | Feature interaction exemplar in discriminative section. | 0 |

## Top Method Analysis

**HSTU** (composite +5) — Positions sparse-ID generative sequence models as a production-credible path for ranking-stage scale and hardware efficiency as you evaluate whether to graft GR modules onto your cascade or redesign stages.

**OneRec / One-series** (composite +5) — Captures the end-to-end generative stack narrative (MFU, named deployments) that defines the benchmark for “when does unified generation beat fragmented discriminative ops” over your next planning horizon.

**RQ-VAE (semantic ID quantization)** (composite +5) — Makes semantic-ID tokenization the default engineering object for catalog grounding and tokenizer–generator co-design before you commit to a generative serving path.

**TIGER** (composite +5) — Embodies generative retrieval with semantic IDs so you can separate “retrieval as generation” experiments from classical two-tower ANN loops in roadmaps.

**SASRec** (composite +4) — Remains the canonical Transformer-ID sequential baseline to beat in offline studies while you invest in long-sequence and generative extensions.

**BERT4Rec** (composite +4) — Keeps bi-directional sequence modeling in the standard comparison set for ranking small candidate lists as you test causal vs. non-causal encoders.

**P5** (composite +4) — Anchors LLM-as-multi-task-recommender framing so you can decide where prompting adds signal vs. latency cost relative to ID-first stacks.

**SIM** (composite +4) — Encodes the retrieve-then-attend template for ultra-long behavior, directly feeding cascade design (what to pre-select before expensive attention).

**Two-Tower (dual-tower) retrieval** (composite +2) — Still the reference decomposition for embedding retrieval at scale when you modernize recall without jumping to full generative recall.

**Collaborative filtering / CBF / hybrid** (composite +2) — Preserves the classical filter families as the sanity baseline when judging whether deep retrieval and generative IDs are worth their ops cost in your surfaces.

### Caveat

Composite scores are computed over a 3-source corpus; absolute baseline counts are small. Treat scores as relative ordering signals, not absolute fundamentality measures. The +3 threshold has been adapted (see Phase 3.5 brief).
