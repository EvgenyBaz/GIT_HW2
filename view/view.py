# pyuic6 MainGuiWindow.ui -o MainGuiWindow.py

from PyQt6 import QtGui
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton
import sys
from PyQt6 import QtWidgets, uic
from MainGuiWindow import Ui_MainWindow
from RusCorpsGuiWindow import Ui_RusCorpsWindow

class MainGuiWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainGuiWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


class RusCorpsWindow(QtWidgets.QMainWindow, Ui_RusCorpsWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(RusCorpsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def show_MainWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.pushButton_Russia.clicked.connect(self.show_RusCorpsWindow) # по нажатию кнопки включаем окно с описанием корпуса русской армии
        self.mainWindow.pushButton_Russia.clicked.connect(self.mainWindow.close) # выключаем текущее окно

        self.mainWindow.pushButton_France.clicked.connect(self.the_fra_button_was_clicked) # заглушка

        self.mainWindow.show()

    def show_RusCorpsWindow(self):
        self.rusCorpsWindow = RusCorpsWindow()
        self.rusCorpsWindow.show()

    def the_fra_button_was_clicked(self): # заглушка
        print("fra_clicked")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show_MainWindow()
app.exec()
