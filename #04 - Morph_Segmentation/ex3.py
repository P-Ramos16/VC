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


copiedImage = image.copy()

for rowID in range(0, height):
    for columnID in range(0, width):
        if copiedImage[rowID][columnID] < 90:
            copiedImage[rowID][columnID] = 255
        else:
            copiedImage[rowID][columnID] = 0



#  Define the Kernels
circularKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
squareKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

#  Dilate the image 
circErodedImage = cv2.erode(copiedImage, circularKernel, iterations=2)
#  Dilate the image 
sqrErodedImage = cv2.erode(copiedImage, squareKernel, iterations=2)


# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

top_image = cv2.hconcat([image, image])
bot_image = cv2.hconcat([circErodedImage, sqrErodedImage])

final_image = cv2.vconcat([top_image, bot_image])

# Show the images
cv2.imshow( "Display window", final_image )
#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass

cv2.destroyWindow( "Display window" )
