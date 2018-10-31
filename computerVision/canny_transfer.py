import cv2


def upper_thresholds_slider(x):
    pass


def lower_thresholds_slider(x):
    pass


def canny_transfer(image):
    cv2.namedWindow('canny')
    cv2.createTrackbar('upper', 'canny', 100, 1000, upper_thresholds_slider)
    cv2.createTrackbar('lower', 'canny', 50, 1000, lower_thresholds_slider)
    upper = cv2.getTrackbarPos('upper', 'canny')
    lower = cv2.getTrackbarPos('lower', 'canny')
    # show the frame
    #  cv2.imshow("Frame", image)
    canny = cv2.Canny(image, upper, lower)
    cv2.imshow("canny", canny)

    return canny
