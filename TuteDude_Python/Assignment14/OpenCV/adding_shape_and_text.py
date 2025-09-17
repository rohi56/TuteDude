import cv2
import numpy as np

#img = cv2.imread('bird.jpg', cv2.IMREAD_COLOR)
img = np.zeros((1000,1000,3), np.uint8)
img.fill(154)

cv2.line(img, (0,0), (150,150), (255,0,0), 15)
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)
cv2.circle(img, (400,50), 30, (0,0,255), 5)
pts_polygon = np.array([[100,50], [100,300], [500,50], [500,300]], np.int32)
cv2.polylines(img, [pts_polygon], True, (0,255,255), 3)
cv2.putText(img, 'Hello OpenCV', (300,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 5, cv2.LINE_AA)

cv2.imshow('Image with shapes and text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()