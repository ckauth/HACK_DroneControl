
from picamera import PiCamera
import picamera
import picamera.array

from time import sleep

from imgproc import *

import numpy as np


def analyzeImage(cameraImg):
    red = []
    green = []
    blue = []

    # store each rgb value
    for x in range(0, cameraImg.width):
        for y in range(0, cameraImg.height):
            # get the value of the current pixel
            idx = x * cameraImg.height + y
            red[idx], green[idx], blue[idx] = cameraImg[x, y]

    totalRed = np.sum(red)
    totalGreen = np.sum(green)

    return (totalRed < totalGreen)

def startCamera():
    camera = PiCamera()

    camera.rotation = 180
    camera.start_preview()
    greencount = 0
    for x in xrange(30): #capture for 1 min
        sleep(2)
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as output:
                camera.capture(cameraImg, 'rgb')
                print('Captured %dx%d image' % (
                    cameraImg.array.shape[1], cameraImg.array.shape[0]))
        if (analyzeImage(cameraImg)): # if it is green, add to green count
            greencount = greencout + 1

        if (greencount > 3):
            # it is green light; should depart
            camera.stop_preview()
            return True
        else:
            camera.stop_preview()
            return False








