#Author:  Peter Di Giorgio
#Date: 09042017
#Version: 1.0
#Purpose: Drawbridge script for BSidesAugusta STEM.


import RPi.GPIO as GPIO
import time

#Set the GPIO mode for BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Input Pins
PSHBTNPIN17 = 17
PSHBTNPIN27 = 27
GPIO.setup(PSHBTNPIN17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(PSHBTNPIN27,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#Output Pins
LEDPIN16 = 16
LEDPIN20 = 20
LEDPIN21 = 21
GPIO.setup(LEDPIN16,GPIO.OUT)
GPIO.setup(LEDPIN20,GPIO.OUT)
GPIO.setup(LEDPIN21,GPIO.OUT)

#Output PWM: GPIO12, GPIO18
servoPINRW = 12
servoPINWW = 13
GPIO.setup(servoPINRW,GPIO.OUT)
GPIO.setup(servoPINWW,GPIO.OUT)

#Set 50 Hz
RoadWay_Gate = GPIO.PWM(servoPINRW,50)
WaterWay_Gate = GPIO.PWM(servoPINWW,50)

#Start servos at full left position or both gates down
RoadWay_Gate.start(5)
WaterWay_Gate.start(5)

#Function to change lights
def ChgLights (Open_Road):
  if Open_Road == 'RoadWay':
    GPIO.output(LEDPIN16,GPIO.LOW)
    GPIO.output(LEDPIN20,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LEDPIN20,GPIO.LOW)
    GPIO.output(LEDPIN21,GPIO.HIGH)
    print "Road Way is Open and Water Way is Closed"
    return;
  if Open_Road == 'WaterWay':
    GPIO.output(LEDPIN21,GPIO.LOW)
    GPIO.output(LEDPIN20,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LEDPIN20,GPIO.LOW)
    GPIO.output(LEDPIN16,GPIO.HIGH)
    print "Road Way is Closed and Water Way is Open"
    return;
  
while True:
  Road_Input = GPIO.input(PSHBTNPIN17)
  Water_Input = GPIO.input(PSHBTNPIN27)
  if Road_Input == True and Water_Input  == False:
    print "Opening Road Way"
    Open_Road = 'RoadWay'
    ChgLights(Open_Road)
    RoadWay_Gate.start(10)
    WaterWay_Gate.start(5)
  if Road_Input == False and Water_Input == True:
    print "Opening Water Way"
    Open_Road = 'WaterWay'
    ChgLights(Open_Road)
    RoadWay_Gate.start(5)
    WaterWay_Gate.start(10)
  if Road_Input == True and Water_Input == True:
    print "Closing Road and Water Way.  Shutting System Down...."
    RoadWay_Gate.start(5)
    WaterWay_Gate.start(5)
    GPIO.output(LEDPIN16,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDPIN20,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDPIN21,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDPIN16,GPIO.LOW)
    GPIO.output(LEDPIN20,GPIO.LOW)
    GPIO.output(LEDPIN21,GPIO.LOW)
    break
  time.sleep(0.1)

print "Good bye!"
GPIO.cleanup()
