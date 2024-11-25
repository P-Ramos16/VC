import numpy as np
import cv2

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

undistortedImageLeft = cv2.undistort(imgLeft, intrinsics1, distortion1)
undistortedImageRight = cv2.undistort(imgRight, intrinsics2, distortion2)

finalImageLeft = cv2.hconcat([imgLeft, undistortedImageLeft])
finalImageRight = cv2.hconcat([imgRight, undistortedImageRight])

cv2.imshow("Image Left", finalImageLeft)

cv2.imshow("Image Right", finalImageRight)

while cv2.waitKey(33) != ord('q'):
    continue

cv2.destroyAllWindows()
