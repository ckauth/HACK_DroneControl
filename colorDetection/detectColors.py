
import numpy as np
import cv2 as cv
import os, sys
import matplotlib.pyplot as plt
import pylab

MAX_NUM_PIC = 15

# trigger to start and end camera operation

def endOperation(numberOfPics):
    if (numberOfPics > MAX_NUM_PIC): # if more than MAX_NUM_PIC pictures are taken, disregard the rest
        return

dir_path = '/Users/yoonheeh/Desktop/starthack/colorDetection/pics/'
results = []
imageArray = []
difference_distribution = []
red_distribution = []
green_distribution = []

def calculateRedGreen(img):
    #print (img.shape)
    b, g, r = cv.split(img)
    b = sum(sum(b))
    g = sum(sum(g))
    r = sum(sum(r))
    # print (b,g,r)
    totalBlueValue, totalRedValue, totalGreenValue = b,g,r
    return totalRedValue, totalGreenValue

def categorize(redVal, greenVal):
    # returns 1 if red, 0 if green
    return (redVal<greenVal)


def makePanoramaImage(imageArray):
    numberOfImages = len(imageArray)
    # width and height of the panorama image we want to show
    for i in range(0, numberOfImages-1):
        imageArray[i] = np.concatenate((imageArray[i], imageArray[i+1]), axis=1)
        imageArray[i+1] = imageArray[i]
    return imageArray[numberOfImages-1]

def analyzeImages():

    #list_dir = os.listdir(dir_path)

    # get number of images in a folder and loop
    for filename in sorted(os.listdir(dir_path)):
        image_path = dir_path + filename
        statinfo = os.stat(image_path)
        #print(image_path)
        # check if it is larger than 10 bytes
        if (statinfo.st_size > 10) and filename.endswith(".jpg") or filename.endswith(".jpeg"):
            currentImg = cv.imread(image_path, 1)
            currentImg = cv.medianBlur(currentImg, 3)  # better at finding the maximum
            r, g = calculateRedGreen(currentImg)
            difference_distribution.append(r-g)
            red_distribution.append(r)
            green_distribution.append(g)

            # better filter for general
            currentImg = cv.GaussianBlur(currentImg, (5, 5), 0)
            r, g = calculateRedGreen(currentImg)
            #print (r, g)
            #print (categorize(r, g))
            results.append(categorize(r, g))
            imageArray.append(currentImg)

        else:
            print ("WARNING: not a valid image file")



def showPanoramaImage():
    panoramaImage = makePanoramaImage(imageArray)
    cv.imwrite('/img_output/panorama_img_output.jpg', panoramaImage)
    cv.namedWindow("final panorama", cv.WINDOW_NORMAL)
    cv.resizeWindow("final panorama", 1440, 900)
    cv.moveWindow("final panorama",0,0)
    cv.imshow('final panorama', panoramaImage)
    cv.waitKey(0)

# green = true
# plot distribution of trues and falses
def plotResults():
    indices = range(0,len(results))

    plt.figure(1)
    plt.subplot(411)
    plt.plot(indices,results,'b')
    plt.title('Green (True) or Red (False)?')

    plt.subplot(412)
    plt.plot(indices,difference_distribution,'k')
    plt.title('Difference Distribution')

    plt.subplot(413)
    plt.plot(indices,red_distribution,'r')
    plt.title('Red Distribution')

    plt.subplot(414)
    plt.plot(indices,green_distribution,'g')
    plt.title('Green Distribution')

    plt.savefig("img_output/output_graph.png")
    plt.show()




# mark the points that experience changes
# assume that the result is quite accurate
def determineRedRegion():
    sample_number = len(difference_distribution)
    # combine results from three regions to decide which has the max
    maxregion = 0
    minregion = difference_distribution[0]
    for i in range(1, sample_number-1):
        regionalsum = difference_distribution[i-1] + difference_distribution[i] + difference_distribution[i+1]
        if (regionalsum > maxregion):
             maxregion = i
        elif (regionalsum < minregion):
            minregion = i
        else: continue
    # now min region and max region is found
    # max region is red; min region is green
    #print("min (green): ", minregion, "max (red): ", maxregion)



    print("======================== result of the detection ========================")
    print("locating broken generator...")
    print("\n")
    # divide regions into three sections
    if (maxregion/sample_number*1.0 >= 0.7):
        # last section
        print("red detected in the last region")
    elif (maxregion/sample_number*1.0 < 0.7 and maxregion/sample_number*1.0 > 0.3 ):
        # second section (middle section)
        print("red detected in the middle region")
    else:
        # first section
        print("red detected in the first region")
    print("\n")
    print("======================== end of the flight ========================")



analyzeImages()
showPanoramaImage()
determineRedRegion()
plotResults()


