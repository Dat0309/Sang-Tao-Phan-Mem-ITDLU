from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2 as cv

from tensorflow.python.keras.backend import dtype

def detect_predict_mask(frame, faceNet, maskNet):
    (h, w) = frame.shape[:2]
    blob = cv.dnn.blobFromImage(frame, 1.0, (224, 224), (104.0, 177.0, 123.0))

    faceNet.setInput(blob)
    detections = faceNet.forward()
    print(detections.shape)

    faces = []
    locs = []
    preds = []

    '''
    Loop over detections
    '''
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            face = frame[startY:endY, startX:endX]
            face = cv.cvtColor(face, cv.COLOR_BGR2RGB)
            face = cv.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)

            faces.append(face)
            locs.append((startX, startY, endX, endY))

    if len(faces) > 0:
        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size = 32)

    return (locs, preds)

prototxt_path = r"face_detector\deploy.prototxt"
weightPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv.dnn.readNet(prototxt_path, weightPath)

maskNet = load_model("mask_detector5.model")

print("Starting video...")
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    (locs, preds) = detect_predict_mask(frame, faceNet, maskNet)

    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        label = "Mask" if mask > withoutMask else "No Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        cv.putText(frame, label, (startX, startY - 10), cv.FONT_HERSHEY_COMPLEX, 0.45, color, 2)
        cv.rectangle(frame, (startX, startY), (endX, endY), color, 2)
    
    # Show the output frame
    cv.imshow("Frame", frame)
    key = cv.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv.destroyAllWindows()
cap.release()