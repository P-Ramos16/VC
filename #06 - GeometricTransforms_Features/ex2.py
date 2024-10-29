#import
import sys
import numpy as np
import cv2
import math

global srcPts
global dstPts

windowName = "Image Window"

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
	if event == cv2.EVENT_LBUTTONDOWN and len(srcPts) < 3:

			srcPts.append((x,y))
			cv2.circle(image, (x, y), 2, (255, 0, 0), 2)
			cv2.putText(image,str(len(srcPts)), (x+10,y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
			cv2.imshow("Original", image)




def select_dst(event, x, y, flags, params):
	global dstPts
	global srcPts
	if event == cv2.EVENT_LBUTTONDOWN and len(dstPts) < 3:

			dstPts.append((x,y))
			cv2.circle(imageTransformed, (x, y), 2, (255, 0, 0), 2)
			cv2.putText(imageTransformed,str(len(dstPts)), (x+10,y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
			cv2.imshow("Warped", imageTransformed)

			if len(dstPts) > 2:
				np_srcPts = np.array(srcPts).astype(np.float32)
				np_dstPts = np.array(dstPts).astype(np.float32)

				M = cv2.getAffineTransform(np_srcPts , np_dstPts)

				warp_dst = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

				cv2.imshow('Final', warp_dst)

				imgDiff = cv2.absdiff(imageTransformed, warp_dst)
				cv2.imshow('Diff', imgDiff)

				print(M)


				print(f"X diff {M[0][2]}")
				print(f"Y diff {M[1][2]}")
				print(f"Angle  {math.degrees(math.acos(M[0][0]))}")




srcPts = []
dstPts = []

# Read the image from argv
#image = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE );
image = cv2.imread( "../images/lena.jpg", cv2.IMREAD_GRAYSCALE );
imageTransformed = cv2.imread( "./imagename_tf.jpg", cv2.IMREAD_GRAYSCALE );

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)


printImageFeatures(image)

cv2.imshow("Original", image)
cv2.imshow('Warped', imageTransformed)

cv2.setMouseCallback("Original", select_src)
cv2.setMouseCallback("Warped", select_dst)



while cv2.waitKey(1000) != 27:
    pass

