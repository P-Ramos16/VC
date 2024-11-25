import numpy as np
import cv2

colors = [(255, 0, 0), (255, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255)]
color_index = 0


def mouse_handler(event, x, y, flags, params):

    global imgLeftRectified, imgRightRectified, colors, color_index
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.line(imgLeftRectified, (0, y), (imgLeftRectified.shape[1], y), colors[color_index], 2)
        cv2.line(imgRightRectified, (0, y), (imgRightRectified.shape[1], y), colors[color_index], 2)

        color_index = (color_index + 1) % len(colors)
        
        cv2.imshow("Image Left", imgLeftRectified)
        cv2.imshow("Image Right", imgRightRectified)

with np.load('stereoParams.npz') as data:

    intrinsics1 = data['intrinsics1']
    distortion1 = data['distortion1']
    intrinsics2 = data['intrinsics2']
    distortion2 = data['distortion2']

    R = data['R']
    T = data['T']
    E = data['E']
    F = data['F']

imgLeft = cv2.imread('../images/left04.jpg')
imgRight = cv2.imread('../images/right04.jpg')

finalOriginal = cv2.hconcat([imgLeft, imgRight])

height, width, _ = imgLeft.shape

R1 = np.zeros(shape=(3,3))
R2 = np.zeros(shape=(3,3))
P1 = np.zeros(shape=(3,4))
P2 = np.zeros(shape=(3,4))
Q = np.zeros(shape=(4,4))

cv2.stereoRectify(intrinsics1, distortion1, intrinsics2, distortion2 ,(width, height), 
                  R, T, R1, R2, P1, P2, Q, flags=cv2.CALIB_ZERO_DISPARITY, 
                  alpha=-1, newImageSize=(0,0))

map1x, map1y = cv2.initUndistortRectifyMap(intrinsics1, distortion1, R1, P1, (width, height), cv2.CV_32FC1)
map2x, map2y = cv2.initUndistortRectifyMap(intrinsics2, distortion2, R2, P2, (width, height), cv2.CV_32FC1)

imgLeftRectified = cv2.remap(imgLeft, map1x, map1y, cv2.INTER_LINEAR)
imgRightRectified = cv2.remap(imgRight, map2x, map2y, cv2.INTER_LINEAR)

for y in range(0, height, 25):
    cv2.line(imgLeftRectified, (0, y), (width, y), (0, 255, 0), 2)
    cv2.line(imgRightRectified, (0, y), (width, y), (0, 255, 0), 2)


cv2.imshow("Original Images", finalOriginal)
cv2.imshow("Image Left", imgLeftRectified)
cv2.imshow("Image Right", imgRightRectified)

cv2.setMouseCallback("Image Left", mouse_handler)
cv2.setMouseCallback("Image Right", mouse_handler)

while cv2.waitKey(33) != ord('q'):
    continue

cv2.destroyAllWindows()
