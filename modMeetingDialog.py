# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class modMeetingDialog(QDialog): 
    id = 0
    mod_meeting_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(modMeetingDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        modMeetingDialog = self
        modMeetingDialog.setObjectName("modMeetingDialog")
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(modMeetingDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblName = QtWidgets.QLabel(modMeetingDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblName.setObjectName("lblName")
        self.txtName = QtWidgets.QLineEdit(modMeetingDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.txtName.setObjectName("txtName")
        self.lblMeeting = QtWidgets.QLabel(modMeetingDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblMeeting)
        self.lblMeeting.setObjectName("lblMeeting")
        self.txtMeeting = QtWidgets.QLineEdit(modMeetingDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtMeeting)
        self.txtMeeting.setObjectName("txtMeeting")
        self.lblTime = QtWidgets.QLabel(modMeetingDialog)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.lblTime.setObjectName("lblTime")
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), modMeetingDialog)
        self.dateEdit.setFixedWidth(245)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.lblAddress = QtWidgets.QLabel(modMeetingDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblAddress)
        self.lblAddress.setObjectName("lblAddress")
        self.txtAddress = QtWidgets.QLineEdit(modMeetingDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtAddress)
        self.txtAddress.setObjectName("txtAddress")
        self.lblWithPeople = QtWidgets.QLabel(modMeetingDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblWithPeople)
        self.lblWithPeople.setObjectName("lblWithPeople")
        self.txtWithPeople = QtWidgets.QLineEdit(modMeetingDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtWithPeople)
        self.txtWithPeople.setObjectName("txtWithPeople")
        self.lblComment = QtWidgets.QLabel(modMeetingDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.lblComment.setObjectName("lblComment")
        self.txtComment = QtWidgets.QLineEdit(modMeetingDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtComment)
        self.txtComment.setObjectName("txtComment")

        self.layoutWidget = QtWidgets.QWidget(modMeetingDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 240, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.btnModMeeting = QtWidgets.QPushButton(self.layoutWidget)
        #self.btnModMeeting.setObjectName("btnModMeeting")
        #self.horizontalLayout.addWidget(self.btnModMeeting)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.horizontalLayout.addWidget(self.buttonBox.button(self.buttonBox.Ok))
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.retranslateUi(modMeetingDialog)
        self.buttonBox.accepted.connect(modMeetingDialog.accept)
        self.buttonBox.rejected.connect(modMeetingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(modMeetingDialog)
        
        #self.btnModMeeting.clicked.connect(self.mod_data)

        
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")

       
        self.dateEdit.setCalendarPopup(True)

    def retranslateUi(self, modMeetingDialog):
        _translate = QtCore.QCoreApplication.translate
        modMeetingDialog.setWindowTitle(_translate("modMeetingDialog", "Update Meeting"))
        self.buttonBox.button(self.buttonBox.Ok).setText("OK")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")
        self.lblName.setText(_translate("modMeetingDialog", "Auditor:"))
        self.lblMeeting.setText(_translate("modMeetingDialog", "Meeting:"))
        #self.btnModMeeting.setText(_translate("modMeetingDialog", "xx"))
        self.lblTime.setText(_translate("modMeetingDialog", "Date:"))
        self.lblAddress.setText(_translate("modMeetingDialog", "Location:"))
        self.lblWithPeople.setText(_translate("modMeetingDialog", "Participant:"))
        self.lblComment.setText(_translate("modMeetingDialog", "Remarks:"))

    @QtCore.pyqtSlot()
    def mod_data(self):
        name = self.txtName.text().strip()
        meeting = self.txtMeeting.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        address = self.txtAddress.text().strip()
        joinno = self.txtWithPeople.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("UPDATE metting SET name = '{1}', meeting = '{2}', date = '{3}', address = '{4}', joinno = '{5}', remark = '{6}' WHERE id = {0}".format(self.id,name,meeting,date,address,joinno,remark))
            QMessageBox.question(self, "Success","Meeting has been updated successfully!",QMessageBox.Ok)
        #self.mod_meeting_success_signal.emit()