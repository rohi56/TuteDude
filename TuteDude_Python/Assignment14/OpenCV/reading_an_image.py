import cv2

img = cv2.imread('im2.jpg', 1)
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()