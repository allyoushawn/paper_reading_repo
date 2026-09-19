# Compact card summaries — truncated Summary + Evidence from this-run cards (2/2)

### AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems [1, 2]
`2025_WWW_AURO_Adaptive-User-Retention-Optimization.md`
**Source:** https://arxiv.org/pdf/2310.03984.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *AURO: Reinforcement Learning for Adaptive User Retention Optimization in Recommender Systems* [1, 2]
* **Authors:** **Zhenghai Xue**¹, **Qingpeng Cai**\*², **Bin Yang**², **Lantao Hu**², **Peng Jiang**², **Kun Gai**³, and **Bo An**¹ (*\*Corresponding author*) [1, 3]
* **Author Affiliations:**
  1. **Nanyang Technological University**, Singapore / Skywork AI [1–2]
  2. **Kuaishou Technology**, Beijing, China [1]
  3. **Unaffiliated**, Beijing, China [1]
* **Year:** **2025** (Published at WWW ’25; arXiv pre-print `arXiv:2310.03984`) [3–4]
* **Venue:** *Proceedings of the ACM Web Conference 2025 (WWW ’25)*, April 28–May 2, 2025, Sydney, NSW, Australia [3–4]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Standard Reinforcement Learning (RL) algorithms for user retention struggle with environment non-stationarity driven by shifting user behavior patterns (such as fluctuating interaction rates and user return time distributions) [2, 4]. Shifting environments cause policy performance degradation, while "implicit cold-start" scenarios force policies to continually interact with users exhibiting novel behaviors [4, 5].
* **Key Contributions:**
  1. **Value-Based State Abstraction Module:** Introduces a state abstraction module in the policy network trained with a value-based
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems [1]
`2026_AAAI_RevisitMTL_Save-Revisit-Retain.md`
**Source:** https://arxiv.org/pdf/2511.18013.pdf  
**Q2 class:** PARTIAL

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Save, Revisit, Retain: A Scalable Framework for Enhancing User Retention in Large-Scale Recommender Systems* [1]
* **Authors:** **Weijie Jiang**, **Armando Ordorica**, **Jaewon Yang**, **Olafur Gudmundsson**, **Yucheng Tu**\*, and **Huizhong Duan** (\*Work done at Pinterest) [1, 2]
* **Affiliations:** **Pinterest Inc.** [1]
* **Year:** **2026** (submitted Nov 2025, Copyright © 2026 AAAI) [1, 2]
* **Venue:** *Proceedings of the AAAI Conference on Artificial Intelligence (AAAI '26)* / arXiv pre-print (`arXiv:2511.18013`) [1, 2]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Optimizing long-term user revisitation (returning to view previously saved content) to drive platform retention faces two major challenges:
  1. *Attribution Noise & Confounding:* Unclear causal links between initial candidate exposures/saves and delayed return visits due to confounding factors like changing user intent, platform notifications, or UI layout [1, 3].
  2. *Scalability Bottleneck:* Tracking cross-session revisitations occurring days or weeks later requires maintaining and joining massive activity logs across millions of users and surfaces, creating heavy computational and serving latency overhead [1, 3].
* **Key Contributions:**
  1. **Surrogate Attribution Framework:** Establishes
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?
`2026_CIKM_LOTUS_Meaningful-Touchpoints-Conversion-Attribution.md`
**Source:** https://arxiv.org/pdf/2608.28649.pdf  
**Q2 class:** NOT

**Summary.** Here is the detailed breakdown for the paper **"Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?"** (from source `https://arxiv.org/pdf/2608.28649.pdf`).

---

### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Can Large Language Models Identify Meaningful Touchpoints in Conversion Attribution?*
* **Authors:** **Jinqi Wu**\*¹, **Sishuo Chen**\*², **Zhangming Chan**², **Yong Bai**², **Chao Yi**², **Han Zhu**², **Shuodian Yu**², **Lei Zhang**², **Sheng Chen**², **Chenghuan Hou**², **Jian Xu**†², and **Chaoyou Fu**¹ (*Co-first authors, †Corresponding author)
* **Author Affiliations:**
  1. **State Key Laboratory for Novel Software Technology, Nanjing University**, Nanjing, China & **School of Intelligence Science and Technology, Nanjing University**, Suzhou, China (`jinqiwu001@gmail.com`, `bradyfu24@gmail.com`)
  2. **Taobao & Tmall Group of Alibaba**, Beijing, China (`{chensishuo, zhangming.czm, baiyong.by, yunan.yc, zhuhan.zh, yushuodian.ysd, zl165646, chensheng.cs, jinyao, xiyu.xj}@alibaba-inc.com`)
* **Year:** 2026
* **Venue:** *Proceedings of the 35th ACM International Conference on Information and Knowledge Management (CIKM ’26), November 07–11, 2026, Rome, Italy*

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Standard conversion attribution relies on heuristic, rule-based
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### ALM-MTA: Front-Door Causal Multi-Touch Attribution Method for Creator-Ecosystem Optimization [1]
`2026_ICLR_ALM-MTA_Front-Door-Causal-Multi-Touch-Attribution.md`
**Source:** https://arxiv.org/pdf/2605.08881.pdf  
**Q2 class:** NOT

**Summary.** ### **Part 1: Dating App Retention Project Evaluation**

#### **(A) Alignment: Q1 or Q2 or Both or Neither?**
* **Q1 (Industry/Production Attribution 2025–2026):** **Yes.** Published in May 2026 (`arXiv:2605.08881`), this paper describes a production causal Multi-Touch Attribution (MTA) system deployed at Kuaishou Technology on a recommendation engine serving **400 million Daily Active Users (DAU)** and evaluated over **30 billion training samples** [1-3].
* **Q2 (Attributing Retention / Engagement / Days-Active to Individual Interactions):** **No.** The paper attributes user content consumption touchpoints to **content creation / video upload behavior (\\(Y \in \{0, 1\}\\))** (the Consumption Drives Production / CDP ecosystem), rather than user retention, active days, or return visits [1, 3, 4].
* **Summary:** **Q1 only.**

---

#### **(B) Q2 Class**
* **Classification:** **NOT** [1, 3, 4].
* **Justification:** The system computes causal multi-touch attribution credit for content creation / video upload conversion events (\\(Y\\)), not for user retention or active days.

---

#### **(C) Per-Interaction Credit & Target Outcome**
* **Per-Interaction Credit:** **Yes.** It produces a per-touchpoint causal uplift credit score \\(\hat{\Delta}(\tau_j \mid X, T) = g_\theta(X, T) - g_\theta(X, T \setminus \{\tau_j\})\\), defined as the counterfactual drop in
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching [1]
`2026_ICLR_MRet_Retention-Optimized-Two-Sided-Matching.md`
**Source:** https://arxiv.org/pdf/2602.15752.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching* [1]
* **Authors:** **Ren Kishimoto**\*¹, **Rikiya Takehi**\*², **Koichi Tanaka**³, **Masahiro Nomura**¹, **Riku Togashi**⁴, **Yoji Tomita**⁴, and **Yuta Saito**⁵ (\*Equal contribution) [1–2]
* **Author Affiliations:**
  1. **Institute of Science Tokyo**, Tokyo, Japan (`kishimoto.r.ab@m.titech.ac.jp`, `nomura@comp.isct.ac.jp`) [1]
  2. **Waseda University**, Tokyo, Japan (`rikiya.takehi@fuji.waseda.jp`) [1]
  3. **Keio University**, Tokyo, Japan (`kouichi1207@keio.jp`) [1]
  4. **CyberAgent**, Tokyo, Japan (`rtogashi@acm.org`, `tomita_yoji@cyberagent.co.jp`) [1]
  5. **Hanjuku-kaso, Co., Ltd.**, Tokyo, Japan (`saito@hanjuku-kaso.com`) [2]
* **Year:** **2026** (arXiv pre-print: `2602.15752`, submitted Feb 2026) [1]
* **Venue:** Submitted to **ICLR 2026** / arXiv pre-print [1, 3]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Two-sided matching platforms (e.g., online dating, recruitment) typically optimize for total matches or axiomatic fairness of exposure [2, 4]. Match maximization concentrates recommendations on popular users, causing under-matched users to receive few matches and churn [2, 5, 6]. Axiomatic exposure fairness is only an unproven heuristic proxy and does not directly
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### A Human-Augmenting Agentic Workflow for Causal Inference (Netflix) — stub
`2026_NetflixBlog_oci-agent_Causal-Inference-Workflow.md`
**Source:** https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af  
**Q2 class:** NOT

**Summary.** Stub card. NotebookLM, jina.ai, and WebFetch all failed to retrieve the Netflix tech blog post. D4 logs it as a 2026 Netflix engineering post that open-sources `oci-agent` for observational causal inference, with a case study that includes **retention treatment-effect estimation** with overlap/trimming diagnostics.

**Evidence.** Not specified in source (fetch failed). No per-interaction credit table is claimed in the discovery log.

### Rethinking User Retention Modeling in Recommendation [1, 2]
`2026_TOIS_IURO+_Rethinking-User-Retention-Modeling.md`
**Source:** https://dl.acm.org/doi/pdf/10.1145/3790098  
**Q2 class:** PARTIAL

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Rethinking User Retention Modeling in Recommendation* [1, 2]
* **Authors:** **Rui Ding**\*¹, **Ruobing Xie**\*², **Xiaobo Hao**², **Xiaochun Yang**\*¹, **Kaikai Ge**², **Xu Zhang**², **Zhanhui Kang**², **Jie Zhou**², and **Leyu Lin**² (\*Corresponding authors) [1, 2]
* **Author Affiliations:**
  1. **Northeastern University**, School of Computer Science and Engineering, Shenyang, China (`ruiding.neu@outlook.com`, `yangxc@mail.neu.edu.cn`) [1, 2]
  2. **Tencent**, Beijing, China (`{xrbsnow-ing, rolyhao, kavinge, xuonezhang, kegokang, withtomzhou, goshawklin}@tencent.com`) [1, 2]
* **Year & Venue:** Published in **March 2026** in *ACM Transactions on Information Systems (TOIS)*, Vol. 44, No. 3, Article 64 (35 pages) [2, 3]. DOI: `10.1145/3790098` [2].

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Standard recommender systems optimize short-term metrics (clicks, impressions, dwell time) that fail to align with long-term user satisfaction and retention [1, 3, 4]. Existing retention models focus strictly on prediction accuracy without revealing the underlying rationale or discovering *why* users return, largely due to the absence of explicit supervised signals [1, 5]. Furthermore, retention modeling suffers from weak causality, high behavioral randomness, and an
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search [1]
`2026_arXiv_DCEO_Direct-Causal-Effect-Optimization.md`
**Source:** https://arxiv.org/html/2608.25635  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search* [1]
* **Authors:** Junzhao Zhang, Tao Zhang, Liren Yu, Feiyi Dong, Zhixuan Zhang, Dan Ou, and Haihong Tang [1]
* **Author Affiliations:** **Taobao & Tmall Group of Alibaba**, Hangzhou & Beijing, Zhejiang, China [1]
* **Year:** **2026** (Published August 26, 2026) [1]
* **Venue:** arXiv pre-print (`arXiv:2608.25635v1 [cs.LG]`) [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Industrial e-commerce search engines face a fundamental **cross-granularity gap** between user-level long-term objectives (such as \\(n\\)-day cumulative purchases or Gross Merchandise Value [GMV] per user) and item-level ranking scores computed for each search request [2, 3]. Conventional search systems bridge this gap using hand-crafted multi-objective fusion formulas with globally shared, manually tuned weights over item-level predictions (click, cart, purchase, transaction value) [2, 4]. These heuristic schemes provide limited personalization, require costly repeated online A/B testing, and optimize predictive association rather than the true causal effect of item-level proxy scores on long-term user value [2, 4, 5].
* **Key Contributions:**
  1. **Cross-Granularity Causal Formulation:**
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning [1, 2]
`2026_arXiv_DownstreamRewards_Long-Term-Engagement-Optimization.md`
**Source:** https://arxiv.org/html/2607.14192  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning* [1, 2]
* **Authors:** **Dingsu Wang**, **Filip Ryzner**, **Kelly He**, **Armando Ordorica**, **David Woo**\* (*Corresponding author*), **Aditya Mantha**, **Liyao Lu**, **Usha Amrutha Nookala**, **Haoran Guo**, **Jiacong He**, **Olafur Gudmundsson**, **Matt Chun**, **Krystal Benitez**, **Haibin Xie**, **Alekhya Pyla**, **Sameer Jain**, **Zhongjian Jiang**, **Shruthi Hariharan**, **Dhruvil Deven Badani**, and **Yijie Dylan Wang** (*All authors contributed equally*) [2].
* **Affiliation:** **Pinterest**, San Francisco, CA, USA [2].
* **Year & Venue:** Published in **August 2026** as an arXiv pre-print (`arXiv:2607.14192v3 [cs.LG]`, 21 Aug 2026) [2].

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** Optimizing long-term user retention in industrial recommender systems is notoriously difficult because revisitation labels are sparse, delayed, and difficult to attribute to individual recommendations [3, 4]. Direct Reinforcement Learning (RL) and long-horizon policy optimization methods suffer from massive action spaces, heavy interaction data requirements, data distribution shifts, and an inability to transfer reward designs cleanly across heterogeneous product surfaces (e.g.,
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM [1]
`2026_arXiv_IMA_Integrated-Marketing-Attribution.md`
**Source:** https://arxiv.org/pdf/2606.16878.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Integrated Marketing Attribution: A Bayesian Framework for Privacy-Safe Granular Measurement Anchored in MMM* [1]
* **Authors:** Meghana R. Bhat, Ankit Umare, Utsav Aggarwal, Richard Vecsler, Arunkumar Mani, Karthik Nair, and Chandhu Nair [1]
* **Affiliations:** Lowe’s Companies, Inc. [1]
* **Year:** 2026 (arXiv e-print: `2606.16878`) [1]
* **Venue:** Not specified in source (arXiv pre-print) [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** The tension between privacy/robustness and granularity in retail marketing measurement [1, 2]. Traditional Multi-Touch Attribution (MTA) relies on deterministic user-level tracking and third-party cookies, which are failing due to privacy restrictions and signal loss [3, 4]. Conversely, Marketing Mix Modeling (MMM) is privacy-safe and robust at the channel level, but too coarse for short-term campaign-level optimization because estimating MMM at the campaign level causes severe overfitting, multicollinearity, and parameter instability [5-7].
* **Key Contributions:**
  1. **Integrated Marketing Attribution (IMA) Framework:** A unified, privacy-safe three-stage attribution architecture that decomposes weekly channel-level incremental sales contributions from MMM down to daily, campaign-level effects using aggregated media data
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Incremental Recommendation via Causal Models [1]
`2026_arXiv_NA_Incremental-Recommendation-Causal-Models.md`
**Source:** https://arxiv.org/pdf/2608.26804.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**
* **Title:** *Incremental Recommendation via Causal Models* [1]
* **Authors:** **Athanasios Vlontzos**\*¹, **David Gustafsson**², **Michael O’Riordan**³, and **Ciarán M. Gilligan-Lee**⁴ (\*Work done while at Spotify) [1, 2]
* **Author Affiliations:**
  1. **Imperial College London / Hologen**, London, UK (`Hologen Imperial College London, UK`) [1]
  2. **Spotify**, Stockholm, Sweden (`davidgustafsson@spotify.com`) [1]
  3. **Spotify**, London, UK (`moriordan@spotify.com`) [1]
  4. **Spotify** (Ireland) & **University College London**, London, UK (`ciaranl@spotify.com`) [1]
* **Year:** **2026** (arXiv pre-print: `2608.26804`) [1, 3]
* **Venue:** arXiv pre-print (`arXiv:2608.26804`) / Conference pre-print [1]

---

### **(2) Core Problem and Key Contribution**
* **Core Problem:** Recommendation impressions are a finite resource. Delivering recommendations to users who would discover the content organically yields no incremental value and displaces other recommendations that could [1]. While platforms collect holdback data (withholding recommendations from a small randomized fraction of users), a fundamental structural obstacle prevents naive Conditional Average Treatment Effect (CATE) subtraction (\\(\hat{p}_1(\mathbf{x}) - \hat{p}_0(\mathbf{x})\\)): **Attribution Window Mismatch** [1, 5–7]. 
  * Treated
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

### Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling [1]
`2026_arXiv_OCARM_Post-Conversion-Content-Retention.md`
**Source:** https://arxiv.org/pdf/2604.25839.pdf  
**Q2 class:** NOT

**Summary.** ### **(1) Title, Authors, Affiliations, Year, Venue**

* **Title:** *Break the Inaccessible Boundary: Distilling Post-Conversion Content for User Retention Modeling* [1]
* **Authors:** **Tianbao Ma**\*¹, **Ruochen Yang**\*¹, **Chengen Li**¹, **Yuexin Shi**¹, **Jiangxia Cao**†¹, **Linxun Chen**¹, **Zhaojie Liu**¹, **Yanan Niu**¹, **Han Li**¹, and **Kun Gai**¹ (\*Equal contributions, †Corresponding author) [1, 2]
* **Affiliations:** **Kuaishou Technology**, Beijing, China (`{matianbao, yangruochen, lichengen, shiyuexin, caojiangxia, chenxi36, zhaotianxing, niuyanan, lihan08}@kuaishou.com`, `gai.kun@qq.com`) [1]
* **Year:** **2026** (arXiv pre-print: `2604.25839`) [1]
* **Venue:** arXiv pre-print (`arXiv:2604.25839`) / Conference pre-print [1]

---

### **(2) Core Problem and Key Contribution**

* **Core Problem:** In Real-Time Bidding (RTB) advertising systems for user re-engagement and growth, retention models must predict a user's future revisit probability at bidding time—before the user converts (clicks to open the app) and consumes any content [1, 3]. While post-conversion content consumption ("Onboarding Content"—videos watched, interactions performed post-conversion) carries exceptionally strong predictive signals for retention, it is strictly inaccessible during bidding [4–5]. Directly incorporating onboarding content into training causes severe
… [truncated]

**Evidence.** See quantitative results in §1 (NLM facts query). Numbers above are from NotebookLM scoped to this source.

---

