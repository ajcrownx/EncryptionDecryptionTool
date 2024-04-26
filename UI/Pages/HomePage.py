from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys


class HomePage(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.thisLayout = QVBoxLayout(self)

        self.contentWidget = QWidget(self)

        self.thisLayout.addWidget(self.contentWidget)

        self.contentLayout = QVBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(0,0,0,0)

        self._labelStyleSheet = """
            QLabel{
                background-color:#161616;
                color: #ffffff;
                font: 700 36px;
                
                /*border:solid;
                border-width: 1px;
                border-color: #282828;*/
            }
        """

        self.tempLabel = QLabel("HOME")
        self.tempLabel.setStyleSheet(self._labelStyleSheet)

        self.contentLayout.addWidget(self.tempLabel)

        

    def init(self):
        pass
