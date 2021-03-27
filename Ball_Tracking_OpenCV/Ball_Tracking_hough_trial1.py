from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())
#Upper = (117,255,255) #Green-Studio
#Lower = (41,103,140) #Green-Studio
Lower = (0, 153, 209) #-- Orange-Studio
Upper = (255, 255, 255) #-- Orange-Studio
#Lower = (164, 196, 91) #-- Orange-Sun
#Upper = (255, 255, 255) #-- Orange-Sun
#Lower = (0, 38, 255) #-- Orange-Torch
#Upper = (255, 255, 255) #-- Orange-Torch
#Lower = (0, 164, 80) #-- Orange-mean
#Upper = (185, 255, 255) #-- Orange-mean
pts = deque(maxlen=args["buffer"])
vs = VideoStream(src=0).start()
time.sleep(2.0)
while True:
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
	if frame is None:
		break
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, Lower, Upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	result = cv2.bitwise_and(frame, frame, mask = mask)
	gray_mask = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
	circles = cv2.HoughCircles(gray_mask, cv2.HOUGH_GRADIENT, 1.35, 30, param1 = 55, param2 = 38, minRadius = 15, maxRadius = 100)
	if circles is not None:
	 circles_present = np.uint64(np.around(circles))
	 #print(circles_present)
	 #time.sleep(5)
	 for (x, y, radius) in circles_present[0, :] :
	 x= circles_present[0,0:0]
	 y=circles_present[0,1:1]
	 radius=circles_present[0,2:2]
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
