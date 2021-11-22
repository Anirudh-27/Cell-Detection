# -*- coding: utf-8 -*-

#First run 

import cv2
import numpy as np

img = cv2.imread('0003.jpg',0)

#Blurring only if required
"""img = cv2.medianBlur(img,5)"""
# No need to convert to grayscale as images already in required format.
"""cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)"""

#Use minDist as 50 for first 4 pics, and 30 for 0012 and 0047. 
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,30,param1=50,param2=20,minRadius=5,maxRadius=20)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # Draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

