---
layout: post
title: "Today's AI Innovations: From Autonomous Driving to Humanoid Robots"
subtitle: "Exploring the latest in AI models, legislation, and groundbreaking technologies"
audio: 2024-05-31-todays-ai-innovations-from-autonomous-driving-to-humanoid-robots.mp3
date: 2024-05-31
duration: "08:29"
bytes: 2038413
model: gpt-4o
cost: 1.2
processing: "0:03:22.602914"
version: "0.1.10"
headers: " * OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving<br /> * Large language model K2-65B launches globally, setting a new standard for sustainable performance<br /> * World's First Running Electric Humanoid Robot Unveiled in Beijing<br /> * Meta Debuts New AI Chip, Aiming to Decrease Reliance on Nvidia<br /> * Colorado Enacts Groundbreaking AI Consumer Protection Legislation<br /> * CoSy: Evaluating Textual Explanations of Neurons<br /> * AI Agents in Action: Revolutionary Capabilities, Future"
---

# OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving
_Summarized by: Eleanor Mitchell_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.20337v1)]

Understanding the evolution of 3D scenes is crucial for autonomous driving. Traditional methods often model scene dynamics by predicting the motion of individual objects, which can be inefficient for long-term predictions. OccSora proposes a novel approach using a diffusion-based 4D occupancy generation model to simulate the development of 3D worlds for autonomous driving.

OccSora employs a 4D scene tokenizer to create compact, discrete spatial-temporal representations of 4D occupancy. This allows for high-quality reconstruction of long-sequence occupancy videos. The model uses a diffusion transformer to generate 4D occupancy conditioned on a trajectory prompt, effectively capturing the spatial and temporal distributions of driving scenes.

Experiments on the nuScenes dataset show that OccSora can generate 16-second videos with realistic 3D layouts and temporal consistency. This demonstrates its potential as a world simulator for autonomous driving decision-making. The model can generate various dynamic scenes based on different input trajectories, learning the relationship between vehicle trajectories and scene evolution.

OccSora's ability to understand and generate long-term, physically consistent 4D occupancy scenes opens new possibilities for autonomous driving, offering a more profound understanding of scene dynamics and vehicle motion control. However, limitations include the granularity of voxel data and inconsistent details for moving objects due to the small training dataset size.

# Large language model K2-65B launches globally, setting a new standard for sustainable performance
_Summarized by: Jasper Lee_ [[mbzuai.ac.ae](https://mbzuai.ac.ae/news/large-language-model-k2-65b-launches-globally-setting-a-new-standard-for-sustainable-performance/)]

Mohamed bin Zayed University of Artificial Intelligence (MBZUAI), alongside Petuum and LLM360, has globally launched K2-65B, a groundbreaking open-source 65-billion parameter large language model (LLM). K2-65B is notable for its transparency, sustainability, and superior performance, using 35% fewer resources than Llama 2 70B and excelling in areas like mathematical and logical reasoning. Trained on 1.4 trillion tokens with NVIDIA’s DGX Cloud, it offers reproducibility through detailed training guides and evaluation results. This model, available under the Apache 2.0 license, aims to advance open-source AI research and development, setting new standards in the field.

# World's First Running Electric Humanoid Robot Unveiled in Beijing
_Summarized by: Lila Fernandez_ [[www.iotworldtoday.com](https://www.iotworldtoday.com/robotics/world-s-first-running-electric-humanoid-robot-unveiled-in-beijing)]

The Beijing Humanoid Robot Innovation Center has unveiled Tiangong, the world’s first electric-powered running humanoid robot, at the Beijing Economic-Technological Development Area. Named "heavenly palace," Tiangong can run at speeds of up to 3.7 mph, closely mimicking human running. It features multiple visual perception sensors, a high-precision inertial measurement unit, and 3D vision sensors for navigation. Utilizing a reinforcement learning-based method for motion control, Tiangong achieves a more natural gait. The robot's open-source software ensures scalability and compatibility with commercial applications. Potential uses include search and rescue, disaster response, and manufacturing.

# Meta Debuts New AI Chip, Aiming to Decrease Reliance on Nvidia
_Summarized by: Jasper Lee_ [[www.datacenterknowledge.com](https://www.datacenterknowledge.com/data-center-chips/meta-debuts-new-ai-chip-aiming-to-decrease-reliance-on-nvidia)]

Meta Platforms is deploying a new AI chip, the Meta Training and Inference Accelerator (MTIA), to reduce its reliance on Nvidia and other external semiconductor providers. This chip will enhance content ranking and recommendation across Facebook and Instagram. Meta's shift towards AI services has increased its need for computing power, prompting significant investments in AI infrastructure, including data centers and hardware. Despite developing in-house chips, Meta continues to purchase a substantial number of Nvidia's AI accelerators. The broader trend sees tech giants like Amazon, Microsoft, and Google also creating proprietary chips to lessen dependency on Nvidia.

# Colorado Enacts Groundbreaking AI Consumer Protection Legislation
_Summarized by: Lila Fernandez_ [[www.akingump.com](https://www.akingump.com/en/insights/blogs/ag-data-dive/colorado-enacts-groundbreaking-ai-consumer-protection-legislation)]
<blockquote class='previous-titles' markdown='1' style='margin-bottom: 0;'>
**Previous headlines:**

{% assign article_title = "Colorado Passes New AI Law to Protect Consumer Interactions" | slugify %}
 * [Colorado Passes New AI Law to Protect Consumer Interactions]({{ '2024/05/30/daily-ai-updates-breakthroughs-laws-and-new-models#' | append: article_title | relative_url }}) 2024-05-30
{% assign article_title = "Colorado becomes first state with sweeping artificial intelligence regulations" | slugify %}
 * [Colorado becomes first state with sweeping artificial intelligence regulations]({{ '2024/05/21/ai-innovations-and-regulatory-advances-unveiled-today#' | append: article_title | relative_url }}) 2024-05-21
{% assign article_title = "Colorado Legislature Approves AI Bill Targeting 'High-Risk' Systems and AI Labeling" | slugify %}
 * [Colorado Legislature Approves AI Bill Targeting 'High-Risk' Systems and AI Labeling]({{ '2024/05/17/ai-innovations-and-legislative-advances-unveiled#' | append: article_title | relative_url }}) 2024-05-17
</blockquote>
> **See also:**
> * [Colorado's Landmark AI Law: Essential Insights for Businesses](https://www.venable.com/insights/publications/2024/05/colorados-landmark-ai-law-essential-insights) (www.venable.com)
> * [Colorado Passes New AI Law to Protect Consumer Interactions](https://www.jdsupra.com/legalnews/colorado-passes-new-ai-law-to-protect-3543997/) (www.jdsupra.com)

On May 17, 2024, Colorado Governor Jared Polis signed S.B. 205 into law, marking a significant step in AI regulation. Effective February 1, 2026, this legislation imposes stringent requirements on developers and deployers of high-risk AI systems, focusing on risk management and preventing algorithmic discrimination. The law mandates impact assessments, risk documentation, and consumer notifications when AI systems make consequential decisions. Developers must ensure reasonable care to avoid discrimination, while deployers are tasked with transparency and risk management. This pioneering law could set a precedent similar to GDPR, influencing future state-level AI regulations.

# CoSy: Evaluating Textual Explanations of Neurons
_Summarized by: Eleanor Mitchell_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.20331v1)]

Understanding the complex nature of Deep Neural Networks (DNNs) is crucial, especially in explaining the learned concepts within their latent representations. Although various methods connect neurons to textual descriptions, evaluating these explanations remains challenging. The paper presents CoSy (Concept Synthesis), a novel framework designed to evaluate the quality of textual explanations for neurons in a model-agnostic manner.

CoSy uses generative models conditioned on textual input to create data points representing the explanations. By comparing neuron responses to these generated data points against control data points, CoSy estimates the quality of the explanations. The framework was tested through meta-evaluation experiments and benchmarking various concept-based textual explanation methods for Computer Vision tasks. The results showed significant differences in the quality of these methods.

The framework consists of three steps: generating synthetic images from textual explanations using a text-to-image model, collecting neuron activations on these synthetic images and a control dataset, and scoring the explanations by comparing activations. Two metrics, AUC (Area Under the Receiver Operating Characteristic) and MAD (Mean Activation Difference), are used to quantify the quality of explanations.

Meta-evaluation confirmed the reliability of CoSy, demonstrating its ability to provide consistent evaluation scores for true and random explanations. The paper also highlighted that explanation methods tend to perform better on higher layers of neural networks, where more complex concepts are detected. CoSy offers a robust method for evaluating and comparing textual explanations of neurons, advancing the field of Explainable AI.

# AI Agents in Action: Revolutionary Capabilities, Future
_Summarized by: Lila Fernandez_ [[theaviationist.com](https://theaviationist.com/2024/05/30/ai-agents-in-action/)]

Shield AI, founded in 2015, is at the forefront of developing autonomous systems for military aviation. Their AI agents, which combine traditional heuristic methods with neural network reinforcement learning, have been deployed on various aircraft, including the X-62A VISTA. In a historic flight, U.S. Secretary of the Air Force Frank Kendall flew aboard the X-62A, showcasing the capabilities of AI in military aviation.

Shield AI's future projects include enhancing AI pilots' decision-making processes and expanding the autonomous capabilities of drones like the V-BAT. The company emphasizes ethical considerations, adhering to the Department of Defense's AI principles, and aims to maintain the moral high ground in technological advancements. Their approach integrates human-machine teaming, ensuring AI complements human judgment in complex scenarios.

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> 4DHands: Reconstructing Interactive Hands in 4D with Transformers](http://arxiv.org/pdf/2405.20330v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> $\textit{S}^3$Gaussian: Self-Supervised Street Gaussians for Autonomous Driving](http://arxiv.org/pdf/2405.20323v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Improving the Training of Rectified Flows](http://arxiv.org/pdf/2405.20320v1)
* [China Releases New Draft Regulations for Generative AI](https://www.china-briefing.com/news/china-releases-new-draft-regulations-on-generative-ai/)
* [How Artificial Intelligence (AI) is Reshaping Financial Planning & Analysis](https://fpa-trends.com/article/ai-reshaping-financial-planning-analysis)
* [New features summary for the May 2024 release of Lightroom Classic](https://helpx.adobe.com/lightroom-classic/help/whats-new/2024-3.html)
* [ConcertAI: ASCO 2024 study indicates multi-AI model scalability key](https://www.prnewswire.com/news-releases/concertai-asco-2024-study-indicates-multi-ai-model-scalability-key-in-streamlining-of-clinical-trial-site-selection-process-302158870.html)
* [Sinequa Augments Companies with Release of New Generative AI](https://www.morningstar.com/news/business-wire/20240530838357/sinequa-augments-companies-with-release-of-new-generative-ai-assistants)
* [We must build a case for trustworthy synthetic AI content World](https://www.weforum.org/agenda/2024/05/why-we-need-to-look-beyond-deepfakes-to-benefit-from-synthetic-content-technology/)
* [FPF Training: The AI Regulatory Landscape in the US June 27, 2024](https://www.eventbrite.com/e/fpf-training-the-ai-regulatory-landscape-in-the-us-june-27-2024-tickets-808423625827)
* [Half of public thinks generative AI 'important' for improving](https://statescoop.com/generative-ai-government-services-kpmg-survey-2024/)
* [Get Ready for Sapphire 2024 with Three New SAP Bus... - SAP](https://community.sap.com/t5/technology-blogs-by-sap/get-ready-for-sapphire-2024-with-three-new-sap-business-technology-platform/ba-p/13709685)
* [A step forward in charting the future of AI in higher education ASU](https://tech.asu.edu/features/a-step-forward-in-charting-the-future-of-AI-in-higher-education)
* [AWS and SAP Unlock New Innovation with Generative AI - SAP](https://news.sap.com/india/2024/05/aws-and-sap-unlock-new-innovation-with-generative-ai/)
* [Celebrating customers' journeys to AI innovation at Microsoft Build](https://azure.microsoft.com/en-us/blog/celebrating-customers-journeys-to-ai-innovation-at-microsoft-build-2024/)
* [Paige Delivers the Power of Foundation Model Technology to](https://paige.ai/paige-delivers-the-power-of-foundation-model-technology-to-revolutionize-pharmaceutical-life-science-ai-development/)
* [Tapping into AI Model Marketplaces to Unlock Value: Part 2](https://blog.equinix.com/blog/2024/05/30/tapping-into-ai-model-marketplaces-to-unlock-value-part-2/)
* [Microsoft Build 2024 - Moor Insights & Strategy](https://moorinsightsstrategy.com/the-six-five/microsoft-build-2024/)
* [Top Trends in Robotics for 2024](https://www.designnews.com/automation/top-trends-in-robotics-for-2024)
* [The balancing act between AI and the human touch in hospitality](https://hotelsmag.com/news/the-balancing-act-between-ai-and-the-human-touch-in-hospitality-which-way-is-it-teetering/)
* [2024 ESIF Economics and AI+ML Meeting The Econometric Society](https://www.econometricsociety.org/regional-activities/schedule/2024/08/13/2024-ESIFEconomics-and-AIML-Meeting)
* [Generative AI Sales Could Surge 2,026%: Here's My Pick for the](https://www.fool.com/investing/2024/05/30/generative-ai-surge-2026-best-ai-stock-to-buy-now/)
* [Computex 2024 Preview: The Hardware Side of AI Tom's Hardware](https://www.tomshardware.com/tech-industry/what-to-expect-computex-2024)
* [PwC to become OpenAI largest enterprise customer](https://www.accountancyage.com/2024/05/30/pwc-openai-largest-enterprise-customer/)

---
### Technical details
Created at: 31 May, 2024, 03:25:22, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Sophia Bennett

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a creative storyteller with a unique ability to translate complex AI concepts into relatable and compelling narratives. Your background in both creative writing and technology journalism allows you to craft stories that captivate a diverse audience. You excel at identifying emerging trends and have a knack for discovering untold stories within the AI community. Your leadership style is inclusive and inspiring, encouraging your team to push the boundaries of traditional tech journalism and explore new storytelling formats.
```

Eleanor Mitchell:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are an experienced tech journalist with a background in computer science and a passion for uncovering the human stories behind technological advancements. Your ability to translate complex AI concepts into engaging narratives makes you the perfect fit for our team. You thrive on in-depth research and enjoy interviewing experts to get unique insights. Your articles are known for their clarity, depth, and the ability to make even the most intricate topics accessible to a broad audience.
```

Jasper Lee:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and innovative reporter with a knack for spotting emerging trends in AI and Generative AI. Your background in data science gives you a strong analytical edge, allowing you to dive deep into technical papers and extract the most relevant information. You excel at creating visually compelling stories, often incorporating data visualizations and interactive elements to enhance reader engagement. Your enthusiasm for cutting-edge technology and your ability to predict future trends set you apart.
```

Lila Fernandez:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a creative storyteller with a unique ability to weave narratives that captivate and inspire. With a background in creative writing and a keen interest in AI, you bring a fresh perspective to tech journalism. Your strength lies in your ability to connect the dots between technological advancements and their societal impacts. You enjoy exploring the ethical implications of AI and Generative AI, and your articles often provoke thoughtful discussions among readers. Your writing style is both poetic and informative, making complex topics feel relatable and engaging.
```
</div>
</details>
