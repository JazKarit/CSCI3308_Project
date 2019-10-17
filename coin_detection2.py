import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('coins1.jpg')
blur = cv2.bilateralFilter(img,9,75,75)
gray_blur = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
#gray_blur = cv2.bilateralFilter(gray,9,75,75)
#thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)
#kernel = np.ones((3, 3), np.uint8)
#closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)
cimg = img.copy()


circles = cv2.HoughCircles(gray_blur,cv2.HOUGH_GRADIENT,1,80,
                            param1=20,param2=40,minRadius=45,maxRadius=80)
for circle in circles[0,:]:
	# draw the outer circle
	cv2.circle(cimg,(circle[0],circle[1]),circle[2],(0,255,0),2)
    # draw the center of the circle
	cv2.circle(cimg,(circle[0],circle[1]),2,(0,0,255),3)
	
cv2.imshow("Original", gray_blur)
cv2.waitKey(0)
# ~ cv2.imshow("Canny", ac_img)
# ~ cv2.waitKey(0)
cv2.imshow('Detected Circles',cimg)
cv2.waitKey(0)
cv2.imwrite('coin_detection_test.jpg', cimg) 
