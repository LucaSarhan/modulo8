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
    turtlebot3_cartographer_dir = get_package_share_directory('turtlebot3_cartographer')
    
    # Command 1: Launch the turtlebot3_world
    turtlebot3_world_launch_file = os.path.join(turtlebot3_gazebo_dir, 'launch', 'turtlebot3_world.launch.py')
    turtlebot3_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(turtlebot3_world_launch_file),
    )
    # Command 2: Run the turtlebot3_teleop node for keyboard teleoperation
    turtlebot3_teleop_node = Node(
        package='turtlebot3_teleop',
        executable='teleop_keyboard',
        name='turtlebot3_teleop_keyboard',
        prefix = 'gnome-terminal --',
        output='screen'
    )
    # Command 3: Launch the turtlebot3_cartographer with use_sim_time parameter
    cartographer_launch_file = os.path.join(turtlebot3_cartographer_dir, 'launch', 'cartographer.launch.py')
    turtlebot3_cartographer_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(cartographer_launch_file),
        launch_arguments={'use_sim_time': 'True'}.items()
    )
    # Create the launch description and populate
    ld = LaunchDescription()
    # Add the actions to the launch description
    ld.add_action(turtlebot3_world_launch)
    ld.add_action(turtlebot3_teleop_node)
    ld.add_action(turtlebot3_cartographer_launch)
    return ld