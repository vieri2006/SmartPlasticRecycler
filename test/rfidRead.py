import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

RFID_state = 0
try:
    while RFID_state == 0:
        print("Silahkan dekatkan kartu anda")
        id, text=reader.read()
        print("ID: %s\nText: %s" % (id,text))
        print(type(id))
        RFID_state = 1
finally:
    GPIO.cleanup()
