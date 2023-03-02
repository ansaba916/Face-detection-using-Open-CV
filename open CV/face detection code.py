# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:17:31 2023

@author: 91974
"""

import cv2


cap= cv2.VideoCapture(0)

while True:
    check, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# read the haarcascade to detect the faces in an image
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# detects faces in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    print('Number of detected faces:', len(faces))

# loop over all detected faces
    if len(faces) > 0:
        for i, (x, y, w, h) in enumerate(faces):
 
      # To draw a rectangle in a face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face = img[y:y + h, x:x + w]
            cv2.imshow("Cropped Face", face)
            #cv2.imshow('video', frame)
            for i in range(0,1):
                c=str(i)
                cv2.imwrite('image/'+c+'.jpg', face)
      #print(f"face{i}.jpg is saved")
 
# display the image with detected faces
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()