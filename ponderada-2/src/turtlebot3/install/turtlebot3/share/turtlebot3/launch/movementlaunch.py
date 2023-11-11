from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    turtlebot3_navigation2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('turtlebot3_navigation2'), 'launch'), '/navigation2.launch.py']
        ),
        launch_arguments={'use_sim_time': 'True', 'map': 'my-map.yaml'}.items(),
    )
    turtlebot3_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch'), '/turtlebot3_world.launch.py'],
        )
    )

    turtlebot3_turtlebot3 = Node(
        package='turtlebot3',
        executable='turtlebot3',
        name='turtlebot3',
        output='screen'
    )

    return LaunchDescription([
        turtlebot3_gazebo,
        turtlebot3_navigation2,
        turtlebot3_turtlebot3
    ])