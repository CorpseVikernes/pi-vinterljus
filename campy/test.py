import cv2
import os
import time

os.system("sudo pkill uv4l")
os.system("sudo uv4l --driver raspicam --auto-video_nr --extension-presence=1 --encoding rgba --width 320 --height 240 --nopreview")

class CamTest():


    threshold = 20
    sensitivity = 180
    colorChannel = 1
    oldImg = 0
    img = 0
    s = 1
    cam = 0

    def __init__(self):

        self.cam = cv2.VideoCapture(0)

    def run(self):
        print "Starting motion detection"
        while True:
            time.sleep(0.05)
            self.s, self.img = self.cam.read()
    
            if self.oldImg != 0:
                motionDetect()
            self.oldImg = self.img

    def motionDetect(self):
    
        pixDiff = 0
        changedPixels = 1
        for x in range(width):
            for y in range(height):
                newPix = self.img[x][y][self.colorChannel]
                oldPix = self.oldImg[x][y][self.colorChannel]
                pixDiff = abs(newPix - oldPix)
            
                if pixDiff > self.threshold:
                    changedPixels += 1
                
                if changedPixels > self.sensitivity:
                    print "motion detected"
                    return

        print "motionless"


camTest = CamTest()
camTest.run()
