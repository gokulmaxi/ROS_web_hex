#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    move()
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
def move():
    # Starts a new node
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")

    #Checking if the movement is forward or backwards

    vel_msg.linear.x = 5
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    
    #Setting the current time for distance calculus
    for i in range(6):
        velocity_publisher.publish(vel_msg)
        time.sleep(0.5)
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        time.sleep(0.5)
        vel_msg.angular.z=10
        velocity_publisher.publish(vel_msg)
        time.sleep(0.5)
        vel_msg.angular.z=0
        vel_msg.linear.x=5
        print(i)
            


if __name__ == '__main__':
    try:
        #Testing our function
        listener()
    except rospy.ROSInterruptException: pass