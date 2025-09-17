import cv2

img = cv2.imread('random.jpg', 1)
img2 = cv2.resize(img, (800, 800))
print('Size of the image: ', img2.size)
flip_horizontally = cv2.flip(img2, 1)
flip_vertically = cv2.flip(img2, 0)
flip_horizontally_vertically = cv2.flip(img2, -1)

cv2.imshow('Original Image', img2)
cv2.imshow('Flipped Horizontally', flip_horizontally)
cv2.imshow('Flipped Vertically', flip_vertically)
cv2.imshow('Flipped Horizontally and Vertically', flip_horizontally_vertically)
cv2.waitKey(0)
cv2.destroyAllWindows()