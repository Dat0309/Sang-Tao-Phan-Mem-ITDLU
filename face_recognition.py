import cv2 as cv
import os
import numpy as np
import face_recognition

# haar_cascade = cv.CascadeClassifier('haar_face.xml')
# DIR = r'C:\Users\ADMIN\Face_mask_detect_Dat\face'
# people = os.listdir(DIR)

# face_recognizer = cv.face.LBPHFaceRecognizer_create()
# face_recognizer.read('faceRecog_model.yml')

# img = cv.imread(r'C:\Users\ADMIN\Face_mask_detect_Dat\Test_model\250.png')

# # cv.imshow('person', gray)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

# for (x, y, w, h) in faces_rect:
#     face_roi = gray[y:y+h, x:x+w]

#     label, confidence = face_recognizer.predict(face_roi)
#     print(f'{people[label]} with a confident of {confidence}')


# cv.imshow('Nhận diện', img)
# cv.waitKey(0)
dir = r'C:\Users\ADMIN\Face_mask_detect_Dat\face2'

#Trong trường hợp tìm không thấy thư mục, sẽ tự tạo thêm thư mục trong đường dẫn đó
if not os.path.exists(dir):
    os.mkdir(dir)

images = []
class_names = []
encode_list = []
attendance_list = os.listdir(dir)
print(attendance_list)

for face in attendance_list:
    path = os.path.join(dir,face)
    cur_image = cv.imread(path)
    images.append(cur_image)
    class_names.append(os.path.splitext(face)[0])

print(images)
print(class_names)

for img in images:
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(img)
    encode_cur_frame = face_recognition.face_encodings(img,boxes)[0]
    encode_list.append(encode_cur_frame)

print(encode_list)