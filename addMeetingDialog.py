# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class addMeetingDialog(QDialog):
    add_meeting_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addMeetingDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        addMeetingDialog = self
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(addMeetingDialog)
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
        self.lblMeeting = QtWidgets.QLabel(self)
        self.lblMeeting.setObjectName("lblMeeting")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblMeeting)
        self.txtMeeting = QtWidgets.QLineEdit(self)
        self.txtMeeting.setObjectName("txtMeeting")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtMeeting)
        self.lblTime = QtWidgets.QLabel(self)
        self.lblTime.setObjectName("lblTime")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.dateEdit = QDateEdit(QDate.currentDate(), addMeetingDialog)
        self.dateEdit.setFixedWidth(245)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.dateEdit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.lblAddress = QtWidgets.QLabel(addMeetingDialog)
        self.lblAddress.setObjectName("lblAddress")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblAddress)
        self.txtAddress = QtWidgets.QLineEdit(addMeetingDialog)
        self.txtAddress.setObjectName("txtAddress")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtAddress)
        self.lblWithPeople = QtWidgets.QLabel(addMeetingDialog)
        self.lblWithPeople.setObjectName("lblWithPeople")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblWithPeople)
        self.txtWithPeople = QtWidgets.QLineEdit(addMeetingDialog)
        self.txtWithPeople.setObjectName("txtWithPeople")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtWithPeople)
        self.lblComment = QtWidgets.QLabel(addMeetingDialog)
        self.lblComment.setObjectName("lblComment")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.txtComment = QtWidgets.QLineEdit(addMeetingDialog)
        self.txtComment.setObjectName("txtComment")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtComment)

  
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 220, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAddMeeting = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAddMeeting.setObjectName("btnAddMeeting")
        self.horizontalLayout.addWidget(self.btnAddMeeting)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(addMeetingDialog)
        QtCore.QMetaObject.connectSlotsByName(addMeetingDialog)
        # self.buttonBox.accepted.connect(addMeetingDialog.accept)
        self.buttonBox.rejected.connect(addMeetingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addMeetingDialog)
        self.btnAddMeeting.clicked.connect(self.add_data)
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)

    def retranslateUi(self, addMeetingDialog):
        _translate = QtCore.QCoreApplication.translate
        addMeetingDialog.setWindowTitle(_translate("addMeetingDialog", "Add meeting"))
        
        self.lblName.setText(_translate("addMeetingDialog", "Auditor's name："))
        self.lblMeeting.setText(_translate("addMeetingDialog", "Meeting："))
        self.lblTime.setText(_translate("addMeetingDialog", "Date："))
        self.lblAddress.setText(_translate("addMeetingDialog", "Location："))
        self.lblWithPeople.setText(_translate("addMeetingDialog", "Participant:"))
        self.lblComment.setText(_translate("addMeetingDialog", "Remarks:"))
        self.btnAddMeeting.setText(_translate("addMeetingDialog", "Add"))
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")

  
    @QtCore.pyqtSlot()
    def add_data(self):
        name = self.txtName.text().strip()
        meeting = self.txtMeeting.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        address = self.txtAddress.text().strip()
        joinno = self.txtWithPeople.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("INSERT INTO metting(id,name,meeting,date,address,joinno,remark) SELECT MAX(id)+1,'{0}','{1}','{2}','{3}','{4}','{5}' FROM metting".format(name,meeting,date,address,joinno,remark))
            self.txtName.clear()
            self.txtMeeting.clear()
            self.dateEdit.setDate(QDate.currentDate())
            self.txtAddress.clear()
            self.txtWithPeople.clear()
            self.txtComment.clear()
            QMessageBox.question(self, "Success","Successfully added meeting!",QMessageBox.Ok)
        self.add_meeting_success_signal.emit()