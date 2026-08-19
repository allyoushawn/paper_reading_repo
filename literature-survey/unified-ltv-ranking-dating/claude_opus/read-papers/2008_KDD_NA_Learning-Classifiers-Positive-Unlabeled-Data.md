# Paper Analysis: Learning Classifiers from Only Positive and Unlabeled Data

**Source:** `/Users/fox/Projects/Awesome-Deep-Learning-Papers-for-Search-Recommendation-Advertising/04_Ranking/Delayed-Feedback-Problem/2008 (KDD) Learning Classifiers from Only Positive and Unlabeled Data.pdf`
**Date analyzed:** 2026-08-17

## 1. Summary

Charles Elkan and Keith Noto (UC San Diego) address learning a standard binary classifier when the training data contains only positive examples (label y=1) and unlabeled examples (which may be either true positives or true negatives), rather than fully labeled positive-and-negative data — the "positive and unlabeled" (PU) learning problem. Under the "selected completely at random" (SCAR) assumption — that the labeled positive examples are a uniformly random sample of all true positives, i.e., p(s=1|x,y=1)=p(s=1|y=1)=c is constant and independent of x — the paper's central theoretical result (Lemma 1) proves that a nontraditional classifier g(x) trained to distinguish labeled (s=1) from unlabeled (s=0) examples predicts probabilities that differ from the true conditional probability of being positive, f(x)=p(y=1|x), by only the constant factor c: p(y=1|x)=p(s=1|x)/c. Two consequences are derived: (i) g can be rescaled by an estimate of c (obtained from a small held-out validation set of positive examples) to recover a properly calibrated classifier for p(y=1|x) directly, or used unscaled for ranking, since f is a monotone increasing function of g; and (ii) the same result yields a principled per-example weighting scheme for treating unlabeled examples as a mixture of a weighted positive and a weighted negative copy (weight p(y=1|x,s=0) and its complement), letting any standard classifier (e.g., an SVM) be trained on PU data without heuristically guessing which unlabeled examples are "really" negative. The methods are applied to a real molecular-biology classification task — identifying which of ~4906 unlabeled SwissProt protein records (a case-control-style dataset; domain knowledge suggests ~10% are true positives) belong in the TCDB transporter-protein database, given 2453 confirmed positive TCDB records — and, evaluated via 10-fold cross-validation, both of the paper's new methods substantially outperform (by F1, AUC, and recall-at-fixed-false-positive-rate) the prior state-of-the-art "biased SVM" method (Liu et al. 2003) while running roughly 300-600× faster, since the new methods compute the correct weighting factor directly (via the estimated constant c) rather than requiring an expensive validation-set search over SVM penalty hyperparameters.

## 2. Experiment Critique

Design and validity are solid within scope (10-fold cross-validation, four methods compared on identical folds, combined confusion matrices, four accuracy metrics including a fixed-false-positive-rate recall comparison chosen for its relevance to a human-expert use case) — not expanded further at this batch's Related/Priority-3 depth allocation.

## 3. Industry Contribution

Not an industry-deployment paper — a foundational academic/theoretical contribution (bioinformatics application only) with no discussion of production serving, latency, or engineering cost; not expanded further at Related depth.

## 4. Novelty vs. Prior Work

The paper's own framing: prior PU-learning approaches either (a) heuristically identify likely-negative examples within the unlabeled set before training a standard classifier, or (b) assign a single uniform weight to all unlabeled examples (e.g., the biased-SVM method of Liu et al. 2003, then state-of-the-art). This paper's contribution is a principled, per-example weighting derived directly from Lemma 1, requiring no expensive hyperparameter search. Not expanded further at Related depth.

## 5. Dataset Availability

| Dataset | Type | Size | Availability |
|---|---|---|---|
| Synthetic 2-D Gaussian illustration | Synthetic | 500 positive / 1000 negative points | Not public (fully specified generative procedure in paper) |
| SwissProt / TCDB protein records | Real, domain-specific (molecular biology) | P=2453 positive (TCDB); U=4906 unlabeled (SwissProt minus TCDB); ~10% of U estimated true positive | Stated in the paper as available at time of publication via www.cs.ucsd.edu/users/elkan/posonly (not verified live in this direct-PDF read) |

## 6. Community Reaction

Not assessed in direct-PDF mode.

## 7. Reference Card

| # | Field | Content |
|---|---|---|
| 1 | Title, authors/company, venue, year, URL | "Learning Classifiers from Only Positive and Unlabeled Data," Charles Elkan and Keith Noto; University of California, San Diego; KDD '08 (14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining), Las Vegas, NV; 2008; https://doi.org/10.1145/1401890.1401920 |
| 2 | Source type | Academic |
| 3 | Direction | D7 |
| 4 | Problem setting | Learning a standard binary classifier when training data provides only a set of confirmed positive examples and a separate set of unlabeled examples (a mixture of true positives and true negatives), with no confirmed-negative examples available at all — the foundational positive-unlabeled (PU) learning setting. |
| 5 | Objective and label definition | Binary classification target y∈{0,1}; observed label s∈{0,1} indicates only whether an example is "labeled" (s=1 ⟹ y=1 with certainty) or "unlabeled" (s=0, true y unknown/could be either). Under the SCAR assumption, p(s=1｜x,y=1)=c is constant. No explicit time horizon or delay mechanism — the framework is purely about which examples happen to be labeled, not about *when* a label becomes available, so it does not itself model a delay process (contrast with the survey's delayed-feedback papers, where the "unlabeled" status resolves over time). |
| 6 | Prediction or incrementality | Prediction only — the paper does not address incrementality. The entire contribution is a method for recovering a correctly calibrated prediction of p(y=1｜x) (or a valid ranking function) from PU data; no causal or exposure-effect estimation is discussed. |
| 7 | Model architecture | Not architecture-specific — the theoretical result (Lemma 1) applies to any probabilistic classifier trained to distinguish labeled vs. unlabeled examples; empirically demonstrated with logistic regression (Section 4 illustration) and soft-margin SVMs with a linear kernel plus Platt scaling for probability calibration (Section 5, real-data experiment, using libSVM). |
| 8 | Credit assignment | Not applicable — this is a single flat binary-classification setting over individual examples (protein records), with no cascade, slate, or multi-item structure; each example's label status is independent of any other example's. |
| 9 | Training data and counterfactual handling | Two disjoint sets drawn from the same underlying distribution: P (labeled positives) and U (unlabeled, of unknown class mixture). No counterfactual estimation; the paper's "weighting" is a bias-correction for the *sampling* of which positives get labeled (assumed SCAR), not a correction for an intervention or exposure. |
| 10 | Offline and online evaluation | Offline only — 10-fold cross-validation on the SwissProt/TCDB protein dataset, reporting accuracy, F1 score, area under the ROC curve, and recall at a fixed false-positive-rate operating point (100 false positives, chosen to reflect what "a human expert will tolerate"). No online or production evaluation — this is a pre-deployment academic study. |
| 11 | Reported gains | On the SwissProt/TCDB dataset (Table 1): the paper's two new methods — (ii) "P versus U" (rescaled) and (iii) "P versus weighted U" — achieve AUC 0.9895 and 0.9899 respectively, F1 0.9308 and 0.9422, versus the prior state-of-the-art biased SVM (iv) at AUC 0.9895 and F1 0.9279 — comparable AUC but higher F1 and accuracy, achieved at roughly 300-600× lower computational cost (relative training time 1-2 for the new methods vs. 621 for biased SVM). At a fixed operating point of 100 tolerated false positives (Fig. 2), the reweighting method (iii) misses 7.6% of true positives versus 9.6% for biased SVM — a stated 21% relative reduction in error at that operating point. |
| 12 | Applicability to a two-sided dating recommender | Not applicable to ranking, reciprocity, or two-sided-market structure at all — this is a foundational statistical-learning result, not a recommender-system paper. Its relevance is purely conceptual: the SCAR-based reweighting logic is the mathematical ancestor of the importance-sampling/reweighting techniques used by this survey's delayed-feedback papers (including Paper 1 of this batch, CBDF), which apply an analogous correction to labels whose "unlabeled" status arises from *not-yet-resolved* delay rather than a one-time random labeling process. |
| 13 | Unverified claims | The paper's own central assumption (SCAR — that labeled positives are selected completely at random from all true positives) is explicitly flagged by the authors as a strong assumption that "results depend on"; they note it does not hold in the case-control scenario (where P and U are sampled independently), only in the "single-training-set" scenario, and the real-data SwissProt/TCDB experiment is technically a case-control-style dataset that the paper treats as if single-training-set for the sake of applying the method — an approximation the authors acknowledge but do not fully resolve. |

## Project Relevance

**Low project relevance** for direct application — this is a foundational statistical-learning paper with no ranking, recommender, delay, or two-sided-market structure, and does not speak to any of the eight research questions on its own terms. Its value to the survey is as the theoretical ancestor of **Q3** (label/horizon definitions, delay and censoring handling): the project's core delayed-label problem — "not yet converted/retained" and "will never convert/retain" are indistinguishable at training time — is structurally the same missing-label problem PU learning formalizes (an unlabeled example may be a true positive whose positive status simply hasn't been observed, or a true negative). The paper's SCAR assumption is, however, a poor fit for the project's actual delayed-feedback setting: SCAR requires that the probability an eventual-positive example is already labeled at training time be *constant across all examples*, whereas in a 7-30 day retention window that probability is highly *contextual* — it depends on how long ago the impression occurred and on context-dependent behavior (exactly the covariate-dependent hazard function Paper 1 of this batch, CBDF, estimates instead of assuming a constant c). This paper is best read as establishing why naive PU-style reweighting is theoretically motivated for missing-label problems in general, while Paper 1 (and the delayed-feedback literature it belongs to) shows the more realistic, covariate-dependent correction the project would actually need.

## Papers That Mention This Paper (Reverse Citation Map)

_This paper proposes no distinctively-named method, so no automated reverse-citation match was possible._

## Meta Information

- **Authors:** Charles Elkan, Keith Noto
- **Affiliations:** Computer Science and Engineering, University of California, San Diego
- **Venue:** KDD '08 (14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining)
- **Year:** 2008
- **Relevance:** Related
- **Priority:** 3
- **nlm:366c024f**
