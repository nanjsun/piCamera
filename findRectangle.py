import cv2
import numpy as np

#thresh


def findRectangles(img,img1):	
#	ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)

	image, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	i = 0
	for c in contours:
		i = i + 1
		print(i)
		# find bounding box coordinates
		x,y,w,h = cv2.boundingRect(c)
		#print('--->',c)  

		print('the hight is:',h)
		cv2.rectangle(img1, (x,y), (x+w, y+h), (0, 255, 0), 2)

		# find minimum area
		rect = cv2.minAreaRect(c)
		# calculate coordinates of the minimum area rectangle
		box = cv2.boxPoints(rect)
		# normalize coordinates to integers
		box = np.int0(box)
		# draw contours
		cv2.drawContours(img1, [box], 0, (0,0, 255), 3)
		
	#cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
	cv2.imshow("contours", img1)

	#cv2.waitKey()
	#cv2.destroyAllWindows()
#image = cv2.imread('canny.jpg')

#findRectangles(image)

