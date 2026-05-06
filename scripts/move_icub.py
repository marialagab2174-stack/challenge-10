#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class IcubMover(Node):
    def __init__(self):
        super().__init__('icub_mover')
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.t = 0.0

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        # On fait bouger le torse et le cou
        msg.name = ['torso_pitch', 'neck_pitch', 'l_shoulder_pitch', 'r_shoulder_pitch']
        val = math.sin(self.t)
        msg.position = [val * 0.2, val * 0.3, val * 0.5, val * 0.5]
        self.pub.publish(msg)
        self.t += 0.1

def main():
    rclpy.init()
    rclpy.spin(IcubMover())
    rclpy.shutdown()
