# Attributed, But Not Incremental: Cannibalization-Corrected Attribution for Large-Scale Advertising

**Source:** https://arxiv.org/pdf/2606.26690.pdf | **NLM source id:** 65be2782-a8bc-41e2-a103-4e8c322830f8 | **Year / venue:** 2026, ADKDD '26 (August 10, 2026, Jeju, Korea) | **Authors / affiliation:** Donghui Li, Bowen Yuan, Zili Yang, Qinxin Chen, Lijing Song — TikTok / ByteDance | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Production attribution (last-touch or simple data-driven attribution) credits paid channels for conversions (Daily New Users) that would have happened anyway via organic demand or brand traffic — the "attribution–cannibalization mismatch." This overstates incremental growth and misallocates budget. The paper proposes ETDC+HCA: (1) Experiment-to-Daily Cannibalization uses sparse channel-day randomized incrementality experiments as causal anchors and fits a GLM (Huber loss, for robustness to noisy daily lift) over proxy/temporal/media-state features to extrapolate a continuous daily cannibalization rate C_t = 1 − Lift_t/A_t; (2) Hierarchical Cannibalization Allocation propagates the calibrated cannibalized volume down through campaign/placement/device hierarchies under aggregate-consistency, feasibility, and locality constraints. **Unit of credit:** channel-day (ETDC), then business-hierarchy node (HCA) — not per-touchpoint or per-user. **Outcome:** Daily New Users (DNU) / net incremental ROI. **Bias handling:** treats cannibalization (users who'd convert anyway) as a causally-anchored correction learned from sparse randomized experiments, deployed as a lightweight add-on layer over the existing attribution pipeline.

## 2. Evidence
18 rounds of channel-level A/B incrementality experiments across up to 8 global markets, forward-in-time rolling validation. Overall calibration error index: Raw Attribution 1.00, Device ML 0.31 (69.11% reduction), ETDC+HCA 0.09 (91.38% reduction). Signed relative error IQR narrows from wide/unstable (Device ML: [-38%, 44%]) to tight and centered (ETDC+HCA: [-8.11%, 7.24%], median 0.60%). Per-slice, Raw Attribution overestimates lift by 179–334%; ETDC+HCA stays within -7% to +10%. Live deployment across multiple TikTok markets drove downstream budget/traffic adjustments and an ~15 percentage-point reduction in measured cannibalization rate.

## 3. Limitations
Depends on experiment quality/coverage — sparse, noisy, or incompletely-isolated experiments propagate uncertainty. Proxy-exogeneity assumption can break under product launches, seasonality, or channel shifts, requiring recalibration. HCA outputs are constrained operational allocations, not independently identified unit-level causal effects. Negative cannibalization (organic spillover/complementarity) is treated only as a bounded diagnostic signal, not fully modeled.

## 4. Prior works named
- Gordon et al. (2019) — comparison of ad measurement approaches, Facebook field experiments
- Blake, Nosko & Tadelis (2015) — paid search cannibalization of organic demand
- Dalessandro et al. (2012) — causally motivated attribution for online advertising
- Bencina et al. (2025) — LiDDA: data-driven attribution at LinkedIn
- Johnson, Lewis & Nubbemeyer (2017) — Ghost Ads

## 5. Project Relevance
- **Answers:** Q1
- **Attributes retention to individual interactions?** No — corrects channel/campaign-level acquisition (DNU) attribution, not per-user/per-interaction retention.
- **Transferable components:** Using sparse randomized holdouts as causal anchors to calibrate an observational attribution signal; explicit cannibalization/baseline-subtraction formulation (H_t = A_t − Lift_t); hierarchical, constraint-respecting credit propagation.
- **Required changes:** Move from channel-day scalar correction to micro sequence-level attribution over individual swipe/match/message histories; replace one-time DNU acquisition target with a recurring daily N7 retention outcome; model heterogeneous, multi-stage touchpoint types rather than a single upstream nominal-attribution input.
- **On last-touch:** Explicitly names last-touch attribution (LTA) as the common production baseline and shows it systematically overstates incremental value by crediting channels/touches that "harvest" existing demand rather than creating it.
- **Transfer rating:** background — the experiment-calibration and cannibalization-correction logic is conceptually relevant, but the framework operates at macro channel/campaign granularity, not on individual in-app interactions.
