# Realsense-Depthmap
[//]: <> (Get depth map using realsense D415 camera)
This repository contains code for obtaining depth maps using the Intel RealSense D415 camera in a ROS (Robot Operating System) environment.

**Prerequisites**

Before using this code, make sure you have the following installed:

1. ROS (Robot Operating System) - [Installation Guide](https://wiki.ros.org/Installation).
2. Intel RealSense SDK - [Installation Guide](https://www.intelrealsense.com/sdk-2/)
3. ROS Wrapper for Intel RealSense Cameras - [Installation Guide](https://github.com/IntelRealSense/realsense-ros)

**Setup**

1. Clone this repository to your ROS workspace:

   ```bash
   git clone https://github.com/MadushankaHP/Realsense-Depthmap.git
   
2. Build the ROS workspace:
   ```bash
   cd your_ros_workspace
   catkin_make
   source devel/setup.bash

**Usage**

Launch the RealSense D415 camera node:
   ```bash
   roslaunch depth_map depth.launch

After running the launch file, you can get the distance between the camera and the selected point by selecting the point with the mouse in the RGB window. As shown in the figure 1 below.


Additionally, a demo video is available [here](https://youtu.be/94TXj-BTWPE).

