
## Indoor non-GPS Autonomous Navigation of UAV using AprilTag Marker 

This repository explains the autonomous navigation and position of drone in indoor environment. Here, I have used Intel RealSense camera to navigate the UAV using AprilTag marker. 

### Required Set-up

#### Software and Dependencies to be needed

    1. Ubuntu 18.04
    2. ROS Melodic
    3. Mission Planner
    4. RViz
    5. vision_to_mavros ROS packages
    6. TensorFlow 
    7. Python 2.7
    
    
#### Hardware used

    1. Raspberry Pi 4
    2. Intel RealSense Camera
    3. Raspberry Pi camera V2.0
    4. UAV
    5. PixHawk 4
    6. RC transmitter
    

##### The repository is divided into two parts:
    1. Detect the predetermined object using computer vision approach
    2. Autonomously navigate UAV using marker
    

#### 2. Autonomously Navigate the UAV using AprilTag marker:

Few things we have to understand to get into this topic.

#### A. MAVROS (http://wiki.ros.org/mavros)
MAVROS is a ROS package that enables MAVLink extendable communication between computers runnig ROS for any ground station. It's officially bridge between ROS and ArduPilot by translating ROS topics into MAVLink messages.

###### Features of MAVROS

    -Communication with autopilot via serial port, UDP or TCP (e.g. PX4 Pro or ArduPilot)
    -Plugin system for ROS-MAVLink translation
    -Parameter manipulation tool
    -Waypoint manipulation tool
    -PX4Flow support (by mavros_extras)
    -OFFBOARD mode support
    -Geographic coordinates conversions.

##### MAVROS Installation













    . 





