# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())
# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
#Upper = (117,255,255) #Green-Studio
#Lower = (41,103,140) #Green-Studio
#Lower = (0, 153, 209) #-- Orange-Studio
#Upper = (255, 255, 255) #-- Orange-Studio
#Lower = (164, 196, 91) #-- Orange-Sun
#Upper = (255, 255, 255) #-- Orange-Sun
#Lower = (0, 38, 255) #-- Orange-Torch
#Upper = (255, 255, 255) #-- Orange-Torch
Lower = (0, 164, 80) #-- Orange-mean
Upper = (185, 255, 255) #-- Orange-mean
pts = deque(maxlen=args["buffer"])
# if a video path was not supplied, grab the reference
# to the webcam
vs = VideoStream(src=0).start()
# otherwise, grab a reference to the video file
# allow the camera or video file to warm up
time.sleep(2.0)
# keep looping
while True:
	# grab the current frame
	frame = vs.read()
	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, Lower, Upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	 circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.157, 20, param1 = 50, param2 = 33, minRadius = 0, maxRadius = 100)
	if circles is not None:
		circles_present = np.uint64(np.around(circles))
		for (x, y, radius) in circles_present[0, :] :
		cv2.circle(frame, (int(x), int(y)), int(radius),(0,255,0), 4)
		center = (x,y)
		cv2.circle(frame, center, 5, (255,150,100), -1)
		cv2.putText(frame, 'Tennis Ball', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
	cv2.imshow("Ball-Tracking", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# close all windows
cv2.destroyAllWindows()
