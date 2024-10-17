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

# Median blur 3 x 3
imageAFilter7x7_normal = cv2.blur( image, (5, 5))
imageAFilter7x7_median = cv2.medianBlur( image, 5)
imageAFilter7x7_gaussian = cv2.GaussianBlur( image, (5, 5), 0)



cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )


top_image = cv2.hconcat([image, imageAFilter7x7_normal])
bot_image = cv2.hconcat([imageAFilter7x7_median, imageAFilter7x7_gaussian])

final_image = cv2.vconcat([top_image, bot_image])

cv2.imshow( "Display window", final_image )

cv2.waitKey(0)


