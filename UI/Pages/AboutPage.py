from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys

class AboutBox(QWidget):
    def __init__(self,UID:str,NAME:str,ROLE:str=None) -> None:
        super().__init__()

        self.Layout = QVBoxLayout(self)
        
        self.content = QWidget()
        self.content.setMinimumSize(300,250)
        self.content.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.Layout.addWidget(self.content)
        self.boxLayout = QVBoxLayout(self.content)

        self._kustomStylesheet = """
            QWidget{
                background-color: #a938f6;
                color: #ffffff;
                border-radius: 50%;
            }
            QLabel{
                /*background-color: #9f9f9f;*/
                
                color: #ffffff;
                border-radius: 23%;
                font: 600 24px;
            }
            
        """

        self.setStyleSheet(self._kustomStylesheet)

        self.UID = QLabel("<font color='black'>UID:</font> \n"+UID)
        self.NAME = QLabel("<font color='black'>NAME:</font> \n"+NAME)
        self.ROLE = QLabel("<font color='black'>ROLE:</font> \n"+ROLE)
        
        self.topSpacer = QSpacerItem(2,2, vPolicy=QSizePolicy.Policy.Expanding)
        self.bottomSpacer = QSpacerItem(2,2, vPolicy=QSizePolicy.Policy.Expanding)

        self.ABOUTDATA = [self.UID,self.NAME,self.ROLE]

        for i in self.ABOUTDATA:
            i.setAlignment(Qt.AlignmentFlag.AlignCenter)
            i.setMinimumHeight(50)
            i.setWordWrap(1)

        self.boxLayout.addSpacerItem(self.topSpacer)
        self.boxLayout.addWidget(self.UID)
        self.boxLayout.addWidget(self.NAME)
        self.boxLayout.addWidget(self.ROLE)
        self.boxLayout.addSpacerItem(self.bottomSpacer)
        
class AboutPage(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.thisLayout = QVBoxLayout(self)

        self.contentWidget = QWidget(self)

        self.thisLayout.addWidget(self.contentWidget)

        self.contentLayout = QGridLayout(self.contentWidget)
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

        self.tempLabel = QLabel("ABOUT")
        self.tempLabel.setStyleSheet(self._labelStyleSheet)

        self.contentLayout.addWidget(self.tempLabel)

        self.aboutBox1 = AboutBox("22BDA70073","Ishan Srivastav", "Backend UI Integration and Researcher.")
        self.aboutBox2 = AboutBox("22BDA70093","Priyanshu Kumar Singh", "UI Design (PyQt) and Documentation.")
        self.aboutBox3 = AboutBox("22BDA70117","Aditya Jaswal", "Encryption Decryption Backend Design and Presentation.")

        bottomSpacer1 = QSpacerItem(50,50, vPolicy=QSizePolicy.Policy.Expanding)

        self.contentLayout.addWidget(self.aboutBox1,1,0)
        self.contentLayout.addWidget(self.aboutBox2,1,1)
        self.contentLayout.addWidget(self.aboutBox3,1,2)
        
        self.thisLayout.addSpacerItem(bottomSpacer1)

    def init(self):
        pass

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     self.adjustButtonSizes()

    # def adjustButtonSizes(self):
    #     # Calculate the size of each button based on the current window size
    #     button_width = (self.width() - (self.contentLayout.horizontalSpacing() * (self.contentLayout.columnCount() - 1))) / self.contentLayout.columnCount()
    #     button_height = (self.height() - (self.contentLayout.verticalSpacing() * (self.contentLayout.rowCount() - 1))) / self.contentLayout.rowCount()

    #     # Iterate through buttons and set their size
    #     for i in range(self.contentLayout.rowCount()):
    #         for j in range(self.contentLayout.columnCount()):
    #             try:
    #                 button = self.contentLayout.itemAtPosition(i, j).widget()
    #                 button.setMinimumSize(int(button_width), int(button_height))
    #                 button.setMaximumSize(int(button_width), int(button_height))
    #             except:pass

