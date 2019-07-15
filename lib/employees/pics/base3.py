"""
This shows how to do face detection using Haar Cascades.

Compared to Deep Learning algorithms, the computer is
given an XML file that descrbes facial features. It
will then "memorize" and use it to detect faces from
other pictures.

This uses the haarcascade_frontalface_default.xml as
the CascadeClassifier input and the face*.jpg images
as sample data.
"""

import cv2
from pathlib import Path


cascade_classifier_xml = Path("./haarcascade_frontalface_default.xml")
face_detector = cv2.CascadeClassifier(cascade_classifier_xml.as_posix())

imgs_dir = Path(".")
for img_file in imgs_dir.glob("face*.jpg"):
    img_file = Path(img_file)
    img_color = cv2.imread(img_file.as_posix())

    # Read the image as color, then convert separately to gray.
    # We will use the color image later to plot the detected
    # face, but face detection works best on grayscale images.
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # https://stackoverflow.com/q/36218385/2745495
    faces = face_detector.detectMultiScale(
        img_gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print(faces)

    img_faces = img_color
    for face in faces:
        rect_x, rect_y, rect_w, rect_h = face
        img_faces = cv2.rectangle(
            img_faces,
            (rect_x, rect_y),
            (rect_x + rect_w, rect_y + rect_h),
            (0, 255, 0),
            2
        )
    cv2.imshow(img_file.name, img_faces)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
