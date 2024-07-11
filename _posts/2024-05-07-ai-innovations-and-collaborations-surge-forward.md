---
layout: post
title: "AI Innovations and Collaborations Surge Forward"
subtitle: "Microsoft, OpenAI, and US Air Force Lead Today's AI Advancements"
audio: 2024-05-07-ai-innovations-and-collaborations-surge-forward.mp3
date: 2024-05-07
duration: "06:59"
bytes: 1679565
model: gpt-4-turbo
cost: 1.56
processing: "0:05:10.326486"
version: "0.1.9"
headers: " * Microsoft readies new AI model to compete with Google, ChatGPT<br /> * MemoryMamba: Memory-Augmented State Space Model for Defect Recognition<br /> * ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection<br /> * OpenAI Gifts Voice to All Users in First Release Since Board Debacle<br /> * US Air Force Conducts Revolutionary AI-Controlled Fighter Jet Test<br /> * Stack Overflow signs deal with OpenAI to supply data to its models ...<br /> * US State Privacy Legislation Tracker"
---

# Microsoft readies new AI model to compete with Google, ChatGPT
_Summarized by: Samantha Cho_ [[nypost.com](https://nypost.com/2024/05/06/business/microsoft-readies-new-ai-model-to-compete-with-google-chatgpt-owner-openai-report/)]

Microsoft is developing MAI-1, a new AI language model poised to compete with Google and OpenAI's ChatGPT. Led by Mustafa Suleyman, a recent addition from Google DeepMind, this initiative aims to boost Microsoft's AI prowess. Described as significantly larger than previous models, MAI-1 will debut at the Build developer conference. Its potential applications hinge on its performance, supported by heavy investments in Nvidia GPU-equipped servers. Microsoft's strategy includes leveraging OpenAI technology and launching models like Phi-3-mini, highlighting its ambition in generative AI.

# MemoryMamba: Memory-Augmented State Space Model for Defect Recognition
_Summarized by: Alex Rivera_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.03673v1)]

MemoryMamba is a new state space model enhanced with memory augmentation, tailored for defect detection in industrial settings. Traditional models like CNNs often struggle with limited or imbalanced data, common in specialized industries. MemoryMamba integrates memory networks that retain and access crucial defect-related information, improving defect recognition.

The model features a fusion module that combines inputs from coarse and fine memory networks, optimizing detection. This setup enhances adaptability across manufacturing environments and handles scarce data scenarios effectively.

Extensive testing across four industrial datasets showed that MemoryMamba outperforms traditional models, capturing dependencies and intricate defect characteristics essential for high-quality detection. Its design incorporates contrastive learning and mutual information maximization, boosting performance.

MemoryMamba's integration of state space models with memory augmentation marks a significant advancement in automated defect detection, offering a robust solution for modern manufacturing complexities.

# ScrewMimic: Bimanual Imitation from Human Videos with Screw Space Projection
_Summarized by: Alex Rivera_ [[<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> arxiv.org](http://arxiv.org/pdf/2405.03666v1)]

Bimanual manipulation, where robots use both arms in a coordinated manner, is complex due to the high degree of freedom and the need for precise timing and spatial coordination. The paper introduces "SCREW MIMIC," a new framework to teach robots bimanual tasks by mimicking human actions from videos. This method leverages screw theory, where the interaction between two hands is modeled as a one-degree-of-freedom screw motion, simplifying the learning process.

SCREW MIMIC captures a human performing a task using a video, then analyzes this video to model the task as a screw motion involving both rotational and translational movement. This model predicts and fine-tunes the robot's actions through self-supervised learning, significantly improving upon traditional methods that require extensive pre-programming or are limited to less complex tasks.

The effectiveness of SCREW MIMIC is demonstrated through various complex tasks like opening a bottle or stirring a pot, showing that it can adapt to different scenarios and outperform existing methods. This approach enhances the robot's ability to perform dual-arm manipulations and provides a scalable way to teach robots new tasks with minimal human intervention.

# OpenAI Gifts Voice to All Users in First Release Since Board Debacle
_Summarized by: Jordan McKenzie_ [[aibusiness.com](https://aibusiness.com/nlp/openai-gifts-voice-to-all-users-in-first-release-since-board-debacle)]

OpenAI has recently made its voice capabilities accessible to all users of ChatGPT, a significant update following a notable boardroom incident involving the temporary dismissal of CEO Sam Altman. This feature, previously exclusive to ChatGPT Plus and Enterprise users, allows for voice interaction with ChatGPT, enhancing user experience by enabling spoken inputs and receiving audio responses. The implementation utilizes Whisper v3, OpenAI's advanced speech recognition model, which boasts increased accuracy and broader commercial use. This update was first demonstrated in September alongside an update permitting image inputs, marking a substantial expansion in ChatGPT's interactive capabilities.

# US Air Force Conducts Revolutionary AI-Controlled Fighter Jet Test
_Summarized by: Jordan McKenzie_ [[elblog.pl](https://elblog.pl/2024/05/06/us-air-force-conducts-revolutionary-ai-controlled-fighter-jet-test/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "USAF Test Pilot School and DARPA announce breakthrough in aerospace machine learning" | slugify %}
 * [USAF Test Pilot School and DARPA announce breakthrough in aerospace machine learning]({{ '2024/04/19/todays-ai-frontiers-innovations-and-regulations#' | append: article_title | relative_url }}) 2024-04-19
</blockquote>

The United States Air Force recently tested an AI-controlled fighter jet, the X-62A VISTA, modeled after the F-16, in a simulated air combat scenario against a human pilot. The AI demonstrated its capability to autonomously handle complex combat maneuvers. Air Force Commander Frank Kendall, who observed from the cockpit, affirmed the AI's efficiency and reliability in controlling combat aircraft. This test aligns with the Air Force's plan to deploy over 1,000 AI-operated jets by 2028. Despite technological advancements, concerns about the ethical and legal implications of AI in combat persist. The Air Force assures that all AI operations will adhere to strict regulations to prevent unauthorized actions.

# Stack Overflow signs deal with OpenAI to supply data to its models ...
_Summarized by: Jordan McKenzie_ [[techcrunch.com](https://techcrunch.com/2024/05/06/stack-overflow-signs-deal-with-openai-to-supply-data-to-its-models/)]

Stack Overflow has partnered with OpenAI to improve AI model responses on programming topics, notably in ChatGPT. This collaboration, set to roll out new platform features by June, marks a shift from Stack Overflow's previous ban on AI-generated responses due to quality concerns. The partnership also introduces a conversational search tool utilizing Stack Overflow's extensive database to answer user queries. Despite some developer backlash over accuracy and privacy, the integration of AI tools is increasingly common in developer workflows. This strategic move aims to keep Stack Overflow relevant and financially viable amidst challenges like declining traffic and cost pressures.

# US State Privacy Legislation Tracker
_Summarized by: Jordan McKenzie_ [[iapp.org](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/)]
<blockquote class='previous-titles' markdown='1' >
**Previous headlines:**

{% assign article_title = "IAPP GPS 2024: Growing Complexities of Digital Governance and AI Regulation" | slugify %}
 * [IAPP GPS 2024: Growing Complexities of Digital Governance and AI Regulation]({{ '2024/04/04/ais-transformative-leap-todays-highlights#' | append: article_title | relative_url }}) 2024-04-04
</blockquote>

The IAPP Westin Research Center offers an up-to-date tracker of U.S. state privacy legislation, focusing on comprehensive privacy bills. It features a map and a detailed chart, categorizing key provisions into consumer rights and business obligations. Each provision is marked with an "X" to denote inclusion. The tracker also links to the full texts of enacted laws. As of the latest update, several states have enacted comprehensive privacy laws, with many others proposing bills, making this a vital resource for professionals navigating the evolving landscape of state-level privacy regulations in the U.S.

## Trending on Twitter
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/AndrewYNg/status/1787525611864695148"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/GaryMarcus/status/1787514538528841958"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/GaryMarcus/status/1787484156743860614"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/Yampeleg/status/1787466323485757743"></a></div>
</blockquote>
<blockquote class="twitter-tweet" data-media-max-width="560" data-dnt="true" style="background-color: white; border-left: 0px; padding: 0px;">
<div class="loading" style="width: 100%; border-left: 0px;"><a href="https://twitter.com/ylecun/status/1787479714577182983"></a></div>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

**Other headlines:**
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Language-Image Models with 3D Understanding](http://arxiv.org/pdf/2405.03685v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> Can LLMs Deeply Detect Complex Malicious Queries? A Framework for Jailbreaking via Obfuscating Intent](http://arxiv.org/pdf/2405.03654v1)
* [<img src="{{ 'images/pdf.png' | relative_url }}" style='vertical-align: middle; width: 1.2em;' /> When LLMs Meet Cybersecurity: A Systematic Literature Review](http://arxiv.org/pdf/2405.03644v1)
* [AI/ML Innovations Inc. Unveils Breakthrough in Cardiac Care with Long ECG Neural Network](https://agoracom.com/ir/AIMLInnovations/forums/discussion/topics/801100-ai-ml-innovations-inc-unveils-breakthrough-in-cardiac-care-with-long-ecg-neural-network/messages/2412090)
* [2024: Year of Robots Transforming the World](https://www.linkedin.com/pulse/2024-year-robots-transforming-world-awesome-analytics-nl4tc)
* [AI in Education: New Research 6th May](https://www.linkedin.com/pulse/ai-education-new-research-6th-may-ray-fleming-h7xge?trk=public_post_main-feed-card_reshare_feed-article-content)
* [Accenture and Oracle Collaborate to Help Clients Accelerate ...](https://newsroom.accenture.com/news/2024/accenture-and-oracle-collaborate-to-help-clients-accelerate-generative-ai-adoption-starting-with-the-finance-organization)

---
### Technical details
Created at: 07 May, 2024, 03:26:25, using `{{ page.model }}`.

Processing time: {{ page.processing }}, cost: {{ page.cost }}$
<details>
<summary>The Staff</summary>
<div markdown="1">
Editor: Lena Zhou

```
You are the Editor-in-Chief of a daily AI and Generative AI specifically magazine named "Tech by AI". Your background as a multimedia storyteller and your extensive experience in digital publishing set you apart. You are particularly skilled at leveraging multimedia tools and platforms to enhance storytelling, making complex topics in AI and Generative AI engaging and understandable to a broad audience. Under your leadership, the magazine is known for its interactive articles, podcasts, and video interviews, which effectively capture the dynamic nature of the AI industry. Your proactive approach in embracing new digital formats has significantly expanded the magazine’s reach and influence.
```

Alex Rivera:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a seasoned journalist with over a decade of experience in technology reporting. Your strength lies in your deep understanding of AI trends and your ability to explain complex technological concepts in a way that is accessible to a broad audience. You have a knack for uncovering under-reported stories and bringing them to light, making you an invaluable asset for covering the latest in AI and Generative AI.
```

Samantha Cho:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are a dynamic reporter with a background in data science, which gives you a unique edge when it comes to reporting on AI. Your analytical skills enable you to sift through vast amounts of information and identify the most significant developments. You are particularly adept at creating engaging multimedia content, which makes your articles not only informative but also visually compelling.
```

Jordan McKenzie:

```
You are a reporter of a daily AI and Generative AI specifically magazine named "Tech by AI". You are an investigative journalist with a keen interest in the ethical implications of AI. Your reporting often focuses on the societal impacts of technology, making you the perfect candidate to explore the broader consequences of advancements in Generative AI. Your ability to engage with experts and laypeople alike ensures that your articles are both thorough and relatable.
```
</div>
</details>
