import cv2

img = cv2.imread('im2.jpg', 1)
print("Original Dimensions : ", img.shape)
resize_img = cv2.resize(img, (1000, 1000))
cv2.imshow('Original Image', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()