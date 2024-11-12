import numpy as np
import cv2

import numpy as np
import cv2

# Board Size
board_h = 9
board_w = 6


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
    cv2.waitKey(1)

    return ret, corners

# Read Capture
char = 0

capture = cv2.VideoCapture(0)

# 3D points of the cube corners
size = 1
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

while char != ord('q'):
    ret = False

    while not ret:
        _, img = capture.read()
        ret, corners = FindAndDisplayChessboard(img)

    with np.load('camera.npz') as data:
        intrinsics = data['intrinsics']
        distortion = data['distortion']

    selected_corners = np.vstack([corners[:4], corners[:4]])

    retval, rvec, tvec = cv2.solvePnP(cube_points, selected_corners, intrinsics, distortion)

    #  Project 3D points to 2D image points
    image_points, _ = cv2.projectPoints(cube_points, rvec, tvec, intrinsics, distortion)

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
    char = cv2.waitKey(33)

cv2.destroyAllWindows()