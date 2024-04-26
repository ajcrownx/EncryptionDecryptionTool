from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import sys
import os

from Backend.passwordChecker import checkPassword
from Backend.suggestPassword import suggestPassword
from Backend.Encrypt import Encrypt

from uuid import uuid4

class CustomPushButton(QPushButton):
    def __init__(self,parent):
        super().__init__()
        self.setAcceptDrops(True)

        self.Parent = parent

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        # print("Dropped files:", files)
        self.Parent.stackChange("ADDF",files)
        

class AddFileWidget(QWidget):
    def __init__(self,parent) -> None:
        super().__init__()

        self.Parent = parent

        self.thisLayout = QVBoxLayout(self)
        self.contentWidget = QWidget(self)
        self.thisLayout.addWidget(self.contentWidget)
        self.contentLayout = QVBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(0,0,0,0)

        self._buttonStylesheet = """
            QPushButton{
                background-color: #282828;
                border-radius: 10%;
                color: #ffffff;
                font: 700 20px;
                padding-left: 70px;
                
            }
            QPushButton:checked{
                background-color: #161616;
            }

            
        """

        self.setStyleSheet(self._buttonStylesheet)

        self.addButton = CustomPushButton(parent)
        self.addButton.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.addButton.setIcon(QIcon("Assets/SVGS/add-w.svg"))
        self.addButton.setIconSize(QSize(500,500))

        self.addButton.setAcceptDrops(1)

        self.addButton.clicked.connect(self.addFileEvent)
        

        self.contentLayout.addWidget(self.addButton)

    def addFileEvent(self, e):
        # filePath, _ = QFileDialog.getOpenFileName(None,"Select a File",".","All Files (*)")
        # if not filePath: return
        # print(filePath)
        
        #Adding multiple files
        fileNames ,_ = QFileDialog().getOpenFileNames(None,"Select some Files",".")
        self.filesList = []
        for fileName in fileNames:
            if os.path.exists(fileName):
                self.filesList.append(fileName)
        
        #print(self.filesList)
        if len(self.filesList)>0:
            self.Parent.stackChange("ADDF",self.filesList)
    
    # def dragEnterEvent(self, event):
    #     if event.mimeData().hasUrls():
    #         event.accept()
    #     else:
    #         event.ignore()

    # def dropEvent(self, event):
    #     for url in event.mimeData().urls():
    #         print(url.toLocalFile())

class AddMetaDataWidget(QWidget):
    def __init__(self,parent) -> None:
        super().__init__()
        self.Parent = parent
        self.files = []
        self.Encrypt = Encrypt()
        
        self.thisLayout = QVBoxLayout(self)
        self.contentWidget = QWidget(self)
        self.thisLayout.addWidget(self.contentWidget)
        self.contentLayout = QVBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.contentLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

        self._buttonStylesheet = """
            QPushButton{
                background-color: #a438f6;
                border-radius: 20%;
                color: #ffffff;
                font: 700 20px;
                
            }
            QPushButton:checked{
                background-color: #161616;
            }
            QPushButton:hover{
                background-color: #a999f9;
            }

            QPushButton:disabled{
                background-color: #282828;
            }
        """

        self._labelStylesheet = """
            QLabel{
                background-color: #282828;
                border-radius: 20%;
                color: #ffffff;
                font: 700 20px;
            }
            
        """

        self.backButton = QPushButton("BACK")
        self.backButton.setMinimumHeight(50)
        self.backButton.setStyleSheet(self._buttonStylesheet)
        self.backButton.clicked.connect(self.goback)

        self.fileCountLabel = QLabel()
        self.fileCountLabel.setStyleSheet(self._labelStylesheet)
        self.fileCountLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fileCountLabel.setMinimumHeight(40)

        self._passwordlabelStylesheet = """
            QLabel{
                /*background-color: #282828;*/
                border-radius: 20%;
                border:none;
                border-color:#282828;
                border-width:1px;
                color: #ffffff;
                font: 700 20px;
                padding-top: 70px;
            }
            
        """

        self.enterPasswordLabel = QLabel("CREATE PASSWORD")
        self.enterPasswordLabel.setStyleSheet(self._passwordlabelStylesheet)
        self.enterPasswordLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.enterPasswordLabel.setMinimumHeight(70)

        self._inputFieldStylesheet = """
            QLineEdit{
                /*background-color: #282828;*/
                border-radius: 20%;
                border:solid;
                border-color:#282828;
                border-width:1px;
                color: #ffffff;
                font: 700 20px;
                padding-left:10px;
                padding-right:10px;
            }
            
        """

        self.passwordInputWidget = QWidget()
        self.passwordInputLayout = QHBoxLayout(self.passwordInputWidget)
        self.passwordInputLayout.setContentsMargins(0,0,0,0)

        self.passwordInput = QLineEdit()
        self.passwordInput.setMinimumHeight(50)
        self.passwordInput.setPlaceholderText("ENTER PASSWORD HERE")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordInput.setStyleSheet(self._inputFieldStylesheet)
        self.passwordInput.textChanged.connect(self.checkStrength)

        self.passwordStrenthLabel = QLabel()
        self.passwordStrenthLabel.setStyleSheet(
            """
            QLabel{
                border-radius: 20%;
                border:none;
                border-color:#282828;
                border-width:1px;
                color: #ffffff;
                font: 700 20px;
            }
            
        """
        )
        self.passwordStrenthLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passwordStrenthLabel.setMinimumHeight(0)
        self.passwordStrenthLabel.setMaximumHeight(0)
        #self.passwordStrenthLabel.setEnabled(0)
        

        self.passwordViewButton = QPushButton()
        self.passwordViewButton.setIcon(QIcon("Assets/SVGS/eye-slash-w.svg"))
        self.passwordViewButton.setIconSize(QSize(50,50))
        self.passwordViewButton.setCheckable(1)
        self.passwordViewButton.clicked.connect(self.passwordHide)


        self.passwordViewButton.setStyleSheet(
            """
            QPushButton{
                border:none;
            }
            """
        )

        self.passwordInputLayout.addWidget(self.passwordInput)
        self.passwordInputLayout.addWidget(self.passwordViewButton)

        self.suggestPasswordButton = QPushButton('Suggest Password')
        self.suggestPasswordButton.setStyleSheet(self._buttonStylesheet)
        self.suggestPasswordButton.setMinimumHeight(40)
        self.suggestPasswordButton.clicked.connect(self.handlePasswordSuggestion)

        self.submitButton = QPushButton('Encrypt')
        self.submitButton.setStyleSheet(self._buttonStylesheet)
        self.submitButton.setMinimumHeight(40)
        self.submitButton.setEnabled(0)
        self.submitButton.clicked.connect(self.handleSubmit)
        

        self._fileloclabelStylesheet = """
            QLabel{
                /*background-color: #282828;*/
                border-radius: 20%;
                border:none;
                border-color:#282828;
                border-width:1px;
                color: #ffffff;
                font: 700 20px;
                padding-top: 50px;
            }
            
        """

        self.enterFileLocationLabel = QLabel("Enter File Save Name")
        self.enterFileLocationLabel.setStyleSheet(self._fileloclabelStylesheet)
        self.enterFileLocationLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.enterFileLocationLabel.setMinimumHeight(70)

        self.encryptFileLocationInput = QLineEdit()
        self.encryptFileLocationInput.setMinimumHeight(50)
        self.encryptFileLocationInput.setPlaceholderText("Enter File Save Name Here")
        self.encryptFileLocationInput.setStyleSheet(self._inputFieldStylesheet)



        self.contentLayout.addWidget(self.backButton)
        self.contentLayout.addWidget(self.fileCountLabel)
        self.contentLayout.addWidget(self.enterPasswordLabel)
        self.contentLayout.addWidget(self.passwordInputWidget)
        self.contentLayout.addWidget(self.passwordStrenthLabel)
        self.contentLayout.addWidget(self.suggestPasswordButton)
        self.contentLayout.addWidget(self.enterFileLocationLabel)
        self.contentLayout.addWidget(self.encryptFileLocationInput)
        self.contentLayout.addWidget(self.submitButton)
        self.addSpacer()

    def addFileAction(self,data):
        self.files = data
        self.fileCountLabel.setText(f"FILE COUNT: {len(data)}")
        pass
    
    def addSpacer(self):
        spacerItem = QSpacerItem(50,50,vPolicy= QSizePolicy.Expanding)
        self.contentLayout.addSpacerItem(spacerItem)

    def goback(self, e):
        self.Parent.stackedWidget.setCurrentIndex(self.Parent.stackedWidget.currentIndex()-1)
        pass

    def handleSubmit(self, e):
        fileName = self.encryptFileLocationInput.text() if len(self.encryptFileLocationInput.text())>0 else str(uuid4())
        fileLoc = f"./Home/Encrypted/{fileName}.enc"
        if self.Encrypt.encrypt_multiple_files(self.files, fileLoc, self.passwordInput.text().encode()):
            self.Parent.stackChange("ENC1", [])
        else:
            self.Parent.stackChange("ENC0", [])

        pass

    def handlePasswordSuggestion(self, e):
        self.passwordInput.setText(suggestPassword())
        pass

    def passwordHide(self, e):
        if self.passwordViewButton.isChecked():
            self.passwordViewButton.setIcon(QIcon("Assets/SVGS/eye-w.svg"))
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordViewButton.setIcon(QIcon("Assets/SVGS/eye-slash-w.svg"))
            self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)
    
    def checkStrength(self, e):
        if len(e)>0:
            #self.passwordStrenthLabel.setEnabled(1)
            self.passwordStrenthLabel.setText(checkPassword(e))
            self.passwordStrenthLabel.setMaximumHeight(1000)
            self.passwordStrenthLabel.setMinimumHeight(70)
        else:
            
            self.passwordStrenthLabel.setText("")
            self.passwordStrenthLabel.setMaximumHeight(0)
            self.passwordStrenthLabel.setMinimumHeight(0)
            
            #self.passwordStrenthLabel.setDisabled(1)

        if checkPassword(e) == "Strong Password":
            self.submitButton.setEnabled(1)
        else:
            self.submitButton.setEnabled(0)

class EncryptionCompletedWidget(QWidget):
    def __init__(self,parent) -> None:
        super().__init__()
        self.Parent = parent
        
        
        self.thisLayout = QVBoxLayout(self)
        self.contentWidget = QWidget(self)
        self.thisLayout.addWidget(self.contentWidget)
        self.contentLayout = QVBoxLayout(self.contentWidget)
        self.contentLayout.setContentsMargins(0,0,0,0)

        topSpacer = QSpacerItem(20,20,vPolicy=QSizePolicy.Policy.Expanding)
        bottomSpacer = QSpacerItem(20,20,vPolicy=QSizePolicy.Policy.Expanding)

        self.label = QLabel()
        self.label.setStyleSheet(
            """
            QLabel{
                border-radius: 20%;
                border:none;
                border-color:#282828;
                border-width:1px;
                color: #ffffff;
                font: 700 40px;
            }
            
        """
        )
        self.label.setMinimumHeight(100)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._buttonStylesheet = """
            QPushButton{
                background-color: #a438f6;
                border-radius: 20%;
                color: #ffffff;
                font: 700 20px;
                
            }
            QPushButton:checked{
                background-color: #161616;
            }
            QPushButton:hover{
                background-color: #a999f9;
            }

            QPushButton:disabled{
                background-color: #282828;
            }
        """

        self.backHomeButton = QPushButton("BACK")
        self.backHomeButton.setMinimumHeight(50)
        self.backHomeButton.setStyleSheet(self._buttonStylesheet)
        self.backHomeButton.clicked.connect(self.goback)

        self.contentLayout.addWidget(self.label)
        self.contentLayout.addWidget(self.backHomeButton)

    def displayStatus(self, i:int):
        if i:
            self.label.setText("Encryption Was Succesful!")
        else:
            self.label.setText("Encryption Was Not Succesful!!!")
        pass

    def goback(self):
        self.Parent.stackedWidget.setCurrentIndex(0)
        pass

class EncryptPage(QWidget):
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

        self.tempLabel = QLabel("ENCRYPT")
        self.tempLabel.setStyleSheet(self._labelStyleSheet)

        self.contentLayout.addWidget(self.tempLabel)

        self._stackedWidgetStyleSheet = """
            QStackedWidget{
                background-color:#161616;
                color: #ffffff;
                font: 700 36px;
                
                /*border:solid;
                border-width: 1px;
                border-color: #282828;*/
            }
        """
        

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setMinimumSize(600,600)
        self.stackedWidget.setStyleSheet(self._stackedWidgetStyleSheet)
        self.contentLayout.addWidget(self.stackedWidget)


        self.addFileWidget = AddFileWidget(parent=self)
        self.addMetadataWidget = AddMetaDataWidget(parent=self)
        self.encryptionCompletedWidget = EncryptionCompletedWidget(parent=self)

        self.stackedWidget.addWidget(self.addFileWidget)
        self.stackedWidget.addWidget(self.addMetadataWidget)
        self.stackedWidget.addWidget(self.encryptionCompletedWidget)

        #self.currentStackIndex = 0

    def stackChange(self, type, data):
        #self.currentStackIndex+=1

        if type!="HOME":
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)

        if type=="ADDF":
            self.stackedWidget.currentWidget().addFileAction(data)

        elif type=="ENC0":
            self.stackedWidget.currentWidget().displayStatus(0)
        
        elif type=="ENC1":
            self.stackedWidget.currentWidget().displayStatus(1)

