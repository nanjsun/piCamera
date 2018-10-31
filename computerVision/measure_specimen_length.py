import cv2
# import time
from canny_transfer import canny_transfer
from find_rectangles import find_rectangles
from start_camera import start_camera


def measure_specimen_length():
    raw_capture, frames = start_camera()
    frame_counter = 0
    measure_sequence = 0
    height = 0;
    for frame in frames:
        image = frame.array
        frame_counter = frame_counter + 1
        if frame_counter > 10 and (measure_sequence < 5):
            canny = canny_transfer(image)
            height = height + find_rectangles(canny, image, measure_sequence)
            frame_counter = 0
            measure_sequence = measure_sequence + 1
            print('average height in 5 measure:')
            print(height/5)

        if measure_sequence == 5:
            return height/5

        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        raw_capture.truncate(0)
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break


if __name__ == '__main__':
    measure_specimen_length()




