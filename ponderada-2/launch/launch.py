from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="turtlebot3_gazebo",
            executable="turtlebot3_world.launch.py",
            output="screen",
        ),
        Node(
            package="turtlebot3_teleop",
            executable="teleop_keyboard",
            output="screen",
        ),
        Node(
            package="turtlebot3_cartographer",
            executable="cartographer.launch.py",
            output="screen",
            parameters=[
                {"use_sim_time": True},
            ]
        ),
    ])
