from PyQt5 import QtSql, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from loginUI import Ui_Form
from outwindow import UI_outDialog
import sys

class myApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(myApp, self).__init__()
        self.setupUi(self)
        self.openDB()
        
        self.widget_2.hide()
        self.loginBtn.clicked.connect(self.checkUser)
        self.loginCreBtn.clicked.connect(self.createUser)
        self.hideBtn.clicked.connect(self.backLogin)
        self.creBtn.clicked.connect(self.addUser)

        self._new_window = None
        self.Videocapture_ = None

    def refreshAll(self):
        self.Videocapture_ = "1"

    def openDB(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.sqlite")
        if not self.db.open():
            print("Error")
        self.query = QtSql.QSqlQuery()

    def checkUser(self):
        usersname = self.userLogin.text()
        password = self.passLogin.text()
        #print(usersname, password)
        self.query.exec_("select * from userdata where username = '%s' and pass = '%s';"%(usersname, password))
        self.query.first()
        if self.query.value("username") != None and self.query.value("pass") != None:
            print("Longin success!!!")
            self.refreshAll()
            print(self.Videocapture_)
            Form.hide()
            self.outputwindow_()
        else:
            print("Longin fail!!")
            self.show_err()

    def addUser(self):
        usersname = self.userCreate.text()
        password = self.passCreate.text()
        #print(usersname, password)
        self.query.exec_("select * from userdata where username = '%s' and pass = '%s';"%(usersname,password))
        self.query.first()

        if self.query.value("username") !=None and self.query.value("pass") !=None:
            self.err_create()
        else: 
            self.query.exec_("insert into userdata (username, pass) values('%s', '%s');"%(usersname,password))
            self.succ()

    def err_create(self):
        mess = QMessageBox()
        mess.setWindowTitle("Error")
        mess.setText("Your user name is already exist!")
        mess.setIcon(QMessageBox.Warning)
        mess.setStandardButtons(QMessageBox.Retry)
        x = mess.exec_()

    def succ(self):
        mess = QMessageBox()
        mess.setWindowTitle("Success!")
        mess.setText('Account successfully created')
        mess.setIcon(QMessageBox.Question)
        mess.setStandardButtons(QMessageBox.Ok)

        x = mess.exec_()
        
    def createUser(self):
        self.widget_3.hide()
        self.widget_2.show()

    def backLogin(self):
        self.widget_3.show()
        self.widget_2.hide() 

    def show_err(self):
        mess = QMessageBox()
        mess.setWindowTitle("Error")
        mess.setText("Your User Name or Password is wrong.Plese Try again!!")
        mess.setIcon(QMessageBox.Warning)
        mess.setStandardButtons(QMessageBox.Retry|QMessageBox.Cancel)

        x = mess.exec_()


    def outputwindow_(self):
        self._new_window = UI_outDialog()
        self._new_window.show()
        

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = myApp()
        Form.show()
        sys.exit(app.exec_())