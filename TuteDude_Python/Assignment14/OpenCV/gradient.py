import cv2
import numpy as np 

img = cv2.imread('car.jpg')
img2 = cv2.resize(img, (600 , 850))

kernel = np.ones((5,5), dtype= 'uint8')

gradient = cv2.morphologyEx(img2, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Original', img)
cv2.imshow('gradient', gradient)


cv2.waitKey(0)
cv2.destroyAllWindows()