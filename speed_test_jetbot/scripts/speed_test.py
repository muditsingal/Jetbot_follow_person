#!/usr/bin/env python

import numpy as np
import time
import serial
import rospy
from speed_test_jetbot.msg import speed_cmd
import os


ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

def make_command(cmd,left_speed,right_speed):
	cmd_to_arduino = cmd + chr(int(left_speed)) + chr(int(right_speed))
	return cmd_to_arduino

def nothing(x):
	pass

move = False
mode = 'S'
left_speed = 0
right_speed = 0
zero_str = 'S' + chr(0) + chr(0)

def callback(cmd):
	#if(cmd.left_speed > -1):
	#	left_speed = int(cmd.left_speed * 126 / 100)

	#else:
	#	left_speed = int((-cmd.left_speed/100)*63)


	#if(cmd.right_speed > -1):
	#	right_speed = int(cmd.right_speed * 126 /100)

	#else:
	#	right_speed = int((-cmd.right_speed/100)*63)

	#command = make_command(mode, left_speed, right_speed)
	#print(command)
	rospy.loginfo("Received command from controller!")
	#ser.write(command.encode())


def jetbot_move():
	print("Node initialized")
	rospy.init_node('jetbot_receiver', anonymous=True)
	print("Subscriber defined")
	rospy.Subscriber('speed_command', speed_cmd, callback)
	print("Ros spinned")
	rospy.spin()

if __name__ == '__main__':
	jetbot_move()
