#!/usr/bin/env python

import rospy
from speed_test_jetbot.msg import speed_cmd

def controller():
	rospy.init_node('speed_controller' , anonymous=True)
	pub_cmd = rospy.Publisher('speed_command', speed_cmd, queue_size=10)
	r = rospy.Rate(10)
	msg = speed_cmd()
	msg.left_speed = 20
	msg.right_speed = 20

	while not rospy.is_shutdown():
		#Print to the Terminal and ROS Log file: ~/.ros/log/loghash/*.log
		rospy.loginfo("Hello from Controller!")
		pub_cmd.publish(msg)
		r.sleep()


if __name__ == '__main__':
	try:
		controller()

	except rospy.ROSInterruptException:
		pass

