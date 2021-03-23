-A collection of ROS and non-ROS (Python, cpp) code that converts data from vision-based system (external localization system like fiducial tags, VIO, SLAM, or depth image) to corresponding MAVROS topics or MAVLink messages that can be consumed by a flight control stack to support precise localization and navigation tasks.

-Download the following github repo which will listen to the output of AprilTag (tags’ pose in the camera frame), perform necessary transformations, then publish the body pose to a topic that can be remapped to /mavros/vision_pose/pose.

https://discuss.ardupilot.org/t/indoor-non-gps-flight-using-apriltags-ros-based/42878
