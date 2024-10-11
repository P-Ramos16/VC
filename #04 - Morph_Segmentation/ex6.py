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
image = cv2.imread("../images/lena.jpg", cv2.IMREAD_UNCHANGED)

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open")
	exit(-1)

h,w = image.shape[:2]

#mask = np.zeros((h+2,w+2), uin)
seedPoint = (430, 30)
newVal = (30,30,30)

copiedImages = []
for i in range(0, 11):
	newImage = image.copy()

	loDiff = 5 * i
	upDiff = 5 * i
	cv2.floodFill(newImage, None, seedPoint, newVal, (loDiff, upDiff))
	copiedImages.append(newImage)

# Create a vsiualization window (optional)
# CV_WINDOW_AUTOSIZE : window size will depend on image size
cv2.namedWindow( "Display window", cv2.WINDOW_AUTOSIZE )

top_image = cv2.hconcat([image, copiedImages[0], copiedImages[1], copiedImages[2]])
mid_image = cv2.hconcat([copiedImages[3], copiedImages[4], copiedImages[5], copiedImages[6]])
bot_image = cv2.hconcat([copiedImages[7], copiedImages[8], copiedImages[9], copiedImages[10]])
final_image = cv2.vconcat([top_image, mid_image, bot_image])

# Show the images
cv2.imshow( "Display window", final_image )
#  Press esc to skip
while cv2.waitKey(0) != 27:
    pass

cv2.destroyWindow( "Display window" )
