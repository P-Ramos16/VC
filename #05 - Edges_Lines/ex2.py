# Aula_04_ex_02.py
#
# Mean Filter
#
# Paulo Dias 

#import
import sys
import numpy as np
import cv2

def printImageFeatures(image):
	# Image characteristics
	if len(image.shape) == 2:
		height, width = image.shape
		nchannels = 1
	else:
		height, width, nchannels = image.shape

	# print some features
	print("Image Height: %d" % height)
	print("Image Width: %d" % width)
	print("Image channels: %d" % nchannels)
	print("Number of elements : %d" % image.size)

# Read the image from argv
image = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE );
#image = cv2.imread( "./lena.jpg", cv2.IMREAD_GRAYSCALE );

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

# Average filter 3 x 3
imageAFilter3x3_1 = cv2.blur( image, (3, 3))
imageAFilter5x5_1 = cv2.blur( image, (5, 5))
imageAFilter7x7_1 = cv2.blur( image, (7, 7))

imageAFilter3x3_2 = cv2.blur( imageAFilter3x3_1, (3, 3))
imageAFilter5x5_2 = cv2.blur( imageAFilter5x5_1, (5, 5))
imageAFilter7x7_2 = cv2.blur( imageAFilter7x7_1, (7, 7))

imageAFilter3x3_3 = cv2.blur( imageAFilter3x3_2, (3, 3))
imageAFilter5x5_3 = cv2.blur( imageAFilter5x5_2, (5, 5))
imageAFilter7x7_3 = cv2.blur( imageAFilter7x7_2, (7, 7))



cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )
cv2.imshow( "Display window", imageAFilter3x3_1 )


top_image = cv2.hconcat([imageAFilter3x3_1, imageAFilter5x5_1, imageAFilter7x7_1])
bot_image = cv2.hconcat([imageAFilter3x3_3, imageAFilter5x5_3, imageAFilter7x7_3])

final_image = cv2.vconcat([top_image, bot_image])

cv2.imshow( "Display window", final_image )

cv2.waitKey(0)


