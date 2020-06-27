#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	text = input('New data: ')
	print("Now plae your tag")
	reader.write(text)
	print("Written")
finally:
	GPIO.cleanup()
