# Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders [1, 2]

**Source:** https://arxiv.org/pdf/2608.14021.pdf  
**Date analyzed:** 2026-09-24  
**NLM source id:** `9dc30dae-7a13-4032-9339-5cf10dc1bc6a`  
**Queue id:** G29  
**Q2 class:** NOT

---

## 1. Summary

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders* [1, 2]
* **Authors:** **Keito Kozaki**, **Keigo Sakurai**, **Ren Togo**, **Takahiro Ogawa**, and **Miki Haseyama** [1]
* **Affiliation:** **Hokkaido University**, Sapporo, Hokkaido, Japan [1]
* **Year & Venue:** Published in **2026** at the *20th ACM Conference on Recommender Systems (RecSys ’26)*, September 27–October 02, 2026, Minneapolis, MN, USA [2]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Transformer-based sequential recommenders with causal self-attention (e.g., SASRec) rely heavily on the most recent interaction at inference time (**last-item reliance**) [2, 4–5]. However, how this behavior is structurally expressed in the prediction representation remains unclear, as attention weights alone vary smoothly across sequence positions and do not explain why predictive influence collapses discontinuously onto the final item [6, 27–28].
* **Key Contributions:**
  1. **Empirical Characterization:** Quantifies last-item reliance using complementary prediction-time diagnostics (inference-time sequence shuffling and recency-localized Hit Rate of the Last Item / **HRLI@K**) across diverse datasets [3-6].
  2. **Residual Dominance:** Applies a norm-based decomposition to the complete attention block, proving that while self-attention aggregates contextual information, residual addition sharply shifts the output toward same-position inputs [3, 4, 7-9]. Combined with a final-position prediction interface, this self-preservation tendency forms a structural account of extreme last-item reliance [7, 8, 10].
  3. **Inference-Time Residual Scaling Probe:** Uses residual scaling (\\(\alpha\\)) as a controlled diagnostic probe without retraining [3, 11-13]. Shows that reducing residual strength weakens last-item reliance, increases contextual mixing, and recovers a subset of final-position misses where non-final positions (\\(L-1, L-2, L-3\\)) already ranked the target item correctly [2, 9, 42, 45–46].

---

### **(3) Proposed Method or Architecture in Detail**

#### **Architectural Components & Diagnostic Method**
* **Norm-Based Attention Block Analysis:** Decomposes the output representation \\(x_i = \text{LN}(\text{Attn}(x_i, X) + x_i) = \sum_j F_i(x_j)\\) into input-wise vector norm contributions \\(F_i(x_j)\\) [29–30].
* **Mixing Ratio Metric (\\(r_i\\)):** Quantifies contextual aggregation versus self-information retention [8]:
  \\[r_i = \frac{\sum_{j \neq i} \|F_i(x_j)\|}{\sum_j \|F_i(x_j)\|}\\]
  Evaluates \\(r_i\\) at three stages of the attention block: attention output alone (**Attn**), after residual addition (**+Res**), and after layer normalization (**+LN**) [30–31, 33].
* **Inference-Time Residual Scaling (\\(\alpha\\)):** Modifies the block at prediction time to \\(h_i^{(\alpha)} = \alpha x_i + \text{Attn}(x)_i\\) [41–42]. Modulating \\(\alpha\\) (from 1.0 down to 0.1) systematically controls residual preservation strength without altering trained parameters [11, 13].
* **Validation-Based Selection Rule:** Reproduces accuracy–recovery trade-offs via \\(\alpha^* = \arg\max_\alpha \text{Recovery}_{\text{val}}(\alpha)\\) subject to \\(\text{HR}@10_{\text{val}}(\alpha) \ge (1 - \epsilon)\text{HR}@10_{\text{val}}(1)\\) [14].

#### **Credit Assignment Mechanics**
* **Does NOT assign multi-touch sequence attribution or fractional credit** across user interaction touchpoints for conversion or retention modeling.
* Contribution is evaluated strictly as the structural vector norm contribution \\(F_i(x_j)\\) of input position \\(j\\) to output representation \\(i\\) within Transformer layers to analyze representation composition [29–30].

---

### **(4) Datasets, Production Deployment, and Comparison Baselines**

* **Datasets & Scale:** Evaluated across 9 benchmark datasets under 5-core filtering and consecutive-repeat removal [13–15]:
  * **Amazon Beauty:** 22,363 users, 12,101 items, 198,502 interactions (avg. length **8.9**) [15].
  * **Amazon Sports:** 35,598 users, 18,357 items, 296,337 interactions (avg. length **8.3**) [15].
  * **Amazon Video:** 24,303 users, 10,672 items, 231,780 interactions (avg. length **9.5**) [15].
  * **Diginetica:** 61,279 users, 25,593 items, 485,903 interactions (avg. length **7.9**) [15].
  * **Amazon Toys:** 19,412 users, 11,924 items, 167,597 interactions (avg. length **8.6**) [15].
  * **Steam:** 281,349 users, 11,961 items, 3,550,272 interactions (avg. length **12.6**) [15].
  * **BeerAdvocate:** 14,635 users, 22,074 items, 1,475,412 interactions (avg. length **100.8**) [15].
  * **MovieLens-1M (ML-1M):** 6,040 users, 3,416 items, 999,611 interactions (avg. length **165.5**) [15].
  * **Zvuk:** 19,267 users, 150,206 items, 8,087,953 interactions (avg. length **419.8**) [15].
* **Production Deployment:** **Not specified in source** (evaluated on offline benchmark datasets under a Global Time Split protocol) [16-18].
* **Comparison Baselines:**
  * **SASRec** (causal self-attention Transformer) [19].
  * **GRU4Rec** (recurrent architecture) [19].
  * **BERT4Rec** (bidirectional Transformer) [19].
  * **DuoRec** (SASRec with contrastive learning loss) [19].
  * **BSARec** (frequency-domain self-attention) [17].

---

### **(5) Key Quantitative Results with Numbers**

* **Mixing Ratio Collapse (Table 2):**
  * Attention outputs alone (**Attn**) maintain high contextual mixing across datasets (**0.721 to 0.959**; e.g., Beauty = **0.776**, ML-1M = **0.856**, BeerAdvocate = **0.959**, Zvuk = **0.941**) [20].
  * Adding the residual connection (**+Res**) causes a sharp drop in mixing ratio to **0.116–0.395** (Beauty = **0.119**, Toys = **0.123**, ML-1M = **0.395**, Steam = **0.317**), proving that residual addition dominates representation structure [9, 20]. Layer normalization (**+LN**) produces almost no further change (Beauty = **0.119**, Toys = **0.123**, ML-1M = **0.386**) [20, 21].
* **Hit Rate of Last Item (HRLI@1 vs. HRL2I@1, Figure 2):**
  * Causal self-attention models show extreme last-item bias: SASRec HRLI@1 reaches **~0.78** (Beauty), **~0.91** (Sports), **~0.82** (Toys), **~0.81** (Zvuk), and **~0.50** (ML-1M), whereas HRL2I@1 is near zero [22].
  * BERT4Rec and GRU4Rec exhibit much lower HRLI@1 (**<0.10** across most datasets) with a minimal gap to HRL2I@1 [22].
* **Correct Non-Final Predictions among Final-Position Misses (Table 4):**
  * For sequences where final position \\(L\\) misses the target item, preceding representations (\\(L-1, L-2, L-3\\)) rank it in the Top-10 at substantial rates [44–45, 48–49]:
    * *Diginetica:* Standard \\(L\\) HR@10 = **0.2900**; \\(L-1\\) hit with \\(L\\) miss = **0.1153** (~**40%** of standard HR@10); \\(L-2\\) = **0.0782**; \\(L-3\\) = **0.0914** [48–49].
    * *ML-1M:* Standard \\(L\\) HR@10 = **0.1588**; \\(L-1\\) hit = **0.0347**; \\(L-2\\) hit = **0.0422**; \\(L-3\\) hit = **0.0298** [48–49].
    * *Zvuk:* Standard \\(L\\) HR@10 = **0.2416**; \\(L-1\\) hit = **0.0583**; \\(L-2\\) hit = **0.0415** [48–49].
    * *Toys:* Standard \\(L\\) HR@10 = **0.0574**; \\(L-1\\) hit = **0.0185** [48–49].
* **Recovery of Misses via Residual Scaling (Figure 5):**
  * Decreasing \\(\alpha\\) to **0.1–0.3** recovers **10% to 33%** of final-position missed sequences (peak recovery reaches ~**33%** on Diginetica, ~**28%** on ML-1M, ~**25%** on Video, and ~**18%** on Toys) [23, 24].

---

### **(6) Limitations, Failure Modes, or Negative Results**

1. **Not the Sole Cause of Recency Bias:** Residual dominance is an inference-time structural mechanism, not the exclusive origin of last-item reliance (causal masking, positional encodings, prediction heads, and training objectives also contribute) [7, 18].
2. **Accuracy–Reliance Trade-off:** Reducing residual strength (\\(\alpha < 1.0\\)) increases contextual mixing, but leads to an overall degradation in standard recommendation accuracy metrics (HR@10 and NDCG@10) [25].
3. **Inapplicability to Bidirectional Models:** The norm-based self-preservation decomposition does not translate directly to bidirectional models like BERT4Rec because BERT4Rec predicts from a virtual `[MASK]` token residual rather than an observed item embedding [26].
4. **Diagnostic Metric Limitations:** HRLI/HRL2I are recency-localized diagnostic metrics rather than replacements for accuracy metrics, and establishing their connection to online business utility remains an open problem [18, 27].
5. **Lack of Real-World Deployment:** Analysis is restricted to offline datasets; real-world production translation remains future work [18].

---

### **(7) Top 5–7 Most Heavily Cited Prior Works**

1. **Kang & McAuley (2018) [Ref 12]:** *Self-attentive sequential recommendation* (SASRec, IEEE ICDM) [28].
2. **Sun et al. (2019) [Ref 33]:** *BERT4Rec: Sequential recommendation with bidirectional encoder representations from transformer* (ACM CIKM) [29].
3. **Hidasi et al. (2015) [Ref 10]:** *Session-based recommendations with recurrent neural networks* (GRU4Rec) [30].
4. **Kobayashi et al. (2020, 2021) [Refs 15, 16]:** *Attention is not only a weight: analyzing transformers with vector norms* & *Incorporating residual and normalization layers into analysis of masked language models* (EMNLP) [31].
5. **Oh & Cho (2024) [Ref 23]:** *Measuring recency bias in sequential recommendation systems* (Introduced HRLI@K) [32].
6. **Vaswani et al. (2017) [Ref 36]:** *Attention is all you need* (NeurIPS) [33].
7. **Xu et al. (2026) [Ref 40]:** *Markovian pre-trained transformer for next-item recommendation* [34].

---

💡 *Would you like to explore how residual scaling (\\(\alpha\\)) or norm-based mixing ratios could be used as diagnostic tools to test whether your dating app's sequential candidate ranker over-indexes on recent profile swipes?*

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

### **Source Evaluation: *Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders***  
*(Kozaki et al., Hokkaido University, RecSys ’26, September 2026)* [1, 2]

---

### **(A) Q1 or Q2 or Both or Neither?**
* **Neither** [3, 4].
* **Explanation:**
  * **Q1 (Industry/Production Attribution 2025-01 to 2026-09):** **No.** This is an academic research paper from Hokkaido University published at RecSys ’26 [1, 2]. It investigates the internal representation mechanics of causal self-attention sequential recommenders (SASRec, DuoRec, BSARec) rather than an industry multi-touch attribution (MTA) ad/conversion measurement platform [3, 5, 6].
  * **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper studies next-item recommendation accuracy and recency bias (last-item reliance) in Transformer-based sequential recommenders [3, 4, 7]. It does not attribute overall user retention, active days, or revisitation across historical logs [3, 7].

---

### **(B) Q2 Class**
* **Classification:** **NOT** [2, 8, 29–30].
* **Justification:** The paper presents an analytical structural framework and diagnostic probe (inference-time residual scaling) to analyze how Transformer sequential recommenders process sequence positions [2, 9, 40–42]. It does **not** produce or publish a per-exposure retention credit table [3, 8].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **No per-interaction sequence attribution credit table** [3, 8].
* **Target Outcome:** **Next-Item Prediction Probability Distribution** over the catalog item set \\(V\\) (\\(p(v_{t+1} = v \mid S_u; \Theta)\\)) evaluated via full-catalog HR@10 and NDCG@10 [7, 9].
* **Mechanics:** The paper uses norm-based vector decomposition (\\(F_i(x_j)\\)) to measure the structural contribution of input position \\(j\\) to output representation \\(i\\) (computing mixing ratio \\(r_i\\)) for analytical representation diagnostics [29–30]. It does not output attribution credit for retention or conversion [3, 8].

---

### **(D) Replacing Last-Touch N7 → Latest Swipes**
* **How it Improves on Last-Touch:** While not a post-hoc attribution model, this paper provides a **structural explanation for why sequential recommendation models over-index on the most recent action** (last-item reliance) [3, 8, 10]. It reveals that while self-attention mechanisms aggregate contextual history, adding the **residual connection** sharply suppresses contextual mixing (mixing ratio drops from **0.72–0.96** down to **0.11–0.39**), causing predictions formed at the final position to be dominated by same-position residual information [8, 11, 12]. The paper introduces **inference-time residual scaling (\\(\alpha\\))** as a diagnostic probe (\\(h_i^{(\alpha)} = \alpha x_i + \text{Attn}(x)_i\\)), showing that reducing residual strength (\\(\alpha \in [0.1, 0.3]\\)) increases contextual mixing and recovers **10% to 33%** of final-position misses where preceding historical positions (\\(L-1, L-2, L-3\\)) already ranked the target item correctly [13-16].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *User Interaction Sequence (\\(S_u = (v_1, \dots, v_t)\\)):* Chronological history of user swipes, matches, and messages [7].
  2. *Final Position (\\(L = t\\)):* The most recent profile swipe or interaction [7, 17].
  3. *Residual Dominance Mechanism:* The residual connection preserves the raw embedding of the latest swipe at position \\(L\\), causing the ranker to anchor predictions on the last swipe rather than integrating deeper conversation and matching signals [8, 18, 19].
  4. *Inference-Time Residual Scaling Probe (\\(\alpha\\)):* Modulating \\(\alpha\\) reduces last-item preservation at prediction time, forcing the ranker to draw predictive signals from earlier swipes, matches, and conversations at non-final positions (\\(L-1, L-2, L-3\\)) [14-16].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Global Time Split (GTS) Protocol:** Eliminates temporal information leakage inherent in leave-one-out evaluation by strictly partitioning training/validation (90%) and test (10%) datasets chronologically using the GTS-Last strategy [20].
2. **5-Core Filtering & Consecutive-Repeat Removal:** Removes consecutive repeated item interactions within sequences to prevent artificial inflation of recency effects [5].
3. **Full-Catalog Ranking:** Ranks ground-truth items against the entire item set \\(V\\), avoiding sampling-based evaluation biases [9].
4. **Diagnostic Filter-Seen Bypass for HRLI@K:** For Hit Rate of the Last Item (HRLI@K) diagnostics, filter-seen is deliberately bypassed because filtering previously seen items would trivially prevent the last interacted item from appearing in recommendations [21]. For standard evaluation metrics (HR@10, NDCG@10), filter-seen is enforced (except on repeat-consumption datasets like Diginetica and Zvuk) [9].

---

### **(F) Deployed or Production Dataset Evidence**
* **Production Deployment:** **Not specified in source** for live deployment (*"understanding how these findings translate to real-world recommendation settings remains an important direction for future work"*) [22].
* **Quoted Dataset Statistics (Table 1):** Analyzed 9 public benchmark datasets under 5-core filtering [23]:
  * *Amazon Beauty:* 22,363 users, 12,101 items, 198,502 interactions (avg. length **8.9**, density **0.07%**) [23].
  * *Amazon Sports:* 35,598 users, 18,357 items, 296,337 interactions (avg. length **8.3**, density **0.05%**) [23].
  * *Amazon Video:* 24,303 users, 10,672 items, 231,780 interactions (avg. length **9.5**, density **0.09%**) [23].
  * *Diginetica:* 61,279 users, 25,593 items, 485,903 interactions (avg. length **7.9**, density **0.03%**) [23].
  * *Amazon Toys:* 19,412 users, 11,924 items, 167,597 interactions (avg. length **8.6**, density **0.07%**) [23].
  * *Steam:* 281,349 users, 11,961 items, 3,550,272 interactions (avg. length **12.6**, density **0.11%**) [23].
  * *BeerAdvocate:* 14,635 users, 22,074 items, 1,475,412 interactions (avg. length **100.8**, density **0.46%**) [23].
  * *MovieLens-1M (ML-1M):* 6,040 users, 3,416 items, 999,611 interactions (avg. length **165.5**, density **4.84%**) [23].
  * *Zvuk:* 19,267 users, 150,206 items, 8,087,953 interactions (avg. length **419.8**, density **0.28%**) [23].
* **Quoted Quantitative Results from Source:**
  * **Mixing Ratio (\\(r_i\\)) Drop across Block Stages (Table 2):**
    * *Attention output alone (`Attn`):* **0.776** (Beauty), **0.775** (Sports), **0.772** (Toys), **0.798** (Video), **0.721** (Diginetica), **0.856** (ML-1M), **0.794** (Steam), **0.959** (BeerAdvocate), **0.941** (Zvuk) [11].
    * *After residual addition (`+Res`):* Drops sharply to **0.119** (Beauty), **0.126** (Sports), **0.123** (Toys), **0.169** (Video), **0.150** (Diginetica), **0.395** (ML-1M), **0.317** (Steam), **0.301** (BeerAdvocate), **0.267** (Zvuk) [11].
    * *After layer normalization (`+LN`):* **0.119** (Beauty), **0.122** (Sports), **0.123** (Toys), **0.169** (Video), **0.149** (Diginetica), **0.386** (ML-1M), **0.276** (Steam), **0.287** (BeerAdvocate), **0.265** (Zvuk) [11].
  * **Last-Item Reliance (HRLI@1 vs. HRL2I@1, Figure 2):** SASRec HRLI@1 reaches **~0.78** (Beauty), **~0.91** (Sports), **~0.82** (Toys), **~0.81** (Zvuk), and **~0.50** (ML-1M), whereas HRL2I@1 is near zero [24].
  * **Preceding Position Correct Hits on Final-Position Misses (Table 4):**
    * *Diginetica:* Standard \\(L\\) HR@10 = **0.2900**; \\(L-1\\) hit with \\(L\\) miss = **0.1153** (~**40%** of standard HR@10); \\(L-2\\) hit = **0.0782**; \\(L-3\\) hit = **0.0914** [25].
    * *ML-1M:* Standard \\(L\\) HR@10 = **0.1588**; \\(L-1\\) hit = **0.0347**; \\(L-2\\) hit = **0.0422**; \\(L-3\\) hit = **0.0298** [25].
    * *Zvuk:* Standard \\(L\\) HR@10 = **0.2416**; \\(L-1\\) hit = **0.0583**; \\(L-2\\) hit = **0.0415** [25].
    * *Toys:* Standard \\(L\\) HR@10 = **0.0574**; \\(L-1\\) hit = **0.0185** [25].
  * **Recovery of Final-Position Misses (Figure 5):** Residual scaling at \\(\alpha \approx 0.1\text{--}0.3\\) recovers **10% to 33%** of final-position missed sequences across datasets (peaking at ~**33%** on Diginetica, ~**28%** on ML-1M, ~**25%** on Video, ~**18%** on Toys) [16].

---

💡 *Would you like to explore how norm-based mixing ratio analyses or residual scaling probes (\\(\alpha\\)) could be used to diagnose last-swipe bias in your dating app's candidate ranker?*

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
**Priority:** see queue.md `G29`
