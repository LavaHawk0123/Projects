#!/usr/bin/env python

import rospy
from turtlesimtask.srv import *
from geometry_msgs.msg import Twist
import math

PI = 3.1415926535897


def handle_move_circle(x):
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	data = Twist()
	speed = x.s
	radius = x.r
	rate = rospy.Rate(10)
        
	print("Reconnecting to client")


	data.linear.x = speed
	data.linear.y = 0
	data.linear.z = 0
	data.angular.x = 0
	data.angular.y = 0
	data.angular.z = speed/radius
	ang_vel = data.angular.z
	
	#Move Robot in circle
        circumference=math.pi*(2*(speed/ang_vel))
        t0= rospy.Time.now().to_sec()
        distance_traversed=0
        while(distance_traversed < circumference):
         pub.publish(data) 
         t= rospy.Time.now().to_sec()
         distance_traversed=speed*(t-t0)
         if(distance_traversed > circumference):
	  break
  
        rospy.loginfo("Linear Velocity = %f: Angular Velocity = %f",speed,ang_vel)

       
        pub.publish(data)
        rate.sleep()

def move_circle_server():
	rospy.init_node('move_circle_server')
	s = rospy.Service( 'move_circle', MoveCircle, handle_move_circle )
	rospy.spin()

if __name__ == "__main__":
	move_circle_server()

