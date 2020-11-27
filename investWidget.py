from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from investTableView import InvestTableView

class InvestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.resize(1000, 745)
        self.setWindowTitle("Welcome to use audit investigation record management module")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.storageView = InvestTableView()
        self.layout.addWidget(self.storageView)