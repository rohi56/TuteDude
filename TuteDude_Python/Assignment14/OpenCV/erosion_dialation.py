import cv2
import numpy as np 

img = cv2.imread('car.jpg')
img2 = cv2.resize(img, (600 , 850))

kernel = np.ones((5,5), dtype= 'uint8')

erosion = cv2.erode(img2, kernel, iterations= 1)
dilation = cv2.dilate(img2, kernel, iterations=1)

cv2.imshow('Original', img)
cv2.imshow('erosion', erosion)
cv2.imshow('dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()