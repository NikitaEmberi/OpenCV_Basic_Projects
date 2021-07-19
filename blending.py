#DAY 3
import cv2

image1 = cv2.imread('images/goku.jpg')
image2 = cv2.imread('images/background.jpg')
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

added_image = image1+image2
blended_image = cv2.addWeighted(image1,0.7,image2,0.3,gamma=0.1)

cv2.imshow('ADDED IMAGE',added_image)
cv2.imshow('Blended IMAGE',blended_image)

cv2.waitKey(0)
