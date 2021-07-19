import cv2
import numpy as np

image = cv2.imread('images/goku.jpg')
height,width,channels = image.shape
#Matrix
M = np.float32([[1,0,50],[0,1,50]]) 
# 👆 push top right to 50 pixel right and bottom by 50
# [[ 0.  1. 50.]
#  [ 1.  0. 50.]]

rotation_matrix = cv2.getRotationMatrix2D((height/2,width/2),90,1)

translated_image = cv2.warpAffine(image,M,(height,width)) #AX+B
rotated_image = cv2.warpAffine(image,rotation_matrix,(height,width))
scaled_image = cv2.resize(image,None,fx=1,fy=2) #double the height with same width

cv2.imshow("Image",image)
#TO CROP
# cv2.imshow("Image",image[:100])
cv2.imshow("Translated Image",translated_image)
cv2.imshow("Rotated Image",rotated_image)
cv2.imshow("Scaled Image",scaled_image)

cv2.waitKey(0)
