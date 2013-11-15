import cv2
import os
import time

os.system("sudo pkill uv4l")
os.system("sudo uv4l --driver raspicam --auto-video_nr --extension-presence=1 --encoding rgba --width 320 --height 240 --nopreview")

cam = cv2.VideoCapture(0)
s, img = cam.read()
if s:
    print "Img was read"
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test", img)
    waitkey(0)
    time.sleep(1)
    destroyWindow("cam-test")
else:
    print "Could not get img"
