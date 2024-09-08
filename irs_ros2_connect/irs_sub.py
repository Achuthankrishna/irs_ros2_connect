#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import pyrealsense2 as rs
from cv_bridge import CvBridge
import cv2
import numpy as np

class IntelSubscriber(Node):
    def __init__(self):
        super().__init__("intel_subsribr")
        self.intel_subscriber_rgb = self.create_subscription(Image,"rgb_frame",self.rgb_callback,10)
        self.intel_subscriber_depth = self.create_subscription(Image,"depth_irs",self.depth_callback,10)
        self.intel_subscriber_fdepth = self.create_subscription(Image,"filtered_depth",self.fdepth_callback,10)

        
        timers=0.5
        self.brg=CvBridge()
    def rgb_callback(self,data):
        self.get_logger().info("Getting RGB Image")
        curr_frame = self.brg.imgmsg_to_cv2(data)
        cv2.imshow("RGB IMAGES",curr_frame)
        cv2.waitKey(1)
    def depth_callback(self,data):
        self.get_logger().info("Getting depth Image")
        curr_frame2 = self.brg.imgmsg_to_cv2(data)
        cv2.imshow("DEPTH IMAGES",curr_frame2)
        cv2.waitKey(1)
    def fdepth_callback(self,data):
        self.get_logger().info("Getting Filtered depth Image")
        curr_frame3 = self.brg.imgmsg_to_cv2(data)
        cv2.imshow("FILTERED DEPTH IMAGES",curr_frame3)
        cv2.waitKey(1)

def main(args =None):
    rclpy.init(args=args)
    irs_sub=IntelSubscriber()
    rclpy.spin(irs_sub)
    irs_sub.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()