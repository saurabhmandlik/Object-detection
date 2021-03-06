### Installation guide for ubuntu OS and ROS:

Here, I have installed ROS melodic in raspberry pi 4 with ubuntu 18.04 version.

Install all the dependencies of ROS melodic using help of ROS beginner tutorials

    (http://wiki.ros.org/ROS/Tutorials)

After understanding basics of ROS we have to install raspicam node in ROS to read camera image as an ROS topic.

Here is the link where we can install raspicam node:

    https://github.com/ubiquityrobotics/raspicam_node

After running command rosdep update, run this command before catkin_make  

    rosdep install --from-paths src --ignore-src --rosdistro=melodic -y --skip-keys libraspberrypi0.

#### Some changes we have done here:

Download following repository:
            
    https://github.com/raspberrypi/userland

Extract this repository and copy the interface folder into include directory of raspicam node. also add the vcinclude and bcm_host.h file into the include dir.

The purpose of adding this file is bacause of we will get some error while running catkin_make.


#### Test our trained model(On windows OS) on raspberry pi4:

We have to install some dependancies for raspberry pi 4 and ubuntu 18.04 

    sudo apt-get update

    sudo apt-get upgrade

#### Install the dependencies (if not already onboard)

    sudo apt-get install python3-pip gfortran

    sudo apt-get install libhdf5-dev libc-ares-dev libeigen3-dev

    sudo apt-get install libatlas-base-dev libopenblas-dev libblas-dev

    sudo apt-get install liblapack-dev

    sudo pip3 install pybind11

    sudo pip3 install Cython==0.29.21

    sudo pip3 install h5py

    sudo pip3 install --upgrade setuptools

Install gdown to download from Google drive
    pip3 install gdown

copy binary
    
    sudo cp /home/ubuntu/.local/bin/gdown /usr/local/bin/gdown

download the wheel

    gdown https://drive.google.com/uc?id=1X2mhbsG1p_RK_rKJrLCwh3cEA0Kwv6Zr

#### Install TensorFlow
    
    sudo -H pip3 install tensorflow-2.4.0-cp36-cp36m-linux_aarch64.whl

#### Install OpenCV (if it is not present in the system)
    
    sudo pip3 install opencv-python
