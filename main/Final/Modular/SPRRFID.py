import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def checkId():
    global id
    try:
        print("Silahkan dekatkan kartu anda")
        id, text=reader.read()
            #print("ID: %s\nText: %s" % (id,text))
            #print(type(id))
    finally:
        GPIO.cleanup()
        return id
    
def getId():
    return id

