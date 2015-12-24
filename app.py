#!/usr/bin/python
import sys
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# The role and status information from being received
role = int(sys.argv[1])
islem = int(sys.argv[2])

# If the number is greater than 0 GPIO make the setup role, implementing a process that you send.
if role>0:
			GPIO.setup(role,GPIO.OUT)
			if islem>=0:
						GPIO.output(role,islem)
