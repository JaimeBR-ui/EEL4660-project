#!/usr/bin/env python3
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
p = io.PWM(7, 50)
p.start(0)

def callback(data):
	value = data.axes[1] * 4 + 7
	p.ChangeDutyCycle(value)
	print(value)

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("joy", Joy, callback)
	rospy.spin()

if __name__ == '__main__':
  	listener()
