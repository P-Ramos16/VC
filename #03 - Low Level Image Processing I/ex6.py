# Aula_02_ex_03.py
#
# Historam visualization with openCV
#
# Paulo Dias


#import
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the image from argv
# image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED );
originalImage = cv2.imread( "../images/Fruits-RGB.tif", cv2.IMREAD_UNCHANGED );

if np.shape(originalImage) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len(originalImage.shape) < 3:
	print ("The loaded image is NOT a RGB-LEVEL image !")
	exit(-1)

# print some features
height, width, _ = originalImage.shape
nchannels = 1
print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %d" % nchannels)
print("Number of elements : %d" % originalImage.size)

print("Image Size: (%d,%d)" % (height, width))

# SizehistImageWidth, 
histSize = 255	 # from 0 to 255
# Intensity Range
histRange = [0, 255]

imageBlue, imageGreen, imageRed = cv2.split(originalImage)


# Compute the histogram
hist_item1 = cv2.calcHist([originalImage], [0], None, [histSize], histRange)
hist_item2 = cv2.calcHist([imageRed], [0], None, [histSize], histRange)
hist_item3 = cv2.calcHist([imageGreen], [0], None, [histSize], histRange)
hist_item4 = cv2.calcHist([imageBlue], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
color = (125)
historiginalImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histimageRed = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histimageGreen = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histimageBlue = np.zeros((histImageWidth,histImageHeight,1), np.uint8)

# Width of each histogram bar
binWidth = int(np.ceil(histImageWidth*1.0 / histSize))

# Normalize values to [0, histImageHeight]
cv2.normalize(hist_item1, hist_item1, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item2, hist_item2, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item3, hist_item3, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item4, hist_item4, 0, histImageHeight, cv2.NORM_MINMAX)

# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(historiginalImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item1[i]) ), (125), -1)
	cv2.rectangle(histimageRed,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item2[i]) ), (125), -1)
	cv2.rectangle(histimageGreen,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item3[i]) ), (125), -1)
	cv2.rectangle(histimageBlue,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item4[i]) ), (125), -1)

# ATTENTION : Y coordinate upside down
historiginalImage = np.flipud(historiginalImage)
histimageRed = np.flipud(histimageRed)
histimageGreen = np.flipud(histimageGreen)
histimageBlue = np.flipud(histimageBlue)


cv2.namedWindow("Colour Hist")
cv2.namedWindow("Original Image")


hist_image = cv2.hconcat([histimageRed, histimageGreen, histimageBlue])
original_image = cv2.hconcat([imageRed, imageGreen, imageBlue])

cv2.imshow('Colour Hist', hist_image)
cv2.imshow('Original Image', original_image)

#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass