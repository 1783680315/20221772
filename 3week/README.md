# 📝 第03周实验汇报：开发环境搭建与ROS2基础
## 1.实验目标
配置GitHub SSH密钥，实现Ubuntu命令行下的无密码代码。

连接 VS Code 与 WSL：Ubuntu 环境，提升开发效率。

运行ROS2小海龟(Turtlesim)节点，练习命令行控制。

## 2.核心实验内容
### 🔑 2.1 GitHub SSH 密钥配置
在Ubuntu终端中生成并配置SSH密钥，确保与GitHub的安全交互：



### 💻 2.2 VS Code 与 WSL 交互
安装WSL扩展插件，在Windows下直接编辑Ubuntu里面的代码文件实现。

通过 VS Code 终端直接运行 ROS2 节点，实现“代码编写-编译-调试”的功能。

### 🐢 2.3 小海龟（Turtlesim）交互实验
启动ROS2核心节点进行命令行交易：

启动仿真：ros2 run turtlesim turtlesim_node

键盘控制：ros2 run turtlesim turtle_teleop_key

话题监控：使用ros2 topic list查看/turtle1/cmd_vel。

## 3.实验截图展示
![图片描述1](/home/dan/20221772/xiaowugui2.png)
## 4.实验总结
通过本周的实验，我打通了从底层环境（SSH/WSL）到上层应用（ROS2）的开发队列。使用top发现，小海龟仿真节点监控虽然量轻，但在高层发送控制指令时，系统的上下文切换会有所增加。