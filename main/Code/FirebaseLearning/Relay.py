import RPi.GPIO as GPIO
import time

RELAY = 16

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT)

def relay_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    
def relay_off(pin):
    GPIO.output(pin, GPIO.LOW)
    
    
while True:
    relay_on(RELAY)
    print("on")
    time.sleep(3)
    GPIO.cleanup()
        
