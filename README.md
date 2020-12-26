# Object-detection
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


Camera Calibration:




Aruco marker detection:

This node finds aruco markers in images stream and publishes their vertices (corner points) and estimates 3D transforms from the camera to the fiducials.

Using https://github.com/UbiquityRobotics/fiducials/tree/kinetic-devel/aruco_detect repo, we have detected marker.

Made some changes in aruco_detect.launch file.




Test our trained model on raspberry pi4:

We have to install some dependancies for raspberry pi 4 and ubuntu 18.04
sudo apt-get update
$ sudo apt-get upgrade

# install the dependencies (if not already onboard)
$ sudo apt-get install python3-pip gfortran
$ sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev
$ sudo apt-get install libatlas-base-dev libopenblas-dev libblas-dev
$ sudo apt-get install liblapack-dev
$ sudo pip3 install pybind11
$ sudo pip3 install Cython==0.29.21









