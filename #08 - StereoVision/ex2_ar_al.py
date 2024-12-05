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
imgpoints = [] # 2d points in image plane.


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
lpoints = [] # 2d points in image plane.
rpoints = []

# Read images
imagesl = sorted(glob.glob('images//left*.jpg'))
imagesr = sorted(glob.glob('images//right*.jpg'))

for fname in imagesl:
    img = cv2.imread(fname)
    ret, lcorners = FindAndDisplayChessboard(img)
    if ret == True:
        objpoints.append(objp)
        lpoints.append(lcorners)

for fname in imagesr:
    img = cv2.imread(fname)
    ret, rcorners = FindAndDisplayChessboard(img)
    if ret == True:
        rpoints.append(rcorners)


image_size = (img.shape[1], img.shape[0])

# Perform stereo calibration
ret, left_camera_matrix, left_dist_coeffs, right_camera_matrix, right_dist_coeffs, R, T, E, F = cv2.stereoCalibrate(
    objpoints, lpoints, rpoints, None, None, 
    None, None,image_size,flags=cv2.CALIB_SAME_FOCAL_LENGTH)

print("Stereo calibration result:", ret)
print("Left camera matrix:\n", left_camera_matrix)
print("Right camera matrix:\n", right_camera_matrix)
print("Rotation matrix:\n", R)
print("Translation vector:\n", T)

np.savez("stereoParams.npz",
         intrinsics1=left_camera_matrix,
         distortion1=left_dist_coeffs,
         intrinsics2=right_camera_matrix,
         distortion2=right_dist_coeffs,
         R=R, T=T, E=E, F=F)

cv2.waitKey(-1)
cv2.destroyAllWindows()