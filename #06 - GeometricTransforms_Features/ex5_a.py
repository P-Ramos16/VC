import numpy as np
import cv2 as cv2
import math
 
img = cv2.imread('../images/lena.jpg', cv2.IMREAD_GRAYSCALE)
imageTransformed = cv2.imread( "./imagename_tf.jpg", cv2.IMREAD_GRAYSCALE)


 
# Initiate ORB detector
sift = cv2.SIFT_create()
 
# find the keypoints and descriptors with ORB
kp1, des1 = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(imageTransformed, None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.DescriptorMatcher_BRUTEFORCE_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)
# Remove not so good matches
numGoodMatches = int(len(matches) * 0.1)
matches = matches[:numGoodMatches]
# Draw matches
im_matches = cv2.drawMatches(img,kp1,imageTransformed,kp2,matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("matches",im_matches)
# Evaluate transform
np_srcPts = np.float32([ kp1[m.queryIdx].pt for m in matches[:3] ]).reshape(-1,1,2)
np_dstPts = np.float32([ kp2[m.trainIdx].pt for m in matches[:3] ]).reshape(-1,1,2)


M = cv2.getAffineTransform(np_srcPts, np_dstPts)

warp_dst = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow('Final', warp_dst)

imgDiff = cv2.absdiff(imageTransformed, warp_dst)
cv2.imshow('Diff', imgDiff)

print(M)


print(f"X diff {M[0][2]}")
print(f"Y diff {M[1][2]}")
print(f"Angle  {math.degrees(math.acos(M[0][0]))}")



while cv2.waitKey(1000) != 27:
    pass