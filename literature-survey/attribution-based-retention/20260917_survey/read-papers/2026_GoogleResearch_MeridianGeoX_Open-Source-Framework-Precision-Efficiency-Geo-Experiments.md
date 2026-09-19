# Meridian GeoX: An Open-Source Framework for Precision and Efficiency in Geo Experiments

**Source:** https://research.google/pubs/meridian-geox-an-open-source-framework-for-precision-and-efficiency-in-geo-experiments/ | **Retrieved via:** NotebookLM source 535371ff-3748-464a-b495-57e0c4b8ce23 | **Year / venue:** 2026 (techreport), Google Research | **Authors / team:** Steven Ye, Fabian Sinn, Yunxiao Li, Yang Jiao (Google) | **Analyzed:** 2026-09-17

## 1. Summary
Introduces Meridian GeoX, Google's open-source framework for geo experiments measuring media/ad effectiveness. Combines data-driven stratified sampling with counterfactual models (Time-Based Regression, Synthetic Control, Synthetic Difference-in-Differences) and a novel Design-Aware Placebo Inference engine to reduce experiment budget and variance while controlling false positives; integrates with the Meridian Marketing-Mix Model.

## 2. Evidence
Benchmarked against industry alternatives: reports improved predictive accuracy, lower Minimum Detectable Effect (MDE), reduced budget requirements, and rigorous false-positive control under placebo evaluation. No specific numeric results are given at the abstract/summary level.

## 3. Limitations
Operates at aggregate geo/market level, not individual users or events. Requires sufficient historical pre-period data and cross-geo variation. Built for top-down media incrementality benchmarking, not granular in-app touchpoint attribution.

## 4. Project Relevance
- **Answers:** Q1 (adjacent) — 2026 state-of-the-art causal geo-experiment tooling, not user-level attribution.
- **Attributes retention to individual interactions?** no — unit of analysis is geographic region/market, not user or interaction.
- **Transferable components:** the general synthetic-control / placebo counterfactual-inference logic could inform macro geo-holdout validation of a ranking-model rollout, but not the per-swipe credit mechanism itself.
- **Required changes:** would need to move entirely from macro geo time-series to user-/event-level sequence modeling — different unit, different data structure.
- **On last-touch:** not discussed.
- **Transfer rating:** background — a state-of-the-art causal geo-experiment framework for ad measurement, useful only as macro validation context, not a transferable attribution method.
