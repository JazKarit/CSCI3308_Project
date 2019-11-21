import numpy as np
import cv2
import statistics
import imutils
import math
import random



def get_circles(mask,original,image,show_result=False,debug=False):
	coin_colors = []
	####
	# noise removal
	kernel = np.ones((3,3),np.uint8)
	opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 2)
	#opening = cv2.erode(mask,kernel,iterations = 5)
	# sure background area - borders enlarged a bit
	sure_bg = cv2.dilate(opening,kernel,iterations=2)
	# Finding sure foreground area
	dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,0)
	ret, sure_fg = cv2.threshold(dist_transform,.41*dist_transform.max(),255,0)#this one effects detection a lot lower number ~ -> more detection
	# Finding unknown region
	sure_fg = np.uint8(sure_fg)
	unknown = cv2.subtract(sure_bg,sure_fg)
	
	#Show sure background and foreground, white=unknown
	if debug:
		cv2.imshow("bg vs fg", unknown)
		cv2.waitKey(0)

	# Marker labelling
	ret, markers = cv2.connectedComponents(sure_fg)
	# Add one to all labels so that sure background is not 0, but 1
	markers = markers+1
	# Now, mark the region of unknown with zero
	markers[unknown==255] = 0


	#markers is an array of the picture, -1 means its part of a detected line
	labels = cv2.watershed(original,markers)
	original[markers == -1] = [0,255,0]

	#https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html
	####

	####
	# loop over the unique labels returned by the Watershed
	# algorithm

	circles = []
	pennies = 0
	for label in np.unique(labels):
		# if the label is 0,-1,1, we are examining the 'background'
		# so simply ignore it
		if label == 0 or label == -1 or label == 1:
			continue
	 
		# otherwise, allocate memory for the label region and draw
		# it on the mask
		mask = np.zeros(mask.shape, dtype="uint8")
		mask[labels == label] = 255
	 
		# detect contours in the mask and grab the largest one
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		c = max(cnts, key=cv2.contourArea)
		
		#contour_list.append(contour)
		# draw a circle enclosing the object
		((x, y), r) = cv2.minEnclosingCircle(c)
		#We're using max enclosing circle, so if the contour is a perfect circle
		#then the are should be 4*pi*r^2. We can filter out contours that 
		#enclose a much smaller area
		if cv2.contourArea(c) > 2*r**2:
			
			if x-r < 0 or y-r < 0 or x+r > len(image[0]) or y+r > len(image):
				continue
			penny = True
			for i in range(-20,20):
				for j in range(-20,20):
					coin_colors.append(image[int(y+j)][int(x+i)])
					if image[int(y+j)][int(x+i)][1] < 40:
						penny = False
			if penny:
				pennies+=1
				continue
			circles.append(((x,y),r))
			
	return circles,pennies,coin_colors


def detect_coin_circles(img_src,show_result=False,debug=False):
	"""
	Detect coins in image and return a list of circles in format((x,y),r)
	
	"""
	image = cv2.imread(img_src)
	original = image.copy()
	original2 = image.copy()
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
	#make pixel_arr, 1D array of all pixels
	#it will be used to find the average and standard deviation of the color
	pixel_arr = []
	
	for i in range(0,len(image)):
		for j in range(0,len(image[0])):
			pixel_arr.append(image[i][j])
	avg_color = np.average(pixel_arr, axis=0)
	std = np.std(pixel_arr, axis=0)

	#Make a mask of everything outside one std from the avg
	#This should mainly include silver colored coins
	lower = avg_color-1*std
	upper = avg_color+1*std
	mask = cv2.inRange(image, lower, upper)
	mask = cv2.bitwise_not(mask)
	cimg = original.copy()
	


	kernel = np.ones((3, 3), np.uint8)

	#show mask: white is possible coins
	if debug:
		cv2.imshow("mask", mask)
		cv2.waitKey(0)

	circles,pennies,coin_colors = get_circles(mask,original,image,show_result,debug)
	

		
	avg_color = np.average(coin_colors, axis=0)
	std = np.std(coin_colors, axis=0)

	#Make a new mask from the colors of detected coins
	lower = avg_color-3.5*std
	upper = avg_color+3.5*std
	mask = cv2.inRange(image, lower, upper)
	#mask = cv2.bitwise_not(mask)
	cimg = original2.copy()

	#show mask: white is possible coins
	if debug:
		cv2.imshow("mask", mask)
		cv2.waitKey(0)
    
    
	circles2,pennies2,coin_colors2 = get_circles(mask,original2,image,show_result,debug)

	circles3 = circles + circles2 
	circles4 = list(circles3)
	for i in range(len(circles3)):
		for j in range(i+1,len(circles3)):
			dist = math.sqrt((circles3[i][0][0]-circles3[j][0][0])**2 + (circles3[i][0][1]-circles3[j][0][1])**2 )
			if (dist*1.3 < circles3[j][1] or dist*1.3 < circles3[i][1]) and len(circles4) > j:
				circles4.pop(j)
			# ~ else:
				# ~ print(dist*1.3,circles3[j][1])
				
	for circle in circles4:			
		cv2.circle(original, (int(circle[0][0]),int(circle[0][1])),int(circle[1]), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)
		#cv2.putText(original, "#{}".format(len(circles)), (int(x) - 10, int(y)),
		#cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
	
	if show_result:
		cv2.imshow("Detected Circles1", original)
		cv2.waitKey(0)

		
	
	
	return circles4,original2,pennies






