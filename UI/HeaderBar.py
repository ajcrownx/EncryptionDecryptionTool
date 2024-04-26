from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys


class HeaderBar(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setMinimumHeight(100)
        self.setMaximumHeight(100)
        self.setMinimumWidth(600)
        
        self._labelStyleSheet = """
            QLabel{
                background-color:#161616;
                color: #ffffff;
                font: 700 36px;
                padding-left:100px;
                border:solid;
                border-width: 1px;
                border-color: #282828;
            }
        """

        self.HeaderNameLabel = QLabel("ENKRYPTOR")
        self.HeaderNameLabel.setStyleSheet(self._labelStyleSheet)

        self.headerLayout = QHBoxLayout(self)
        self.headerLayout.setContentsMargins(0,0,0,0)
        self.headerLayout.addWidget(self.HeaderNameLabel)