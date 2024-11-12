import numpy as np
import cv2

import numpy as np
import cv2

# Board Size
board_h = 9
board_w = 6


def getAruCOMarker(image):
    # Find the chess board corners
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()

    # Create the ArUco detector
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    # Detect the markers
    corners, ids, rejected = detector.detectMarkers(gray)
    # Print the detected markers
    print("Detected markers:", ids)
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(image, corners, ids)

    return ids is not None, image, corners


size = 1
cube_points = np.array([
    [0, 0],
    [size, 0],
    [size, size],
    [0, size],
], dtype=np.float32)

# Read Capture
char = 0
capture = cv2.VideoCapture(0)

while char != ord('q'):
    ret = False

    while not ret:
        _, img = capture.read()
        ret, img, corners = getAruCOMarker(img)

    with np.load('camera.npz') as data:
        intrinsics = data['intrinsics']
        distortion = data['distortion']

    print((corners[0]))
    image_points = np.array(corners[0], dtype=np.float32).reshape(-1, 2)

    retval, rvec, tvec = cv2.solvePnP(cube_points, image_points, intrinsics, distortion)

    print(f"Rvec: {rvec}")
    print(f"Tvec: {tvec}")

    #  Display the image with the projected cube
    cv2.imshow('Projected Square', img)
    char = cv2.waitKey(33)

cv2.destroyAllWindows()