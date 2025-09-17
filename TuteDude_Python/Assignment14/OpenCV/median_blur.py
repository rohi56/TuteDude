import cv2

img = cv2.imread('eagle.jpg')
resize = cv2.resize(img, (640 , 640))

blur = cv2.medianBlur(resize, 7)

cv2.imshow('Original Image', resize)
cv2.imshow('Median Blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
