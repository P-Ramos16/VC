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
image4 = cv2.imread("../images/art4.bmp", cv2.IMREAD_UNCHANGED)

if  np.shape(image4) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

copiedImage4 = image4.copy()


#  Define the Kernels
circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
#  Dilate the image 
erodedImage3 = cv2.erode(copiedImage4, circularKernel, iterations=1)
openImage1 = cv2.dilate(erodedImage3, circularKernel, iterations=1)

circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#  Dilate the image 
erodedImage3 = cv2.erode(copiedImage4, circularKernel, iterations=1)
openImage2 = cv2.dilate(erodedImage3, circularKernel, iterations=1)


circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
#  Dilate the image 
erodedImage3 = cv2.erode(copiedImage4, circularKernel, iterations=1)
openImage3 = cv2.dilate(erodedImage3, circularKernel, iterations=1)

# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

top_image = cv2.hconcat([image4, openImage1])
bot_image = cv2.hconcat([openImage2, openImage2])
final_image = cv2.vconcat([top_image, bot_image])

# Show the images
cv2.imshow( "Display window", final_image )
#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass

cv2.destroyWindow( "Display window" )
