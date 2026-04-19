Date: 2026-04-12 (last updated — Phase 3.5: method-tracker sort + composite realignment + Top Method Analysis ranks 1–10.)
Topic: Proxy Label Learning / Learning with Noisy Labels

# Proxy Label Learning - Methodology Fundamentality Tracking

This file is accumulated automatically while reading papers during Phase 3 batch processing.
Update after each batch. **Rows sorted (Phase 3.5):** descending **Baseline Mention Count**; ties → descending **Fundamentality Composite Score**; ties → **Method Name** (A→Z).

## Methodology Table

| Method Name | Proposal Paper (Year) | Baseline Mention Count | Derived Variant Count | Independent Measured Performance (Dataset: metric | source) | Component Count | Simplicity Score (1-5) | Performance Consistency Score (1-5) | Fundamentality Composite Score |
|-------------|----------------------|----------------------|----------------------|--------------------------------------------------------|-----------------|----------------------|-------------------------------------|-------------------------------|
| Small-loss trick / Sample Selection | Various (Han et al. 2018, Jiang et al. 2018) | 4 | 5 | Used as mechanism in Co-teaching, DivideMix, MentorNet, ELR | 1 | 5 | 5 | 37 |
| Noise Transition Matrix (T) | Patrini et al., CVPR 2017 | 4 | 3 | CIFAR-100 asym N=0.6: forward 68.4% vs CE 17.1%; Clothing1M ResNet-50 best 80.38% vs 78.24% prior table; CIFAR-10/IMDB excerpts in source; **Dual-T** (Han NeurIPS 2020) reduces T estimation error via auxiliary classifier + dual loss (see read-papers; canonical PDF not `2006.07501`) | 2 | 4 | 3 | 28 |
| LUPI (Learning Using Privileged Information) | Vapnik & Vashist 2009 | 3 | 5 | Foundational framework — SVM+; cited by TRAM, TRAM++, Pi-DUAL, PFD | 1 | 5 | 3 | 30 |
| Co-teaching | Han et al., NeurIPS 2018 | 3 | 2 | MNIST Pair-45%: 87.63% (Co-teaching paper); CIFAR-10 Pair-45%: 72.62%; CIFAR-100 Sym-50%: 41.37% | 2 | 5 | 5 | 28 |
| DivideMix | Li et al., ICLR 2020 | 3 | 2 | CIFAR-10 Sym-90%: 76.0%; CIFAR-100 Sym-90%: 31.5%; WebVision top-1: 77.32%; Clothing1M: 74.76% | 3 | 4 | 5 | 27 |
| MentorNet | Jiang et al., ICML 2018 | 3 | 1 | CIFAR-10 40% noise: 89% (vs FullModel 69%); ImageNet 40%: 65.1%; WebVision: 70.8% | 3 | 4 | 4 | 23 |
| Temporal Ensembling (Target Estimation) | Laine & Aila 2018 | 2 | 2 | Used in ELR; foundational SSL technique | 2 | 5 | 4 | 23 |
| TRAM (Transfer and Marginalize) | Collier et al., ICML 2022 | 2 | 2 | CIFAR-10H: 70.1% (vs No-PI 67.0%); ImageNet: 72.5% (vs No-PI 71.7%); Civil Comments: 98.2% | 2 | 5 | 4 | 23 |
| GMM Loss Modeling | Arazo et al. 2019 (BMM); Li et al. 2020 (GMM) | 2 | 2 | Key component of DivideMix | 2 | 4 | 4 | 22 |
| ELR (Early-Learning Regularization) | Liu et al., NeurIPS 2020 | 2 | 1 | Clothing1M: 74.81%; WebVision top-1: 77.78%; CIFAR-10 Sym-90%: 75.2% | 2 | 5 | 4 | 21 |
| SCE (Symmetric Cross Entropy) | Wang et al., ICCV 2019 | 2 | 1 | CIFAR-100 Sym-80%: 15.00% vs GCE 8.43%; CIFAR-10 Sym-80%: 53.81% vs 40.81%; Clothing1M: 71.02% vs Forward 69.84% | 2 | 5 | 4 | 21 |
| TRAM++ | Ortiz-Jimenez et al., ICML 2023 | 2 | 1 | CIFAR-10H: 66.8% (vs TRAM 64.9%); CIFAR-10N: 83.9% (vs TRAM 80.5%); TRAM+SOP: 70.9% | 2 | 5 | 4 | 21 |
| SOP (Sparse Over-Parameterization) | Liu et al., ICML 2022 | 2 | 1 | CIFAR-10 Sym-80%: 68.32% (base), SOP+ 94.0%; Clothing-1M: 73.5%; WebVision top-1: 76.6%; CIFAR-10N Worst: 93.24% | 2 | 4 | 4 | 20 |
| CCN surrogate correction (unbiased \(\tilde\ell\) + \(\alpha\)-weighted / biased SVM) | Natarajan et al., NeurIPS 2013 | 1 | 2 | Linear synthetic 98.5% acc @ ρ=0.4; banana C-SVM 88.5% @ 0.4; competitive on 6 UCI vs RP/NHERD/PAM | 2 | 5 | 4 | 20 |
| Meta-gradient example reweighting (validation-aligned) | Ren et al., ICML 2018 | 1 | 2 | CIFAR-10 40% uniform flip: ~86.92% vs MentorNet ~76.6% w/ 1000 clean val (paper table excerpt) | 2 | 4 | 4 | 19 |
| Dual-T transition estimator (factorized T-club / T-spade) | Yao et al., NeurIPS 2020 | 1 | 1 | Clothing1M DT Revision 71.49% vs T Revision 71.01%; CIFAR-10 Sym-50 DT Co-teaching 71.49% vs T Co-teaching 39.71% (paper excerpts) | 3 | 4 | 4 | 17 |
| Taobao PFD (privileged+regular teacher, inner-product student) | Xu et al., KDD 2020 | 1 | 1 | CTR student AUC 0.6745 vs 0.6625 (1-day); PFD+MD 0.7160 vs 0.7042 (10-day); CVR 0.9135 vs 0.9040 (60-day); online +5.0% clicks / +2.3% conv | 3 | 4 | 4 | 17 |
| GJS (Generalized Jensen-Shannon Divergence Loss) | Englesson & Azizpour, NeurIPS 2021 | 1 | 0 | CIFAR-100 Sym-60%: 70.15% (+4.94pp over GCE 65.21%); WebVision top-1 (single): 77.99% vs DivideMix 77.32%; ILSVRC12 top-1: 74.33% vs ELR+ 70.29%; ANIMAL-10N: 84.2% vs PLC 83.4% | 2 | 5 | 4 | 16 |
| LogitClip | Wei et al., ICML 2023 | 1 | 0 | CIFAR-10 IDN-40%: CE+LC 86.60% vs CE 68.36% (+18.24%); WebVision: 65.12% vs CE 62.6%; DivideMix+LC: +0.74% | 2 | 5 | 4 | 16 |
| NLS (Negative Label Smoothing) | Wei et al., ICML 2022 | 1 | 0 | Clothing-1M: 74.24% (4th/21); CIFAR-10N Worst: 82.99%; CIFAR-100 Sym-60%: 46.58% vs CE 38.27% | 2 | 5 | 4 | 16 |
| PFD (Privileged Features Distillation) | Yang et al., NeurIPS 2022 (Amazon) | 1 | 2 | E-commerce LTR: multi-teacher +11.2%; Non-monotone: very high PI predictiveness → worse student | 3 | 3 | 3 | 16 |
| Identifiability Framework (Kruskal-based) | Liu, Cheng, Zhang 2023 | 1 | 0 | Theoretical: 3 i.i.d. noisy labels ↔ identifiability; IPIRM features reduce T-matrix error 3.73% vs. SimCLR 4.42% vs. WS 14.51% | 3 | 4 | 3 | 13 |
| Knowledge distillation (temperature softmax, dark knowledge) | Hinton et al., NIPS 2014 workshop | 0 | 6 | MNIST 800-hid student 74 vs 146 errs; speech distilled 60.8% frame / 10.7% WER vs 10-ens 61.1%/10.7%; JFT +specialists 25.0%→26.1% top-1 | 2 | 5 | 5 | 27 |
| Pi-DUAL | Wang et al., ICML 2024 | 0 | 1 | CIFAR-10H: 71.3% (+4.5 over TRAM++); ImageNet-PI high-noise: 62.1% (+6.8 over AFM); Pi-DUAL+: 83.23% | 3 | 4 | 5 | 16 |
| Data Programming | Ratner et al., NeurIPS 2016 | 0 | 3 | +2.34 avg F1 over distant supervision; TAC-KBP LSTM: +5.98 F1; user study: within 10 F1 of supervised | 3 | 3 | 3 | 15 |
| DebiasPL (ACDE logit debias + LAML + optional CLD) | Wang et al., CVPR 2022 | 0 | 1 | ImageNet-1K SSL 0.2% labels: up to +8.0 top-1 pts vs FixMatch+EMAN excerpt; +26% rel. / +9% rel. headline claims; CIFAR-10-LT +9.0 vs best FixMatch variant (NLM/table excerpts) | 3 | 4 | 4 | 14 |
| FINE (Filtering Noisy Instances via Eigenvectors) | Kim et al., NeurIPS 2021 | 0 | 2 | F-DivideMix CIFAR-10 Sym-90%: 90.5% vs DivideMix 76.0%; CIFAR-100 Sym-80%: 25.6% vs CRUST 21.7%; Clothing1M: 74.37% vs DivideMix 74.30% | 3 | 4 | 3 | 14 |
| ALIGN (noisy web image–text contrastive) | Jia et al., ICML 2021 | 0 | 1 | Flickr/MSCOCO retrieval SOTA excerpts; ImageNet zero-shot 76.4%; ImageNet fine-tune 88.64% | 3 | 3 | 4 | 13 |
| ANL (Active Negative Loss) | Ye et al., NeurIPS 2023 | 0 | 0 | CIFAR-10 Sym-80%: 61.27% vs 55.62%; WebVision: 67.44% vs 65.00%; Clothing-1M: 69.93% vs 69.07% | 2 | 5 | 4 | 13 |
| CausalNL (SCM + VAE + dual co-teaching) | Yao et al., arXiv 2021 | 0 | 1 | CIFAR-10 IDN-50 77.39% vs CE 39.42%; Clothing1M 72.24% vs T-Revision 70.97% (paper excerpts) | 4 | 3 | 4 | 13 |
| CDDC (covariance-based dynamic distribution calibration) | Zhang et al., ACM MM 2022 | 0 | 1 | WebVision 64.82%; Clothing1M 74.43% vs PLC 74.02%; DivideMix-C WebVision 77.62% (paper excerpts) | 4 | 3 | 4 | 13 |
| Label Wave (Early Stopping / PC Metric) | ICLR 2024 | 0 | 0 | CIFAR-10 Sym-40% CE: 80.15% (oracle: 80.45%); ELR+LW: 90.45% vs ELR 87.2%; CIFAR-100 Sym-80%: 35.2% vs 21.8% | 1 | 5 | 4 | 13 |
| MDDC (mean-based dynamic distribution calibration) | Zhang et al., ACM MM 2022 | 0 | 1 | WebVision 65.06% vs PLC 63.90%; Clothing1M 74.39% vs PLC 74.02% (Table 3 excerpt) | 4 | 3 | 4 | 13 |
| Mixup + min-k labeled + soft pseudo-labels (confirmation-bias SSL) | Arazo et al., arXiv 2019 | 0 | 1 | CIFAR-10 500 lbl: 13.68% val err (M*); SVHN 250: 3.66% test err; Mini-ImageNet 4k: large margin vs LP in paper tables | 4 | 3 | 4 | 13 |
| UPS (uncertainty-aware pseudo-label selection + negative PL) | Rizve et al., ICLR 2021 | 0 | 1 | CIFAR-10 1000 lbl: 8.18% err; CIFAR-10 4000: 6.39%; CIFAR-100 10k lbl: 32.00%; UCF-101 50% lbl: 50.2%; VOC2007 mAP 40.34% @20% labels | 4 | 3 | 4 | 13 |
| CLID (normalized pCTR list-CE distillation) | Gui et al., WSDM 2024 | 0 | 0 | Production +0.38% GAUC vs Base with +0.02% LogLoss vs Base+ListMLE +0.78% LogLoss; Web30K NDCG@10 0.4495 vs Base 0.4478 (NLM tables) | 3 | 4 | 4 | 12 |
| DST (decoupled heads + worst-case adversarial features) | Chen et al., NeurIPS 2022 | 0 | 1 | +6.3% avg vs SSL SOTA from scratch; +18.9% vs FixMatch on 13 transfer tasks; CIFAR-100 worst-20-class acc 1.0%→34.5% | 4 | 2 | 4 | 12 |
| FBR (feature similarity surrogate for meta-reweighting) | Zhang et al., arXiv 2025 | 0 | 0 | CIFAR-100 40% asym: 73.2% vs FINE 61.7%; Clothing1M 74.16%; CIFAR-10N Worst 85.6% vs Co-teaching 83.3% (paper tables) | 3 | 4 | 4 | 12 |
| GRM (LM-head regularized reward model) | Yang et al., NeurIPS 2024 | 0 | 0 | HHH 73.4→79.8, MT-Bench 71.2→73.4 @400K; RewardBench avg 76.3→79.5 (Mistral-7B linear head); 8B scaling 84.7→87.0 RewardBench avg (paper tables) | 3 | 4 | 4 | 12 |
| L1 marginal pseudolikelihood structure learning (generative WS deps) | Bach et al., ICML 2017 | 0 | 0 | ~100× faster than MLE+Gibbs structure search; ~1/4 extraneous deps vs MLE; +1.5 F1 avg (IE tasks) vs conditionally independent LM | 3 | 4 | 4 | 12 |
| SGN (Shifted Gaussian Noise) | ICLR 2024 | 0 | 0 | CIFAR-100 Asym-40%: 71.01% vs NAL 58.01% (+13pp); CIFAR-100N Worst: 60.36%; Clothing1M: 73.9%; WebVision: 77.2% | 3 | 4 | 4 | 12 |
| SoftMatch (truncated-Gaussian pseudo-label weights + UA) | Chen et al., ICLR 2023 | 0 | 0 | CIFAR-100 400 lbl: +7.73% vs FlexMatch excerpt; CIFAR-10-LT γ=150: +2.4% vs 2nd best excerpt | 3 | 4 | 4 | 12 |
| AdaptCDRP (Conditional DRO) | Guo, Yi, Wang NeurIPS 2024 | 0 | 0 | CIFAR-10N: 88.25% vs 87.23%; CIFAR-100 IDN-High: 54.24% vs 46.12%; Animal-10N: 83.08% | 3 | 3 | 4 | 11 |
| Bayes-label transition matrix (BLTM) + forward correction | Yang et al., ICML 2022 (arXiv 2105.13001) | 0 | 1 | Instance-dependent BLTM vs CLTM; distilled Bayes labels + transition network (Batch 1 read-papers) | 3 | 3 | 3 | 11 |
| BLTM + Bayes label transition network (parametric DNN) | Yang et al., ICML 2022 | 0 | 0 | Clothing1M BLTM-V 73.39% vs PTD 70.07%; CIFAR-10 IDN-40 +7.01pp vs PTD (paper excerpts) | 4 | 3 | 4 | 11 |
| Co-teaching+ (disagreement filter + small-loss cross-update + \(\lambda(e)\) schedule) | Yu et al., ICML 2019 | 0 | 0 | Tiny-ImageNet sym 50% max 41.77% vs Co-teaching 37.60% vs MentorNet 35.76%; Open-set CIFAR-10+SVHN 40% noise max 80.95% vs Iterative 77.73% (paper excerpts) | 3 | 3 | 4 | 11 |
| COINNet (Instance-Dependent Outliers) | Ying et al., NeurIPS 2024 Spotlight | 0 | 0 | CIFAR-10N: 92.09% vs Max-MIG 90.11%; ImageNet-15N: 93.71% vs 81.13%; CIFAR-100N: 65.22% vs 64.77% | 3 | 3 | 4 | 11 |
| DeFT (VLM Noisy Label Detection) | Wei et al., NeurIPS 2024 | 0 | 0 | CIFAR-100N: 79.04% vs UNICON 77.68%; Clothing1M: 72.44%; WebVision: 85.12% | 3 | 3 | 4 | 11 |
| HA-PFD (focal logit PFD + latent layer alignment + MI feature pick) | Yuan et al., KDD 2025 (ByteDance) | 0 | 0 | Douyin offline HA-PFD V2 test AUC 0.88772 vs Review 0.88698; online +1.426% conversions, +3.739% advertiser value vs MTL (paper tables via NLM) | 4 | 3 | 4 | 11 |
| Hyper Label Model (HLM, GNN one-pass label aggregation) | Wu et al., ICLR 2023 | 0 | 0 | 14 WRENCH: 69.0 vs CLL 67.6 avg; ~6× speed vs best-accuracy baseline; end-model avg 69.4 vs CLL 68.1 | 4 | 3 | 4 | 11 |
| MAL (AKA multi-attribution towers + CAT + PTP knowledge add) | Chen et al., CIKM 2025 (Alibaba) | 0 | 0 | Taobao offline +0.51% GAUC / +0.14% AUC (Last-Click primary); online +2.6% ROI, +2.7% GMV (NLM); ablation +0.01% GAUC if towers use only primary | 4 | 3 | 4 | 11 |
| MO-LTR-MD (per-objective teachers → soft label → single student; self-distill) | Tang et al., KDD 2024 (Airbnb) | 0 | 0 | Offline +1.1% NDCG; online +0.37% bookings p=0.02; −1.6% serving latency vs multi-model fusion (NLM) | 4 | 3 | 4 | 11 |
| PENCIL (probabilistic end-to-end label distributions; reversed KL + compatibility + entropy) | Yi & Wu, CVPR 2019 (arXiv 1903.07788) | 0 | 0 | CIFAR-10 sym 90%: 61.21% vs Tanaka et al. 54.36% vs CE 50.74% (best); Clothing1M noisy-only 73.49% vs Tanaka 72.16% vs Forward 69.84% vs CE 68.94%; CUB-200 +0.71pp over CE in reported row | 4 | 3 | 4 | 11 |
| RepReg (Representation Regularization) | Cheng et al., ICLR 2023 | 0 | 0 | CIFAR-10N Worst: 88.74%; CIFAR-100N: 60.81%; Clothing1M: 73.48%; CIFAR-10 Sym-80% last: 56.78% vs CE 15.05% | 3 | 3 | 4 | 11 |
| WSL / weighted soft labels (per-sample KD reweighting) | Zhou et al., arXiv 2021 | 0 | 0 | CIFAR-100 WRN-40-2→16-2: 76.05% vs KD 73.33 vs CRD 75.51; ImageNet R34→R18: 72.04% top-1; MultiNLI BERT-12→3: 76.28% | 2 | 5 | 3 | 11 |
| CLIP training-free clean selection + LNABM (transition-matrix + class-frequency margins) + focal on selected subset | Liang et al., arXiv 2023 (`2310.10463`) | 0 | 0 | CIFAR-10 sym 90%: **89.2%** vs DivideMix **75.4%**; CIFAR-100 sym 90%: **45.7%** vs **31.0%**; WebVision top-1 **79.08%** vs DivideMix **77.32%**; Red Mini-ImageNet +**2.9–6.0%** vs InstanceGM by noise rate; CIFAR-10N Aggregate **95.95%** vs DivideMix **95.33%** (paper tables via NLM) | 4 | 2 | 4 | 10 |
| CrossSplit | Kim et al., ICML 2023 | 0 | 0 | CIFAR-10 Asym-40%: 96.0% vs UNICON 94.1%; CIFAR-100 Sym-90%: 52.4% vs UNICON 44.8%; CIFAR-100 Sym-92%: 46.25% vs 32.08%; mini-WebVision: 78.48% vs UNICON 77.60% | 3 | 4 | 3 | 10 |
| CSGN (Latent Causal Structure) | NeurIPS 2024 | 0 | 0 | CIFAR-10 IDN-50%: 95.88% vs DivideMix 86.30%; CIFAR-100N: 71.99%; WebVision: 79.84% | 4 | 2 | 4 | 10 |
| CSOT (Curriculum Structure-Aware OT) | Chang, Shi, Wang NeurIPS 2023 | 0 | 0 | CIFAR-100 Sym-90%: 50.5% vs UNICON 44.8%; WebVision top-1: 79.67%; Clothing1M: 75.16% | 4 | 2 | 4 | 10 |
| LLPFC (LLP via Forward Correction) | Zhang, Wang, Scott NeurIPS 2022 | 0 | 0 | Outperforms LLP baselines on CIFAR-10/100; primarily theoretical (excess risk bound via T-norm) | 2 | 4 | 3 | 10 |
| LRA-diffusion (label retrieval + label diffusion) | Chen et al., NeurIPS 2023 | 0 | 0 | CIFAR-10 35% PMD: CLIP LRA 96.54% vs C2D+SimCLR 85.61%; WebVision 84.16%; Food-101N 93.42% | 4 | 2 | 4 | 10 |
| NMTune | Chen et al., ICLR 2024 | 0 | 0 | Swin-L OOD: 52.35% (vs LP 50.88%); ConvNext-L OOD: 70.30% (vs LP 66.86%); text-ada-002 OOD: 53.48% (vs LP 44.06%) | 3 | 4 | 3 | 10 |
| Optimal masked surrogate (linear KD / W2S theory) | Ildiz et al., arXiv 2024 | 0 | 0 | Sharp non-asymptotic risk; W2S can beat strong labels in theory; scaling exponent unchanged; CIFAR NN: surrogate-to-target > surrogate but < strong baseline | 2 | 4 | 3 | 10 |
| Pseudo-labeling unification (fuzzy partitions + stochastic labels) + cross-SSL/UL/KD taxonomy | Kage et al., arXiv 2024 review | 0 | 0 | Table 1 excerpts: CIFAR-10-4k / ImageNet-10% compiled SOTA numbers (e.g., BLOPL 96.88; MPL 96.11 / 73.89; FixMatch 95.74 / 71.5) | 2 | 4 | 3 | 10 |
| SAM robustness under label noise (1-SAM / J-SAM decomposition) | Baek et al., ICLR 2024 | 0 | 0 | CIFAR-10 30% noise: 1-SAM 69.47% vs SGD 52.48%; J-SAM 69.17%; explicit reg SGD 60.8% | 2 | 4 | 3 | 10 |
| SEAD (Self-auxiliary distillation; bilateral-branch auxiliary + selector) | Yin Zhang et al., RecSys 2024 | 0 | 0 | Google production pCTR +0.35%/+0.20% AUC, pCVR +0.26% AUC; iOS signal-loss +17% / +3% SKAN AUC (paper tables) | 3 | 4 | 3 | 10 |
| TDSM (transition-aware weighted DSM) | Na et al., ICLR 2024 | 0 | 0 | CIFAR-10 40% sym: CW-FID 30.45→15.92; CAS 47.21→62.28; Clothing1M FID 6.67→4.94 | 4 | 2 | 4 | 10 |
| Δ–γ soft-label learnability (biased teachers) | Yuan & Xu, arXiv 2023 | 0 | 0 | PLL CIFAR-10 93.98% @ Δ=γ=0.1; students trained on <30%-acc soft labels approach GT-trained caps (95.29% / 78.13% refs) | 3 | 4 | 3 | 10 |
| CDNL (Causal Structure Detection for Noisy Labels) | Yao et al., ICML 2023 | 0 | 0 | CDNL flip-rate estimation error ≈ 0 vs. VolMinNet high error; anticausal: DivideMix 94.50% vs Forward 74.72% (CIFAR-10 IDN-40%) | 3 | 3 | 3 | 9 |
| Instance-level memorization / disparate impact (long-tail noise) | Liu, 2021 / ICML framing in survey | 0 | 0 | Theoretical: robust methods fix high-frequency errors; rare instances fail (memorization paradox); loss correction vs label smoothing tradeoffs | 1 | 5 | 2 | 9 |
| Instance-level memorization analysis (disparate impacts/treatments) | Liu, ICML 2021 | 0 | 0 | Theorems/bounds + 2D + CIFAR-10 loss-distribution illustrations (not a new SOTA trainer) | 1 | 5 | 2 | 9 |
| MDDC (mean / covariance dynamic distribution calibration, IDN) | Zhang et al., 2022 (arXiv 2210.05126) | 0 | 0 | Gaussian calibration of deep features; mean-based + covariance-based; mitigates distribution shift from IDN | 3 | 3 | 3 | 9 |
| Neural Relation Graph | Kim, Yun, Song, NeurIPS 2023 | 0 | 0 | ImageNet 8% noise: AP 0.526 vs Margin 0.484; TNR95 0.695 vs 0.521; ESC-50: AP 0.779 vs 0.739; SST2: AP 0.881 vs 0.861 | 3 | 3 | 3 | 9 |
| Noise Shape Analysis (feature-dependent) | Oyen et al., NeurIPS 2022 | 0 | 0 | GapMax 20% noise → near-chance accuracy (vs uniform 80% → minimal degradation); CleanLab/CoTeaching fail under feature-dependent noise | 1 | 5 | 2 | 9 |
| On-policy + coreset active querying for proxy evaluator (`M_eval`) | Chen et al., arXiv 2024 | 0 | 0 | ~9× DPO pair labeling vs queried EFT; >1% avg AlpacaEval2+MMLU @ ~1.7K queries vs <0.1% direct labeling (paper claims) | 4 | 3 | 3 | 9 |
| Snorkel / Data Programming | Ratner et al., VLDB 2017 | 0 | 0 | — | 3 | 3 | 3 | 9 |
| SSL “\(L_s+\mu L_u\)” taxonomy (consistency / pseudo / hybrid + pretrain interplay) | Weng, 2021 blog | 0 | 0 | Aggregated pointers (CIFAR-10 supervised refs 5.4/2.7 err bars in UDA figure caption; Zoph/Chen findings summarized) | 1 | 5 | 2 | 9 |
| Tree-structured preference RM + IBN topology (RLHF) | Qiu et al., arXiv 2024 | 0 | 0 | ~65% avg GPT-4 win vs chain-RM (HH-RLHF/GSM-8K/DialogSum); GSM-8K acc 0.51 vs 0.43 chain / 0.41 DPO / 0.36 SFT (paper tables) | 4 | 3 | 3 | 9 |
| WRENCH (WS benchmark harness + LF generators) | Zhang et al., NeurIPS 2021 | 0 | 0 | 22 datasets / 120+ method variants — infrastructure not a single accuracy | 4 | 3 | 3 | 9 |
| Multi-task tri-training (MT-Tri) + orthogonality + target-only pseudo-head | Ruder & Plank, ACL 2018 (surveyed in Ruder 2018 blog) | 0 | 0 | NLP SSL + domain shift: classic tri-training described as strong vs recent methods (qualitative; exact task tables not in blog excerpt) | 3 | 4 | 2 | 8 |
| Source-aware Influence Function (PWS loss decomposition) | Zhang et al., NeurIPS 2022 | 0 | 0 | +9–37% AP vs LM/EM/KNN on LF mislabeling; +13–24% vs ordinary IF on test-loss improvement (paper-reported ranges) | 4 | 2 | 3 | 8 |

## How to Compute the Fundamentality Composite Score

```
score = (baseline_mention_count × 3)
      + (derived_variant_count × 2)
      + (performance_consistency_score × 2)
      + simplicity_score
      - (complexity_penalty)   # -1 if components ≥ 6 and hard to reproduce
```

Simplicity score 1–5 (5 = simplest):
- 5: ≤ 3 components, ≤ 2 hyperparameters
- 4: 3–4 components, 3 hyperparameters
- 3: 4–5 components, 3–4 hyperparameters
- 2: 5–6 components, 4–5 hyperparameters
- 1: ≥ 6 components, ≥ 5 hyperparameters or widely noted as hard to reproduce

Performance consistency score 1–5 (5 = most consistent):
- Determined by how consistently the method beats baselines across ≥ 3 independent papers

**Phase 3.5:** Rows that previously used an em dash (—) for performance consistency were assigned an integer **1–5** using the same rubric (theory-only / infrastructure / blog-survey entries trend **2–3**; widely benchmarked trainers trend **4–5**). **Complexity penalty:** no current row has `Component Count ≥ 6`, so **no row** applies the optional `−1` penalty in this tracker snapshot.


## Top Method Analysis

Composite-based ranks (1–10) use the **Fundamentality Composite Score** after Phase 3.5 realignment; tie-breakers follow the methodology table (higher baseline mention, then method name).

### Rank 1 — Small-loss trick / Sample Selection
- **Why fundamental:** It turns the empirical “clean examples fit first” observation into a reusable training-time filter, making large-scale learning with noisy labels tractable without extra annotators.
- **Representative citation:** Han et al., NeurIPS 2018 (Co-teaching); Jiang et al., ICML 2018 (MentorNet)—canonical instantiations cited in the tracker.
- **Surveyed baselines (`read-papers/`):** `2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md`; `2023_arXiv_NA_Combating-Label-Noise-With-A-General.md`; `2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md` (tables/discussion vs Co-teaching+, MentorNet, DivideMix, ELR+); additional LNL comparators in **method-tracker** rows / NLM batch notes.
- **Variants / extensions:** Cross-peer updates (Co-teaching), learned curriculum gates (MentorNet), disagreement-first pools (Co-teaching+), composition with GMM/two-component loss modeling (DivideMix lineage).
- **Performance range:** Not a single architecture—see linked methods (e.g., tracker Co-teaching CIFAR-10 Pair-45% **72.62%**; Liang et al. `2310.10463` tables report **~89.2%** @ CIFAR-10 sym 90% vs DivideMix **75.4%** in that paper’s excerpt).

### Rank 2 — LUPI (Learning Using Privileged Information)
- **Why fundamental:** It formalizes settings where training-time side information is richer than test-time inputs, which is the conceptual backbone for privileged distillation in ads/ranking and many PI-transfer papers in this survey.
- **Representative citation:** Vapnik & Vashist 2009 (tracker entry; LUPI / SVM+ framing).
- **Surveyed baselines (`read-papers/`):** `2024_WSDM_CLID_Calibration-Compatible-Listwise-Distillation-Privileged-Features.md`; `2025_KDD_HA-PFD_Hardness-aware-Privileged-Features-Distillation-CVR.md`; `2020_KDD_NA_Privileged-Features-Distillation-Taobao.md` (PFD-style privileged teacher–student); TRAM/Pi-DUAL discussion in tracker performance cells.
- **Variants / extensions:** PFD/KD variants (Taobao PFD, HA-PFD), TRAM/TRAM++/Pi-DUAL transfer-and-marginalize family, calibration-aware listwise distillation (CLID).
- **Performance range:** Domain-specific (e.g., HA-PFD offline test AUC **0.88772** vs ReviewKD **0.88698** in tracker excerpt).

### Rank 3 — Noise Transition Matrix (T)
- **Why fundamental:** It parameterizes label corruption as a structured linear map on class probabilities, enabling correction losses and identifiability discussions that recur across vision, web-noise, and weak-supervision settings.
- **Representative citation:** Patrini et al., CVPR 2017 (*Making Deep Neural Networks Robust to Label Noise: A Loss Correction Approach*).
- **Surveyed baselines (`read-papers/`):** `2017_CVPR_NA_Loss-Correction-Label-Noise.md`; `2020_NeurIPS_DualT_Dual-T-Reducing-Estimation-Error-Transition-Matrix.md`; `2019_CVPR_PENCIL_Probabilistic-End-to-End-Noise-Correction.md` (explicitly contrasts “no known T” regimes); Liang `2310.10463` notes (CLIP-estimated **T** for margin shaping).
- **Variants / extensions:** Forward vs backward correction, Dual-T factorizations, instance-dependent / Bayes transition networks (see related tracker rows).
- **Performance range:** Tracker excerpts include CIFAR-100 asym **68.4%** (forward) vs CE **17.1%**; Clothing1M ResNet-50 **80.38%** vs prior **78.24%** in the cited table.

### Rank 4 — Co-teaching
- **Why fundamental:** Dual networks with peer-selected small-loss batches mitigate single-network confirmation bias and remain a standard robust-learning comparator family.
- **Representative citation:** Han et al., NeurIPS 2018.
- **Surveyed baselines (`read-papers/`):** `2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md`; Liang `2310.10463` read-papers (Co-teaching+ in baseline tables); `2023_arXiv_NA_Combating-Label-Noise-With-A-General.md` (Co-teaching / small-loss baselines).
- **Variants / extensions:** Co-teaching+, JoCoR/JoSRC-style coupling (per Liang notes), hybrids with transition-matrix and sample-selection pipelines.
- **Performance range:** Tracker: CIFAR-10 Pair-45% **72.62%**; CIFAR-100 Sym-50% **41.37%** (paper excerpts).

### Rank 5 — DivideMix
- **Why fundamental:** It combines **GMM-based** loss splitting with **SSL-style** clean/noisy partitioning, giving a practical end-to-end recipe for extreme synthetic noise and large web datasets.
- **Representative citation:** Li et al., ICLR 2020.
- **Surveyed baselines (`read-papers/`):** `2023_arXiv_NA_Combating-Label-Noise-With-A-General.md`; `2023_arXiv_NA_Combating-Label-Noise-General-Surrogate-Sample-Selection.md` (reproduced DivideMix comparisons); broadly referenced across LNL `read-papers/` in this topic folder.
- **Variants / extensions:** DivideMix + auxiliary objectives (e.g., LogitClip row), filtering-augmented variants (FINE / F-DivideMix lineage in tracker).
- **Performance range:** Tracker: CIFAR-10 Sym-90% **76.0%**; WebVision top-1 **77.32%**; Clothing1M **74.76%**.

### Rank 6 — Knowledge distillation (temperature softmax, dark knowledge)
- **Why fundamental:** Logit-level matching defines how “teacher knowledge” becomes a **trainable proxy target**, linking classical compression to modern weak-to-strong and privileged-information chains surveyed here.
- **Representative citation:** Hinton et al., NIPS 2014 workshop; surveyed read-paper `2014_NIPS_NA_Distilling-the-Knowledge-in-a-Neural-Network.md`.
- **Surveyed baselines (`read-papers/`):** PFD/CLID/HA-PFD/MO-LTR-MD and related distillation read-papers in this survey; when a note does not enumerate KD explicitly, use **method-tracker** derived-variant counts + NLM batch notes.
- **Variants / extensions:** Temperature scaling, ensemble teachers, self-distillation, listwise pCTR matching (CLID), hardness-aware weighting (HA-PFD).
- **Performance range:** Tracker includes MNIST student vs teacher error (**74 vs 146** errs) and other domain excerpts—ranges are task-dependent.

### Rank 7 — MentorNet
- **Why fundamental:** Learning a data-driven curriculum for example weights generalizes fixed heuristics and influenced later meta-reweighting / robust-training designs.
- **Representative citation:** Jiang et al., ICML 2018.
- **Surveyed baselines (`read-papers/`):** `2019_ICML_CoTeachingPlus_Disagreement-Label-Corruption.md`; Liang `2310.10463` baseline lists (MentorNet/MentorMix family); overlaps with small-loss survey notes in `2023_arXiv_NA_Combating-Label-Noise-With-A-General.md`.
- **Variants / extensions:** MentorMix (per Liang notes), schedules combining curriculum gates with robust trainers.
- **Performance range:** Tracker: CIFAR-10 40% noise **~89%** vs FullModel **69%** excerpt; ImageNet 40% **65.1%**; WebVision **70.8%**.

### Rank 8 — Temporal Ensembling (Target Estimation)
- **Why fundamental:** Temporal smoothing of targets reduces variance in semi-supervised / noisy training and is a recurring sub-component inside modern composite objectives (e.g., ELR-related pipelines).
- **Representative citation:** Laine & Aila, Temporal Ensembling (2016 workshop / ICLR 2017 line).
- **Surveyed baselines (`read-papers/`):** `2021_Blog_NA_Semi-Supervised-Learning-Not-Enough-Data.md` (mentions temporal ensembling in SSL taxonomy); paper-level baseline tables otherwise defer to **method-tracker** / NLM notes (ELR linkage in tracker).
- **Variants / extensions:** Mean Teacher and other EMA-teacher successors; hybrids with consistency regularization and pseudo-labeling.
- **Performance range:** Typically reported **inside** composite methods rather than as a standalone SOTA number in this tracker.

### Rank 9 — TRAM (Transfer and Marginalize)
- **Why fundamental:** It provides an explicit PI-transfer objective (marginalizing privileged signals) connecting LUPI-style side information to deep networks under shift.
- **Representative citation:** Collier et al., ICML 2022.
- **Surveyed baselines (`read-papers/`):** No dedicated TRAM filename in the current `read-papers/` batch list—**see method-tracker table / NLM batch notes** for Pi-DUAL/TRAM++ comparative citations.
- **Variants / extensions:** TRAM++, Pi-DUAL (+) in tracker.
- **Performance range:** Tracker: CIFAR-10H **70.1%** vs No-PI **67.0%**; ImageNet **72.5%** vs **71.7%**; Civil Comments **98.2%**.

### Rank 10 — GMM Loss Modeling
- **Why fundamental:** Modeling the loss distribution as a **two-component mixture** turns heuristic small/large-loss splits into a probabilistic clean-vs-noisy mechanism that anchors DivideMix-style training.
- **Representative citation:** Arazo et al., 2019 (BMM); Li et al., 2020 (DivideMix)—tracker proposal column.
- **Surveyed baselines (`read-papers/`):** `2023_arXiv_NA_Combating-Label-Noise-With-A-General.md` (Arazo et al. / GMM references); Liang `2310.10463` text comparing selection to **GMM** baselines.
- **Variants / extensions:** BMM parameterizations; composition with SSL losses and robust baselines (Co-teaching family) per DivideMix ablations.
- **Performance range:** Read primarily through **DivideMix** headline numbers (Rank 5); mixture fitting is modular rather than a single standalone accuracy in this tracker.

