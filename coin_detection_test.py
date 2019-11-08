import cv2
import numpy as np
from coin_detection import detect_coin_circles

#Test our coin detection on all the test images we have
for i in range(1,13):
	circles,image = detect_coin_circles('coins' + str(i) + '.jpg',True)

