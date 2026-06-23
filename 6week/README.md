# 📝 Week 6：ROS2 动作（Actions）与机器人逻辑集成
实验内容
本周完成了以下任务：

ROS2 Actions 深度解析：理解了 Action 与 Topic/Service 的区别，掌握了其“可抢占、有反馈、适合长时间任务”的特性。

Action 服务器与客户端实现：编写 Python 代码实现 Action Server 和 Client，处理目标（Goal）、反馈（Feedback）和结果（Result）。

机器人复杂行为控制：通过 Action 机制控制机器人执行需要时间累积的任务，如“旋转 360 度”或“移动到指定坐标”。

自定义通信接口：学习如何定义 .action 文件，并编译生成对应的 Python 通信接口。

实验截图

<img src="img/zidongjiashi.png" width="800" alt="KITTI RViz2 可视化">

*KITTI 数据集在 RViz2 中成功渲染，点云和图像同步显示*

<img src="img/zidongjiashi.png" width="800" alt="避障流程图">

*基于传感器数据的避障决策流程*

<img src="img/zidongjiashi.png" width="800" alt="避障运行">

*避障逻辑在仿真环境中运行验证*

<img src="img/zidongjiashi.png" width="800" alt="KITTI 数据发布">

*KITTI 数据发布节点运行状态*

Action 反馈机制调试
机器人执行长时间序列任务
运行命令
Bash
# 查看系统中的 action 列表
ros2 action list

# 模拟发送一个 action 目标并查看反馈
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}" --feedback

# 编译包含自定义 action 的包
colcon build --packages-select my_robot_interfaces
遇到的问题
问题：在 Action 客户端发送目标后，程序处于阻塞状态，无法处理其他逻辑。
解决：使用了异步调用方法 send_goal_async()，并通过回调函数（Callback）来处理结果，实现了非阻塞式控制。

问题：Action Server 启动时提示接口类型不匹配。
解决：检查了 .action 文件的定义顺序（Goal, Result, Feedback 需用 --- 分隔），并确保在 package.xml 中添加了相应的依赖。

学习心得
本周的学习让我对 ROS2 的通信模型有了完整的认识。相比于 Topic 的即时发布和 Service 的同步等待，Action 提供的“进度条”式反馈（Feedback）对提升用户体验和系统稳定性至关重要。例如在控制机械臂抓取或小车长距离导航时，Action 允许我们在任务进行中随时获取进度，甚至中途取消，这才是实现智能机器人复杂逻辑的正确方式。

返回
← 返回首页
## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| RViz2 无点云显示 | Fixed Frame 设置错误 | 设置为 velodyne 或对应传感器帧 |
| 话题发布频率过低 | 数据量大导致处理延迟 | 减小数据量或使用 --rate 参数优化 |

## 总结与反思

KITTI 数据集与 ROS2 可视化工具的结合，为自动驾驶感知算法的开发和验证提供了标准化的数据接口。

[← 返回首页](../)
