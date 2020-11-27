# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class modInspectDialog(QDialog): 
    id = 0
    mod_Inspect_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(modInspectDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        modInspectDialog = self
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(modInspectDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.lblName = QtWidgets.QLabel(modInspectDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblName.setObjectName("lblName")
        self.txtName = QtWidgets.QLineEdit(modInspectDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.txtName.setObjectName("txtName")
        self.lblInspect = QtWidgets.QLabel(modInspectDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInspect)
        self.lblInspect.setObjectName("lblInspect")
        self.txtInspect = QtWidgets.QLineEdit(modInspectDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtInspect)
        self.txtInspect.setObjectName("txtInspect")
        self.lblTime = QtWidgets.QLabel(modInspectDialog)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.lblTime.setObjectName("lblTime")
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), modInspectDialog)
        self.dateEdit.setFixedWidth(245)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.lblAddress = QtWidgets.QLabel(modInspectDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblAddress)
        self.lblAddress.setObjectName("lblAddress")
        self.txtAddress = QtWidgets.QLineEdit(modInspectDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtAddress)
        self.txtAddress.setObjectName("txtAddress")
        self.lblWithPeople = QtWidgets.QLabel(modInspectDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblWithPeople)
        self.lblWithPeople.setObjectName("lblWithPeople")
        self.txtWithPeople = QtWidgets.QLineEdit(modInspectDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtWithPeople)
        self.txtWithPeople.setObjectName("txtWithPeople")
        self.lblComment = QtWidgets.QLabel(modInspectDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.lblComment.setObjectName("lblComment")
        self.txtComment = QtWidgets.QLineEdit(modInspectDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtComment)
        self.txtComment.setObjectName("txtComment")

        self.layoutWidget = QtWidgets.QWidget(modInspectDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 240, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.btnModInspect = QtWidgets.QPushButton(self.layoutWidget)
        #self.btnModInspect.setObjectName("btnModInspect")
        #self.horizontalLayout.addWidget(self.btnModInspect)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.horizontalLayout.addWidget(self.buttonBox.button(self.buttonBox.Ok))
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(modInspectDialog)
        self.buttonBox.accepted.connect(modInspectDialog.accept)
        self.buttonBox.rejected.connect(modInspectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(modInspectDialog)
        
        #self.btnModInspect.clicked.connect(self.mod_data)

        self.dateEdit.setDisplayFormat("yyyy/MM/dd")        

        self.dateEdit.setCalendarPopup(True)

    def retranslateUi(self, modInspectDialog):
        _translate = QtCore.QCoreApplication.translate
        modInspectDialog.setWindowTitle(_translate("modInspectDialog", "Modification and rectification inspection"))
        self.buttonBox.button(self.buttonBox.Ok).setText("Ok")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")
        self.lblName.setText(_translate("modInspectDialog", "Auditor:"))
        self.lblInspect.setText(_translate("modInspectDialog", "Rectification inspection:"))
        #self.btnModInspect.setText(_translate("modInspectDialog", "xxx"))
        self.lblTime.setText(_translate("modInspectDialog", "Date:"))
        self.lblAddress.setText(_translate("modInspectDialog", "Location:"))
        self.lblWithPeople.setText(_translate("addInspectDialog", "Participants:"))
        self.lblComment.setText(_translate("modInspectDialog", "Remarks:"))


    @QtCore.pyqtSlot()
    def mod_data(self):
        id = self.id
        name = self.txtName.text().strip()
        inspect = self.txtInspect.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        address = self.txtAddress.text().strip()
        joinDep = self.txtWithPeople.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("UPDATE inspect SET name = '{1}', inspDetils = '{2}', date = '{3}', address = '{4}', joinDep = '{5}', remark = '{6}' WHERE id = {0}".format(id,name,inspect,date,address,joinDep,remark))
            QMessageBox.question(self, "Success","Modification, rectification and inspection succeeded!",QMessageBox.Ok)
        #self.mod_Inspect_successful_signal.emit()