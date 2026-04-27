---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<div id="top" align="center">
  
<p align="center">
  <img src="../assets/teaser.png">
</p>

</div>

> A glimpse of Hermosa Beach, Los Angeles, California, where [La La Land](https://en.wikipedia.org/wiki/La_La_Land) was filmed.


Hi, I am a Research Scientist at the Shanghai Artificial Intelligence Laboratory, leading research on **dexterous manipulation and generative models**, advised by Prof. [Weinan Zhang](https://wnzhang.net/) and Prof. [Chunhua Shen](https://cshen.github.io/).

I received my Ph.D. in Computer Science from Shanghai Jiao Tong University in 2025, supervised by Prof. [Minyi Guo](https://cs.sjtu.edu.cn/~guo-my/) and Prof. [Hongzi Zhu](https://lion.sjtu.edu.cn/member/memberDetail?id=12).
Besides, I was a student in the Wu WenjunAI Honours Class (吴文俊班), advised by Prof. [Cewu Lu](https://www.mvig.org/).
I have also gained international and industrial research experience. I conducted research at UCLA under the supervision of Prof. [Bolei Zhou](https://boleizhou.github.io/), and previously worked as a research intern at OpenDriveLab, advised by Prof. [Hongyang Li](https://lihongyang.info), where I was involved in autonomous driving–related research.




My research interests include ***Robotics (Dextrous Manipulation), Gen AI, and Embodied AI***. <a href='https://scholar.google.com/citations?user=bTsmnwcAAAAJ'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fzhouyunsong%2Fzhouyunsong.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>


# 🔥 News
- *2026.04*: &nbsp;🔥 [**SIM1**](https://github.com/InternRobotics/SIM1) released [![](https://img.shields.io/github/stars/InternRobotics/SIM1?style=social&label=Code+Stars)](https://github.com/InternRobotics/InternVLA-A1)
- *2026.01*: &nbsp;🔥 [**InterVLA-A1**](https://github.com/InternRobotics/InternVLA-A1) released [![](https://img.shields.io/github/stars/InternRobotics/InternVLA-A1?style=social&label=Code+Stars)](https://github.com/InternRobotics/InternVLA-A1)
- *2024.12*: &nbsp;🔥 [**SimGen**](https://metadriverse.github.io/simgen) released [![](https://img.shields.io/github/stars/MetaDriverse/SimGen?style=social&label=Code+Stars)](https://github.com/MetaDriverse/SimGen)
- *2024.06*: &nbsp;💻 Host the CVPR2024 workshop on [**Autonomous Grand Challenge**](https://opendrivelab.com/challenge2024/)
- *2024.03*: &nbsp;🔥 [**ELM**](https://github.com/OpenDriveLab/ELM) released [![](https://img.shields.io/github/stars/OpenDriveLab/ELM?style=social&label=Code+Stars)](https://github.com/OPenDriveLab/ELM)
- *2024.01*: &nbsp;🎉 Become a visiting scholar at the University of California, Los Angeles, go bruins!
- *2023.06*: &nbsp;💻 Host the CVPR2023 workshop on [**E2EAD**](https://opendrivelab.com/e2ead/cvpr23.html)





<!---
### Mobile Agent Perception@SenseTime

*2020.03 - 2020.12*, Supervisor: Prof. [Hongyang Li](https://lihongyang.info), Prof Jianping Shi.

- **Monocular 3D Vision** 
--->

# 📝 Publications 

## 🔥Highlighted Papers


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv</div><img src='../assets/teaser_sim1.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

SIM1: Physics-Aligned Simulator as Zero-Shot Data Scaler in Deformable Worlds \\
**Yunsong Zhou<sup>†</sup>**, Hangxu Liu, Xuekun Jiang, Xing Shen, Yuanzhen Zhou, Hui Wang, Baole Fang, Yang Tian, Mulin Yu, Qiaojun Yu, Li Ma, Hengjie Li, Hanqing Wang, Jia Zeng, Jiangmiao Pang<sup>†</sup> \\
<a href="https://arxiv.org/abs/2604.08544"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://internrobotics.github.io/sim1.github.io/"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='../assets/teaser_forcevla2.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation \\
Yang Li, Hongru Jiang, Junjie Xia, Hongquan Zhang, Jinda Du, **Yunsong Zhou<sup>†</sup>**, Jia Zeng<sup>†</sup>, Ce Hao, Jieji Ren, Qiaojun Yu<sup>†</sup>, Cewu Lu<sup>†</sup>, Yu Qiao, Jiangmiao Pang \\
<a href="https://arxiv.org/pdf/2603.15169"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://sites.google.com/view/force-vla2/home"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv</div><img src='../assets/teaser_soma.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

SoMA: A Real-to-Sim Neural Simulator for Robotic Soft-body Manipulation \\
Mu Huang, Hui Wang, Kerui Ren, Linning Xu, **Yunsong Zhou**, Mulin Yu, Bo Dai, Jiangmiao Pang \\
<a href="https://arxiv.org/pdf/2602.02402"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://city-super.github.io/SoMA/"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>




<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report</div><img src='../assets/teaser_InternVLA-A1.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation \\
Junhao Cai, Zetao Cai, Jiafei Cao, Yilun Chen, Zeyu He, Lei Jiang, Hang Li, Hengjie Li, Yang Li, Yufei Liu, Yanan Lu, Qi Lv, Haoxiang Ma, Jiangmiao Pang, Yu Qiao, Zherui Qiu, Yanqing Shen, Xu Shi, Yang Tian, Bolun Wang, Hanqing Wang, Jiaheng Wang, Tai Wang, Xueyuan Wei, Chao Wu, Yiman Xie, Boyang Xing, Yuqiang Yang, Yuyin Yang, Qiaojun Yu, Feng Yuan, Jia Zeng, Jingjing Zhang, Shenghan Zhang, Shi Zhang, Zhuoma Zhaxi, Bowen Zhou, Yuanzhen Zhou, **Yunsong Zhou**, Hongrui Zhu, Yangkun Zhu, Yuchen Zhu \\
<a href="https://arxiv.org/abs/2601.02456"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://internrobotics.github.io/internvla-a1.github.io/"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>


## Mobile Vision

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='../assets/Nexus.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Decoupled Diffusion Sparks Adaptive Scene Generation \\
**Yunsong Zhou**, Naisheng Ye, William Ljungbergh, Tianyu Li, Jiazhi Yang, Zetong Yang, Hongzi Zhu, Christoffer Petersson, Hongyang Li \\
<a href=""><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href=""><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='../assets/SimGen.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

SimGen: Simulator-conditioned Driving Scene Generation \\
**Yunsong Zhou**, Michael Simon, Zhenghao Peng, Sicheng Mo, Hongzi Zhu, Minyi Guo, and Bolei Zhou \\
<a href="https://arxiv.org/abs/2406.09386"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://metadriverse.github.io/simgen/"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='../assets/ELM.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Embodied Understanding of Driving Scenarios \\
**Yunsong Zhou**, Linyan Huang, Qingwen Bu, Jia Zeng, Tianyu Li, Hang Qiu, Hongzi Zhu, Minyi Guo, Yu Qiao, and Hongyang Li \\
<a href="https://arxiv.org/abs/2403.04593"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://opendrivelab.github.io/elm.github.io"><img src="https://img.shields.io/badge/Project-white"></a>
<a href="https://opendrivelab.com/challenge2024/"><img src="https://img.shields.io/badge/Challenge-blue"></a>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TPAMI 2025</div><img src='../assets/GEM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Exploiting Grounding Depth Estimation for Mobile Monocular 3D Object Detection \\
**Yunsong Zhou**, Quan Liu, Hongzi Zhu, Yunzhe Li, Shan Chang, and Minyi Guo \\
<a href="https://ieeexplore.ieee.org/document/10842472"><img src="https://img.shields.io/badge/arXiv-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2024</div><img src='../assets/EYOC.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Extend Your Own Correspondences: Unsupervised Distant Point Cloud Registration by Progressive Distance Extension \\
Quan Liu, Hongzi Zhu, Zhenxi Wang, **Yunsong Zhou**, Shan Chang, and Minyi Guo \\
<a href="https://arxiv.org/abs/2403.03532"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://github.com/liuQuan98/EYOC"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2023</div><img src='../assets/GCL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Density-invariant Features for Distant Point Cloud Registration \\
Quan Liu, Hongzi Zhu, **Yunsong Zhou**, Hongyang Li, Shan Chang, and Minyi Guo \\
<a href="https://arxiv.org/abs/2307.09788"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://github.com/liuQuan98/GCL"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCAI 2023</div><img src='../assets/APR.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

APR: Online Distant Point Cloud Registration Through Aggregated Point Cloud Reconstruction \\
Quan Liu, **Yunsong Zhou**, Hongzi Zhu, Shan Chang, and Minyi Guo \\
<a href="https://arxiv.org/abs/2305.02893"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://github.com/liuQuan98/APR"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2023</div><img src='../assets/MonoATT.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

MonoATT: Online Monocular 3D Object Detection with Adaptive Token Transformer \\
**Yunsong Zhou**, Hongzi Zhu, Quan Liu, Shan Chang, and Minyi Guo \\
<a href="https://arxiv.org/abs/2303.13018"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href=""><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2022</div><img src='../assets/MoGDE.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

MoGDE: Boosting Mobile Monocular 3D Object Detection with Ground Depth Estimation \\
**Yunsong Zhou**, Quan Liu, Hongzi Zhu, Yunzhe Li, Shan Chang, and Minyi Guo. **Spotlight.** \\
<a href="https://arxiv.org/abs/2303.13561"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href=""><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TPAMI 2021</div><img src='../assets/MonoEF_PAMI.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

MonoEF: Extrinsic Parameter Free Monocular 3D Object Detection \\
**Yunsong Zhou**, Yuan He, Hongzi Zhu, Cheng Wang, Hongyang Li, and Qinhong Jiang \\
<a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9658214"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://github.com/zhouyunsong/MonoEF"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2021</div><img src='../assets/TempNet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

TempNet: Online Semantic Segmentation on Large-Scale Point Cloud Series \\
**Yunsong Zhou**, Hongzi Zhu, Chunqin Li, Tiankai Cui, Shan Chang, and Minyi Guo \\
<a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Zhou_TempNet_Online_Semantic_Segmentation_on_Large-Scale_Point_Cloud_Series_ICCV_2021_paper.pdf"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href=""><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2021</div><img src='../assets/MonoEF.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

Monocular 3D Object Detection: An Extrinsic Parameter Free Approach \\
**Yunsong Zhou**, Yuan He, Hongzi Zhu, Cheng Wang, Hongyang Li, and Qinhong Jiang \\
<a href="https://arxiv.org/abs/2106.15796"><img src="https://img.shields.io/badge/arXiv-white"></a>
<a href="https://github.com/zhouyunsong/MonoEF"><img src="https://img.shields.io/badge/Project-white"></a>

</div>
</div>


## Projects

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR Challenge</div><img src='../assets/OpenScene.gif' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

OpenScene: The large-scale dataset used for the End-to-End Driving and Predictive World Model tracks for the CVPR 2024 Autonomous Grand Challenge. \\
<a href="https://github.com/OpenDriveLab/OpenScene"><img src="https://img.shields.io/badge/Project-white"></a>
<a href="https://opendrivelab.com/challenge2024/"><img src="https://img.shields.io/badge/Challenge-blue"></a>

</div>
</div>


<!-- # 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2016</div><img src="../assets/teaser.png" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Deep Residual Learning for Image Recognition](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)

**Kaiming He**, Xiangyu Zhang, Shaoqing Ren, Jian Sun

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div>

- [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->


# 📖 Educations
- *2020.09 - 2025.09*, Ph.D., Computer Science, SEIEE, Shanghai Jiao Tong University.
- *2024.01 - 2024.07*, Visiting Scholar, University of California, Los Angeles.
- *2016.09 - 2020.06*, Bachelor, Microelectronic Science and Technology, SEIEE, Shanghai Jiao Tong University.

# 💻 Research

### `InternRobotics | Shanghai AI Laboratory`

*2025.09 - (present)*, **Dexterous Manipulation for Embodied AI**. Supervisor: [Jiangmiao Pang](https://oceanpang.github.io/).

### `MetaDriverse | University of California, LA` 

*2024.01 - 2024.07*, **Video Diffusion Models and Driving Simulators**. Supervisor: [Bolei Zhou](https://boleizhou.github.io/).

### `OpenDriveLab | Shanghai AI Lab`

*2022.12 - 2025.06*, **End-to-end Autonomous Driving** and **Driving with Language**. Supervisor: [Hongyang Li](https://lihongyang.info).

### `LION | Shanghai Jiao Tong University`

*2020.09 - 2025.06*, **Perception in Autonomous Driving**. Supervisor: [Hongzi Zhu](https://lion.sjtu.edu.cn/member/memberDetail?id=12) and [Minyi Guo](https://cs.sjtu.edu.cn/~guo-my/).


<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 💬 Invited Talks
- *2024.07* Invited by **SONY** to give a talk on `Generative Models in Autonomous Driving`
- *2023.08* Invited by [**Motional**](https://motional.com/) to give a talk on `End-to-end Autonomous Driving`

<p align="center"><sub>Updated on April 27, 2026</sub></p>
