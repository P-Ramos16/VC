 # Aula_02_ex_02.py
 #
 # Example of visualization of an image with openCV
 #
 # Pedro Ramos

#import
import numpy as np
import cv2
import sys

# Read the image
bmpImage = cv2.imread("../images/deti.bmp", cv2.IMREAD_UNCHANGED)
jpgImage = cv2.imread("../images/deti.jpg", cv2.IMREAD_UNCHANGED)

if  np.shape(bmpImage) == () or  np.shape(jpgImage) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

# Image characteristics

shapeValues = bmpImage.shape

height = shapeValues[0]
width = shapeValues[1]

print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %s" % (bmpImage.dtype))

copiedImage = bmpImage.copy()

for rowID in range(0, height):
    for columnID in range(0, width):
         for colour in range(0, shapeValues[2]):
            copiedImage[rowID][columnID][colour] -= jpgImage[rowID][columnID][colour]


# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

final_image = cv2.hconcat([bmpImage, jpgImage, copiedImage])

# Show the images
cv2.imshow( "Display window", final_image )
cv2.waitKey( 0 )
cv2.destroyWindow( "Display window" )
