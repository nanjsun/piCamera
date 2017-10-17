# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import datetime
 

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1080, 720)
camera.framerate = 30
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(1080, 720))

# allow the camera to warmup
time.sleep(0.1)
photoNumber = 1
videoNumber = 1

def recordVideo():
    global videoName
    global videoNumber
    global key
    print('start recording vidoe')
    videoName = str(datetime.date.today()) + '-' + str(videoNumber) + '.h264'
    videoNumber = videoNumber + 1
    camera.start_recording(videoName)

    
    
    


# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array   

    # show the frame
    cv2.imshow("Frame", image)   
    
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("p"):
        photoName = str(datetime.date.today()) + '-' + str(photoNumber) + '.jpg'
        photoNumber = photoNumber + 1
        
        cv2.imwrite(photoName, image)
        print('take photo ok!')
    
    
    if key == ord("v"):
        recordVideo()
        
    if key == ord("s"):
        camera.stop_recording()
        print('recording vidoeb ok !')

        
    
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break








