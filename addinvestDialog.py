# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class addInvestDialog(QDialog):
    add_invest_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addInvestDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        addInvestDialog = self
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(addInvestDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblName = QtWidgets.QLabel(self)
        self.lblName.setObjectName("lblName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.txtName = QtWidgets.QLineEdit(self)
        self.txtName.setObjectName("txtName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.lblInvest = QtWidgets.QLabel(self)
        self.lblInvest.setObjectName("lblInvest")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInvest)
        self.txtInvest = QtWidgets.QLineEdit(self)
        # self.txtInvest.setGeometry(QtCore.QRect(340, 40, 113, 20))
        self.txtInvest.setObjectName("txtInvest")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtInvest)
        self.lblTime = QtWidgets.QLabel(self)
        # self.lblTime.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.lblTime.setObjectName("lblTime")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), addInvestDialog)
        self.dateEdit.setFixedWidth(245)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.dateEdit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.lblAddress = QtWidgets.QLabel(addInvestDialog)
        # self.lblAddress.setGeometry(QtCore.QRect(40, 140, 47, 13))
        self.lblAddress.setObjectName("lblAddress")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblAddress)
        self.txtAddress = QtWidgets.QLineEdit(addInvestDialog)
        # self.txtAddress.setGeometry(QtCore.QRect(100, 140, 351, 20))
        self.txtAddress.setObjectName("txtAddress")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtAddress)
        self.lblComment = QtWidgets.QLabel(addInvestDialog)
        # self.lblComment.setGeometry(QtCore.QRect(40, 180, 47, 13))
        self.lblComment.setObjectName("lblComment")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.txtComment = QtWidgets.QLineEdit(addInvestDialog)
        # self.txtComment.setGeometry(QtCore.QRect(100, 180, 351, 20))
        self.txtComment.setObjectName("txtComment")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtComment)
  
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 220, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAddInvest = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAddInvest.setObjectName("btnAddInvest")
        self.horizontalLayout.addWidget(self.btnAddInvest)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(addInvestDialog)
        #self.buttonBox.accepted.connect(addInvestDialog.accept)
        self.buttonBox.rejected.connect(addInvestDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addInvestDialog)

        self.btnAddInvest.clicked.connect(self.add_data)


        self.dateEdit.setDisplayFormat("yyyy/MM/dd")

        self.dateEdit.setCalendarPopup(True)

    def retranslateUi(self, addInvestDialog):
        _translate = QtCore.QCoreApplication.translate
        addInvestDialog.setWindowTitle(_translate("addInvestDialog", "Add audit investigation"))
        #self.buttonBox.button(self.buttonBox.Ok).setText("xxxx")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")
        self.lblName.setText(_translate("addInvestDialog", "Auditor's name:"))
        self.lblInvest.setText(_translate("addInvestDialog", "Research:"))
        self.btnAddInvest.setText(_translate("addInvestDialog", "Add"))
        self.lblTime.setText(_translate("addInvestDialog", "Date:"))
        self.lblAddress.setText(_translate("addInvestDialog", "Location:"))
        self.lblComment.setText(_translate("addInvestDialog", "Remarks:"))

  
    @QtCore.pyqtSlot()
    def add_data(self):
        name = self.txtName.text().strip()
        Invest = self.txtInvest.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        address = self.txtAddress.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("INSERT INTO invest(name,invDetils,date,address,remark) SELECT '{0}','{1}','{2}','{3}','{4}'".format(name,Invest,date,address,remark))
            QMessageBox.question(self, "Success","Successfully added audit investigation!",QMessageBox.Ok)
            self.txtName.clear()
            self.txtInvest.clear()
            self.dateEdit.setDate(QDate.currentDate())
            self.txtAddress.clear()
            self.txtComment.clear()
        self.add_invest_success_signal.emit()