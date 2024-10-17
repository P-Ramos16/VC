 # Aula_02_ex_01.py
 #
 # Example of visualization of an image with openCV
 #
 # Pedro Ramos

#import
import numpy as np
import cv2
import sys

def mouse_handler(event, x, y, flags, params):

	seedPoint = (x, y)
	newVal = (125,125,125)
	loDiff = 15
	upDiff = 15

	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.floodFill(image, None, seedPoint, newVal, (loDiff, upDiff))
		cv2.imshow("Display window", image)


# Read the image			lena.jpg
image = cv2.imread("../images/tools_2.png", cv2.IMREAD_UNCHANGED)

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow("Display window", cv2.WINDOW_AUTOSIZE )

cv2.setMouseCallback("Display window", mouse_handler)

# Show the images
cv2.imshow( "Display window", image )
#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass

cv2.destroyWindow( "Display window" )
