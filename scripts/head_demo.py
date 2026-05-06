#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class ICubHeadDemo(Node):
    def __init__(self):
        super().__init__('icub_head_demo')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.angle = 0.0

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['neck_pitch', 'neck_yaw']
        self.angle += 0.05
        msg.position = [0.2 * math.sin(self.angle), 0.5 * math.cos(self.angle)]
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(ICubHeadDemo())
    rclpy.shutdown()
