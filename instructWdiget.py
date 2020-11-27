import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from instructTableView import InstructTableView


class InstructWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.resize(1000, 745)
        self.setWindowTitle("Welcome to use the rectification suggestion management module")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.storageView = InstructTableView()
        self.layout.addWidget(self.storageView)
