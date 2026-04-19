Date: 2026-04-12
Source: https://arxiv.org/pdf/2109.02986
NLM Source ID: 8ae72a0a-251b-4dc7-9191-b0d6112c57b8
Venue: arXiv 2021
Relevance: Core
Priority: 2

# Instance-dependent Label-noise Learning under a Structural Causal Model (2021)

**Authors:** Not specified in source.
**Affiliation:** Not specified in source.

## Contribution, method, and experimental setup (NLM Q1)

**(1) Core problem and key contribution**
*   **Core problem:** Deep learning models easily overfit to label errors, which degrades their performance [1]. To solve this, existing methods try to model the transition matrix—the probability $P(\tilde{Y}|Y, X)$ that a clean label $Y$ flips to a noisy label $\tilde{Y}$ for a given instance $X$ [2]. However, this transition matrix is generally not identifiable without making strong, often unrealistic assumptions, such as assuming the noise is instance-independent, part-dependent, or has strict upper bounds [2, 3].
*   **Key contribution:** The authors introduce **CausalNL**, a novel generative approach that provides a structural causal perspective to learning with instance-dependent label noise [4]. They observe that in many standard datasets (e.g., SVHN, CIFAR, FashionMNIST), the underlying true label $Y$ is a *cause* of the image instance $X$ [1, 4, 5]. Because of this causal relationship, the distribution of the instances $P(X)$ and the conditional distribution $P(Y|X)$ are entangled [1, 6]. The authors demonstrate that adding constraints to properly model the instances, such as a low-dimensional manifold constraint, helps make the label noise transition matrix identifiable without relying on the restrictive assumptions of prior work [6, 7]. This ultimately leads to a better classifier that successfully recovers clean labels [6, 8].

**(2) Proposed method or architecture in detail**
The proposed CausalNL method is built upon the Variational Autoencoder (VAE) framework to model the causal structure between the instance ($X$), noisy label ($\tilde{Y}$), latent feature ($Z$), and latent clean label ($Y$) [8, 9].
*   **Encoder (Inference) Networks:** The model approximates the posterior distribution using two encoder networks [10]. The first, $q_{\phi_1}(Y|X)$, acts as the primary classifier, taking an instance and inferring its clean label [11]. The second, $q_{\phi_2}(Z|Y,X)$, infers the latent feature representation $Z$ based on the instance and the inferred label [12, 13].
*   **Decoder Networks:** The architecture utilizes two decoder networks [10]. The first decoder, $p_{\theta_1}(X|Y,Z)$, attempts to reconstruct the original instance [12]. By constraining the latent feature $Z$ to a low dimension, the network is forced to rely on $Y$ (acting as a cluster ID) to successfully minimize the reconstruction error [14]. The second decoder, $p_{\theta_2}(\tilde{Y}|Y,X)$, predicts the noisy label, effectively acting as the transition matrix [12, 14].
*   **Optimization via ELBO:** The model is trained end-to-end by minimizing the negative Evidence Lower Bound (ELBO) [15]. This loss function combines an $\mathcal{L}_1$ reconstruction loss for the instance, a cross-entropy loss for the noisy label predictions, and two Kullback-Leibler (KL) divergence regularizers [14, 16]. The regularizers enforce a uniform prior distribution for $Y$ and a standard multivariate Gaussian prior for $Z$ [16, 17].
*   **Integration with Co-teaching:** To accurately link the unsupervised clusters discovered by the VAE to the actual clean labels while reducing selection bias, the authors duplicate their architecture into a two-branch framework [18, 19]. The framework integrates the "co-teaching" technique, where the two sets of encoders identify instances with small loss values and exchange them in each mini-batch to update their peer network [18, 20].

**(3) Datasets used for evaluation and comparison baselines**
*   **Datasets Used:**
    *   *Synthetic Label Noise:* The framework was evaluated on four standard datasets manually corrupted with instance-dependent label noise: **FashionMNIST, SVHN, CIFAR-10, and CIFAR-100** [21]. An illustrative 2D **MOON** dataset was also used to visually demonstrate how the manifold constraint recovers label transitions [6].
    *   *Real-World Label Noise:* The method was tested on **Clothing1M**, a massive dataset containing one million images with unknown, real-world label noise [21, 22].
*   **Comparison Baselines:** The proposed CausalNL model was benchmarked against several state-of-the-art approaches:
    *   **CE (Cross Entropy):** Standard deep network training on noisy data [23].
    *   **Decoupling:** A method that trains two networks specifically on samples where their predictions disagree [23].
    *   **MentorNet & Co-teaching:** Approaches that handle noisy labels by selectively training on instances with small loss values [23].
    *   **Mixup:** An empirical risk minimization baseline [6, 24].
    *   **Forward, Reweight, and T-Revision:** Methods that explicitly utilize a class-dependent transition matrix to correct the loss function [23].

## Results, limitations, and prior work (NLM Q2)

**(1) Key quantitative results and improvements over baselines**
*   **Massive Gains Under High Noise (IDN-50%):** The proposed CausalNL method widens the performance gap significantly in the hardest cases, achieving **at least a 10% higher classification accuracy than the best baseline methods** on synthetic datasets corrupted with 50% instance-dependent noise [1].
*   **CIFAR-10 and SVHN:** On CIFAR-10 with 50% noise, CausalNL achieved **77.39% accuracy**, whereas the standard Cross-Entropy (CE) baseline fell to 39.42% and the best competing baseline (Decoupling) reached only 50.43% [2]. On SVHN with 50% noise, CausalNL reached **85.41%**, compared to Mixup's 68.95% and Co-teaching's 67.62% [3, 4].
*   **FashionMNIST and CIFAR-100:** On FashionMNIST at 50% noise, CausalNL achieved **78.19%** against T-Revision's 68.99% [3, 5]. On CIFAR-100, while accuracy was universally lower, it still led with **32.12%** versus Co-teaching's 23.97% [6, 7].
*   **Real-World Data Success (Clothing1M):** When evaluated on the real-world Clothing1M dataset, which contains unknown and naturally occurring label noise, CausalNL achieved the highest accuracy of **72.24%**, surpassing strong baselines like T-Revision (70.97%) and Reweight (70.40%) [1, 7].

**(2) Limitations, failure modes, or negative results noted by the authors**
*   **Computational Inefficiency:** The generative CausalNL model contains **more parameters** than previous discriminative methods because it explicitly learns the distribution of the instances $P(X)$, resulting in a "little bit sacrifice on computational efficiency" [8].
*   **Approximation Error in Inference:** To efficiently infer clean labels on test data (where noisy labels are absent), the authors approximate the posterior $q_{\phi_1}(Y|\tilde{Y}, X)$ by dropping the noisy label condition entirely, yielding $q_{\phi_1}(Y|X)$ [9]. The authors note this introduces some approximation error, though they argue it is not very large because the images themselves contain sufficient information [9].
*   **Universal Struggles on CIFAR-100:** The authors observed a general negative result on the highly complex CIFAR-100 dataset, explicitly noting that **"all the methods do not work well"**, even though CausalNL still managed to achieve the highest relative performance [1].
*   **Lack of Theoretical Identifiability Proof:** In their conclusion, the authors note that they **have not yet established the strict theoretical identifiability result** for their method under specific data-generative assumptions, leaving this mathematical proof for future work [8].

**(3) Top 5–7 most heavily cited prior works named in the related work or introduction**
*   **Kingma and Welling (2013) - *Auto-encoding variational bayes*:** Heavily cited as the foundational architecture establishing the Variational Autoencoder (VAE) framework and the reparameterization trick, which the authors extend to perform inference in their causal model [10-13].
*   **Han et al. (2018) - *Co-teaching: Robust training of deep neural networks with extremely noisy labels*:** Extensively referenced as a leading baseline and explicitly integrated into the CausalNL framework to dynamically select reliable training examples and reduce selection bias [14-20].
*   **Pearl (2000) - *Causality: Models, Reasoning, and Inference*:** Cited as the foundational text for structural causal models (SCMs), Markov conditions, and the causal graphs used to model the data generation process [11, 21, 22].
*   **Xia et al. (2020) - *Part-dependent label noise: Towards instance-dependent label noise*:** Referenced for prior attempts to model instance-dependent noise using part-dependent assumptions, and heavily utilized as the primary methodology for manually injecting instance-dependent label noise into the synthetic evaluation datasets [23-25].
*   **Natarajan et al. (2013) - *Learning with noisy labels*:** Cited as a foundational work attempting to make the transition matrix identifiable by relying on the restrictive "instance-independent" assumption [15, 23, 26].
*   **Patrini et al. (2017) - *Making deep neural networks robust to label noise: A loss correction approach*:** Frequently cited as a primary baseline ("Forward" loss correction) that utilizes a class-dependent transition matrix to correct the network's loss function [15, 22, 23, 27, 28].
*   **Angluin and Laird (1988) - *Learning from noisy examples*:** Cited in the introduction as the pioneering work that initiated the study of learning with noisy labels [29, 30].

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

This work informs supervised learning when training targets are **proxy or surrogate labels** (e.g., attribution-derived continuous scores rather than direct measurements of the deployment objective). Compare the paper's assumptions about label noise structure (systematic vs. random; instance-dependent vs. class-conditional) to Shapley-style credit assignments used as training signals.

## Method Tracker Update

- Add or increment counts for primary method and baselines named in this paper (see `method-tracker.md`).

