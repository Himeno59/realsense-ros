#!/usr/bin/env python  
# -*- coding: utf-8 -*-
import roslib
import rospy
from visualization_msgs.msg import Marker
from nav_msgs.msg import Odometry

rospy.init_node('rs_t265_confidence_viewer')

marker_pub = rospy.Publisher("rs_t265_confidence_marker", Marker, queue_size = 1)

def callback(msg):
    marker = Marker()
    marker.header = msg.header;
    marker.header.frame_id = "~odom_ground_frame"
    marker.id = 0
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.lifetime = rospy.Duration();
    marker.scale.x = 0.1
    marker.scale.y = 0.1
    marker.scale.z = 0.1
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0
    marker.pose.orientation.y = 0
    marker.pose.orientation.z = 0
    marker.pose.orientation.w = 1
    if msg.pose.covariance[0] > 0.5:
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
    elif msg.pose.covariance[0] > 0.05:
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
    else:
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
    marker.color.a = 1.0
    marker_pub.publish(marker)


sub = rospy.Subscriber("~input", Odometry, callback)
rospy.spin()
