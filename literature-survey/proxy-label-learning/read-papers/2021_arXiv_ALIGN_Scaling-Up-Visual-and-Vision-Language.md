Date: 2026-04-12
Source: https://arxiv.org/pdf/2102.05918
NLM Source ID: 9c12099c-02c5-4980-a6e0-4ad3af2c8ca4
Venue: arXiv 2021
Relevance: Related
Priority: 1

# Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision (ALIGN, ICML 2021)

**Authors:** Not specified in source.
**Affiliation:** Not specified in source.

## Contribution, method, and experimental setup (NLM Q1)

**(1) Core problem and key contribution**

The **core problem** identified by the authors is that learning high-quality visual and vision-language representations typically relies on heavily curated, cleanly annotated training datasets (such as ImageNet, MSCOCO, or Conceptual Captions) [1-3]. This expensive and time-consuming curation bottleneck restricts dataset sizes (usually limited to around 10 million examples), which fundamentally hinders the ability to scale up trained models [1, 3].

The **key contribution** of this paper is demonstrating that **scale can compensate for noise** [1]. The authors introduce a method to learn state-of-the-art representations by leveraging a massive dataset of **1.8 billion naturally noisy image alt-text pairs** obtained from the web, completely bypassing the need for complex, expensive human filtering, balancing, or semantic cleaning [1, 3-5].

**(2) Proposed method or architecture in detail**

The proposed model, named **ALIGN** (A Large-scale ImaGe and Noisy-text embedding), utilizes a **simple dual-encoder architecture** to align visual and language representations into a shared latent embedding space [1, 6, 7].
*   **Encoders:** The framework uses an **EfficientNet** (specifically EfficientNet-L2) with global pooling as the image encoder, and a **BERT** (specifically BERT-Large) model with a `[CLS]` token embedding as the text encoder [8, 9]. Fully-connected layers with linear activation are added to the top of the BERT encoder to ensure its dimensions match the image tower [8].
*   **Contrastive Learning Objective:** The model is trained from scratch using a **normalized softmax contrastive loss** [7, 8, 10]. The training objective simultaneously minimizes two symmetric loss functions: an image-to-text classification loss and a text-to-image classification loss [10]. This effectively treats the noisy text as fine-grained labels, pushing the embeddings of matched image-text pairs closer together while pushing unmatched, random in-batch pairs apart [7, 10]. A learnable temperature parameter dynamically scales the logits during training [10-12]. 
*   **Data Processing:** Instead of heavy curation, the dataset construction relies on **minimal frequency-based filtering** [4, 5]. The authors remove obvious junk, such as pornographic images, oddly proportioned images, alt-texts shared by more than 10 images (which are usually generic metadata like "1920x1080" or "alt img"), texts containing rare tokens, and texts that are too short ($<3$ unigrams) or too long ($>20$ unigrams) [13, 14].

**(3) Datasets used for evaluation and comparison baselines**

*   **Evaluation Datasets:**
    *   *Image-Text Retrieval (Zero-shot and Fine-tuned):* **Flickr30K**, **MSCOCO**, and **Crisscrossed Captions (CxC)** (which includes extended semantic similarity judgments) [11, 15-17]. A multilingual version of the model was also evaluated on **Multi30k** [18].
    *   *Zero-Shot Visual Classification:* **ImageNet (ILSVRC-2012)** and its more challenging domain-shift variants (**ImageNet-R**, **ImageNet-A**, and **ImageNet-V2**) [15, 19, 20].
    *   *Downstream Visual Classification:* **ImageNet**, the 19 diverse tasks in the **Visual Task Adaptation Benchmark (VTAB)**, and fine-grained classification datasets including **Oxford Flowers-102, Oxford-IIIT Pets, Stanford Cars, and Food101** [21, 22].
    *   *Word Similarity:* **SimLex-999** [23].

*   **Comparison Baselines:**
    *   *For Image-Text Retrieval:* Evaluated against strong vision-language models and cross-attention architectures including **CLIP, ImageBERT, UNITER, GPO, ERNIE-ViL, VILLA, Oscar**, and other multi-modal embeddings like **VSE++, VSRN, DEI2T, and DET2T+I2T** [17, 24, 25]. The multilingual model was compared to **M3P and UC2** [18, 26].
    *   *For Classification Tasks:* Compared against state-of-the-art vision models including **CLIP, WSL, BiT (Big Transfer), ViT (Vision Transformer), NoisyStudent, Meta-Pseudo-Labels, and SAM** [22, 27-30].

## Results, limitations, and prior work (NLM Q2)

**(1) Key quantitative results and improvements over baselines**

*   **Image-Text Retrieval (Flickr30K & MSCOCO):** ALIGN achieved state-of-the-art (SOTA) results across all metrics. In the zero-shot setting, it outperformed the previous SOTA (CLIP) by **more than 7% in image retrieval** (e.g., reaching 75.7% R@1 on Flickr30K vs CLIP's 68.7%) [1, 2]. With fine-tuning, ALIGN significantly outperformed complex cross-attention models (like UNITER and Oscar), achieving **95.3% image-to-text R@1 on Flickr30K** and **77.0% on MSCOCO** [1, 2].
*   **Crisscrossed Captions (CxC):** ALIGN beat baselines by a massive margin, improving **image-to-text retrieval by +22.2% R@1** and **text-to-image by +20.1% R@1** [3]. It also improved the Semantic Image-Text Similarity (SITS) metric by 5.7% [3].
*   **Zero-Shot Visual Classification (ImageNet):** By feeding class names into the text encoder, ALIGN achieved **76.4% top-1 accuracy on ImageNet** without seeing any training samples [4, 5]. It also demonstrated robust domain-shift transfer, scoring **92.2% on ImageNet-R**, beating CLIP's 88.9% [5].
*   **Downstream Visual Classification:** With frozen visual features, ALIGN achieved a **SOTA 85.5% top-1 accuracy on ImageNet** (edging out CLIP's 85.4%). When fully fine-tuned, it reached **88.64%**, outperforming major models like BiT and ViT [6, 7]. It also outperformed BiT-L on the Visual Task Adaptation Benchmark (VTAB) with an average accuracy of **79.99%** [8].
*   **Multilingual Retrieval:** A multilingual version of the model (ALIGNmling) evaluated on Multi30k vastly outperformed the M3P baseline on all zero-shot languages, showing a massive **+57.8 absolute mean Recall (mR) improvement on French** [9, 10].

**(2) Limitations, failure modes, or negative results noted by the authors**

*   **Poor Intra-Modal Performance:** While ALIGN dominates inter-modal tasks (image-to-text), the authors note it is **not as impressive on intra-modal tasks** (text-to-text and image-to-image retrieval). Its performance on Semantic Textual Similarity (STS) and Semantic Image Similarity (SIS) was actually slightly worse than older baselines like VSE++ and DEI2T [3, 11]. The authors attribute this to the training objective solely focusing on cross-modal matching [11].
*   **Word Embeddings Struggle with Adjectives/Abstract Concepts:** When evaluated on the SimLex-999 word similarity benchmark, ALIGN's text embeddings performed **slightly worse overall than standard GloVe embeddings** [12, 13]. Specifically, the visually-grounded text embeddings performed significantly worse on adjectives and less concrete categories [13].
*   **Strict Reliance on Massive Scale:** The authors demonstrate that scaling up the dataset size is an absolute requirement to make up for the noise. When restricted to a smaller 3-million image dataset (CC-3M), ALIGN's noisy data performed **much worse** than cleaned Conceptual Captions data [14, 15]. Furthermore, when trained on small datasets, large architectures (like EfficientNet-B7) actually overfit and performed worse than smaller architectures (EfficientNet-B3) [16].
*   **Social and Fairness Risks:** The authors explicitly warn that relying on completely uncurated, unfiltered web alt-texts risks **reinforcing harmful stereotypes and demographic skews** present on the internet [17, 18]. 

**(3) Top 5–7 most heavily cited prior works named in the related work or introduction**

1.  **CLIP (Radford et al., 2021):** Cited extensively as the most closely related work (learning visual representations from natural language supervision via contrastive learning) and the primary state-of-the-art baseline ALIGN compares against [1, 5, 6, 11, 19].
2.  **Conceptual Captions (Sharma et al., 2018):** Cited as the foundation for ALIGN's data collection methodology, though ALIGN intentionally skips this paper's complex filtering steps [20-22].
3.  **ImageNet (Deng et al., 2009):** Repeatedly cited as the standard paradigm for supervised visual pre-training and the primary benchmark for downstream classification [23-25].
4.  **BiT / Big Transfer (Kolesnikov et al., 2020):** Cited as a major prior work in large-scale visual representation pre-training and used as a primary comparison baseline for VTAB and downstream fine-tuning [6, 8, 23, 26-28].
5.  **Flickr30K (Plummer et al., 2015) & MSCOCO (Chen et al., 2015):** Cited together frequently as the foundational benchmarking datasets for fine-grained image-text retrieval and matching [24, 29, 30].
6.  **ViT / Vision Transformer (Dosovitskiy et al., 2021):** Cited as a leading method for high-quality visual representations and compared against in ImageNet fine-tuning baselines [6, 26, 31].

## Papers That Mention This Paper (Reverse Citation Map)

*(no cross-links to other read-papers notes detected)*

| Mentioning Paper | Mention Context | Summary of Original Wording |
| --- | --- | --- |

---
## Relevance to Proxy Label Learning

This work informs supervised learning when training targets are **proxy or surrogate labels** (e.g., attribution-derived continuous scores rather than direct measurements of the deployment objective). Compare the paper's assumptions about label noise structure (systematic vs. random; instance-dependent vs. class-conditional) to Shapley-style credit assignments used as training signals.

## Method Tracker Update

- Add or increment counts for primary method and baselines named in this paper (see `method-tracker.md`).

