# pyuic6 StartGuiWindow.ui -o StartGuiWindow.py

from PyQt6 import QtGui
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt6 import QtWidgets, uic


# from StartWindow import StartWindow
# from RusCorpsWindow import RusCorpsWindow
from view.StartWindow import StartWindow
from view.RusCorpsWindow import RusCorpsWindow

class MainWindow(QMainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.setupUi(self)


    def show_StartWindow(self):
        self.startWindow = StartWindow()
        self.startWindow.pushButton_Russia.clicked.connect(self.show_RusCorpsWindow) # по нажатию кнопки включаем окно с описанием корпуса русской армии
        self.startWindow.pushButton_Russia.clicked.connect(self.startWindow.close) # выключаем текущее окно
        self.startWindow.pushButton_France.clicked.connect(self.the_fra_button_was_clicked) # заглушка
        self.startWindow.show()

    def show_RusCorpsWindow(self):
        self.rusCorpsWindow = RusCorpsWindow()

        self.rusCorpsWindow.brigadeLists()
        self.rusCorpsWindow.brigadeAdditionalList()

        self.rusCorpsWindow.show()


    def the_fra_button_was_clicked(self): # заглушка
        print("fra_clicked")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show_StartWindow()
app.exec()
