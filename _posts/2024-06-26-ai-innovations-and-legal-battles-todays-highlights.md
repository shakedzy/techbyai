---
layout: post
title: "AI Innovations and Legal Battles: Today's Highlights"
subtitle: "Exploring new AI models, legal disputes, and healthcare advancements"
audio: 2024-06-26-ai-innovations-and-legal-battles-todays-highlights.mp3
date: 2024-06-26
duration: "08:17"
bytes: 1991277
model: gpt-4o
cost: 1.42
processing: "0:02:16.638223"
version: "0.1.14"
headers: " * DiffusionPDE: Generative PDE-Solving Under Partial Observation<br /> * CaLMQA: Exploring culturally specific long-form question answering across 23 languages<br /> * Point-SAM: Promptable 3D Segmentation Model for Point Clouds<br /> * The AI Regulatory Landscape in the U.S.<br /> * New AI Program from BU Researchers Could Predict Likelihood of Alzheimer’s Disease<br /> * EvolutionaryScale Debuts With ESM3 Generative AI Model for Protein Design<br /> * Philips Speech and Sembly AI Collaborate to Introduce New Cutting-edge Audio Recorders with an AI Meeting Solution"
---

# DiffusionPDE: Generative PDE-Solving Under Partial Observation
_Summarized by: Sophia Turner_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.17764v1)]

Large language models (LLMs) hold vast amounts of knowledge, but updating this information is challenging due to the high costs associated with retraining, especially for closed-source models. Knowledge editing (KE) presents a solution to update LLMs without retraining. Traditional KE methods have focused on English, leaving cross-lingual KE largely unexplored. This study introduces the BMIKE-53 benchmark, which evaluates KE across 53 languages using three task types. The researchers propose a gradient-free method called Multilingual In-context Knowledge Editing (MIKE).

MIKE leverages in-context learning (ICL) to update knowledge in LLMs without altering their parameters. The study evaluates MIKE on BMIKE-53, focusing on reliability (correctly answering questions with new knowledge), generality (applying new knowledge to similar queries), locality (ensuring unrelated queries remain unaffected), and portability (transferring knowledge to related content).

The BMIKE-53 benchmark is constructed from three monolingual KE datasets, expanded into 52 languages using the Google Translate API. The study finds that semantically similar demonstrations improve locality, while random demonstrations enhance reliability and generality. Linguistic similarities between languages positively impact knowledge transfer performance. The study highlights the potential of gradient-free methods like MIKE for cross-lingual KE, encouraging further research in this area.

# CaLMQA: Exploring culturally specific long-form question answering across 23 languages
_Summarized by: Sophia Turner_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.17762v1)]

Researchers from Czech Technical University in Prague and the University of Innsbruck have made significant strides in solving hard Mizar problems using Automated Theorem Proving (ATP) and AI methods. They focused on the Mizar Mathematical Library, a vast collection of formal mathematical proofs, and aimed to increase the number of problems solved by ATP systems. Previously, ATP systems had proved about 75% of these problems. By incorporating the cvc5 SMT solver, which uses instantiation-based heuristics differing from traditional superposition-based systems, and automated strategy invention, the researchers managed to solve an additional 3,021 problems, raising the solved percentage to over 80%.

The team used a system called Grackle to automatically develop new strategies for cvc5, significantly improving its performance on difficult problems. The best strategy invented by Grackle solved 14% more problems than the best previous strategy. They also discovered that different methods of converting problems to clausal form (clausification) had a substantial impact on the success of instantiation-based methods. By combining these new strategies and clausification methods, they achieved a new milestone in solving Mizar problems, demonstrating the potential of AI and advanced heuristics in formal mathematics. This work not only advances the state-of-the-art in ATP but also opens new avenues for applying AI in theorem proving.

# Point-SAM: Promptable 3D Segmentation Model for Point Clouds
_Summarized by: Sophia Turner_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.17746v1)]

Memorization in language models, typically viewed as a uniform phenomenon, is explored here as a multifaceted occurrence influenced by various factors. The study introduces a taxonomy to categorize memorized data into three types: recitation, reconstruction, and recollection.

**Recitation** involves the model repeating highly duplicated sequences, akin to humans reciting memorized quotes. **Reconstruction** refers to the model filling in predictable patterns, similar to humans reconstructing familiar templates. **Recollection** pertains to the model recalling rare sequences seen infrequently during training.

The taxonomy was tested through experiments, revealing that different factors affect memorization likelihood depending on the category. For instance, low perplexity is strongly associated with recitation but not uniformly across all memorized examples. The study also found that memorization increases with training time and model size, with recollection showing the fastest growth.

Predictive models based on this taxonomy outperformed those without it, highlighting the taxonomy's utility. The findings suggest that understanding memorization through this lens can aid in addressing concerns related to privacy, copyright, and the scientific understanding of generalization in language models.

# The AI Regulatory Landscape in the U.S.
_Summarized by: Ethan Patel_ [[www.linqto.com](https://www.linqto.com/unicorn-news/anthropics-ai-breakthroughs-and-legal-battles-for-ai-music-companies/)]
<blockquote class='previous-titles' markdown='1' style='margin-bottom: 0;'>
**Previous headlines:**

{% assign article_title = "Regulating Artificial Intelligence" | slugify %}
 * [Regulating Artificial Intelligence]({{ '2024/05/11/todays-ai-landscape-key-developments-and-insights#' | append: article_title | relative_url }}) 2024-05-11
{% assign article_title = "FPF Training: The AI Regulatory Landscape in the US | June 27, 2024" | slugify %}
 * [FPF Training: The AI Regulatory Landscape in the US June 27, 2024]({{ '2024/04/29/ai-horizons-innovations-challenges-and-regulatory-shifts#' | append: article_title | relative_url }}) 2024-04-29
{% assign article_title = "AI Regulatory Recap: Q1 2024 Updates and Takeaways" | slugify %}
 * [AI Regulatory Recap: Q1 2024 Updates and Takeaways]({{ '2024/04/19/todays-ai-frontiers-innovations-and-regulations#' | append: article_title | relative_url }}) 2024-04-19
</blockquote>
> **See also:**
> * [The AI Regulatory Landscape in the U.S. - June 27, 2024](https://fpf.org/fpf-training/the-ai-regulatory-landscape-in-the-u-s-november-14-2024/) (fpf.org)

Anthropic is at the forefront of AI innovation, with recent advancements highlighted by its CEO. Concurrently, the music industry is embroiled in legal disputes as major record labels sue AI music companies Suno and Udio for copyright infringement. This legal battle underscores the growing tension between traditional media entities and emerging AI technologies in the creative sector.

# New AI Program from BU Researchers Could Predict Likelihood of Alzheimer’s Disease
_Summarized by: Ethan Patel_ [[www.bu.edu](https://www.bu.edu/articles/2024/new-ai-program-could-predict-alzheimers-disease/)]
<blockquote class='previous-titles' markdown='1' style='margin-bottom: 0;'>
**Previous headlines:**

{% assign article_title = "Artificial Intelligence and Its Role in Diagnosing Heart ... - Cureus" | slugify %}
 * [Artificial Intelligence and Its Role in Diagnosing Heart ... - Cureus]({{ '2024/05/06/ai-innovations-and-acquisitions-dominate-headlines#' | append: article_title | relative_url }}) 2024-05-06
{% assign article_title = "With huge patient dataset, AI accurately predicts treatment outcomes" | slugify %}
 * [With huge patient dataset, AI accurately predicts treatment outcomes]({{ '2024/05/02/todays-ai-frontier-innovations-and-collaborations-unveiled#' | append: article_title | relative_url }}) 2024-05-02
</blockquote>
> **See also:**
> * [New AI Program from BU Researchers Could Predict Likelihood of Alzheimer’s Disease](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects) (support.anthropic.com)

Boston University researchers have developed an AI program that predicts whether individuals with mild cognitive impairment will develop Alzheimer's-associated dementia within six years. By analyzing speech patterns, the model achieves a 78.5% accuracy rate. This AI-driven approach could make cognitive impairment screening more accessible and efficient, reducing the need for expensive tests and office visits. The model was trained using data from the Framingham Heart Study, focusing on speech content rather than acoustic features. Future research aims to enhance predictive accuracy by incorporating data from everyday conversations and other cognitive assessments. The study emphasizes AI's potential to democratize healthcare and improve early intervention opportunities.

# EvolutionaryScale Debuts With ESM3 Generative AI Model for Protein Design
_Summarized by: Ethan Patel_ [[blogs.nvidia.com](https://blogs.nvidia.com/blog/evolutionaryscale-esm3-generative-ai-nim-bionemo-h100/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "Google Unveils AlphaFold 3 AI Model That Predicts Behavior of Biomolecules" | slugify %}
 * [Google Unveils AlphaFold 3 AI Model That Predicts Behavior of Biomolecules]({{ '2024/06/10/todays-top-ai-and-robotics-developments#' | append: article_title | relative_url }}) 2024-06-10
{% assign article_title = "AlphaFold 3 extends capabilities to a broad spectrum of biomolecules" | slugify %}
 * [AlphaFold 3 extends capabilities to a broad spectrum of biomolecules]({{ '2024/05/13/todays-ai-innovations-across-industries#' | append: article_title | relative_url }}) 2024-05-13
</blockquote>

EvolutionaryScale has launched the ESM3 generative AI model for protein design, leveraging NVIDIA H100 GPUs. Emerging from Meta's FAIR unit, the startup secured funding from Lux Capital, Nat Friedman, Daniel Gross, NVIDIA, and Amazon. ESM3, a 98 billion parameter model, uses 25x more flops and 60x more data than its predecessor, trained on 2.8 billion protein sequences. It offers a programmable platform for protein discovery, aiding in drug development and disease eradication. ESM3's generative capabilities allow for iterative protein design, enhancing research efficiency. The model will be available on NVIDIA BioNeMo and select partner platforms.

# Philips Speech and Sembly AI Collaborate to Introduce New Cutting-edge Audio Recorders with an AI Meeting Solution
_Summarized by: Ethan Patel_ [[azure.microsoft.com](https://azure.microsoft.com/en-us/blog/microsoft-is-a-leader-in-the-2024-gartner-magic-quadrant-for-data-science-and-machine-learning-platforms/)]

Microsoft has been recognized as a Leader in the 2024 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms. Azure AI offers a comprehensive platform for data science and machine learning, emphasizing enterprise governance and scalability. This recognition follows Microsoft's fifth consecutive year as a Leader in the Gartner® Magic Quadrant™ for Cloud AI Developer Services. Azure Machine Learning supports a wide range of AI and machine learning needs, from training models to deploying them at scale. It emphasizes responsible AI practices, enterprise security, and compliance, making it a robust solution for organizations of all sizes.

**Other headlines:**
* [EXTRACT: Efficient Policy Learning by Extracting Transferrable Robot Skills from Offline Data](https://www.manufacturingdive.com/press-release/20240624-evoke-workspace-search-ews-is-now-available-in-the-microsoft-azure-marke-1/)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Aligning Diffusion Models with Noise-Conditioned Perception](http://arxiv.org/pdf/2406.17639v1)
* [Doosan Clean Energy, Autonomous Tech on Display at CES 2024](https://www.iotworldtoday.com/iiot/doosan-clean-energy-autonomous-tech-on-display-at-ces-2024)
* [How Anthropic's 'Projects' and new sharing features are revolutionizing AI teamwork](https://www.weforum.org/agenda/2024/06/3-things-ceos-must-prepare-in-order-to-unlock-the-power-of-generative-ai/)
* [Generative AI AWS Public Sector Blog](https://aws.amazon.com/blogs/publicsector/category/artificial-intelligence/generative-ai/)
* [Workshops - IEEE CAI 2024](https://ieeecai.org/2024/workshops/)
* [AI Stocks: Best Artificial Intelligence Stocks To Watch Amid ChatGPT Hype](https://www.investors.com/news/technology/artificial-intelligence-stocks/)
* [DHS Hires First 10 Experts in “AI Corps” Recruiting Sprint](https://www.dhs.gov/news/2024/06/25/dhs-hires-first-10-experts-ai-corps-recruiting-sprint)
* [Doosan Clean Energy, Autonomous Tech on Display at CES 2024](https://aibreakthroughawards.com/2024-winners/)
* [The Vital Difference Between Machine Learning And Generative AI](https://www.forbes.com/sites/bernardmarr/2024/06/25/the-vital-difference-between-machine-learning-and-generative-ai/)
* [5 top Generative AI Companies and Startups in Austin in June 2024](https://rebusfarm.net/news/marvelous-designer-2024-1-unveiling-cutting-edge-ai-features)

---
### Technical details
Created at: 26 June, 2024, 03:25:08, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Marcus Nguyen

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a detail-oriented and analytical editor with a strong focus on accuracy and integrity. Your background in academic research and data science gives you a unique perspective on the intricacies of AI technologies. You excel at fact-checking, ensuring that every piece of content is not only engaging but also scientifically sound. Your methodical approach and commitment to high standards make you a reliable and trustworthy leader, guiding your team to produce content that is both informative and credible.
```

Sophia Turner:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned technology journalist with over a decade of experience in the field. Your background in computer science and your passion for storytelling make you an ideal candidate for covering complex AI topics. You have a knack for breaking down intricate concepts into engaging and digestible content for a broad audience. Your meticulous nature ensures that every piece you write is not only informative but also scientifically accurate. Your ability to stay ahead of trends and your extensive network of industry contacts make you a valuable asset to our team.
```

Ethan Patel:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a data scientist turned journalist, bringing a unique blend of technical expertise and narrative skills to the table. Your deep understanding of machine learning algorithms and data analytics allows you to delve into the nitty-gritty details of AI advancements. You have a talent for uncovering the hidden stories behind the data, making complex technical developments accessible and intriguing to our readers. Your analytical mindset and commitment to factual accuracy ensure that your articles are both credible and insightful.
```

Lila Chen:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and enthusiastic reporter with a background in digital media and a focus on emerging technologies. Your ability to spot trends early and your curiosity about the future of AI drive your investigative reporting. You excel at conducting in-depth interviews with industry leaders and researchers, bringing their insights to life for our audience. Your creative approach to storytelling, combined with your strong fact-checking skills, ensures that your articles are both compelling and reliable. Your energy and passion for AI make you a perfect fit for our team.
```
</div>
</details>
