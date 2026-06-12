# 🤖 Week 14 实验汇报：PyBullet 机器狗仿真 & TurtleSim 乌龟迷宫

## 1. 实验目标

完成双方向机器人操控实验：

- **方向 A**：基于 PyBullet 物理引擎的四足机器狗仿真，通过手机网页远程发送运动指令
- **方向 B**：基于 ROS2 TurtleSim 的乌龟迷宫探索，实现自主导航与 Web 桥接控制

打通完整链路：手机网页控制器 → Tailscale 内网穿透 → WSL2 虚拟机 → Docker/ROS2 → PyBullet 仿真 → 机器人运动

## 2. 核心实验步骤与原理

### 2.1 Tailscale + WSL2 远程组网

通过 Tailscale 将手机与 WSL Ubuntu 加入同一虚拟网络（Tailscale IP: `100.66.42.5`），解决 WSL2 NAT 网络下外部设备无法直接访问的问题。

### 🐍 2.2 方向 A — PyBullet 机器狗仿真

- 使用 PyBullet 物理引擎加载四足机器人模型（`server.py`）
- AI Agent 模式通过 DeepSeek API 实现智能决策控制（`agent.py`）
- 关键优化：`PYBULLET_GUI=0` DIRECT 模式（无 GUI），将内存从 600MB 降至 273MB，CPU 从 96% 降至 15%
- 网页控制器（`index.html`）运行在端口 8765

### 🐢 2.3 方向 B — TurtleSim 乌龟迷宫

- ROS2 Humble Docker 容器内运行 TurtleSim 仿真
- 迷宫生成（`maze.py`）与自主探索算法（`explorer.py`）
- Web 桥接（`turtlesim_web_bridge.py`）实现浏览器端控制
- 网页界面（`turtlesim_index.html`）运行在端口 8080

### 📦 2.4 Docker 容器编排

`docker-compose.yml` 管理 ROS2 容器的启动与环境变量配置

## 3. 项目架构

```
手机浏览器 ──→ Tailscale ──→ WSL2 Ubuntu ──→ PyBullet 仿真 (8765)
                   │              │
                   └──────────────┴──────→ Docker/ROS2 TurtleSim (8080)
```

| 端口 | 用途 |
|------|------|
| 8765 | 方向 A 机器狗网页控制器 |
| 8080 | 方向 B 乌龟控制器 |
| 6080 | noVNC 远程桌面 |

## 4. 文件说明

| 文件 | 说明 |
|------|------|
| `server.py` | PyBullet 机器狗仿真服务器 |
| `agent.py` | AI Agent 决策控制器 |
| `maze.py` | 迷宫地图生成 |
| `explorer.py` | 迷宫自主探索器 |
| `index.html` | 机器狗网页控制界面 |
| `docker-compose.yml` | Docker 容器编排配置 |
| `turtlesim_web_bridge.py` | TurtleSim ROS2 Web 桥接 |
| `turtlesim_maze.py` | 乌龟迷宫地图 |
| `turtlesim_explorer.py` | 乌龟迷宫探索 |
| `turtlesim_index.html` | 乌龟控制网页界面 |
| `Week14_项目报告.docx` | 完整项目报告文档 |

## 5. 关键命令

```bash
# 启动 PyBullet 仿真（Agent 模式）
wsl -d Ubuntu-24.04 -u root bash -c "cd /mnt/d/ai-robotics-course/week14_starters/pybullet_dog && DEEPSEEK_API_KEY=sk-xxx PYBULLET_GUI=0 python3 server.py"

# 启动 Docker 容器
wsl -d Ubuntu-24.04 -u root bash -c "service docker start && cd /mnt/d/ai-robotics-course/week14_starters/docker && docker compose up -d"

# 查看日志
wsl -d Ubuntu-24.04 -u root bash -c "cat /tmp/pybullet_wsl.log"
```

## 6. 实验总结

本项目成功打通了从手机网页到仿真机器人的完整控制链路。主要技术挑战及解决方案：

1. **端口转发问题**：Docker 在 WSL2 上端口转发不稳定 → 直接在 WSL 运行 PyBullet，绕过 Docker
2. **资源占用过高**：PyBullet GUI 模式（xvfb）600MB/96% CPU → 改用 DIRECT 模式（273MB/15% CPU）
3. **容器依赖丢失**：容器重建后 pip 包消失 → 建议固化至 Dockerfile
4. **跨设备通信**：WSL2 NAT 隔离 → Tailscale 虚拟组网解决
