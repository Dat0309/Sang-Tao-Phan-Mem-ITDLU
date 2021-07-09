from main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, icons
from PySide2 import *
from main_window import Ui_MainWindow

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

        self.ui.menuBtn.clicked.connect(self.showMenubar)
        self.ui.hideBtn.clicked.connect(self.showMinimized)
        self.ui.maxBtn.clicked.connect(self.restore_or_maximized_window)
        self.ui.xBtn.clicked.connect(self.close)
        self.ui.exitBtn.clicked.connect(self.close)

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
            newWidth = 200
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
