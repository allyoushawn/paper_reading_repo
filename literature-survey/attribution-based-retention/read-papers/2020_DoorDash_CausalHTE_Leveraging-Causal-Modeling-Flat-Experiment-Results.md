# Paper Analysis: Leveraging Causal Modeling to Get More Value from Flat Experiment Results

**Source:** https://doordash.engineering/2020/09/18/causal-modeling-to-get-more-value-from-flat-experiment-results/  
**Date analyzed:** 2026-04-11

---

## 1. Summary

**Title:** Leveraging Causal Modeling to Get More Value from Flat Experiment Results  
**Authors:** Ezra Berger, Jared Bauman (DoorDash)  
**Abstract:**
This DoorDash engineering blog post describes how to use Heterogeneous Treatment Effect (HTE) / uplift modeling to extract business value from A/B experiments that yield flat (non-significant) aggregate results. The core insight is that flat average effects can hide substantial subpopulation-level effects. By estimating CATE using S-learner with LightGBM, DoorDash identified churned customers who would respond to promotions, reducing promotional cost per incremental delivery by 33%.

**Key contributions:**
- Practical S-learner implementation with LightGBM for consumer promotion targeting
- Noise contrastive estimation for generating negative examples when original data was not A/B tested
- 33% reduction in Promotional Cost/Incremental Delivery at 5% audience reach
- Tutorial-level explanation of S/T/X-learner tradeoffs for practitioners

**Methodology:**
S-learner: single LightGBM model trained on (treatment T, user features X) → Y. CATE = S(1,X) − S(0,X). Features: historical delivery counts, app visits, customer tenure, delivery quality (ratings), merchant count. Training data: positive examples from actual promo redemptions; negative examples from noise contrastive estimation (replace positive examples with non-ordering users in same region at same time). S-learner chosen over T/X because dataset was small relative to effect size.

**Main results:**
At 5% audience reach targeting: 33% reduction in Promotional Cost per Incremental Delivery vs. untargeted baseline. Framework generalizes to targeting curves — marketers can tune reach/cost tradeoff by adjusting CATE threshold.

---

## 2. Experiment Critique

**Design:**
Single case study (consumer churn re-engagement). No statistical comparison against T-learner or X-learner on this dataset. The noise contrastive estimation for negative examples is a pragmatic workaround that introduces potential bias if churned user population differs from the negative sample population.

**Statistical validity:**
Limited — no confidence intervals reported on the 33% improvement. Blog post format provides directional results without formal statistical testing. The "5% audience reach → 33% cost reduction" is a meaningful practical result.

**Online experiments (if any):**
The S-learner targets churned users; deployment presumably validated via online comparison (implied but not detailed).

**Reproducibility:**
No code or data released. Methodology is fully described and implementable.

**Overall:**
Strong practical blog post for ML practitioners. The S-learner with noise contrastive estimation workaround for non-RCT data is a useful pattern. The explicit tradeoff discussion (S vs T vs X learner) is well-written. Not a research contribution but a validated industry application.

---

## 3. Industry Contribution

**Deployability:**
Very high. S-learner + LightGBM is one of the simplest possible CATE implementations. DoorDash production deployment with measurable 33% cost reduction validates the approach. The noise contrastive estimation workaround is directly applicable to any platform lacking clean RCT data.

**Problems solved:**
For dating platform retention: the exact same pattern applies — flat aggregate results from "send push notification to re-engage dormant users" experiments may hide that only a subset of users (e.g., users who received a match recently, or users with high historical engagement) respond positively. S-learner CATE targeting can identify those users and reduce wasted notifications.

**Engineering cost:**
Very low. S-learner requires a single LightGBM model training. The noise contrastive estimation is a simple data processing step.

---

## 4. Novelty vs. Prior Work

**Paper's claimed novelty:**
Not a research paper — industry application. References Kunzel et al. (2019) X-learner/S-learner paper as the theoretical foundation.

**Prior work comparison:**
Kunzel et al. PNAS 2019: theoretical S/T/X-learner framework; DoorDash implements the S-learner with LightGBM in production. The noise contrastive estimation for non-RCT data is a practical adaptation not in the original framework.

**Verification:**
33% cost reduction is a concrete production metric.

---

## 5. Dataset Availability

| Dataset | Link | Accessible | Notes |
|---------|------|------------|-------|
| DoorDash Consumer Promotion Data | Not public | No | Proprietary historical promo redemption data |

**Offline experiment reproducibility:**
Not reproducible — proprietary data.

---

## 6. Community Reaction

DoorDash Engineering Blog, 2020. Widely shared in industry ML circles. One of the clearer practical explanations of CATE/uplift modeling for non-academic audiences. No formal citation count (blog post).

---

## Papers That Mention This Paper (Reverse Citation Map)

Scanned source sections in other corpus files: headings matching Introduction / Related Work / Background / Literature Review; **1. Summary**; **Novelty** / **Prior Work**; and any `##` block before the first Experiment or Method section.

| Mentioning Paper | Mention Context | Summary of Original Wording |
|------------|----------|----------|
| *(none yet)* | — | No inbound mentions from corpus in scanned sections (traceability). |

---

## Meta Information

**Authors:** Ezra Berger, Jared Bauman  
**Affiliations:** DoorDash  
**Venue:** DoorDash Engineering Blog 2020  
**Year:** 2020  
**PDF:** https://doordash.engineering/2020/09/18/causal-modeling-to-get-more-value-from-flat-experiment-results/  
**Relevance:** Related  
**Priority:** 3
