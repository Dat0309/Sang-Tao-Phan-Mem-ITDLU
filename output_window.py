import re

from numpy.lib.npyio import save
from main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, icons
from PySide2 import *
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2 as cv
import os
from pygame import mixer

mixer.init()
sound = mixer.Sound('alarm.wav')



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(":/icon/icons/mask.svg"))
        self.setWindowTitle("Facemask Dectect")
        QtWidgets.QSizeGrip(self.ui.size_grip)
        self.ui.mainBody.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.menuBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5))
        self.ui.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.slideMenu.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.show()

        self.ui.widget_main.show()
        self.logic = 0
        self.value = 1
        self.score = 0
        self.new_path = 'C:/Users/ADMIN/Face_mask_detect_Dat/Test_model/'

        self.ui.show_main.clicked.connect(self.show_video)
        self.ui.cap_main.clicked.connect(self.cap_video)
        self.ui.menuBtn.clicked.connect(self.showMenubar)
        self.ui.hideBtn.clicked.connect(self.showMinimized)
        self.ui.maxBtn.clicked.connect(self.restore_or_maximized_window)
        self.ui.xBtn.clicked.connect(self.close)
        self.ui.exitBtn.clicked.connect(self.close)
        self.ui.showBtn.clicked.connect(self.showButton)
        # self.ui.homeBtn.clicked.connect(self.homeButton)
        self.ui.capBtn.clicked.connect(self.fileOpen)

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
                
        self.ui.headerFrame.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def restore_or_maximized_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.maxBtn.setIcon(QtGui.QIcon(u":/icon/icons/maximize.svg"))
        else:
            self.showMaximized()
            self.ui.maxBtn.setIcon(QtGui.QIcon(u":/icon/icons/minimize.svg"))

    def showMenubar(self):
        width = self.ui.slideMenu.width()
        if width == 0:
            newWidth = 248
            self.ui.menuBtn.setIcon(QtGui.QIcon(u":/icon/icons/chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.menuBtn.setIcon(QtGui.QIcon(u":/icon/icons/Search-write.svg"))
        
        self.animation = QtCore.QPropertyAnimation(self.ui.slideMenu, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def showButton(self):
        # self.ui.widget.hide()
        self.ui.widget_main.show()

    def homeButton(self):
        self.ui.widget_main.hide()
        self.ui.widget.show()

    def savePic(self, img, box, width=224, height=224):
        self.value += 1
        x, y, w, h = box
        imgCrop = img[y:h, x:w]
        imgCrop = cv.resize(imgCrop, (width, height))
        cv.imwrite(self.new_path + '%s.png'%(self.value), imgCrop)

    def fileOpen(self):
        try:
            fr = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', r'C:\Users\ADMIN\Face_mask_detect_Dat\Test_model', 'PNG files (*.png)')
            print(fr[0])

            img = cv.imread(fr[0])
            cv.imshow("img", img)
            cv.waitKey(0)
            cv.destroyAllWindows()
        except:
            pass
        
    def show_video(self):
        prototxt_path = r"face_detector\deploy.prototxt"
        weightPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
        faceNet = cv.dnn.readNet(prototxt_path, weightPath)

        maskNet = load_model("mask_detector6.model")

        print("Starting Video...")
        cap = cv.VideoCapture(0)
        # cap = cv.VideoCapture(r'C:\Users\ADMIN\Face_mask_detect_Dat\Test_model\nomask.mp4')

        while True:
            ret, frame = cap.read()

            (locs, preds) = self.detect_predict_mask(frame, faceNet, maskNet)

            for (box, pred) in zip(locs, preds):
                (startX, startY, endX, endY) = box
                (mask, withoutMask) = pred

                #label = "Mask" if mask > withoutMask else "No Mask"

                if mask > withoutMask:
                    label = "Mask"
                    self.score = 0
                else:
                    label = "No mask" 
                    self.score = 1
                    

                color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

                label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

                cv.putText(frame, label, (startX, startY - 10), cv.FONT_HERSHEY_COMPLEX, 0.45,color, 2)
                cv.rectangle(frame, (startX, startY), (endX, endY), color, 2)
                
            if self.score==1:
                self.savePic(frame, box)
                try:
                    sound.play()
                    #time.sleep(1)
                except:
                    pass

            if ret == True:
                self.displayImage(frame, 1)

                if (self.logic==2):
                    self.logic = 1
                    break
                    # self.value = self.value + 1
                    # cv.imwrite('%s.png'%(self.value), frame)


                
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
                
            else:
                print("return not found")

        cap.release()
        cv.destroyAllWindows()

    def displayImage(self, img, window = 1):
        qformat = QtGui.QImage.Format_Indexed8

        if len(img.shape) == 3:
            if(img.shape[2]) == 4:
                qformat = QtGui.QImage.Format_RGBA888

            else:
                qformat = QtGui.QImage.Format_RGB888

        img = QtGui.QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        #self.ui.label_4.setScaledContents(True)
        self.ui.label_4.setPixmap(QtGui.QPixmap.fromImage(img))
        self.ui.label_4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


    def cap_video(self):
        self.logic = 2

    def detect_predict_mask(self, frame, faceNet, maskNet):
        (h, w) = frame.shape[:2]
        blob = cv.dnn.blobFromImage(frame, 1.0, (224, 224), (104.0, 177.0, 123.0))

        faceNet.setInput(blob)
        detections = faceNet.forward()
        print(detections.shape)

        faces = []
        locs = []
        preds = []

        '''
        Loop over dectections
        '''
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                (startX, startY) = (max(0, startX), max(0, startY))
                (endX, endY) = (min(w-1, endX), min(h-1, endY))

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
