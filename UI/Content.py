from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys

from UI.HeaderBar import HeaderBar
from UI.Pages import *


class Content(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.Header = HeaderBar()


        self.thisLayout = QVBoxLayout(self)
        self.thisLayout.setContentsMargins(0,0,0,0)

        self.contentWidget = QWidget(self)
        self.thisLayout.addWidget(self.contentWidget)
        self.contentLayout = QVBoxLayout(self.contentWidget)
        
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.contentLayout.setSpacing(0)

        self.init()
        self.addSpacer()

    def init(self):
        self.contentLayout.addWidget(self.Header)
        
        # self.contentWidget.setMinimumWidth(600)
        # self.contentWidget.setMinimumHeight(700)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setMinimumWidth(600)
        self.stackedWidget.setMinimumHeight(700)
        self.stackedWidget.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)

        self.contentLayout.addWidget(self.stackedWidget)

        self.homePage = HomePage()
        self.encryptPage = EncryptPage()
        self.decryptPage = DecryptPage()
        self.aboutPage = AboutPage()

        #self.stackedWidget.addWidget(self.homePage)
        self.stackedWidget.addWidget(self.encryptPage)
        self.stackedWidget.addWidget(self.decryptPage)
        self.stackedWidget.addWidget(self.aboutPage)


    def addSpacer(self):
        self.spacer = QSpacerItem(20,50,vPolicy=QSizePolicy.Policy.Expanding)
        #self.contentLayout.addSpacerItem(self.spacer)
        pass

    def changePage(self,index):
        self.stackedWidget.setCurrentIndex(index)
        pass

