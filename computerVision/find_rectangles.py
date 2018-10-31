import datetime

import cv2
# import numpy as np


def find_rectangles(img, img1, measure_sequence):

    image, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    x = 0
    y = 0
    w = 0
    h = 0

    i = 0
    rect_lengths = [[0, 0, 0, 0, 0]]
    for c in contours:
        i = i + 1
        # find bounding box coordinates
        x, y, w, h = cv2.boundingRect(c)
        
        if w > 40 and h > 40:
            rect_lengths.append([x, y, w, h, h + w])
            print(rect_lengths)
            print('the hight is:', h)

    # find the lagerest rectangle ( the max h + w)
    max_rectangle = [0, 0, 0, 0, 0]
    print('--->')
    print(rect_lengths)
    
    for rectLength in rect_lengths:
        if rectLength[4] > max_rectangle[4]:
            max_rectangle[4] = rectLength[4]
            x = rectLength[0]
            y = rectLength[1]
            w = rectLength[2]
            h = rectLength[3]

    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img1, 'height:' + str(h) + 'width:' + str(w), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
    
    cv2.imshow("rectangle", img1)
    photo_number = measure_sequence
    photo_name = '/pi/computerVersion/photos/''specimenLength' + str(datetime.date.today()) + '-' + str(photo_number) + '.jpg'

    cv2.imwrite(photo_name, img1)
    return h

    
if __name__ == '__main__' :
    image = cv2.imread('2017-10-17-1.jpg', 0)
    edges = cv2.Canny(image, 10 , 60)
    cv2.imshow('canny', edges)
    find_rectangles(edges, image)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    

