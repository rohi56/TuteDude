import cv2

video = cv2.VideoCapture('ds.mp4')

while video.isOpened():
    ret, frame = video.read()
    if not ret or frame is None:
        break
    frame = cv2.resize(frame, (800 , 720))
    cv2.imshow('Video Frame', frame)
    if cv2.waitKey(10000) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()