<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,30:0a192f,70:1a1a2e,100:16213e&height=220&section=header&text=Sutharsan%20K&fontSize=55&fontColor=58a6ff&animation=fadeIn&fontAlignY=38&desc=ROS2%20%C2%B7%20Autonomous%20Robotics%20%C2%B7%20AI%20Systems&descAlignY=60&descColor=8b949e&descSize=20" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2500&pause=800&color=58A6FF&center=true&vCenter=true&multiline=true&width=700&height=120&lines=Junior+ROS2+Developer+%40+Spotless+AI;Building+autonomous+robots+in+hospitals;Perception+%7C+Nav2+%7C+AI+Agents;From+simulation+to+real+deployment+🤖;Let+the+robots+do+the+work.)](https://git.io/typing-svg)

<br/>

[![Portfolio](https://img.shields.io/badge/🌐%20Portfolio-sutharsan.is--a.dev-58a6ff?style=for-the-badge&logoColor=white)](https://sutharsan.is-a.dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sutharsan311)
[![Email](https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sutharsanmail311@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sutharsan-311)

![Profile Views](https://komarev.com/ghpvc/?username=sutharsan-311&color=58a6ff&style=for-the-badge&label=PROFILE+VIEWS)
![Open to Work](https://img.shields.io/badge/🟢%20Open%20to%20Work-Robotics%20Engineering%20Roles-22c55e?style=for-the-badge)

</div>

---

<img align="right" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnpodGNxOWdyMndseW41ZTR1Z3FvdGd2ZHNmd3d5OGh1dHdhb2llciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SWoSkN6DxTszqIKEqv/giphy.gif" width="280" />

### About me

I build robots that drive themselves around hospitals at **Spotless AI**, out of Coimbatore, India.

Most of my day is Nav2, LiDAR, depth cameras and a Jetson Orin NX. Simulation is the easy part. The real work starts when the robot leaves Gazebo and meets an actual hospital corridor.

When I hit the same annoyance three times, I write a tool for it. That is where most of the repos below come from.

```python
class Sutharsan:
    role     = "Junior ROS2 Developer"
    company  = "Spotless AI"
    location = "Coimbatore, India"

    day_job = [
        "Autonomous navigation (Nav2)",
        "Perception: LiDAR, RGB-D, open-vocab detection",
        "Hardware integration (ros2_control)",
        "Shipping robots out of simulation and into hospitals",
    ]

    after_hours = [
        "tiny-dllm: a diffusion language model, from scratch",
        "eon: a personal AI assistant on WhatsApp",
        "Flutter apps for my family's garment business",
    ]
```

<br clear="right"/>

---

### 🤖 What I work on

- **Navigation.** Nav2 tuning, costmaps, controllers and lifecycle management on real hardware. I got tired of the edit YAML, kill, relaunch, wait loop, so I built [nav2_config](https://github.com/sutharsan-311/nav2_config).
- **Perception.** Open-vocabulary detection and segmentation (OWLv2, NanoOWL, SAM, NanoSAM), TensorRT on Jetson, projecting 2D detections into 3D and keeping track of them in a scene graph.
- **Edge AI.** Squeezing models onto an Orin NX. Sometimes that works. When it doesn't, I write down why ([unified-perception](https://github.com/sutharsan-311/unified-perception)).
- **Tooling.** Small, sharp tools for things that annoy me: Claude Code plugins, git visualisations, ROS2 utilities.

---

### ⚡ Tech Stack

<div align="center">

**Robotics & Navigation**

[![Robotics Skills](https://skillicons.dev/icons?i=ros,arduino,raspberrypi,cmake&perrow=6)](https://skillicons.dev)

**AI & Perception**

[![AI Skills](https://skillicons.dev/icons?i=pytorch,tensorflow,opencv,python&perrow=6)](https://skillicons.dev)

**Languages & Tools**

[![Dev Skills](https://skillicons.dev/icons?i=python,cpp,bash,git,github,linux,vscode,docker&perrow=8)](https://skillicons.dev)

</div>

---

### 📊 GitHub Stats

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=sutharsan-311&show_icons=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=8b949e&icon_color=58a6ff&ring_color=58a6ff&include_all_commits=true&count_private=true" height="170"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sutharsan-311&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=8b949e&langs_count=6" height="170"/>

<br/>

<img src="https://streak-stats.demolab.com?user=sutharsan-311&theme=github-dark-blue&hide_border=true&background=0d1117&stroke=58a6ff&ring=58a6ff&fire=58a6ff&currStreakLabel=58a6ff" height="150"/>

</div>

---

### 🚀 Featured projects

#### [nav2_config](https://github.com/sutharsan-311/nav2_config) ![Stars](https://img.shields.io/github/stars/sutharsan-311/nav2_config?color=58a6ff&style=flat)

Tune Nav2 on a running robot, no relaunch. It finds live Nav2 nodes, shows every parameter with a description and tuning advice (706 of them across 21 nodes), and pushes changes straight to the stack. It also has lifecycle controls, live topic and TF dropdowns, and YAML save/load. [Watch the demo](https://www.youtube.com/watch?v=e--45aJRZY4).

#### [samowl](https://github.com/sutharsan-311/samowl) ![Stars](https://img.shields.io/github/stars/sutharsan-311/samowl?color=58a6ff&style=flat)

Ask a robot to find "the red chair" and it finds it in 3D. OWLv2 does open-vocabulary detection, SAM (TensorRT) does the masks, depth turns them into 3D positions, and a persistent scene graph remembers objects across frames so you can query by label or distance. C++ runs the ROS2 side, Python runs the ML.

#### [unified-perception](https://github.com/sutharsan-311/unified-perception)

Could one vision encoder feed both NanoOWL and NanoSAM on a Jetson and halve the per-frame cost? I trained a ~525K-param adapter to find out. **It didn't work**: training converged and the masks were useless. The repo is an honest write-up of the idea, the test that caught it, and the lessons. I also raised it upstream in [NVIDIA-AI-IOT/nanosam#42](https://github.com/NVIDIA-AI-IOT/nanosam/issues/42).

#### [tiny-dllm](https://github.com/sutharsan-311/tiny-dllm) [![HF](https://img.shields.io/badge/🤗-model-ffd21e?style=flat)](https://huggingface.co/sutharsan-311/tiny-dllm)

A masked diffusion language model written from scratch in PyTorch. It starts with every token masked and fills them in by confidence, using bidirectional attention. Loss went from 4.2 to 1.4 over 50k steps, and it now writes passable fake Shakespeare.

#### [git-recap](https://github.com/sutharsan-311/git-recap) [![npm](https://img.shields.io/npm/v/git-recap?color=ff6ec4&label=npx%20git-recap&style=flat)](https://www.npmjs.com/package/git-recap)

Spotify Wrapped for your git history. Run `npx git-recap` in any repo and you get an animated story (heatmap, 3AM commits, your favourite commit words, a personality verdict) plus a shareable SVG card. It runs locally with zero dependencies: no API key, nothing uploaded.

#### [claude-sudo](https://github.com/sutharsan-311/claude-sudo)

`sudo` hangs in Claude Code because there is no TTY. This plugin adds a hook that asks you to approve each root command, then feeds sudo the password from GNOME Keyring through `SUDO_ASKPASS`. Your password never touches the transcript. Linux only.

#### [robotics-playbook](https://github.com/sutharsan-311/robotics-playbook)

Notes from real deployments: ROS2, navigation and AI-robotics, written down so I stop relearning them.

---

### 🔧 Upstream contributions

- **ros/rosdistro**: added the `python3-pyqt6` rosdep key (merged) and submitted nav2_config for Humble and Jazzy
- **ros-navigation/navigation2**: proposed snake_case plugin names in `nav2_params.yaml`
- **ros2/rcutils**: proposed a `SUCCESS` log severity between INFO and WARN
- **NVIDIA-AI-IOT/nanosam**: reported the shared-encoder adapter findings ([#42](https://github.com/NVIDIA-AI-IOT/nanosam/issues/42))
---

### 🐍 Contribution Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sutharsan-311/sutharsan-311/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sutharsan-311/sutharsan-311/output/github-contribution-grid-snake.svg" />
  <img alt="GitHub contribution snake" src="https://raw.githubusercontent.com/sutharsan-311/sutharsan-311/output/github-contribution-grid-snake-dark.svg" />
</picture>

### 🌐 3D Contribution Calendar

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sutharsan-311/sutharsan-311/output/profile-3d-contrib/profile-night-rainbow.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sutharsan-311/sutharsan-311/output/profile-3d-contrib/profile-gitblock.svg" />
  <img alt="3D Contribution Calendar" src="https://raw.githubusercontent.com/sutharsan-311/sutharsan-311/output/profile-3d-contrib/profile-night-rainbow.svg" />
</picture>

---

<!-- EON:CURRENTLY_BUILDING -->
> **Currently building:** `samowl` — open-vocab 3D detection for ROS2 · `nav2_config` — live Nav2 tuning · `eon` — personal AI assistant · `tiny-dllm` — masked diffusion LM from scratch
<!-- EON:CURRENTLY_BUILDING_END -->

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:1a1a2e,100:0d1117&height=120&section=footer" width="100%"/>
</div>
