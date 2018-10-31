# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import datetime
 

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.sensor_mode = 2# set the sensor_mode to 2, and get the resolution of 1296X730 ,framerate from 1 to 42
camera.resolution = (1640, 1232)
#camera.resolution = (2592, 1944)
camera.framerate = 2
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(1640, 1232))
#rawCapture = PiRGBArray(camera, size=(2592, 1944))

# allow the camera to warmup
time.sleep(0.1)
photoNumber = 1
videoNumber = 1

def recordVideo():
    global videoName
    global videoNumber
    global key
    print('start recording vidoe')
    #videoName = str(datetime.date.today()) + '-' + str(videoNumber) + '.h264'
    videoName = str(time.strftime("%Y-%m-%d-%H-%M", time.localtime())) + '-' + str(videoNumber) + '.h264'
    videoNumber = videoNumber + 1
    camera.start_recording('/home/pi/piCamera/photos/' + videoName)

    
    
    


# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array   

    # show the frame
    cv2.namedWindow("Frame", 0)
    cv2.resizeWindow("Frame",400, 300) 
    
    cv2.imshow("Frame", image)   
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("p"):
        photoName = str(time.strftime("%Y-%m-%d-%H-%M", time.localtime())) + '-' + str(photoNumber) + '.jpg'
        photoNumber = photoNumber + 1
        
        cv2.imwrite('/home/pi/piCamera/photos/' + photoName, image)
        print('take photo ok! and save in ' + photoName)
    
    
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








