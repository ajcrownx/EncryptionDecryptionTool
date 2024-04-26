from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys


class NavButton(QPushButton):
    def __init__(self,text:str,parent,index:int=None):
        super().__init__()
        self.Parent = parent
        self.index = index
        
        text="    "+text
        self.setText(text)
        self.setMinimumWidth(200)
        self.setMinimumHeight(70)

        self.clicked.connect(self.onClick)
        #self.setCheckable(1)
        
        self._buttonStylesheet = """
            QPushButton{
                background-color: #282828;
                /*border-radius: 25px;*/
                border-bottom-left-radius: 25px;
                border-top-left-radius: 25px;
                color: #ffffff;
                font: 700 20px;
                text-align: left;
                padding-left: 70px;
                
            }
            QPushButton:checked{
                background-color: #161616;
            }
        """

        self.setStyleSheet(self._buttonStylesheet)

    def setIndex(self,index):
        self.index=index
        
    def onClick(self):
        self.Parent.navButtonEvent(self.index)
        pass
