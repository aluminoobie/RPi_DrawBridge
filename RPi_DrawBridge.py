#Author:  Peter Di Giorgio
#Date: 15032017
#Version: 0.2
#Purpose: Drawbridge script for BSidesAugusta STEM.


import RPi.GPIO as GPIO
import time

#Set the GPIO mode for BCM numbering
GPIO.setmode(GPIO.BCM)

#Input Pins

#Output Pins

#Output PWM: GPIO12, GPIO18
servoPIN12 = 12
servoPIN18 = 18
GPIO.setup(servoPIN12,GPIO.OUT)
GPIO.setup(servoPIN18,GPIO.OUT)

#Set 50 Hz
RoadWay_Gate = GPIO.PWM(servoPIN12,50)
WaterWay_Gate = GPIO.PWM(servoPIN18,50)

#Start servos at full left position or both gates down
RoadWay_Gate.start(5)
WaterWay_Gate.start(5)

