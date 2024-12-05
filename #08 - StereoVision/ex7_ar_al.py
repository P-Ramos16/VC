import numpy as np
import cv2

# Load the stereo calibration parameters
with np.load("stereoParams.npz") as data:
    left_camera_matrix = data['intrinsics1']
    left_dist_coeffs = data['distortion1']
    right_camera_matrix = data['intrinsics2']
    right_dist_coeffs = data['distortion2']
    R = data['R']  # Rotation matrix between the cameras
    T = data['T']  # Translation vector between the cameras

# Select a stereo pair of images from the calibration set
imagesl = cv2.imread('images/left01.jpg')
imagesr = cv2.imread('images/right01.jpg')

# Image size
height, width = imagesl.shape[:2]

# Initialize matrices for stereo rectification
R1 = np.zeros((3, 3))
R2 = np.zeros((3, 3))
P1 = np.zeros((3, 4))
P2 = np.zeros((3, 4))
Q = np.zeros((4, 4))

# Stereo rectification
cv2.stereoRectify(left_camera_matrix, left_dist_coeffs, right_camera_matrix, right_dist_coeffs,
                  (width, height), R, T, R1, R2, P1, P2, Q,
                  flags=cv2.CALIB_ZERO_DISPARITY, alpha=-1, newImageSize=(0, 0))

# Compute rectification maps
map1x, map1y = cv2.initUndistortRectifyMap(left_camera_matrix, left_dist_coeffs, R1, P1, (width, height), cv2.CV_32FC1)
map2x, map2y = cv2.initUndistortRectifyMap(right_camera_matrix, right_dist_coeffs, R2, P2, (width, height), cv2.CV_32FC1)

# Apply the rectification maps to the images
rectified_left = cv2.remap(imagesl, map1x, map1y, cv2.INTER_LINEAR)
rectified_right = cv2.remap(imagesr, map2x, map2y, cv2.INTER_LINEAR)

# Convert to gray scale
gray_left = cv2.cvtColor(rectified_left, cv2.COLOR_BGR2GRAY)
gray_right = cv2.cvtColor(rectified_right, cv2.COLOR_BGR2GRAY)

# Create StereoBM object and compute disparity map
stereo = cv2.StereoBM_create(numDisparities=16*5, blockSize=21)
disparity = stereo.compute(gray_left, gray_right)

# Normalize the disparity map to display it as a CV_8UC1 image
disparity = cv2.normalize(src=disparity, dst=disparity, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX)
disparity = np.uint8(disparity)

# Reproject the disparity map to 3D coordinates using Q matrix
points_3D = cv2.reprojectImageTo3D(disparity,Q)

# Save the 3D coordinates in a npz file
np.savez("3D_coordinates.npz", points_3D=points_3D)

# Display the images
cv2.imshow("Rectified Left", gray_left)
cv2.imshow("Rectified Right", gray_right)
cv2.imshow('Disparity Map', disparity)

cv2.waitKey(0)
cv2.destroyAllWindows()