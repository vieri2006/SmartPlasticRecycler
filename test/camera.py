from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.annotate_text = "Masukkan Botol"
sleep(5)
camera.capture('/home/pi/Desktop/botol.jpg')
camera.stop_preview()