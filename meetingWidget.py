from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from meetingTableView import MeetingTableView

class MeetingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.resize(1000, 745)
        self.setWindowTitle("Welcome to use the rectification inspection management module")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.storageView = MeetingTableView()
        self.layout.addWidget(self.storageView)