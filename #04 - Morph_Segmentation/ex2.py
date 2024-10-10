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
        if copiedImage[rowID][columnID] < 120:
            copiedImage[rowID][columnID] = 255
        else:
            copiedImage[rowID][columnID] = 0



#  Define the Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

#  Dilate the image 
dilatedImages = [] 
  

for val in range(0, 5):
    #  Dilate the image 
    dilatedImages.append(cv2.erode(copiedImage, kernel, iterations=val))


# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

top_image = cv2.hconcat([image, dilatedImages[0], dilatedImages[1]])
bot_image = cv2.hconcat([dilatedImages[2], dilatedImages[3], dilatedImages[4]])

final_image = cv2.vconcat([top_image, bot_image])

# Show the images
cv2.imshow( "Display window", final_image )
#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass

cv2.destroyWindow( "Display window" )
