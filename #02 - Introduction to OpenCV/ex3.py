 # Aula_02_ex_03.py
 #
 # Example of visualization of an image with openCV
 #
 # Pedro Ramos

#import
import numpy as np
import cv2
import sys

def mouse_handler(event, x, y, flags, params):

    color = [255, 25, 100]
    thickness = 3
    radius = 12

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), radius, color, thickness)
        cv2.imshow("Display window", image)  


# Read the image
image = cv2.imread("../images/deti.bmp", cv2.IMREAD_UNCHANGED)

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

# Image characteristics

shapeValues = image.shape

height = shapeValues[0]
width = shapeValues[1]

print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %s" % (image.dtype))


# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

cv2.setMouseCallback("Display window", mouse_handler)

# Show the images
cv2.imshow( "Display window", image )
cv2.waitKey( 0 )
cv2.destroyWindow( "Display window" )