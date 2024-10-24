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
image = cv2.imread( "../images/lena.jpg", cv2.IMREAD_UNCHANGED );

<<<<<<<< HEAD:#03 - Low Level Image Processing I/ex2.py
if np.shape(image) == ():
========
if  np.shape(image) == ():
>>>>>>>> upstream/master:#03 - Low Level Image Processing I/Aula_03_ex_03.py
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
<<<<<<<< HEAD:#03 - Low Level Image Processing I/ex2.py
if len(image.shape) > 2:
========
if len (image.shape) > 2:
>>>>>>>> upstream/master:#03 - Low Level Image Processing I/Aula_03_ex_03.py
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)

# Display the image
cv2.namedWindow("Original Image")
cv2.imshow("Original Image", image)

# print some features
height, width = image.shape
nchannels = 1
print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %d" % nchannels)
print("Number of elements : %d" % image.size)

print("Image Size: (%d,%d)" % (height, width))

<<<<<<<< HEAD:#03 - Low Level Image Processing I/ex2.py
# SizehistImageWidth, 
histSize = 255	 # from 0 to 255
# Intensity Range
histRange = [0, 255]

#  If both are changed to, for example, 512, a lot of zero values appear 
# on the right of the histogram

========
# Size
histSize = 256	 # from 0 to 255
# Intensity Range
histRange = [0, 256]
>>>>>>>> upstream/master:#03 - Low Level Image Processing I/Aula_03_ex_03.py

# Compute the histogram
hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)

##########################################
# Drawing with openCV
# Create an image to display the histogram
histImageWidth = 512
histImageHeight = 512
color = (125)
histImage = np.zeros((histImageWidth,histImageHeight,1), np.uint8)

# Width of each histogram bar
<<<<<<<< HEAD:#03 - Low Level Image Processing I/ex2.py
binWidth = int(np.ceil(histImageWidth*1.0 / histSize))
========
binWidth = int (np.ceil(histImageWidth*1.0 / histSize))
>>>>>>>> upstream/master:#03 - Low Level Image Processing I/Aula_03_ex_03.py

# Normalize values to [0, histImageHeight]
cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)

# Draw the bars of the nomrmalized histogram
for i in range (histSize):
	cv2.rectangle(histImage,  ( i * binWidth, 0 ), ( ( i + 1 ) * binWidth, int(hist_item[i]) ), (125), -1)

# ATTENTION : Y coordinate upside down
histImage = np.flipud(histImage)

cv2.imshow('colorhist', histImage)
cv2.waitKey(0)

##########################
# Drawing using matplotlib
plt.plot(hist_item,'r')
plt.xlim(histRange)
plt.show()




