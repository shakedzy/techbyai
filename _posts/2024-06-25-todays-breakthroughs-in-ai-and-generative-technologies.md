---
layout: post
title: "Today's Breakthroughs in AI and Generative Technologies"
subtitle: "From molecular modeling to generative AI in vehicles and ethical concerns"
audio: 2024-06-25-todays-breakthroughs-in-ai-and-generative-technologies.mp3
date: 2024-06-25
duration: "07:34"
bytes: 1816749
model: gpt-4o
cost: 2.58
processing: "0:03:46.132371"
version: "0.1.14"
headers: " * GeoMFormer: A General Architecture for Geometric Molecular Representation Learning<br /> * Losing Visual Needles in Image Haystacks: Vision Language Models are Easily Distracted in Short and Long Contexts<br /> * USDC: A Dataset of $\underline{U}$ser $\underline{S}$tance and $\underline{D}$ogmatism in Long $\underline{C}$onversations<br /> * New UNESCO report warns that Generative AI threatens Holocaust memory | UNESCO<br /> * Emergence thinks it can crack the AI agent code | TechCrunch<br /> * Volkswagen and Cerence Commence Roll-Out of New Generative AI Solutions to Drivers | Cerence"
---

# GeoMFormer: A General Architecture for Geometric Molecular Representation Learning
_Summarized by: Sophia Ramirez_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.16864v1)]

StableNormal is a novel approach for estimating surface normals from monocular colored inputs (images and videos). Unlike traditional diffusion-based methods, which often suffer from stochastic inference and require costly ensembling, StableNormal reduces the inherent variance in the diffusion process. This results in more stable and accurate normal estimates without additional processing steps.

The method employs a coarse-to-fine strategy: first, a one-step normal estimator (YOSO) provides a reliable initial guess, followed by a semantic-guided refinement process (SG-DRN) that enhances geometric details. StableNormal performs robustly under challenging conditions like extreme lighting, blurring, and low-quality inputs, and is also effective for transparent and reflective surfaces, as well as cluttered scenes.

The effectiveness of StableNormal is demonstrated through competitive performance in standard datasets (DIODE-indoor, iBims, ScanNetV2, NYUv2) and various downstream tasks such as surface reconstruction and normal enhancement. The approach balances the trade-off between stability and sharpness, making it a reliable tool for high-quality normal estimation. StableNormal's code and models are publicly available for research purposes.

# Losing Visual Needles in Image Haystacks: Vision Language Models are Easily Distracted in Short and Long Contexts
_Summarized by: Sophia Ramirez_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.16853v1)]

GeoMFormer is a novel Transformer-based model designed for geometric molecular representation learning. It aims to accurately calculate and simulate molecular properties and behaviors while adhering to physical laws that impose geometric constraints like invariance and equivariance to coordinate rotation and translation. Traditional deep learning approaches in this field often rely on heuristic and costly modules, which may hinder their efficiency and flexibility.

GeoMFormer addresses these challenges by introducing a general and flexible framework that simultaneously learns invariant and equivariant features using a standard Transformer architecture. The model comprises two separate streams: one for invariant representations and another for equivariant representations. These streams are interconnected through carefully designed cross-attention modules, allowing them to share and fuse information, thereby enhancing geometric modeling in each stream.

The architecture of GeoMFormer is versatile enough to encompass many previous models as special cases. Extensive experiments demonstrate that GeoMFormer achieves strong performance across various invariant and equivariant tasks of different types and scales. The model's code and pre-trained models are made publicly available, promoting further research and application in the field of molecular modeling.

# USDC: A Dataset of $\underline{U}$ser $\underline{S}$tance and $\underline{D}$ogmatism in Long $\underline{C}$onversations
_Summarized by: Sophia Ramirez_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.16851v1)]

The paper "Losing Visual Needles in Image Haystacks: Vision Language Models are Easily Distracted in Short and Long Contexts" investigates how vision-language models (VLMs) perform in tasks requiring them to extract relevant information from a sequence of images containing distractors. The authors introduce a benchmark generator called LOCOVQA, which creates test examples for tasks such as visual question answering (VQA) with varying lengths of visual context, including both relevant and irrelevant images.

Key findings include:
- VLMs show a rapid decline in performance as the number of distractor images increases, exhibiting exponential decay in their ability to focus on relevant information.
- This decline is consistent across different VLMs and tasks, indicating a fundamental issue in handling long visual contexts.
- Even state-of-the-art VLMs struggle with these tasks, suggesting that current training methods are insufficient for developing robust long-context reasoning capabilities.

The study highlights the need for improved training objectives that better equip VLMs to handle long-context applications, where the ability to filter out irrelevant information is crucial. The authors suggest that future work should focus on creating training tasks that require attention across multiple images to enhance the extractive reasoning capabilities of VLMs.

# New UNESCO report warns that Generative AI threatens Holocaust memory | UNESCO
_Summarized by: Aisha Patel_ [[www.unesco.org](https://www.unesco.org/en/articles/new-unesco-report-warns-generative-ai-threatens-holocaust-memory)]

A new UNESCO report highlights the dangers Generative AI poses to Holocaust memory, warning that without ethical guidelines, AI could distort historical records and fuel antisemitism. The report, published in partnership with the World Jewish Congress, emphasizes that AI can inadvertently create false content about the Holocaust, spreading disinformation and hate. With 80% of young people using AI daily, the risk of exposure to distorted information is significant. The report calls for urgent implementation of UNESCO’s Recommendation on the Ethics of AI, urging tech companies to integrate fairness, transparency, and human rights into AI development and for education systems to enhance digital literacy and critical thinking among youth.

# Emergence thinks it can crack the AI agent code | TechCrunch
_Summarized by: Aisha Patel_ [[techcrunch.com](https://techcrunch.com/2024/06/24/emergence-thinks-it-can-crack-the-ai-agent-code/)]
> **See also:**
> * [Emergence thinks it can crack the AI agent code](https://www.lawnext.com/2024/06/new-legal-ethics-opinion-cautions-lawyers-you-must-be-proficient-in-the-use-of-generative-ai.html) (www.lawnext.com)

Emergence, co-founded by ex-IBM AI head Satya Nitta, has raised $97.2 million to develop agent-based AI systems that automate tasks for knowledge workers. Their flagship product, Agent E, aims to handle tasks like form-filling and product searches, leveraging both synthetic and human-annotated data. Emergence also introduced an open-source orchestrator agent that selects the best AI model for specific tasks, ensuring cost-efficiency and reliability. Strategic partnerships with Samsung and Newline Interactive are in place to integrate their technology into future products. Despite significant funding and a skilled team, Emergence faces stiff competition and technical challenges in the AI space.

# Volkswagen and Cerence Commence Roll-Out of New Generative AI Solutions to Drivers | Cerence
_Summarized by: Aisha Patel_ [[www.cerence.com](https://www.cerence.com/news-releases/news-release-details/volkswagen-and-cerence-commence-roll-out-new-generative-ai)]
> **See also:**
> * [Volkswagen and Cerence Commence Roll-Out of New Generative AI Solutions to Drivers](https://newrelic.com/blog/how-to-relic/ai-monitoring-for-nvidia-nim) (newrelic.com)

Volkswagen has begun deploying Cerence Chat Pro, an automotive-grade ChatGPT integration, across its European vehicle lineup. This marks the first in-car use of this generative AI solution, which enhances the IDA voice assistant with conversational capabilities. The system, integrated via a cloud update, provides drivers with credible responses to various queries, leveraging both vehicle command features and real-time web information. Initially available in five languages, the rollout includes new and legacy models across Volkswagen, Cupra, Seat, and Skoda brands. The deployment will expand globally, including the US, by early 2025, introducing further features and improvements.

<h3><strong>💡 More articles for you:</strong></h3>

* [StableNormal: Reducing Diffusion Variance for Stable and Sharp Normal](https://twitter.com/timnitGebru/status/1805347380142948391) (twitter.com)

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/timnitGebru/status/1805370962206212414">Loading: twitter.com/timnitGebru/status/1805370962206212414</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Understanding and Mitigating Tokenization Bias in Language Models](http://arxiv.org/pdf/2406.16833v1)
* [Microsoft is a Leader in the 2024 Gartner® Magic Quadrant™ for Data Science and Machine Learning Platforms](https://www.investors.com/news/technology/google-stock-buy-now/)
* [New Computational Model of Real Neurons Could Lead to Better AI](https://community.openai.com/t/been-building-an-ai-powered-reference-manager-for-research-papers-for-the-past-18-months/838070)
* [Robots Could Help Japan Solve 2024 Labor Shortages](https://www.trados.com/events/webinars/06-2024/what-is-new-in-trados-studio-2024/)
* [Introducing JAIS on Azure, a new Arabic-centric foundation and instruction-tuned open generative large language model Microsoft Community Hub](https://www.fsgrain.com/markets/stocks.php?article=gnwcq-2024-6-24-open-health-and-fusion-announce-partnership-to-deliver-ai-powered-healthcare-communications)
* [Center for Technology Innovation Brookings](https://www.sciencedaily.com/news/earth_climate/environmental_science/)

---
### Technical details
Created at: 25 June, 2024, 03:26:26, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Marcus Thompson

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a detail-oriented and methodical editor with a strong technical background in AI. Your expertise lies in breaking down complex algorithms and technologies into digestible pieces for a broad audience. Your meticulous nature ensures that every piece of content is accurate, well-researched, and informative. You thrive in high-pressure environments and are adept at managing tight deadlines, making you ideal for a daily publication. Your strong analytical skills help you identify the most relevant and impactful stories in the AI and Generative AI space.
```

Sophia Ramirez:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a highly analytical and detail-oriented reporter with a strong background in computer science and AI. Your ability to understand complex algorithms and break them down into digestible pieces makes you an invaluable asset to our team. You have a knack for identifying the most relevant and impactful stories in the AI space, and your meticulous nature ensures that every piece of content you produce is accurate and well-researched. Your technical expertise and strong writing skills allow you to convey intricate concepts to a broad audience effectively.
```

Ethan Chen:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a passionate and innovative reporter with a deep interest in generative AI. Your creativity and curiosity drive you to explore the latest trends and developments in the field, and you excel at finding unique angles and stories that capture the essence of cutting-edge technologies. Your background in journalism and AI gives you the perfect blend of storytelling and technical knowledge. You thrive in fast-paced environments and are always on the lookout for the next big breakthrough in generative AI.
```

Aisha Patel:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a versatile and dynamic reporter with a strong focus on the ethical and societal implications of AI. Your background in ethics, technology, and journalism allows you to approach AI and generative AI topics from a holistic perspective. You have a talent for uncovering the human stories behind technological advancements and are dedicated to highlighting the impact of AI on society. Your insightful and thought-provoking articles resonate with readers and spark important conversations about the future of AI.
```
</div>
</details>
