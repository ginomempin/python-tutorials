"""
This shows how to capture video stream from a video camera,
detect objects and draw bounding boxes around them, and then
record the times when objects enter/exit the frame.

This requires an active webcamera connected to the PC.
"""

from collections import namedtuple
from datetime import datetime
import time

import cv2
import pandas


Color = namedtuple("RGB", ["red", "green", "blue"])
WHITE = Color(255, 255, 255)
GREEN = Color(0, 255, 0)

video = cv2.VideoCapture(0)

# Give time for the video to be captured.
time.sleep(2)

prev_frame = None

tracker = [False, False]  # pre-load 2 frames with no objects
objects_timestamps = []

while True:
    has_object = False

    _, video_frame = video.read()
    # print(type(check), check)

    # Apply grayscale (because it's required by the threshold
    # functions) and Gaussian Blur to smoothen the image and
    # remove noise.
    curr_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
    curr_frame = cv2.GaussianBlur(curr_frame, (21, 21), 0)

    if prev_frame is None:
        prev_frame = curr_frame
        continue

    # Get the difference in pixels between the previous and
    # current frames.
    delta_frame = cv2.absdiff(prev_frame, curr_frame)

    # Apply simple thresholding. If the difference in pixel
    # value intensity is above a certain value, show it as
    # white. Otherwise, show it as black. Also apply dilation
    # to smoothen and remove noise from the resulting whites.
    _, thresh_frame = cv2.threshold(
        delta_frame,
        30, WHITE.red,
        cv2.THRESH_BINARY
    )
    # print(type(check), check)
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=3)

    # Find the contours from the thresholded image but ignoring
    # contours with small areas, which we won't be considered as
    # "objects". For each contour found, draw its bounding box on
    # the original video frame.
    contours, _ = cv2.findContours(
        thresh_frame.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    for cnt in contours:
        if cv2.contourArea(cnt) < 1000:
            continue
        has_object = True
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(
            video_frame,
            (x, y),
            (x + w, y + h),
            GREEN,
            thickness=3
        )

    # Display the original video frame with the
    # superimposed bounding box.
    cv2.imshow("video", video_frame)

    # Track if an object entered/exited the frame.
    #
    # If the previous frame does not have an object and
    # this current frame has, then we save this as the
    # event where "an object entered the frame".
    #
    # Similarly, if the previous frame had an object and
    # this current frame does not have one anymore, then
    # we save this as the event where "an object exited
    # the frame".
    #
    # The tracker array was pre-loaded with empty frames,
    # has_object=False. This handles the case for the 1st
    # frames and there are no previously stored0 events yet.
    tracker.append(has_object)
    if tracker[-1] is True and tracker[-2] is False:
        objects_timestamps.append(datetime.now())
    if tracker[-1] is False and tracker[-2] is True:
        objects_timestamps.append(datetime.now())

    # Show 10 frames per 1s (10 fps) unless user pressed 'q'.
    key = cv2.waitKey(100)
    if key == ord('q'):
        # Handle the case where there is an object and the
        # video loop was quit. This would result in an odd
        # numbered timestamps. To ensure pairs of enter-exit,
        # manually add the quit time as the exit timestamp.
        if len(objects_timestamps) % 2 != 0:
            objects_timestamps.append(datetime.now())
        break

# Save the timestamps to a dataframe (for extended processing)
# and finally to a CSV file.
objects_df = pandas.DataFrame(columns=["Enter", "Exit"])
for idx in range(0, len(objects_timestamps), 2):
    objects_df = objects_df.append({
        "Enter": objects_timestamps[idx],
        "Exit": objects_timestamps[idx + 1]
    }, ignore_index=True)
print(objects_df)
objects_df.to_csv("timestamps.csv")

cv2.destroyWindow("video")
video.release()
