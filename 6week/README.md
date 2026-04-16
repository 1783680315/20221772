# 📝 第07周实验汇报：ROS 2 KITTI数据发布与RViz2可视化
## 1.实验目标
学习如何在ROS 2环境下解析并发布KITTI自动驾驶数据集。

掌握利用RViz2实时显示点云数据（PointCloud2）、图像（Image）和坐标系（TF）。

理解自动驾驶传感器数据流在 ROS 2 中的传送机制。

## 2.核心任务说明
数据读取：编写或运行Python节点，读取KITTI数据集中的.bin点云文件和图像。

话题发布：将原始数据封装成ROS 2标准消息格式（如sensor_msgs/msg/PointCloud2），并发布到指定主题。

RViz2配置：

添加全局选项中的Fixed Frame（通常设置velo_link或map）。

添加PointCloud2插件以显示3D环境。

添加Image插件以查看货车摄像头视角。

## 3.实验截图展示
![图片描述](/home/dan/20221772/6week/Screenshot from 2026-04-09 11-29-50.png)

图标说明：上图展示了RViz2成功加载KITTI场景。通过点云数据可以看到车辆周围的街道和障碍物。

## 4. 关键运行命令
巴什
### 1. 启动 KITTI 数据发布节点
ros2 run kitti_publishers kitti_publisher_node

### 2. 启动 RViz2
rviz2

### 3. 查看当前发布的话题
ros2 topic list
## 5.实验总结
通过这周的实验，我深刻理解了TF坐标转换在自动驾驶中的重要性（例如雷达到相机的坐标转换）。相比前几周的仿真，KITTI的真实场景更加复杂，这就要求我在RViz2中更准确地配置渲染参数，保证以点云显示的坐标。