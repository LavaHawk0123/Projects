#!/usr/bin/env python

import rospy
import sys
import rosbag
import numpy
import math
import socket,traceback
from imutask.srv import *
from std_msgs.msg import Int32, String, Float32MultiArray

def IMU_client():
    host = '192.168.1.26'
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind((host, port))
    while True:
        try:
            message, address = s.recvfrom(1024)
	    message=message.replace(" ","")
	    message=message.split(",")
	    message=list(map(float,message))
            message=numpy.array(message)
	    acc_x=message[2]
	    acc_y=message[3]
	    acc_z=message[4]
	    mag_x=message[6]
	    mag_y=message[7]
	    mag_z=message[8]
	    rospy.wait_for_service('imu_to_quat')
	    try:
	        imus=rospy.ServiceProxy('imu_to_quat',imu)
		print("connected to server")
	        resp=imus(acc_x,acc_y,acc_z,mag_x,mag_y,mag_z)
	        print(resp.qw,resp.qx,resp.qy,resp.qz)
	    except rospy.ServiceException as e:
	        print("Server call failed ")
	    


        except (KeyboardInterrupt, SystemExit):
            raise
        
        except:
            traceback.print_exc()

if _name_ == "_main_":
    print("Sending data to the server")
    IMU_client()
