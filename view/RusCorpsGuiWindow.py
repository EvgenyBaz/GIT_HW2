# Form implementation generated from reading ui file 'RusCorpsGuiWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RusCorpsWindow(object):
    def setupUi(self, RusCorpsWindow):
        RusCorpsWindow.setObjectName("RusCorpsWindow")
        RusCorpsWindow.resize(1780, 600)
        self.centralwidget = QtWidgets.QWidget(parent=RusCorpsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 191, 41))
        self.label.setObjectName("label")
        self.firstBatallion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.firstBatallion.setGeometry(QtCore.QRect(70, 110, 191, 22))
        self.firstBatallion.setObjectName("firstBatallion")

        self.secondfirstBatallion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.secondfirstBatallion.setGeometry(QtCore.QRect(70, 130, 191, 22))
        self.secondfirstBatallion.setObjectName("secondfirstBatallion")

        self.thirdBatallion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.thirdBatallion.setGeometry(QtCore.QRect(70, 150, 191, 22))
        self.thirdBatallion.setObjectName("thirdBatallion")

        self.fourthBatallion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.fourthBatallion.setGeometry(QtCore.QRect(70, 170, 191, 22))
        self.fourthBatallion.setObjectName("fourthBatallion")
        self.additionalfirstBatallion = QtWidgets.QComboBox(parent=self.centralwidget)
        self.additionalfirstBatallion.setGeometry(QtCore.QRect(70, 200, 191, 22))
        self.additionalfirstBatallion.setObjectName("additionalfirstBatallion")
        self.mainTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(670, 0, 341, 41))
        self.mainTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainTitle.setObjectName("mainTitle")
        RusCorpsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RusCorpsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1780, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        RusCorpsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RusCorpsWindow)
        self.statusbar.setObjectName("statusbar")
        RusCorpsWindow.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(parent=RusCorpsWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RusCorpsWindow)
        QtCore.QMetaObject.connectSlotsByName(RusCorpsWindow)

    def retranslateUi(self, RusCorpsWindow):
        _translate = QtCore.QCoreApplication.translate
        RusCorpsWindow.setWindowTitle(_translate("RusCorpsWindow", "MainWindow"))
        self.label.setText(_translate("RusCorpsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Line Infantry brigade</span></p></body></html>"))
        self.mainTitle.setText(_translate("RusCorpsWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Imperial Russian Army Corps</span></p></body></html>"))
        self.menuFile.setTitle(_translate("RusCorpsWindow", "File"))
        self.menuHelp.setTitle(_translate("RusCorpsWindow", "Help"))
        self.actionSave.setText(_translate("RusCorpsWindow", "Save"))
