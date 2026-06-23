#!/bin/bash
sudo apt update && sudo apt install -y ros-humble-desktop
echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
