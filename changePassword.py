# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout,QMessageBox,QDialog,QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

class change_password(QDialog):
    retshow = None

    def __init__(self):
        super(change_password, self).__init__()
        self.resize(300, 180)
        self.setWindowTitle('Change Password')
        font = QFont()
        font.setPixelSize(20)
        self.signin_user_label = QLabel('Username:', self)
        self.signin_user_label.setFont(font)
        self.signin_user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signin_user_label.setMaximumWidth(200)
        self.signin_pwd_label = QLabel('Old password:', self)
        self.signin_pwd_label.setFont(font)
        self.signin_pwd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signin_pwd_label.setMaximumWidth(200)
        self.signin_pwd2_label = QLabel('New password:', self)
        self.signin_pwd2_label.setFont(font)
        self.signin_pwd2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.signin_pwd2_label.setMaximumWidth(200)
        self.signin_user_line = QLineEdit(self)
        self.signin_user_line.setMaximumWidth(200)
        self.signin_user_line.setFont(font)
        self.signin_pwd_line = QLineEdit(self)
        self.signin_pwd_line.setFont(font)
        self.signin_pwd_line.setMaximumWidth(200)
        self.signin_pwd2_line = QLineEdit(self)
        self.signin_pwd2_line.setFont(font)
        self.signin_pwd2_line.setMaximumWidth(200)
        self.signin_button = QPushButton('Change', self)
        self.signin_button.setFont(font)
        self.login_button = QPushButton('Cancel', self)
        self.login_button.setFont(font)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.btn_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()

    def layout_init(self):
        self.signin_user_line.setPlaceholderText('Please enter user name!')
        self.signin_pwd_line.setPlaceholderText('Please enter the old password!')
        self.signin_pwd2_line.setPlaceholderText('Please enter a new password!')
        self.user_h_layout.addWidget(self.signin_user_label)
        self.user_h_layout.addWidget(self.signin_user_line)
        self.pwd_h_layout.addWidget(self.signin_pwd_label)
        self.pwd_h_layout.addWidget(self.signin_pwd_line)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_label)
        self.pwd2_h_layout.addWidget(self.signin_pwd2_line)
        self.btn_h_layout.addWidget(self.login_button)
        self.btn_h_layout.addWidget(self.signin_button)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addLayout(self.btn_h_layout)
        self.all_v_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.signin_pwd_line.setEchoMode(QLineEdit.Password)
        self.signin_pwd2_line.setEchoMode(QLineEdit.Password)

        self.signin_user_line.textChanged.connect(self.check_input_func)
        self.signin_pwd_line.textChanged.connect(self.check_input_func)
        self.signin_pwd2_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.signin_button.setEnabled(False)
        self.signin_button.clicked.connect(self.check_signin_func)
        self.login_button.clicked.connect(self.check_login_func)

    def check_input_func(self):
        if self.signin_user_line.text() and self.signin_pwd_line.text() and self.signin_pwd2_line.text():
            self.signin_button.setEnabled(True)
        else:
            self.signin_button.setEnabled(False)

    def check_signin_func(self):
        name = self.signin_user_line.text()
        pwd = self.signin_pwd_line.text()
        pwd2 = self.signin_pwd2_line.text()
        query = QSqlQuery()
        query.prepare("SELECT count(username) FROM users where username=? and password=?")
        query.addBindValue(name)
        query.addBindValue(pwd)
        query.exec_()
        query.next()
        count = query.value(0)
        if count == 1:
            if self.signin_pwd_line.text() == self.signin_pwd2_line.text():
                QMessageBox.critical(self, 'Error', 'Old password same as the new password')
            else:
                query.prepare("UPDATE users SET password=? WHERE username=?")
                query.addBindValue(pwd2)
                query.addBindValue(name)
                query.exec()
                QMessageBox.information(self, 'Success', 'Password reset complete!')
                self.retshow()
        else:
            QMessageBox.critical(self, 'Error：', "Username does not exist or old password is wrong!")
            self.signin_user_line.clear()
            self.signin_pwd_line.clear()
            self.signin_pwd2_line.clear()
        
    def check_login_func(self):
        self.retshow()
