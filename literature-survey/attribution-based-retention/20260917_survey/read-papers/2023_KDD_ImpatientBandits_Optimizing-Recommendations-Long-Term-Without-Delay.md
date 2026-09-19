
# Impatient Bandits: Optimizing Recommendations for the Long-Term Without Delay

**Source:** https://arxiv.org/pdf/2307.09943.pdf | **NLM source id:** efd1746f-02ac-4f6a-8849-446ff29ee4e2 | **Year / venue:** KDD 2023 (arXiv 2307.09943) | **Authors / affiliation:** Thomas M. McDonald (Univ. of Manchester, internship at Spotify), Lucas Maystre, Mounia Lalmas, Kamil Ciosek (Spotify), Daniel Russo (Columbia University & Spotify) | **Analyzed:** 2026-09-17 (NotebookLM, 2 queries)

## 1. Summary
Addresses the cold-start "content exploration" problem for new podcast shows when the true long-term reward (habitual engagement over 60 days) is delayed, creating a trade-off between waiting weeks for the full signal (slow learning) and using fast short-term proxies (misaligned with the real goal). **Unit of decision:** per candidate item (podcast show, a bandit arm) — this is a non-contextual, non-personalized bandit; it explicitly integrates out individual-user heterogeneity rather than crediting individual user interactions. **Outcome optimized:** "stickiness" — expected number of days (0–59) a user engages with a show in the 60 days following a first listen ("discovery"). **Method:** models "progressive feedback" — daily binary activity indicators z₁...z₅₉ revealed with increasing delay — via a Bayesian filter that maintains an exact Gaussian posterior belief over the full activity trace from partial observations, with prior mean/covariance (μ, Σ) and noise covariance (V) meta-learned from historical shows; a Thompson-sampling "Impatient Bandit" algorithm samples from this belief each round to balance exploration/exploitation. No selection-bias/confounding correction is attempted (non-contextual setting), but the paper does sketch a contextual extension conditioning on user embeddings.

## 2. Evidence
- **Data:** real-world Spotify podcast-discovery logs (anonymized, category names obfuscated for confidentiality); reward = number of engaged days out of 59 following a discovery, observed with a 60-day delay.
- **Baselines:** *Delayed* (wait for the full 60-day reward before updating), *Day-two proxy* (treat day-2 return as the reward, representative of CTR/dwell-time-style short-term proxies), *Oracle* (unrealistic — full 60-day trace available immediately, upper bound).
- **Results:** stickiness predictions are already fairly accurate after only ~10 days of observation and improve further with more days/user traces (Figure 3, MAE curves for M=10/100/1000 traces). Per-step regret (Figure 5): the delayed approach stays poor for the first 60 rounds due to pure delay; the day-two proxy tracks the proposed method for about a month but then plateaus at high, non-zero regret because the proxy is misaligned; the proposed progressive/impatient-bandit approach tracks closest to the oracle and also explores more broadly early on (higher action-entropy) than the day-two proxy, which collapses onto a small subset of shows.

## 3. Limitations
- Explicitly non-personalized: "we do not foresee any major difficulty" extending to a personalized/contextual setting, but only a sketch (Appendix C, conditioning on user embeddings) is provided, not implemented or evaluated.
- Assumes traces are approximately Gaussian even though the underlying activity indicators are binary — acknowledged as a modeling simplification.
- No formal theoretical characterization of the regret benefit of progressive feedback vs. fully delayed feedback is given; left as future work.
- Category names/business specifics are obfuscated for confidentiality, limiting external reproducibility of the exact deployment setting.

## 4. Prior works named
- Maystre et al. (2024) — defined "clickiness" (CTR) and "stickiness" (59-day engagement) for podcast recommendation; this paper's direct predecessor and source of the reward definition, but did not address the content-exploration/cold-start problem.
- Rasmussen et al. — Gaussian-process-style Bayesian filter update equations used for the iterative belief update.
- Thompson sampling literature (bandit exploration-exploitation via posterior sampling).
- Multi-armed bandit formalization of content/cold-start exploration (general bandit literature, cited generically).
- Short-term proxy metrics literature (CTR, dwell time, conversion rate) used to motivate and construct the day-two-proxy baseline.

## 5. Project Relevance
- **Answers:** Q2, direct (an industry paper — Spotify — explicitly about forecasting a delayed, retention-like outcome from early interaction signals, cited by the survey as "Q2 direct").
- **Attributes retention to individual interactions?** No — forecasts population/item-level delayed engagement (stickiness) from early aggregate activity traces; does not attribute retention to a specific user's individual historical interactions (swipes/likes), and explicitly integrates out user-level heterogeneity in its core (non-contextual) model.
- **Transferable components:** intermediate-outcome/trace forecasting (using early post-exposure signals to predict a delayed N7-style outcome without waiting the full window) is highly relevant; the Bayesian filter over partial traces and meta-learned prior/noise covariances that encode how predictive early signals are of later ones; Thompson-sampling exploration under delayed reward.
- **Required changes:** move from a non-contextual, per-item bandit to a contextual, per-user multi-touch attribution model; expand the homogeneous daily-activity trace to heterogeneous interaction types (swipe/like/match/message); replace the single terminal 60-day cumulative reward with a recurring daily N7 binary retention target evaluated on rolling reference dates.
- **On last-touch:** does not name last-touch/last-click explicitly, but its central empirical finding — that a short-term proxy (day-two return) tracks well briefly then plateaus at high regret because it's misaligned with the true long-term goal — is a direct structural argument against the production baseline's late-only/most-recent-swipe credit rule.
- **Transfer rating:** adaptable — the progressive-feedback/early-signal-forecasting machinery is directly reusable for early N7-retention prediction, but attributing that retention to specific prior swipes requires moving well beyond this paper's non-personalized, single-item bandit framing.
