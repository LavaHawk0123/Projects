#!/usr/bin/env python

    
from imutask.srv import *
import rospy
import math
import numpy as np
    
def quaternions(req):
    PI=3.141593
    pitch = 57.3 * math.atan (req.acc_x/math.sqrt(req.acc_y*req.acc_y + req.acc_z*req.acc_z))
    roll = 57.3 * math.atan (req.acc_y/math.sqrt(req.acc_x*req.acc_x + req.acc_z*req.acc_z))

    Yh = (req.mag_y * math.cos(roll)) - (req.mag_z * math.sin(roll))
    Xh = (req.mag_x * math.cos(pitch))+(req.mag_y * math.sin(roll)*math.sin(pitch)) + (req.mag_z * math.cos(roll) * math.sin(pitch))

    yaw=57.3* math.atan(Yh,Xh)

    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

    return imuResponse(qw,qx,qy,qz)
   
def imu_data():
    rospy.init_node('imu_to_quat_server')
    s = rospy.Service('imu_to_quat', imu, quaternions)
    rospy.spin()
   
if _name_ == "_main_":
     imu_data()
