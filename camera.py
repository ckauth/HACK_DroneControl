from picamera import PiCamera
from time import sleep

def take_photos():

    with PiCamera() as camera:
        #camera.rotation = 180
        for i in xrange(60): #capture for 1 min
            sleep(1)
            camera.capture('cam-server/images/'+str(i)+'.jpg')

