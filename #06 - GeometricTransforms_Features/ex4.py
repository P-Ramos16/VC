import numpy as np
import cv2 as cv2
 
img = cv2.imread('../images/lena.jpg', cv2.IMREAD_GRAYSCALE)
imageTransformed = cv2.imread( "./imagename_tf.jpg", cv2.IMREAD_GRAYSCALE)


 
# Initiate ORB detector
orb = cv2.ORB_create()
 
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img,None)
kp2, des2 = orb.detectAndCompute(imageTransformed,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.DescriptorMatcher_BRUTEFORCE, crossCheck=True)
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
src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)




while cv2.waitKey(1000) != 27:
    pass

