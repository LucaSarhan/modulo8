from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the package directories
    turtlebot3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    turtlebot3_navigation2_dir = get_package_share_directory('turtlebot3_navigation2')
    print(turtlebot3_navigation2_dir)
    
    # Command 1: Launch the turtlebot3_world
    turtlebot3_world_launch_file = os.path.join(turtlebot3_gazebo_dir, 'launch', 'turtlebot3_world.launch.py')
    turtlebot3_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(turtlebot3_world_launch_file),
    )

    # Command 2: Run the tartabot node
    #pond2_tartabot_node = Node(
    #    package='pond2',
    #   executable='tartabot',
    #   name='tartabot',
    #    output='screen'
    #)
    
    # Command 3: Launch the turtlebot3_cartographer with use_sim_time parameter
    navigation2_launch_file = os.path.join(turtlebot3_navigation2_dir, 'launch', 'navigation2.launch.py')
    print(navigation2_launch_file)
    navigation2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(navigation2_launch_file),
        launch_arguments={'use_sim_time': 'True', 'map': 'my-map.yaml'}.items()
    )
    # Create the launch description and populate
    ld = LaunchDescription()
    # Add the actions to the launch description
    ld.add_action(turtlebot3_world_launch)
    #ld.add_action(pond2_tartabot_node)
    ld.add_action(navigation2_launch)
    return ld