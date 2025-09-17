import cv2
import numpy as np 

img = cv2.imread('car.jpg')
img2 = cv2.resize(img, (600 , 850))

kernel = np.ones((5,5), dtype= 'uint8')

opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original', img)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()