# pyuic6 StartGuiWindow.ui -o StartGuiWindow.py
# pyuic6 RusCorpsGuiWindow.ui -o RusCorpsGuiWindow.py
# pyuic6 LineInfantryBonusGuiWindow.ui -o LineInfantryBonusGuiWindow.py

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
        self.startWindow.setWindowTitle("Black Powder 2.0 Army Builder")

        self.startWindow.pushButton_Russia.clicked.connect(self.show_RusCorpsWindow) # по нажатию кнопки включаем окно с описанием корпуса русской армии
        self.startWindow.pushButton_Russia.clicked.connect(self.startWindow.close) # выключаем текущее окно
        self.startWindow.pushButton_France.clicked.connect(self.the_fra_button_was_clicked) # заглушка
        self.startWindow.show()


    def show_RusCorpsWindow(self):
        self.rusCorpsWindow = RusCorpsWindow()
        self.rusCorpsWindow.setWindowTitle("Black Powder 2.0 Army Builder")

        self.rusCorpsWindow.a_brigade_bttln_Lists()

        self.rusCorpsWindow.show()


    def the_fra_button_was_clicked(self): # заглушка
        print("fra_clicked")




app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show_StartWindow()
app.exec()
