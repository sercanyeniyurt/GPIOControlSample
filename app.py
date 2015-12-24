#!/usr/bin/python
import sys
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

role = int(sys.argv[1])
islem = int(sys.argv[2])


if role>0:
			GPIO.setup(role,GPIO.OUT)
			if islem>=0:
						GPIO.output(role,islem)