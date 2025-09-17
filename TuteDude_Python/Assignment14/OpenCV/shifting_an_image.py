import cv2
import numpy as np

img = cv2.imread('bird.jpg')
column = img.shape[1]
row = img.shape[0]

transition_matrix = np.float32([[1, 0, 100], [0, 1, 50]])

shifted_img = cv2.warpAffine(img, transition_matrix, (column, row))

cv2.imshow('Original', img)
cv2.imshow('Shifted', shifted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()