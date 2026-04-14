# Paper Analysis: Adapted Switch-back Testing to Quantify Incrementality for App Marketplace Search Ads

**Source:** https://doordash.engineering/2022/11/08/adapted-switch-back-testing-to-quantify-incrementality-for-app-marketplace-search-ads/  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Adapted Switch-back Testing to Quantify Incrementality for App Marketplace Search Ads  
**Authors:** DoorDash Data Science / Engineering Team  
**Abstract:**
This DoorDash engineering blog post describes an adapted switchback testing methodology for measuring incrementality of app marketplace search ads when the publisher lacks A/B testing infrastructure, geo-targeting, user-level randomization, or robust synthetic control capabilities. The method uses alternating time-based treatment assignment, bootstrapped historical baseline confidence intervals, and a scalar conversion factor to estimate incremental new user acquisitions.

**Key contributions:**
- Adapted switchback experiment: randomize treatment (campaign on/off) by day in week 1, reverse in week 2, repeat
- Alternating time intervals chosen over simple/stratified random sampling — balances weekends without requiring long test duration
- Bootstrapped baseline CI: simulate on/off pattern on historical data with replacement, compute 95% CI for normal variation
- Incrementality scalar: ratio of experimentally measured incrementality to standard attribution (last-click/MTA) — provides a correction factor for calibrating attribution models
- Framework for when switchback is applicable: immediate conversion, stable historical trend, clean experimental unit randomization

**Methodology:**
(1) Identify new-user acquisition campaigns. (2) Alternate campaign on/off by day (week 1 pattern, reversed in week 2). (3) Measure app downloads per day. (4) Compute download difference between on/off groups. (5) Multiply by historically stable download-to-first-order conversion rate → incremental new customers. (6) Bootstrap historical data (same on/off pattern) → 95% CI for natural download variation. (7) Test if observed lift exceeds CI. (8) Calculate incrementality scalar = experimentally measured lift / attribution-reported lift. Operational detail: account for campaign pause/unpause lag of ~2 hours.

**Main results:**
Confidential metric values not disclosed. Primary outcome: incrementality scalar computed for the app marketplace channel. This scalar calibrates DoorDash's Marketing Mix Model and provides right-sizing for attribution results from last-click/MTA models on this publisher.

---

## 2. Experiment Critique

**Design:**
Practical case study with rigorous design justification. The alternating time interval design avoids weekend imbalance without requiring long test duration — a genuine methodological contribution for practitioners.

**Statistical validity:**
The bootstrapped CI approach is a valid frequentist method for establishing the natural variation baseline. No parametric assumptions about download distribution. The t-test on historical data + bootstrap resampling is standard and appropriate. Limitation: assumes stable conversion rate (download → first order) which may fluctuate.

**Online experiments (if any):**
This IS an online field experiment (ads turned on/off in production).

**Reproducibility:**
No code or data released. Methodology fully described and implementable by any team with access to daily campaign metrics and historical download data.

**Overall:**
Strong practical contribution for marketers dealing with measurement-constrained advertising platforms. The incrementality scalar concept (calibrating attribution models using experimental evidence) is widely applicable. More rigorous than most industry blog posts on the topic.

---

## 3. Industry Contribution

**Deployability:**
Very high. The switchback design requires only daily campaign on/off control and download tracking — no specialized infrastructure. The bootstrapping baseline is simple to implement.

**Problems solved:**
For dating platform attribution: this methodology is directly applicable for measuring whether push notifications, email campaigns, or in-app promotions are actually driving retention vs. attributing organic retention to those channels. The incrementality scalar pattern (experiment-based correction of attribution) is a key tool for any platform measuring retention interventions.

**Engineering cost:**
Very low. Day-level campaign toggling + download/action tracking is standard. Bootstrap computation is fast.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
Not a research paper — industry application. The switchback/turnback testing framework has prior art in DoorDash's own marketplace testing work. The alternating time interval design and bootstrapped baseline are practical innovations within that framework.

**Prior work comparison:**
Geo experiments (Vaver & Koehler 2011, Trimmed Match): require geo-targeting capability not available here; switchback fills the gap. Standard A/B testing: requires user-level randomization not available from this publisher.

**Verification:**
The incrementality scalar outcome is a concrete, measurable result. The 95% CI validity is straightforward.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| DoorDash App Marketplace Ad Data | Not public | No | Confidential production data |

**Offline experiment reproducibility:**
Not reproducible — proprietary data.

---

## 6. Community Reaction

DoorDash Engineering Blog, 2022. Practical industry contribution. No formal citation count. The switchback testing pattern for ad incrementality is increasingly standard in industry — DoorDash's documented implementation adds to the growing body of practical guidance.

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| [2020_arXiv_MinimaxSwitchback_Design-Analysis-Switchback-Experiments](./2020_arXiv_MinimaxSwitchback_Design-Analysis-Switchback-Experiments.md) | 1. Summary | Unique survey token `Switchback` (filename disambiguation) appears in scanned sections. |

---

## Meta Information

**Authors:** DoorDash Data Science Team  
**Affiliations:** DoorDash  
**Venue:** DoorDash Engineering Blog 2022  
**Year:** 2022  
**PDF:** https://doordash.engineering/2022/11/08/adapted-switch-back-testing-to-quantify-incrementality-for-app-marketplace-search-ads/  
**Relevance:** Core  
**Priority:** 3
