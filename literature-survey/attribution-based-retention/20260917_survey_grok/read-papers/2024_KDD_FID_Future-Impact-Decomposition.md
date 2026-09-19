# **Part 1: Dating App Retention Project Evaluation**

**Source:** https://arxiv.org/pdf/2401.16108.pdf  
**Date analyzed:** 2026-09-18  
**NLM source id:** `088b1ae5-f3f7-4ccc-88db-d6e8408e50f1`  
**Queue id:** G4  
**Q2 class:** NOT

---

## 1. Summary

### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Answer:** **Neither Q1 nor Q2** [1, 6–7].
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), falling outside the 2025–2026 window [6–7].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on reinforcement learning (RL) policy optimization for list-wise recommendations rather than multi-touch causal attribution over historical user journey logs [8–12, 18].

---

#### **(B) Q2 Classification**
* **Classification:** **NOT** [15, 21–23, 31–36].
* **Justification:** The paper presents an RL actor-critic policy optimization method (**ItemA2C**) that decomposes list-level future value \\(V(s_{t+1})\\) down to individual items for policy gradient updates, rather than publishing an explicit per-exposure retention credit table or multi-touch attribution model [15–18, 35–41].

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (in the form of an RL item-level advantage score)** [1-3]. 
* **Target Outcome & Formula:** Allocates cumulative session rewards and long-term state value \\(V(s_{t+1})\\) (which correlates with 7-day retention) to individual items \\(i_{t,k}\\) in list \\(a_t\\) via item target value \\(\Psi_w\\) and advantage \\(A\\):
  \\[\Psi_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} \gamma (1-d) V(s_{t+1})\\]
  \\[A(s_t, i_{t,k}, w_{t,k}) = \Psi_w(s_t, i_{t,k}) - \frac{V(s_t)}{K}\\]
  where \\(r_{t,k}\\) is the immediate item reward, \\(V(s_{t+1})\\) is the estimated future state value, and \\(w_{t,k}\\) is a reward-based or model-based item weight (\\(\sum_{k=1}^K w_{t,k} = 1\\)) [36, 39, 41, 47–48].

---

#### **(D) Improving on Last-Touch N7 → Latest Swipes**
* **How it Improves Last-Touch:** Last-touch assigns binary N7 labels exclusively to the most recent swipes, ignoring earlier swipes and intermediate value creation. **ItemA2C** provides a mathematically grounded RL framework to decompose long-term value \\(V(s_{t+1})\\) (which directly drives N7 retention) across all candidate recommendations in a session based on immediate engagement signals \\(r_{t,k}\\) and learned future impact weights \\(w_{t,k}\\) [15, 36–39].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Immediate Item Reward (\\(r_{t,k}\\)):* Formulated as a weighted sum of immediate candidate interaction events:
     \\[r(s_t, \text{candidate}_k) = w_1 \cdot \mathbb{1}[\text{swipe\_right}] + w_2 \cdot \mathbb{1}[\text{match}] + w_3 \cdot \mathbb{1}[\text{4-way\_conversation}]\\]
  2. *Value Function (\\(V(s_{t+1})\\)):* Estimates the user's expected cumulative long-term engagement / retention probability given their updated profile state \\(s_{t+1}\\) after the swiping session [31–32].
  3. *Item Credit Allocation (\\(w_{t,k}\\)):* Uses reward-based weighting (\\(w_{t,k} = r_{t,k} / R\\)) or adversarial model-based weighting (\\(w_{t,k} = w(i_{t,k}, s_t, s_{t+1}, r_{t,k})\\)) to assign fractional credit for \\(V(s_{t+1})\\) to each candidate profile shown [39, 43–45].

---

#### **(E) Selection-Bias & Confounding Handling**
1. **Critic Baseline Subtraction (Advantage Formulation):** Subtracts the mean expected state baseline \\(V(s_t)/K\\) from the item target value \\(\Psi_w(s_t, i_{t,k})\\) to compute the item advantage \\(A(s_t, i_{t,k}, w_{t,k})\\), preventing naturally hyper-active users (who have high baseline \\(V(s_t)\\)) from inflating individual item scores [3, 4].
2. **Quantile Normalization:** Uses quantile-based discretization for continuous engagement signals (e.g., watch time) to prevent extreme outlier sessions from skewing reward distributions [5].

---

#### **(F) Deployment and Dataset Evidence**
* **Datasets & Deployment:** Evaluated offline on MovieLens-1M (ML1M), KuaiRand1K, and the KuaiSim simulator [50–52]. Deployed live in the **refined ranking stage** (ranking ~500 candidates down to \\(K=6\\)) of Kuaishou's short-video platform serving **over 100 million Daily Active Users (DAU)** [75–78, 81].
* **Quoted Quantitative Results:**
  * **Offline Simulator (KuaiRand1K, \\(K=6\\), Table 1):** `ItemA2C-M` achieved **Total Reward = 16.03 ± 0.53** and **Depth = 16.59 ± 0.45** vs. standard request-level `A2C` (**10.01 ± 0.86 / 11.56 ± 0.72**) and state-of-the-art `HAC` (**12.65 ± 0.26 / 13.72 ± 0.22**), representing a **+26.7% reward increase** (\\(p < 0.05\\)) [55–56, 64].
  * **Live Production A/B Test (Table 3, 100M+ DAU Platform):**
    * *`ItemA2C` vs. `request-level A2C`:* **+0.129% Watch Time**, **+1.103% Like Rate**, **+0.300% Follow Rate**, **+0.963% Collect Rate**, **+0.221% Comment Rate** (\\(p < 0.05\\)) [6].
    * *`ItemA2C-W (\alpha=1)` vs. `ItemA2C`:* Additional **+0.451% Like Rate**, **+0.636% Follow Rate**, **+0.616% Collect Rate**, **+0.258% Comment Rate** [6].
    * *Macro Platform Impact:* Generated a **+0.028% increase in Daily Active Users (DAU)** and a **+0.016% increase in 7-day User Retention** [7].

---

### **Part 2: Detailed Technical Breakdown of the Source**

#### **(1) Title, Authors, Affiliations, Year, Venue**
* **Full Title:** *Future Impact Decomposition in Request-level Recommendations* [8, 9]
* **Authors:** **Xiaobei Wang**\*†, **Shuchang Liu**\*, **Xueliang Wang**, **Qingpeng Cai**‡, **Lantao Hu**, **Han Li**, **Peng Jiang**‡, **Kun Gai**, and **Guangming Xie**‡ (\*Equal contribution; †Work done during internship at Kuaishou; ‡Corresponding authors) [8, 9]
* **Author Affiliations:**
  1. **Peking University**, Beijing, China (`wangxiaobei@stu.pku.edu.cn`, `xiegming@pku.edu.cn`) [1–2]
  2. **Kuaishou Technology**, Beijing, China (`{liushuchang, wangxueliang03, caiqingpeng, hulantao, lihan08, jiangpeng}@kuaishou.com`) [1–2]
  3. **Unaffiliated**, Beijing, China (`gai.kun@qq.com`) [10]
* **Year & Venue:** Published in **2024** at the *30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24), August 25–29, 2024, Barcelona, Spain* [6–7].

---

#### **(2) Core Problem and Key Contribution**
* **Core Problem:** In recommender systems, reinforcement learning (RL) policies typically recommend a *list* of \\(K\\) items per request to efficiently process continuous user browsing [2–3, 10]. In the corresponding Markov Decision Process (MDP), user state transitions are updated at the *request level* [3, 11–12]. However, this list-wise mechanism is fundamentally inconsistent with individual user behaviors (users pay attention to one item at a time, and state transitions occur per item) [11, 12]. Standard request-level RL methods optimize cumulative list-wise rewards, inducing severe information loss on item characteristics and failing to distribute an item's future impact properly [1, 13].
* **Key Contributions:**
  1. **Request-Level MDP with Item-Wise Rewards:** Formulates a practical request-level MDP framework where state transitions occur per request but item-level immediate rewards are observable [12–13, 18, 27–31].
  2. **ItemA2C Framework:** Proposes an item-decomposed advantage actor-critic framework (**ItemA2C**) that decomposes both temporal difference (TD) critic targets and actor advantage objectives into item-level optimizations [15, 35–37].
  3. **Future Impact Reweighting:** Introduces heuristic **reward-based re-weighting** (`itemA2C-W`) and **model-based adversarial re-weighting** (`itemA2C-M`) to allocate long-term future value \\(V(s_{t+1})\\) across individual items in a list rather than splitting it uniformly [16–18, 38–46].
  4. **Mathematical Consistency:** Proves that the item-wise target function sums up to reconstruct the original request-level TD target (\\(\sum_{k=1}^K \Psi_w(s_t, i_{t,k}) = \Psi(s_t, a_t)\\)), ensuring theoretical consistency [18, 47–48].

---

#### **(3) Proposed Method or Architecture in Detail**
* **MDP Formulation:** Action \\(a_t = [i_{t,1}, \dots, i_{t,K}] \in \mathcal{I}^K\\). Immediate list reward \\(R(s_t, a_t) = \sum_{k=1}^K r_{t,k}\\) where item rewards \\(r_{t,k} = r(s_t, i_{t,k})\\) are observable [28–29].
* **Decomposed Item Target Function:**
  \\[\Psi_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} \gamma (1-d) V(s_{t+1})\\]
  where \\(w_{t,k}\\) determines how the future state value \\(V(s_{t+1})\\) is allocated across items in the list [2, 14].
* **Reweighting Schemes (\\(w_{t,k}\\)):**
  * *Equal-Weight Decomposition (`itemA2C`, \\(\alpha=0\\)):* \\(w_{t,k} = 1/K\\) [2, 14].
  * *Reward-Based Strategy (`itemA2C-W`):* \\(w_{t,k} = \frac{\alpha r_{t,k} + (1-\alpha)}{\alpha R(s_t, a_t) + (1-\alpha)K}\\). Setting \\(\alpha=1.0\\) yields pure reward-proportional weights \\(w_{t,k} = r_{t,k} / R(s_t, a_t)\\) [39–40].
  * *Model-Based Adversarial Strategy (`itemA2C-M`):* Paramterizes weights as a neural network \\(w_{t,k} = w(i_{t,k}, s_t, s_{t+1}, r_{t,k})\\) with softmax output across the list [43–44]. Trained via an adversarial objective \\(\mathcal{L}_{weight} = -\sum_{k=1}^K \mathcal{L}_{actor}(i_{t,k})\\), forcing the actor to learn from "harder" item decompositions [45–46].
* **Actor Loss Function:**
  \\[\mathcal{L}_{actor}(i_{t,k}) = -A(s_t, i_{t,k}, w_{t,k}) \log \pi_\theta(i_{t,k} | s_t)\\]
  \\[A(s_t, i_{t,k}, w_{t,k}) = \Psi_w(s_t, i_{t,k}) - \frac{V(s_t)}{K}\\]
* **Credit Assignment Mechanics:** Assigns credit to individual items \\(i_{t,k}\\) within a list/request \\(a_t\\) by splitting both immediate reward \\(r_{t,k}\\) and weighted long-term future value \\(w_{t,k} V(s_{t+1})\\). This evaluates each item's individual contribution to both short-term feedback and long-term user retention [2, 3, 14].

---

#### **(4) Datasets, Production Deployment, and Comparison Baselines**
* **Datasets:**
  * **MovieLens-1M (ML1M):** 10-core filtered movie ratings dataset [15].
  * **KuaiRand1K:** Unbiased sequential short-video dataset [15].
  * **KuaiSim:** Session-based user simulator environment [16, 17].
* **Production Deployment:** Deployed in the **refined ranking stage** (ranking ~500 candidates down to list size \\(K=6\\)) of Kuaishou's short-video platform serving **100+ million Daily Active Users (DAU)** [75–78, 81].
* **Comparison Baselines:**
  * *Request-level RL:* DDPG (continuous vector hyper-actions), A2C (standard list-level A2C), HAC (Hyper-Action Representation + Actor-Critic) [55–58].
  * *Supervised Learning:* SASRec Transformer encoder + BCE loss [18, 19].
  * *Item-decomposed RL:* SlateQ (DQN slate decomposition under single-choice assumption) [18, 20, 21].

---

#### **(5) Key Quantitative Results with Numbers**
* **Offline Simulator Performance (KuaiRand1K, \\(K=6\\), Table 1):**
  * `itemA2C-M` achieved **Total Reward = 16.03 ± 0.53** and **Depth = 16.59 ± 0.45** vs. standard request-level `A2C` (**10.01 ± 0.86 / 11.56 ± 0.72**) and `HAC` (**12.65 ± 0.26 / 13.72 ± 0.22**), representing a **+26.7% reward gain** (\\(p < 0.05\\)) [55–56, 64].
  * `itemA2C-W (\alpha=1)` achieved **15.48 ± 0.61 Reward**; `itemA2C (\alpha=0)` achieved **13.45 ± 0.08 Reward** [22].
* **Offline Simulator Performance (ML1M, \\(K=6\\), Table 1):**
  * `itemA2C-M` achieved **Total Reward = 17.94 ± 0.47** and **Depth = 18.24 ± 0.40** vs. `HAC` (**17.53 ± 0.13 / 17.90 ± 0.12**) and `A2C` (**16.88 ± 0.58 / 17.32 ± 0.50**) [54–55].
* **Live Online A/B Test (Table 3, 100M+ DAU Short-Video Platform):**
  * *`ItemA2C` vs. `request-level A2C`:* **+0.129% Watch Time**, **+1.103% Like Rate**, **+0.300% Follow Rate**, **+0.963% Collect Rate**, **+0.221% Comment Rate** (\\(p < 0.05\\)) [6].
  * *`ItemA2C-W (\alpha=1)` vs. `ItemA2C`:* Additional **+0.451% Like Rate**, **+0.636% Follow Rate**, **+0.616% Collect Rate**, **+0.258% Comment Rate** [6].
  * *Macro Platform Metrics:* Driven a **+0.028% increase in Daily Active Users (DAU)** and a **+0.016% increase in 7-day User Retention** [7].

---

#### **(6) Limitations, Failure Modes, or Negative Results**
1. **SlateQ Failure under Multi-Interaction:** SlateQ performs poorly (Total Reward 3.39 on KuaiRand vs 16.03 for `itemA2C-M`) because its "single-choice" assumption fails when users engage with multiple items in a list [20, 22, 23].
2. **List Size Degradation:** As list size \\(K\\) increases (\\(K \in \{1, 2, 4, 6, 8, 16, 32\}\\)), performance of all methods gradually deteriorates (e.g., `itemA2C-M` reward drops from 16.93 at \\(K=1\\) to 11.39 at \\(K=32\\) on KuaiRand), confirming the growing mismatch between request-level MDPs and item-level user attention [24, 25].
3. **Model-Based Reweighting Training Overhead:** `itemA2C-M` introduces additional adversarial modeling and training overhead during offline policy learning (though zero extra compute during online inference) [84–85].
4. **Dependence on Linear Reward Additivity:** Assumes list-wise immediate reward is a linear sum of item-wise rewards (\\(R = \sum r\\)), which does not account for complex non-linear intra-list effects such as diversity [26, 27].
5. **Inability to Directly Serve Early Retrieval Stages:** Suited for refined ranking or re-ranking stages (\\(K\\) small); accommodating early retrieval/pre-ranking where candidate pools are huge and output size is not \\(K\\) requires additional modifications [81, 86–87].

---

#### **(7) Top 5–7 Most Heavily Cited Prior Works**
1. **Ie et al. (2019) [SlateQ]:** *SlateQ: A Tractable Decomposition for Reinforcement Learning with Recommendation Sets* (IJCAI '19) [20, 28].
2. **Liu et al. (2023) [HAC]:** *Exploration and Regularization of the Latent Action Space in Recommendation* (WWW '23) [29, 30].
3. **Cai et al. (2023) [Two-Stage Constrained Actor-Critic / Retention RL]:** *Reinforcing User Retention in a Billion Scale Short Video Recommender System* & *Two-Stage Constrained Actor-Critic for Short Video Recommendation* (WWW '23) [9, 31-33].
4. **Mnih et al. (2016) [A2C / Asynchronous Actor-Critic]:** *Asynchronous methods for deep reinforcement learning* (ICML '16) [34, 35].
5. **Lillicrap et al. (2016) [DDPG]:** *Continuous control with deep reinforcement learning* (ICLR '16) [36, 37].
6. **Zhao et al. (2023) [KuaiSim] & Gao et al. (2022) [KuaiRand]:** *KuaiSim: A comprehensive simulator for recommender systems* & *KuaiRand: An Unbiased Sequential Recommendation Dataset* [16, 38-40].
7. **Kang & McAuley (2018) [SASRec]:** *Self-attentive sequential recommendation* (ICDM '18) [19].

---

💡 *Would you like to explore how to adapt ItemA2C's advantage formulation or adversarial future-impact reweighting (\\(w_{t,k}\\)) to construct an N7 retention ranking pipeline for your dating platform?*

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

### **Source Evaluation: ItemA2C (*Future Impact Decomposition in Request-level Recommendations*)**
*(Wang et al., Peking University & Kuaishou Technology, KDD 2024: `arxiv:2401.16108`)* [1, 6–7]

---

### **(A) Query Categorization: Q1 vs. Q2**
* **Answer:** **Neither Q1 nor Q2.**
* **Explanation:** 
  * *Q1 (Industry Attribution 2025–2026):* Published in August 2024 (KDD ’24), which falls outside the specified 2025–2026 timeframe [6–7].
  * *Q2 (Interaction-Level Retention Attribution):* Focuses on reinforcement learning (RL) policy optimization for list-wise recommendations rather than multi-touch causal sequence attribution over historical user journey logs [8–12, 18].

---

### **(B) Q2 Class**
* **Classification:** **NOT**
* **Justification:** The paper presents an RL actor-critic policy optimization method (**ItemA2C**) that decomposes list-level future value \\(V(s_{t+1})\\) down to individual items for policy gradient updates, rather than publishing an explicit per-exposure retention credit table or multi-touch attribution model [15–18, 35–41].

---

### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes (in the form of an RL item-level advantage score)** [39–41].
* **Target Outcome & Formula:** Allocates cumulative session rewards \\(R(s_t, a_t) = \sum r_{t,k}\\) and long-term state value \\(V(s_{t+1})\\) (which drives user retention) to individual items \\(i_{t,k}\\) in list \\(a_t\\) via item target value \\(\Psi_w\\) and advantage \\(A\\) [1-4]:
  \\[\Psi_w(s_t, i_{t,k}) = r_{t,k} + w_{t,k} \gamma (1-d) V(s_{t+1}) \quad [3]\\]
  \\[A(s_t, i_{t,k}, w_{t,k}) = \Psi_w(s_t, i_{t,k}) - \frac{V(s_t)}{K} \quad [4]\\]
  where \\(r_{t,k}\\) is the immediate item reward, \\(V(s_{t+1})\\) is the estimated future state value, and \\(w_{t,k}\\) is a reward-based or model-based item weight (\\(\sum_{k=1}^K w_{t,k} = 1\\)) [36, 39, 43–44, 47].

---

### **(D) Application to Dating Platform Retention (Replacing Last-Touch N7)**
* **How it Improves Last-Touch:** Last-touch assigns binary N7 retention labels exclusively to the most recent swipes, ignoring earlier swipes and intermediate value creation. **ItemA2C** provides a mathematically grounded RL framework to decompose long-term value \\(V(s_{t+1})\\) (which directly drives N7 retention) across all candidate recommendations in a swiping session based on immediate engagement signals \\(r_{t,k}\\) and learned future impact weights \\(w_{t,k}\\) [15, 36–39].
* **Dating Platform Mapping (Swipe / Match / Conversation):**
  1. *Immediate Item Reward (\\(r_{t,k}\\)):* Formulated as a weighted sum of immediate candidate interaction events [76–77]:
     \\[r(s_t, \text{candidate}_k) = w_1 \cdot \mathbb{1}[\text{swipe\_right}] + w_2 \cdot \mathbb{1}[\text{match}] + w_3 \cdot \mathbb{1}[\text{4-way\_conversation}] \quad [5]\\]
  2. *Value Function (\\(V(s_{t+1})\\)):* Estimates the user's expected cumulative long-term engagement and retention probability given their updated profile state \\(s_{t+1}\\) after the swiping session [31–32].
  3. *Item Credit Allocation (\\(w_{t,k}\\)):* Uses reward-based weighting (\\(w_{t,k} = r_{t,k} / R\\)) or adversarial model-based weighting (\\(w_{t,k} = w(i_{t,k}, s_t, s_{t+1}, r_{t,k})\\)) to assign fractional credit for \\(V(s_{t+1})\\) to each candidate profile shown [39, 43–45].

---

### **(E) Selection-Bias & Confounding Handling**
1. **Critic Baseline Subtraction (Advantage Formulation):** Subtracts the mean expected state baseline \\(V(s_t)/K\\) from the item target value \\(\Psi_w(s_t, i_{t,k})\\) to compute the item advantage \\(A(s_t, i_{t,k}, w_{t,k})\\), preventing naturally hyper-active users (who have high baseline \\(V(s_t)\\)) from artificially inflating individual item scores [4].
2. **Quantile Normalization:** Uses quantile-based discretization for continuous engagement signals (e.g., watch time) to prevent extreme outlier sessions from skewing reward distributions [5].

---

### **(F) Deployment and Dataset Evidence**
* **Production Deployment:** Deployed in the **refined ranking stage** (ranking ~500 candidates down to list size \\(K=6\\)) of Kuaishou's short-video platform serving **over 100 million Daily Active Users (DAU)** [75–78, 81].
* **Datasets:** Evaluated offline on **MovieLens-1M (ML1M)**, **KuaiRand1K**, and the **KuaiSim** simulator [50–52].
* **Quoted Quantitative Results:**
  * **Offline Simulator (KuaiRand1K, \\(K=6\\), Table 1):** `ItemA2C-M` achieved **Total Reward = 16.03 ± 0.53** and **Depth = 16.59 ± 0.45** vs. standard request-level `A2C` (**10.01 ± 0.86 / 11.56 ± 0.72**) and state-of-the-art `HAC` (**12.65 ± 0.26 / 13.72 ± 0.22**), representing a **+26.7% reward increase** (\\(p < 0.05\\)) [55–56, 64].
  * **Live Online A/B Test (Table 3, 100M+ DAU Platform):**
    * *`ItemA2C` vs. `request-level A2C`:* **+0.129% Watch Time**, **+1.103% Like Rate**, **+0.300% Follow Rate**, **+0.963% Collect Rate**, **+0.221% Comment Rate** (\\(p < 0.05\\)) [6].
    * *`ItemA2C-W (\alpha=1)` vs. `ItemA2C`:* Additional **+0.451% Like Rate**, **+0.636% Follow Rate**, **+0.616% Collect Rate**, **+0.258% Comment Rate** [6].
    * *Macro Platform Metrics:* Generated a **+0.028% increase in Daily Active Users (DAU)** and a **+0.016% increase in 7-day User Retention** [7].

---

💡 *Would you like to explore how ItemA2C's advantage formulation or adversarial future-impact reweighting (\\(w_{t,k}\\)) can be adapted to structure per-swipe retention credit labels for your ranking pipeline?*

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
**Priority:** see queue.md `G4`
