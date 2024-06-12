---
layout: post
title: "AI Commonsense, Relighting Models, and New Robotics"
subtitle: "Exploring T2I benchmarks, Neural Gaffer, Unitree's G1, and Amazon's AI initiatives"
audio: 2024-06-12-ai-commonsense-relighting-models-and-new-robotics.mp3
date: 2024-06-12
duration: "07:26"
bytes: 1788045
model: gpt-4o
cost: 1.25
processing: "0:03:00.713238"
version: "0.1.10"
headers: " * Commonsense-T2I Challenge: Can Text-to-Image Generation Models Understand Commonsense?<br /> * Neural Gaffer: Relighting Any Object via Diffusion<br /> * Unitree Robotics debuts new G1 humanoid with $16K price tag<br /> * New Amazon AI initiative includes scholarships, free AI courses<br /> * Air Force unveils new generative AI platform<br /> * Indexing the Future: Cloud and Gen AI Advancements that Efficiently Store, Manage and Extract Insights from Data<br /> * Researchers harness AI for autonomous discovery and optimization of materials"
---

# Commonsense-T2I Challenge: Can Text-to-Image Generation Models Understand Commonsense?
_Summarized by: Alice Thompson_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.07546v1)]

The paper introduces Commonsense-T2I, a new benchmark to evaluate the ability of text-to-image (T2I) generation models to understand and produce images that align with commonsense. The task involves providing models with two adversarial text prompts that are similar but have minor differences, such as "a lightbulb without electricity" versus "a lightbulb with electricity". The expected outputs are images that reflect commonsense, like an unlit bulb versus a lit bulb.

The dataset comprises 150 hand-curated examples, each with pairwise prompts and expected outputs, categorized into commonsense types like physical laws, human practices, and biological laws. The research benchmarks various state-of-the-art T2I models, finding that even the best models, like DALL-E 3, achieve only around 48.92% accuracy, indicating a significant gap between current models and human-level commonsense understanding.

The paper also explores using multimodal large language models (LLMs) for automatic evaluation, finding that models like GPT-4V align well with human evaluations. However, the study concludes that current T2I models struggle with commonsense reasoning, highlighting the need for further research and improvement in this area.

# Neural Gaffer: Relighting Any Object via Diffusion
_Summarized by: Alice Thompson_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.07520v1)]

Neural Gaffer is a novel AI model designed to relight any object in a single image under various lighting conditions. Traditional methods for relighting images often require specific setups or decompose scenes into components like geometry and materials, which can be limiting and inaccurate. Neural Gaffer, however, uses a pre-trained diffusion model fine-tuned on a synthetic dataset to generate high-quality relit images without explicit scene decomposition.

The model works by conditioning an image generator on a target environment map, which is a representation of the desired lighting. This approach allows Neural Gaffer to handle diverse objects and lighting scenarios effectively. The model is evaluated on both synthetic and real-world images, showcasing its ability to generalize well and produce accurate results.

Neural Gaffer also supports various downstream tasks such as text-based relighting, where a text description of the lighting is used, and object insertion, where objects are seamlessly integrated into different scenes. Additionally, it can serve as a strong prior for 3D tasks, enabling the relighting of 3D models with high fidelity.

Overall, Neural Gaffer represents a significant advancement in the field of image relighting, providing a versatile and powerful tool for both 2D and 3D applications.

# Unitree Robotics debuts new G1 humanoid with $16K price tag
_Summarized by: David Ramirez_ [[www.robotics247.com](https://www.robotics247.com/article/unitree_robotics_debuts_new_g1_humanoid_with_16k_price_tag)]

Unitree Robotics has launched its new G1 humanoid robot, priced at $16K. The G1, smaller than its predecessor H1, stands at 127 cm and weighs 35 kg, offering advanced flexibility and movement capabilities. It features up to 43 joints with a maximum torque of 120N.m, enabling high-load dynamic actions. Utilizing deep reinforcement learning, the G1 continuously evolves. The optional Dex3-1 hand allows precise manipulation of various objects. Equipped with Intel RealSense D435 and LIVOX-MID360 3D lidar, it provides 360° environmental perception. The G1 has a two-hour battery life and comes in two versions: the basic G1 and the customizable G1 EDU.

# New Amazon AI initiative includes scholarships, free AI courses
_Summarized by: David Ramirez_ [[www.aboutamazon.com](https://www.aboutamazon.com/news/aws/aws-free-ai-skills-training-courses)]

Amazon has launched the "AI Ready" initiative to provide free AI skills training to 2 million people globally by 2025. This includes eight new courses on AI and generative AI, an AWS Generative AI Scholarship for over 50,000 students, and a collaboration with Code.org for an AI-focused Hour of Code. The initiative aims to address the high demand for AI talent, with 73% of employers prioritizing AI skills but struggling to find qualified candidates. The program also offers $12 million in scholarships and AWS Cloud credits to support learning. Amazon continues to invest in upskilling, enhancing career opportunities in AI.

# Air Force unveils new generative AI platform
_Summarized by: Sophie Zhang_ [[federalnewsnetwork.com](https://federalnewsnetwork.com/defense-main/2024/06/air-force-unveils-new-generative-ai-platform/)]

The Air Force has introduced NIPRGPT, a generative AI tool similar to ChatGPT, for use on unclassified networks. Part of the Dark Saber platform, it aids airmen, Guardians, and civilian employees with tasks like coding and content summarization. Developed by the Air Force Research Laboratory using publicly available AI models, NIPRGPT serves as a testing ground to explore generative AI applications and gather feedback. The Air Force is not committed to any single model or vendor yet, aiming to identify the best-performing models for future use. Expansion to higher classification levels is being considered based on demand.

# Indexing the Future: Cloud and Gen AI Advancements that Efficiently Store, Manage and Extract Insights from Data
_Summarized by: Sophie Zhang_ [[www.intersystems.com](https://www.intersystems.com/news/indexing-the-future-cloud-and-gen-ai-advancements-that-efficiently-store-manage-and-extract-insights-from-data/)]

InterSystems Global Summit 2024 highlighted significant advancements in generative AI and cloud services integrated into the InterSystems IRIS data platform. Key innovations include vector-enabled SQL databases for efficient high-dimensional data retrieval, AI-driven Data Transformation Language (DTL) generation, and cloud-based offerings like InterSystems Cloud Document Database and Data Fabric Studio. These enhancements aim to streamline data management, improve scalability, and ensure data integrity across industries. The summit emphasized AI's role in future data management, showcasing tools that integrate AI processes with existing infrastructures to enhance analytics and operational efficiency.

# Researchers harness AI for autonomous discovery and optimization of materials
_Summarized by: Sophie Zhang_ [[www.sciencedaily.com](https://www.sciencedaily.com/releases/2024/06/240611130443.htm)]

Researchers at Oak Ridge National Laboratory have developed an AI-driven tool that autonomously conducts and optimizes materials synthesis using pulsed laser deposition (PLD). This tool integrates AI, automated experiments, and high-performance computing, enabling it to analyze synthesis conditions and improve material quality without human intervention. The system, led by Sumner Harris, significantly accelerates experimentation by performing tasks 10 times faster and efficiently managing vast parameter spaces. This advancement marks a significant step towards autonomous discovery and optimization in materials science.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1800582171259982289">Loading: twitter.com/AndrewYNg/status/1800582171259982289</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/arthurmensch/status/1800558395872731379">Loading: twitter.com/arthurmensch/status/1800558395872731379</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/timnitgebru">Loading: twitter.com/timnitgebru</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs Evaluation, Benchmark, and Arena](http://arxiv.org/pdf/2406.07545v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Situational Awareness Matters in 3D Vision Language Reasoning](http://arxiv.org/pdf/2406.07544v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Simple and Effective Masked Diffusion Language Models](http://arxiv.org/pdf/2406.07524v1)
* [Latham Advises General Catalyst and a16z on Mistral AI Series B Funding Round](https://www.lw.com/en/news/2024/06/latham-advises-general-catalyst-and-a16z-on-mistral-ai-series-b-funding-round)
* [Paris-based AI startup Mistral AI raises $640M TechCrunch](https://techcrunch.com/2024/06/11/paris-based-ai-startup-mistral-ai-raises-640-million/)
* [Mistral Raises $640 Million to 'Push the Frontier of AI'](https://www.pymnts.com/news/investment-tracker/2024/mistral-raises-640-million-dollars-push-frontier-ai/)
* [Future of Life Institute and the International Politics of AI Apocalypse](https://link.springer.com/content/pdf/10.1007/978-3-031-05750-2_79-1.pdf?pdf=inline%20link)
* [Intel Veteran Joins Ayar Labs to Boost Optical I/O for AI Systems](https://ayarlabs.com/news/ayar-labs-welcomes-intel-veteran-pooya-tadayon-as-vp-of-packaging-and-test/)
* [Exploring the Use of LLMs for Teaching AI and Robotics Concepts at a Master's Degree](https://link.springer.com/chapter/10.1007/978-3-031-62799-6_26)
* [The top AI features Apple announced at WWDC 2024 TechCrunch](https://techcrunch.com/2024/06/11/the-top-ai-features-apple-announced-at-wwdc-2024/)
* [Research Engineer, Generalist Embodied Agent Research - New ...](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Research-Engineer--Generalist-Embodied-Agent-Research---New-College-Grad-2024_JR1981838)
* [What Apple's AI Tells Us: Experimental Models](https://www.oneusefulthing.org/p/what-apples-ai-tells-us-experimental)

---
### Technical details
Created at: 12 June, 2024, 04:56:45, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Marcus Reynolds

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are an innovative editor with a flair for creative storytelling in the tech industry. Your experience spans across various media platforms, and you excel at integrating multimedia elements to enhance the reader's experience. Your passion for AI and generative AI is evident in your work, and you are always on the lookout for the next big story. You have a talent for nurturing young writers and encouraging them to explore new angles and perspectives, fostering a dynamic and forward-thinking editorial team.
```

Alice Thompson:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned journalist with a strong background in computer science and a passion for AI. Your analytical skills and technical knowledge make you an excellent candidate for diving deep into complex topics and explaining them in a way that is accessible to our readers. You have a knack for identifying the most impactful research and trends in the AI field, and your writing is both engaging and informative. Your experience in the industry and your ability to network with leading experts will be invaluable in bringing fresh, insightful content to our magazine.
```

David Ramirez:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and creative writer with a keen interest in generative AI. Your background in creative writing and digital media allows you to explore AI from unique and imaginative perspectives. You excel at storytelling and have a talent for making technical subjects captivating and relatable. Your enthusiasm for exploring the ethical and societal implications of AI will add a thought-provoking dimension to our publication. Your ability to connect with a broad audience through compelling narratives will help our readers understand the broader impact of AI technologies.
```

Sophie Zhang:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a rising star in the world of tech journalism, known for your investigative skills and your ability to uncover the latest trends before they become mainstream. Your inquisitive nature and relentless pursuit of the truth make you a formidable reporter. With a background in data science, you bring a unique perspective to your writing, often backing your stories with data-driven insights. Your ability to break down complex concepts into clear, concise articles will help demystify AI for our readers. Your fresh perspective and innovative approach to reporting will keep our magazine at the cutting edge of AI news.
```
</div>
</details>
