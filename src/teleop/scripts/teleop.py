#!/usr/bin/env python
import rospy
import json
import RPi.GPIO as io
import time
from sensor_msgs.msg import Joy
from std_msgs.msg import String

# sudo chmod og+rwx gpio*

io.setwarnings(False)
io.setmode(io.BOARD)
io.setup(7, io.OUT)
io.setup(16, io.OUT)

drive = io.PWM(7, 50)
drive.start(0)

turn = io.PWM(16, 50)
turn.start(0)

def callback(data):
	drive_v = data.axes[8] * 3 + 7
	turn_v = -2 * data.axes[0] + 7
	if abs(drive_v - 7) < 0.1:
		drive_v = 0
	if abs(turn_v - 7) < 0.1:
		turn_v = 0
	drive.ChangeDutyCycle(drive_v)
	turn.ChangeDutyCycle(turn_v)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("joy", Joy, callback, queue_size=1)
	rospy.spin()

if __name__ == '__main__':
  	listener()
