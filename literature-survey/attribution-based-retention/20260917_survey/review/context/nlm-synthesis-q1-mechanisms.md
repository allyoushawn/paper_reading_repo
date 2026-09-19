# NotebookLM synthesis query 1 — retention credit mechanisms (2026-09-17)

Scope: 43 new sources + 5 parent anchors. Query: which sources assign credit for a retention / return / long-term engagement outcome to individual interactions; grouped by mechanism.

### **1. Counterfactual Removal / Deletion Credit**
* **ALM-MTA** (*Kuaishou Technology & Univ. of Auckland*) [1]:
  * **Unit of Credit:** Individual consumed video touchpoint in a user consumption sequence [2].
  * **Outcome:** Creator content upload probability [2, 3].
  * **Production Evidence:** **Yes** (Live A/B test on 400M DAU: +0.04% DAU, +0.6% daily active creators) [1].

---

### **2. RL or Flow-Based Backward Credit Assignment**
* **GFN4Retention** (*City Univ. of Hong Kong & Kuaishou*) [4]:
  * **Unit of Credit:** Individual recommended item list per request step in a session [5, 6].
  * **Outcome:** End-of-session retention reward & return time gap [5, 7, 8].
  * **Production Evidence:** **Yes** (Live A/B test on Kuaishou: statistically significant reduction in return time gap) [8].
* **RLUR** (*Kuaishou Technology*) [9]:
  * **Unit of Credit:** Individual recommendation request action [10, 11].
  * **Outcome:** Cumulative returning time interval & 1st/7th-day retention (DAU) [10-12].
  * **Production Evidence:** **Yes** (Live A/B test on Kuaishou: +0.450% app open frequency, +0.200% DAU, +0.063% 7th-day retention) [10].
* **IURO** (*WeChat / Tencent & Northeastern Univ.*) [13]:
  * **Unit of Credit:** Individual interacted item / historical behavior [14, 15].
  * **Outcome:** Next-day and next-three-day user retention [15, 16].
  * **Production Evidence:** **Yes** (Live A/B test on WeChat article feed: +0.76% next-day retention, +0.65% next-three-day retention) [16].

---

### **3. Surrogate-Index or Long-Term-Value Prediction Per Item**
* **Downstream Rewards (DR)** (*Pinterest*) [17]:
  * **Unit of Credit:** Individual recommended candidate Pin impression [18, 19].
  * **Outcome:** Long-term retention (DAU/WAU/MAU, Successful Sessions, Total Time Spent) [18, 20, 21].
  * **Production Evidence:** **Yes** (Live A/B tests across Pinterest Homefeed, Search, Notifications: +0.36% Successful Sessions, +0.35% Time Spent, +0.11% WAU) [21-23].
* **Retentive Relevance** (*Meta*) [24]:
  * **Unit of Credit:** Individual user-item recommendation pair [24-26].
  * **Outcome:** Next-day user retention and live Sessions per User [24, 27, 28].
  * **Production Evidence:** **Yes** (Live 14-day A/B test on Meta video feed: +0.030% Sessions per User) [28, 29].
* **Impatient Bandits** (*Spotify / Univ. of Manchester / Columbia Univ.*) [30]:
  * **Unit of Credit:** Individual candidate show / item discovery action [30, 31].
  * **Outcome:** 60-day cumulative active days ("stickiness") [31].
  * **Production Evidence:** **No** (Offline evaluation on 8.77M Spotify interaction traces).

---

### **4. Per-Action Uplift or CATE**
* **CDUM** (*Kuaishou Technology & Tsinghua Univ.*) [32]:
  * **Unit of Credit:** Individual user request strategy decision [33, 34].
  * **Outcome:** Unbiased 7-day active retention (Enter LT7 / Slide LT7) and app usage time [33-35].
  * **Production Evidence:** **Yes** (Live A/B test on Kuaishou: +0.048% Enter LT7, +0.034% next-day retention, +0.135% app usage time) [34, 35].
* **HMUM** (*Kuaishou Technology & Tsinghua Univ.*) [36]:
  * **Unit of Credit:** Individual user request multi-strategy enablement [37, 38].
  * **Outcome:** App usage time and video view counts [37, 39].
  * **Production Evidence:** **Yes** (Live A/B test on Kuaishou: +0.044% to +0.073% app usage time) [39].
* **Instagram Notification Management** (*Meta / Instagram*) [40, 41]:
  * **Unit of Credit:** Individual daily digest push notification candidate [41-43].
  * **Outcome:** User return vs. organic story views [41, 43].
  * **Production Evidence:** **Yes** (Live deployment on Instagram reducing push volume while preserving user activity) [41].

---

### **5. Retention-Curve Marginal Gain Per Match**
* **MRet** (*Hanjuku-kaso Co., Ltd.*) [44]:
  * **Unit of Credit:** Individual recommended user profile / match [44-46].
  * **Outcome:** User retention rate / login continuation rate [44, 46, 47].
  * **Production Evidence:** **No** (Offline simulation on real-world dating platform dataset of 2,000 users / 60,000 records) [48, 49].
* **Retention-Focused Recommendation** (*Wantedly, Inc. & Hanjuku-kaso Co., Ltd.*) [50]:
  * **Unit of Credit:** Individual candidate profile recommendation / scout [50-52].
  * **Outcome:** User churn / 30-day user retention [50, 51, 53].
  * **Production Evidence:** **Yes** (Live A/B experiment on Wantedly job-matching platform: odds ratio 0.948–0.957 for user churn) [50, 53].

---

### **Production Evidence Summary**
**Surrogate-index/long-term-value prediction per item** (Pinterest DR, Meta Retentive Relevance) and **RL/flow-based backward credit assignment** (Kuaishou RLUR, GFN4Retention, WeChat IURO) possess the strongest production evidence, with fully deployed live A/B experiments across hundreds of millions of daily active users demonstrating statistically significant lifts in active user retention and long-term engagement metrics [8, 10, 16, 18, 28].

---

💡 *Would you like to generate a comparative analysis or slide deck contrasting these five mechanisms for per-swipe retention attribution on your dating platform?*