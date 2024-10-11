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
circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(22,22))
#  Dilate the image 
dilatedImage1 = cv2.dilate(copiedImage4, circularKernel, iterations=1)
closedImage1 = cv2.erode(dilatedImage1, circularKernel, iterations=1)

circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13))
#  Dilate the image 
dilatedImage2 = cv2.dilate(copiedImage4, circularKernel, iterations=1)
closedImage2 = cv2.erode(dilatedImage2, circularKernel, iterations=1)


circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#  Dilate the image 
dilatedImage3 = cv2.dilate(copiedImage4, circularKernel, iterations=1)
closedImage3 = cv2.erode(dilatedImage3, circularKernel, iterations=1)

# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

top_image = cv2.hconcat([image4, closedImage1])
bot_image = cv2.hconcat([closedImage2, closedImage3])
final_image = cv2.vconcat([top_image, bot_image])

# Show the images
cv2.imshow( "Display window", final_image )
#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass

cv2.destroyWindow( "Display window" )
