import cv2 as cv
import os
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')
DIR = r'C:\Users\ADMIN\Face_mask_detect_Dat\face'
people = os.listdir(DIR)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('faceRecog_model.yml')

img = cv.imread(r'C:\Users\ADMIN\Face_mask_detect_Dat\Test_model\42.png')

# cv.imshow('person', gray)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'{people[label]} with a confident of {confidence}')


cv.imshow('Nhận diện', img)
cv.waitKey(0)