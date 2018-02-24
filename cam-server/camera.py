from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.start_preview()
for x in xrange(30): #capture for 1 min
    sleep(2)
    camera.capture('images/image.jpg')
camera.stop_preview()
