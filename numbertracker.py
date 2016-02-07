#!/usr/bin/env python
import cv2, sys, time, os
from pantilt import *

# Load the BCM V4l2 driver for /dev/video0
os.system('sudo modprobe bcm2835-v4l2')
# Set the framerate ( not sure this does anything! )
os.system('v4l2-ctl -p 4')

# Frame Size. Smaller is faster, but less accurate.
# Wide and short is better, since moving your head
# vertically is kinda hard!
FRAME_W = 640
FRAME_H = 480

# Set up the capture with our frame size
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  FRAME_W)
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, FRAME_H)
time.sleep(2)

# Default Pan/Tilt for the camera in degrees.
# Camera range is from 0 to 180
cam_pan = 90
cam_tilt = 90
# Move camera to default
pan(cam_pan)
tilt(cam_tilt)
panlist = [90, 70, 50]

#Take image and pan 20 degrees
for x in panlist:
    ret, frame = video_capture.read()
    pan(x)
    picName = "Pic_" + str(x) + ".png"
    cv2.imwrite(picName, frame)

#cv2.imshow("Image", gray)
cv2.waitKey(0)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()