import cv2

video = cv2.VideoCapture('ds.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (1920, 1080))

while video.isOpened():
    ret, frame = video.read()
    if ret:
            frame_resized = cv2.resize(frame, (1920, 1080))
            out.write(frame_resized)
            cv2.imshow('Video Frame', frame_resized)
            if cv2.waitKey(10) & 0xFF == ord('s'):
                break
    
    else:
        break
cv2.destroyAllWindows()