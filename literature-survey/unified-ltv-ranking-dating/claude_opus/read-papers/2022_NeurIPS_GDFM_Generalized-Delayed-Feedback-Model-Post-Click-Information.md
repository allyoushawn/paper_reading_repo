# Paper Analysis: Generalized Delayed Feedback Model with Post-Click Information in Recommender Systems

**Source:** /Users/fox/Projects/paper_reading_repo/literature-survey/unified-ltv-ranking-dating/claude_opus/pdfs/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf
**Date analyzed:** 2026-08-17

## 1. Summary

**Title:** Generalized Delayed Feedback Model with Post-Click Information in Recommender Systems
**Authors:** Jia-Qi Yang, De-Chuan Zhan (State Key Laboratory for Novel Software Technology, Nanjing University)
**Venue/Year:** NeurIPS 2022

GDFM generalizes Chapelle's Delayed Feedback Model by treating both post-click user behaviors (e.g., add-to-cart, favorite) and early conversions as a single "stochastic post-click information" family, each action a_j paired with its own revealing time δ_j. The model factorizes p^t(x,y,a,δ) = p^t(y|x)·p(a|x,y,δ)·p(δ)·p^t(x), assuming the post-action distribution p(a|x,y,δ) is stable while the target CVR distribution p^t(y|x) shifts with time t — this stability assumption lets post-click actions serve as an early, informative proxy for the eventual (delayed) conversion label. An action prediction model q_φ(a|x,y,δ) is trained to approximate p(a|x,y,δ); a "proxy feedback loss" then lets each post-click action update the CVR model q_θ(y|x) at its revealing time δ_j, long before the conversion label itself (revealed at δ_y) arrives. Because not every action is equally informative or equally fresh, GDFM reweights each proxy-loss term by an information weight w_info = e^(−αH(y|a_j)) (conditional entropy of y given the action — lower entropy means the action is more informative) and a temporal weight w_time = e^(−βδ_j) (penalizing actions revealed further in the past, i.e., a larger elapsed-time/distribution-shift gap). A KL regularizer against the standard delayed-negative-labeled model stabilizes training and prevents uninformative actions from degrading performance. On Criteo (60-day display-advertising conversion logs) and Taobao (9-day user-behavior logs with page-view/cart/favorite/buy actions), under a streaming hour-by-hour evaluation protocol, GDFM outperforms FNW, ES-DFM, and MM-DFM baselines on AUC, PR-AUC, and NLL, closing 74.9%/79.4% of the Pretrain-to-Oracle AUC gap on Criteo/Taobao respectively, ahead of the strongest AUC baseline on each dataset, ES-DFM, at 71.4%/62.6%.

## 2. Experiment Critique / 3. Industry Contribution / 4. Novelty vs. Prior Work / 5. Dataset Availability

Condensed per the Priority-4 depth rule — see the Reference Card (Section 7) and Project Relevance below for the substantive extraction. Datasets: Criteo Conversion Logs (public, https://labs.criteo.com/2013/12/conversion-logs-dataset/) and Taobao User Behavior (public, Tianchi dataDetail?dataId=649). Baselines compared: Pretrain, Vanilla, Oracle, FNW (Ktena et al. 2019), ES-DFM (Gu et al. 2021), MM-DFM (Hou et al. 2021). Code released at github.com/ThyrixYang/gdfm_nips22. Novelty is the unification of post-click behaviors and conversion labels as one "stochastic post-click information" family under a single generalized formulation, plus the conditional-entropy/temporal-decay reweighting scheme and the delayed-regularizer safety net — a genuine extension of the DFM lineage (DFM → FNW/ES-DFM/MM-DFM → GDFM) rather than a different paradigm.

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Generalized Delayed Feedback Model with Post-Click Information in Recommender Systems," Jia-Qi Yang, De-Chuan Zhan; Nanjing University; NeurIPS 2022 (36th Conference on Neural Information Processing Systems); no public URL captured from the PDF header, code at https://github.com/ThyrixYang/gdfm_nips22 |
| 2 | Source type | Academic |
| 3 | Direction | D7 |
| 4 | Problem setting | CVR prediction under delayed feedback in recommender systems / display advertising, where the true conversion label arrives after a long delay, and the paper additionally exploits post-click user behaviors (add-to-cart, favorite) as informative early signals to reduce the effective delay. |
| 5 | Objective and label definition | Binary CVR label y (1 if converted, 0 otherwise), revealed after a delay δ_y — a sample not yet converted after a "long enough waiting time, e.g., 30 days" (citing Chapelle 2014) is labeled negative (the standard hard-threshold DFM convention). Post-click actions a_j each have their own, typically much shorter, revealing time δ_j (paper gives examples of 10 minutes, 30 minutes, 1 hour for cart events). Horizon: the paper does not restate an explicit attribution window for its own experiments beyond citing the 30-day convention; Figure 4 sweeps revealing time δ_j from ~0.1 to ~1000 hours (roughly minutes to ~6 weeks) and finds the combined information weight peaks around the 7th day. |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. GDFM re-weights and corrects a proxy training signal to reduce label bias/staleness in a CVR probability prediction; it does not estimate the causal effect of an exposure. |
| 7 | Model architecture | Two coupled models: (a) an action prediction model q_φ(a|x,y,δ) (an MLP with m heads, one per action, each gated by a revealing-time mask) estimating p(a|x,y,δ); (b) the CVR prediction model q_θ(y|x) (an MLP over a shared feature encoder). Trained with a streaming procedure (Algorithm 1) combining a standard delayed cross-entropy loss (Eq. 3) with a re-weighted "proxy feedback loss" (Eq. 4, using q_φ to marginalize over y) and a KL regularizer (Eq. 9) that anchors updates to the ground-truth-labeled model. Weights combine an information term w_info = e^(−αH(y\|a_j)) and a temporal term w_time = e^(−βδ_j). |
| 8 | Credit assignment | Not specified in source. Operates at single impression/click → single conversion-label granularity; no multi-item slate or ranked-list credit assignment is addressed. |
| 9 | Training data and counterfactual handling | Criteo Conversion Logs (60 days, ~16M samples) and Taobao User Behavior (9 days, >70M samples, 1M users; behaviors: page-view, buy, cart, favorite). No counterfactual/causal handling — this is delayed-label bias correction via an auxiliary proxy signal and regularization, not treatment-effect estimation. |
| 10 | Offline and online evaluation | Offline only, via a streaming hour-by-hour evaluation protocol (models pretrained on an initial window, then evaluated and updated hour by hour on a streaming split), reporting AUC, PR-AUC, and NLL. No online A/B test is reported. |
| 11 | Reported gains | On the Pretrain(0%)→Oracle(100%) relative-improvement scale (Table 1): Criteo — GDFM RI-AUC 74.9±0.7%, RI-PRAUC 68.1±1.6%, RI-NLL 72.4±0.6%, vs. the strongest baseline on each metric, ES-DFM, at RI-AUC 71.4±0.5%, RI-PRAUC 63.3±1.1%, RI-NLL 66.2±1.2%. Taobao — GDFM RI-AUC 79.4±0.5%, RI-PRAUC 80.7±0.9%, RI-NLL 49.6±3.1%, vs. the strongest baseline per metric: ES-DFM at RI-AUC 62.6±0.7%, and MM-DFM at RI-PRAUC 62.1±2.6% / RI-NLL −14.9±10.5%. |
| 12 | Applicability to a two-sided dating recommender | The proxy-feedback mechanism (using an intermediate, faster-revealing signal to update a model before the true delayed label arrives) is directly analogous to using match→subscription activity as an early signal for retention/revenue prediction. But GDFM's own post-click revealing times are minutes-to-weeks (peaking at ~7 days) against a 30-day conversion horizon — an order of magnitude shorter than the project's 7–30 day retention / weeks-long revenue horizon, and the method is untested at that scale or in a two-sided setting. |
| 13 | Unverified claims | The paper states its method "can be applied to multi-class case[s] without modification," a generalization claim made in passing (Background section) but never tested experimentally in the paper — flagged as an unverified extension claim. |

## Project Relevance

Speaks most directly to **Q3** (label/horizon/delay handling: standard 30-day hard-threshold negative labeling, unchanged from the DFM lineage) and offers a transferable methodological idea for **Q4** (combining a short-term/intermediate signal with a long-term label) via its proxy-feedback-loss mechanism — the closest analogue in this batch to the project's match→subscription intermediate-activity signal, since it is explicitly designed to inject a faster-revealing signal into training before the delayed ground truth arrives. Does not address Q1, Q2, Q5, Q6, Q7, or Q8.

**Low project relevance regarding horizon and market structure.** The paper's informative revealing times top out around 7 days against a 30-day conversion label, one to two orders of magnitude short of the project's weeks-long revenue horizon, and the setting is single-sided e-commerce/advertising with no reciprocity, congestion, or two-sided fairness treatment. Its transferable contribution is the mechanism (weighted proxy-signal injection with an entropy-based informativeness measure and a KL safety-net regularizer), not its specific numbers or dataset.

## Papers That Mention This Paper (Reverse Citation Map)

_No other card in this corpus names the method token `GDFM`._

## Meta Information

- **Authors:** Jia-Qi Yang, De-Chuan Zhan
- **Affiliations:** State Key Laboratory for Novel Software Technology, Nanjing University
- **Venue:** NeurIPS
- **Year:** 2022
- **Relevance:** Related
- **Priority:** 4
- nlm:3e6b9c81
