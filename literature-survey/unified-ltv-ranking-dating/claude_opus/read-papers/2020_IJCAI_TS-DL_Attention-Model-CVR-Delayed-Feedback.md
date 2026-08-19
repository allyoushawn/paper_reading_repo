# Paper Analysis: An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2020 (JD) (IJCAI) [TS-DL] An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Title/authors/venue: "An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration," Yumin Su, Liang Zhang, Quanyu Dai, Bo Zhang, Jinyao Yan, Dan Wang, Yongjun Bao, Sulong Xu, Yang He, Weipeng Yan (JD.com / The Hong Kong Polytechnic University / Communication University of China). IJCAI 2020.

Key contribution: A two-stage deep learning framework (TS-DL) for CVR prediction that jointly tackles data sparsity (scarce positive conversion samples relative to click data) and delayed feedback. Stage 1 extracts a pretrained dense item embedding (via "Telepath," a pretrained image-based item representation, Wang et al. 2017) from impressions/clicks to substitute for sparse item-ID features. Stage 2 has two components trained jointly via a novel EM algorithm: (a) a conversion model using inner-attention + self-attention over the user's GRU-encoded sequential click history to predict conversion probability, and (b) a time delay model that uses survival analysis — with a dynamic, learned hazard function calibrated on abundant post-click behavioral data (not assumed static/parametric) — to estimate the conversion-delay distribution and calibrate the conversion label. The delay model differs from prior static time-delay models (e.g., Chapelle 2014's exponential model) in that the hazard function is dynamic, updated by post-click sequential information (a two-level GRU over "day slots" of post-click item interactions) rather than fixed at click time.

Datasets and baselines: Evaluated on three JD e-commerce datasets (WP1, WP2 — two WeChat ad placements; JD-MP — JD mobile page), each with roughly 25K-415K training samples and 11K-68K test samples, using 1 week of training data and 1 day of test data. Baselines: DFM (Chapelle 2014), DIN (Zhou et al. 2018), Wide&Deep, GRU+Att, and ablations TS-DL/I, TS-DL/D, TS-DL/S (removing the image embedding, delay model, or self-attention respectively).

Main results: TS-DL improves AUC over the DIN benchmark by 5.24% (WP1), 44.76% (WP2), and 8.02% (JD-MP) relative AUC (RelaImpr metric). Ablations show the delay-model component and self-attention are each important — removing either causes a measurable AUC drop. Time-delay analysis: TS-DL achieves the lowest Jensen-Shannon divergence between predicted and true delay distributions across all three datasets (e.g., a 23.9%/29.8% relative reduction over DFM on JD-MP test/train data), and rCVR/ΔrCVR calibration analysis shows TS-DL predicts closer-to-true average CVR and better separates positive from negative samples than DFM.

## 2. Experiment Critique

The offline evaluation spans three proprietary e-commerce datasets from a single company (JD), each with one week of training data and one day of test data — no public benchmark is used, limiting external reproducibility. The paper reports point-estimate AUC/RelaImpr/JSD numbers without confidence intervals, standard deviations, or significance tests across runs. Comparisons are internally consistent (the same first-stage image embedding is fed to all baselines), which strengthens the fairness of the ablation study, but no online/production A/B test is reported — the evaluation is entirely offline. The "post-click calibration" claim rests on comparing predicted vs. actual delay distributions (Jensen-Shannon divergence) rather than on any causal or production validation.

## 3. Industry Contribution

Deployability: the paper explicitly frames its choice of a pretrained image embedding as a way to sidestep sparse item-ID cold-start/sparsity issues in e-commerce CVR prediction, a direct engineering concern. The two-level GRU + EM training procedure is more complex to productionize than a single end-to-end model, and the paper's own complexity analysis (Section 3.3, big-O in embedding dimension, sequence length, and post-click day-slot count N) signals this is compute-heavier than a standard wide&deep or DIN pipeline — the time-delay model in particular requires collecting and processing post-click behavioral sequences per candidate item, which adds real-time feature-engineering and serving cost. At inference, only the conversion model (Eq. 9) is used; the time-delay/survival model is training-time-only, which limits the added serving latency to that of the conversion model's attention+GRU forward pass.

## 4. Novelty vs. Prior Work

Positioned against Chapelle 2014's DFM (static exponential delay assumption, no post-click information), Ji et al. 2017 (Weibull delay distribution), and Yoshikawa & Imai 2018 (non-parametric delay model, still static/fixed at click time). The paper's stated novelty is that all prior delay models are "static" — the delay distribution is fixed once the click happens — whereas TS-DL's hazard function is dynamic, updated using post-click behavior (e.g., a user browsing related items after adding to cart reveals a strengthening purchase intent). ESMM (Xiao et al. 2018) is cited as related work on entire-space multi-task modeling for CVR but is not benchmarked directly.

## 5. Dataset Availability

| Dataset | Type | Size | Availability |
|---|---|---|---|
| WP1 (WeChat ad placement 1, JD) | Proprietary | 247,627 train / 33,703 test | Not available — proprietary |
| WP2 (WeChat ad placement 2, JD) | Proprietary | 73,952 train / 11,202 test | Not available — proprietary |
| JD-MP (JD mobile page) | Proprietary | 415,270 train / 68,415 test | Not available — proprietary |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "An Attention-based Model for Conversion Rate Prediction with Delayed Feedback via Post-click Calibration," Su, Zhang, Dai, Zhang, Yan, Wang, Bao, Xu, He, Yan; JD.com; IJCAI 2020; https://doi.org/10.24963/ijcai.2020/487 |
| 2 | Source type | Industry paper (JD.com), peer-reviewed at an academic venue (IJCAI) |
| 3 | Direction | D7 |
| 4 | Problem setting | E-commerce ad CVR prediction with two compounding challenges: (1) extreme positive-class sparsity relative to CTR data, and (2) conversion delay ranging from seconds to weeks after a click, which creates false-negative labels if the model is trained too soon after the click. |
| 5 | Objective and label definition | Binary conversion label Pr(C=1\|X,H) (whether the candidate item is eventually converted, given item features X and click history H). Horizon/delay handling: a survival-analysis-based dynamic hazard function h(D=d\|X,H,S_E) estimates the time-delay distribution using post-click behavioral data S_E observed up to elapsed time e; delay is discretized into day slots up to N = max observed elapsed days across examples. When the true label is not yet resolved (Y=0, elapsed time e < true delay d), the model does not discard the sample or hard-label it negative — an EM algorithm treats the eventual-conversion indicator C as a latent variable, computing its expectation w_i from the current hazard/conversion model estimate (E-step) and using that soft expectation as the training target (M-step). |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. It predicts a calibrated conversion probability and a calibrated delay distribution; it does not estimate the causal effect of showing an ad or item. |
| 7 | Model architecture | Two-stage framework: Stage 1 — pretrained "Telepath" image-based item embedding (50-dim) substitutes for sparse item-ID features. Stage 2 — (a) conversion model: one-layer GRU over sequential click history, self-attention over the GRU hidden states to capture global conversion interest patterns across sub-sequences, inner-attention to align the candidate-item representation against the weighted history representation, followed by fully connected layers to output Pr(C=1\|X,H); (b) time delay model: a two-level GRU (day-slot level, then across-day-slot level) over post-click item sequences, combined with the conversion model's hidden state via a fully connected layer to output a dynamic hazard rate h(D=e\|X,H,S_E) at each elapsed-time step, used with a survival function to derive a delay-probability distribution. Both sub-models are trained jointly via a custom EM algorithm that treats the unresolved conversion indicator as a latent variable. |
| 8 | Credit assignment | Operates at the single candidate-item level (one click on one candidate ad/product maps to one conversion label); does not address multi-item slates or cross-item credit assignment. Within a single item's outcome, credit is distributed across time via the survival/hazard model rather than across items. |
| 9 | Training data and counterfactual handling | Trained on 1 week of JD click/conversion logs per dataset, using post-click behavioral sequences as auxiliary "post-click calibration" information for the delay model. No explicit counterfactual/causal adjustment; "counterfactual handling" here means the EM-based soft-labeling of currently-unresolved (Y=0) samples via their estimated latent conversion probability, rather than a causal-inference technique. |
| 10 | Offline and online evaluation | Offline only: AUC and RelaImpr (relative AUC improvement vs. DIN) for conversion prediction; rCVR (ratio of predicted to true average CVR) and ΔrCVR (positive-vs-negative-sample separation) for calibration quality; Jensen-Shannon divergence between predicted and true delay distributions for the time-delay model. No online/production A/B test reported. |
| 11 | Reported gains | AUC RelaImpr over DIN, JD e-commerce datasets (Table 2): +8.02% on JD-MP, +5.24% on WP1, +44.76% on WP2. Jensen-Shannon divergence reduction vs. the DFM baseline on JD-MP (Table 4): 23.9% (test) / 29.8% (train). |
| 12 | Applicability to a two-sided dating recommender | The dynamic, post-interaction-conditioned hazard function is conceptually relevant to the project's idea of updating a retention/conversion estimate as more post-impression behavior (e.g., subsequent likes, messages) accumulates rather than freezing the estimate at exposure time. However, it is single-sided e-commerce CVR (buyer-item), with no reciprocity or congestion modeling, and its delay horizon (seconds to weeks, tuned to e-commerce cart/purchase behavior) is not validated at the 7-30 day retention scale the project needs. |
| 13 | Unverified claims | The claim that TS-DL "has the most accurate average CVR prediction in all datasets" (Section 4.3) rests on the paper's own rCVR metric computed on its own three proprietary datasets, with no external validation. The choice of L=10 most recent clicked items and the pretrained Telepath embedding's transferability outside JD's product-image e-commerce setting are asserted but not tested. |

## Project Relevance

Speaks to **Q3** (delay/censoring handling — the EM-based soft-labeling of unresolved samples, and the dynamic survival-based hazard function, are a more sophisticated censoring treatment than the static exponential model used as this paper's own baseline) and loosely to **Q4**, via its use of auxiliary post-click sequence information to recalibrate a conversion estimate over time — a pattern that echoes how the project might update a retention estimate as post-impression signal (likes, messages) accumulates. **Low relevance to Q1, Q2, Q5, Q6 (online), Q7, Q8** — the paper's label is a single binary e-commerce conversion, not retention or revenue; there is no online evaluation; no two-sided/reciprocal structure; and it does not address incrementality. The delay horizon (seconds to weeks, e-commerce cart-to-purchase) is shorter than and structurally different from the project's 7-30 day retention window.

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|---|---|---|
| [2021_arXiv_NA_Many-Conversions-Per-Click-Delayed-Feedback.md](./2021_arXiv_NA_Many-Conversions-Per-Click-Delayed-Feedback.md) | Related Work / Experiments | Names this paper's method (`TS-DL`) |

_1 in-corpus paper(s) name this method. Generated in Phase 3.7 by exact word-boundary matching on the method token `TS-DL` across all 133 cards._

## Meta Information

- **Authors:** Yumin Su, Liang Zhang, Quanyu Dai, Bo Zhang, Jinyao Yan, Dan Wang, Yongjun Bao, Sulong Xu, Yang He, Weipeng Yan
- **Affiliations:** JD.com; The Hong Kong Polytechnic University; Communication University of China
- **Venue:** IJCAI 2020 (29th International Joint Conference on Artificial Intelligence)
- **Year:** 2020
- **Relevance:** Related
- **Priority:** 2
- **nlm:1ae7b034**
