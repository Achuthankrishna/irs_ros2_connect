#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import pyrealsense2 as rs
from cv_bridge import CvBridge
import cv2
import numpy as np
##### LEGACY CODE ######
# pipe= rs.pipeline()
# config=rs.config()

# config.enable_stream(rs.stream.color,640,480,rs.format.bgr8,20)
# config.enable_stream(rs.stream.depth,640,480,rs.format.mono16,20)

# pipe.start(config)

# while True:
#     #wait for frames
#     frames=pipe.wait_for_frames()
#     #get depth and rgb
#     depth_frame=frames.get_depth_frame()
#     color_frames=frames.get_color_frame()

class IntelPublisher(Node):
    def __init__(self):
        super().__init__("intel_publisher")
        self.intel_publisher_rgb = self.create_publisher(Image,"rgb_frame",10)
        self.intel_publisher_depth = self.create_publisher(Image,"depth_irs",10)
        
        timers=0.5
        self.brg=CvBridge()
        try:
            self.timer=self.create_timer(timers,self.timer_callback)
            
            
            self.pipe=rs.pipeline()
            self.config=rs.config()
            self.config.enable_stream(rs.stream.color,640,480,rs.format.bgr8,30)
            self.config.enable_stream(rs.stream.depth,640,480,rs.format.z16,30)
            self.pipe.start(self.config)
            # self.timer=self.create_timer(timers,self.timer_callback)
        
        except Exception as e:
            print(f"Exception caused due to {e}")
            self.get_logger().error("REALSENSE NOT CONNECTED")
    def timer_callback(self):
        fr=self.pipe.wait_for_frames()
        color_frame = fr.get_color_frame()
        depth_frame = fr.get_depth_frame()
        c_img = np.asanyarray(color_frame.get_data())
        d_img = np.asanyarray(depth_frame.get_data())
        self.intel_publisher_rgb.publish(self.brg.cv2_to_imgmsg(c_img))
        self.get_logger().info("RGB PUBLISHED")

 
def main(args=None):
    rclpy.init(args=None)
    ir_pub=IntelPublisher()
    rclpy.spin(ir_pub)
    ir_pub.destroy_node()
    
if __name__=="__main__":
    main()