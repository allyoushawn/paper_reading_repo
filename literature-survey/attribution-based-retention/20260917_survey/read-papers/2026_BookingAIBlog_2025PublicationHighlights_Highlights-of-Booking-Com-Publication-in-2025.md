# Highlights of Booking.com's publication in 2025

**Source:** https://booking.ai/highlights-of-booking-coms-publication-in-2025-1c1a6deba066 | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** 2026-01-20, Booking.com (booking.ai Medium blog) | **Authors / team:** multiple (incl. Dmitri Goldenberg, Philipp Hager; roundup of 8 accepted papers) | **Analyzed:** 2026-09-17

## 1. Summary
Roundup of Booking.com's 2025 accepted publications. Most relevant: "Challenges and Methods of Causal Promotions Recommendation in E-commerce" (Goldenberg et al., TORS) and "Converted Data is All You Need" (CIKM 2025), which use causal ML for continuous promotion-campaign optimization, including a "converted-only data" approach that filters non-converted sessions to reduce noise and simplify budget-constrained promotion-allocation attribution.

## 2. Evidence
Described as deployed at scale ("positively impacting the experience of millions of customers"); no specific quantitative metrics are given in this summary post — would require reading the individually cited papers.

## 3. Limitations
The post itself does not discuss method limitations; real-world deployment complexity (triggered costs, sparse conversions, multi-product interactions) is acknowledged only qualitatively.

## 4. Project Relevance
- **Answers:** Q1 — represents current (2025–2026) industry practice in causal promotion attribution, adjacent to but not the same problem as retention attribution.
- **Attributes retention to individual interactions?** partly — attributes conversion (not retention/days-active) to promotional touchpoints, and only for converted sessions.
- **Transferable components:** retrospective / "converted-only" estimation to reduce noise; causal uplift framing (references an AddIPW-style estimator) for interference-aware multi-touch settings.
- **Required changes:** replace conversion outcome with N7 retention; cannot rely on "converted-only" filtering since retention labels exist regardless of conversion, and dropping non-matching swipes would reintroduce the very selection bias the project wants removed; extend single-touchpoint promotion credit to a multi-swipe sequence.
- **On last-touch:** not directly discussed in this summary; no explicit comparison to last-touch/last-click.
- **Transfer rating:** adaptable — describes live, large-scale causal promotion-attribution work adjacent to the project's problem, but the "converted-only" simplification runs counter to the project's specific need to also credit non-converting earlier swipes.
