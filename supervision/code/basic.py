#!/usr/bin/env python
import cv2
import numpy as np
import sys
import rospy
import imutils


from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String
from geometry_msgs.msg import Point


rospy.init_node('opencv_example', anonymous=True)

# Print "Hello ROS!" to the Terminal and to a ROS Log file located in ~/.ros/log/loghash/*.log
rospy.loginfo("Hello ROS!")

bridge = CvBridge()

def show_image(img):
    cv2.imshow("Image", img)
    cv2.waitKey(3)

def image_callback(img_msg):
    # log some info about the image topic
    #rospy.loginfo(img_msg.header)

    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    

        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        edged = cv2.Canny(blurred, 50, 150)
	# find contours in the edge map
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

		# loop over the contours
        for c in cnts:
		# approximate the contour
	        peri = cv2.arcLength(c, True)
	        approx = cv2.approxPolyDP(c, 0.01 * peri, True)
		# ensure that the approximated contour is "roughly" rectangular
	        if len(approx) >= 4 and len(approx) <= 6:
			# compute the bounding box of the approximated contour and
			# use the bounding box to compute the aspect ratio
			        (x, y, w, h) = cv2.boundingRect(approx)
			        aspectRatio = w / float(h)
			# compute the solidity of the original contour
			        area = cv2.contourArea(c)
			        hullArea = cv2.contourArea(cv2.convexHull(c))
			        solidity = area / float(hullArea)
			# compute whether or not the width and height, solidity, and
			# aspect ratio of the contour falls within appropriate bounds
			        keepDims = w > 25 and h > 25
			        keepSolidity = solidity > 0.9
			        keepAspectRatio = aspectRatio >= 0.8 and aspectRatio <= 1.2
			# ensure that the contour passes all our tests
			        if keepDims and keepSolidity and keepAspectRatio:
				# draw an outline around the target and update the status
				# text
				        cv2.drawContours(cv_image, [approx], -1, (0, 0, 255), 4)
				        status = "Target(s) Acquired"
				# compute the center of the contour region and draw the
				# crosshairs
				        M = cv2.moments(approx)
				        (cX, cY) = (int(M["m10"] // M["m00"]), int(M["m01"] // M["m00"]))
				        (startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
				        (startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
				        cv2.line(cv_image, (startX, cY), (endX, cY), (0, 0, 255), 3)
				        cv2.line(cv_image, (cX, startY), (cX, endY), (0, 0, 255), 3)
			# draw the status text on the frame
				        cv2.putText(cv_image, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                             (0, 0, 255), 2)

    except CvBridgeError as e:
        print(e)
    
    show_image(cv_image)
  


sub_image = rospy.Subscriber("/raspicam_node/image", Image, image_callback)


cv2.namedWindow("Image", 1)

# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
    rospy.spin()