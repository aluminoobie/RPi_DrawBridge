#Author:  Peter Di Giorgio
#Date: 15032017
#Version: 0.1
#Purpose: Drawbridge script for BSidesAugusta STEM.


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Input Pins
#Output Pins
#Output PWM: GPIO12, GPIO18
GPIO.setup(