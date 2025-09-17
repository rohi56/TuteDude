import cv2

img = cv2.imread('eagle.jpg', 1)
print("Original Dimensions : ", img.shape)

scale = 50
width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)

dim = (width, height)
resize_img = cv2.resize(img, dim, interpolation= cv2.INTER_AREA)
print("Resized Dimensions : ", resize_img.shape)
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
