# Phase 4 Conflict Follow-up — Quantitative Claims

**Query:** Conflict resolution using only these sources: report the exact quantitative results for (a) virtual-rose acceptance and eight-versus-two treatment outcomes, (b) ECDA simulation and field outcomes, (c) Nash-social-welfare expected matches, envy, and whether any Gini is reported, (d) Airbnb cluster-randomization overall interference bias and whether market-tightness subgroup percentages are statistically established, and (e) TEC field favorites and match outcomes. Quote labels/tables when possible. Do not infer; write Not specified where absent.

## Response

### **(a) Virtual-Rose Acceptance and Eight-versus-Two Treatment Outcomes**
*Source: “Propose with a rose? Signaling in internet dating markets” (Lee & Niederle, 2015)* [1]

#### **Acceptance Probability Effects:**
*   **Overall Baseline Impact:** Attaching a rose to a proposal "increases the probability that a recipient will accept the proposal by 3.3 % points, which corresponds to a 20 % increase in the acceptance rate." [2, 3]
*   **Regression Coefficients (Table 2):**
    *   **Model A (OLS with Recipient Fixed Effects):** `Rose` coefficient = **`0.033**` (standard error `0.016`). [4]
    *   **Model A (Instrumental Variable (IV) Estimation):** `Rose` coefficient = **`0.041`** (standard error `0.029`). [4]
*   **Heterogeneity across Recipient Desirability Groups (Table 4, Model B):**
    *   **Bottom Recipients (`R_Bottom Rose`):** **`0.054`** (s.e. `0.047`) under OLS; **`0.035`** (s.e. `0.054`) under IV. [5, 6]
    *   **Middle Recipients (`R_Middle Rose`):** **`0.078***`** (s.e. `0.027`) under OLS; **`0.064**`** (s.e. `0.031`) under IV. [5, 6]
    *   **Top Recipients (`R_Top Rose`):** **`-0.001`** (s.e. `0.021`) under OLS; **`-0.002`** (s.e. `0.025`) under IV. [5, 6]
*   **Bilateral Pairwise Effects (Table 5, Model C):**
    *   *For Bottom Recipients (`R_Bottom`):* `S_Bottom Rose` is **`-0.052`** (`0.064`); `S_Middle Rose` is **`0.125*`** (`0.070`); `S_Top Rose` is **`0.160*`** (`0.084`). [7, 8]
    *   *For Middle Recipients (`R_Middle`):* `S_Bottom Rose` is **`0.106**`** (`0.049`); `S_Middle Rose` is **`0.019`** (`0.039`); `S_Top Rose` is **`0.124***`** (`0.040`). [8, 9]
    *   *For Top Recipients (`R_Top`):* `S_Bottom Rose` is **`-0.003`** (`0.044`); `S_Middle Rose` is **`0.034`** (`0.032`); `S_Top Rose` is **`-0.033`** (`0.032`). [9]

#### **Eight-versus-Two Rose Endowment Treatment Outcomes (Table 3):**
*   **Panel A. Men (Seoul, Full Verification):**
    *   `Have at least one initiated date`: **`0.313`** (2 Roses) vs. **`0.452`** (8 Roses) — **`45 %**`** relative increase. [10]
    *   `No of initiated dates`: **`0.556`** (2 Roses) vs. **`0.833`** (8 Roses) — **`48 %*`** relative increase. [10]
    *   `Quality adj. no of initiated dates`: **`0.535`** (2 Roses) vs. **`0.806`** (8 Roses) — **`51 %*`** relative increase. [10]
*   **Panel B. Men (Regular Members):**
    *   `Have at least one initiated date`: **`0.308`** (2 Roses) vs. **`0.420`** (8 Roses) — **`36 %*`** relative increase. [10]
    *   `No of initiated dates`: **`0.556`** (2 Roses) vs. **`0.800`** (8 Roses) — **`44 %*`** relative increase. [10]
    *   `Quality adj. no of initiated dates`: **`0.540`** (2 Roses) vs. **`0.767`** (8 Roses) — **`42 %*`** relative increase. [10, 11]
*   **Panel C. Women:**
    *   `Have at least one initiated date`: **`0.218`** (2 Roses) vs. **`0.328`** (8 Roses) — **`50 %**`** relative increase. [11]
    *   `No of initiated dates`: **`0.379`** (2 Roses) vs. **`0.705`** (8 Roses) — **`86 %**`** relative increase. [11]
    *   `Quality adj. no of initiated dates`: **`0.369`** (2 Roses) vs. **`0.688`** (8 Roses) — **`86 %**`** relative increase. [11]

---

### **(b) ECDA Simulation and Field Outcomes**
*Source: “Integrating Predictive Models into Two-Sided Recommendations: A Matching-Theoretic Approach” (Sekiya et al., 2026)* [12]

#### **Synthetic Market Simulation Outcomes (Table 2):**
*   **`One-sided (like-sort)`:** Avg. Dates = **`0.2184`**, Avg. Effective Dates = **`0.1859`**, Dating Prob (Proposer) = **`0.1260`**, Dating Prob (Receiver) = **`0.1716`**, Avg. Likes = **`4.182`**. [13]
*   **`DA (like-sort)`** *(capacity \\(q_j = 25\\))*: Avg. Dates = **`0.2227`**, Avg. Effective Dates = **`0.1926`**, Dating Prob (Proposer) = **`0.1269`**, Dating Prob (Receiver) = **`0.1816`**, Avg. Likes = **`3.978`**. [13, 14]
*   **`One-sided (date-sort)`:** Avg. Dates = **`0.3543`**, Avg. Effective Dates = **`0.2317`**, Dating Prob (Proposer) = **`0.1527`**, Dating Prob (Receiver) = **`0.2237`**, Avg. Likes = **`3.531`**. [13]
*   **`DA (date-sort)`** *(capacity \\(q_j = 25\\))*: Avg. Dates = **`0.3030`**, Avg. Effective Dates = **`0.2312`**, Dating Prob (Proposer) = **`0.1407`**, Dating Prob (Receiver) = **`0.2233`**, Avg. Likes = **`3.736`**. [13, 14]
*   **`DA (date-sort, cap=40)`:** Avg. Dates = **`0.3372`**, Avg. Effective Dates = **`0.2436`**, Dating Prob (Proposer) = **`0.1495`**, Dating Prob (Receiver) = **`0.2340`**, Avg. Likes = **`3.675`**. [13]

#### **Empirical Market Simulation Outcomes (Table 3):**
*   **`One-sided (like-sort)`:** Avg Dates = **`0.0401`**, Avg Effective Dates = **`0.0241`**, Dating Prob (Proposer) = **`0.0288`**, Dating Prob (Receiver) = **`0.0344`**, Avg Likes = **`5.384`**. [15]
*   **`One-sided (date-sort)`:** Avg Dates = **`0.1231`**, Avg Effective Dates = **`0.0579`**, Dating Prob (Proposer) = **`0.0508`**, Dating Prob (Receiver) = **`0.0857`**, Avg Likes = **`3.693`**. [15]
*   **`Current`:** Avg Dates = **`0.1182`**, Avg Effective Dates = **`0.0584`**, Dating Prob (Proposer) = **`0.0493`**, Dating Prob (Receiver) = **`0.0863`**, Avg Likes = **`3.565`**. [15]
*   **`DA (date-sort, cap=140)`:** Avg Dates = **`0.1033`**, Avg Effective Dates = **`0.0605`**, Dating Prob (Proposer) = **`0.0424`**, Dating Prob (Receiver) = **`0.0904`**, Avg Likes = **`3.610`**. [15]
*   **`ECDA (like-exposure, cap=22.0)`:** Avg Dates = **`0.1054`**, Avg Effective Dates = **`0.0603`**, Dating Prob (Proposer) = **`0.0424`**, Dating Prob (Receiver) = **`0.0912`**, Avg Likes = **`3.308`**. [15]
*   **`ECDA (date-exposure, cap=1.5)`:** Avg Dates = **`0.0928`**, Avg Effective Dates = **`0.0623`**, Dating Prob (Proposer) = **`0.0401`**, Dating Prob (Receiver) = **`0.0932`**, Avg Likes = **`3.658`**. [15]

#### **Geographic Field Rollout DID Outcomes (Treat × Post):**
*   **Predicted Outcomes at Recommendation (Table 4a):**
    *   `Avg Dates`: **`-0.003***`** (s.e. `0.001`)
    *   `Avg Eff Dates`: **`0.001**`** (s.e. `0.000`)
    *   `DatProb(P)`: **`-0.001***`** (s.e. `0.000`)
    *   `DatProb(R)`: **`0.004***`** (s.e. `0.001`)
    *   `AvgLikes(R)`: **`0.415***`** (s.e. `0.054`). [16]
*   **Realized Full-Sample Outcomes (Table 4b):**
    *   `Avg Dates`: **`-0.002`** (s.e. `0.002`)
    *   `Avg Eff Dates`: **`0.002`** (s.e. `0.001`)
    *   `DatProb(P)`: **`-0.001`** (s.e. `0.001`)
    *   `DatProb(R)`: **`0.003`** (s.e. `0.002`)
    *   `AvgLikes(R)`: **`0.264***`** (s.e. `0.059`). [16, 17]
*   **Realized Post-Engagement Full-Sample Outcomes (Table 4c):**
    *   `AvgMsg(P)`: **`-0.002`** (s.e. `0.001`)
    *   `AvgMsg(R)`: **`-0.004*`** (s.e. `0.002`)
    *   `MsgProb(P)`: **`-0.001*`** (s.e. `0.001`)
    *   `MsgProb(R)`: **`-0.001`** (s.e. `0.001`). [17]
*   **Realized Outcomes Excluding Top 0.1% Receivers (Table 5a):**
    *   `Avg Dates`: **`0.003`** (s.e. `0.002`)
    *   `Avg Eff Dates`: **`0.003**`** (s.e. `0.001`)
    *   `DatProb(P)`: **`0.002*`** (s.e. `0.001`)
    *   `DatProb(R)`: **`0.005*`** (s.e. `0.002`)
    *   `AvgLikes(R)`: **`0.334***`** (s.e. `0.058`). [18]
*   **Realized Post-Engagement Excluding Top 0.1% Receivers (Table 5b):**
    *   `AvgMsg(P)`: **`0.000`** (s.e. `0.001`)
    *   `AvgMsg(R)`: **`0.000`** (s.e. `0.002`)
    *   `MsgProb(P)`: **`0.000`** (s.e. `0.001`)
    *   `MsgProb(R)`: **`0.000`** (s.e. `0.001`). [18]

---

### **(c) Nash-Social-Welfare Expected Matches, Envy, and Gini Reporting**
*Source: “Fair Reciprocal Recommendation in Matching Markets” (Tomita & Yokoyama, 2024)* [19]

*   **Expected Matches and Envy:** The exact numerical values for the expected matches and the number of envious pairs are **Not specified** as text-based tables in the paper's main body. They are reported graphically in **Figure 1** (for synthetic sweeps across the popularity parameter \\(\lambda\\)) and **Figure 2** (for the real-world dating platform dataset). [20, 21]
*   **Is any Gini reported?** **Not specified in source.** (The Gini coefficient is not evaluated or mentioned anywhere in this source's text or figures. *Note: Gini statistics cited in previous turns belonged to a different, excluded Tomita paper*). [19-126]

---

### **(d) Airbnb Cluster-Randomization Overall Interference Bias and Market-Tightness Subgroups**
*Source: “Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization...” (Holtz et al., 2025)* [127]

*   **Overall Interference Bias:**
    *   The meta-experiment establishes that "at least 20%" — specifically **`19.76%`** — of the individual-level (naive) TATE estimate is attributable to interference bias and is eliminated by cluster randomization. [128-130]
    *   In the joint regression analysis (Table 3, Column 1), the coefficient for `Individual-level Randomized × Treatment` is **`-0.068***`** (s.e. `0.018`), and the reported `Interference bias estimate, %` is **`19.76`** (with standard error/delta printed as `(69.06)`). [131, 132]
*   **Market-Tightness Subgroup Percentages (Table 3):**
    *   **Supply Constrained (Column 2):** Interference bias is estimated to be **`12.05%`** (reported as `12.05` with standard error/delta printed as `(611.55)`). [132, 133]
    *   **Demand Constrained (Column 3):** Interference bias is estimated to be **`28.65%`** (reported as `28.65` with standard error/delta printed as `(614.91)`). [132, 133]
*   **Statistical Significance of Subgroups:** **Not statistically established.** The difference between the supply-constrained and demand-constrained subgroup estimates is not statistically significant. The authors explicitly clarify: "although these results are consistent with both our hypothesis and the results reported in Johari et al. (2022), the difference between these two point estimates is not statistically significant... and hence, these results should only be considered suggestive." [133, 134]

---

### **(e) TEC Field Favorites and Match Outcomes**
*Source: “Designing Recommendation Exposure and Favorite Lists: A Field Experiment in a Spot-Work Platform” (Sekiya et al., 2026)* [135]

*   **Daily Favorites ("Fav") Outcome (Table 3, Panel c):**
    *   The estimated `Treatment × After` coefficient is **`-40.458`** (s.e. `51.977`). This represents a "null effect on this margin" and is statistically insignificant. [136, 137]
*   **Matches ("Match") Outcome (Table 3, Panel c):**
    *   The estimated `Treatment × After` coefficient is **`9.045**`** (s.e. `4.374`). This is positive and statistically significant (at the `p < 0.05` level), representing an ITT effect of **9.045 matches per prefecture-day**. [136, 137]
*   **Active Template-Day Outcomes (Table 3, Panel d):**
    *   `Avg Rec Workers (Active)`: **`0.571**`** (s.e. `0.253`). [136]
    *   `Avg Subscribers (Active)`: **`-0.082`** (s.e. `0.056`). [136]
    *   `Per-Round Fill Rate (Active)`: **`-0.002`** (s.e. `0.007`). [136]

