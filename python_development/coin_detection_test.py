import cv2
import numpy as np
import math
from coin_detection import detect_coin_circles
from coin_identification import coinFinder

actual_circles = [19,  19,19,21,15,15,15,15,15,15,15,15,15,15,15,15,15]
actual_values =  [2.74,0.1,0.1,3.09,1.74,0.1,1.74,1.74,1.74,1.74,1.74,1.74,1.0,2.75]
calculated_value_errors = []
errors = []
tests = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#var_tries = [.41,.39,.4,.38,.37,.36]
#Test our coin detection on all the test images we have
#for var_a in var_tries:
errors = []
for i in tests:
	circles,image,pennies = detect_coin_circles('test_images/coins' + str(i) + '.jpg',True)
	errors.append(1 - abs(len(circles)-actual_circles[i-1])/float(actual_circles[i-1]))
	calculated_value = coinFinder(circles)
	calculated_value_errors.append(1-abs(actual_values[i-1]-calculated_value)/float(actual_values[i-1]))
	print("calculated value: " + str(calculated_value+pennies*.01))
	print("actual value: " + str(actual_values[i-1]))
	print("percent: " + str(1-abs(actual_values[i-1]-calculated_value)/float(actual_values[i-1])))
#print("var = " + str(var_a) + ": " + str(np.average(np.array(errors))))

#print(str(np.average(np.array(errors))))
print(errors)
print("Avg percent of value detected:" + str(np.average(np.array(errors))))
