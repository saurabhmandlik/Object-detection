



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

$ sudo pip3 install h5py

$ sudo pip3 install --upgrade setuptools

# install gdown to download from Google drive

$ pip3 install gdown

# copy binairy

$ sudo cp /home/ubuntu/.local/bin/gdown /usr/local/bin/gdown

# download the wheel

$ gdown https://drive.google.com/uc?id=1X2mhbsG1p_RK_rKJrLCwh3cEA0Kwv6Zr

# install TensorFlow 

$ sudo -H pip3 install tensorflow-2.4.0-cp36-cp36m-linux_aarch64.whl

# Install OpenCV (if it is not present in the system)

sudo pip3 install opencv-python







