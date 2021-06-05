
# Indoor non-GPS Autonomous Navigation of UAV using AprilTag Marker 

This repository explains the autonomous navigation and position of drone in indoor environment. Here, I have used Intel RealSense camera to navigate the UAV using AprilTag marker. 

### Required Set-up

#### Software and Dependencies to be needed

    1. Ubuntu 18.04
    2. ROS Melodic
    3. Mission Planner
    4. RViz
    5. vision_to_mavros ROS packages and AprilTag marker
    6. TensorFlow 
    7. Python 2.7
    
    
#### Hardware used

    1. Raspberry Pi 4
    2. Intel RealSense Camera
    3. Raspberry Pi camera V2.0
    4. UAV
    5. PixHawk 4
    6. RC transmitter
    7. 4500 mAh LiPo Battery
    8. StromPi and Battery module
    

#### The repository is divided into two parts:
    1. Detect the predetermined object using computer vision approach
    2. Autonomously navigate UAV using marker
    

### 2. Autonomously Navigate the UAV using AprilTag marker:

Few things we have to understand to get into this topic.

#### MAVROS  (http://wiki.ros.org/mavros)
MAVROS is a ROS package that enables MAVLink extendable communication between computers runnig ROS for any ground station. It's officially bridge between ROS and ArduPilot by translating ROS topics into MAVLink messages.

##### Features of MAVROS

    -Communication with autopilot via serial port, UDP or TCP (e.g. PX4 Pro or ArduPilot)
    -Plugin system for ROS-MAVLink translation
    -Parameter manipulation tool
    -Waypoint manipulation tool
    -PX4Flow support (by mavros_extras)
    -OFFBOARD mode support
    -Geographic coordinates conversions.

##### MAVROS Installation

    sudo apt-get install python-catkin-tools python-rosinstall-generator -y
     
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws
    catkin init
    wstool init src


    rosinstall_generator --rosdistro melodic mavlink | tee /tmp/mavros.rosinstall

    rosinstall_generator --upstream mavros | tee -a /tmp/mavros.rosinstall

    wstool merge -t src /tmp/mavros.rosinstall
    wstool update -t src -j4
    rosdep install --from-paths src --ignore-src -y

    ./src/mavros/mavros/scripts/install_geographiclib_datasets.sh
    
    catkin build
    source devel/setup.bash
    
#### Pixhawk FCU
Pixhawk is a flight controller unit that is used for many applications of multicopters, rovers etc.  It offers a wide variety of flight modes from fully manual to fully autonomous. As part of the wider ArduPilot software platform it works seamlessly with a variety of Ground Control Station programs that are used to setup the vehicle, monitor the vehicle’s flight in real-time and perform powerful mission planning activities.
For this project, I have used Pixhawk 4 FCU.

![image](https://user-images.githubusercontent.com/67440191/120722181-a1fe3d00-c4cf-11eb-9db3-75c651216857.png)



## Overall Setup to Fly the UAV

### Hardware Setup
    -Connect Pixhawk FCU to LiPo battery. 
    -Connect FCU to on board computer raspberry pi through USB Port of FCU. 
    -Connect realsense camera to raspberry pi 4.
    -Connect telemetry radio cable to PC. (Baud rate=57600)
    
    
Before doing this, check the following parameters in Mission Planner Software: (Information regarding mission planner software and mandatory hardware configuration steps can available in Thesis Work -> Mission Planner directory)
 
    AHRS_EKF_TYPE = 2
    BRD_RTC_TYPES = 2
    EK2_ENABLE = 1
    EK3_ENABLE = 0
    EK2_GPS_TYPE = 3
    EK2_POSNE_M_NSE = 0.1
    EK2_VELD_M_NSE = 0.1
    EK2_VELNE_M_NSE = 0.1
    GPS_TYPE = 0
    COMPASS_USE = 0
    COMPASS_USE2 = 0
    COMPASS_USE3 = 0
    SERIAL5_BAUD = 921 (the serial port used to connect to Raspberry Pi)
    SERIAL5_PROTOCOL = 1
    SYSID_MYGCS = 1 (to accept control from mavros)
    VISO_TYPE = 0


## Ground test

Go to misssion planner software and click on the connect button (upper right part of the window) with having baudrate 57600.

### Steps to do on Linux Platform

We have to run three main nodes at the same time on 3 seperated terminal of RPi.

    1. RealSense camera node:
    - roslaunch rs_continous.launch
    
    2. MAVROS node
    - roslaunch px4.launch fcu_url:ttyACM0:57600
    
    3. vision_to_mavros node:
    - roslaunch vision_to_mavros tf_to_mavros_rs.launch

on another terminal of RPi, run command "mavros echo /mavros/vision_pose/pose" to see the pose data from the vehicles (UAV).

and also run the "mavros echo /tf" to see the camera pose in Apriltag frame with Z-axis pointing downwards. /tf is basically transforms the pose of source_frame_id and target_frame_id which is defined in tf_to_mavros_rs.launch file.  

The information regarding tf, vision_pose topic is available in "Thesis work-> vision_to_mavros" directory.


## Check On Mission Planner Software

After running the all the nodes (realsense camera node, mavros node, vision_to_mavros node), move to mission planner software and connect the battery. 

I already mentioned above how to connect FCU to MP. After connecting to MP, You can see the pop-up screen on MP window that shows getting parameters. 

Then you have to set the EKF home position. It's shows the vehicle position in the world. For that, I have a script set_origin.py where I have set SET_GPS_GLOBAL_origin and SET_HOME_POSITION MAVLink messages. Run this scropt on terminal by command "rosrun vision_to_mavros set_origin.py". Script available in visio_to_mavros -> scripts directory. 

