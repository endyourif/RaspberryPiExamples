# Next two lines only required if using OpenELEC
import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib/')

import time
import RPi.GPIO as GPIO
from led import Led

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redled = Led(18, "RED", 5)
yellowled = Led(8, "YELLOW", 2) 
greenled = Led(20, "GREEN", 0)
whiteled = Led(17, "WHITE", 3)
flashled = Led(27, "FLASH", 0)

redled.on()
redled.off()

greenled.on()
whiteled.on()
whiteled.off()
flashled.flash()
greenled.off()

yellowled.on()
yellowled.off()
flashled.off()

redled.on()
redled.off()

GPIO.cleanup()