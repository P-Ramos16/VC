# Aula_02_ex_04.py
#
# Historam visualization with openCV
#
# Paulo Dias

#import
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


def calcIntensity(original, min, max):
    return (original - min) / (max - min)


# Read the image from argv
# image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED );
originalimage = cv2.imread( "../images/DETI_greyscale.png", cv2.IMREAD_UNCHANGED );

if np.shape(originalimage) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len(originalimage.shape) > 2:
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)

# print some features
height, width = originalimage.shape
nchannels = 1
print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %d" % nchannels)
print("Number of elements : %d" % originalimage.size)

print("Image Size: (%d,%d)" % (height, width))


##########################################
#  Create the Contrast Stretched image
##########################################


conStretchedImage = originalimage.copy()

(min, max, _, _) = cv2.minMaxLoc(conStretchedImage)

for rowID in range(0, height):
    for columnID in range(0, width):
        conStretchedImage[rowID][columnID] = calcIntensity(originalimage[rowID][columnID], min, max) * 255



# SizehistImageWidth, 
histSize = 255	 # from 0 to 255
# Intensity Range
histRange = [0, 255]

#  If both are changed to, for example, 512, a lot of zero values appear 
# on the right of the histogram


# Compute the histogram
hist_item1 = cv2.calcHist([originalimage], [0], None, [histSize], histRange)
hist_item2 = cv2.calcHist([conStretchedImage], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
color = (125)
histOriginalImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)
histconStretchedImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)

# Width of each histogram bar
binWidth = int(np.ceil(histImageWidth*1.0 / histSize))

# Normalize values to [0, histImageHeight]
cv2.normalize(hist_item1, hist_item1, 0, histImageHeight, cv2.NORM_MINMAX)
cv2.normalize(hist_item2, hist_item2, 0, histImageHeight, cv2.NORM_MINMAX)

# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(histOriginalImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item1[i]) ), (125), -1)
	cv2.rectangle(histconStretchedImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item2[i]) ), (125), -1)

# ATTENTION : Y coordinate upside down
histOriginalImage = np.flipud(histOriginalImage)
histconStretchedImage = np.flipud(histconStretchedImage)


cv2.namedWindow("Colour Hist")
cv2.namedWindow("Original Image")

hist_image = cv2.hconcat([histOriginalImage, histconStretchedImage])
original_image = cv2.hconcat([originalimage, conStretchedImage])

cv2.imshow('Colour Hist', hist_image)
cv2.imshow('Original Image', original_image)


#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass