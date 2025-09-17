import cv2

img = cv2.imread('bird.jpg')
row = img.shape[0]
column = img.shape[1]
center = (column // 2, row // 2)
angle = 180

rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (column, row))

cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
