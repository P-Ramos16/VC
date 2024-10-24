#import
import sys
import numpy as np
import cv2

def printImageFeatures(image):
	# Image characteristics
	if len(image.shape) == 2:
		height, width = image.shape
		nchannels = 1;
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

rows, cols = image.shape
M = cv2.getRotationMatrix2D((0, 0), 25, 1)

print(M)

M[0][2] = -50
M[1][2] = 100

print(M)

imageTransformed = cv2.warpAffine(image, M, (cols, rows))

cv2.imwrite("imagename_tf.jpg", imageTransformed)

final_image = cv2.hconcat([image, imageTransformed])

cv2.imshow('Orginal', imageTransformed)

while cv2.waitKey(1000) != 27:
    pass

