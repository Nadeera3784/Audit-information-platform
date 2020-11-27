# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

class addInstructDialog(QDialog):
    add_Instruct_success_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(addInstructDialog, self).__init__(parent)
        self.setUpUI()
        self.setWindowModality(Qt.WindowModal)

    def setUpUI(self):
        addInstructDialog = self
        self.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(addInstructDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 300, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.txtName = QtWidgets.QLineEdit(self)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtName)
        self.txtName.setObjectName("txtName")
        self.lblName = QtWidgets.QLabel(self)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblName)
        self.lblName.setObjectName("lblName")
        self.lblInstruct = QtWidgets.QLabel(self)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblInstruct)
        self.lblInstruct.setObjectName("lblInstruct")

        self.txtInstruct = QtWidgets.QLineEdit(self)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtInstruct)
        self.txtInstruct.setObjectName("txtInstruct")
        self.lblTime = QtWidgets.QLabel(self)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblTime)
        self.lblTime.setObjectName("lblTime")
        
        self.dateEdit = QDateTimeEdit(QDate.currentDate(), addInstructDialog)
        self.dateEdit.setFixedWidth(245)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.lblDocName = QtWidgets.QLabel(addInstructDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblDocName)
        self.lblDocName.setObjectName("lblDocName")
        self.txtDocName = QtWidgets.QLineEdit(addInstructDialog)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtDocName)
        self.txtDocName.setObjectName("txtDocName")
        self.lblDocNo = QtWidgets.QLabel(addInstructDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblDocNo)
        self.lblDocNo.setObjectName("lblDocNo")
        self.txtDocNo = QtWidgets.QLineEdit(addInstructDialog)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtDocNo)
        self.txtDocNo.setObjectName("txtDocNo")
        self.lblPerformance = QtWidgets.QLabel(addInstructDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblPerformance)
        self.lblPerformance.setObjectName("lblPerformance")
        self.txtPerformance = QtWidgets.QLineEdit(addInstructDialog)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.txtPerformance)
        self.txtPerformance.setObjectName("txtPerformance")
        self.lblComment = QtWidgets.QLabel(addInstructDialog)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblComment)
        self.lblComment.setObjectName("lblComment")
        self.txtComment = QtWidgets.QLineEdit(addInstructDialog)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.txtComment)
        self.txtComment.setObjectName("txtComment")

        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 240, 300, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAddInstruct = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAddInstruct.setObjectName("btnAddInstruct")
        self.horizontalLayout.addWidget(self.btnAddInstruct)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(addInstructDialog)
        #self.buttonBox.accepted.connect(addInstructDialog.accept)
        self.buttonBox.rejected.connect(addInstructDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(addInstructDialog)

        self.btnAddInstruct.clicked.connect(self.add_data)

        
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")

        
        
        

        
        self.dateEdit.setCalendarPopup(True)

    def retranslateUi(self, addInstructDialog):
        _translate = QtCore.QCoreApplication.translate
        addInstructDialog.setWindowTitle(_translate("addInstructDialog", "Add rectification suggestions"))
        #self.buttonBox.button(self.buttonBox.Ok).setText("xxx")
        self.buttonBox.button(self.buttonBox.Cancel).setText("Cancel")
        self.lblName.setText(_translate("addInstructDialog", "Auditor:"))
        self.lblInstruct.setText(_translate("addInstructDialog", "Contents of rectification opinions;"))
        self.btnAddInstruct.setText(_translate("addInstructDialog", "Add"))
        self.lblTime.setText(_translate("addInstructDialog", "Date："))
        self.lblDocName.setText(_translate("addInstructDialog", "Document name:"))
        self.lblDocNo.setText(_translate("addInstructDialog", "Document Number:"))
        self.lblPerformance.setText(_translate("addInstructDialog", "Rectification situation;"))
        self.lblComment.setText(_translate("addInstructDialog", "Remarks:"))


    @QtCore.pyqtSlot()
    def add_data(self):
        name = self.txtName.text().strip()
        instruct = self.txtInstruct.text().strip()
        date = self.dateEdit.dateTime().toString('yyyy/MM/dd')
        docName = self.txtDocName.text().strip()
        docNo = self.txtDocNo.text().strip()
        performance = self.txtPerformance.text().strip()
        remark = self.txtComment.text().strip()
        if(name != ""):
            query = QSqlQuery()
            query.exec_("INSERT INTO instruct(name,instrDetils,date,docName,docNo,performance,remark) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(name,instruct,date,docName,docNo,performance,remark))
            QMessageBox.question(self, "Success","Successfully added rectification opinions!",QMessageBox.Ok)
            self.txtName.clear()
            self.txtInstruct.clear()
            self.dateEdit.setDate(QDate.currentDate())
            self.txtDocName.clear()
            self.txtDocNo.clear()
            self.txtPerformance.clear()
            self.txtComment.clear()
        #self.add_Instruct_success_signal.emit()