#!/usr/bin/env python

import rospy
from turtlesimtask.srv import *
import math

def move_circle_client():
    rospy.wait_for_service('move_circle')
    try:
        radius = float(input("Enter Radius (0 - 2.5) : "))
        speed = float(input("Enter Speed : "))
        move_circle = rospy.ServiceProxy('move_circle', MoveCircle)
        print("connecting with server")
        move_circle(speed,radius)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print("Moving turtle in a circle")
    move_circle_client()
