# 📝 Week 08 实验汇报：基于 Docker 的 ROS2 环境容器化部署
## 1. 实验目标
在 Windows (WSL2) 和 Mac 系统上完成 Docker Desktop 的安装与配置。

掌握 Docker 的基本指令，实现 ROS2 镜像的拉取与容器运行。

解决 Docker 容器的图形界面（GUI）转发问题，成功运行小海龟仿真。

## 2. 核心任务说明
🐳 2.1 Docker 环境搭建
Windows：启用 WSL2 后端，并在 Docker Desktop 中集成 Ubuntu 22.04。

Mac：针对 Apple Silicon (M1/M2/M3) 架构配置 Docker 环境，确保兼容性。

📦 2.2 ROS2 镜像部署
使用以下流程部署 ROS2 Humble 环境：

拉取镜像：从官方 Docker Hub 获取 osrf/ros:humble-desktop。

创建容器：配置环境变量（DISPLAY）和挂载卷（Volumes），实现代码持久化。

🖥️ 2.3 图形界面转发 (GUI Forwarding)
通过配置 X11 转发（Windows 下使用 WSLg 或 Mac 下使用 XQuartz），实现在容器内启动 turtlesim 窗口并在宿主机显示。

## 3. 实验截图展示


## 4. 关键实验操作
Bash
### 1. 启动带 GUI 转发的 ROS2 容器 (以 Windows 为例)
docker run -it \
  --net=host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  osrf/ros:humble-desktop

### 2. 容器内验证 ROS2 环境
source /opt/ros/humble/setup.bash
ros2 run turtlesim turtlesim_node
## 5. 实验总结
通过 Docker 部署 ROS2，我实现了开发环境的高度解耦。相比于直接在宿主机安装，Docker 能够快速复现环境，避免了复杂的依赖冲突。这对于未来在机器狗、机械臂等不同平台上迁移控制算法具有重大意义。