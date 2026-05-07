📝 Week 10 实验汇报：Docker 深度应用与 OpenCV 视觉基础
1. 实验目标
深入理解 Docker 的核心概念（镜像、容器、仓库）。

掌握在 Ubuntu 环境下安装与配置 OpenCV 计算机视觉库。

编写基础脚本，验证 OpenCV 在图像处理中的基本功能。

2. 核心实验内容
🐳 2.1 Docker 核心概念与使用
Docker 通过将软件及其依赖打包，解决了“在我的电脑上能跑，在你的电脑上不行”的问题。

镜像 (Image)：软件运行环境的只读模板。

容器 (Container)：镜像运行后的实例，可以理解为一个轻量级的虚拟机。

常用指令：

Bash
docker ps          # 查看运行中的容器
docker stop [ID]   # 停止容器
docker rm [ID]     # 删除容器
📷 2.2 OpenCV 介绍与安装
OpenCV 是全球最流行的开源计算机视觉库，支持图像处理、特征检测和机器学习。

安装步骤（在 Ubuntu/Docker 中）：

Bash
sudo apt update
sudo apt install python3-opencv
功能验证：编写 Python 脚本读取并显示图像，转换为灰度图以验证库文件是否正常调用。

3. 实验截图展示
建议：这里放两张图。一张是 Docker 终端操作截图，一张是 OpenCV 处理图像的结果（比如原图 vs 灰度图）。

左图：Docker 镜像管理与容器启动过程。

右图：OpenCV 成功读取并处理机器狗/机械臂的仿真截图。

4. 关键代码片段 (OpenCV 验证)
Python
import cv2

# 读取图像
img = cv2.imread('robot_dog.jpg')

# 转换为灰度图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 保存结果
cv2.imwrite('robot_dog_gray.jpg', gray_img)
print("OpenCV 图像处理成功！")
5. 实验总结
本周通过对 Docker 的学习，我能够更高效地管理不同版本的 ROS 2 环境。同时，OpenCV 的引入为后续给机器狗添加“视觉感知”能力奠定了基础。在实验中我发现，在 Docker 容器内运行 OpenCV 窗口需要额外配置 X11 转发，这与第八周的 GUI 配置逻辑是一致的。