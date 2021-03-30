#!/usr/bin/env python2


#Importing required Packages
import rospy
from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist, Point, Vector3
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from std_msgs.msg import Float64
import pyproj
import math
import numpy as np 
import time

#Class defined encapsulationg variables and functions nessecary for Traversal
class Traverse:

	#The init function executed every time the constructor/Class name is called in main:

	def __init__(self,x,y):
		self.goal_x = x
		self.goal_y = y
		self.speed = Twist()
		self.Flag =True
		self.sub_gps = rospy.Subscriber('/fix', NavSatFix, self.GPS) #Subscriber to the topic /fix
		print(self.goal_x,self.goal_y)
		R = rospy.Rate(1)
		R.sleep()
		self.sub = rospy.Subscriber('/imu', Imu, self.Angle)	     #Subscriber to the /imu topic
		self.pub = rospy.Publisher('/cmd_vel',Twist, queue_size = 1) #Publisher to /cmd_vel topic
		
	#Function to correct the angle and convert range from (-180,180) to (0,360):

	def Angle_correction(self,az,angle):
		if(az<0):
			az_angle = 360+az
		else:
			az_angle = az
		if(angle<0):
			angle_conv = 360+angle
		else:
			angle_conv = angle

		return az_angle,angle_conv

	#Function to find the shortest angle the rover has to rotate with the angle difference as the input parameter

	def Short_Angle(self,theta_i):
		if(theta_i<0):
			if(math.fabs(theta_i)>180):	#Case 1 : Large and Negative
				theta_corr = 360+theta_i
				self.fac = 1
			else:				#Case 2 : Small and negative
				theta_corr = theta_i
				self.fac = -1
		else:
			if(theta_i>180):		#Case 3 : Large and Positive
				theta_corr = 360-theta_i
				self.fac =-1
			else:				#Case 4 : Small and Positive
				theta_corr = theta_i
				self.fac =1
		return theta_corr

	#Callback Function of GPS Subscriber to obtain the latitude,longitude and altitude from the /fix topic's message and use Pyproj to calculate fwd azimuthal angle and distance:

	def GPS(self,req):
		self.latitude = req.latitude
		self.longitude = req.longitude
		self.altitude = req.altitude
		geodesic = pyproj.Geod(ellps='WGS84')
	    	self.fwd_angle,self.back_angle,self.dist = geodesic.inv(self.longitude,self.latitude,self.goal_y,self.goal_x)
		self.fwd_angle = -self.fwd_angle
	
	#Function that sets the linear velocity of the rover to 0.2 when it is aligned and at a distance greater than 0.2 m (Forward Traversal):

	def Straight(self):
		Distance = self.dist
		rospy.loginfo("Distance from goal: %lf",Distance)
		if(Distance>1):
			self.speed.linear.x=1
			self.pub.publish(self.speed)

		else:
			self.speed.linear.x=0
			self.pub.publish(self.speed)
			print("Traversal Complete")
			rospy.signal_shutdown("Traversal Complete") #Shuts the node down once Traversal is complete

	#Function to rotate the rover to the desired heading dynamically calculating angle difference and setting angular velocity (+/-) accordingly			

	def Turn(self):
		self.angle = math.degrees(self.yaw)
		#rospy.loginfo("Fwd Angle : %lf, yaw: %lf",self.fwd_angle,self.angle)
		fwd_net,angle_net = self.Angle_correction(self.fwd_angle,self.angle)
		#rospy.loginfo("IMU angle: %lf, Azimuth Angle: %lf",angle_net,fwd_net)
		theta_input = fwd_net-angle_net
		rospy.loginfo("corrected angle diff: %lf",theta_input)
		self.theta = self.Short_Angle(theta_input)
		rospy.loginfo("corrected shortest angle diff: %lf",self.theta)
		if(math.fabs((self.theta))>0.9):
			self.speed.angular.z=0.8*(self.fac)
			self.pub.publish(self.speed)
		else:
			self.speed.angular.z=0
			self.pub.publish(self.speed)
			print("Turning Complete")
			self.Flag = False

	#Callback function of the IMU Subscriber to Obtain the orientation of the rover in real time and execute turning or traversal:

	def Angle(self,msg):
		self.x = msg.orientation.x
		self.y = msg.orientation.y
		self.z = msg.orientation.z
		self.w = msg.orientation.w
		(self.roll, self.pitch, self.yaw) = euler_from_quaternion([self.x,self.y,self.z,self.w])
		if(self.Flag):
			self.Turn()
		else:
			print("Rover Aligned. Executing Traversal forward")
			self.Straight()
			
#Test Cases
#3rd Quadrent:
#latitude: 49.8999263921
#longitude: 8.89986112816

#4th Quadrent:
#latitude: 49.8999178634
#longitude: 8.90014491787

#1st Quadrent:
#latitude: 49.9000908658
#longitude: 8.90013613349

#2nd Quadrent:
#latitude: 49.9000910927
#longitude: 8.89987401299

	
#Main function iterated repeatedly using rospy.spin() 

if __name__ == '__main__':
    rospy.init_node('IMU')
    x = np.float64(input("Enter Latitude : "))	#Obtaining goal latitude from user
    y = np.float64(input("Enter Longitude : ")) #Obtaining goal longitude from user
    Traverse(x,y) 				#Constructor of the class called
    rospy.spin()
