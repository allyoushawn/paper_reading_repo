# Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking [1]

**Source:** https://arxiv.org/pdf/2508.00751.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `4c1119dd-6713-4864-a194-a53a14065084`  
**Queue id:** G15  
**Q2 class:** NOT

---

## 1. Summary

### **Part 1: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking* [1]
* **Authors:** **Qing Zhang**¹, **Alex Deng**\*², **Michelle Du**¹, **Huiji Gao**¹, **Liwei He**¹, and **Sanjeev Katariya**¹ (\*Work completed while employed by Airbnb) [1]
* **Affiliations:** 
  1. **Airbnb** (San Francisco, CA & Seattle, WA, USA) [1]
  2. **Microsoft** (Seattle, WA, USA) [1]
* **Year:** **2025** (Conference dates: August 3–7, 2025) [2]
* **Venue:** *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD ’25), August 3–7, 2025, Toronto, ON, Canada* [2–3]

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** Online A/B testing on e-commerce platforms like Airbnb requires long running times to achieve statistical power for sparse conversion metrics (accommodations booking) [3]. Airbnb users travel infrequently (~twice a year), search journeys span multiple days, and effect sizes of mature ranking algorithms are small [3]. Offline evaluation metrics (e.g., NDCG) are fast but lack accuracy and disconnect from online business conversion metrics [6–7].
* **Key Contributions:**
  1. **Competitive Pair Team Drafting Interleaving:** An unbiased, computationally efficient online interleaving framework that achieved a **50x speedup** (traffic reduction) over standard A/B testing [4, 5].
  2. **Online Counterfactual Evaluation:** An off-policy counterfactual evaluation framework that avoids blending search results (preserving pristine user experience) and handles set-level re-ranking optimizations with up to a **100x speedup** over A/B testing [4, 6-8].
  3. **Multi-Session Conversion Event Attribution:** Establishes a multi-session event attribution framework that credits booking conversions across all search occurrences during the experiment period [9].
  4. **Side-by-Side Industrial Deployment:** Deployed and evaluated both techniques side-by-side in live production across over 100 search ranking experiments at Airbnb [6, 10-13].

---

#### **(3) Proposed Method or Architecture in Detail**
* **Competitive Pair Interleaving:**
  * Given candidate lists \\(C\\) (Control) and \\(T\\) (Treatment), a coin flip determines team selection priority once [24–25]. In each draft step, available items from \\(C\\) and \\(T\\) are compared: if different, they form a "competitive pair" \\([C[k_c]_C, T[k_t]_T]\\); if identical, the item is inserted without team assignment [24–25, 27].
  * Team preference is measured by counting competitive pair wins (clicks/bookings) at the user level (\\(\tau_i = \text{wins}(T) - \text{wins}(C)\\)) [14].
  * Delivered via a two-layer delivery system: Layer 1 splits traffic into A/B vs. interleaving; Layer 2 routes users to interleaving "lanes" with parallel calls to control/treatment rankers [31–32].
* **Online Counterfactual Evaluation:**
  * Generates full lists \\(L_c\\) and \\(L_t\\) for each search query, displays one list \\(w \in \{c, t\}\\) (determined by user ID coin flip), and treats \\(1-w\\) as the counterfactual list [35–36].
  * **Estimators:**
    * *Direct Decomposition (\\(\tau_{\text{decomp}}\\)):* Decomposes outcomes into similar ranking positions (\\(\tau_{\text{sim}}\\)) vs. different ranking positions (\\(\tau_{\text{diff}}\\)), reweighting with \\(\theta = 0.2\\) [37–38].
    * *Estimated Reward Based (\\(\tau_g, \tau_{\text{win-loss}}\\)):* Uses an exponential position decay model \\(f(r) = \gamma^{-r}\\) (\\(\gamma \in \{0.9, 0.95\}\\)) and similarity threshold \\(\alpha = 2\\) [39–41]. Gain \\(g_i = 1 - \gamma^{\max(|r_i(w) - r_i(1-w)| - \alpha, 0)}\\) [40–41].
    * *OEC Metric (\\(\tau_{\text{oec}}\\)):* Combines direct decomposition and gain estimators: \\(\tau_{\text{oec}} = 0.5 \cdot \tau_{\text{decomp}} + 0.5 \cdot \tau_g\\) [15].
* **Credit Assignment & Event Attribution Mechanics:**
  * Events (clicks or bookings) are attributed to competitive pairs (interleaving) or relative position rank differences (counterfactual evaluation) [26, 28, 39–41].
  * For sparse booking conversions, the framework attributes the booking event to **all search occurrences** where the listing was presented to the user during the experiment period, accounting for compound exposure across the multi-session search journey [9, 16].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Production Dataset & Corpus:** Evaluated directly in production at Airbnb (not on simulated datasets) using a validation corpus of **29 interleaving–A/B test pairs** and **30 counterfactual–A/B test pairs** [10, 12, 13, 17].
* **Production Deployment:** Fully deployed live in production on Airbnb's search ranking infrastructure serving all ranking experimentations [6, 10, 12].
* **Comparison Baselines:**
  * Standard Online A/B Testing [12, 13, 18, 19].
  * Prior Interleaving: Balanced Interleaving with IPW (Bi et al., 2022 at Amazon, which reported 60x speedup on 10 tests) [20-23].
  * Prior Counterfactual Evaluation: Metric Decomposition in A/B tests (Deng et al., 2024) [22, 24, 25].

---

#### **(5) Key Quantitative Results with Numbers**
* **Speedup / Traffic Efficiency over A/B Testing:**
  * *Competitive Pair Interleaving:* **50x speedup** (requires 1/50th of the traffic to achieve equal statistical power) [4, 12].
  * *Counterfactual Evaluation:* **15x speedup** for \\(\tau_{\text{oec}}\\), **23x speedup** for \\(\tau_{\text{win-loss}}\\), and **100x speedup** for \\(\tau_g\\) [8].
* **Directional Alignment & Point Estimate Correlation with A/B Tests:**
  * *Interleaving vs. A/B:* **82% directional alignment**, point estimate correlation **corr = 0.60** across 29 test pairs [12].
  * *Counterfactual Evaluation vs. A/B:* Point estimate correlation **corr = 0.65** for \\(\tau_{\text{oec}}\\), **0.66** for \\(\tau_g\\), **0.58** for \\(\tau_{\text{win-loss}}\\), **0.55** for \\(\tau_{\text{diff}}\\), and **-0.29** for \\(\tau_{\text{sim}}\\) across 30 test pairs [52–53].
* **Hyperparameter Sensitivity:** Setting position similarity threshold \\(\alpha = 2\\) achieved superior correlation (**0.66** for \\(\tau_g\\), **0.60** for \\(\tau_{\text{win-loss}}\\)) compared to \\(\alpha = 1\\) (**0.64** and **0.58**) [54–55].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **Failure of Interleaving under Set-Level Optimization:** Interleaving fails when rankers perform set-level re-ranking (e.g., diversity optimization) [6, 23]. Side-by-side placement in competitive pairs causes users to prefer higher-booking-probability control listings over re-ranked treatment listings, yielding false negative drops in interleaving while live A/B test conversion remained neutral [23].
2. **Failure of Counterfactual Evaluation under Shared Real-Time Signals:** When control and treatment rankers differ in their capability to utilize shared real-time user engagement features, the stronger ranker leverages engagement earned by the weaker ranker, gaining an unfair advantage [25].
3. **Negative Correlation of \\(\tau_{\text{sim}}\\):** Direct decomposition similarity metric \\(\tau_{\text{sim}}\\) exhibited a negative correlation (**-0.29**) with A/B test outcomes [25].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Radlinski, Kurup, & Joachims (2008) [Ref 25]:** *How does clickthrough data reflect retrieval quality?* (Team Drafting Interleaving) [5, 26].
2. **Joachims et al. (2002, 2003) [Refs 16, 17]:** *Optimizing search engines using clickthrough data* & *Evaluating Retrieval Performance Using Click-through Data* (Balanced Interleaving) [15–16].
3. **Bi et al. (2022) [Ref 1]:** *Debiased balanced interleaving at Amazon Search* (BI + IPW at Amazon) [20-23, 27, 28].
4. **Hofmann, Whiteson, & De Rijke (2011, 2013) [Refs 11, 12]:** *A probabilistic method for inferring preferences from clicks* & *Fidelity, soundness, and efficiency of interleaved comparison methods* (Probabilistic Interleaving) [9, 15, 29].
5. **Deng et al. (2024) [Ref 6]:** *Metric Decomposition in A/B Tests* (Direct Counterfactual Metric Decomposition) [23, 36–38, 48, 53].
6. **Tan et al. (2023) [Ref 31]:** *Optimizing Airbnb Search Journey with Multi-task Learning* (Airbnb Search Journey) [9].
7. **Deng et al. (2013, 2023) [Refs 5, 7]:** *Improving the sensitivity of online controlled experiments...* (Variance reduction / CUPED in A/B testing) [27].

---

### **Part 2: Dating App Retention Attribution Project Evaluation**

#### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**
* **Answer:** **Q1 only** (Neither Q2) [2, 7–9].
* **Explanation:**
  * *Q1 (Industry/Production Attribution 2025–2026):* **Yes.** Published in KDD 2025 (August 2025) and deployed in live production at Airbnb [2, 8–9].
  * *Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):* **No.** The paper focuses on online experiment acceleration and search ranker evaluation (Interleaving and Counterfactual Evaluation) for e-commerce booking conversion [4, 9, 30], rather than attributing user retention, active days, or return visits to individual in-app interactions.

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [8–10, 35–36].
* **Justification:** The paper presents online experimentation and counterfactual evaluation frameworks (Interleaving and Counterfactual Evaluation) for A/B test acceleration of candidate search rankers, rather than publishing a per-exposure retention credit table or interaction-level retention attribution model [8–10, 35–36].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (at the competitive-pair / search-result level for online ranking evaluation)** [26, 28, 39–41].
* **Target Outcome:** **Booking / Conversion events** (and clicks) [9]. For conversion event attribution, booking events are attributed across **all search occurrences/impressions** where the listing appeared during the experiment period [9, 16].

---

#### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves on Last-Touch:** Last-touch heuristically credits 100% of an outcome to the final touchpoint. Section 5.5 explicitly rejects single-touch/last-touch assumptions for high-stakes multi-session user journeys, noting that user decisions are influenced by every impression experienced across their journey [9].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Multi-Touch Attribution Window:* Assigns retention/match conversion credit to **all profile exposures and swipes** that occurred throughout the user's swiping journey during the experiment period [9, 16].
  2. *Counterfactual Pairwise Evaluation:* Instead of waiting weeks for N7 retention signals in standard A/B tests, compares treatment vs. control candidate rankers using counterfactual position shifts (\\(\tau_g, \tau_{\text{oec}}\\)) on candidate profiles shown during swipes, achieving **15x–100x speedups** in ranker evaluation [9, 39–42, 55].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Competitive Pair Team Drafting:** Single coin flip at startup + alternating drafting eliminates position bias in interleaving lists (\\(P(r=1) = P(r=2) = 0.5\\)) [24–25, 29].
2. **Equal Zone Threshold (\\(\alpha = 2\\)):** Ignores minor rank position perturbations (\\(|r_i(w) - r_i(1-w)| \le \alpha\\)) in counterfactual evaluation to prevent noise from non-meaningful rank changes [31, 32].
3. **Data Quality Monitoring:** Tracks impression distribution and team first-place rates as automated quality control checks to detect unbiasness violations [30–31, 51].

---

#### **(F) Deployment and Production Dataset Evidence**
* **Production Deployment:** Fully deployed in production on Airbnb's search ranking system serving over 100 live experiments [6, 10, 12].
* **Production Validation Corpus:** Evaluated on a production corpus of **29 interleaving–A/B test pairs** and **30 counterfactual–A/B test pairs** [12, 13].
* **Quoted Quantitative Results:**
  * *Interleaving:* **50x speedup** over A/B testing; **82% directional alignment**; point estimate correlation **corr = 0.60** with A/B tests [4, 12].
  * *Counterfactual Evaluation:* **15x speedup** (\\(\tau_{\text{oec}}\\)), **23x speedup** (\\(\tau_{\text{win-loss}}\\)), **100x speedup** (\\(\tau_g\\)); point estimate correlation **corr = 0.65** (\\(\tau_{\text{oec}}\\)), **0.66** (\\(\tau_g\\)), **0.58** (\\(\tau_{\text{win-loss}}\\)), **0.55** (\\(\tau_{\text{diff}}\\)), **-0.29** (\\(\tau_{\text{sim}}\\)) [52–53, 55].
  * *Hyperparameter Sensitivity:* Position similarity threshold \\(\alpha = 2\\) yielded higher correlation (**0.66**) than \\(\alpha = 1\\) (**0.64**) [54–55].

---

💡 *Would you like to explore how Airbnb's multi-session exposure attribution or counterfactual position-decay scoring (\\(\tau_g\\)) could be adapted to evaluate candidate ranker changes for your dating platform?*

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

### **Source Evaluation: *Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking***
*(Zhang et al., Airbnb & Microsoft, KDD 2025: `arXiv:2508.00751`)* [1, 2]

---

### **(A) Query Categorization: Q1 or Q2 or Both or Neither?**

**Q1 only.** [1-3]  
* **Q1 (Industry/Production Attribution 2025–01 to 2026-09):** **Yes.** Published in August 2025 at KDD 2025 (`arXiv:2508.00751`), this paper describes a production evaluation and multi-session conversion attribution framework deployed live in production across Airbnb's search ranking infrastructure [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper focuses on evaluating candidate search rankers and attributing accommodation booking conversions across multi-session search journeys, rather than attributing user retention, active days, or return visits [1, 4, 5].

---

### **(B) Q2 Class**

**NOT.** [8, 10, 35–36]  
* **Justification:** The paper presents online experimentation and counterfactual evaluation frameworks (Interleaving and Counterfactual Evaluation) for accelerating search ranker evaluation, rather than publishing a per-exposure retention credit table or interaction-level retention attribution model [8, 10, 35–36].

---

### **(C) Per-Interaction Credit & Target Outcome**

* **Per-Interaction Credit:** **Yes (at the search-occurrence and competitive-pair level)** [15, 26, 28, 39–41].
* **Target Outcome:** **Accommodation Booking Conversions** (and clicks) [1, 5]. Section 5.5 explicitly details that booking conversions are attributed across **all search occurrences** where a listing appeared during the experiment period, acknowledging the compound effect of repeated exposure across multi-session search journeys [5].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**

* **How it Improves on Last-Touch:** Section 5.5 explicitly rejects single-touch or last-touch rules for high-stakes multi-session user journeys, observing that decisions are influenced by every exposure across the user's journey rather than merely the final interaction [5].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Multi-Touch Journey Window:* Replaces last-touch post-hoc attribution by crediting 7-day retention across **all profile exposures, candidate swipes, and interactions** that occurred throughout the user's multi-session swiping journey during the evaluation period [5].
  2. *Counterfactual Ranker Evaluation:* Rather than waiting weeks for N7 retention signals in standard A/B testing, evaluates candidate profile rankers using counterfactual position-decay estimators (\\(\tau_g, \tau_{\text{oec}}\\)) on profile exposures, achieving **15x–100x speedups** in statistical power [9, 39–41, 55].

---

### **(E) Selection-Bias & Confounding Handling**

1. **Competitive Pair Team Drafting:** Uses a single initial coin flip and alternating selection to eliminate position bias in interleaved result lists, ensuring each ranker has an equal 50% probability (\\(P(r=1) = P(r=2) = 0.5\\)) of occupying top positions [24–25, 29].
2. **Rank Similarity Thresholding (\\(\alpha = 2\\)):** Incorporates an equal-zone similarity threshold \\(\alpha = 2\\) in counterfactual reward estimation, setting incremental gain \\(g_i = 0\\) when position rank differences are minor (\\(|r_i(w) - r_i(1-w)| \le \alpha\\)) to eliminate noise from non-meaningful rank changes [40–41, 54].
3. **Automated Data Quality Checks:** Continuously monitors impression distribution and team first-place rates to verify unbiasedness in production [30–31, 51].

---

### **(F) Deployment & Production Dataset Evidence**

* **Production Deployment:** Fully deployed live in production on Airbnb's search ranking infrastructure and utilized to conduct over 100 search ranking experiments [3, 6, 7].
* **Validation Corpus:** Evaluated directly on a real-world production validation corpus of **29 interleaving–A/B test pairs** and **30 counterfactual–A/B test pairs** [8, 9].
* **Quoted Quantitative Results:**
  * **Interleaving Sensitivity & Speedup:** Achieved a **50x speedup** over traditional A/B testing (requiring 1/50th of the traffic to reach equal statistical power) [8, 10].
  * **Interleaving Alignment:** **82% directional alignment** with A/B test outcomes, with a point estimate correlation of **corr = 0.60** across 29 test pairs [8].
  * **Counterfactual Evaluation Speedup:** Achieved a **15x speedup** for \\(\tau_{\text{oec}}\\), **23x speedup** for \\(\tau_{\text{win-loss}}\\), and **100x speedup** for \\(\tau_g\\) compared to A/B testing [10, 11].
  * **Counterfactual Evaluation Correlations with A/B Tests (Table 2):**
    * \\(\tau_g\\) (Gain Estimator): **corr = 0.66** [12].
    * \\(\tau_{\text{oec}}\\): **corr = 0.65** [9].
    * \\(\tau_{\text{win-loss}}\\): **corr = 0.58** [12].
    * \\(\tau_{\text{diff}}\\): **corr = 0.55** [12].
    * \\(\tau_{\text{sim}}\\): **corr = -0.29** [12].
  * **Position Similarity Threshold Impact (Table 3):** Setting \\(\alpha = 2\\) yielded higher correlation (**0.66** for \\(\tau_g\\), **0.60** for \\(\tau_{\text{win-loss}}\\)) than setting \\(\alpha = 1\\) (**0.64** and **0.58**) [54–55].
  * **Unbiasedness Data Quality Verification (Table 1):**
    * Listings shown: **\\(\Delta = 0.00\%\\)** (\\(p = 0.91\\)) [13].
    * Shown first: **\\(\Delta = -0.01\%\\)** (\\(p = 0.85\\)) [13].
    * Shown reciprocal rank: **\\(\Delta = -0.02\%\\)** (\\(p = 0.85\\)) [13].
    * Listings found: **\\(\Delta = 0.00\%\\)** (\\(p = 0.95\\)) [13].

---

💡 *Would you like to explore how Airbnb's multi-session exposure attribution or counterfactual position-decay scoring (\\(\tau_g\\)) could be adapted to evaluate candidate profile rankers for your dating platform?*

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
**Priority:** see queue.md `G15`
