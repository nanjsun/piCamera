from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from find_rectangles import find_rectangles


def start_camera():
    camera = PiCamera()
    camera.sensor_mode = 5
    camera.resolution = (1296, 200)
    camera.framerate = 10
    camera.hflip = True
    camera.vflip = True
    raw_capture = PiRGBArray(camera, size=(1296, 200))

    # allow the camera to warm up
    time.sleep(0.1)
    frames = camera.capture_continuous(raw_capture, format="bgr", use_video_port=True)

    return raw_capture, frames


if __name__ == '__main__':
    x = start_camera()

