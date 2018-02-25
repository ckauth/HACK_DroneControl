import picamera.array

from time import sleep

from imgproc import *

import numpy as np


def analyzeImage(cameraImg):
    width = cameraImg.array.shape[1]
    height = cameraImg.array.shape[0]
    red = [0]*width*height
    green = [0]*width*height
    blue = [0]*width*height

    # store each rgb value
    print cameraImg.array[:,:,1].size
    r1, g1 = cameraImg.array[:,:,0], cameraImg.array[:,:,1]
    '''for x in range(0, cameraImg.array.shape[1]):
        for y in range(0, cameraImg.array.shape[0]):
            # get the value of the current pixel
            idx = x * cameraImg.array.shape[0] + y
            red[idx], green[idx], blue[idx] = cameraImg.array[y][x]'''
    
    totalRed = np.sum(r1)
    totalGreen = np.sum(g1)

    return (totalRed < totalGreen)

def startCamera():
    #camera = PiCamera()

    #camera.rotation = 180
    #camera.start_preview()
    greencount = 0
    prior_color = 'red'
    for x in xrange(30): #capture for 1 min
        sleep(0.5)
	cameraImg = None
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as cameraImg:
                camera.resolution = (480, 270)
		camera.capture(cameraImg, 'rgb')
                print('Captured %dx%d image' % (
                    cameraImg.array.shape[1], cameraImg.array.shape[0]))
        	if cameraImg is None:
	    	    print 'no image'
		else:
		    print cameraImg.array.shape
	    	    if (analyzeImage(cameraImg)): # if it is green, add to green count
                	if prior_color == 'green':
			    greencount = greencount + 1
			else:
			    greencount = 1
			print greencount
			prior_color = 'green'
		    else:
			prior_color = 'red'

        if (greencount > 3):
            # it is green light; should depart
            #camera.stop_preview()
            return True
	
	print x
	
    #return false

#startCamera()






