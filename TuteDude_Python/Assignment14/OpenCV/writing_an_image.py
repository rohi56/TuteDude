import cv2

img = cv2.imread('im2.jpg', 0)
cv2.imshow('Original Image', img)
cv2.imwrite('im2_gray.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

