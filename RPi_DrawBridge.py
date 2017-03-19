#Author:  Peter Di Giorgio
#Date: 19032017
#Version: 0.3
#Purpose: Drawbridge script for BSidesAugusta STEM.


import RPi.GPIO as GPIO
import time

#Set the GPIO mode for BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Input Pins
PSHBTNPIN17 = 17
PSHBTNPIN27 = 27
GPIO.setup(PSHBTNPIN17,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(PSHBTNPIN27,GPIO.IN,GPIO.PUD.UP)

#Output Pins
LEDPIN16 = 16
LEDPIN20 = 20
LEDPIN21 = 21
GPIO.setup(LEDPIN16,GPIO.OUT)
GPIO.setup(LEDPIN20,GPIO.OUT)
GPIO.setup(LEDPIN21,GPIO.OUT)

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

#Function to change lights
def ChgLights (Open_Road):
  if Open_Road = 'RoadWay':
    GPIO.output(LEDPIN16,LOW)
    GPIO.output(LEDPIN20,HIGH)
    time.sleep(1)
    GPIO.output(LEDPIN20,LOW)
    GPIO.output(LEDPIN21,HIGH)
    return;
  if Open_Road = 'WaterWay':
    GPIO.output(LEDPIN21,LOW)
    GPIO.output(LEDPIN20,HIGH)
    time.sleep(1)
    GPIO.output(LEDPIN20,LOW)
    GPIO.output(LEDPIN16,HIGH)
    return;
  
while True:
  Road_Input = GPIO.input(PSHBTNPIN17)
  Water_Input = GPIO.input(PSHBTNPIN27)
  if Road_Input = True and Water_Input  = False:
    Open_Road = 'RoadWay'
    ChgLights(Open_Road)
    RoadWay_Gate.start(10)
    WaterWay_Gate.start(5)
  if Road_Input = False and Water_Input = True:
    Open_Road = 'WaterWay'
    ChgLights(Open_Road)
    RoadWay_Gate.start(5)
    WaterWay_Gate.start(10)
  if Road_Input = True and Water_Input = True:
    RoadWay_Gate.start(5)
    WaterWay_Gate.start(5)
    GPIO.output(LEDPIN16,HIGH)
    time.sleep(0.5)
    GPIO.output(LEDPIN20,HIGH)
    time.sleep(0.5)
    GPIO.output(LEDPIN21,HIGH)
    GPIO.output(LEDPIN16,LOW)
    GPIO.output(LEDPIN20,LOW)
    GPIO.output(LEDPIN21,LOW
    break
  time.sleep(0.1)

print "Good bye!"
GPIO.cleanup()
