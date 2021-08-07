
import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')
DIR = r'C:\Users\ADMIN\Face_mask_detect_Dat\face'
PEOPLE = os.listdir(DIR)

features = []
labels = []

def create_train():
    for person in PEOPLE:
        path = os.path.join(DIR, person)
        label = PEOPLE.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()

print('training done .................')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features, labels)

face_recognizer.save('faceRecog_model.yml')
np.save('feature.npy', features)
np.save('labels.npy', labels)

print('DONE!!')