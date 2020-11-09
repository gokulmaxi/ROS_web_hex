#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import String
import time
import math

def callback(data):
	x=turtlesim()
	x.move()
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
class turtlesim:
	def __init__(self):
		self.velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.poseCallback)
		self.pose = Pose()
	def poseCallback(self,data):
		self.pose.theta=round(data.theta,2)
	def move(self):
		vel_msg=Twist()
		rate =rospy.Rate(1)
		for i in range(0,6,1):
			vel_msg.linear.x =0
			vel_msg.angular.z=1.0472/1
			self.velocity_publisher.publish(vel_msg)
			rate.sleep()
			vel_msg.linear.x=1
			vel_msg.angular.z=0
			self.velocity_publisher.publish(vel_msg)
			rate.sleep()
		vel_msg.linear.x=0
		vel_msg.linear.y=0
		vel_msg.angular.y=0
		vel_msg.angular.z=0
		self.velocity_publisher.publish(vel_msg)
		rospy.loginfo("completed")
		rate.sleep()
if __name__ == '__main__':
    try:
        #Testing our function
        listener()
    except rospy.ROSInterruptException: pass