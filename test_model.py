from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2 as cv

haar_casscade = r"C:\Users\ADMIN\Face_mask_detect_Dat\haar_face.xml"
faceCascade = cv.CascadeClassifier('haar_face.xml')

def face_mask_test(frame, model, required_size=(224, 224)):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 5, minSize =(60, 60), flags= cv.CASCADE_SCALE_IMAGE)

    faces_list = []
    pred=[]

    for (x, y, w, h) in faces:
        face_frame = frame[y:y+h, x:x+w]
        face_frame = cv.cvtColor(face_frame, cv.COLOR_BGR2RGB)
        face_frame = cv.resize(face_frame, required_size)
        face_frame = img_to_array(face_frame)
        #face_frame = np.expand_dims(face_frame, axis=0)
        face_frame = preprocess_input(face_frame)

        faces_list.append(face_frame)

    if len(faces_list)>0:
        faces_list = np.array(faces_list, dtype='float32')
        pred = model.predict(faces_list, batch_size = 32)
        
    for preds in pred:
        (mask, withoutMask) = preds
        
    label = "Mask" if mask > withoutMask else "No Mask"
    color = (0, 255, 0 ) if label == "Mask" else (0, 0, 255)
    label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
    cv.putText(frame, label, (x, y-10), cv.FONT_HERSHEY_COMPLEX, 1, color, 2)
    cv.rectangle(frame, (x, y), (x + w, y + h), color, 3)

    return frame

model = load_model('mask_detector2.model')

test_image = cv.imread(r"C:\Users\ADMIN\Face_mask_detect_Dat\Test_model\test6.jpg")
output = face_mask_test(test_image, model)
cv.resize(output, (500,500))
cv.imshow("frame", output)

cv.waitKey(0)