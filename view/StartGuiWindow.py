# Form implementation generated from reading ui file 'StartGuiWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Russia = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Russia.setGeometry(QtCore.QRect(260, 200, 271, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Russia.setFont(font)
        self.pushButton_Russia.setObjectName("pushButton_Russia")
        self.pushButton_France = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_France.setGeometry(QtCore.QRect(260, 240, 271, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_France.setFont(font)
        self.pushButton_France.setObjectName("pushButton_France")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 731, 161))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuT = QtWidgets.QMenu(parent=self.menubar)
        self.menuT.setObjectName("menuT")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionLoad = QtGui.QAction(parent=MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuT.addAction(self.actionLoad)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuT.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Russia.setText(_translate("MainWindow", "Russia"))
        self.pushButton_France.setText(_translate("MainWindow", "France"))
        self.label.setText(_translate("MainWindow", "Welcome to the Black Powder 2.0 army list builder.\n"
" Napoleonic Wars\n"
"\n"
"Choose the side!"))
        self.menuT.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionAbout.setText(_translate("MainWindow", "About"))