
Install ROS melodic in raspberry pi 4 with ubuntu 18.04 version.

Install all the dependencies of ROS melodic using help of ROS beginner tutorials(http://wiki.ros.org/ROS/Tutorials).

After understanding basics of ROS we have to install raspicam node in ROS to read camera image as an ROS topic.

Here is the link where we can install raspicam node:
https://github.com/ubiquityrobotics/raspicam_node

After running command rosdep update, run this command before catkin_make " rosdep install --from-paths src --ignore-src --rosdistro=melodic -y --skip-keys libraspberrypi0 ".

Some changes we have done here:

Download following repository:
https://github.com/raspberrypi/userland

Extract this repo and copy the interface folder into include directory of raspicam node. also add the vcinclude and bcm_host.h file into the include dir.

The purpose of the adding this file is bacause of we will get some error while running catkin_make.
