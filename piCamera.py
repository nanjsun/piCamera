# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from findRectangle import findRectangles


def upperThresholdsSlider(x):
    pass
def lowerThresholdsSlider(x):
    pass
    
#def minLineLengthSlider(x):
#    pass
#def maxLineGapSlider(x):
#    pass    
    
    
cv2.namedWindow('canny')  
#cv2.namedWindow('HoughlinesP')   
cv2.createTrackbar('upper', 'canny', 100, 1000, upperThresholdsSlider)
cv2.createTrackbar('lower', 'canny', 50, 1000, lowerThresholdsSlider)

#cv2.createTrackbar('minLineLength', 'HoughlinesP', 100, 1000, minLineLengthSlider)
#cv2.createTrackbar('maxLineGap', 'HoughlinesP', 400, 1000, maxLineGapSlider)




# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.sensor_mode = 5
camera.resolution = (1296, 200)
camera.framerate = 10
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(1296, 200))

# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
frameCounter = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array   
    upper = cv2.getTrackbarPos('upper', 'canny')
    lower = cv2.getTrackbarPos('lower', 'canny')   
    # show the frame
  #  cv2.imshow("Frame", image)   
    canny = cv2.Canny(image, upper, lower)
    cv2.imshow("canny", canny)
    
    frameCounter = frameCounter + 1
    if frameCounter > 10:
        findRectangles(canny, image)
        frameCounter = 0
        
    minLineLength = minLineLength = cv2.getTrackbarPos('minLineLength', 'lines')
    maxLineGap = maxLineGap = cv2.getTrackbarPos('maxLineGap', 'lines')
    lines = cv2.HoughLinesP(canny, 1, np.pi/180, 20, minLineLength, maxLineGap)
    #print(lines)
    
#    try:
#        if lines.any():
#            for line in lines:
#                for x1, y1, x2, y2 in line:
#                    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#            cv2.imshow('HoughlinesP', image)
#    except:
#        print("None line found!")
    
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
