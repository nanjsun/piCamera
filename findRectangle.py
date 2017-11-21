import cv2
import numpy as np


def findRectangles(img,img1):   
#   ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)

    image, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    i = 0
    rectLengths = [[0,0,0,0,0]]
    for c in contours:
        i = i + 1
        #print(i)
        # find bounding box coordinates
        x,y,w,h = cv2.boundingRect(c)
        
       
        
        if w > 40 and h > 40:
            #print('--->',c)  
            rectLengths.append([x, y, w, h, h + w])
            print(rectLengths)
		
            print('the hight is:',h)
           
    #        cv2.rectangle(img1, (x,y), (x+w, y+h), (0, 255, 0), 2)

            # find minimum area
     #       rect = cv2.minAreaRect(c)
            # calculate coordinates of the minimum area rectangle
     #       box = cv2.boxPoints(rect)
            # normalize coordinates to integers
      #      box = np.int0(box)
            # draw contours
    #        cv2.drawContours(img1, [box], 0, (0,0, 255), 3)
            
   #         cv2.putText(img1, 'height:' + str(rectLength[1]) + 'width:' + str(rectLength[0]), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
    #cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
    
    # find the lagerest rectangle ( the max h + w)
    maxrectangle = [0,0,0,0,0]
    print('--->')
    print(rectLengths)
    
    for rectLength in rectLengths:
        if rectLength[4] > maxrectangle[4]:
            maxrectangle[4] = rectLength[4]
            x = rectLength[0]
            y = rectLength[1]
            w = rectLength[2]
            h = rectLength[3]

            
    cv2.rectangle(img1, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img1, 'height:' + str(h) + 'width:' + str(w), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
        
    
    cv2.imshow("rectangle", img1)

    #cv2.waitKey()
    #cv2.destroyAllWindows()
    
if __name__ == '__main__' :
    image = cv2.imread('2017-10-17-1.jpg', 0)
    edges = cv2.Canny(image, 10 , 60)
    cv2.imshow('canny', edges)
    findRectangles(edges, image)
    
    cv2.waitKey()
    cv2.destroyAllWindows()
    

