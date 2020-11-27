# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class addInspectDialog(QDialog):
    add_inspect_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addInspectDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        addInspectDialog = self
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(addInspectDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.lblName = QtWidgets.QLabel(self)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblName.setObjectName("lblName")
        self.txtName = QtWidgets.QLineEdit(self)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.txtName.setObjectName("txtName")
        self.lblInspect = QtWidgets.QLabel(self)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInspect)
        self.lblInspect.setObjectName("lblInspect")
        self.txtInspect = QtWidgets.QLineEdit(self)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtInspect)
        self.txtInspect.setObjectName("txtInspect")
        self.lblTime = QtWidgets.QLabel(self)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.lblTime.setObjectName("lblTime")
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), addInspectDialog)
        self.dateEdit.setFixedWidth(245)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.lblAddress = QtWidgets.QLabel(addInspectDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblAddress)
        self.lblAddress.setObjectName("lbladdress")
        self.txtAddress = QtWidgets.QLineEdit(addInspectDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtAddress)
        self.txtAddress.setObjectName("txtAddress")
        self.lblWithPeople = QtWidgets.QLabel(addInspectDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblWithPeople)
        self.lblWithPeople.setObjectName("lblWithPeople")
        self.txtWithPeople = QtWidgets.QLineEdit(addInspectDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtWithPeople)
        self.txtWithPeople.setObjectName("txtWithPeople")
        self.lblComment = QtWidgets.QLabel(addInspectDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.lblComment.setObjectName("lblComment")
        self.txtComment = QtWidgets.QLineEdit(addInspectDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtComment)
        self.txtComment.setObjectName("txtComment")

        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 240, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAddInspect = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAddInspect.setObjectName("btnAddInspect")
        self.horizontalLayout.addWidget(self.btnAddInspect)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel |
        #QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(addInspectDialog)
        #self.buttonBox.accepted.connect(addInspectDialog.accept)
        self.buttonBox.rejected.connect(addInspectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addInspectDialog)

        self.btnAddInspect.clicked.connect(self.add_data)

     
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")

     
        self.dateEdit.setCalendarPopup(True)

    def retranslateUi(self, addInspectDialog):
        _translate = QtCore.QCoreApplication.translate
        addInspectDialog.setWindowTitle(_translate("addInspectDialog", "Add rectification check"))
        #self.buttonBox.button(self.buttonBox.Ok).setText("xxx")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")
        self.lblName.setText(_translate("addInspectDialog", "Auditor:"))
        self.lblInspect.setText(_translate("addInspectDialog", "Rectification inspection:"))
        self.btnAddInspect.setText(_translate("addInspectDialog", "Add"))
        self.lblTime.setText(_translate("addInspectDialog", "Date:"))
        self.lblAddress.setText(_translate("addInspectDialog", "Location:"))
        self.lblWithPeople.setText(_translate("addInspectDialog", "Participants:"))
        self.lblComment.setText(_translate("addInspectDialog", "Remarks:"))

    
    @QtCore.pyqtSlot()
    def add_data(self):
        name = self.txtName.text().strip()
        inspect = self.txtInspect.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        address = self.txtAddress.text().strip()
        joinno = self.txtWithPeople.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("INSERT INTO inspect(id,name,inspDetils,date,address,joinDep,remark) SELECT MAX(id)+1,'{0}','{1}','{2}','{3}','{4}','{5}' FROM inspect".format(name,inspect,date,address,joinno,remark))
            QMessageBox.question(self, "Success","The newly added rectification inspection is successful!",QMessageBox.Ok)
            self.txtName.clear()
            self.txtInspect.clear()
            self.dateEdit.setDate(QDate.currentDate())
            self.txtAddress.clear()
            self.txtWithPeople.clear()
            self.txtComment.clear()
        #self.add_Inspect_success_signal.emit()