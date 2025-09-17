import cv2

img = cv2.imread('eagle.jpg')

resize = cv2.resize(img, (520 , 520))
d = 7
sigmaColor = 255
sigmaSpace = 100

blur = cv2.bilateralFilter(resize, d, sigmaColor, sigmaSpace)
cv2.imshow('Original Image', resize)
cv2.imshow('Bilateral Filter', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()