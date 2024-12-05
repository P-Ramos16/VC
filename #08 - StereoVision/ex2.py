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
        cv2.waitKey(100)

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

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-3)
left_pts, right_pts = [], []
img_size = None

for imageIndex in range(len(imagesLeft)):

    imgLeft = cv2.imread(imagesLeft[imageIndex])
    imgRight = cv2.imread(imagesRight[imageIndex])

    if img_size is None:
        img_size = (imgLeft.shape[1], imgLeft.shape[0])

    retLeft, cornersLeft = FindAndDisplayChessboard(imgLeft)
    retRight, cornersRight = FindAndDisplayChessboard(imgRight)

    if retLeft and retRight:
        objpoints.append(objp)
        imgCornersLeft.append(cornersLeft)
        imgCornersRight.append(cornersRight)

flags = cv2.CALIB_USE_INTRINSIC_GUESS + cv2.CALIB_FIX_INTRINSIC

(retval, intrinsics1, distortion1,
 intrinsics2, distortion2, R, 
 T, E, F)                       = cv2.stereoCalibrate(objpoints, imgCornersLeft, imgCornersRight,
                                                      None, None,
                                                      None, None, img_size, flags=cv2.CALIB_SAME_FOCAL_LENGTH)

if retval:
    print('Left camera:')
    print(intrinsics1)
    print('Left camera distortion:')
    print(distortion1)
    print('Right camera:')
    print(intrinsics2)
    print('Right camera distortion:')
    print(distortion2)
    print('Rotation matrix:')
    print(R)
    print('Translation:')
    print(T)

    np.savez('stereoParams.npz', **{'intrinsics1': intrinsics1, 
                           'distortion1': distortion1, 
                           'intrinsics2': intrinsics2,
                           'distortion2': distortion2,
                           'R': R, 'T': T, 'E': E, 'F': F})

else:
    print("An error occured on the stereo calibration")

cv2.waitKey(-1)
cv2.destroyAllWindows()