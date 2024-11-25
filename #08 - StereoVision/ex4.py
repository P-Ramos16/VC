import numpy as np
import cv2

global imgLeft, imgRight

global colors
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0),  (0, 255, 255), (0, 0, 255), (255, 0, 255)]
global color_index
color_index = 0

def mouse_handler_left(event, x, y, flags, params):

    global imgLeft, imgRight, colors, color_index
    
    if event == cv2.EVENT_LBUTTONDOWN:
        point = np.array([[x, y]], dtype=np.float32).reshape(-1, 1, 2)

        linesRight = cv2.computeCorrespondEpilines(point, 2, F)

        cv2.line(imgLeft, (0, y), (imgLeft.shape[1], y), colors[color_index], 2)
        
        for r in linesRight:
            a, b, c = r[0]
            
            x0, y0 = map(int, [0, -(a * imgRight.shape[1] + c) / b])  # y-intercept
            x1, y1 = map(int, [imgRight.shape[1], -(a * imgRight.shape[1] + c) / b])  # x-intercept

            cv2.line(imgRight, (x0, y0), (x1, y1), colors[color_index], 2)

        color_index = (color_index + 1) % len(colors)

        cv2.imshow("Image Left", imgLeft)
        cv2.imshow("Image Right", imgRight)


def mouse_handler_right(event, x, y, flags, params):

    global imgLeft, imgRight, colors, color_index
    
    if event == cv2.EVENT_LBUTTONDOWN:
        point = np.array([[x, y]], dtype=np.float32).reshape(-1, 1, 2)

        linesLeft = cv2.computeCorrespondEpilines(point, 1, F)

        cv2.line(imgRight, (0, y), (imgLeft.shape[1], y), colors[color_index], 2)

        for r in linesLeft:
            a, b, c = r[0]
            
            x0, y0 = map(int, [0, -(a * imgRight.shape[1] + c) / b])  # y-intercept
            x1, y1 = map(int, [imgLeft.shape[1], -(a * imgLeft.shape[1] + c) / b])  # x-intercept

            cv2.line(imgLeft, (x0, y0), (x1, y1), colors[color_index], 2)
        
        color_index = (color_index + 1) % len(colors)

        cv2.imshow("Image Left", imgLeft)
        cv2.imshow("Image Right", imgRight)



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

imgLeft = cv2.undistort(imgLeft, intrinsics1, distortion1)
imgRight = cv2.undistort(imgRight, intrinsics2, distortion2)

cv2.imshow("Image Left", imgLeft)
cv2.imshow("Image Right", imgRight)

cv2.setMouseCallback("Image Left", mouse_handler_left)
cv2.setMouseCallback("Image Right", mouse_handler_right)


while cv2.waitKey(33) != ord('q'):
    continue

cv2.destroyAllWindows()
