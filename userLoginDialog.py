# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
#from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit, QPushButton, QMainWindow, QApplication

from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlQuery
from MainWindow import *
from ui.Notification import NotificationWindow

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 127)
        MainWindow.setWindowIcon(QIcon("images\logo.png"))
        MainWindow.setStyleSheet("background-image:url(images/Background.jpg)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineUserEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineUserEdit.setGeometry(QtCore.QRect(190, 20, 175, 20))
        self.lineUserEdit.setText("")
        self.lineUserEdit.setObjectName("lineEdit")
        self.linePasswordEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.linePasswordEdit.setGeometry(QtCore.QRect(190, 50, 175, 20))
        self.linePasswordEdit.setText("")
        self.linePasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePasswordEdit.setObjectName("lineEdit_2")
        # self.label = QtWidgets.QLabel(self.centralWidget)
        # self.label.setGeometry(QtCore.QRect(180, 24, 50, 15))
        # self.label.setTextFormat(QtCore.Qt.AutoText)
        # self.label.setObjectName("label")
        # self.label_2 = QtWidgets.QLabel(self.centralWidget)
        # self.label_2.setGeometry(QtCore.QRect(200, 54, 24, 15))
        # self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lineUserEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.linePasswordEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        # self.label.setText(_translate("MainWindow", "username"))
        # self.label_2.setText(_translate("MainWindow", "password"))
        self.pushButton.setText(_translate("MainWindow", "login"))
        self.pushButton_2.setText(_translate("MainWindow", "cancel"))

    def word_get(self):
        login_user = self.lineUserEdit.text()
        login_password = self.linePasswordEdit.text()
        query = QSqlQuery()
        query.prepare("SELECT count(username) FROM users where username=? and password=?")
        query.addBindValue(login_user)
        query.addBindValue(login_password)
        query.exec_()
        query.next()
        count = query.value(0)
        if count == 1:
            QMessageBox.information(self, 'Success', "login successful!")
            ui_main.show()
            MainWindow.close()
        else:
            QMessageBox.information(self, 'Error', "Username or password is incorrect!")
            NotificationWindow.info('Error', 'Shit wnt down')
            self.lineUserEdit.setFocus()
            self.lineUserEdit.clear()
            self.linePasswordEdit.clear()

    def callback():
        print('boom')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui_main = Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

