 # Aula_01_ex_02.py
 #
 # Chessboard Calibration
 #
 # Paulo Dias

import numpy as np
import cv2

# Board Size
board_h = 9
board_w = 6

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


def FindAndDisplayChessboard(img):
    # Find the chess board corners
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (board_w,board_h),None)

    # If found, display image with corners
    if ret == True:

        criteria = (cv2.TermCriteria_EPS+cv2.TermCriteria_MAX_ITER, 30, 0.001)
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        img = cv2.drawChessboardCorners(gray, (board_w, board_h), corners, ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)
    else:
        cv2.imshow('img',img)
        cv2.waitKey(500)

    return ret, corners

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((board_w*board_h,3), np.float32)
objp[:,:2] = np.mgrid[0:board_w,0:board_h].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Read Capture
capture = cv2.VideoCapture(0)

for _ in range(0, 10):
    _, frame = capture.read()
    ret, corners = FindAndDisplayChessboard(frame)
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

ret, intrinsics, distortion, rvecs, tvecs = cv2.calibrateCamera( 
                                                objpoints, imgpoints,
                                                (640, 480), None, None
                                            ) 


print("Intrinsics: ")
print (intrinsics)
print("Distortion: ")
print(distortion)
for i in range(len(tvecs)):
    print ("\nTranslations(%d) : " % i )
    print(tvecs[0])
    print ("Rotation(%d) : " % i )
    print(rvecs[0])

np.savez('camera.npz', intrinsics=intrinsics, distortion=distortion )

img = frame

# 3D points of the cube corners
size = 5
cube_points = np.array([
    [0, 0, 0],
    [size, 0, 0],
    [size, size, 0],
    [0, size, 0],
    [0, 0, size],
    [size, 0, size],
    [size, size, size],
    [0, size, size]
], dtype=np.float32)

#  Connect the cube edges (use the indices to connect the points)
lines = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]


#  Project 3D points to 2D image points
image_points, _ = cv2.projectPoints(cube_points, rvecs[-1], tvecs[-1], intrinsics, distortion)

#  Convert to integer coordinates
image_points = np.int32(image_points).reshape(-1, 2)

#  Draw the projected cube
for i, point in enumerate(image_points):
    cv2.circle(img, tuple(point), 5, (0, 0, 255), -1)

for line in lines:
    pt1 = tuple(image_points[line[0]])
    pt2 = tuple(image_points[line[1]])
    #  Draw cube edges in blue
    cv2.line(img, pt1, pt2, (200, 255, 0), 2)

#  Display the image with the projected cube
cv2.imshow('Projected Cube', img)
cv2.waitKey(0)
cv2.destroyAllWindows()