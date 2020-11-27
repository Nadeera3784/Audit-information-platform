from PyQt5.QtWidgets import *	
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sip
from ui.Main import Ui_MainWindow
from meetingWidget import MeetingWidget
from investWidget import InvestWidget
from instructWdiget import InstructWidget
from inspectWidget import InspectWidget
from changePassword import change_password
import os

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('./cmdb.sqlite')
        self.db.open()
        
        self.init()

        self.actionmeeting.triggered.connect(self.meetingshow)
        self.actioninvest.triggered.connect(self.investshow)
        self.actioninstruct.triggered.connect(self.instructshow)
        self.actioninspect.triggered.connect(self.inspectshow)
        
        self.actioninput.triggered.connect(self.inputexcel)
        self.actionoutput.triggered.connect(self.outputexcel)
        self.actionprint.triggered.connect(self.print)
        self.actionperpage.triggered.connect(self.page_setting)
        
        self.actionhelp.triggered.connect(self.help)
        self.actionAbout_Us.triggered.connect(self.about)
        
        self.actionchangepassword.triggered.connect(self.changepasswordshow)

    def init(self):
        self.actionperpage.setEnabled(True)
        self.actionprint.setEnabled(True)
        self.actionmeeting.setEnabled(True)
        self.actioninvest.setEnabled(True)
        self.actioninstruct.setEnabled(True)
        self.actioninspect.setEnabled(True)
        self.actioninput.setEnabled(True)
        self.actionoutput.setEnabled(True)
        #self.actionData_Analytical.setEnabled(True)
        self.actionhelp.setEnabled(True)
        self.meetingshow()
        self.actionmeeting.setChecked(True)

    def help(self):
        fd = os.startfile("help.pdf")

    def about(self):
        reply = QMessageBox.about(self,"About","Audit Information Statistics Platform V1.0\nDevelop by R.Nadeera Sampath\n")

    def meetingshow(self):
        self.widget = MeetingWidget()
        self.setCentralWidget(self.widget)
        if self.actioninvest.isChecked():
            self.actioninvest.setChecked(False)
        if self.actioninstruct.isChecked():
            self.actioninstruct.setChecked(False)
        if self.actioninspect.isChecked():
            self.actioninspect.setChecked(False)

    def investshow(self):
        sip.delete(self.widget)
        self.widget = InvestWidget()
        self.setCentralWidget(self.widget)
        if self.actionmeeting.isChecked():
            self.actionmeeting.setChecked(False)
        if self.actioninstruct.isChecked():
            self.actioninstruct.setChecked(False)
        if self.actioninspect.isChecked():
            self.actioninspect.setChecked(False)

    def instructshow(self):
        sip.delete(self.widget)
        self.widget = InstructWidget()
        self.setCentralWidget(self.widget)
        if self.actionmeeting.isChecked():
            self.actionmeeting.setChecked(False)
        if self.actioninvest.isChecked():
            self.actioninvest.setChecked(False)
        if self.actioninspect.isChecked():
            self.actioninspect.setChecked(False)

    def inspectshow(self):
        sip.delete(self.widget)
        self.widget = InspectWidget()
        self.setCentralWidget(self.widget)
        if self.actionmeeting.isChecked():
            self.actionmeeting.setChecked(False)
        if self.actioninvest.isChecked():
            self.actioninvest.setChecked(False)
        if self.actioninstruct.isChecked():
            self.actioninstruct.setChecked(False)

    def changepasswordshow(self):
        sip.delete(self.widget)
        self.widget = change_password()
        self.setCentralWidget(self.widget)
        if self.actionmeeting.isChecked():
            self.widget.retshow = self.meetingshow
        if self.actioninvest.isChecked():
            self.widget.retshow = self.investshow
        if self.actioninstruct.isChecked():
            self.widget.retshow = self.structshow
        if self.actioninspect.isChecked():
            self.widget.retshow = self.inspectshow

    def inputexcel(self):
        self.widget.storageView.imp_excel_data()

    def outputexcel(self):
        self.widget.storageView.xpt_excel_data()

    def print(self):
        self.widget.storageView.prt_row_data()

    def page_setting(self):
        self.widget.storageView.prt_setup_data()
