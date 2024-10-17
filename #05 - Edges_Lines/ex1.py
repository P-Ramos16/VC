 # Aula_05_ex_01.py
 #
 # Example of visualization of an image with openCV
 #
 # Pedro Ramos

#import
import numpy as np
import cv2
import sys

# Read the image
image = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)

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


copiedImg = image.copy()

ret, binImage =       cv2.threshold(copiedImg, 127, 255, cv2.THRESH_BINARY)
ret, binInvImage =    cv2.threshold(copiedImg, 127, 255, cv2.THRESH_BINARY_INV)
ret, truncImage =     cv2.threshold(copiedImg, 127, 255, cv2.THRESH_TRUNC)
ret, toZeroImage =    cv2.threshold(copiedImg, 127, 255, cv2.THRESH_TOZERO)
ret, toZeroInvImage = cv2.threshold(copiedImg, 127, 255, cv2.THRESH_TOZERO_INV)




# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

top_image = cv2.hconcat([image, binImage, binInvImage])
bot_image = cv2.hconcat([truncImage, toZeroImage, toZeroInvImage])

final_image = cv2.vconcat([top_image, bot_image])


# Show the images
cv2.imshow( "Display window", final_image )

cv2.waitKey( 0 )
cv2.destroyWindow( "Display window" )
