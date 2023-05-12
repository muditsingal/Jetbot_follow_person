#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pin = 37
i = 6

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


while i>0:
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
	i = i - 1


GPIO.cleanup()
