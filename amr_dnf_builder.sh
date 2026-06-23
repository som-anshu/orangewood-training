# 1. Source the core ROS 2 Jazzy installation
source /opt/ros/jazzy/setup.bash

# 2. Go to your workspace root
cd ~/Projects/orangewood-training/amr

# 3. Build the newly created room_simulator package to register it
colcon build --symlink-install

# 4. Source your local workspace overlay
source install/setup.bash