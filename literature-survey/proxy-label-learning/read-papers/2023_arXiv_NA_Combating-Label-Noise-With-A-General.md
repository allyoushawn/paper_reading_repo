Date: 2026-04-12
Source: https://arxiv.org/pdf/2310.10463
NLM Source ID: b98116fd-ce0c-4390-bae5-5e7d6ef68246
Venue: arXiv 2023
Relevance: Core
Priority: 2

# Combating Label Noise With A General Surrogate Model For Sample Selection (2023)

**Authors:** Not specified in source.
**Affiliation:** Not specified in source.

## Contribution, method, and experimental setup (NLM Q1)

**(1) Core problem and key contribution**

*   **Core Problem:** When learning with noisy labels, a common sample selection strategy is to use the "small-loss criterion," which assumes that deep neural networks fit clean and simple samples before noisy ones [1, 2]. However, this learning-centric approach suffers from confirmation bias: networks inevitably **memorize noisy samples that share frequently occurring corrupted visual patterns**, falsely identifying them as clean in-distribution data because they have small losses [1-3]. 
*   **Key Contribution:** The authors propose a novel, **training-free sample selection method using CLIP** as an open-vocabulary vision-language surrogate model [1, 4]. Because CLIP evaluates samples based on zero-shot text-image alignment rather than the network's training dynamics, it bypasses the memorization effect and filters out corrupted patterns effectively [3, 5]. Additionally, to counteract the selection bias introduced by CLIP (such as overconfidence in certain classes and class imbalance), the authors introduce a **noise-aware balanced margin adaptive loss (LNABM)** to robustly optimize the classifier [1, 4].

**(2) Proposed method or architecture in detail**

The proposed framework utilizes a pretrained feature encoder and re-trains a classifier using a clean subset of data filtered by a frozen CLIP model, optimized by the LNABM loss [6].

*   **Sample Selection via CLIP:** A frozen CLIP model acts as a zero-shot scorer during training [6]. An image is passed through the image encoder alongside a text prompt (e.g., "a photo of a {CLASS}") passed through the text encoder [7]. The authors propose two criteria to build the clean dataset:
    *   *Prediction Confidence:* The instance is selected as clean if CLIP's prediction probability for the original noisy label is greater than a predefined threshold $\rho$ [7, 8].
    *   *Prompt Consistency:* To inject domain knowledge and filter out ambiguous, out-of-domain data (e.g., distinguishing a "stingray" car from the animal), two differently contextualized prompts are used [8, 9]. The Jensen-Shannon (JS) divergence between the two predictions is calculated, and samples with a JS divergence below a threshold $\mu$ are kept [9].
*   **Noise-Aware Balanced Margin Adaptive Loss (LNABM):** Because CLIP can be biased and its filtering naturally causes a long-tailed (imbalanced) class distribution, the authors modify the network's output logits by integrating two priors [10, 11]:
    *   *Transition Matrix ($M$):* Estimated by averaging CLIP's predictions across all training samples, acting as a margin penalty to suppress the model's overconfidence on biased classes [12, 13].
    *   *Class Frequency Prior ($\pi$):* Calculated from the distribution of the selected clean dataset, serving as a balanced margin to counteract class imbalance [11, 13].
*   **Focal Loss Integration:** The authors observed that standard cross-entropy loss performs poorly on the selected clean subset because it treats all samples equally, causing the network to be overwhelmed by "easy" samples at the center of a class [14]. Instead, the margin-adjusted logits are optimized using **Focal Loss**, which assigns larger weights to the fewer "hard" samples located near the decision boundaries [15, 16].

**(3) Datasets used for evaluation and comparison baselines**

*   **Datasets Used:**
    *   *Real-World Noisy Datasets:* Evaluated on **Clothing1M**, **WebVision 1.0** (with subsequent transfer testing on ImageNet ILSVRC12), **Red Mini-ImageNet** (with controlled real-world noise up to 80%), **CIFAR-10N**, and **CIFAR-100N** [17-19].
    *   *Synthetic Noisy Datasets:* Evaluated on **CIFAR-10** and **CIFAR-100**, which were manually corrupted with symmetric, asymmetric, and instance-dependent label noise at extreme rates up to 90% [18, 20, 21].
*   **Comparison Baselines:** The method was benchmarked against standard Cross-Entropy (CE) and a wide array of state-of-the-art Label Noise Learning (LNL) baselines [22, 23]. Prominent baselines explicitly compared against include:
    *   **DivideMix** and **Sel-CL** (which the authors use as primary initializations/baselines to build upon and improve) [19, 23-25].
    *   State-of-the-art robust learning and selection baselines like **InstanceGM**, **LSL**, **Co-teaching / Co-teaching+**, **MentorNet / MentorMix**, **ELR / ELR+**, **NGC**, **TCL**, **NCR**, and **MOIT+** [20-22, 26].
    *   Standard loss-correction and reweighting baselines like **F-correction**, **P-correction**, **M-correction**, **Decoupling**, and **Mixup** [20, 21, 26].

## Results, limitations, and prior work (NLM Q2)

**(1) Key quantitative results and improvements over baselines**

*   **Massive Improvements on Extreme Synthetic Noise:** On the CIFAR-10 and CIFAR-100 datasets under an extreme 90% symmetric noise rate, the proposed method achieved **89.2% and 45.7% test accuracy**, respectively [1-3]. This substantially outperformed the DivideMix baseline by large margins of 13.8% and 14.7% [3]. Under asymmetric noise settings, the method surpassed DivideMix by 3.0% and MOIT+ by 1.9% [3].
*   **Superiority on Controlled Real-World Noise:** Evaluated on the Red Mini-ImageNet dataset, the proposed framework surpassed the previous state-of-the-art method (InstanceGM) across all noise rates [4, 5]. Specifically, at 20%, 40%, 60%, and 80% noise rates, it achieved accuracies of **61.26%, 57.09%, 53.25%, and 45.65%**, beating InstanceGM by 2.9%, 4.8%, 5.3%, and 6.0% respectively [4, 5].
*   **WebVision and ImageNet Performance:** When initialized using DivideMix, the method achieved a top-1 accuracy of 79.08% and top-5 accuracy of 91.96% on the WebVision dataset, improving upon DivideMix by 1.76% and 0.32% respectively [6, 7]. When evaluating this model's transferability directly on ImageNet, its top-5 accuracy reached **93.12%**, outperforming DivideMix by 2.28% [6, 7].
*   **Enhancement on Human-Annotated Noise:** The framework showed consistent improvements on the Clothing1M benchmark (achieving 74.84% accuracy compared to DivideMix's 74.76%), and it successfully improved upon the DivideMix baseline across all human-annotated noise splits (Aggregate, Random, and Worst) in the CIFAR-10N and CIFAR-100N datasets [5, 8, 9].

**(2) Limitations, failure modes, or negative results noted by the authors**

*   **Negative Result for Cross-Entropy Loss:** The authors explicitly note a failure mode when attempting to train the classifier on the CLIP-selected clean subset using standard cross-entropy loss, which caused the top-1 accuracy on ImageNet to **drop by 0.6%** compared to the baseline [10]. This failure occurs because the selected clean data contains many "easy" samples and very few "hard" samples [11]. Because cross-entropy assigns equal weight to all samples, the model overfits the simple patterns and fails to learn an accurate decision boundary, requiring the authors to replace it with Focal Loss [11].
*   **Underwhelming Results for "Prompt Consistency":** The authors hypothesized that using two different contextual prompts (e.g., adding a domain-specific word like "animal") and measuring the Jensen-Shannon divergence between their predictions would help filter out out-of-domain noisy data [12, 13]. However, this strategy yielded a negative result: its performance was **"almost comparable against GMM"** and failed to meaningfully surpass the simpler "Prediction Confidence" strategy, leading the authors to conclude it requires far more sophisticated prompt design [10, 14].
*   **Sensitivity to High Selection Thresholds ($\rho$):** If the prediction confidence threshold ($\rho$) is set too high (e.g., 0.9), the system aggressively discards too many training instances [15]. The authors note this extreme reduction in data prevents the model from learning a good decision boundary, causing **WebVision accuracy to drop significantly** [15].
*   **Failure at Large Margin Values ($\delta$):** While the noise-aware margin ($\delta$) is crucial for preventing the model from becoming overconfident, the authors observed a failure mode if it is set too high [16]. At $\delta = 1.0$, the large margin severely hinders classifier optimization, causing WebVision top-1 accuracy to **plummet to just 31.0%** [16].

**(3) Top 5–7 most heavily cited prior works named in the related work or introduction**

1.  **Li et al. (2020) [DivideMix]:** Heavily cited as the primary state-of-the-art semi-supervised learning baseline, which the authors use both as a comparative benchmark and as the initialization backbone for their own architecture [5, 6, 17-19].
2.  **Radford et al. (2021) [CLIP]:** Cited extensively as the foundational open-vocabulary vision-language surrogate model that the authors leverage for their zero-shot, training-free sample selection [20-22].
3.  **Han et al. (2018a/b) [Co-teaching]:** Cited as a foundational approach representing the "small-loss criterion," a learning-centric strategy that identifies clean samples by assuming networks fit simple patterns first [17, 23, 24].
4.  **Arpit et al. (2017):** Cited to establish the foundational theoretical premise of label noise research: the "memorization effect," which posits that deep networks fit clean patterns before eventually memorizing noisy, corrupted labels [23, 25-27].
5.  **Arazo et al. (2019):** Cited as a foundational work for utilizing unsupervised label noise modeling and prediction-based pseudo-label correction, as well as for establishing standard Gaussian Mixture Model (GMM) baselines [14, 23, 28, 29].
6.  **Xiao et al. (2015):** Cited for exploring early methods of learning from massive noisy web data, and for introducing the Clothing1M dataset that the authors use for real-world benchmarking [5, 30-32].
7.  **Ortego et al. (2021) [MOIT]:** Cited as a recent methodology that handles label noise by utilizing neighborhood information (K-Nearest-Neighbors) for sample selection and contrastive learning [17, 18, 22, 23].

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

This work informs supervised learning when training targets are **proxy or surrogate labels** (e.g., attribution-derived continuous scores rather than direct measurements of the deployment objective). Compare the paper's assumptions about label noise structure (systematic vs. random; instance-dependent vs. class-conditional) to Shapley-style credit assignments used as training signals.

## Method Tracker Update

- Add or increment counts for primary method and baselines named in this paper (see `method-tracker.md`).

