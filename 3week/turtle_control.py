#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
rclpy.init()
node = Node('turtle_control')
pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)
msg = Twist()
msg.linear.x = 2.0
msg.angular.z = 1.8
pub.publish(msg)
print("Velocity command sent")
node.destroy_node()
rclpy.shutdown()
