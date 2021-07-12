import os
import numpy as np
import cv2

# this can be used to play videos
# cap = cv2.VideoCapture(os.path.join('tmp', 'test.mp4'))

cap = cv2.VideoCapture(0) # this captures the video from webcam
w, h = [int(cap.get(i)) for i in range(3, 5)]

# Sepia effect
kernel = np.array(
    [[0.272, 0.534, 0.131],
     [0.349, 0.686, 0.168],
     [0.393, 0.769, 0.189]])

outpath = os.path.join('tmp', 'output.avi')
out = cv2.VideoWriter(outpath, cv2.VideoWriter_fourcc(*'MJPG'), 25, (w, h))

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Apply effects
        frame = cv2.filter2D(frame, -1, kernel)
        frame = cv2.flip(frame, 1)
        out.write(frame)
        # Display the resulting frame
        cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) == 27:
            break
    else:
        break

# When everything done, release the video capture object
cap.release()
out.release()
# Closes all the frames
cv2.destroyAllWindows()
