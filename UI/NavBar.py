from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys

from UI.Content import Content
from UI.NavButton import NavButton


class NavBar(QWidget):
    def __init__(self,content:Content) -> None:
        super().__init__()
        self.contentWidget = content

        self.setMinimumWidth(300)
        self.setMaximumWidth(300)
        self.setMinimumHeight(700)
        

        self._stylesheet = """
            QWidget{
                background-color:#282828;
                border-width: 1px;
                border-color: #ffffff;
            }
        """

        self.setStyleSheet(self._stylesheet)

        self._labelStyleSheet = """
            QLabel{
                /*background-color:#161616;*/
                color: #ffffff;
                font: 700 26px;
                
            }
        """
        self.init()
        self.addSpacer()

    def init(self):
        #LABELS NAMESPACE
        self._NAME = QLabel("ENKRYPT")
        self._NAME.setMaximumHeight(70)
        self._NAME.setMinimumHeight(70)
        self._NAME.setMaximumWidth(300)
        self._NAME.setMinimumWidth(300)
        self._NAME.setStyleSheet(self._labelStyleSheet)
        self._NAME.setAlignment(Qt.AlignCenter)

        self._VERSION = QLabel("v0.0.1b")
        self._VERSION.setMaximumHeight(30)
        self._VERSION.setMinimumHeight(30)
        self._VERSION.setMaximumWidth(300)
        self._VERSION.setMinimumWidth(300)
        self._VERSION.setStyleSheet(self._labelStyleSheet)
        self._VERSION.setAlignment(Qt.AlignCenter)

        ###############
        
        # self.navLayout = QVBoxLayout(self)
        # self.navLayout.setContentsMargins(0,0,0,0)
        # self.navLayout.setSpacing(0)

        self.thisLayout = QVBoxLayout(self)
        self.thisLayout.setContentsMargins(0,0,0,0)
        self.thisWidget = QWidget(self)
        self.thisLayout.addWidget(self.thisWidget)
        self.navLayout = QVBoxLayout(self.thisWidget)
        self.navLayout.setContentsMargins(0,0,0,0)
        self.navLayout.setSpacing(0)

        self.navLayout.addWidget(self._NAME)
        self.navLayout.addWidget(self._VERSION)

        self.addNavigation()

    def addNavigation(self):
        self.NAVTABS = QWidget()
        self.navLayout.addWidget(self.NAVTABS)
        
        self.navTabLayout = QVBoxLayout(self.NAVTABS)
        self.navTabLayout.setContentsMargins(20,50,0,0)
        self.navTabLayout.setSpacing(5)

        self.NAVTABS.setMinimumHeight(400)
        self.NAVTABS.setSizePolicy(QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Maximum)
        self.NAVTABS.setMinimumWidth(300)



        ##NAV_BUTTONS##

        self.HomeButton = NavButton("Home",self)
        homeicon = QIcon("Assets/SVGS/home-w.svg")
        self.HomeButton.setIcon(homeicon)
        self.HomeButton.setIconSize(QSize(30,30))

        self.EncryptButton = NavButton("Encrypt",self)
        encypticon = QIcon("Assets/SVGS/security-padlock-w.svg")
        self.EncryptButton.setIcon(encypticon)
        self.EncryptButton.setIconSize(QSize(30,30))

        self.DecryptButton = NavButton("Decrypt",self)
        decypticon = QIcon("Assets/SVGS/unlock-w.svg")
        self.DecryptButton.setIcon(decypticon)
        self.DecryptButton.setIconSize(QSize(30,30))

        self.AboutButton = NavButton("About",self)
        abouticon = QIcon("Assets/SVGS/about-w.svg")
        self.AboutButton.setIcon(abouticon)
        self.AboutButton.setIconSize(QSize(30,30))

        #self.navTabLayout.addWidget(self.HomeButton)
        self.navTabLayout.addWidget(self.EncryptButton)
        self.navTabLayout.addWidget(self.DecryptButton)
        self.navTabLayout.addWidget(self.AboutButton)

        self.navButtonList = [self.EncryptButton,self.DecryptButton,self.AboutButton]
        [j.setIndex(i) for i,j in enumerate(self.navButtonList)]

        self.navButtonList[0].setCheckable(1)
        self.navButtonList[0].setChecked(1)
        self.navButtonList[0].setDisabled(1)
        self.currentTab = 0

        ################    

    def addSpacer(self):
        self.spacer1 = QSpacerItem(20, 50, vPolicy=QSizePolicy.Policy.Expanding)
        self.spacer2 = QSpacerItem(20, 50, vPolicy=QSizePolicy.Policy.Expanding)

        #horizontalLine = QFrame.
        self.navLayout.addSpacerItem(self.spacer1)
        self.navTabLayout.addSpacerItem(self.spacer2)

        # self.SettingButton = NavButton("Settings",self)
        # settingsIcon = QIcon("Assets/SVGS/about-w.svg")
        # self.SettingButton.setIcon(settingsIcon)
        # self.SettingButton.setIconSize(QSize(30,30))
        # self.navTabLayout.addWidget(self.SettingButton)


        pass


    
    def navButtonEvent(self,index):
        #print(index)
        self.navButtonList[self.currentTab].setCheckable(0)
        self.navButtonList[self.currentTab].setChecked(0)
        self.navButtonList[self.currentTab].setDisabled(0)

        self.navButtonList[index].setCheckable(1)
        self.navButtonList[index].setChecked(1)
        self.navButtonList[index].setDisabled(1)

        self.currentTab = index

        self.contentWidget.changePage(index)
        
        pass
    