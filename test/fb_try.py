# File percobaan

import sys
from firebase import firebase
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

### Setup Firebase ###
SPR = firebase.FirebaseApplication('https://smartplastic-65d5e.firebaseio.com/', None)

### Setup Firebase ###
reader = SimpleMFRC522()

try:
    id = 0
    while id == 0:
        print("Silahkan dekatkan kartu anda")
        id, text=reader.read()
        print("ID: %s\nText: %s" % (id,text))
        print(type(id))
        sleep(5)
finally:
    GPIO.cleanup()


# Make the userPath
userPath = 'Alat1/pengguna/' + id

# Get data to update
SPRdicOn = SPR.get(userPath, None)
print (SPRdicOn)

# Update data
SPR.put(userPath, 'botol kecil', 4)

# Check if the data has been updated
SPRdicOn = SPR.get(userPath, None)
print (SPRdicOn)







