import cv2

img = cv2.imread('eagle.jpg')
resize = cv2.resize(img, (640 , 640))
blur = cv2.GaussianBlur(resize, (7,7), 0)

cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()