# Week 11 — Docker 进阶与 GitHub Pages 部署

## 实验目标

掌握 Docker 容器的高级操作，包括镜像提交、容器管理和环境固化，并将实验成果部署为 GitHub Pages 静态网页。

## 实验环境

| 组件 | 说明 |
|------|------|
| 容器引擎 | Docker |
| 版本管理 | Git |
| 部署平台 | GitHub Pages |

## 实验步骤

1. 在 Docker 容器中配置 ROS2 + OpenCV + PyBullet 环境
2. 将配置好的容器提交为新镜像
3. 验证镜像可复现性
4. 配置 GitHub Pages 部署实验页面

## 关键命令

```bash
docker commit -m "install pybullet and opencv" container_id my-ros2-full:v1.0
docker images
docker ps
```

## 遇到的问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 容器提交后镜像过大 | 包含了不必要的缓存文件 | 清理 apt 缓存和 pip 缓存后再提交 |
| GitHub Pages 构建失败 | 配置文件格式错误 | 检查 _config.yml 缩进和主题名称 |
| 推送时权限被拒 | Token 过期或权限不足 | 重新生成 GitHub Token 并更新凭证 |

## 总结与反思

Docker 的镜像提交功能让开发环境可以"一次配置，到处运行"，结合 GitHub Pages 的自动部署，实现了从实验到展示的完整闭环。

[← 返回首页](../)

## 延伸思考

Docker 容器化技术让开发环境的迁移成本降到了最低。结合 GitHub Pages，实验成果不仅能本地运行，还能通过网页向他人展示，形成从开发到展示的完整工作流。
