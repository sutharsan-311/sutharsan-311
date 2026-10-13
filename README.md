<a href="https://sutharsan.is-a.dev"><img src="assets/hero.svg" width="100%" alt="Sutharsan K, Robotics Engineer at Spotless AI"/></a>

<div align="center">

[![Portfolio](https://img.shields.io/badge/sutharsan.is--a.dev-0b0906?style=flat-square&logo=googlechrome&logoColor=ffb347)](https://sutharsan.is-a.dev)
[![LinkedIn](https://img.shields.io/badge/linkedin-0b0906?style=flat-square&logo=linkedin&logoColor=ffb347)](https://linkedin.com/in/sutharsan311)
[![Email](https://img.shields.io/badge/email-0b0906?style=flat-square&logo=gmail&logoColor=ffb347)](mailto:sutharsanmail311@gmail.com)
![Views](https://komarev.com/ghpvc/?username=sutharsan-311&color=ffb347&style=flat-square&label=views)

</div>

```
> whoami
```

**Sutharsan K** is a robotics engineer at **Spotless AI**, building autonomous robots that navigate hospitals. The work sits where navigation, perception and real hardware meet, and most of it happens after the robot leaves simulation, which is where robots discover that glass doors exist.

Sutharsan wrote [**nav2_config**](https://github.com/sutharsan-311/nav2_config) ![stars](https://img.shields.io/github/stars/sutharsan-311/nav2_config?style=flat-square&label=★&labelColor=0b0906&color=0b0906&logoColor=ffb347), the live Nav2 tuning GUI that roboticists use to change navigation parameters on a running robot without a relaunch, and [**samowl**](https://github.com/sutharsan-311/samowl), an open-vocabulary 3D object detection and scene graph system for ROS2. Type "find the red chair" and the robot goes looking for it.

```
> ros2 node list --verbose
```

| node | what runs there |
|:--|:--|
| `/navigation` | Nav2 tuning, costmaps, controllers and lifecycle management on real robots |
| `/perception` | LiDAR and RGB-D pipelines, open-vocabulary detection and segmentation with OWLv2 and SAM |
| `/edge_ai` | Fitting models onto a Jetson Orin NX with TensorRT, and measuring what it actually costs |
| `/hardware` | Bringing up drivers and controllers with ros2_control |

```
> ls case_files/
```

<p align="center">
<a href="https://sutharsan.is-a.dev"><img src="assets/case-001.svg" width="49%" alt="Case file 001: UV Disinfection Robot, redacted"/></a>
<a href="https://sutharsan.is-a.dev"><img src="assets/case-002.svg" width="49%" alt="Case file 002: Krishi Bot, redacted"/></a>
</p>

```
> ros2 topic echo /field_notes
```

```yaml
data: "a robot that works in simulation is a hypothesis"
---
data: "tune inflation_radius and cost_scaling_factor together. a soft gradient keeps the robot centred in corridors instead of hugging walls"
---
data: "before blaming the controller, check TF. a stale transform looks exactly like bad tuning"
---
data: "benchmark on the Jetson, not the laptop. the laptop always lies"
---
# waiting for next message...
```

```
> ros2 pkg list --stack
```

<p>
<img src="https://img.shields.io/badge/ROS2-0b0906?style=flat-square&logo=ros&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/Nav2-0b0906?style=flat-square&logo=ros&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/C++-0b0906?style=flat-square&logo=cplusplus&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/Python-0b0906?style=flat-square&logo=python&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/PyTorch-0b0906?style=flat-square&logo=pytorch&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/TensorRT-0b0906?style=flat-square&logo=nvidia&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/OpenCV-0b0906?style=flat-square&logo=opencv&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/Jetson-0b0906?style=flat-square&logo=nvidia&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/Docker-0b0906?style=flat-square&logo=docker&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/Linux-0b0906?style=flat-square&logo=linux&logoColor=ffb347"/>
<img src="https://img.shields.io/badge/CMake-0b0906?style=flat-square&logo=cmake&logoColor=ffb347"/>
</p>

<details>
<summary><code>> cat /etc/classified</code></summary>
<br/>

```
Permission denied. clearance level: visitor
```

</details>

<a href="https://sutharsan.is-a.dev"><img src="assets/footer.svg" width="100%" alt="Robot exploring toward the edge of the map"/></a>
