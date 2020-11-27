from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from inspectTableView import InspectTableView

class InspectWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.resize(1000, 745)
        self.setWindowTitle("Inspection management module")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.storageView = InspectTableView()
        self.layout.addWidget(self.storageView)