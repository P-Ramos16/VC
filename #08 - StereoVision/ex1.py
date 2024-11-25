 # Cheesboard.py
 #
 # Chessboard Calibration
 #
 # Paulo Dias

import numpy as np
import cv2
import glob

# Board Size
board_h = 9
board_w = 6

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgCorners = [] # 2d points in image plane.


def  FindAndDisplayChessboard(img):
    # Find the chess board corners
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (board_w,board_h),None)

    # If found, display image with corners
    if ret == True:
        img = cv2.drawChessboardCorners(img, (board_w, board_h), corners, ret)
        cv2.imshow('img',img)
        cv2.waitKey(125)

    return ret, corners

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((board_w*board_h,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgCornersLeft = [] # 2d points in image plane.
imgCornersRight = [] # 2d points in image plane.

# Read images
imagesLeft = sorted(glob.glob('..//images//left*.jpg'))
imagesRight = sorted(glob.glob('..//images//right*.jpg'))

for imageIndex in range(len(imagesLeft)):

    imageLeft = imagesLeft[imageIndex]
    imageRight = imagesRight[imageIndex]

    img = cv2.imread(imageLeft)
    ret, corners = FindAndDisplayChessboard(img)
    if ret == True:
        objpoints.append(objp)
        imgCornersLeft.append(corners)

    img = cv2.imread(imageRight)
    ret, corners = FindAndDisplayChessboard(img)
    if ret == True:
        objpoints.append(objp)
        imgCornersRight.append(corners)

print(f"Image corners on the left: {imgCornersLeft}")
print(f"Image corners on the right: {imgCornersRight}")
print(f"Image points: {objpoints}")

cv2.waitKey(-1)
cv2.destroyAllWindows()