#!/usr/bin/env python
# import the necessary packages
import cv2, sys, time, os
from pantilt import *
from picamera.array import PiRGBArray
from picamera import PiCamera
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
rawCapture = PiRGBArray(camera,size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)

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
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    pan(x)
    picName = "Pic_" + str(x) + ".png"
    cv2.imwrite(picName, image)
    cv2.waitKey(0)
    rawCapture.truncate(0)
    time.sleep(2)