#! /usr/bin/env python3 
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from math import pi

def create_pose_stamped(navigator, pos_x, pos_y):
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, pi/4)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

def main():
    rclpy.init()
    nav = BasicNavigator()
    nav.waitUntilNav2Active()

    initial_pose = create_pose_stamped(nav, 0.0, 0.0)

    nav.setInitialPose(initial_pose)
    
    waypoints = [
    create_pose_stamped(nav, 2.5, 0.0),
    create_pose_stamped(nav, 2.0, 1.0),
    create_pose_stamped(nav, 0.0, 1.0),
    initial_pose
    ]

    nav.followWaypoints(waypoints)
    while not nav.isTaskComplete():
        print(nav.getFeedback())

    rclpy.shutdown()

if __name__ == "__main__":
    main()