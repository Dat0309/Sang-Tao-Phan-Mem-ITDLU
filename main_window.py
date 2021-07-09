from PyQt5 import QtCore, QtGui, QtWidgets
import sys, icons
from PySide2 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1287, 831)
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        MainWindow.setStyleSheet("border:none;\n"
"background-color:rgba(255,255,255,255);\n"
"border-radius:10px\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slideMenu = QtWidgets.QFrame(self.centralwidget)
        self.slideMenu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.slideMenu.setStyleSheet("")
        self.slideMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slideMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slideMenu.setObjectName("slideMenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slideMenu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.slideMenu)
        self.slide_menu.setMinimumSize(QtCore.QSize(248, 0))
        self.slide_menu.setStyleSheet("background-color:rgba(30,30,30,30);")
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.slide_menu)
        self.frame_7.setStyleSheet("background-color:rgba(30,30,30,30);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0,0,0,200);\n"
"background-color:rgba(30,30,30,30);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setMaximumSize(QtCore.QSize(100, 50))
        self.label_3.setStyleSheet("background-color:rgba(30,30,30,30);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icon/icons/mask.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet("")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("color:rgba(0,0,0,200);\n"
"")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 214, 623))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.page.setFont(font)
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_10 = QtWidgets.QFrame(self.page)
        self.frame_10.setStyleSheet("QPushButton#homeBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#homeBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#homeBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#showBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#showBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#showBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#capBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#capBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#capBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.homeBtn = QtWidgets.QPushButton(self.frame_10)
        self.homeBtn.setMinimumSize(QtCore.QSize(214, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.homeBtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QtCore.QSize(50, 50))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_8.addWidget(self.homeBtn)
        self.showBtn = QtWidgets.QPushButton(self.frame_10)
        self.showBtn.setMinimumSize(QtCore.QSize(214, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.showBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showBtn.setIcon(icon1)
        self.showBtn.setIconSize(QtCore.QSize(50, 50))
        self.showBtn.setObjectName("showBtn")
        self.verticalLayout_8.addWidget(self.showBtn)
        self.capBtn = QtWidgets.QPushButton(self.frame_10)
        self.capBtn.setMinimumSize(QtCore.QSize(214, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.capBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.capBtn.setIcon(icon2)
        self.capBtn.setIconSize(QtCore.QSize(50, 50))
        self.capBtn.setObjectName("capBtn")
        self.verticalLayout_8.addWidget(self.capBtn)
        self.verticalLayout_7.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/drop-black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon3, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 214, 606))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_11 = QtWidgets.QFrame(self.page_2)
        self.frame_11.setStyleSheet("QPushButton#subMenu1{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#subMenu1:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#subMenu1:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#subMenu2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#subMenu2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#subMenu2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.subMenu1 = QtWidgets.QPushButton(self.frame_11)
        self.subMenu1.setMinimumSize(QtCore.QSize(214, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subMenu1.setFont(font)
        self.subMenu1.setObjectName("subMenu1")
        self.verticalLayout_10.addWidget(self.subMenu1)
        self.subMenu2 = QtWidgets.QPushButton(self.frame_11)
        self.subMenu2.setMinimumSize(QtCore.QSize(214, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subMenu2.setFont(font)
        self.subMenu2.setObjectName("subMenu2")
        self.verticalLayout_10.addWidget(self.subMenu2)
        self.verticalLayout_9.addWidget(self.frame_11, 0, QtCore.Qt.AlignTop)
        self.toolBox.addItem(self.page_2, icon3, "")
        self.verticalLayout_6.addWidget(self.toolBox)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.slide_menu)
        self.frame_9.setStyleSheet("QPushButton#exitBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#exitBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#exitBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.exitBtn = QtWidgets.QPushButton(self.frame_9)
        self.exitBtn.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exitBtn.setFont(font)
        self.exitBtn.setIconSize(QtCore.QSize(32, 32))
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout_9.addWidget(self.exitBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout_5.addWidget(self.frame_9, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.slide_menu)
        self.horizontalLayout.addWidget(self.slideMenu)
        self.mainBody = QtWidgets.QFrame(self.centralwidget)
        self.mainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerFrame = QtWidgets.QFrame(self.mainBody)
        self.headerFrame.setStyleSheet("background-color:rgba(30,30,30,30);\n"
"")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.headerFrame)
        self.frame_6.setStyleSheet("QPushButton#menuBtn{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:0.55 rgba(85, 98, 112, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#menuBtn:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:0.55 rgba(85, 81, 84, 226), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QPushButton#menuBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.menuBtn = QtWidgets.QPushButton(self.frame_6)
        self.menuBtn.setMinimumSize(QtCore.QSize(50, 0))
        self.menuBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/Search-write.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon4)
        self.menuBtn.setIconSize(QtCore.QSize(40, 40))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_7.addWidget(self.menuBtn)
        self.horizontalLayout_2.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.headerFrame)
        self.frame_3.setStyleSheet("QPushButton#searchBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"background-color:rgba(30,30,30,30)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(133, 0))
        self.lineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.searchBtn = QtWidgets.QPushButton(self.frame_3)
        self.searchBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/menu_write.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBtn.setIcon(icon5)
        self.searchBtn.setIconSize(QtCore.QSize(20, 20))
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout_6.addWidget(self.searchBtn)
        self.horizontalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.headerFrame)
        self.frame_2.setStyleSheet("QPushButton#userBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#bellBtn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.userBtn = QtWidgets.QPushButton(self.frame_2)
        self.userBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icons/user-black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.userBtn.setIcon(icon6)
        self.userBtn.setIconSize(QtCore.QSize(20, 20))
        self.userBtn.setObjectName("userBtn")
        self.horizontalLayout_5.addWidget(self.userBtn)
        self.bellBtn = QtWidgets.QPushButton(self.frame_2)
        self.bellBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icons/alarm_alert_bell_notification_ring_icon_123294.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bellBtn.setIcon(icon7)
        self.bellBtn.setIconSize(QtCore.QSize(16, 16))
        self.bellBtn.setObjectName("bellBtn")
        self.horizontalLayout_5.addWidget(self.bellBtn)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.headerFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hideBtn = QtWidgets.QPushButton(self.frame)
        self.hideBtn.setStyleSheet("")
        self.hideBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icons/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hideBtn.setIcon(icon8)
        self.hideBtn.setIconSize(QtCore.QSize(20, 20))
        self.hideBtn.setObjectName("hideBtn")
        self.horizontalLayout_4.addWidget(self.hideBtn)
        self.maxBtn = QtWidgets.QPushButton(self.frame)
        self.maxBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maxBtn.setIcon(icon9)
        self.maxBtn.setIconSize(QtCore.QSize(20, 20))
        self.maxBtn.setObjectName("maxBtn")
        self.horizontalLayout_4.addWidget(self.maxBtn)
        self.xBtn = QtWidgets.QPushButton(self.frame)
        self.xBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xBtn.setIcon(icon10)
        self.xBtn.setIconSize(QtCore.QSize(20, 20))
        self.xBtn.setObjectName("xBtn")
        self.horizontalLayout_4.addWidget(self.xBtn)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.headerFrame, 0, QtCore.Qt.AlignTop)
        self.mainBody_contain = QtWidgets.QFrame(self.mainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody_contain.sizePolicy().hasHeightForWidth())
        self.mainBody_contain.setSizePolicy(sizePolicy)
        self.mainBody_contain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBody_contain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBody_contain.setObjectName("mainBody_contain")
        self.verticalLayout.addWidget(self.mainBody_contain)
        self.footer = QtWidgets.QFrame(self.mainBody)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.footer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.footer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_7.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/icons/box0black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon11)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.size_grip = QtWidgets.QFrame(self.footer)
        self.size_grip.setMinimumSize(QtCore.QSize(10, 10))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 10))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_3.addWidget(self.size_grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)

        self.mainBody.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.menuBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=5, yOffset=5))
        self.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.slideMenu.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))


        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Facemask Detect"))
        self.homeBtn.setText(_translate("MainWindow", "Home"))
        self.showBtn.setText(_translate("MainWindow", "Show"))
        self.capBtn.setText(_translate("MainWindow", "Capture"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Tool"))
        self.subMenu1.setText(_translate("MainWindow", "Sub Menu"))
        self.subMenu2.setText(_translate("MainWindow", "Sub Menu"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Setting"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Facemask Detect v 1.0.0"))



# if __name__ == "__main__":
#         app = QtWidgets.QApplication(sys.argv)
#         window = Ui_MainWindow()
#         Form = QtWidgets.QMainWindow()
#         window.setupUi(Form)
#         window.hideBtn.clicked.connect(Form.showMinimized())
#         Form.show()
#         sys.exit(app.exec_())
