from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from UI.mainWidget import MainWidget

import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        self.setWindowTitle("Enkryptor v0.0.1b (BETA_BUILD_ID:0011504)")

        self.setMinimumSize(1300,800)
        self.setContentsMargins(0,0,0,0)

        self.init()
        self.show()

    def init(self):
        self.mainLayout=QHBoxLayout(self.widget)
        self.mainLayout.setContentsMargins(0,0,0,0)

        self.mainWidget = MainWidget()

        self.mainLayout.addWidget(self.mainWidget)


        self._stylesheet = """
            QWidget{
                background-color:#161616;
                border-width: 10px;
            }
        """

        self.setStyleSheet(self._stylesheet)




app = QApplication(sys.argv)
win = MainWindow()
#win.client.destroy()
sys.exit(app.exec_())