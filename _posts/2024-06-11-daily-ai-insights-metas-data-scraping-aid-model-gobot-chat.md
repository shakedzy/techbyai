---
layout: post
title: "Daily AI Insights: Meta's Data Scraping, AID Model, GoBot Chat"
subtitle: "Privacy concerns, advanced AI research, and new AI-driven customer support solutions."
audio: 2024-06-11-daily-ai-insights-metas-data-scraping-aid-model-gobot-chat.mp3
date: 2024-06-11
duration: "06:18"
bytes: 1515117
model: gpt-4o
cost: 0.94
processing: "0:02:40.072446"
version: "0.1.10"
headers: " * Can I Opt Out of Meta's A.I. Scraping on Instagram and Facebook? Sort Of. - The New York Times<br /> * AID: Adapting Image2Video Diffusion Models for Instruction-guided Video Prediction<br /> * Adaptive Opponent Policy Detection in Multi-Agent MDPs: Real-Time Strategy Switch Identification Using Running Error Estimation<br /> * Ready to Take on the Giants, GoVeyance Announces the Launch of GoBot Chat at Collision 2024. | The AI Journal<br /> * California Proposes 30 AI Regulation Laws Amid Federal Standstill"
---

# Can I Opt Out of Meta's A.I. Scraping on Instagram and Facebook? Sort Of. - The New York Times
_Summarized by: David Patel_ [[www.nytimes.com](https://www.nytimes.com/2024/06/07/technology/meta-ai-scraping-policy.html)]

Meta has notified European users that, starting June 26, their public posts on Facebook and Instagram will be used to train its AI services, including chatbots. This has raised privacy concerns, although in the U.S., such data scraping is already in effect. Meta asserts it complies with privacy laws and aims to enhance service relevance. Users can opt out of sharing their information, but the specifics of data usage remain unclear. Meta's AI, akin to ChatGPT, is integrated across its platforms and responds to user prompts, aiming to improve user interaction and service personalization.

# AID: Adapting Image2Video Diffusion Models for Instruction-guided Video Prediction
_Summarized by: Emily Chen_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.06465v1)]

The paper introduces AID, a novel approach for text-guided video prediction (TVP). TVP involves predicting future video frames based on initial frames and a text instruction, useful in areas like VR, robotics, and content creation. Traditional TVP methods face challenges with frame consistency due to limited video datasets. AID leverages pretrained Image2Video diffusion models, known for video dynamics, and enhances them with textual control using the Multi-Modal Large Language Model (MLLM).

AID's core innovation is the Dual Query Transformer (DQFormer) architecture, which integrates instructions and frames into conditional embeddings for future frame prediction. Additionally, Long-Short Term Temporal Adapters and Spatial Adapters are introduced for efficient model transfer to specific scenarios with minimal training costs. The method shows significant performance improvements over state-of-the-art techniques on datasets like Something Something V2, Epic Kitchen-100, Bridge Data, and UCF-101, achieving up to 91.2% FVD improvement on Bridge Data.

AID's pipeline includes a 3D U-Net for diffusion, VAE for encoding/decoding, and DQFormer for text conditioning. The model is pretrained on large-scale datasets and fine-tuned for specific tasks, ensuring high-quality, stable video generation. Experimental results validate AID's effectiveness in various domains, demonstrating its potential for future TVP applications.

# Adaptive Opponent Policy Detection in Multi-Agent MDPs: Real-Time Strategy Switch Identification Using Running Error Estimation
_Summarized by: Emily Chen_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2406.06500v1)]

In multi-agent reinforcement learning (MARL), understanding opponents' strategies is crucial, especially in dynamic settings where strategies can change unexpectedly. Traditional algorithms like Proximal Policy Optimization (PPO) struggle in these environments due to high variance and non-stationary opponent policies. The paper introduces OPS-DeMo (Online Policy Switch-Detection Model), an algorithm designed to detect and adapt to changes in opponents' strategies in real-time. OPS-DeMo uses a dynamic error decay mechanism to continuously update its beliefs about opponents' policies and selects appropriate response strategies from a pre-trained policy bank.

Key contributions include:
1. A running error estimation metric that assesses an agent’s compliance with a stochastic policy using only observed state-action pairs.
2. An online algorithm that detects policy switches and adapts the response policy accordingly.
3. An empirical evaluation demonstrating OPS-DeMo's effectiveness in a Predator-Prey scenario, showing improved performance over traditional PPO models in dynamic environments.

The model's architecture involves training response policies against potential opponent policies and dynamically updating beliefs based on observed actions. The method effectively handles sudden policy shifts and is optimized for efficiency, making it suitable for resource-constrained environments. The results indicate that OPS-DeMo provides more consistent rewards and better adaptation to opponents' policy changes compared to standalone PPO models.

# Ready to Take on the Giants, GoVeyance Announces the Launch of GoBot Chat at Collision 2024. | The AI Journal
_Summarized by: David Patel_ [[aijourn.com](https://aijourn.com/ready-to-take-on-the-giants-goveyance-announces-the-launch-of-gobot-chat-at-collision-2024/)]

GoVeyance announced the launch of GoBot Chat at Collision 2024, their third AI feature this year, aimed at transforming customer support for legal firms. GoBot Chat provides real-time assistance, leveraging advanced AI for accurate and immediate responses, and offers 24/7 availability. This launch follows GoVeyance's rapid growth since April 2023, achieving profitability and over $1M in annual recurring revenue. CEO Jessie Vaid emphasizes their commitment to enhancing the legal experience through AI-driven innovation. GoBot Chat will be available to GoVeyance firms starting June 28, 2024, initially in British Columbia.

# California Proposes 30 AI Regulation Laws Amid Federal Standstill
_Summarized by: Sophia Martinez_ [[www.nytimes.com](https://www.nytimes.com/2024/06/10/technology/california-ai-regulation.html)]

California lawmakers have proposed around 30 new AI regulations to protect consumers and jobs, marking one of the most significant efforts to control the technology. The proposed bills aim to impose strict restrictions on AI, addressing concerns such as job displacement, election interference through disinformation, and national security risks. Key measures include preventing AI discrimination in housing and healthcare, and protecting intellectual property and employment. This legislative push follows California's history of pioneering tech consumer protections, like the 2020 privacy law and the 2022 child safety law. As federal regulation lags, state-level initiatives like California's could set national precedents.

<h3><strong>💡 More articles for you:</strong></h3>

* [Realbotix Announces Strategic Partnership with ROBOTIS INC to Enhance AI Integration in Human-Like Robots](https://www.otcmarkets.com/stock/XBOTF/news/Realbotix-Announces-Strategic-Partnership-with-ROBOTIS-INC?id=443347) (www.otcmarkets.com)

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/karpathy/status/1800242310116262150">Loading: twitter.com/karpathy/status/1800242310116262150</a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/RichardSocher/status/1800182894234857878">Loading: twitter.com/RichardSocher/status/1800182894234857878</a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> IllumiNeRF: 3D Relighting without Inverse Rendering](http://arxiv.org/pdf/2406.06527v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Decentralized Personalized Federated Learning](http://arxiv.org/pdf/2406.06520v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Monkey See, Monkey Do: Harnessing Self-attention in Motion Diffusion for Zero-shot Motion Transfer](http://arxiv.org/pdf/2406.06508v1)
* [Apple Intelligence is the company's new generative AI offering TechCrunch](https://techcrunch.com/2024/06/10/apple-intelligence-is-the-companys-new-generative-ai-offering/)
* [Qualcomm Launches AI-Ready IoT Platform at Embedded World 2024IoT World Today](https://www.iotworldtoday.com/connectivity/qualcomm-launches-ai-ready-iot-platform-at-embedded-world-2024)
* [Apple brings ChatGPT to Siri as it debuts ‘Apple Intelligence’ at WWDC 2024 Apple The Guardian](https://www.theguardian.com/technology/article/2024/jun/10/apple-ai-product-launch)
* [AI Stocks: Best Artificial Intelligence Stocks To Watch Amid ChatGPT Hype Investor's Business Daily](https://www.investors.com/news/technology/artificial-intelligence-stocks/)
* [China's Humanoid Robot Advancements Signal a New Era in Robotics](https://m.facebook.com/permalink.php/?story_fbid=409897575303162&id=100088487694208)
* [Introducing Apple Intelligence for iPhone, iPad, and Mac](https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/)
* [Razor Labs Launches DataMind AI™ Version 3.1: Unleashing Next-Gen Predictive Maintenance with Cutting-Edge AI Sensor Fusion and Computer Vision](https://www.morningstar.com/news/pr-newswire/20240610ln35201/razor-labs-launches-datamind-ai-version-31-unleashing-next-gen-predictive-maintenance-with-cutting-edge-ai-sensor-fusion-and-computer-vision)

---
### Technical details
Created at: 11 June, 2024, 03:24:52, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Alexandra Bennett

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a visionary leader with a deep understanding of both traditional journalism and cutting-edge AI technologies. Your knack for storytelling is matched by your technical acumen, making you adept at translating complex AI concepts into engaging, accessible content. You thrive in fast-paced environments and have a proven track record of managing editorial teams to produce high-quality, timely publications. Your strategic mindset and innovative approach will drive the magazine's growth and influence in the rapidly evolving field of Generative AI.
```

Emily Chen:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned technology journalist with over a decade of experience covering the tech industry. Your background in computer science gives you a unique edge in understanding and explaining complex AI concepts. You have a knack for breaking down technical jargon into engaging, reader-friendly content. Your ability to identify emerging trends and your extensive network of industry contacts make you a valuable asset to our team. You are always on the lookout for the next big story in AI and Generative AI, and your analytical skills ensure that your articles are both insightful and informative.
```

David Patel:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic and curious reporter with a strong background in data science and machine learning. Your passion for AI drives you to stay updated with the latest research and developments in the field. You have a talent for storytelling, making complex AI topics accessible and interesting to a broad audience. Your writing is characterized by clarity and depth, often highlighting the real-world applications and implications of AI technologies. Your enthusiasm and dedication to uncovering the latest trends in Generative AI make you an indispensable part of our editorial team.
```

Sophia Martinez:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are an innovative journalist with a deep understanding of AI ethics and policy. Your interdisciplinary approach combines expertise in technology with a keen awareness of its societal impacts. You excel at exploring the ethical dimensions of AI and Generative AI, bringing a critical perspective to your reporting. Your articles often provoke thoughtful discussions and provide readers with a comprehensive view of the implications of AI advancements. Your ability to connect with experts and thought leaders in the field ensures that your reporting is both authoritative and insightful.
```
</div>
</details>
