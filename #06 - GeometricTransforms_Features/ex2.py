#import
import sys
import numpy as np
import cv2

global srcPts

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

def select_src(event, x, y, flags, params):
	global srcPts
	if event == cv2.EVENT_LBUTTONDOWN:
		srcPts.append((x,y))
		cv2.circle(src, (x, y), 2, (255, 0, 0), 2)
		cv2.putText(src,str(len(srcPts)), (x+10,y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
		cv2.imshow("orginal", src)


# Read the image from argv
#image = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE );
image = cv2.imread( "./imagename_tf.jpg", cv2.IMREAD_GRAYSCALE );


if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)


printImageFeatures(image)

rows, cols = image.shape

select_src()



imageTransformed = cv2.warpAffine(image, M, (cols, rows))

final_image = cv2.hconcat([image, imageTransformed])

cv2.imshow('Orginal', imageTransformed)

while cv2.waitKey(1000) != 27:
    pass

