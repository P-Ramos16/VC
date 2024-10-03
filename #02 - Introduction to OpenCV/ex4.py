 # Aula_02_ex_04.py
 #
 # Example of visualization of an image with openCV
 #
 # Pedro Ramos

#import
import numpy as np
import cv2
import sys

# Read the image
colourImage = cv2.imread("../images/Orchid.bmp", cv2.IMREAD_UNCHANGED)

if  np.shape(colourImage) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

# Image characteristics

shapeValues = colourImage.shape

height = shapeValues[0]
width = shapeValues[1]

print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %s" % (colourImage.dtype))

greyscaleImage = cv2.cvtColor(colourImage, cv2.COLOR_BGR2GRAY)
hslImage = cv2.cvtColor(colourImage, cv2.COLOR_RGB2HLS)
xyzImage = cv2.cvtColor(colourImage, cv2.COLOR_RGB2XYZ)
hsvImage = cv2.cvtColor(colourImage, cv2.COLOR_RGB2HSV)
bgrImage = cv2.cvtColor(colourImage, cv2.COLOR_RGB2BGR)

# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

#  Convert the greyscale image to colour only to allow it to be displayed beside the original
greyscaleImage = cv2.cvtColor(greyscaleImage,cv2.COLOR_GRAY2BGR)

row1_image = cv2.hconcat([colourImage, greyscaleImage, xyzImage])
row2_image = cv2.hconcat([bgrImage, hslImage, hsvImage])

final_image = cv2.vconcat([row1_image, row2_image])

# Show the images
cv2.imshow( "Display window", final_image )
cv2.waitKey( 0 )
cv2.destroyWindow( "Display window" )
