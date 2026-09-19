# NotebookLM deep-research report — Q2 query (2026-09-17)

Query: attributing user retention or engagement to individual in-app interactions or recommendations: retention attribution, engagement credit assignment, incremental retention value of an action, long-term user retention reward credit assignment in recommender systems, reinforcement learning for user retention, dating app matches likes swipes retention causal effect

Sources found: 45. Imported into notebook (2026-09-17): GFN4Retention (arXiv 2406.06043), Stratified Expert Cloning (arXiv 2504.05628), DT4Rec (arXiv 2303.06347), RLUR (arXiv 2302.01724), From Clicks to Conversions (arXiv 2009.00497), Model-agnostic Downstream Rewards Learning (arXiv 2607.14192). Not importable from the research result (ResearchGate pages): "Not All Matches Are Equally Valuable: An Online Experiment of Retention-Focused Recommendation in a Job-Matching Platform"; "Interpretable User Retention Modeling in Recommendation". The deep report itself (index 0) did not import.

Verbatim report follows. Citation numbers refer to the numbered source list at the end.

---

# Algorithmic Credit Assignment and Causal Attribution for Long-Term User Retention in Recommender Systems

## Foundations of Retention Credit Assignment

Modern recommendation architectures have historically optimized for localized, immediate surrogates of user engagement, such as Click-Through Rate (CTR), immediate conversion, or single-session watch time [cite: 1, 2]. While point-wise and list-wise ranking functions effectively capture immediate gratification, they inherently fail to model long-term user retention and platform loyalty [cite: 1, 3]. Optimizing exclusively for immediate feedback creates local algorithmic maxima that frequently recommend addictive, clickbait, or overly repetitive content [cite: 2, 3]. Although such strategies elevate short-term interaction volume, they accelerate user fatigue, diminish sustainable interest, and ultimately increase platform churn [cite: 2, 3].

Transitioning optimization objectives from instantaneous engagement to long-term user retention introduces severe technical challenges, primarily centered on temporal credit assignment, delayed feedback, and high environment variance [cite: 1, 4]. Unlike immediate signals that return within seconds of an interaction, retention feedback is inherently multi-session and delayed across hours, days, or weeks [cite: 1, 3]. Furthermore, retention outcomes are heavily confounded by external stochastic noise—such as weekend-versus-weekday usage patterns, social events, and offline user obligations—making it difficult to attribute a user's decision to return to any single item or recommendation list [cite: 1].

To address these challenges, the recommendation task can be mathematically formalized as an infinite-horizon, request-based Markov Decision Process (MDP) represented by the tuple $(\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)$ [cite: 1, 5]. At any given session $i$ and interaction request step $t$, the state $s_t \in \mathcal{S}$ incorporates user demographic profiles, long-term historical interaction sequences, contextual environment attributes, and candidate item spaces [cite: 1]. The recommendation policy $\pi(a_t|s_t)$ selects an action $a_t \in \mathcal{A}$, which maps to ranking parameterizations or direct top-$K$ candidate selections [cite: 1]. While the agent receives immediate feedback signals $I(s_t, a_t)$ such as clicks, watch durations, or explicit likes, the primary optimization objective is to minimize the cumulative inter-session returning time interval $\Delta T_{\text{return}}$, thereby maximizing Daily Active Users (DAU) and sustained long-term retention [cite: 1, 5].

The fundamental mathematical bottleneck in this MDP formulation is the delayed credit assignment problem: back-propagating the scalar reward of a user returning in a subsequent session to individual actions taken throughout a prior session [cite: 3, 4, 6]. Across a multi-step user trajectory, an initial recommendation may spark exploration or content fatigue that alters the user's hidden psychological state, while subsequent recommendations capture the immediate conversion [cite: 4, 7]. Resolving this temporal attribution gap requires advanced methodologies spanning reinforcement learning, probabilistic generative flows, sequence modeling transformers, and structural causal inference [cite: 1, 3, 8, 9].

---

## Reinforcement Learning Paradigms for Delayed Retention Rewards

Reinforcement learning provides a framework for multi-session retention optimization by explicitly modeling the long-term cumulative reward of sequential decision-making [cite: 1, 3, 5]. However, standard off-the-shelf algorithms fail when applied to retention optimization due to extreme reward latency, user activity biases, and action-space dimensionality [cite: 1, 4]. Industrial recommendation systems have introduced specialized reinforcement learning frameworks to address these non-Markovian properties [cite: 1, 3, 8].

The Reinforcement Learning for User Retention (RLUR) architecture models retention by defining the agent's goal as the minimization of accumulated inter-session returning time across an infinite-horizon request-based MDP [cite: 1, 5]. Deployed at scale on platforms such as Kuaishou, RLUR addresses three primary system pathologies [cite: 1, 5]. To mitigate environmental uncertainty, RLUR implements a predictive variance-normalization module that estimates expected user returning times based on contextual features, scaling the observed delayed reward to isolate the recommender system's true policy impact from external noise [cite: 1, 5]. To eliminate user activity bias—wherein highly active power users log in frequently regardless of algorithmic variations and dominate global policy gradients—RLUR utilizes group-based policy branching and stratified value functions [cite: 1, 5]. Finally, to stabilize off-policy value estimation under multi-hour reward delays, RLUR enforces soft policy regularization that blends intermediate heuristic rewards with intrinsic motivation bonuses [cite: 1, 5].

An alternative to standard value-based reinforcement learning is the probabilistic flow modeling framework known as Generative Flow Networks for Retention (GFN4Retention) [cite: 3, 10]. Rather than treating retention as a distant, monolithic scalar reward, GFN4Retention models a user's multi-session trajectory as a forward probabilistic flow $S = \{s_1 \rightarrow s_2 \rightarrow \dots \rightarrow s_T\}$ [cite: 3]. The system decomposes the total state flow estimator $F(s_t)$ at step $t$ into a non-parametric immediate feedback component $F_I(s_t)$ and a parametric long-term retention component $F_R(s_t)$:

$$F(s_t) = F_R(s_t) \cdot \left(F_I(s_t)\right)^\alpha = F_R(s_t) \cdot \exp\left(\alpha \sum_{j=1}^{t-1} r_j\right)$$

At the terminal session boundary $s_T$, the parametric retention flow $F_R(s_T)$ is pinned directly to the observed scalar retention signal $R$ via a terminal loss function $\mathcal{L}_{\text{terminal}} = (\log F_R(s_T) - \log R)^2$ [cite: 3]. To back-propagate this terminal retention credit to every intermediate item recommendation, GFN4Retention enforces a Detailed Balance constraint across adjacent states [cite: 3]. For non-terminal steps $1 \le t \le T-1$, the forward transition policy $P_F(s_{t+1}|s_t)$ and backward transition policy $P_B(s_t|s_{t+1})$ must satisfy the flow preservation objective:

$$\mathcal{L}_{\text{DB}} = \left( \log F_R(s_t) + \log P_F(s_{t+1} | s_t) - \log F_R(s_{t+1}) - \log P_B(s_t | s_{t+1}) - \alpha \cdot r_t \right)^2$$

By optimizing this Detailed Balance loss across session trajectories, the end-of-session retention reward $R$ flows backward step-by-step [cite: 3]. This allows the recommender system to calculate an exact action-level retention attribution score for every individual item presented to the user, directly balancing immediate gratification $r_t$ against long-term retention value [cite: 3].

To avoid the sample inefficiency, off-policy overestimation, and exploration risks inherent to dynamic value-based reinforcement learning in live production environments, modern architectures leverage sequence-to-sequence transformers and imitation learning [cite: 4, 8, 11]. Decision Transformer frameworks, such as DT4Rec, reframe offline reinforcement learning into an autoregressive sequence modeling problem [cite: 8]. By conditioning recommendations on auto-discretized reward prompts, transformer architectures eliminate Q-value estimation instability and the bootstrapping issues associated with off-policy value approximation [cite: 8]. During inference, conditioning the network on high target retention prompts forces the model to generate action sequences that yield the desired long-term retention outcomes [cite: 8].

Similarly, Stratified Expert Cloning (SEC) bypasses delayed reward modeling altogether through behavioral cloning [cite: 4, 11]. SEC stratifies user populations into retention tiers based on historical return frequencies and trains imitation learning policies on the trajectories of top-tier, highly retained expert users [cite: 4, 11]. Coupled with dynamic adaptive expert selection and entropy regularization, SEC steers vulnerable users toward interaction patterns characteristic of highly retained cohorts without requiring risky online exploration [cite: 4, 11].

| Architecture / Paradigm | Core Optimization Mechanism | Temporal Credit Assignment Strategy | Action Space Scalability | Primary Operational Trade-Off |
| :--- | :--- | :--- | :--- | :--- |
| **RLUR (Request-Based MDP)** [cite: 1, 5] | Continuous policy optimization minimizing session return interval $\Delta T$ [cite: 1, 5]. | Variance-normalized delayed reward combined with heuristic reward shaping [cite: 1, 5]. | High (Linear action weighting / Continuous vectors) [cite: 1]. | Susceptible to off-policy instability under long temporal delays [cite: 1]. |
| **GFN4Retention (Flow Networks)** [cite: 3] | Probabilistic flow preservation via Detailed Balance constraints [cite: 3]. | Backward step-wise propagation of terminal session flow $F_R(s_T)$ [cite: 3]. | High (Integrates natively with learning-to-rank objectives) [cite: 3]. | Computationally intensive backward flow estimation per transition [cite: 3]. |
| **DT4Rec (Decision Transformer)** [cite: 8] | Autoregressive sequence generation conditioned on reward prompts [cite: 8]. | Global trajectory sequence modeling via self-attention mechanisms [cite: 8]. | Moderate (Constrained by transformer context window length) [cite: 8]. | Sensitive to reward prompt discretization boundaries [cite: 8]. |
| **SEC (Stratified Expert Cloning)** [cite: 4, 11] | Supervised imitation learning on top-tier user trajectories [cite: 4, 11]. | Implicit temporal attribution via expert sequence pattern matching [cite: 4, 11]. | Very High (Standard supervised target cross-entropy) [cite: 4]. | Inability to discover optimal novel policies beyond observed expert demonstrations [cite: 4]. |

---

## Causal Inference and Uplift Modeling for Action-Level Attribution

While reinforcement learning models sequence trajectories to maximize long-term rewards, it frequently struggles to differentiate between correlation and direct causation [cite: 9, 12]. High-frequency users naturally generate higher retention metrics regardless of algorithmic intervention [cite: 1, 9]. To isolate the true incremental retention value of an individual action, recommender systems must integrate causal inference and uplift modeling [cite: 9, 13].

Standard predictive retention models estimate baseline response probability $P(Y=1|X, A)$, where $Y \in \{0, 1\}$ represents user retention, $X$ denotes context features, and $A$ is the algorithmic intervention [cite: 9]. However, optimizing directly for baseline response leads to inefficient resource allocation [cite: 9]. Recommender systems require the Conditional Average Treatment Effect (CATE), which measures the net change in retention probability caused strictly by action $A=1$ relative to control $A=0$ [cite: 9, 14]:

$$\tau(X) = \mathbb{E}\left[Y(1) - Y(0) \mid X\right] = P\left(Y=1 \mid X, \text{do}(A=1)\right) - P\left(Y=1 \mid X, \text{do}(A=0)\right)$$

Evaluating user interactions through CATE partitions the user population into four distinct behavioral quadrants, each dictating a specific algorithmic strategy [cite: 9]. The primary source of incremental retention value resides in the Persuadables quadrant, where $\tau(X) > 0$ [cite: 9]. These users will remain retained if and only if a specific action, recommendation, or nudge is delivered [cite: 9].

Conversely, the Sure Things quadrant represents highly loyal users where $Y(1)=1$ and $Y(0)=1$ [cite: 9]. Standard predictive models incorrectly over-allocate premium recommendations or incentives to this group, creating zero incremental lift because these users return regardless of intervention [cite: 9]. The Lost Causes quadrant contains users where $Y(1)=0$ and $Y(0)=0$, who will churn irrespective of recommendation quality [cite: 9]. Finally, the Sleeping Dogs quadrant captures instances where $\tau(X) < 0$ [cite: 9]. For these users, an algorithmic intervention causes friction, notification fatigue, or annoyance, actively increasing their probability of churn [cite: 9].

In computational advertising and content platforms, conversion attribution historically relied on heuristic models such as last-click or linear decay [cite: 6, 7]. In multi-step recommendation environments, these heuristic methods fail because user state transitions are non-Markovian and conditionally dependent on cumulative historical exposures [cite: 6, 7, 15]. Causal counterfactual evaluation resolves this by modeling the unobserved potential outcome—what the user's retention state $Y(0)$ would have been had they received an alternative recommendation sequence [cite: 6, 16]. Modern uplift modeling frameworks utilize Inverse Propensity Scoring (IPS) and Doubly Robust estimators to adjust for selection bias in logged interaction data [cite: 8, 9].

When combined with multi-session simulation environments, doubly robust causal estimators evaluate how recommendation policies modify user internal hidden states over extended horizons [cite: 6, 7]. This enables platforms to quantify the precise incremental retention value of non-converting actions—such as introducing topic diversity or serendipitous content—that temporarily reduce immediate CTR but prevent long-term platform fatigue [cite: 4, 7].

---

## Retention Attribution in Reciprocal and Two-Sided Matching Markets

While content-consumption platforms feature one-sided consumer dynamics, reciprocal platforms—including online dating applications and job-matching marketplaces—operate under fundamentally different dynamic constraints [cite: 17, 18, 19]. In reciprocal recommendations, the system must establish mutual compatibility between two human actors [cite: 17, 20, 21].

In traditional content recommendation, increasing user engagement and consumption directly drives platform retention [cite: 1, 3]. In reciprocal matching markets, recommender systems face a structural tension known as the Reciprocal Retention Paradox [cite: 19]. If a dating or recruitment platform delivers highly accurate reciprocal recommendations instantly, both matched users achieve their real-world objective and exit the market, resulting in platform offboarding and reduced active retention [cite: 19]. Conversely, if the system delivers poor recommendations that yield zero matches, users experience severe search fatigue, rejection, and frustration, leading to high churn rates [cite: 18, 19].

Empirical evaluations on reciprocal platforms demonstrate that the relationship between match accumulation and user retention is non-linear and concave [cite: 18]. Users receiving zero or extremely few matches exhibit high churn rates [cite: 18]. However, once a user reaches a baseline threshold of successful mutual matches, the marginal retention gain of additional matches drops rapidly toward zero [cite: 18].

To optimize ecosystem-wide retention without reducing aggregate match quality, reciprocal platforms employ retention-focused score-boosting algorithms [cite: 18]. Traditional reciprocal algorithms rank candidate profiles by combining bilateral preference probabilities:

$$S(u, v) = P(u \rightarrow v) \cdot P(v \rightarrow u)$$

Where $P(u \rightarrow v)$ is the predicted probability that user $u$ likes user $v$, and $P(v \rightarrow u)$ is the reciprocal probability [cite: 17, 22]. Retention-focused score boosting modifies this matching score by incorporating an explicit churn-risk multiplier $\psi(v)$ based on candidate $v$'s recent match history [cite: 18]:

$$S_{\text{retention}}(u, v) = P(u \rightarrow v) \cdot P(v \rightarrow u) \cdot \left[ 1 + \beta \cdot \psi(v) \right]$$

$$\psi(v) = \exp\left(-\lambda \cdot M_v\right)$$

Where $M_v$ represents the recent match count of candidate user $v$, and $\beta, \lambda$ are hyper-parameters controlling retention intervention intensity [cite: 18]. By applying score boosts to users who are at high risk of churning due to low recent match counts ($M_v \to 0$), the platform increases their exposure and match probability [cite: 18]. Because the marginal retention gain is highest for low-match users, reallocating match opportunities from saturated power users to churn-risk users lifts total platform-wide DAU and multi-session retention without degrading overall matching efficiency [cite: 18].

| Platform Metric / Dimension | Single-Sided Content Platforms | Reciprocal Matching Platforms |
| :--- | :--- | :--- |
| **Core Transaction** | Asymmetric consumption of digital items [cite: 1]. | Bilateral mutual preference between two human actors [cite: 17, 19]. |
| **Primary Retention Driver** | Content relevance, freshness, and feed diversity [cite: 4, 23]. | Mutual match rate, response rate, and profile discovery [cite: 18, 19]. |
| **Primary Churn Mechanism** | Content boredom, repetitive recommendations, clickbait fatigue [cite: 2, 3]. | Search fatigue (zero matches) vs. market exit (platform success) [cite: 18, 19]. |
| **Marginal Match / Engagement Value** | Monotonically positive engagement yield [cite: 1, 3]. | Strongly concave; diminishing returns past baseline match thresholds [cite: 18]. |
| **Attribution Complexity** | Temporal delay across multi-session viewing trajectories [cite: 1, 3]. | Bilateral interaction dependency, two-sided congestion, and offline conversion [cite: 17, 19]. |

---

## Systemic Challenges and Engineering Realities in Production Deployment

Deploying retention-attribution and credit-assignment architectures in large-scale production environments introduces complex system trade-offs [cite: 1, 2, 23]. Engineering teams must navigate environmental non-stationarity, user activity distribution imbalances, and multi-objective reward shaping [cite: 1, 2, 23].

Real-world recommendation logs are inherently noisy and non-stationary [cite: 1, 23]. User behavior changes systematically across time-of-day, day-of-week, and external real-world events [cite: 1, 23]. An algorithm that evaluates unnormalized inter-session return times will over-index on weekend activity spikes or penalize recommendations served immediately prior to standard working hours [cite: 1]. Raw retention logs also exhibit severe power-law distribution imbalances [cite: 1]. Highly active power users log into the platform multiple times daily, generating millions of interaction trajectories, whereas casual or churn-vulnerable users generate sparse log sequences [cite: 1, 4]. If value-based reinforcement learning models or transformer policies are trained on unweighted global logs, the loss function is dominated by power-user dynamics [cite: 1]. Consequently, the system optimizes policies for users who are already retained, while failing to generate effective interventions for vulnerable demographics [cite: 1, 9]. Industrial deployments counteract this by enforcing stratified cohort re-weighting and variance-normalized reward targets [cite: 1, 4].

Relying exclusively on a pure delayed retention reward creates severe gradient sparsity, sample inefficiency, and training instability [cite: 1, 2, 4]. Production systems address this by constructing composite multi-objective reward functions that merge immediate interaction utility with long-term value functions [cite: 2, 23]:

$$R_{\text{composite}}(s_t, a_t) = \omega_{\text{inst}} \cdot R_{\text{instant}}(s_t, a_t) + \omega_{\text{div}} \cdot R_{\text{diversity}}(a_t) + \omega_{\text{ret}} \cdot \hat{V}_{\text{retention}}(s_{t+1})$$

Where $R_{\text{instant}}$ aggregates immediate signals such as clicks, completion rates, or likes; $R_{\text{diversity}}$ penalizes intra-session content fatigue; and $\hat{V}_{\text{retention}}$ represents the predicted long-term retention value generated by a nearline flow estimator or reinforcement learning policy [cite: 3, 23]. To maintain policy stability, intermediate heuristic rewards are calibrated using temporal-difference learning flow-backs, ensuring that immediate signals serve as dense step-by-step guidance without overriding the long-term retention signal [cite: 1, 2].

Industrial production deployment architectures operationalize these multi-scale time dynamics through a three-tiered infrastructure framework:

1. **Real-Time Online Scoring Tier (<20ms)**: Lightweight linear ranking functions, contextual bandits, or multi-task deep neural networks compute immediate item scores by combining CTR predictions, immediate engagement metrics, and action-vector continuous weights generated by the policy model [cite: 1, 23].
2. **Nearline Session Processing Tier (Seconds to Minutes)**: Stream-processing engines log real-time session state transitions $s_t \to s_{t+1}$, track candidate exposure logs, and calculate intra-session diversity bonuses or immediate reward shaping adjustments [cite: 2, 23].
3. **Offline Asynchronous Attribution Tier (Hours to Days)**: High-throughput distributed computing clusters aggregate cross-session user returning logs, compute causal counterfactual weights, run Detailed Balance flow-matching updates, or update Decision Transformer weights [cite: 3, 8]. Updated policy parameters are continuously streamed back to the online scoring tier, completing the long-term credit assignment feedback loop [cite: 1, 23].

---

## Conclusions

Systematically attributing long-term user retention to individual in-app recommendations represents a critical paradigm shift in recommender system design [cite: 1, 3, 24]. Moving beyond immediate engagement surrogates requires treating recommendation as an infinite-horizon sequential decision problem, where delayed feedback, environmental noise, and attribution complexity must be explicitly modeled [cite: 1, 5].

Reinforcement learning approaches—such as request-based MDP formulations and Generative Flow Networks—provide rigorous frameworks for back-propagating terminal multi-session retention rewards into step-wise action-level scores [cite: 1, 3]. Sequence modeling via Decision Transformers and imitation learning via Stratified Expert Cloning offer robust offline alternatives that bypass the sample inefficiency and exploration risks of standard online reinforcement learning policies [cite: 4, 8, 11].

Complementing these sequential paradigms with causal uplift modeling ensures that recommender systems isolate direct incremental retention value ($\text{CATE}$), targeting persuadable user segments while avoiding wasted exposure on already-retained users [cite: 9]. In reciprocal matching markets, addressing the concave retention-match curve through churn-risk score boosting resolves the fundamental conflict between individual user success and platform-wide ecosystem stability [cite: 18, 19]. The optimal production path forward lies in integrating multi-objective reward shaping with hybrid real-time, nearline, and offline architecture pipelines, ensuring scalable execution and sustainable user retention [cite: 1, 3, 12, 23].

---

1. Reinforcing User Retention in a Billion Scale Short Video Recommender System — https://www.researchgate.net/publication/368290588
2. Sarcouncil Journal — Reinforcement Learning for Multi-Objective Ad Optimization: Beyond Click — https://sarcouncil.com/download-article/SJECS-551-2025-66-73.pdf
3. Modeling User Retention through Generative Flow Networks — https://arxiv.org/pdf/2406.06043
4. Stratified Expert Cloning for Retention-Aware Recommendation at Scale — https://arxiv.org/html/2504.05628v2
5. Reinforcing User Retention in a Billion Scale Short Video Recommender System — https://arxiv.org/pdf/2302.01724
6. From Clicks to Conversions: Recommendation for long-term reward — https://arxiv.org/html/2009.00497v1
7. From Clicks to Conversions (PDF) — https://arxiv.org/pdf/2009.00497
8. User Retention-oriented Recommendation with Decision Transformer — https://arxiv.org/html/2303.06347v1
9. Stability-Aware Uplift Policy Selection for Customer Retention (MDPI) — https://www.mdpi.com/2076-3417/16/10/4918
10. Modeling User Retention through Generative Flow Networks (ResearchGate) — https://www.researchgate.net/publication/383419238
11. Stratified Expert Cloning (alphaXiv) — https://www.alphaxiv.org/audio/2504.05628
12. Causality Engine glossary — https://www.causalityengine.ai/glossary/recommender-systems
13. iAge predictive ROI — https://iage.net/resources/predictive-roi-calculator
14. Hoang Dang, Beyond the limitation of A/B Testing (Medium) — https://medium.com/@dangvanconghoang.ch/beyond-the-limitations-of-a-b-testing-using-causal-inference-044d85b19c74
15. Causal Policy Learning — https://causaldm.github.io/Causal-Decision-Making/0_Motivating_Examples/CPL.html
16. Herm.io personalisation attribution — https://www.herm.io/blog/why-your-attribution-model-is-undermining-personalization-roi/
17. Multi-Objective Recommender Systems: Survey and Challenges — https://arxiv.org/html/2210.10309v1
18. Not All Matches Are Equally Valuable: An Online Experiment of Retention-Focused Recommendation in a Job-Matching Platform — https://www.researchgate.net/publication/413926236
19. Multistakeholder recommendation: Survey and research directions — https://www.researchgate.net/publication/338516177
20. Popularity Bias in Recommendation: A Multi-stakeholder Perspective — https://arxiv.org/html/2008.08551v1
21. A survey on multi-objective recommender systems — https://pmc.ncbi.nlm.nih.gov/articles/PMC10073543/
22. KDD '23 proceedings TOC — https://kdd.org/kdd2023/wp-content/uploads/2023/08/toc.html
23. Reinforcement Learning for Recommendation Systems — ApplyingML — https://applyingml.com/resources/rl-for-recsys/
24. Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning — https://arxiv.org/html/2607.14192v3

Other hits not cited in the report (index: title): 26 QCon SF Nov 2024 talk "Reinforcement Learning for User Retention in Large-Scale Recommendation Systems"; 27 "Interpretable User Retention Modeling in Recommendation" (ResearchGate); 44 EnhancedRL multi-task fusion (arXiv 2409.11678). Indices 28–43 were off-topic.
