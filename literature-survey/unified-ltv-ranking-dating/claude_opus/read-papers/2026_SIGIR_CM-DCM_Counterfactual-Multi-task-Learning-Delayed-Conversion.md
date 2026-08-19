# Paper Analysis: Counterfactual Multi-task Learning for Delayed Conversion Modeling in E-commerce Sales Pre-Promotion

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/2604.21675.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Counterfactual Multi-task Learning for Delayed Conversion Modeling in E-commerce Sales Pre-Promotion
**Authors:** Xin Song, Kaiyuan Li, Jinxin Hu (Alibaba Group)
**Venue/Year:** SIGIR '26, 2026 (arXiv:2604.21675)

CM-DCM targets a delayed-conversion pattern specific to promotional e-commerce: during the pre-promotion window users browse and add items to cart but deliberately postpone purchase until the promotion day itself, so conversions concentrate sharply on one future date rather than decaying continuously over time as standard delayed-feedback models assume. The architecture is a multi-task stack: a pretrained "Ori CVR/ATC Predictor" tower (frozen via stop-gradient) supplies a baseline same-day conversion and add-to-cart probability, and a new "Delay CVR Predictor" tower estimates the residual probability that a pre-promotion click converts specifically on the promotion day; the two are summed to give the final all-conversion probability. A personalized gating mechanism (inspired by PEPNet) modulates the frozen tower's hidden representations with real-time add-to-cart/purchase behavior sequences before feeding the Delay tower, adaptively transferring pretrained knowledge under sparse pre-promotion data. The paper's central causal contribution is a counterfactual causal regularizer: because observed add-to-cart→conversion correlations are confounded by user intent and item popularity, a Doubly Robust (DR) estimator (outcome regression + inverse-propensity-weighted correction, using a pretrained ATC model as the propensity model) is used to compute an individual causal-effect estimate of the add-to-cart action, and the model's delayed-CVR prediction is regularized to align with that DR-based causal estimate for users who added to cart. Evaluated offline on Taobao, Tmall, and an internal industrial ads dataset (AUC_all, AUC_delay, NLL_delay) against DFM-lineage baselines (FNW, ES-DFM, DEFER, DEFUSE, HDR, plus "reuse" variants), CM-DCM significantly outperforms all baselines, and an online A/B test during two major promotional events (Double 11 and Double 12, 20% traffic each arm, six days) reported +7.87% revenue, +4.24% delayed GMV, +1.42% overall GMV, and only +2ms P99 latency.

## 2. Experiment Critique / 3. Industry Contribution / 4. Novelty vs. Prior Work / 5. Dataset Availability

Condensed per the Priority-4 depth rule — see the Reference Card (Section 7) and Project Relevance below. Datasets: Taobao (public, tianchi.aliyun.com/dataset/649) and Tmall (public, tianchi.aliyun.com/dataset/140281), both repurposed by the authors into pre-promotion/promotion splits since neither carries native promotion labels; plus a proprietary Alibaba industrial ads dataset (July 1–Nov 11, 2023, spanning five major promo days D7–D11). Ablation study (industrial dataset) shows each of the three components — the All-cvr transition-probability term, the Personalized Gating module, and the Counterfactual Causal Regularization (CCRA) — contributes measurably, with CCRA removal causing the largest degradation. Novelty is the combination: this is presented as the first work to model delayed conversion specifically for the pre-promotion phase (as opposed to the generic continuous-delay assumption of the standard DFM lineage), and the first in this lineage to inject a Doubly-Robust causal-effect estimate as a training regularizer rather than relying solely on importance-sampling label correction.

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Counterfactual Multi-task Learning for Delayed Conversion Modeling in E-commerce Sales Pre-Promotion," Xin Song, Kaiyuan Li, Jinxin Hu; Alibaba Group; SIGIR '26 (49th ACM SIGIR Conference), 2026; https://doi.org/10.1145/3805712.3809849, arXiv:2604.21675 |
| 2 | Source type | Industry paper (Alibaba Group, with online A/B deployment) |
| 3 | Direction | D7 |
| 4 | Problem setting | Delayed CVR prediction in the pre-promotion window of e-commerce sales events (e.g., Double 11), where conversions are not continuously delayed but concentrate sharply on the promotion day, violating the continuous-delay-window assumption of standard delayed feedback models. |
| 5 | Objective and label definition | Two binary labels per pre-promotion click: y^all_cvr (1 if the user converts either same-day or on the promotion day, 0 otherwise) and y^delay_cvr (1 only if conversion occurs specifically on the promotion day despite the click occurring during pre-promotion, 0 otherwise). Non-conversion by the fixed promotion-day cutoff resolves the label deterministically as 0 for both — there is no open-ended waiting/duplication mechanism; the horizon is a single fixed future date (the promotion day), not a rolling elapsed-time window. Pre-promotion windows used: 3–7 days (industrial platform's typical warm-up), with the paper's Taobao/Tmall reconstructions using roughly 5–7-day pre-promotion phases. |
| 6 | Prediction or incrementality | Primarily prediction — the model's final output p^delay_cvr is a probability prediction of delayed conversion, not an estimate of the incremental effect of an exposure. However, the counterfactual causal regularizer (L_CM) internally uses a Doubly Robust estimator to compute the causal effect of the user's own add-to-cart action on delayed conversion, and uses that causal estimate only to correct confounding-driven label bias in the training signal — i.e., the causal machinery is used to de-bias a prediction target, not to make the model's output itself a treatment-effect estimate of an exposure decision. |
| 7 | Model architecture | Multi-task tower stack: frozen pretrained "Ori CVR/ATC Predictor" (stop-gradient) + a new "Delay CVR Predictor" tower whose input is the frozen tower's last hidden layer plus price/discount features and pooled real-time ATC/purchase behavior-sequence embeddings, gated by personalized MLP gating networks (Eqs. 6–8) at each layer. Final all-conversion probability is the stop-gradient sum of the frozen tower's output and the Delay tower's output (Eq. 2). Trained with a joint loss: delayed-conversion BCE + λ·all-conversion BCE + λ_c·counterfactual causal-regularization MSE term (Eq. 11), the latter based on a Doubly Robust estimator (Eq. 9) combining outcome regression and IPW correction using a pretrained ATC propensity model. |
| 8 | Credit assignment | Not specified in source beyond single click → single promotion-day conversion outcome; no multi-item slate or ranked-list credit assignment is addressed. |
| 9 | Training data and counterfactual handling | Taobao and Tmall public click/cart/purchase logs (author-constructed pre-promotion/promotion splits, 80/20 historical/held-out promotion cycles) plus a proprietary Alibaba industrial ads dataset. Counterfactual handling is explicit: a Doubly Robust estimator (outcome regression + inverse-propensity weighting via a pretrained ATC propensity model) estimates the individual causal effect of add-to-cart on delayed conversion, used as a regularization target — this is a genuine causal-inference component, unlike most of this batch. |
| 10 | Offline and online evaluation | Offline: AUC_all, AUC_delay, NLL_delay on Taobao, Tmall, and the industrial dataset, averaged over five runs with significance testing (p<0.05), against Delay-conversion, ES-DFM, DEFER, DEFUSE, and "reuse"/HDR baselines, plus an ablation study on the industrial dataset. Online: a live A/B test during Double 11 and Double 12 (two of the platform's largest annual promotions), 20% traffic per arm, six days total. |
| 11 | Reported gains | Offline — industrial dataset: AUC_all 0.8570* / AUC_delay 0.8801* / NLL_delay 0.0238* for CM-DCM vs. best baseline HDR at 0.8182 / 0.8287 / 0.0270 (* = p<0.05 vs. best baseline). Online — industrial ads platform, Double 11/12 A/B test: +7.87% revenue, +4.24% delayed GMV, +1.42% overall GMV, +2ms P99 latency. |
| 12 | Applicability to a two-sided dating recommender | The point-mass, event-driven delay structure (conversion concentrated on one future date rather than decaying continuously) does not match the project's retention/revenue labels, which resolve over a continuous 7–30-day window with no analogous fixed "promotion day." The Doubly-Robust causal regularizer for correcting confounded intermediate-action bias, however, is a directly transferable technique for de-biasing a match→subscription intermediate signal the way this paper de-biases add-to-cart→conversion. |
| 13 | Unverified claims | The paper asserts the ATC action "likely causally influences—not merely correlates with—delayed conversion" as a motivating premise for the whole causal-regularization design, but this causal premise itself is stated as an assumption/intuition rather than independently validated (e.g., no randomized or quasi-experimental evidence for the ATC→conversion causal link is presented beyond the DR estimator's own internal assumptions) — flagged as an asserted-but-not-independently-verified causal claim. |

## Project Relevance

Speaks most directly to **Q3** (label/horizon definition: a fixed-date rather than continuous-delay censoring scheme, evidence that "delayed feedback" need not always mean an open-ended elapsed-time window) and **Q5** (where causal/incremental effects sit inside a ranking-adjacent model — here as a Doubly-Robust regularizer correcting confounded label bias, not as the training objective itself). Also relevant to Q4 (combining a short-term pretrained tower with a residual long-term-delay head via personalized gating, a fixed-fusion-plus-adaptive-gate pattern). Does not address Q1, Q2, Q6, Q7, or Q8.

**Moderate project relevance with an important structural mismatch.** The event-concentrated delay distribution (single promotion day) is a poor structural match for the project's smoothly-distributed 7–30-day retention window, so the label-definition mechanics do not transfer directly. But the counterfactual causal regularizer is the most causally-sophisticated technique in this D7 batch and offers a concrete pattern — using a DR estimator to de-bias an intermediate behavioral signal (add-to-cart here, match-to-activity in the project) before it feeds a delayed-outcome prediction — worth flagging for Q5.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `CM-DCM`._

## Meta Information

- **Authors:** Xin Song, Kaiyuan Li, Jinxin Hu
- **Affiliations:** Alibaba Group
- **Venue:** SIGIR
- **Year:** 2026
- **Relevance:** Related
- **Priority:** 4
- nlm:5ea68e79
