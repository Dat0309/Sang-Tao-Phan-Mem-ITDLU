import cv2 as cv
import os
import face_recognition
import numpy as np

frame = cv.imread(r'C:\Users\ADMIN\Face_mask_detect_Dat\Test_model\1.png')

path = r'C:\Users\ADMIN\Face_mask_detect_Dat\face'
if not os.path.exists(path):
    os.mkdir(path)

# Xác nhận các khuôn mặt và tên
images = []
class_names = []
encode_list = []

PEOPLE = os.listdir(path)

# print(PEOPLE)
for face in PEOPLE:
    cur_img = cv.imread(f'{path}/{face}')
    images.append(cur_img)
    class_names.append(os.path.splitext(face)[0])

for img in images:
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(img)
    encode_cur_frame = face_recognition.face_encodings(img, boxes)[0]
    encode_list.append(encode_cur_frame)

# print(images)
# print(class_names)
# print(encode_list)

faces_cur_frame = face_recognition.face_locations(frame)
encode_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)

for encodeFace, faceLoc in zip(encode_cur_frame, faces_cur_frame):
    match = face_recognition.compare_faces(encode_list, encodeFace, tolerance=0.50)
    face_dis = face_recognition.face_distance(encode_list, encodeFace)
    name = 'unknown'
    best_match_index = np.argmin(face_dis)
    
    if match[best_match_index]:
        name = class_names[best_match_index].upper()
    if (name != 'unknown'):
        print(name)
    else:
        print('unknown')
