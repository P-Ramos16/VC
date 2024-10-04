# Aula_02_ex_03.py
#
# Historam visualization with openCV
#
# Paulo Dias

# Results:
#
# Img 1: Good
# Img 2: Very Overexposed
# Img 3: Overexposed
# Img 4: Good
# Img 5: Very low colour space
# Img 6: Low colour space

#import
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the image from argv
# image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED );
image1 = cv2.imread( "../images/ireland-06-01.tif", cv2.IMREAD_UNCHANGED );
image2 = cv2.imread( "../images/ireland-06-02.tif", cv2.IMREAD_UNCHANGED );
image3 = cv2.imread( "../images/ireland-06-03.tif", cv2.IMREAD_UNCHANGED );
image4 = cv2.imread( "../images/ireland-06-04.tif", cv2.IMREAD_UNCHANGED );
image5 = cv2.imread( "../images/ireland-06-05.tif", cv2.IMREAD_UNCHANGED );
image6 = cv2.imread( "../images/ireland-06-06.tif", cv2.IMREAD_UNCHANGED );

if np.shape(image1) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len(image1.shape) > 2:
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)

# print some features
height, width = image1.shape
nchannels = 1
print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %d" % nchannels)
print("Number of elements : %d" % image1.size)

print("Image Size: (%d,%d)" % (height, width))

# SizehistImageWidth, 
histSize = 255	 # from 0 to 255
# Intensity Range
histRange = [0, 255]

#  If both are changed to, for example, 512, a lot of zero values appear 
# on the right of the histogram


# Compute the histogram
hist_item1 = cv2.calcHist([image1], [0], None, [histSize], histRange)
hist_item2 = cv2.calcHist([image2], [0], None, [histSize], histRange)
hist_item3 = cv2.calcHist([image3], [0], None, [histSize], histRange)
hist_item4 = cv2.calcHist([image4], [0], None, [histSize], histRange)
hist_item5 = cv2.calcHist([image5], [0], None, [histSize], histRange)
hist_item6 = cv2.calcHist([image6], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
color = (125)
histImage1 = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histImage2 = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histImage3 = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histImage4 = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histImage5 = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histImage6 = np.zeros((histImageWidth,histImageHeight,1), np.uint8)

# Width of each histogram bar
binWidth = int(np.ceil(histImageWidth*1.0 / histSize))

# Normalize values to [0, histImageHeight]
cv2.normalize(hist_item1, hist_item1, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item2, hist_item2, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item3, hist_item3, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item4, hist_item4, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item5, hist_item5, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item6, hist_item6, 0, histImageHeight, cv2.NORM_MINMAX)

# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(histImage1,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item1[i]) ), (125), -1)
	cv2.rectangle(histImage2,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item2[i]) ), (125), -1)
	cv2.rectangle(histImage3,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item3[i]) ), (125), -1)
	cv2.rectangle(histImage4,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item4[i]) ), (125), -1)
	cv2.rectangle(histImage5,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item5[i]) ), (125), -1)
	cv2.rectangle(histImage6,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item6[i]) ), (125), -1)

# ATTENTION : Y coordinate upside down
histImage1 = np.flipud(histImage1)
histImage2 = np.flipud(histImage2)
histImage3 = np.flipud(histImage3)
histImage4 = np.flipud(histImage4)
histImage5 = np.flipud(histImage5)
histImage6 = np.flipud(histImage6)


cv2.namedWindow("Colour Hist")
cv2.namedWindow("Original Image")

hist_image = cv2.hconcat([histImage1, histImage2, histImage3])
original_image = cv2.hconcat([image1, image2, image2])

cv2.imshow('Colour Hist', hist_image)
cv2.imshow('Original Image', original_image)


#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass


hist_image = cv2.hconcat([histImage4, histImage5, histImage6])
original_image = cv2.hconcat([image4, image5, image6])

cv2.imshow('Colour Hist', hist_image)
cv2.imshow('Original Image', original_image)

#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass