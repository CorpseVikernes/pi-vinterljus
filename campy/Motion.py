#!/usr/bin/python
# -*- coding: utf-8 -*-

import StringIO
import subprocess
import os
import time
from datetime import datetime
from PIL import Image

import threading


class Motion(threading.Thread):


    def __init__(self):

        # Threading init
        threading.Thread.__init__(self)
        self.setName = "Motion"
        self.daemon = True
        
        # Threshold (Amount of pixel color change)
        self.threshold = 10
        # Sensitivity (Amount of pixels needed to signal motion detected)
        self.sensitivity = 180

        # Preview options
        self.previewON = True
        self.previewX = 0
        self.previewY = 0
        self.previewWidth = 1024
        self.previewHeight = 800

        # Image options
        self.imageWidth = 100
        self.imageHeight = 100
        self.imageQuality = 100
        
        # Init buffers
        self.image1 = None
        self.image2 = None
        self.buffer1 = None
        self.buffer2 = None

        # Init matrix
        self.matrixSize = 20
        self.squareWidth = self.imageWidth/self.matrixSize
        self.squareHeight = self.imageHeight/self.matrixSize
        self.matrix = [[0 for i in range(self.matrixSize)] for j in range(self.matrixSize)]

        # Raspistill options
        if(self.previewON):
            self.command = "raspistill -w %s -h %s -q %s -p %s,%s,%s,%s -t 1000 -e bmp -o -" %(self.imageWidth, self.imageHeight, self.imageQuality, self.previewX, self.previewY, self.previewWidth, self.previewHeight)
        else:
            self.command = "raspistill -w %s -h %s -q %s -t 1000 -e bmp -o -" %(self.imageWidth, self.imageHeight, self.imageQuality)



    def run(self):
        print "            Motion Detection Started"
        print "            ------------------------"
        print "Pixel Threshold (How much)   = " + str(self.threshold)
        print "Sensitivity (changed Pixels) = " + str(self.sensitivity)
        print "---------- Motion Capture File Activity --------------"

        self.matrixDetection()


    # Capture a small test image (for motion detection)
    def captureTestImage(self):
        imageData = StringIO.StringIO()
        imageData.write(subprocess.check_output(self.command, shell=True))
        imageData.seek(0)
        im = Image.open(imageData)
        buffer = im.load()
        imageData.close()
        return im, buffer


    # Help function for matrixDetection (DETECTS MOTION)
    def motionDetection(self, matrixX, matrixY, oldValue):
        # Count changed pixels
        changedPixels = 0
        for x in xrange(0, self.squareWidth):
            xPos = matrixX*self.matrixSize + x
            # Scan one line of image then check sensitivity for movement
            for y in xrange(0, self.squareHeight):
                yPos = matrixY*self.matrixSize + y
                # Just check green channel as it's the highest quality channel
                pixdiff = abs(buffer1[xPos,yPos][1] - buffer2[xPos,yPos][1])
                if pixdiff > self.threshold:
                    changedPixels += 1

                # If a motion should be counted as detected
                if changedPixels > self.sensitivity:   
                    # Add motion activity
                    print "Motion detected in : " + str(matrixX) + ", " + str(matrixY)
                    return oldValue + 2
                    break
                continue
        
        # Remove motion activity 
        if(oldValue > 0):
            oldValue = oldValue - 1
        return oldValue
        
    # Check for motion in diffrent parts of the image
    def matrixDetection(self):

        # Get first image
        self.image1, self.buffer1 = self.captureTestImage()

        while (True):
            # Putting thread to sleep so CPU LOAD will decrease
            time.sleep(1)
            
            # Get comparison image
            self.image2, self.buffer2 = self.captureTestImage()
            
            # For each position in the matrix check for motion
            for x in xrange(self.matrixSize):
                for y in xrange(self.matrixSize):
                    matrixValue = self.matrix[x][y]
                    self.matrix[x][y] = self.motionDetection(x,y, matrixValue)
 
            # Swap comparison buffers
            self.image1  = self.image2
            self.buffer1 = self.buffer2
