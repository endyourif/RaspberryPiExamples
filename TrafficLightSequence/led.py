import time
import RPi.GPIO as GPIO

class Led:
	
	def __init__(self, pinNumber, name, duration):
		self.pinNumber = pinNumber
		self.name = name
		self.duration = duration
		GPIO.setup(pinNumber,GPIO.OUT)
	
	def on (self):
		print(self.name + " on")
		GPIO.output(self.pinNumber, GPIO.HIGH)

	def off (self):
		time.sleep(self.duration)
		print(self.name + " off")
		GPIO.output(self.pinNumber, GPIO.LOW)
	
	def flash (self):
		print(self.name + " flash")
		for x in range (0, 3):
			GPIO.output(self.pinNumber, GPIO.LOW)
			time.sleep(0.5)
			GPIO.output(self.pinNumber, GPIO.HIGH)
			time.sleep(0.5)