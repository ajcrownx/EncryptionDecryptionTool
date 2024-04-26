from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys

from UI.Pages import *

from UI import *


class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self._stylesheet = """
            QWidget{
                background-color:#161616;
                
            }
        """

        self.setStyleSheet(self._stylesheet)

        self.mainwidgetlayout = QHBoxLayout(self)
        self.mainwidgetlayout.setContentsMargins(0,0,0,0)
        self.MainContent = QWidget(self)
        self.mainwidgetlayout.addWidget(self.MainContent)

        self.mainLayout = QHBoxLayout(self.MainContent)


        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)

        self.content = Content()
        self.navBar = NavBar(self.content)

        self.mainLayout.addWidget(self.navBar)
        self.mainLayout.addWidget(self.content)






if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWidget()
    #win.client.destroy()
    sys.exit(app.exec_())