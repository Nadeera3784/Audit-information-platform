# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class modInvestDialog(QDialog): 
    id = 0
    mod_Invest_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(modInvestDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        modInvestDialog = self
        modInvestDialog.setObjectName("modInvestDialog")
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(modInvestDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.lblName = QtWidgets.QLabel(modInvestDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblName.setObjectName("lblName")
        self.txtName = QtWidgets.QLineEdit(modInvestDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.txtName.setObjectName("txtName")
        self.lblInvest = QtWidgets.QLabel(modInvestDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInvest)
        self.lblInvest.setObjectName("lblInvest")
        self.txtInvest = QtWidgets.QLineEdit(modInvestDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtInvest)
        self.txtInvest.setObjectName("txtInvest")
        self.lblTime = QtWidgets.QLabel(modInvestDialog)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.lblTime.setObjectName("lblTime")
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), modInvestDialog)
        self.dateEdit.setFixedWidth(220)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.lblAddress = QtWidgets.QLabel(modInvestDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblAddress)
        self.lblAddress.setObjectName("lblAddress")
        self.txtAddress = QtWidgets.QLineEdit(modInvestDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtAddress)
        self.txtAddress.setObjectName("txtAddress")
        self.lblComment = QtWidgets.QLabel(modInvestDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.lblComment.setObjectName("lblComment")
        self.txtComment = QtWidgets.QLineEdit(modInvestDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtComment)
        self.txtComment.setObjectName("txtComment")

        self.layoutWidget = QtWidgets.QWidget(modInvestDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 180, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.btnModInvest = QtWidgets.QPushButton(self.layoutWidget)
        #self.btnModInvest.setObjectName("btnModInvest")
        #self.horizontalLayout.addWidget(self.btnModInvest)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.horizontalLayout.addWidget(self.buttonBox.button(self.buttonBox.Ok))
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(modInvestDialog)
        self.buttonBox.accepted.connect(modInvestDialog.accept)
        self.buttonBox.rejected.connect(modInvestDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(modInvestDialog)
        
        #self.btnModInvest.clicked.connect(self.mod_data)


        self.dateEdit.setDisplayFormat("yyyy/MM/dd")


        self.dateEdit.setCalendarPopup(True)

    def retranslateUi(self, modInvestDialog):
        _translate = QtCore.QCoreApplication.translate
        modInvestDialog.setWindowTitle(_translate("modInvestDialog", "Update audit investigation"))
        self.buttonBox.button(self.buttonBox.Ok).setText("Ok")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")
        self.lblName.setText(_translate("modInvestDialog", "Auditor:"))
        self.lblInvest.setText(_translate("modInvestDialog", "Research:"))
        #self.btnModInvest.setText(_translate("modInvestDialog", "xx"))
        self.lblTime.setText(_translate("modInvestDialog", "Date:"))
        self.lblAddress.setText(_translate("modInvestDialog", "Location:"))
        self.lblComment.setText(_translate("modInvestDialog", "Remarks:"))


    @QtCore.pyqtSlot()
    def mod_data(self):
        id = self.id
        name = self.txtName.text().strip()
        Invest = self.txtInvest.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        address = self.txtAddress.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("UPDATE invest SET name = '{1}', invDetils = '{2}', date = '{3}', address = '{4}', remark = '{5}' WHERE id = {0}".format(id,name,Invest,date,address,remark))
            QMessageBox.question(self, "Success","Audit investigation has been updated successfully!",QMessageBox.Ok)
        #self.mod_Invest_successful_signal.emit()