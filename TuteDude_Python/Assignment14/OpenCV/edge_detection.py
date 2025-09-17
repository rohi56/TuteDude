import cv2
import numpy as np

img = cv2.imread('eagle.jpg', 0)
resize = cv2.resize(img, (520 , 520))
min_Thresh = 100
max_Thresh = 200

edges = cv2.Canny(resize, min_Thresh, max_Thresh)

cv2.imshow('Original Image', resize)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()