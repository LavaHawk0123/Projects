# The following code is written for an orange ball whose image is attached in the github folder.
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
#Lower = (0, 153, 209) #-- Orange-Studio
#Upper = (255, 255, 255) #-- Orange-Studio
#Lower = (164, 196, 91) #-- Orange-Sun
#Upper = (255, 255, 255) #-- Orange-Sun
#Lower = (0, 38, 255) #-- Orange-Torch
#Upper = (255, 255, 255) #-- Orange-Torch
Lower = (0, 164, 80) #-- Orange-mean
Upper = (185, 255, 255) #-- Orange-mean
pts = deque(maxlen=args["buffer"])
vs = VideoStream(src=0).start()
time.sleep(3.0)
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
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		if M["m00"] !=0:
			Cx = int(M["m10"] / M["m00"])
			Cy = int(M["m01"] / M["m00"])
		else:
			Cx,Cy = 0,0
		center = (Cx,Cy)
		if radius > 1:
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0,255,0), 4)
			cv2.circle(frame, center, 5, (255,150,100), -1)
	pts.appendleft(center)
	cv2.imshow("Ball-Tracking", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cv2.destroyAllWindows()
