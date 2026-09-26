# On the Convergent Validity of Offline Evaluation Designs for Recommender Systems [1, 2]

**Source:** https://arxiv.org/pdf/2607.25097.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `7fedeced-8eec-409c-adc9-cff816b1f314`  
**Queue id:** G35  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *On the Convergent Validity of Offline Evaluation Designs for Recommender Systems* [1, 2]
* **Authors:** **Sushobhan Parajuli**, **Samira Vaez Barenji**, and **Michael D. Ekstrand** [1]
* **Affiliations:** Department of Information Science, **Drexel University**, Philadelphia, PA, USA [1]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [2]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Offline evaluation based on historical interaction logs is the standard methodology for evaluating recommender systems, but interaction data is sparse, incomplete, and missing not at random (MNAR) [1, 4–5]. Common experimental design choices—data filtering, candidate set construction, relevance thresholds, and list cutoffs—substantially alter recommender algorithm rankings, but it remains unclear whether sparse offline evaluation setups reliably reflect true user preferences or align with dense ground-truth feedback [1, 6–7].
* **Key Contribution:**
  * Performs the first systematic measurement study assessing the **convergent validity** (using Kendall's \\(\tau\\) rank correlation) between sparse top-N offline evaluations and dense ground-truth user feedback [1, 3, 4].
  * Evaluates 45 recommendation models across 97–123 configurations on MovieLens and KuaiRec, demonstrating that sparse evaluations do not consistently capture user preferences and can even completely invert model rankings depending on dataset and design choices [1, 5-7].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Evaluation Framework & Design Configurations**
* **Measurement Protocol:** Compares model rankings obtained from sparse offline evaluation setups (\\(M_S\\)) against rankings derived from dense ground-truth evaluation setups (\\(M_D\\)) using Kendall’s \\(\tau\\) rank correlation [7–8, 12, 18, 20].
* **Recommendation Models Evaluated:** Evaluates 45 recommendation algorithms from LensKit 2026.1.0 (yielding 97 model variants on MovieLens and 123 on KuaiRec), including UserKNN, ItemKNN, Implicit/Biased Matrix Factorization (ALS/SGD), BiasedSVD, NMF, BPR, WARP, Logistic MF, and fsSLIM [18–19, 24].
* **Experimental Factors Varied:**
  1. *Candidate Set Construction:* Full candidates (all unseen items), U-1000 (1,000 uniformly sampled items), and P-1000 (1,000 popularity-weighted sampled items) [8].
  2. *Evaluation List Lengths:* \\(k \in \{10, 20, 100\}\\) [26–27].
  3. *Relevance Thresholds:* Binary rating/watch-ratio thresholds vs. graded relevance gain functions [9, 10].

#### **Credit Assignment Mechanics**
* **Not specified in source / Does NOT assign credit to individual touchpoints, items, or actions.** This work is a measurement-theoretic evaluation study analyzing offline metric validity, not an attribution model or recommendation algorithm that assigns interaction-level credit [1, 7–8].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Ground-Truth Interventions:**
  1. **MovieLens-32M:** Sparse training/evaluation data consists of 31.7M explicit ratings (0.5–5.0 scale) [21–22]. Dense ground truth uses `interest.qrels` (51 active MovieLens users evaluating pooled recommendation lists on a 0–4 explicit interest scale) from Smucker & Chamani (2025) [21–22].
  2. **KuaiRec:** Sparse data uses the "Big" matrix (7,176 users, 10,728 items, 16.3% density) based on video watch ratios [9]. Dense ground truth uses the "Small" matrix (1,411 users, 3,327 items, 99.6% density collected via controlled exposure) from Gao et al. (2022) [9].
* **Production Deployment:** **Not specified in source** (this is an offline empirical measurement study) [1, 11, 12].
* **Comparison Baselines / Models Evaluated:** Evaluates 45 model architectures across LensKit 2026.1.0, including Popularity, Bias, UserKNN (\\(k \in \{5, 20\}\\)), ItemKNN (implicit/explicit), Implicit MF (ALS), Biased MF (ALS/SGD), BiasedSVD (\\(d \in \{32, 64\}\\)), NMF, BPR, WARP, Logistic MF, and fsSLIM (\\(k \in \{50, 100, 1000\}\\)) [18–19, 24].

---

### **(5) Key Quantitative Results with Numbers**

* **MovieLens-32M Kendall's \\(\tau\\) Rank Correlations:**
  * For short-list dense targets (**Very Interested, \\(k=10\\)**): P-1000 candidate set at sparse \\(k=100, r \ge 3.0\\) achieved the highest correlation (\\(\mathbf{\tau = 0.29}\\)), compared to Full candidates (\\(\mathbf{\tau = 0.21}\\) at \\(k=10\\) and \\(\mathbf{\tau = 0.26}\\) at \\(k=100\\)) [28–29, 32].
  * For long-list dense targets (**Very Interested, \\(k=100\\)**): Full candidate set at sparse \\(k=100, r \ge 3.0\\) achieved the highest overall correlation (\\(\mathbf{\tau = 0.43}\\)) [13-15]. At \\(k=100\\), U-1000 dropped to \\(\mathbf{\tau = 0.36}\\) and P-1000 dropped to \\(\mathbf{\tau = 0.18}\\) [15-17].
  * *Model Rank Discrepancies:* Top dense model **BiasedSVD-d64** (Dense NDCG@10 = **0.323**) ranked **40th** under P-1000 sparse evaluation (\\(k=100, r \ge 3.0\\)) and **23rd** under its best sparse design [18, 19]. Conversely, **fsSLIM-nn1000** ranked **1st** in sparse evaluation and **3rd** in dense evaluation [19].
* **KuaiRec Kendall's \\(\tau\\) Rank Correlations:**
  * Sparse evaluation was **negatively correlated** with dense ground truth across ALL evaluation designs (\\(\mathbf{\tau}\\) ranged from \\(\mathbf{-0.19}\\) to \\(\mathbf{-0.58}\\)) [41, 52–53].
  * For **Watched \\(2\times\\) (\\(k=10\\))**: Least negative correlation was P-1000 at sparse \\(k=20, r \ge 2.0\\) (\\(\mathbf{\tau = -0.19}\\)); Full candidates achieved \\(\mathbf{\tau = -0.24}\\) [41–42, 53–54].
  * For **Graded relevance**: \\(\tau\\) reached extreme negative inversion (\\(\mathbf{\tau = -0.57}\\) to \\(\mathbf{-0.58}\\)) [43–46, 53].
  * *Model Rank Discrepancies:* Top dense models **BiasedSVD-d32** (Dense NDCG@10 = **0.672**) and **BiasedSVD-d64** (**0.665**) ranked **35th** and **32nd** under Full candidate sparse evaluation (\\(k=20, r \ge 2.0\\)) [48–49, 53].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Complete Metric Inversion Failure (KuaiRec):** Sparse offline evaluation completely failed and inverted model rankings relative to dense ground truth across all design choices (\\(\tau < 0\\), down to \\(-0.58\\)), showing that offline evaluation on implicit watch-ratio data can be fundamentally incompatible with true user preferences [52–53].
2. **Severe Misranking of Explicit Matrix Factorization:** Explicit feedback models (e.g., BiasedSVD) achieved top performance on dense ground truth but were severely penalized and misranked as low-performing algorithms (e.g., 23rd–40th place) under sparse evaluations [18, 20, 21].
3. **Popularity Sampling Reversal at Long Cutoffs:** Popularity-weighted candidate sampling (P-1000) improved correlation for short-list targets (\\(k=10, \tau=0.29\\)) but broke down and performed poorly for long-list targets (\\(k=100, \tau=0.18\\)) [13, 15].
4. **Absence of Uniform Best Evaluation Design:** No single evaluation setup was uniformly optimal across datasets, list cutoffs, or relevance targets, proving that observed algorithm performance differences are often driven by evaluation design rather than underlying model effectiveness [8, 55, 58–60].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Steck (2010) [Ref 29]:** *Training and Testing of Recommender Systems on Data Missing Not at Random* (KDD '10) [22-24].
2. **Krichene & Rendle (2020) [Ref 20]:** *On Sampled Metrics for Item Recommendation* (KDD '20) [25-28].
3. **Gao et al. (2022) [Ref 10]:** *KuaiRec: A Fully-observed Dataset and Insights for Evaluating Recommender Systems* (CIKM '22) [9, 29].
4. **Smucker & Chamani (2025) [Ref 28]:** *Extending MovieLens-32M to Provide New Evaluation Objectives* (SIGIR '25) [30, 31].
5. **Cañamares & Castells (2020) [Ref 4]:** *On Target Item Sampling in Offline Recommender System Evaluation* (RecSys '20) [32, 33].
6. **Marlin & Zemel (2009 / 2012) [Refs 22, 23]:** *Collaborative Prediction and Ranking with Non-Random Missing Data* (RecSys '09) / *Collaborative Filtering and the Missing at Random Assumption* (arXiv '12) [22, 23, 28, 34].
7. **Beel & Brunel (2019) / Beel & Langer (2015) [Refs 1, 2]:** *Data Pruning in Recommender Systems Research* & *A Comparison of Offline Evaluations, Online Evaluations, and User Studies* [35-37].

---

💡 *Would you like to explore how convergent validity findings regarding full candidate set evaluation vs. popularity-weighted candidate sampling apply to offline evaluation protocols for your dating platform's ranker?*

---

## 2. Evidence

See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

## 3. Limitations

See limitations in §1 if present. Replace any NLM refusal with: Not specified in source.

---

## 4. Prior works named

See cited prior works in §1.

---

## 5. Project Relevance

### **Source Evaluation: *On the Convergent Validity of Offline Evaluation Designs for Recommender Systems***  
*(Parajuli, Vaez Barenji, & Ekstrand, Drexel University, RecSys ’26)* [1]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Neither.** [1, 7–8]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **No.** While published in RecSys 2026 [2], it is an academic empirical measurement study on the **convergent validity** of offline recommender system evaluation protocols across sparse interaction logs vs. dense ground truth [1, 7–8]. It is not an industry multi-touch attribution (MTA) measurement system.
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** It evaluates how offline evaluation design choices (filtering thresholds, candidate sampling, relevance cutoffs) correlate with dense ground-truth user preferences using Kendall’s \\(\tau\\) rank correlation across 45 recommendation algorithms [1, 3, 4], rather than attributing user retention or active days to individual interaction touchpoints.

---

### **(B) Q2 Class**

**NOT.** [1, 7–8]  
* **Justification:** This paper is an offline evaluation design measurement study. It does **not** propose an interaction-level retention attribution model, surrogate linkage framework, or RL/bandit retention policy, and does **not** publish a per-exposure retention credit table.

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **No per-interaction credit table.** [1, 7–8]
* **Target Outcome:** Evaluates offline ranking metrics (**NDCG@k** and **DCG@k** at \\(k \in \{10, 20, 100\}\\)) across sparse logs compared to dense ground-truth user feedback [20, 26–27]:
  1. *MovieLens-32M Target:* User interest in watching pooled recommended movies (\\(r \ge 2.0\\) Interested, \\(r \ge 3.0\\) Very Interested on a 0–4 scale) [5].
  2. *KuaiRec Target:* Short-video watch ratios (\\(r \ge 0.85\\) Watched \\(\ge 85\%\\), \\(r \ge 2.0\\) Watched \\(2\times\\), and Graded watch ratio) [6].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves/Informs Last-Touch N7:** This paper does **not** provide a post-hoc attribution model or ranking algorithm to replace last-touch N7 [1, 7–8]. Instead, it provides **critical methodological cautions for offline ranker evaluation**:
  1. It demonstrates that sparse offline metrics can be **fundamentally incompatible or even negatively correlated** with dense user preferences (e.g., Kendall’s \\(\tau\\) ranged from **\\(-0.19\\) to \\(-0.58\\)** on KuaiRec) [41, 52–53].
  2. It warns that offline model comparisons are heavily distorted by candidate sampling (Full vs. U-1000 vs. P-1000) and rating cutoffs, proving that observed algorithm performance gains are often artifacts of testing protocols rather than true model superiority [8, 40, 58–60].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  * **Sparse Interaction Logs:** Swiping histories, match logs, and chat events represent sparse, Missing Not At Random (MNAR) interaction matrices [7, 8].
  * **Evaluation Design Caution:** Evaluating swipe/match rankers against sparse test sets using popularity-sampled candidates (P-1000) or truncated lists (\\(k=10\\)) can severely misrank models relative to true user preferences [29, 31, 40, 48–49].

---

### **(E) Selection-Bias & Confounding Handling**

* **Addresses Missing Not At Random (MNAR) & Exposure Bias:** Evaluates how different experimental candidate sampling and filtering strategies mitigate or amplify observational bias in sparse interaction data [5–6, 10, 16]:
  1. **Candidate Set Construction:** Compares **Full candidate sets** (all unseen items), **U-1000** (1,000 uniformly sampled unseen items), and **P-1000** (1,000 popularity-weighted sampled items) [9].
  2. **Relevance Thresholding & Graded Gains:** Compares binary thresholds vs. graded relevance functions [10].
  3. **Convergent Validity Baseline:** Uses dense ground-truth interventions—pooled user interest judgments (`interest.qrels` on MovieLens-32M) and a 99.6% dense "small" matrix from controlled exposure on KuaiRec—as reference points to measure offline metric validity [17, 21–23].

---

### **(F) Deployed or Production Dataset Evidence**

* **Production Deployment:** **Not specified in source** (academic empirical measurement study conducted at Drexel University) [1].
* **Datasets & Numbers Quoted from Source:**
  * **MovieLens-32M:** **31.7 million explicit ratings** on a 0.5–5.0 scale as sparse data [21–22]; dense ground-truth uses `interest.qrels` from **51 active users** evaluating pooled recommendation lists on a 0–4 explicit interest scale [21–22].
  * **KuaiRec:** "Big" sparse matrix (**7,176 users, 10,728 items, 16.3% density**) [6]; "Small" dense matrix (**1,411 users, 3,327 items, 99.6% density**) collected via controlled exposure [6].
  * **Model Suite:** Evaluated **45 recommendation models** from LensKit 2026.1.0 across **97 configurations** on MovieLens and **123 configurations** on KuaiRec [18–19, 24].
  * **MovieLens Kendall's \\(\tau\\) Correlations:**
    * *Short-list dense target (\\(k=10\\), Very Interested):* P-1000 candidate set at sparse \\(k=100, r \ge 3.0\\) achieved highest correlation (**\\(\tau = 0.29\\)**), vs. Full candidates (**\\(\tau = 0.21\\)** at \\(k=10\\), **\\(\tau = 0.26\\)** at \\(k=100\\)) [28–29, 32].
    * *Long-list dense target (\\(k=100\\), Very Interested):* Full candidate set at sparse \\(k=100, r \ge 3.0\\) achieved highest overall correlation (**\\(\tau = 0.43\\)**); U-1000 dropped to **\\(\tau = 0.36\\)** and P-1000 dropped to **\\(\tau = 0.18\\)** [11-13].
    * *Model Misrankings:* Top dense explicit model **BiasedSVD-d64** (Dense NDCG@10 = **0.323**) ranked **40th** under P-1000 sparse evaluation (\\(k=100, r \ge 3.0\\)) and **23rd** under its best sparse design [14, 15].
  * **KuaiRec Kendall's \\(\tau\\) Metric Inversion:**
    * Sparse evaluation showed **negative correlation / metric inversion** across ALL designs (\\(\tau\\) ranged from **\\(-0.19\\) to \\(-0.58\\)**) [41, 52–53].
    * *For Watched \\(2\times\\) (\\(k=10\\)):* Least negative was P-1000 at sparse \\(k=20, r \ge 2.0\\) (**\\(\tau = -0.19\\)**); Full candidates achieved **\\(\tau = -0.24\\)** [41–42, 53]. Graded relevance reached extreme negative inversion (**\\(\tau = -0.57\\) to \\(-0.58\\)**) [43–46, 53].
    * *Model Misrankings:* Top dense models **BiasedSVD-d32** (Dense NDCG@10 = **0.672**) and **BiasedSVD-d64** (**0.665**) ranked **35th** and **32nd** under Full candidate sparse evaluation (\\(k=20, r \ge 2.0\\)) [48–49, 53].

---

💡 *Would you like to explore how these convergent validity findings regarding full candidate evaluation vs. popularity-weighted sampling apply to setting up offline evaluation protocols for your dating app's ranker?*

---

## 6. Community Reaction

No significant community discussion searched at card-write time; extraction is NLM-scoped.

---

## Papers That Mention This Paper (Reverse Citation Map)

| Mentioning Paper | Section | Summary of Mention |
|-----------------|---------|-------------------|
| (To be filled in during Phase 3.7) | | |

---

## Meta Information

**PDF:** ingested via NotebookLM  
**Relevance:** Core if Q2 class is TRUE or PARTIAL or Q1 industry system; else Related  
**Priority:** see queue.md `G35`
