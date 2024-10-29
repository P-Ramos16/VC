import numpy as np
import cv2 as cv2
 
img = cv2.imread('../images/lena.jpg')
imageTransformed = cv2.imread( "./imagename_tf.jpg", cv2.IMREAD_GRAYSCALE );

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(imageTransformed, None)
 
img=cv2.drawKeypoints(img,kp1,img)
imageTransformed=cv2.drawKeypoints(imageTransformed,kp2,imageTransformed)
 
cv2.imshow('Image', img)
cv2.imshow('Image Transformed', imageTransformed)



while cv2.waitKey(1000) != 27:
    pass

