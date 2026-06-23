import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Paths to dependencies and files
    room_simulator_share = get_package_share_directory('room_simulator')
    turtlebot3_desc_share = get_package_share_directory('turtlebot3_description')
    ros_gz_sim_share = get_package_share_directory('ros_gz_sim')

    # Path to your custom world file inside the source/install tree
    # (Using the absolute path to your source folder for convenience during development)
    world_file_path = os.path.expanduser('~/Projects/orangewood-training/amr/src/room_simulator/worlds/room_world.sdf')
    
    # Path to the specific TurtleBot3 model URDF (burger, waffle, etc.)
    urdf_file_path = os.path.join(turtlebot3_desc_share, 'urdf', 'turtlebot3_burger.urdf')

    # Read the URDF content to feed into Robot State Publisher
    with open(urdf_file_path, 'r') as infp:
        robot_description_content = infp.read()

    # 2. Launch Gazebo with your custom world
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_share, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'-r {world_file_path}'}.items()
    )

    # 3. Robot State Publisher (Broadcasts the robot transforms / tf)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content, 'use_sim_time': True}]
    )

    # 4. Spawner Node (Injects the URDF into the Gazebo world)
    robot_spawner = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=[
            '-name', 'turtlebot3_burger',
            '-topic', 'robot_description',
            '-x', '0.0', # Change spawn coordinates here
            '-y', '0.0',
            '-z', '0.1'
        ]
    )

    return LaunchDescription([
        gazebo_launch,
        robot_state_publisher,
        robot_spawner
    ])
