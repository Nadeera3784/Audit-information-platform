# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class modInstructDialog(QDialog): 
    id = 0
    mod_Instruct_successful_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(modInstructDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        modInstructDialog = self
        modInstructDialog.setObjectName("modInstructDialog")
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(modInstructDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.txtName = QtWidgets.QLineEdit(modInstructDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.txtName.setObjectName("txtName")
        self.lblName = QtWidgets.QLabel(modInstructDialog)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblName.setObjectName("lblName")
        self.lblInstruct = QtWidgets.QLabel(modInstructDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInstruct)
        self.lblInstruct.setObjectName("lblInstruct")
        self.txtInstruct = QtWidgets.QLineEdit(modInstructDialog)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtInstruct)
        self.txtInstruct.setObjectName("txtInstruct")
        self.lblTime = QtWidgets.QLabel(modInstructDialog)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.lblTime.setObjectName("lblTime")
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), modInstructDialog)
        self.dateEdit.setFixedWidth(220)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.lblDocName = QtWidgets.QLabel(modInstructDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDocName)
        self.lblDocName.setObjectName("lblDocName")
        self.txtDocName = QtWidgets.QLineEdit(modInstructDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtDocName)
        self.txtDocName.setObjectName("txtDocName")
        self.lblDocNo = QtWidgets.QLabel(modInstructDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblDocNo)
        self.lblDocNo.setObjectName("lblDocNo")
        self.txtDocNo = QtWidgets.QLineEdit(modInstructDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtDocNo)
        self.txtDocNo.setObjectName("txtDocNo")
        self.lblPerformance = QtWidgets.QLabel(modInstructDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblPerformance)
        self.lblPerformance.setObjectName("lblPerformance")
        self.txtPerformance = QtWidgets.QLineEdit(modInstructDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtPerformance)
        self.txtPerformance.setObjectName("txtPerformance")
        self.lblComment = QtWidgets.QLabel(modInstructDialog)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.lblComment.setObjectName("lblComment")
        self.txtComment = QtWidgets.QLineEdit(modInstructDialog)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtComment)
        self.txtComment.setObjectName("txtComment")

        self.layoutWidget = QtWidgets.QWidget(modInstructDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 240, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #self.btnModInstruct = QtWidgets.QPushButton(self.layoutWidget)
        #self.btnModInstruct.setObjectName("btnModInstruct")
        #self.horizontalLayout.addWidget(self.btnModInstruct)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.horizontalLayout.addWidget(self.buttonBox.button(self.buttonBox.Ok))
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(modInstructDialog)
        self.buttonBox.accepted.connect(modInstructDialog.accept)
        self.buttonBox.rejected.connect(modInstructDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(modInstructDialog)
        
        #self.btnModInstruct.clicked.connect(self.mod_data)


        self.dateEdit.setDisplayFormat("yyyy/MM/dd")
        

        self.dateEdit.setCalendarPopup(True)

    def retranslateUi(self, modInstructDialog):
        _translate = QtCore.QCoreApplication.translate
        modInstructDialog.setWindowTitle(_translate("modInstructDialog", "Revise and correct opinions"))
        self.buttonBox.button(self.buttonBox.Ok).setText("Ok")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")
        self.lblName.setText(_translate("modInstructDialog", "Auditor:"))
        self.lblInstruct.setText(_translate("modInstructDialog", "Rectification opinions:"))
        #self.btnModInstruct.setText(_translate("modInstructDialog", "xxx"))
        self.lblTime.setText(_translate("addInstructDialog", "Date:"))
        self.lblDocName.setText(_translate("modInstructDialog", "Document name:"))
        self.lblDocNo.setText(_translate("modInstructDialog", "Document number:"))
        self.lblPerformance.setText(_translate("modInstructDialog", "Rectification situation:"))
        self.lblComment.setText(_translate("modInstructDialog", "Remarks:"))

    # ?????
    @QtCore.pyqtSlot()
    def mod_data(self):
        id = self.id
        name = self.txtName.text().strip()
        instruct = self.txtInstruct.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        docName = self.txtDocName.text().strip()
        docNo = self.txtDocNo.text().strip()
        performance = self.txtPerformance.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("UPDATE instruct SET name = '{1}', instrDetils = '{2}', date = '{3}', docName = '{4}', docNo = '{5}', performance = '{6}', remark = '{7}' WHERE id = {0}".format(id,name,instruct,date,docName,docNo,performance,remark))
            QMessageBox.question(self, "Success","Successfully revised and rectified opinions!",QMessageBox.Ok)
        #self.mod_Instruct_successful_signal.emit()