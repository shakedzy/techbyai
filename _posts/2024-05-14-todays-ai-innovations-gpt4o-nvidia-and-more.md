---
layout: post
title: "Today's AI Innovations: GPT-4o, NVIDIA, and More"
subtitle: "Exploring OpenAI's GPT-4o, NVIDIA's AI hardware, and the latest in multimodal search."
audio: 2024-05-14-todays-ai-innovations-gpt4o-nvidia-and-more.mp3
date: 2024-05-14
duration: "07:56"
bytes: 1907181
model: gpt-4o
cost: 2.14
processing: "0:03:48.433444"
version: "0.1.9"
headers: " * OpenAI Releases New Model GPT-4o with Real-Time Vision & Audio Capabilities | Swipe Insight<br /> * NVIDIA’s Dominance and the RTX 40 Series: The growth of AI Hardware | Deepgram<br /> * Building Multimodal Search and RAG - DeepLearning.AI<br /> * Azure OpenAI Service models - Azure OpenAI | Microsoft Learn<br /> * Scaling generative AI with flexible model choices<br /> * SPIN: Simultaneous Perception, Interaction and Navigation<br /> * Localized Adaptive Risk Control"
---

# OpenAI Releases New Model GPT-4o with Real-Time Vision & Audio Capabilities | Swipe Insight
_Summarized by: Priya Kapoor_ [[web.swipeinsight.app](https://web.swipeinsight.app/posts/openai-releases-new-model-gpt-4o-with-real-time-vision-audio-capabilities)]
> **See also:**
> * [OpenAI Unveils GPT-4o, A New State-of-the-Art Multimodal AI Model](https://www.maginative.com/article/openai-unveils-groundbreaking-multimodal-ai-model/) (www.maginative.com)
> * [OpenAI debuts GPT-4o 'omni' model now powering ChatGPT](https://techcrunch.com/2024/05/13/openais-newest-model-is-gpt-4o/) (techcrunch.com)

OpenAI has introduced GPT-4o, a generative AI model that offers real-time responses across audio, text, and vision. It is twice as fast, 50% cheaper, and has a 5x higher rate limit than GPT-4 Turbo. GPT-4o can detect and convey emotions, extract text from images, describe image content, and generate emotive voices. It supports real-time interaction, emotional intelligence, and improved multilingual performance in 50 languages. OpenAI is also launching a desktop version of ChatGPT and a refreshed UI. The new model will be rolled out iteratively across OpenAI's products in the coming weeks.

# NVIDIA’s Dominance and the RTX 40 Series: The growth of AI Hardware | Deepgram
_Summarized by: Priya Kapoor_ [[deepgram.com](https://deepgram.com/learn/growth-of-ai-hardware-nividia-dominance)]

NVIDIA has been a pivotal player in AI hardware, evolving its GPUs from graphics accelerators to essential tools for deep learning. Initially designed for gaming and graphics, GPUs became crucial for AI due to their parallel processing capabilities. NVIDIA's introduction of CUDA in 2006 simplified general-purpose GPU (GPGPU) programming, catalyzing their use in AI. The breakthrough came with AlexNet in 2012, showcasing GPUs' potential in deep learning. NVIDIA's innovations, including Tensor Cores and data center GPUs, further solidified their dominance. The latest advancements, like the RTX 40 series and the upcoming Blackwell architecture, highlight NVIDIA's commitment to leading AI hardware development amidst growing competition.

# Building Multimodal Search and RAG - DeepLearning.AI
_Summarized by: Priya Kapoor_ [[www.deeplearning.ai](https://www.deeplearning.ai/short-courses/building-multimodal-search-and-rag/)]

Learn to build multimodal search and Retrieval-Augmented Generation (RAG) systems with DeepLearning.AI’s new course. The course, led by Sebastian Witalec, covers implementing multimodal models using contrastive learning to create modality-independent embeddings for seamless retrieval across text, images, audio, and video. It teaches how to enhance Large Language Models (LLMs) with multimodal data, enabling them to understand and reason over diverse data types through visual instruction tuning. Practical applications include creating multi-vector recommender systems and analyzing multimodal contexts to generate relevant answers. Basic Python knowledge and familiarity with RAG are recommended. The course is free during the beta phase.

# Azure OpenAI Service models - Azure OpenAI | Microsoft Learn
_Summarized by: Priya Kapoor_ [[learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)]

Azure OpenAI Service offers a range of models with various capabilities and price points. The latest models include GPT-4o and GPT-4 Turbo, which are multimodal, accepting both text and images. GPT-4o is available in a limited early access playground and excels in non-English languages and vision tasks. GPT-4 Turbo, optimized for chat and text completion tasks, is available for standard and provisioned deployments. GPT-3.5 models, including GPT-3.5 Turbo, are also available, optimized for chat and traditional completions. Additionally, embedding models like text-embedding-3-large provide enhanced multi-language retrieval performance. Other models include DALL-E for image generation, Whisper for speech-to-text, and text-to-speech models. Model availability varies by region.

# Scaling generative AI with flexible model choices
_Summarized by: Liam O'Connor_ [[www.ibm.com](https://www.ibm.com/blog/scaling-generative-ai-with-flexible-model-choices/)]

IBM's blog post emphasizes the significance of flexible model choices in scaling generative AI for enterprises. It outlines how diverse model options spur innovation, customize AI for competitive advantage, accelerate time to market, and maintain flexibility amid changing market conditions. The post also highlights the importance of optimizing costs and mitigating risks through a multimodel strategy. IBM's watsonx library offers a range of models, including proprietary, open-source, and third-party options, enabling businesses to select models that best fit their needs. IBM Granite models, known for their trust, performance, and cost-effectiveness, exemplify this approach.

# SPIN: Simultaneous Perception, Interaction and Navigation
_Summarized by: Eleanor Simmons_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.07991v1)]

The paper introduces SPIN, a framework for robots to perform Simultaneous Perception, Interaction, and Navigation in cluttered environments. Traditional approaches often separate perception, planning, and action, leading to inefficiencies and delays. SPIN integrates these processes, allowing the robot to dynamically perceive and react to its surroundings, similar to human coordination of movement and vision.

SPIN utilizes an active visual system, where the robot's camera is not fixed but moves to gather necessary information. This approach is trained using reinforcement learning (RL), where the robot learns to navigate and manipulate objects in cluttered scenarios without needing pre-built maps. The training involves a two-phase process: initially, the robot learns behaviors using a simplified depth representation (scandots), and subsequently, these behaviors are distilled into a policy that operates using real depth images.

The study demonstrates that SPIN significantly outperforms classical methods, especially in dynamic environments. Classical methods rely on static maps and precise measurements, which are impractical in real-world scenarios where environments are constantly changing. SPIN's reactive approach allows for continuous adaptation and real-time decision-making, making it robust against unexpected obstacles and changes in the environment.

The paper also highlights emergent behaviors from SPIN, such as dynamic obstacle avoidance and whole-body coordination, which were not explicitly programmed but developed through extensive training. This capability is crucial for effective navigation and interaction in unstructured, real-world environments.

# Localized Adaptive Risk Control
_Summarized by: Eleanor Simmons_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.07976v1)]

Localized Adaptive Risk Control (L-ARC) is an advanced online calibration method that builds on Adaptive Risk Control (ARC). ARC adjusts prediction set sizes in real-time by modifying a threshold based on past performance, ensuring long-term risk control. However, ARC can unevenly distribute risk guarantees across different input subpopulations, potentially leading to biased outcomes.

L-ARC addresses this by introducing localized statistical risk guarantees, ranging from conditional to marginal risk. It updates a threshold function within a reproducing kernel Hilbert space (RKHS), where the kernel dictates the level of localization. This allows L-ARC to provide more uniform performance across various data subpopulations.

Theoretical results demonstrate a trade-off between the degree of localization and the speed of convergence to the long-term risk target. Experiments show that L-ARC improves fairness and performance in tasks like image segmentation and wireless network beam selection by producing prediction sets that maintain consistent risk guarantees across different subpopulations.

In summary, L-ARC enhances the reliability and fairness of predictive models in online settings by localizing risk control, ensuring that all subpopulations receive adequate attention and performance.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/andrewyng/status/1790088683259048120"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/karpathy/status/1790076925508977096"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1790108163582115862"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/GaryMarcus/status/1790144194150801625"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1790050852776112439"></a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> MambaOut: Do We Really Need Mamba for Vision?](http://arxiv.org/pdf/2405.07992v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> The Platonic Representation Hypothesis](http://arxiv.org/pdf/2405.07987v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Investigating the Semantic Robustness of CLIP-based Zero-Shot Anomaly Segmentation](http://arxiv.org/pdf/2405.07969v1)
* [vFunction's AI-Driven Architectural Observability to Tackle Debt](https://futurumgroup.com/insights/vfunction-unveils-ai-driven-architectural-observability-to-tackle-debt/)

---
### Technical details
Created at: 14 May, 2024, 03:25:58, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Sophia Martinez

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a visionary editor with a passion for the ethical implications of AI and generative technologies. Your background in philosophy and ethics, combined with your writing experience, allows you to tackle complex moral questions and present them in thought-provoking articles. You are an advocate for responsible AI development and enjoy curating content that sparks meaningful conversations among readers. Your innovative approach to storytelling sets you apart in the industry.
```

Eleanor Simmons:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are Eleanor Simmons, a seasoned tech journalist with over a decade of experience in the field. Your expertise lies in dissecting complex AI algorithms and making them accessible to a broader audience. You have a knack for finding the human stories behind technological advancements, which brings a unique and relatable angle to your pieces. Your background in computer science and journalism allows you to bridge the gap between technical details and engaging storytelling. You are meticulous in your research and have a reputation for delivering well-rounded, insightful articles.
```

Liam O'Connor:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are Liam O'Connor, a rising star in the world of tech journalism. With a background in data science and a passion for generative AI, you bring a fresh and innovative perspective to your writing. You are known for your ability to spot emerging trends and predict the next big thing in AI. Your articles are not only informative but also thought-provoking, often challenging readers to think about the ethical implications of new technologies. Your youthful energy and forward-thinking mindset make you a perfect fit for covering the latest developments in AI and generative technologies.
```

Priya Kapoor:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are Priya Kapoor, a dedicated reporter with a strong focus on the ethical and societal impacts of AI. With a background in philosophy and ethics, your writing delves deep into the moral questions surrounding AI advancements. You are passionate about advocating for responsible AI development and ensuring that technological progress benefits society as a whole. Your articles often feature interviews with leading ethicists, policymakers, and AI researchers, providing a well-rounded view of the issues at hand. Your thoughtful and balanced approach to journalism makes you a respected voice in the field.
```
</div>
</details>
