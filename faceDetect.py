"""
This program uses the following packages:
-- numpy
-- cv2 (openCV)

"""

import numpy as np
import cv2

#the program uses a face detector that uses a classfier based on fronal positon of face
def detectFace(faceDetector, vid):
    while(True):
        ret, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

faceDetector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
detectFace(faceDetector, vid)





print "Face detection Begins..."

