from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(659, 614)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 591, 500))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/mask2.jpg);\n"
"border-top-left-radius:50px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(310, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 70, 271, 101))
        self.label_5.setStyleSheet("background-color:rgba(50,50,50,50);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(70, 70, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(225,225,225,225);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(180, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(225,225,225,225);")
        self.label_7.setObjectName("label_7")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(310, 30, 240, 430))
        self.widget_2.setStyleSheet("QPushButton#creBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#creBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#creBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QPushButton#hideBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#hideBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#hideBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"border-bottom-right-radius:50px;")
        self.widget_2.setObjectName("widget_2")
        self.userCreate = QtWidgets.QLineEdit(self.widget_2)
        self.userCreate.setGeometry(QtCore.QRect(20, 90, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userCreate.setFont(font)
        self.userCreate.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.userCreate.setObjectName("userCreate")
        self.passCreate = QtWidgets.QLineEdit(self.widget_2)
        self.passCreate.setGeometry(QtCore.QRect(20, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passCreate.setFont(font)
        self.passCreate.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.passCreate.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passCreate.setObjectName("passCreate")
        self.creBtn = QtWidgets.QPushButton(self.widget_2)
        self.creBtn.setGeometry(QtCore.QRect(30, 330, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.creBtn.setFont(font)
        self.creBtn.setObjectName("creBtn")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(80, 50, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_8.setObjectName("label_8")
        self.hideBtn = QtWidgets.QPushButton(self.widget_2)
        self.hideBtn.setGeometry(QtCore.QRect(0, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.hideBtn.setFont(font)
        self.hideBtn.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.hideBtn.setObjectName("hideBtn")
        self.cpassCreate = QtWidgets.QLineEdit(self.widget_2)
        self.cpassCreate.setGeometry(QtCore.QRect(20, 230, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cpassCreate.setFont(font)
        self.cpassCreate.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cpassCreate.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpassCreate.setObjectName("cpassCreate")
        self.widget_3 = QtWidgets.QWidget(self.label_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 240, 430))
        self.widget_3.setStyleSheet("\n"
"QPushButton#loginBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#loginBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#loginBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QPushButton#loginCreBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#loginCreBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#loginCreBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"border-bottom-right-radius:50px;")
        self.widget_3.setObjectName("widget_3")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(80, 50, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_9.setObjectName("label_9")
        self.userLogin = QtWidgets.QLineEdit(self.widget_3)
        self.userLogin.setGeometry(QtCore.QRect(20, 90, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userLogin.setFont(font)
        self.userLogin.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.userLogin.setObjectName("userLogin")
        self.passLogin = QtWidgets.QLineEdit(self.widget_3)
        self.passLogin.setGeometry(QtCore.QRect(20, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passLogin.setFont(font)
        self.passLogin.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.passLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLogin.setObjectName("passLogin")
        self.loginBtn = QtWidgets.QPushButton(self.widget_3)
        self.loginBtn.setGeometry(QtCore.QRect(30, 240, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.loginCreBtn = QtWidgets.QPushButton(self.widget_3)
        self.loginCreBtn.setGeometry(QtCore.QRect(30, 300, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginCreBtn.setFont(font)
        self.loginCreBtn.setObjectName("loginCreBtn")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.loginBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5))
        self.loginCreBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5))
        self.creBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Face Mask"))
        self.label_7.setText(_translate("Form", "Detect"))
        self.userCreate.setPlaceholderText(_translate("Form", "User Name"))
        self.passCreate.setPlaceholderText(_translate("Form", "Password"))
        self.creBtn.setText(_translate("Form", "Create Acconts"))
        self.label_8.setText(_translate("Form", "Create"))
        self.hideBtn.setText(_translate("Form", "<"))
        self.cpassCreate.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.label_9.setText(_translate("Form", "Login"))
        self.userLogin.setPlaceholderText(_translate("Form", "User Name"))
        self.passLogin.setPlaceholderText(_translate("Form", "Password"))
        self.loginBtn.setText(_translate("Form", "Login"))
        self.loginCreBtn.setText(_translate("Form", "Create Acconts"))

