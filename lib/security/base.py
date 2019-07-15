"""
This shows how to capture video stream from a video camera.

This requires an active webcamera connected to the PC.
"""

import cv2
import time


video = cv2.VideoCapture(0)

# Give time for the video to be captured.
time.sleep(2)

while True:
    check, frame = video.read()
    # print(type(check), check)
    # print(type(frame))

    cv2.imshow("video", frame)

    # Show 10 frames per 1s (10 fps)
    # unless user pressed 'q'.
    key = cv2.waitKey(100)
    if key == ord('q'):
        break

cv2.destroyWindow("video")
video.release()
