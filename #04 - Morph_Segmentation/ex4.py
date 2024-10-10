 # Aula_02_ex_01.py
 #
 # Example of visualization of an image with openCV
 #
 # Pedro Ramos

#import
import numpy as np
import cv2
import sys

# Read the image
image2 = cv2.imread("../images/art2.bmp", cv2.IMREAD_UNCHANGED)
image3 = cv2.imread("../images/art3.bmp", cv2.IMREAD_UNCHANGED)

if  np.shape(image2) == () or np.shape(image3) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

copiedImage2 = image2.copy()
copiedImage3 = image3.copy()


#  Define the Kernels
circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
#  Dilate the image 
erodedImage3 = cv2.erode(copiedImage3, circularKernel, iterations=1)
openImage3 = cv2.dilate(erodedImage3, circularKernel, iterations=1)

#  Define the Kernels
sqrKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,9))
#  Dilate the image 
erodedImage2 = cv2.erode(copiedImage2, sqrKernel, iterations=1)
openImage2 = cv2.dilate(erodedImage2, sqrKernel, iterations=1)

#  Define the Kernels
sqrKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))
#  Dilate the image 
erodedImage2 = cv2.erode(copiedImage2, sqrKernel, iterations=1)
openImage22 = cv2.dilate(erodedImage2, sqrKernel, iterations=1)

# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window 2", cv2.WINDOW_AUTOSIZE )
cv2.namedWindow( "Display window 3", cv2.WINDOW_AUTOSIZE )
cv2.namedWindow( "Display window 22", cv2.WINDOW_AUTOSIZE )

top_image = cv2.hconcat([image3, openImage3])
bot_image = cv2.hconcat([image2, openImage2])
bot_image2 = cv2.hconcat([image2, openImage22])

# Show the images
cv2.imshow( "Display window 3", top_image )
cv2.imshow( "Display window 2", bot_image )
cv2.imshow( "Display window 22", bot_image2 )
#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass

cv2.destroyWindow( "Display window 2" )
cv2.destroyWindow( "Display window 3" )
cv2.destroyWindow( "Display window 22" )
