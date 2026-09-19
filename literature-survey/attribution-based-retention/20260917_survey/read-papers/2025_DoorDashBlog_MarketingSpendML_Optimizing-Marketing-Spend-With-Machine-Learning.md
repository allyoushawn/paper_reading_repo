# Optimizing DoorDash's Marketing Spend with Machine Learning

**Source:** https://careersatdoordash.com/blog/optimizing-marketing-spend-with-ml/ | **Retrieved via:** jina proxy (direct WebFetch returned 403) | **Year / venue:** item metadata lists 2025-04; page byline shows July 31, 2020 — date discrepancy, flagged not resolved | **Authors / team:** Aman Dhesi, Robert B. Kaspar (DoorDash) | **Analyzed:** 2026-09-17

## 1. Summary
Describes an ML platform that builds per-campaign cost curves (across thousands of campaigns and multiple channels) to optimally allocate marketing budget for new-user acquisition, using ML-generated synthetic data to handle sparse and noisy weekly spend data.

## 2. Evidence
Projects 10 to 30 percent lower marketing cost for the same customer volume; describes an ongoing rollout managing part of the marketing team's weekly budget. No controlled-experiment numbers are published.

## 3. Limitations
Noisy/sparse weekly data for low-spend campaigns; clustered spend data lacking historical low-spend ranges; risk of model extrapolation beyond observed spend ranges.

## 4. Project Relevance
- **Answers:** Q1 — confirms the tag's flagged claim: DoorDash explicitly uses a **modified last-touch attribution** model, at the channel level.
- **Attributes retention to individual interactions?** no — attributes new-user acquisition conversion to a marketing channel, not retention to an in-app interaction.
- **Transferable components:** synthetic-data augmentation for sparse/noisy interaction data; general cost-curve / budget-allocation framing.
- **Required changes:** unit of credit must move from channel to individual in-app interaction; outcome must move from acquisition conversion to N7 retention; last-touch must be replaced by a fractional/causal credit scheme.
- **On last-touch:** explicitly confirmed — DoorDash uses "modified last-touch attribution" at the channel level as the uncritiqued foundation for its cost curves.
- **Transfer rating:** background — confirms modified last-touch is still current industry practice (useful negative evidence for Q1) but offers no fractional-credit or bias-correction method to transfer.
